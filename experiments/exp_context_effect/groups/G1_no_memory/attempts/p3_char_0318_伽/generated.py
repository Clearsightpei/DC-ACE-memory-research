"""Render 伽 (jiā) — 亻 radical + 加 (力 + 口)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5


def poly(points, w=LW):
    d.line(points, fill=INK, width=w, joint="curve")


# ============ 亻 (person radical) — left side ============
# 撇 (left-falling): starts upper-right, curves down-left
poly([(80, 90), (72, 130), (60, 180), (48, 230)], w=LW)
# 竖 (vertical): meets the 撇 near its start
poly([(78, 130), (78, 255)], w=LW)

# ============ 力 — middle ============
# 横折钩 (horizontal-turn-hook): top horizontal → vertical down → small hook up-left
poly([(120, 105), (188, 100)], w=LW)                       # top horizontal
poly([(186, 100), (188, 210), (178, 225)], w=LW)           # vertical + hook curve
poly([(178, 225), (162, 220)], w=LW)                        # hook tip flicks left-up

# 撇 (long left-falling) through the 力
poly([(155, 105), (140, 160), (120, 215), (108, 250)], w=LW)

# ============ 口 — right side ============
# left vertical (竖)
poly([(212, 140), (212, 235)], w=LW)
# top horizontal + right vertical (横折)
poly([(210, 138), (275, 135), (273, 235)], w=LW)
# bottom horizontal (横)
poly([(212, 233), (275, 235)], w=LW)

out = os.path.join(os.path.dirname(__file__), "01_伽.png")
img.save(out)
print(f"wrote {out}")
