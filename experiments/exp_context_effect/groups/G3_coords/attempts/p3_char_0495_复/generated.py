# BANK_DEVIATION
# skipped: ri.py (日) and jiu_long_char.py (久)
# reason: 日 in 复 is compressed (roughly 1:1.2 aspect) and sits between the
#   top 亠 cap and the bottom 夂; ri.py bakes a tall 1:1.7 aspect at fixed
#   coords that won't slot cleanly. 夂 bottom needs 撇+捺 spanning the
#   full lower half, wider than jiu_long_char's cluster.
# fresh_component: fu_top_cap + fu_middle_ri_compact + fu_bottom_zhi

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
t = ImageDraw.Draw(img)


def tapered(t, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = w0 + (w1 - w0) * ((u0 + u1) / 2)
        t.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=max(1, int(round(w))))


def curved_pie(t, p0, p1, bow, w0, w1, steps=40):
    """Bow=perpendicular offset at midpoint (positive = right of direction)."""
    import math
    x0, y0 = p0
    x1, y1 = p1
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    mx = (x0 + x1) / 2 + nx * bow
    my = (y0 + y1) / 2 + ny * bow
    prev = p0
    for i in range(1, steps + 1):
        u = i / steps
        # quadratic bezier
        xu = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u * u * x1
        yu = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u * u * y1
        w = w0 + (w1 - w0) * u
        t.line([prev, (xu, yu)], fill=(0, 0, 0), width=max(1, int(round(w))))
        prev = (xu, yu)


# ==== Top: 亠-like cap (丿 + 一) ====
# Short 丿 top-left (starts upper-right, sweeps to lower-left)
curved_pie(t, (160, 32), (118, 82), bow=+5, w0=7, w1=2)
# Long 一 heng
tapered(t, (55, 82), (245, 78), w0=4, w1=6)

# ==== Middle: compressed 日 ====
x_l, x_r = 105, 200
y_t, y_b = 92, 180
y_mid = 138
# Left 竖
t.line([(x_l, y_t), (x_l, y_b)], fill=(0, 0, 0), width=5)
# Top 横折 (top heng + right shu)
t.line([(x_l - 2, y_t), (x_r, y_t)], fill=(0, 0, 0), width=5)
t.line([(x_r, y_t), (x_r, y_b)], fill=(0, 0, 0), width=5)
# Middle 横
t.line([(x_l + 3, y_mid), (x_r - 3, y_mid)], fill=(0, 0, 0), width=4)
# Bottom 横
t.line([(x_l - 2, y_b), (x_r, y_b)], fill=(0, 0, 0), width=5)

# ==== Bottom: 夂 (撇 + 捺 crossing) ====
# Long 撇 sweeping SW, from upper-right down to lower-left
curved_pie(t, (180, 185), (40, 285), bow=-16, w0=8, w1=2)
# Long 捺 sweeping SE — starts on the pie shaft, ends lower-right
curved_pie(t, (128, 215), (290, 280), bow=+10, w0=3, w1=13)

img.save("01_复.png")
print("Wrote 01_复.png")
