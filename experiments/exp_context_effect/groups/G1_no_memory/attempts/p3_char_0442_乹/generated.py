"""Render 乹 as a 300x300 PNG using PIL.

Structure (from GT):
- Left component: 卓-like radical (十 on top with a horizontal bar, then 早 lower).
  Looking closely at the GT it's actually 卓 (top 十 + 日 + 十-like base)
  Simplified: top horizontal, vertical stroke through center-top, then a
  rectangular box (日), then a long horizontal at the bottom with a
  vertical tail dropping.
- Right component: 乙 (a hooked stroke curving down-right then hooking left-up)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ============ LEFT COMPONENT: 卓 ============
# Top horizontal (short)
line([(55, 70), (140, 68)], width=5)

# Small vertical/dot above the top horizontal (like 十 top)
line([(95, 45), (95, 70)], width=5)

# Vertical descending through the box
line([(95, 70), (95, 175)], width=5)

# 日 box (rectangle with middle horizontal)
# Top of box
line([(55, 95), (140, 95)], width=5)
# Left side
line([(55, 95), (55, 175)], width=5)
# Right side
line([(140, 95), (140, 175)], width=5)
# Middle horizontal
line([(55, 135), (140, 135)], width=5)
# Bottom of box
line([(55, 175), (140, 175)], width=5)

# Long horizontal (bottom, wider than box)
line([(30, 210), (170, 208)], width=5)

# Vertical tail dropping from middle of long horizontal
line([(95, 175), (95, 270)], width=5)

# ============ RIGHT COMPONENT: 乙 ============
# 乙 shape: short horizontal top, sweeping diagonal down-left,
# then a long horizontal bottom stroke with a slight hook up at end.
pts = [
    (195, 65),
    (255, 65),   # short top horizontal
    (252, 85),
    (230, 115),
    (205, 155),  # diagonal descending
    (185, 200),
    (180, 235),
    (195, 260),  # curve into bottom
    (235, 268),
    (270, 265),  # bottom horizontal
    (272, 250),  # tiny hook up
]
line(pts, width=5)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0442_乹/01_乹.png"
img.save(out)
print("wrote", out)
