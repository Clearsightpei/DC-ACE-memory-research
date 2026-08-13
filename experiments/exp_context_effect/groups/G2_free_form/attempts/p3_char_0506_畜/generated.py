"""
p3_char_0506_畜 — top-bottom compound: 亠 (dot + long horiz) + 幺 (two small
curls) + 田 (口 with 十 inside). ~10 strokes.

Applies calligraphic 4-move: teardrop taper on 点, bezier on curves, shoulder
dabs at 折 corners, correct hook flicks. Components touch (top 亠 sweep covers
田 width; 幺 tucks into top).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab(xy, r):
    x, y = xy
    d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def stroke(pts, widths):
    """Sample ellipses along polyline with interpolated radius."""
    n = len(pts)
    if isinstance(widths, (int, float)):
        widths = [widths] * n
    elif len(widths) == 2 and n != 2:
        w_start, w_end = widths
        widths = [w_start + (w_end - w_start) * i / (n - 1) for i in range(n)]
    for i in range(n - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        dx, dy = x1 - x0, y1 - y0
        dist = max(1, (dx * dx + dy * dy) ** 0.5)
        steps = max(2, int(dist))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = (w0 * (1 - t) + w1 * t) / 2.0
            dab((x, y), r)

def bez(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3*u**2*t*p1[0] + 3*u*t**2*p2[0] + t**3*p3[0]
        y = u**3 * p0[1] + 3*u**2*t*p1[1] + 3*u*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

# ---- 亠 top ----
# 点 (dot at top, small teardrop tilting down-right)
stroke([(150, 24), (161, 40)], [3, 9])

# 长横 (long horizontal — bracketing the whole width, slight bow)
stroke([(70, 60), (235, 58)], [5, 6])
dab((235, 58), 4)

# ---- 幺 (two small triangular curls) ----
# left curl: 撇折 — pie going down-left then a short 提/折 back to right
p = bez((132, 74), (120, 88), (108, 100), (128, 108), n=30)
stroke(p, [5, 4])
stroke([(128, 108), (145, 105)], [4, 3])

# right curl mirrored, slightly lower
p = bez((160, 78), (176, 92), (188, 106), (170, 116), n=30)
stroke(p, [5, 4])
stroke([(170, 116), (185, 114)], [4, 3])

# small central 点 anchoring 幺 to 田
dab((152, 128), 4)

# ---- 田 (bottom rectangle with 十 inside) ----
LX, RX, TY, BY = 88, 218, 145, 265
# left 竖
stroke([(LX, TY), (LX, BY)], [7, 6])
# top 横 + 折 down (single continuous 横折)
stroke([(LX, TY), (RX, TY)], [7, 7])
dab((RX, TY), 5)  # shoulder dab at 折
stroke([(RX, TY), (RX, BY)], [7, 6])
# bottom 横 (closing)
stroke([(LX, BY), (RX + 3, BY)], [6, 6])

# inner 十: 竖 then 横
MX = (LX + RX) // 2
MY = (TY + BY) // 2
stroke([(MX, TY + 4), (MX, BY - 4)], [5, 5])
stroke([(LX + 4, MY), (RX - 4, MY)], [5, 5])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0506_畜/01_畜.png")
