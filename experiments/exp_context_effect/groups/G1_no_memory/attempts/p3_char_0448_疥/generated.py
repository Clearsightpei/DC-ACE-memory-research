"""G1 render of 疥 (jie). 疒 radical (left) + 介 (right).

Structure per GT:
  - 疒: top dot, long horizontal top, long piě sweeping down-left,
        two small inner strokes.
  - 介: inverted-V apex, then two legs hanging (left piě, right vertical),
        plus a short middle vertical from apex.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 疒 radical (left half, occupies most vertical space) ----

# 1. Top short dot (tick) — upper area, slightly right of center-left
stroke([(120, 50), (135, 38)], width=5)

# 2. Long horizontal top of 疒 (spans across, slight downward slope)
stroke([(70, 78), (185, 70)], width=5)

# 3. Long left-falling piě of 疒 — from top down-left to bottom-left corner
stroke([(125, 55), (110, 100), (90, 160), (60, 240), (45, 275)], width=5)

# 4. Upper inner short stroke of 疒 (small piě)
stroke([(95, 110), (80, 128)], width=5)

# 5. Lower inner short stroke of 疒 (small horizontal tick)
stroke([(80, 155), (100, 150)], width=5)

# ---- 介 (right/lower, inside the radical's cradle) ----

# 6. Apex left stroke (piě) of 介
stroke([(190, 90), (155, 145)], width=5)

# 7. Apex right stroke (nà) of 介
stroke([(190, 90), (235, 145)], width=5)

# 8. Left leg of 介 — piě sweeping down-left
stroke([(180, 140), (150, 265)], width=5)

# 9. Right leg of 介 — vertical/slight right lean, ending with hook to right
stroke([(215, 140), (225, 270)], width=5)

# 10. Middle vertical from apex (short)
stroke([(193, 100), (192, 195)], width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_疥.png")
img.save(out_path)
print(f"Saved: {out_path}")
