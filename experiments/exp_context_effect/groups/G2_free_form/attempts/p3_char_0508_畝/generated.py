"""p3_char_0508_畝 — 畝 = 亠(top) + 田(bottom-left) + 攵(right, full height)
G2 free-form render. bez + tapered stroke for curves (TIER-0 F);
straight strokes use PIL line. Components touch (TIER-0 H).
"""
from PIL import Image, ImageDraw
import os

W = 300
img = Image.new("RGB", (W, W), "white")
d = ImageDraw.Draw(img)

def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts

def taper(pts, w_start=8, w_end=4):
    """Draw variable-width polyline by dabbing ellipses at every sampled point."""
    n = len(pts) - 1
    for i, (x, y) in enumerate(pts):
        t = i / max(n, 1)
        r = (w_start * (1 - t) + w_end * t) / 2.0
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def line(p0, p1, w=7):
    d.line([p0, p1], fill="black", width=w)
    # rounded end caps
    r = w / 2.0
    for (x, y) in (p0, p1):
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---- 亠 (top) — centered over 田 (which sits on the left) ----
# 点 (small teardrop dot)
taper(bez((118, 40), (121, 46), (125, 52), (130, 60)), 3, 8)
# long 横 under it
line((55, 74), (172, 74), 7)

# ---- 田 (left, ~55% width) ----
# top 横
line((50, 92), (168, 92), 7)
# left 竖
line((52, 92), (52, 232), 8)
# right 竖
line((166, 90), (166, 232), 8)
# bottom 横
line((50, 230), (168, 230), 7)
# inner middle 横
line((54, 162), (164, 162), 6)
# inner middle 竖
line((108, 92), (108, 230), 6)

# ---- 攵 (right side) — full height, hugs 田 ----
# top short 撇 (tapered, from upper-right down-left)
taper(bez((220, 62), (212, 78), (200, 92), (185, 108)), 6, 3)
# 横 (short horizontal crossbar)
line((190, 108), (258, 104), 7)
# main long 撇 (long sweeping down-left from crossbar)
taper(bez((228, 112), (214, 150), (192, 180), (168, 220)), 9, 3)
# 捺 (S-curve sweeping down-right from the crossing point)
taper(bez((202, 158), (222, 190), (248, 225), (278, 262)), 3, 11)

out = os.path.join(os.path.dirname(__file__), "01_畝.png")
img.save(out)
print("saved:", out)
