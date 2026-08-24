# p3_char_0365_和 — G3 attempt
# 和 = 禾 (left) + 口 (right, upper-middle).
# Fresh inline render (禾 is 木 + short leading 撇 above the 横 — no clean
# bank alias for 禾, and 口 needs different scale/position than kou.py's
# standalone-radical proportions, so inlined for size control).

import math
from PIL import Image, ImageDraw

CANVAS_SIZE = 300
img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
t = ImageDraw.Draw(img)


def _px(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _line(x0, y0, x1, y1, w=6):
    a, b = _px(x0, y0)
    c, d = _px(x1, y1)
    t.line([(a, b), (c, d)], fill=(0, 0, 0), width=w)


def _pie(x0, y0, x1, y1, w_head=7.0, w_tail=1.5, bow_perp=-6.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _px(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _na(x0, y0, x1, y1, w_head=2.0, w_belly=10.0, w_tail=2.5, bow_perp=6.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 60
    u_belly = 0.7
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _px(bx, by)
        if u <= u_belly:
            w = w_head + (w_belly - w_head) * (u / u_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - u_belly) / (1 - u_belly))
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


# ---- Left: 禾 (occupies left ~50% of canvas, cx ≈ -55) ----
LX = -55
# 1) Short leading 撇 above the heng: (~top-right down-left).
_pie(x0=LX + 10, y0=110, x1=LX - 20, y1=65, w_head=6.5, w_tail=2.0, bow_perp=-4.0)
# 2) 横 across, y=50, width ~90.
_line(LX - 45, 50, LX + 45, 50, w=6)
# 3) 竖 through center from y=50 down to y=-115.
_line(LX, 50, LX, -115, w=6)
# 4) Crossing 撇, starts near (LX+15, 25) sweeps down-left.
_pie(x0=LX + 15, y0=25, x1=LX - 55, y1=-95, w_head=7.0, w_tail=1.5, bow_perp=-6.0)
# 5) Crossing 捺, starts (LX-5, 15) sweeps down-right into right area.
_na(x0=LX - 5, y0=15, x1=LX + 55, y1=-95, w_head=2.5, w_belly=10.0, w_tail=3.0, bow_perp=6.0)

# ---- Right: 口 (middle-right, cx ≈ 70, cy ≈ 0) ----
# Box roughly 70w x 65h — sized to match 禾's vertical center presence.
RX_L, RX_R = 35, 108
RY_T, RY_B = 40, -30
# Left 竖 (slightly angled inward at bottom for calligraphy).
_line(RX_L, RY_T - 2, RX_L + 2, RY_B, w=6)
# Top 横 into right 竖 (heng_zhe) — top horizontal then down.
_line(RX_L - 2, RY_T, RX_R, RY_T, w=6)
_line(RX_R, RY_T, RX_R - 3, RY_B, w=6)
# Bottom 横 closing the box.
_line(RX_L, RY_B, RX_R - 1, RY_B, w=6)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0365_和/01_和.png"
)
