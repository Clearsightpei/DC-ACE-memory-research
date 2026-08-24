"""G1 render for radical 礻 (4 strokes).
Strokes (top to bottom):
  1. dot (点) at top — short slanted stroke top-right
  2. short horizontal (橫) below dot, going right-down slightly
  3. long left-falling curve (撇) from top-right down-left
  4. vertical hook / vertical (竖) crossing the pie
Plus a small right-falling dot for the final component.
Actually the standard 礻 = 4 strokes: 点, 横撇 (combined), 竖, 点.
Order: dot, horizontal-then-pie, vertical, right-dot.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    # draw a polyline with rounded joints; approximate with multiple line segs
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    # round caps
    r = width // 2
    for (x, y) in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Stroke 1: top dot (点) — small slanted stroke, higher up, more offset
stroke([(160, 55), (178, 78)], width=7)

# Stroke 2: 横撇 — short horizontal then long pie
# horizontal part (small, near upper area)
stroke([(120, 108), (188, 100)], width=6)
# pie continues from end of horizontal — curves down-left, gentler
stroke([(188, 100), (170, 130), (130, 175), (85, 235)], width=7)

# Stroke 3: vertical (竖) — center vertical from junction area down
stroke([(150, 128), (150, 265)], width=7)

# Stroke 4: right dot (点) — small down-right dot to right of vertical
stroke([(162, 165), (198, 200)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_116_礻/01_礻.png")
print("saved")
