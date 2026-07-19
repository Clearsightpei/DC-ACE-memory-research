"""Render 彳 (chì) — 3-stroke radical.

Strokes (top to bottom):
1. 短撇 (short 撇) in the upper region — small tick curving down-left
2. 撇 (longer 撇) starting lower-left of stroke 1, with a visible GAP —
   curves down-left, longer arc
3. 竖 (vertical) — starts at the "elbow" where stroke 2 was, going straight down

Reference GT: upper short 撇 is high & to the right; lower 撇 begins
clearly below and slightly left of it (not touching); 竖 drops from
the middle of that 撇 straight down to bottom.

Output: 300x300 white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=6):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=BLACK, width=width)
    for p in points:
        draw.ellipse((p[0] - width // 2, p[1] - width // 2,
                      p[0] + width // 2, p[1] + width // 2), fill=BLACK)

# Stroke 1: short 撇 in upper region — a tick from upper-right to lower-left
# Small: ~30px span. Placed high (y=60..95) and to the right (x=180..155)
s1 = [(182, 62), (172, 78), (158, 95)]
stroke(s1, width=6)

# Stroke 2: longer 撇 — starts BELOW stroke 1 with a clear gap.
# Begins around (168, 108) — visibly separated from s1 end (158,95).
# Curves down-left, ending lower-left near (95, 230).
s2 = [(168, 108), (155, 140), (135, 175), (115, 210), (95, 240)]
stroke(s2, width=7)

# Stroke 3: 竖 — drops from around midpoint of stroke 2 straight down.
# Starts at approximately (140, 170) — on the arc of stroke 2 — goes to (140, 265).
s3 = [(140, 172), (140, 265)]
stroke(s3, width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_041_彳/01_彳.png")
print("saved")
