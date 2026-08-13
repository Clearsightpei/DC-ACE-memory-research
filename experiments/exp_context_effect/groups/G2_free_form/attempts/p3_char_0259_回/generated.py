"""回 — outer 口 + inner 口 (6 strokes).

Stroke order:
  Outer: 1) 竖 left side, 2) 横折 top+right, 3) 横 bottom (closes outer)
  Inner: 4) 竖 left, 5) 横折 top+right, 6) 横 bottom
Slight brush waver via multiple offset lines.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width=8):
    # Slight brush feel: draw main line + small offset for weight
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # end-cap circles
    for (x, y) in [pts[0], pts[-1]]:
        r = width // 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# Outer square bounds (roughly centered, a bit off vertical center like GT)
OL, OR = 55, 250
OT, OB = 55, 255

# 1) 竖 left side (outer)
stroke([(OL, OT + 5), (OL - 2, OB)], width=9)

# 2) 横折 top + right side (outer): from left-top going right, then down
stroke([(OL - 4, OT), (OR + 2, OT - 2), (OR + 5, OB - 2)], width=9)

# Inner square (smaller, sits inside)
IL, IR = 105, 200
IT, IB = 115, 200

# 4) 竖 left (inner)
stroke([(IL, IT + 2), (IL - 1, IB)], width=6)

# 5) 横折 top + right (inner)
stroke([(IL - 2, IT), (IR + 2, IT - 1), (IR + 3, IB - 1)], width=6)

# 6) 横 bottom (inner)
stroke([(IL - 3, IB), (IR + 4, IB - 1)], width=6)

# 3) 横 bottom (outer) — drawn last, closes outer square
stroke([(OL - 6, OB), (OR + 6, OB - 2)], width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0259_回/01_回.png")
print("wrote 01_回.png")
