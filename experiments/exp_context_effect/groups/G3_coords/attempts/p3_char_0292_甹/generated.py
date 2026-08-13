"""Render 甹 (pīng) — G3 inline fresh (thin uniform lines, GT-matched).

Structure from GT:
- Small vertical hat on top (dian-like short stroke)
- Rectangular 由/甶-like top box with internal vertical descending below
- Long horizontal spanning canvas at mid-height
- Curved hook stroke (丂-like) at bottom: short heng + hooked S-curve
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 3  # thin uniform width to match MMH GT

def line(p, q, w=LW):
    d.line([p, q], fill="black", width=w)

def curve(pts, w=LW):
    # simple polyline through pts
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# --- Top: small pie-like hat (short diagonal from top-left down)
curve([(118, 55), (122, 68), (128, 80)])

# --- Rectangular box (top): 甶/由-like
# top horizontal
line((100, 82), (188, 82))
# left vertical of box
line((100, 82), (100, 148))
# right vertical of box (with tiny hook stub down implied via long heng)
line((188, 82), (188, 148))
# bottom of box
line((100, 148), (188, 148))
# internal vertical descending (from top through box, continuing down to long heng)
line((144, 82), (144, 175))
# one internal horizontal (mid-bar)
line((100, 118), (188, 118))

# --- Long horizontal spanning wide (mid-bottom)
line((45, 175), (258, 175))

# --- Bottom: 丂-like curved hook stroke
# short heng at top of bottom section
line((108, 200), (208, 200))
# vertical drop at right end
line((205, 200), (208, 218))
# S-curve descending then hooking left-up (more asymmetric, sweeping left)
curve([
    (208, 218),
    (205, 232),
    (198, 246),
    (185, 258),
    (165, 266),
    (140, 268),
    (118, 264),
    (102, 254),
    (95, 240),
], w=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_甹.png"))
print("wrote 01_甹.png", img.size)
