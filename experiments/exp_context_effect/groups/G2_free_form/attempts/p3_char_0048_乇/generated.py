"""Render 乇 (p3_char_0048) at 300x300, black on white.

Structure (from GT):
  3 strokes.
  1) 撇 (short flick) at top-right: from about (170, 80) down-left to (110, 105).
  2) 横 (long horizontal): from about (55, 135) rightward to (235, 130) —
     crosses through where the 撇 sits, i.e. 撇 hangs above/through it.
     Actually looking again: the 撇 sits ON the 横 crossing near its right end.
  3) 竖弯钩: starts near the middle-right (~x=175, y=110), goes down,
     curves rightward at the baseline, hooks up.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width=8):
    d.line(points, fill=INK, width=width, joint="curve")
    # brush-dab endpoints
    r = width // 2
    for (x, y) in [points[0], points[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# --- Stroke 1: 撇 (short flick) sitting above the crossbar ---
# Longer 撇 with tip up-right near (195, 65), sweeping down-left to (90, 125).
strk1 = []
import math
p0 = (200, 60)
p1 = (85, 128)
for t in [i / 20 for i in range(21)]:
    ctrl = (160, 88)
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * ctrl[0] + t ** 2 * p1[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * ctrl[1] + t ** 2 * p1[1]
    strk1.append((x, y))
stroke(strk1, width=8)

# --- Stroke 2: 横 (long horizontal crossbar) ---
# Long, slightly rising to the right end.
strk2 = [(35, 155), (140, 148), (250, 142)]
stroke(strk2, width=9)

# --- Stroke 3: 竖弯钩 ---
# Starts near right end of 撇 crossing (~x=185, y=90), descends nearly vertical,
# curves rightward along the bottom well below the 横, terminal hook up.
strk3 = []
# Vertical portion: (185, 100) → (185, 245), gently curving inward
for i in range(0, 40):
    t = i / 39
    x = 185 + 0  # straight vertical
    y = 100 + t * 145
    strk3.append((x, y))
# Curve rightward at the bottom - wide sweep
for t in [i / 20 for i in range(21)]:
    p0v = (185, 245)
    ctrlv = (215, 285)
    p1v = (260, 275)
    x = (1 - t) ** 2 * p0v[0] + 2 * (1 - t) * t * ctrlv[0] + t ** 2 * p1v[0]
    y = (1 - t) ** 2 * p0v[1] + 2 * (1 - t) * t * ctrlv[1] + t ** 2 * p1v[1]
    strk3.append((x, y))
# Terminal hook: up-and-slightly-left tick
strk3.append((262, 260))
strk3.append((258, 240))
stroke(strk3, width=9)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0048_乇/01_乇.png"
img.save(out)
print("saved", out)
