"""Render 龹 (p3_char_0284) to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 4  # stroke thickness

def line(x1, y1, x2, y2, w=TH):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

def poly(points, w=TH):
    d.line(points, fill=INK, width=w, joint="curve")

# Top group: small 丷 (two dots) - looks like the top of 羊/关
# Left short slanted stroke (top-left dot going down-left)
poly([(105, 80), (100, 100), (95, 115)], w=TH)
# Right short slanted stroke (top-right dot going down-right)
poly([(190, 80), (200, 100), (210, 115)], w=TH)

# Central vertical descending into the middle
# 龹 top piece resembles 类/关 top: 丷 + 天/夫-like body
# Vertical stroke
line(150, 95, 150, 165, w=TH)

# Upper horizontal (short, above middle)
line(115, 135, 185, 135, w=TH)

# Middle long horizontal (across body)
line(80, 165, 220, 165, w=TH)

# Lower body: like 八 shape (left-down and right-down strokes forming legs)
# Left leg (long diagonal down-left, curving)
poly([(150, 165), (135, 195), (110, 225), (75, 260)], w=TH)

# Right leg — like 乀 (long right-down sweep)
poly([(150, 175), (175, 200), (205, 230), (240, 260)], w=TH)


out_path = os.path.join(os.path.dirname(__file__), "01_龹.png")
img.save(out_path)
print(f"saved {out_path}")
