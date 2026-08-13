"""
其 (qí) — 8 strokes, Phase-3 character
Standard stroke order:
 1. 一 top short horizontal
 2. 丨 left vertical (slanted outward — head is up/inside, foot is down/outside)
 3. 一 first inner horizontal (short)
 4. 一 second inner horizontal (short)
 5. 丨 right vertical (slanted outward the other way, cuts through)
 6. 一 long bottom horizontal (wide, extends past the body)
 7. 丿 left foot (short pie sloping down-left)
 8. 丶 right foot (dot sloping down-right)

G3 v8: no direct alias in bank. 皿/min_dish gives the "box + long
base heng" pattern; here the box has slanted walls (like 甘/其-body)
and two feet dangle below. Inlining fresh via PIL.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# --- Stroke 1: top short horizontal ---
# Sits between the two vertical heads
d.line([(78, 62), (200, 60)], fill=INK, width=LW)

# --- Stroke 2: left vertical, slanted (head narrow, foot wide) ---
# From ~(78, 62) down-left to ~(50, 205)
d.line([(78, 62), (52, 205)], fill=INK, width=LW)

# --- Stroke 3: first inner horizontal ---
d.line([(88, 118), (198, 118)], fill=INK, width=LW - 1)

# --- Stroke 4: second inner horizontal ---
d.line([(82, 162), (205, 162)], fill=INK, width=LW - 1)

# --- Stroke 5: right vertical, slanted the other way ---
# From ~(200, 60) down-right to ~(228, 208), cutting through
d.line([(200, 60), (228, 208)], fill=INK, width=LW)

# --- Stroke 6: long base horizontal ---
d.line([(28, 210), (275, 208)], fill=INK, width=LW + 1)

# --- Stroke 7: left foot 丿 (short pie, down-left, slight curve) ---
# Anchor near the left third of base, drop down-left
import math
pts_pie = []
for i in range(21):
    t = i / 20.0
    # Start (115, 222) -> end (78, 275), slight bow to the left
    x0, y0 = 115, 222
    x1, y1 = 78, 275
    bx = (x0 + x1) / 2 - 6  # small left bow
    by = (y0 + y1) / 2
    x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * bx + t ** 2 * x1
    y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * by + t ** 2 * y1
    pts_pie.append((x, y))
for i in range(len(pts_pie) - 1):
    w = int(round(LW - 1 - 2.5 * (i / (len(pts_pie) - 1))))  # taper
    w = max(2, w)
    d.line([pts_pie[i], pts_pie[i + 1]], fill=INK, width=w)

# --- Stroke 8: right foot 丶 (dot, down-right) ---
# Anchor near right third of base
pts_dot = []
for i in range(15):
    t = i / 14.0
    x0, y0 = 195, 222
    x1, y1 = 225, 268
    x = x0 + (x1 - x0) * t
    y = y0 + (y1 - y0) * t
    pts_dot.append((x, y))
for i in range(len(pts_dot) - 1):
    w = int(round(3 + 4 * (i / (len(pts_dot) - 1))))  # grows toward tail
    d.line([pts_dot[i], pts_dot[i + 1]], fill=INK, width=w)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0369_其/01_其.png"
img.save(out)
print("saved", out)
