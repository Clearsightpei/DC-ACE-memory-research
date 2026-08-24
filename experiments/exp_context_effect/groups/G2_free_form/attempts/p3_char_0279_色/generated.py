"""
色 (sè) — 6 strokes
Structure: top 勹-like (撇 + 横折钩) over bottom 巴-like
  1. 撇 — top-left long diagonal
  2. 横折钩 — top cap horizontal → down → UP-LEFT hook flick
  3. 横折 — top of bottom 巴 (short horizontal + down)
  4. 竖 — left side of 巴 (goes down from top-left of bottom section)
  5. 横 — middle horizontal inside 巴
  6. 竖弯钩 — right side down, sweep right along bottom, hook UP-LEFT

Revision notes vs pass 1:
- Enlarged and moved top 勹 to sit ON TOP of bottom, wider.
- Bottom rewritten as open 巴 shape (not a closed rectangle).
- 竖弯钩 sweeps as one long stroke: down right-side then across bottom
  with terminal UP-LEFT flick per TIER-0 hook rule.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def line(pts, w=6):
    d.line(pts, fill=BLACK, width=w, joint="curve")

def brush_taper(pts, w_start, w_end, steps=25):
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i+1]
        for s in range(steps):
            t0 = s / steps
            t1 = (s + 1) / steps
            xa = x0 + (x1 - x0) * t0
            ya = y0 + (y1 - y0) * t0
            xb = x0 + (x1 - x0) * t1
            yb = y0 + (y1 - y0) * t1
            frac = (i + t0) / max(1, len(pts) - 1)
            w = int(round(w_start + (w_end - w_start) * frac))
            if w < 1: w = 1
            d.line([(xa, ya), (xb, yb)], fill=BLACK, width=w)

# ==== TOP 勹 (larger, centered above bottom) ====
# Stroke 1: 撇 — long diagonal from top-mid down-left
brush_taper([(155, 55), (135, 90), (110, 135)], w_start=7, w_end=3)

# Stroke 2: 横折钩 — starts near top of 撇, goes right, folds down, tiny UP-LEFT hook
line([(150, 68), (210, 68)], w=6)
line([(210, 68), (210, 140)], w=6)
# hook flick UP-LEFT (per TIER-0 rule)
line([(210, 140), (198, 130)], w=5)

# ==== BOTTOM 巴 (open shape) ====
# Stroke 3: 横折 — top of bottom 巴 (short horizontal + short down)
# begins on left, extends right, folds down a bit
line([(85, 155), (215, 155), (215, 205)], w=6)

# Stroke 4: 竖 — left vertical
line([(85, 155), (85, 250)], w=6)

# Stroke 5: 横 — middle horizontal inside bottom
line([(85, 205), (215, 205)], w=6)

# Stroke 6: 竖弯钩 — from top-right area of bottom, actually it forms
# the sweep along bottom and up on right. Bottom of 巴 is left-vertical
# plus this sweeping stroke. Draw sweep: from (215, 205) continues down,
# curves right across the bottom, ends with UP-LEFT hook.
# But 巴 stroke order: 竖弯钩 is the final sweep on right side + bottom.
# I'll draw the bottom-right sweep as one polyline.
sweep = [(215, 205), (215, 245), (222, 258), (240, 262), (255, 258), (262, 248)]
line(sweep, w=6)
# hook flick UP-LEFT at terminal
line([(262, 248), (250, 240)], w=5)

# Connect left 竖 to sweep along bottom (the bottom horizontal of 巴)
line([(85, 250), (215, 250)], w=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0279_色/01_色.png")
print("saved")
