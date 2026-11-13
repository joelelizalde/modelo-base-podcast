# Modelo Base · Podcast

Podcast de ingeniería de IA en español mexicano. Dos voces, 10 episodios de temporada, tráiler y cierre.

**Nombre:** Modelo Base
**Subtítulo:** Ingeniería de IA, de la demo a producción
**Web del curso:** https://joelelizalde.github.io/ai-engineering-edicion-esencial/

---

## Qué hay aquí

```
biblia-del-podcast.md          Formato, voces, tono y reglas de escritura
guiones/                       12 guiones con turnos de Ana y Joel
  00-trailer.md
  01-...md … 10-...md
  11-cierre.md
audio/                         MP3 finales, −16 LUFS, 44.1 kHz, 192 kbps
portada/                       Portada 3000 × 3000 (PNG y JPG)
distribucion/kit-spotify.md    Ficha, descripciones y pasos de publicación
produccion/generar_audio.py    Guion → audio con edge-tts + ffmpeg
produccion/portada.py          Genera la portada con Pillow
produccion/bin/ffmpeg          ffmpeg estático para Linux x86_64 (no se versiona)
```

`.gitignore` excluye `produccion/bin/`, `produccion/cache/` y `produccion/tmp/`:
los binarios pesan 169 MB cada uno y GitHub rechaza archivos de más de 100 MB.

---

## Voces

| Personaje | Voz | Rol |
|---|---|---|
| Ana | `es-MX-DaliaNeural` | Producto, escepticismo, preguntas incómodas |
| Joel | `es-MX-JorgeNeural` | Ingeniería, ejemplos, matices |

Son voces sintéticas de Microsoft Edge. No se clona ninguna voz real.

---

## Regenerar el audio

Requisitos: Python 3.10+, `edge-tts`, `ffmpeg`.

```bash
cd podcast-ia-esencial
python3 -m venv .venv
source .venv/bin/activate
pip install edge-tts

# todos los episodios
python produccion/generar_audio.py

# solo algunos
python produccion/generar_audio.py 00 01
```

El script usa `produccion/bin/ffmpeg` si existe; si no, busca `ffmpeg` en el PATH.

Cada turno se cachea en `produccion/cache/` por hash de voz y texto. Si cambias una línea, solo se regenera esa línea.

Salida: `audio/<nombre-del-guion>.mp3`.

Ajustes de mezcla en `generar_audio.py`:

- Pausa entre turnos: 280 ms.
- Pausa de sección: 600 ms.
- Sting original de 5 s al inicio y al cierre.
- Normalización: −16 LUFS, pico −1 dB, LRA 11.
- MP3 192 kbps, 44.1 kHz, estéreo.

---

## Regenerar la portada

```bash
python produccion/portada.py
```

Usa las tipografías del curso (Fraunces e Inter) desde
`../ai-engineering-esencial/assets/fonts/`. Si mueves la carpeta, ajusta `FONTS` en el script.

---

## Duraciones

| Episodio | Duración |
|---|---|
| 00 · Tráiler | 1:54 |
| 01 · Tu modelo no es tu producto | 8:47 |
| 02 · Tu modelo no lee palabras | 7:20 |
| 03 · Aprobar no es evaluar | 6:42 |
| 04 · La calidad no es una sola cosa | 6:31 |
| 05 · El prompt es una especificación | 6:10 |
| 06 · Dale un documento | 6:00 |
| 07 · El ajuste fino no es la primera opción | 6:14 |
| 08 · Datos sucios, modelo confiado | 6:02 |
| 09 · La latencia media miente | 6:04 |
| 10 · Lo que no se mide no se mejora | 6:09 |
| 11 · Cinco decisiones y un cierre | 3:52 |

Total: 1 h 11 min.

Los valores exactos están en `audio/`; el generador imprime la duración al terminar.

---

## Publicación

Empieza por `distribucion/kit-spotify.md`. Resumen:

1. Crear el podcast en Spotify for Creators con la ficha y la portada.
2. Subir el tráiler.
3. Programar el episodio 01 un martes a las 09:00 (CDMX).
4. Un episodio por semana.
5. Importar el RSS en Apple Podcasts y YouTube Music.

---

## Criterio editorial

- Ana abre con una objeción; Joel responde con un ejemplo.
- Un solo ejemplo concreto por episodio, antes del minuto 6.
- Nada de «en el mundo actual» ni «la IA está transformando».
- El cierre deja una frase repetible, no un resumen.
- Cada episodio enlaza al módulo correspondiente del curso.

Todo está detallado en `biblia-del-podcast.md`.
