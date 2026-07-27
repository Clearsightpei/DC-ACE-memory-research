"""Render 乜 (character p3_char_0018) — G1 no-memory attempt (revision).

Reading GT more carefully, 乜 has 2 strokes:
  1) 横折竖弯钩 shape: a short vertical descent at top, folds into
     horizontal along middle, drops down as vertical on the right,
     and finishes with a small upward hook at bottom-right.
     BUT visually the GT shows the short top-left vertical + a long
     horizontal middle line, and a bottom-right L-hook.
  2) A pie (撇) from upper-mid going down-left, and a small angled
     mark inside (like a ✓ tick) sitting on the horizontal.

Rendered in PIL at 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
INK = 0
BG = 255
STROKE = 6

img = Image.new("L", (W, H), BG)
draw = ImageDraw.Draw(img)


def polyline(points, width=STROKE):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)
    for p in points:
        draw.ellipse([p[0] - width / 2, p[1] - width / 2,
                      p[0] + width / 2, p[1] + width / 2], fill=INK)


# --- Stroke 1a: short vertical at top-left ---
polyline([(115, 85), (115, 135)])

# --- Stroke 1b: horizontal across the middle ---
polyline([(55, 160), (180, 160)])

# --- Stroke 1c: right side vertical + upward hook (竖弯钩 tail) ---
polyline([(195, 155), (200, 245), (215, 245), (215, 220)])

# --- Stroke 2: 撇 (pie) from upper-mid going down-left, crossing top ---
polyline([(155, 75), (135, 110), (100, 140), (70, 160)])

# --- Small internal ✓-like mark (inside the bowl) ---
polyline([(140, 130), (155, 165), (170, 145)])

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_乜.png")
img.convert("RGB").save(out_path)
print(f"Wrote {out_path}")
