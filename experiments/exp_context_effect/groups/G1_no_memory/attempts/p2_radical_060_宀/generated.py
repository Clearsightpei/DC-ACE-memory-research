"""G1 attempt: 宀 (radical, 3 strokes)

宀 = "roof" radical. Three strokes:
  1. Top dot (点) — small stroke top-center.
  2. Left dot / short slanting stroke (点/竖) on the upper-left of the roof.
  3. Horizontal turn hook (横钩) — long horizontal top with a hook down at right end.
Actually the canonical decomposition is:
  1. Top dot (点) — small centered on top.
  2. Left short slanted stroke (点).
  3. 横钩 — a long horizontal ending with a small hook down-left at the right.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 5  # base stroke width


def line(pts, width=INK):
    d.line(pts, fill=BLACK, width=width, joint="curve")


def dot_stroke(x, y, dx, dy, w=INK):
    # small stroke from (x,y) to (x+dx,y+dy) — thick-ish
    line([(x, y), (x + dx, y + dy)], width=w)


# GT observation:
# - The character sits roughly middle-vertical.
# - Top "dot" is small near center-top of the roof.
# - Under-left there is a slanting stroke (dian) going down-left.
# - The 横钩 spans left-to-right at mid-height, ending with a downward hook on the right.

# ---- Stroke 1: top dot (点) ----
# short slanting stroke, centered upper — slants down-right
line([(150, 110), (160, 130)], width=5)

# ---- Stroke 2: left dot (点) — a short slanted stroke on the roof's left ----
# separated from the horizontal, sits above-left
line([(95, 175), (85, 210)], width=5)

# ---- Stroke 3: 横钩 (horizontal-hook) ----
# long horizontal with slight downward slant to the right, then a sharp hook down-left
# horizontal segment — starts a bit right of the left dot, goes to right side
line([(105, 170), (230, 180)], width=4)
# hook: short stroke turning down-left from the right end
line([(230, 180), (215, 210)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_060_宀/01_宀.png")
print("wrote 01_宀.png")
