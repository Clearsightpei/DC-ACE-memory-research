# p3_char_0285_师 — G3 attempt (revision 1)
# 师: left component (短横 + 长撇竖) + right 帀 (一 + 巾).
# Thin uniform strokes per P12 / MMH GT style.
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

def line(p, q, w=LW):
    d.line([p, q], fill=INK, width=w)

def curve(pts, w=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill=INK, width=w)

def draw_shi(ox=0, oy=0):
    # ---- Left component ----
    # short 一 near top-center of left half, slight upward tilt right
    line((35 + ox, 115 + oy), (95 + ox, 108 + oy))
    # long 丿 (竖撇): starts high near where 一 ends, curves down-left
    curve([
        (78 + ox, 85 + oy),
        (72 + ox, 130 + oy),
        (62 + ox, 175 + oy),
        (48 + ox, 220 + oy),
        (30 + ox, 265 + oy),
    ])

    # ---- Right component 帀 ----
    # top heng: long, spans right side
    line((100 + ox, 92 + oy), (280 + ox, 90 + oy))
    # inner heng (top of 巾), just under the top heng
    line((118 + ox, 128 + oy), (258 + ox, 126 + oy))
    # left 竖 of 巾
    line((125 + ox, 128 + oy), (125 + ox, 245 + oy))
    # right 横折钩: vertical drop + small hook up-left
    line((252 + ox, 126 + oy), (252 + ox, 240 + oy))
    line((252 + ox, 240 + oy), (238 + ox, 230 + oy))
    # middle 竖 of 巾: descends from inner heng, extends past bottom
    line((188 + ox, 128 + oy), (188 + ox, 278 + oy))

draw_shi()

out = os.path.join(os.path.dirname(__file__), "01_师.png")
img.save(out)
print("saved", out)
