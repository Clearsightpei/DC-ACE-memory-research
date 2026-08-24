"""G1 render for 已 (p3_char_0079_已).
3 strokes:
  1) top: horizontal then turn down (horizontal-fold) — forms top+left+right of upper box
     Actually 已 stroke 1 is 横折 (horizontal then bend down) — top and right side.
  2) middle: horizontal stroke starting from left, going right into the fold
  3) bottom: 竖弯钩 (vertical-bend-hook) — starts as left vertical, curves right along bottom, ends with small up-hook
Traditional structure:
  Stroke 1 draws top-left corner going right, then bends down (short vertical) — the "コ" opening
  Stroke 2 is the middle horizontal
  Stroke 3 wraps: down-left, bottom-right, then hook up
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# Layout (matches GT roughly): character occupies rough band y=70..260, x=60..230
# Stroke 1 — 横折 (top horizontal then bend down): starts upper-left, goes right, then down a short bit
# In 已, stroke 1 forms the top and right side of the upper compartment
s1 = [(70, 90), (200, 82), (205, 145)]
d.line(s1, fill=BLACK, width=LW, joint="curve")

# Stroke 2 — middle horizontal: starts at left (inside), goes right to meet stroke 1's descender
s2 = [(85, 140), (200, 145)]
d.line(s2, fill=BLACK, width=LW, joint="curve")

# Stroke 3 — 竖弯钩: starts high on left (at top-left near stroke1's start), goes down as vertical,
# curves right along bottom, then hooks up at the right end
# In 已 the hook goes UP (distinguishing from 己 and 巳)
s3 = [
    (72, 95),    # top-left start (aligned with stroke 1 start)
    (68, 200),   # down the left side
    (75, 245),   # curve
    (130, 262),  # bottom
    (220, 258),  # bottom-right
    (232, 220),  # hook up
    (228, 195),  # hook tip
]
d.line(s3, fill=BLACK, width=LW, joint="curve")

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0079_已/01_已.png")
