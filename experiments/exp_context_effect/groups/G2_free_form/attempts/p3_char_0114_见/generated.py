"""
见 (jiàn) — Phase 3 character, item p3_char_0114_见

# SIGNATURE CHECK (per sibling_signature_checklist.md):
#   target = 见
#   bit = 冂 + ONE 横 + 撇+竖弯钩 legs (vs 贝 which has TWO internal 横 + straight ㅅ legs)
#   flick = 竖弯钩 terminal: UP-and-LEFT after the arc (~-105° to -115°)

Structure (rendered as 4 strokes per standard MMH decomposition,
with the "interior 横" realized as the inner horizontal that visually
sits inside the 冂 box):

  1) 竖 — left wall of 冂 (top-left down)
  2) 横折 — top of 冂 plus right wall (right-then-down); includes
     the return-inner-横 as the last small segment visually inside
  3) 撇 — left leg, from bottom-left of 冂 slanting down-left
  4) 竖弯钩 — right leg, from bottom-right descending, curving right,
     terminal hook flicking UP-and-LEFT (into character body)

Note: a distinct interior 横 line is added because the GT shows one
mid-body cross-bar; keeping the render true to GT.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # brush width

# Layout inside 米字格 (approx). 冂 box:
#   top-left  ~ (80, 55)
#   top-right ~ (215, 55)
#   left wall bottom ~ (80, 180)
#   right wall bottom ~ (215, 190)

# --- Stroke 1: 竖 (left wall of 冂), slight lean, top-left → bottom-left ---
d.line([(85, 60), (78, 200)], fill=BLACK, width=LW)

# --- Stroke 2: 横折 (top of 冂 + right wall) ---
# horizontal top
d.line([(80, 58), (215, 55)], fill=BLACK, width=LW)
# right wall going down (the "折" turns down)
d.line([(215, 55), (212, 195)], fill=BLACK, width=LW)

# --- Interior 横 (single, per signature bit "ONE 横") ---
# sits roughly mid-box horizontally
d.line([(90, 118), (208, 118)], fill=BLACK, width=LW)

# --- Stroke 3: 撇 (left leg) — from bottom-left corner slanting down-left ---
d.line([(80, 195), (50, 275)], fill=BLACK, width=LW)

# --- Stroke 4: 竖弯钩 (right leg) ---
# descend from bottom-right of 冂
p1 = (150, 118)   # actually the right leg of 见 originates from inside
# Reconsider: right leg starts near center-bottom of the box, descends,
# then curves rightward, then flicks UP-and-LEFT.
# Path: start at ~ (150, 120), descend to (155, 245), curve to (215, 275),
# then hook up-left to (200, 250).
# Draw as poly-line approximating a smooth curve.
curve_pts = [
    (152, 120),
    (152, 170),
    (154, 210),
    (160, 245),
    (180, 268),
    (210, 275),
    (222, 268),
]
d.line(curve_pts, fill=BLACK, width=LW)
# Terminal hook: UP-and-LEFT flick (~-110°)
d.line([(222, 268), (208, 250)], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0114_见/01_见.png")
print("saved 01_见.png")
