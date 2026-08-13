# 皿 (mǐn) — bank entry (B7 curator promotion, main PASS)
# Source: groups/G3_coords/attempts/p3_char_0195_皿/generated.py
# Note: 5 (PIL inline: 3 shus + top-right corner + long base heng)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

"""
皿 (min, "dish/vessel") — 5 strokes
Standard stroke order:
1. 丨 left vertical (slightly slanted inward)
2. 丨 first inner vertical (short)
3. 丨 second inner vertical (short)
4. ㇕ 横折 (top-right: short horizontal then vertical down)
5. 一 bottom horizontal (wide, extends beyond the box)

G3 v8: bank is REFERENCE only. This character has no direct alias in bank.
Inlining fresh via PIL — GT shows a wide, shallow open-topped basin
with a long base horizontal.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6  # main line width

# Box coords (looking at GT: box is wide, roughly y=95..200, x=60..240)
# Bottom horizontal extends beyond: x=30..270 at y=215

# Top of box interior (there is no top horizontal — 皿 is open top; the
# top-right corner 横折 provides only a short right cap)

# --- Stroke 1: left vertical (slanted slightly inward toward bottom) ---
d.line([(70, 100), (78, 205)], fill=INK, width=LW)

# --- Stroke 2: first inner short vertical ---
d.line([(120, 108), (122, 205)], fill=INK, width=LW)

# --- Stroke 3: second inner short vertical ---
d.line([(170, 108), (170, 205)], fill=INK, width=LW)

# --- Stroke 4: 横折 top-right corner (short horizontal, then down) ---
# Horizontal cap runs from ~x=105 to x=225 at y=100
d.line([(105, 100), (225, 100)], fill=INK, width=LW)
# Then vertical down (right wall, slanted slightly inward)
d.line([(225, 100), (218, 205)], fill=INK, width=LW)

# --- Stroke 5: long bottom horizontal (extends beyond box on both sides) ---
d.line([(35, 220), (270, 218)], fill=INK, width=LW+1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0195_皿/01_皿.png")
print("saved")
