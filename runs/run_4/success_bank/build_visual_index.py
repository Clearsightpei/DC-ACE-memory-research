#!/usr/bin/env python3
"""Rebuild success_bank/visual/visual_index.png from current INDEX.md.

Curator runs this whenever a new entry is added.
Looks at each row in success_bank/INDEX.md, finds the corresponding
attempt PNG at attempts/cycle_<N>/01_<char>.png, and tiles them in
a 4-column grid with CJK captions.

Usage: cd into the run dir, then `python3 success_bank/build_visual_index.py`.
"""
import os
import re
from PIL import Image, ImageDraw, ImageFont

RUN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INDEX = os.path.join(RUN_DIR, 'success_bank', 'INDEX.md')
OUT = os.path.join(RUN_DIR, 'success_bank', 'visual', 'visual_index.png')

# Parse INDEX.md table rows: | <char> | ... | c<N> |
entries = []
with open(INDEX) as f:
    for line in f:
        # Match the char column. Atomic strokes are 1 char, compound strokes
        # can be 2+ chars (e.g. 横折). Stop at the next | or whitespace before |.
        m = re.match(r'^\|\s*(\S+?)\s*\|.*\bc(\d+)\s*\|', line)
        if m:
            entries.append((m.group(1), int(m.group(2))))

if not entries:
    print('No entries found in INDEX.md — visual_index left as-is.')
    raise SystemExit(0)

imgs = []
for char, cycle_n in entries:
    png = os.path.join(RUN_DIR, 'attempts', f'cycle_{cycle_n}', f'01_{char}.png')
    if not os.path.exists(png):
        print(f'WARN: png missing for {char} at {png}')
        continue
    imgs.append((char, Image.open(png).convert('RGB')))

COLS = 4
THUMB_W, THUMB_H = 200, 150
CAPTION_H = 30
PAD = 16
n = len(imgs)
rows = max(1, (n + COLS - 1) // COLS)
cell_w, cell_h = THUMB_W + PAD, THUMB_H + CAPTION_H + PAD
canvas_w = max(cell_w * COLS + PAD, 400)
canvas_h = cell_h * rows + PAD

canvas = Image.new('RGB', (canvas_w, canvas_h), 'white')
draw = ImageDraw.Draw(canvas)

# Pick a CJK-capable font (macOS-friendly fallback chain).
font = None
for candidate in [
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/STHeiti Light.ttc',
    '/System/Library/Fonts/PingFang.ttc',
]:
    if os.path.exists(candidate):
        font = ImageFont.truetype(candidate, 24)
        break
if font is None:
    font = ImageFont.load_default()

for i, (char, img) in enumerate(imgs):
    col, row = i % COLS, i // COLS
    x = PAD + col * cell_w
    y = PAD + row * cell_h
    img.thumbnail((THUMB_W, THUMB_H))
    canvas.paste(img, (x + (THUMB_W - img.width) // 2,
                       y + (THUMB_H - img.height) // 2))
    bbox = draw.textbbox((0, 0), char, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((x + (THUMB_W - tw) // 2, y + THUMB_H + 4),
              char, fill='black', font=font)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
canvas.save(OUT, 'PNG')
print(f'Wrote {OUT}  ({canvas.size}, {len(imgs)} entries)')
