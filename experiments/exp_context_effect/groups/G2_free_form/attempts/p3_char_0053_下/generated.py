"""Render 下 (xia) — 3 strokes: long top 横, through-going 竖 slightly left
of center descending well below, and a small 点 (right-slanting dot/flick)
to the right of the 竖 at mid-height.

Consulted memory:
- form_catalog "横 as top-vs-bottom length-differentiator (上 vs 下)":
  for 下 the TOP heng is the long base.
- form_catalog "竖 as through-going axis" for the vertical.
- Small 点 to the right of the 竖 is the identity mark of 下.

Output: 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def stroke_line(p0, p1, width):
    # Thick line with round caps via dabs at each end.
    draw.line([p0, p1], fill="black", width=width)
    dab(p0[0], p0[1], width // 2)
    dab(p1[0], p1[1], width // 2)


# --- Stroke 1: long top 横 (heng) ---
# GT: long horizontal near the top with very slight up-tilt.
# Start ~x=40, y=92; end ~x=265, y=85.
heng_start = (40, 92)
heng_end = (265, 85)
stroke_line(heng_start, heng_end, 9)
# terminal dun (small down curl at right end)
dab(262, 92, 6)
dab(258, 96, 5)

# --- Stroke 2: through-going 竖 (shu) ---
# Vertical LEFT of center (roughly under x=130), starts on the heng
# and descends WELL BELOW the heng. No hook.
shu_top = (130, 88)
shu_bot = (130, 278)
stroke_line(shu_top, shu_bot, 9)
# small dun at top
dab(130, 91, 6)

# --- Stroke 3: 点 (dian) — right-slanting tapered flick ---
# Sits to the RIGHT of the 竖 at mid-height. Continuous tapered stroke
# from thin top-left to thick bottom-right.
import math
p_start = (148, 140)
p_end = (188, 185)
n_steps = 40
for i in range(n_steps + 1):
    t = i / n_steps
    x = p_start[0] + (p_end[0] - p_start[0]) * t
    y = p_start[1] + (p_end[1] - p_start[1]) * t
    # radius grows from 2 to 6
    r = 2 + 4 * t
    dab(x, y, r)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0053_下/01_下.png")
print("saved")
