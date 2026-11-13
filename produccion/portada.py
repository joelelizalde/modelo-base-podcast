#!/usr/bin/env python3
"""Genera la portada 3000x3000 de Modelo Base."""

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONTS = Path("/mnt/c/Users/Joel/Downloads/IA/ai-engineering-esencial/assets/fonts")
OUT = ROOT / "portada"
S = 3000

CREAM = "#F5F1E8"
INK = "#18140F"
VERMILION = "#C9481B"
TEAL = "#0D6A61"


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (S, S), CREAM)
    d = ImageDraw.Draw(img)

    # Marco editorial
    d.rectangle([90, 90, S - 90, S - 90], outline=INK, width=5)
    d.rectangle([120, 120, S - 120, S - 120], outline=INK, width=1)

    fraunces = font("Fraunces-700.ttf", 400)
    fraunces_s = font("Fraunces-500.ttf", 150)
    inter = font("Inter-500.ttf", 78)
    inter_s = font("Inter-400.ttf", 62)
    inter_xs = font("Inter-500.ttf", 52)

    # Etiqueta superior
    d.text((S / 2, 250), "T E M P O R A D A   1", font=inter_xs, fill=INK, anchor="mm")

    # Título en dos líneas
    d.text((S / 2, 780), "MODELO", font=fraunces, fill=INK, anchor="mm")
    d.text((S / 2, 1190), "BASE", font=fraunces, fill=VERMILION, anchor="mm")

    # Regla
    d.line([(900, 1450), (2100, 1450)], fill=INK, width=4)

    # Subtítulo
    d.text((S / 2, 1585), "Ingeniería de IA,", font=fraunces_s, fill=INK, anchor="mm")
    d.text((S / 2, 1755), "de la demo a producción", font=fraunces_s, fill=INK, anchor="mm")

    # Onda de audio
    random.seed(7)
    bars = 34
    width = 26
    gap = 30
    total = bars * width + (bars - 1) * gap
    x0 = (S - total) / 2
    base = 2150
    for i in range(bars):
        h = random.choice([40, 60, 90, 130, 170, 220, 280, 340, 400])
        if 12 <= i <= 21:
            h = int(h * 1.25)
        x = x0 + i * (width + gap)
        d.rounded_rectangle([x, base - h / 2, x + width, base + h / 2],
                            radius=width / 2, fill=VERMILION if 10 <= i <= 23 else INK)

    # Nombres
    d.text((S / 2, 2490), "ANA  ·  JOEL", font=inter, fill=INK, anchor="mm")

    # Pie
    d.text((S / 2, 2680), "AI ENGINEERING · EDICIÓN ESENCIAL", font=inter_xs, fill=TEAL, anchor="mm")
    d.text((S / 2, 2760), "2026 · ESPAÑOL", font=inter_xs, fill=INK, anchor="mm")

    png = OUT / "modelo-base-portada.png"
    jpg = OUT / "modelo-base-portada.jpg"
    img.save(png)
    img.save(jpg, quality=92, subsampling=0)
    print(png, png.stat().st_size // 1024, "KB")
    print(jpg, jpg.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
