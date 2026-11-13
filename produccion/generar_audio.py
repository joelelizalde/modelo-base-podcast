#!/usr/bin/env python3
"""Genera los episodios de Modelo Base a partir de los guiones en Markdown.

Uso:
    python generar_audio.py                 # todos los guiones
    python generar_audio.py 00 01           # solo los que empiezan por 00, 01

Requiere: edge-tts, ffmpeg.
"""

import asyncio
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
GUIONES = ROOT / "guiones"
AUDIO = ROOT / "audio"
CACHE = ROOT / "produccion" / "cache"
TMP = ROOT / "produccion" / "tmp"

VOICES = {
    "ANA": ("es-MX-DaliaNeural", "+2%"),
    "JOEL": ("es-MX-JorgeNeural", "-2%"),
}

PAUSA_TURNO = 0.28
PAUSA_SECCION = 0.60
SR = 48000


def find_ffmpeg() -> str:
    local = ROOT / "produccion" / "bin" / "ffmpeg"
    if local.exists():
        return str(local)
    found = shutil.which("ffmpeg")
    if found:
        return found
    raise SystemExit("No encuentro ffmpeg. Instálalo o deja el binario en produccion/bin/ffmpeg")


FFMPEG = find_ffmpeg()


def run(args, **kw):
    return subprocess.run(args, check=True, capture_output=True, text=True, **kw)


def parse(path: Path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^## (.+)$", text, re.M)
    title = title.group(1).strip() if title else path.stem
    turns = []
    current = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            current = None
            continue
        m = re.match(r"^\*\*(ANA|JOEL):\*\*\s*(.*)$", line)
        if m:
            current = [m.group(1), m.group(2).strip()]
            turns.append(current)
        elif current is not None:
            current[1] += " " + line
    return title, [(s, t) for s, t in turns if t]


def sha(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:16]


async def synth(text, voice, rate, out: Path):
    for attempt in range(3):
        try:
            com = edge_tts.Communicate(text, voice, rate=rate)
            await com.save(str(out))
            if out.exists() and out.stat().st_size > 1000:
                return
        except Exception as exc:  # noqa: BLE001
            if attempt == 2:
                raise
            await asyncio.sleep(1.5 * (attempt + 1))


def to_wav(src: Path, dst: Path):
    run([FFMPEG, "-y", "-v", "error", "-i", str(src),
         "-ar", str(SR), "-ac", "1", str(dst)])


def silence(duration: float, dst: Path):
    run([FFMPEG, "-y", "-v", "error", "-f", "lavfi",
         "-i", f"anullsrc=r={SR}:cl=mono", "-t", f"{duration}",
         str(dst)])


def ensure_sting(dst: Path):
    if dst.exists():
        return
    # Acorde suave en La menor add9, con caída larga.
    tones = [220.00, 261.63, 329.63, 493.88]
    inputs = []
    for f in tones:
        inputs += ["-f", "lavfi", "-i", f"sine=frequency={f}:duration=5:sample_rate={SR}"]
    filt = "".join(
        f"[{i}]volume=0.18,afade=t=in:st=0:d=0.02,afade=t=out:st=0.6:d=4.2[a{i}];"
        for i in range(len(tones))
    )
    filt += "".join(f"[a{i}]" for i in range(len(tones)))
    filt += f"amix=inputs={len(tones)}:normalize=0,aecho=0.8:0.9:60|120:0.25|0.15,lowpass=f=2800,volume=1.6[out]"
    run([FFMPEG, "-y", "-v", "error", *inputs, "-filter_complex", filt,
         "-map", "[out]", "-t", "5", str(dst)])


def duration(path: Path) -> float:
    out = run([FFMPEG.replace("ffmpeg", "ffprobe"), "-v", "error",
               "-show_entries", "format=duration", "-of",
               "default=nw=1:nk=1", str(path)]).stdout.strip()
    try:
        return float(out)
    except ValueError:
        return 0.0


async def build(path: Path):
    title, turns = parse(path)
    print(f"\n== {title} ({len(turns)} turnos)")

    CACHE.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    AUDIO.mkdir(parents=True, exist_ok=True)

    sem = asyncio.Semaphore(4)

    async def one(idx, speaker, text):
        voice, rate = VOICES[speaker]
        key = sha(f"{voice}|{rate}|{text}")
        mp3 = CACHE / f"{key}.mp3"
        if not mp3.exists():
            async with sem:
                await synth(text, voice, rate, mp3)
        wav = TMP / f"{path.stem}_{idx:03d}.wav"
        to_wav(mp3, wav)
        return wav

    tasks = [one(i, s, t) for i, (s, t) in enumerate(turns)]
    wavs = []
    for i, task in enumerate(asyncio.as_completed(tasks)):
        wavs.append(await task)
        if (i + 1) % 10 == 0 or i + 1 == len(tasks):
            print(f"   {i + 1}/{len(tasks)}")

    # Reordenar: as_completed altera el orden.
    ordered = [TMP / f"{path.stem}_{i:03d}.wav" for i in range(len(turns))]

    gap = TMP / "gap.wav"
    silence(PAUSA_TURNO, gap)
    sting = TMP / "sting.wav"
    ensure_sting(sting)
    gap_long = TMP / "gap_long.wav"
    silence(PAUSA_SECCION, gap_long)

    lista = TMP / f"{path.stem}.txt"
    with lista.open("w", encoding="utf-8") as f:
        f.write(f"file '{sting}'\n")
        f.write(f"file '{gap_long}'\n")
        for i, w in enumerate(ordered):
            f.write(f"file '{w}'\n")
            if i < len(ordered) - 1:
                f.write(f"file '{gap}'\n")
        f.write(f"file '{gap_long}'\n")
        f.write(f"file '{sting}'\n")

    out = AUDIO / f"{path.stem}.mp3"
    run([FFMPEG, "-y", "-v", "error", "-f", "concat", "-safe", "0",
         "-i", str(lista),
         "-af", "loudnorm=I=-16:TP=-1:LRA=11",
         "-ar", "44100", "-ac", "2", "-b:a", "192k", str(out)])

    d = duration(out)
    print(f"   -> {out.name}  {int(d // 60)}:{int(d % 60):02d}")
    return out, d


async def main():
    wanted = sys.argv[1:]
    files = sorted(GUIONES.glob("*.md"))
    if wanted:
        files = [f for f in files if any(f.name.startswith(w) for w in wanted)]
    if not files:
        raise SystemExit("No hay guiones que coincidan.")
    total = 0.0
    for f in files:
        _, d = await build(f)
        total += d
    print(f"\nTotal: {int(total // 60)} min {int(total % 60)} s en {len(files)} archivos")


if __name__ == "__main__":
    asyncio.run(main())
