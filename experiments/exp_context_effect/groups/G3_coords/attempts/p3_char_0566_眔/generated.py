# BANK_DEVIATION
# skipped: si_four.py (四) — its enclosure has 儿-like interior strokes, not 罒's plain vertical bars
# reason: 眔's top is 罒 (net) — wider aspect, plain internal verticals; and 眔's bottom (氺-like diverging strokes) has no clean bank match
# fresh_component: wang_net_top_for_mu (罒 rectangle with 2 inner verticals) + shui_diverge_bottom (central shu + 4 diverging strokes)

# 眔 — top 罒 (net-like rectangle, 3 windows) + bottom 氺-like (4 diverging strokes around a central shu)
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)
INK = (0, 0, 0)


def _pie(x0, y0, x1, y1, w_head=8.0, w_tail=2.0, bow_perp=-8.0):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    px, py = -dy / L, dx / L
    mx = (x0 + x1) / 2 + px * bow_perp
    my = (y0 + y1) / 2 + py * bow_perp
    prev = None
    n = 60
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (bx, by)], fill=INK, width=wi)
            r = w / 2
            d.ellipse([bx - r, by - r, bx + r, by + r], fill=INK)
        prev = (bx, by)


def _na(x0, y0, x1, y1, w_head=2.0, w_belly=10.0, w_tail=2.0, bow_perp=8.0):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    px, py = -dy / L, dx / L
    mx = (x0 + x1) / 2 + px * bow_perp
    my = (y0 + y1) / 2 + py * bow_perp
    prev = None
    n = 60
    u_belly = 0.7
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        if u <= u_belly:
            w = w_head + (w_belly - w_head) * (u / u_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - u_belly) / (1 - u_belly))
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, (bx, by)], fill=INK, width=wi)
            r = w / 2
            d.ellipse([bx - r, by - r, bx + r, by + r], fill=INK)
        prev = (bx, by)


# --- Top: 罒 (net) rectangle ---
# Wider than tall, 3 windows (2 inner vertical bars).
w = 6
x_L, x_R = 60, 235
y_T, y_B = 40, 130
# Left vertical (shu)
d.line([(x_L, y_T + 2), (x_L - 2, y_B)], fill=INK, width=w)
# Top heng
d.line([(x_L, y_T), (x_R, y_T - 2)], fill=INK, width=w)
# Right vertical (shu, slight inward slant)
d.line([(x_R, y_T - 2), (x_R - 3, y_B)], fill=INK, width=w)
# Bottom heng closing box
d.line([(x_L - 2, y_B), (x_R - 3, y_B)], fill=INK, width=w)
# Inner vertical bar 1
d.line([(118, y_T), (117, y_B)], fill=INK, width=w)
# Inner vertical bar 2
d.line([(177, y_T - 1), (177, y_B)], fill=INK, width=w)

# --- Bottom: 氺-like diverging strokes ---
# Central shu (vertical spine)
cx = 150
d.line([(cx, 140), (cx - 4, 265)], fill=INK, width=w)

# Left inner pie (short, from spine top-ish)
_pie(cx - 5, 155, 95, 210, w_head=7, w_tail=2, bow_perp=-4)

# Right inner (short 挑 or dot toward upper-right)
_pie(cx + 5, 165, 200, 205, w_head=6, w_tail=2, bow_perp=4)

# Left long pie (from mid-spine sweeping down-left)
_pie(cx - 3, 195, 68, 275, w_head=8, w_tail=2, bow_perp=-10)

# Right long na (from mid-spine sweeping down-right)
_na(cx + 3, 195, 235, 275, w_head=2, w_belly=10, w_tail=2, bow_perp=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0566_眔/01_眔.png")
