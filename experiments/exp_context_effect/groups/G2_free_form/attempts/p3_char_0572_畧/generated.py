"""
p3_char_0572_畧 — top-bottom compound: 田 (top) + 各 (bottom).
各 = 夂 (top) + 口 (bottom). ~11 strokes total.

Applies calligraphic 4-move: teardrop taper on 撇/捺, bezier on curves,
shoulder dabs at 折 corners. Components touch (田 bottom overlaps 各 top).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(xy, r):
    x, y = xy
    d.ellipse([x - r, y - r, x + r, y + r], fill="black")


def stroke(pts, widths):
    n = len(pts)
    if isinstance(widths, (int, float)):
        widths = [widths] * n
    elif len(widths) == 2 and n != 2:
        w0, w1 = widths
        widths = [w0 + (w1 - w0) * i / (n - 1) for i in range(n)]
    for i in range(n - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        r0, r1 = widths[i] / 2.0, widths[i + 1] / 2.0
        dx, dy = x1 - x0, y1 - y0
        dist = max(1, (dx * dx + dy * dy) ** 0.5)
        steps = max(2, int(dist))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = r0 * (1 - t) + r1 * t
            dab((x, y), r)


def bez(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3*p0[0] + 3*u**2*t*p1[0] + 3*u*t**2*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u**2*t*p1[1] + 3*u*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts


# ==== 田 top ====
LX, RX, TY, BY = 95, 205, 28, 132
# left 竖
stroke([(LX, TY), (LX, BY)], [7, 6])
# top 横 continuing to 折 (right 竖)
stroke([(LX, TY), (RX, TY)], [7, 7])
dab((RX, TY), 5)
stroke([(RX, TY), (RX, BY)], [7, 6])
# bottom 横 (closing)
stroke([(LX - 2, BY), (RX + 2, BY)], [6, 6])
# inner 十: 竖 then 横
MX = (LX + RX) // 2
MY = (TY + BY) // 2
stroke([(MX, TY + 4), (MX, BY - 4)], [5, 5])
stroke([(LX + 4, MY), (RX - 4, MY)], [5, 5])

# ==== 各 bottom ====
# --- 夂 ---
# 撇 (long sweeping pie from top-right going down-left, teardrop taper)
p = bez((175, 138), (160, 165), (135, 190), (78, 235), n=50)
stroke(p, [8, 3])

# 横撇 (short horiz then a small pie) — starts on the 撇 upper stem,
# going right then hooking down-left slightly
stroke([(120, 168), (185, 168)], [5, 6])
dab((185, 168), 4)  # shoulder dab
p = bez((185, 168), (180, 180), (170, 190), (150, 205), n=30)
stroke(p, [6, 3])

# 捺 (long sweep from around the fold going down-right with foot flare)
p = bez((150, 185), (175, 210), (200, 232), (232, 248), n=50)
stroke(p, [5, 10])
# foot flare
stroke([(232, 248), (245, 245)], [10, 4])

# --- 口 (bottom small rectangle) ---
lx, rx, ty, by = 118, 192, 232, 285
# left 竖
stroke([(lx, ty), (lx, by)], [6, 5])
# top 横 then 折 down
stroke([(lx, ty), (rx, ty)], [6, 6])
dab((rx, ty), 5)
stroke([(rx, ty), (rx, by)], [6, 5])
# bottom 横
stroke([(lx - 2, by), (rx + 2, by)], [5, 5])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0572_畧/01_畧.png")
