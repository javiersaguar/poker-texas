#!/usr/bin/env python3
"""Genera los iconos de la app (PNG) a partir de las fuentes SVG de esta carpeta.

Uso:  python3 icons/build-icons.py
Requisitos: Pillow y un Chromium/Chrome para rasterizar el SVG.
            (variable de entorno CHROME para indicar la ruta del binario)
"""
import os
import shutil
import subprocess
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FELT = (10, 22, 17)  # #0a1611, el fondo de la app


def spade(cx, cy, h, fill):
    """Pica dibujada en una caja de 100x100 y escalada a la altura `h`."""
    s = h / 80.0
    d = ("M50 10 C50 10 84 38 84 58 C84 71 74 78.5 65 78.5 "
         "C59 78.5 54 75.5 51 71.5 C51 79.5 55 86.5 61 90 H39 "
         "C45 86.5 49 79.5 49 71.5 C46 75.5 41 78.5 35 78.5 "
         "C26 78.5 16 71 16 58 C16 38 50 10 50 10 Z")
    return (f'<g transform="translate({cx - 50 * s:.2f},{cy - 50 * s:.2f}) '
            f'scale({s:.4f})"><path d="{d}" fill="{fill}"/></g>')


def rim_marks(cx, cy, r, n, fill):
    """Las marcas doradas del canto de la ficha."""
    return "\n    ".join(
        f'<rect x="-22" y="-15" width="44" height="30" rx="9" fill="{fill}" '
        f'transform="rotate({90 + i * (360.0 / n):.2f} {cx} {cy}) '
        f'translate({cx:.2f} {cy - r:.2f})"/>'
        for i in range(n))


def svg(maskable=False):
    size = 512
    c = size / 2
    k = 0.80 if maskable else 1.0  # zona segura para iconos maskable (Android)
    chip_r = 176 * k
    ring_r = 124 * k
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">
  <defs>
    <radialGradient id="felt" cx="50%" cy="8%" r="95%">
      <stop offset="0%" stop-color="#1a5643"/>
      <stop offset="55%" stop-color="#123a2e"/>
      <stop offset="100%" stop-color="#0a1611"/>
    </radialGradient>
    <linearGradient id="chip" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1d1d22"/>
      <stop offset="100%" stop-color="#0d0d10"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#f0cd7a"/>
      <stop offset="45%" stop-color="#d8a94e"/>
      <stop offset="100%" stop-color="#a87f31"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="{size}" height="{size}" fill="url(#felt)"/>
  <circle cx="{c}" cy="{c}" r="{chip_r:.1f}" fill="url(#chip)"/>
  <circle cx="{c}" cy="{c}" r="{chip_r:.1f}" fill="none" stroke="url(#gold)" stroke-width="{10 * k:.1f}"/>
  <g transform="translate({c} {c}) scale({k:.4f}) translate({-c} {-c})">
    {rim_marks(c, c, 156, 6, "url(#gold)")}
  </g>
  <circle cx="{c}" cy="{c}" r="{ring_r:.1f}" fill="#123a2e" stroke="url(#gold)" stroke-width="{5 * k:.1f}"/>
  {spade(c, c, 150 * k, "url(#gold)")}
</svg>
'''


def chrome():
    env = os.environ.get("CHROME")
    if env:
        return env
    for name in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("No encuentro Chromium; indica la ruta con CHROME=/ruta/al/chrome")


def render(svg_path, png_path, size):
    html = os.path.join(HERE, "_render.html")
    with open(html, "w", encoding="utf-8") as fh:
        fh.write(f'<!doctype html><meta charset="utf-8">'
                 f'<style>html,body{{margin:0;padding:0}}'
                 f'img{{display:block;width:{size}px;height:{size}px}}</style>'
                 f'<img src="{os.path.basename(svg_path)}">')
    # la ventana se pide más alta que el icono y luego se recorta: headless deja
    # relleno blanco si el viewport se queda corto respecto al tamaño pedido
    subprocess.run([chrome(), "--headless", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={size},{size + 400}",
                    f"--screenshot={png_path}", html],
                   check=True, capture_output=True)
    os.remove(html)
    Image.open(png_path).crop((0, 0, size, size)).save(png_path)


def flatten(path):
    """iOS pinta de negro cualquier transparencia: los iconos van sin alfa."""
    im = Image.open(path)
    if im.mode != "RGB":
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, FELT)
        bg.paste(im, mask=im.split()[-1])
        bg.save(path, optimize=True)


def main():
    for name, maskable in (("icon.svg", False), ("icon-maskable.svg", True)):
        with open(os.path.join(HERE, name), "w", encoding="utf-8") as fh:
            fh.write(svg(maskable))

    render(os.path.join(HERE, "icon.svg"), os.path.join(HERE, "icon-512.png"), 512)
    render(os.path.join(HERE, "icon-maskable.svg"),
           os.path.join(HERE, "icon-maskable-512.png"), 512)
    for path in ("icon-512.png", "icon-maskable-512.png"):
        flatten(os.path.join(HERE, path))

    # los tamaños pequeños salen mejor reduciendo el de 512 que rasterizando de nuevo
    base = Image.open(os.path.join(HERE, "icon-512.png")).convert("RGB")
    for size, name in ((180, "apple-touch-icon-180.png"), (192, "icon-192.png"),
                       (32, "favicon-32.png")):
        base.resize((size, size), Image.LANCZOS).save(os.path.join(HERE, name), optimize=True)

    print("iconos generados en", HERE)


if __name__ == "__main__":
    main()
