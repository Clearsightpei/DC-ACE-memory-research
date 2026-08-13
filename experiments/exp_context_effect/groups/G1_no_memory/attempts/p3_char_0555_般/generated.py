"""G1 render of 般 - PIL-based, 300x300, white background, black ink. Revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# 般 = 舟 (left, occupies ~x 40-130) + 殳 (right, ~x 145-265)
# ---- Left: 舟 ----
# 1) 撇 - short diagonal top
stroke([(75, 60), (55, 95)], width=5)
# 2) 竖 - left vertical, slight lean, ends with hook
stroke([(58, 90), (52, 210)], width=5)
# hook
stroke([(52, 210), (72, 220)], width=5)
# 3) top horizontal of box
stroke([(60, 100), (125, 95)], width=5)
# 4) right vertical of box
stroke([(125, 95), (115, 215)], width=5)
# 5) middle horizontal (crossing both verticals)
stroke([(48, 155), (128, 150)], width=5)
# 6) two horizontals inside (dots-like short strokes) - upper
stroke([(72, 125), (108, 122)], width=4)
# 7) lower inside horizontal
stroke([(72, 180), (108, 178)], width=4)

# ---- Right: 殳 ----
# Top part: 几-shape (compact, upper right)
# short 撇 at top-left of 几
stroke([(170, 65), (162, 90)], width=5)
# horizontal top
stroke([(162, 90), (250, 88)], width=5)
# right side: vertical then curve/hook
stroke([(250, 88), (255, 140)], width=5)
stroke([(255, 140), (240, 150)], width=5)
# left leg of 几 - curving down-left
stroke([(172, 100), (150, 155)], width=5)

# Bottom part: 又
# top horizontal-diagonal of 又 (横撇)
stroke([(155, 165), (235, 158)], width=5)
# comes down as 撇 sweeping down-left from right side of that horizontal
stroke([(235, 158), (155, 260)], width=6)
# 捺 - starts from around the crossing and sweeps down-right
stroke([(195, 195), (265, 260)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_般.png")
img.save(out)
print(f"Saved {out}")
