"""Render 川 (chuan1 - river) as 300x300 PNG, white bg, black ink.

Character 川 has 3 strokes:
  1. Left stroke: 撇 (pie) — short curved stroke, top-left, curving down-left
  2. Middle stroke: 竖 (shu) — vertical, slightly shorter, starts a bit lower
  3. Right stroke: 竖 (shu) — long vertical, slight curve, tallest
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6  # line width

def stroke(points, width=LW):
    # draw a polyline with rounded joints
    draw.line(points, fill=INK, width=width, joint="curve")
    # cap the endpoints with small circles for smooth ends
    r = width / 2
    for x, y in (points[0], points[-1]):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)

# --- Stroke 1: left 撇 (pie) — starts upper-left, curves down and slightly left ---
s1 = [
    (95, 105),
    (92, 140),
    (88, 175),
    (82, 210),
    (72, 240),
    (60, 260),
]
stroke(s1)

# --- Stroke 2: middle 竖 — shorter vertical, starts a bit lower ---
s2 = [
    (150, 125),
    (150, 160),
    (150, 200),
    (150, 240),
]
stroke(s2)

# --- Stroke 3: right 竖 — long vertical, slight leftward curve at top ---
s3 = [
    (218, 90),
    (218, 130),
    (218, 175),
    (218, 220),
    (218, 260),
]
stroke(s3)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0088_川/01_川.png"
img.save(out)
print(f"Saved {out}")
