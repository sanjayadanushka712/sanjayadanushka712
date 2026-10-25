#!/usr/bin/env python3
"""Prepare the public GitHub avatar for a terminal-style ASCII portrait.

Only the derived SVG is committed; the avatar stays a temporary build file.
"""
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / 'source-prepped.png'
URL = 'https://github.com/leticiazooe.png?size=850'

def fallback():
    canvas = Image.new('L', (850, 850), 255)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((180, 180, 670, 670), radius=120, fill=230, outline=82, width=14)
    draw.ellipse((325, 260, 525, 460), fill=190, outline=55, width=12)
    draw.arc((282, 465, 568, 760), 180, 360, fill=55, width=18)
    return canvas

def main():
    try:
        req = Request(URL, headers={'User-Agent': 'leticia-profile-art/1.0'})
        with urlopen(req, timeout=30) as response:
            img = Image.open(BytesIO(response.read())).convert('RGB')
        img = ImageOps.fit(img, (850, 850), method=Image.Resampling.LANCZOS)
        img = ImageOps.grayscale(img)
        img = ImageOps.autocontrast(img, cutoff=1)
        img = ImageEnhance.Contrast(img).enhance(1.25)
        mask = Image.new('L', (850, 850), 0)
        ImageDraw.Draw(mask).ellipse((18, 18, 832, 832), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(14))
        img = Image.composite(img, Image.new('L', img.size, 255), mask)
        print('Prepared GitHub avatar for ASCII conversion')
    except Exception as exc:
        print(f'Avatar unavailable: {exc}. Using a neutral silhouette.')
        img = fallback()
    img.save(TARGET)

if __name__ == '__main__':
    main()
