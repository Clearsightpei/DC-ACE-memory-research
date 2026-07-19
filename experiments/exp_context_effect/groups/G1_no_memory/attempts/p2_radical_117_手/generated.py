"""G1 render of 手 (radical 117, 4 strokes)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

def curve(pts, width=LW):
    # simple polyline; caller passes many pts to approximate a curve
    d.line(pts, fill=INK, width=width, joint="curve")

# Center of character ~ x=150. Vertical spans top ~70 to bottom ~255.
# Stroke 1: 撇 (ノ) — starts upper-right, curves down-left, crosses vertical near top
s1 = [(200, 70), (180, 80), (160, 92), (135, 108), (110, 122), (85, 138)]
curve(s1)

# Stroke 2: short upper horizontal — sits just below stroke 1's crossing,
# from around (105,120) rightward to (195,110), slight upward slant
s2 = [(108, 122), (140, 118), (170, 114), (198, 110)]
curve(s2)

# Stroke 3: long middle horizontal — widest stroke, spans nearly full width,
# slight upward slant to the right
s3 = [(50, 175), (100, 172), (150, 168), (210, 164), (258, 160)]
curve(s3)

# Stroke 4: 竖钩 vertical hook — comes down center from top, ends with left hook
s4_down = [(155, 95), (154, 130), (153, 170), (152, 210), (151, 250), (151, 268)]
curve(s4_down)
# hook segment — small hook curving up-left
hook = [(151, 268), (142, 268), (132, 262), (126, 252)]
curve(hook)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_手.png")
img.save(out)
print("Saved:", out)
