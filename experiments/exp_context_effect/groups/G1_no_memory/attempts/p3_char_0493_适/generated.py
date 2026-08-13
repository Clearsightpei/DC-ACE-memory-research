"""Render 适 to a 300x300 PNG (G1, no memory). Revised once."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- 舌 on the right/upper (fits inside 辶 pocket) ----
# 千 on top:
# 丿 (short slant) topmost
line([(170, 45), (150, 75)], 6)
# 一 (long horizontal)
line([(115, 85), (245, 85)], 6)
# 千 middle short horizontal
line([(140, 115), (215, 115)], 5)
# 千 vertical descending into 口
line([(180, 70), (178, 165)], 6)

# 口 (mouth) below 千
LX, RX, TY, BY = 140, 225, 160, 215
# top horizontal
line([(LX, TY), (RX, TY)], 5)
# left vertical
line([(LX, TY), (LX, BY)], 5)
# right vertical (with slight 横折 feel)
line([(RX, TY), (RX, BY)], 5)
# bottom horizontal
line([(LX, BY), (RX, BY)], 5)

# ---- 辶 radical on left/bottom ----
# 点 (dot) upper-left
line([(70, 55), (85, 78)], 7)

# 横折折撇 middle: short horizontal, turn down, then a small hook/slant
line([(55, 115), (100, 112)], 5)
line([(100, 112), (92, 145)], 5)
line([(92, 145), (75, 165)], 5)

# 平捺 — the long sweeping bottom stroke of 辶
# Starts upper-left, dips low, sweeps right and rises with a flared tail
sweep = [
    (55, 195),
    (70, 220),
    (110, 245),
    (170, 258),
    (225, 253),
    (260, 235),
    (280, 215),
]
line(sweep, 7)
# small flare tail
line([(275, 220), (290, 210)], 6)

out_path = os.path.join(os.path.dirname(__file__), "01_适.png")
img.save(out_path)
print(f"wrote {out_path}")
