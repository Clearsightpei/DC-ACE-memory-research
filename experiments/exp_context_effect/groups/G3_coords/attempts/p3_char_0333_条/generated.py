# p3_char_0333_条 — 条 (tiáo), 7 strokes: 夂 top + 木 bottom
# Revised: better layout, 夂 in upper 45%, 木 cleanly below.

import math
from PIL import Image, ImageDraw

CANVAS = 300

def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy

def line(t, x0, y0, x1, y1, w=5):
    p0 = _to_pixel(x0, y0)
    p1 = _to_pixel(x1, y1)
    t.line([p0, p1], fill=(0, 0, 0), width=w)

def curve(t, x0, y0, x1, y1, bow_perp=0.0, w_head=6.0, w_tail=2.0, n=60):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)

def na_curve(t, x0, y0, x1, y1, bow_perp=6.0, w_head=2.0, w_belly=10.0, w_tail=2.0, n=70):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    u_belly = 0.7
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
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

def draw_tiao():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # ========== TOP 夂 (upper zone, y from +115 down to +5) ==========
    # Stroke 1: 撇 — from upper-right area angling down-left
    curve(t, x0=15, y0=115, x1=-55, y1=45, bow_perp=-4.0, w_head=6, w_tail=2)

    # Stroke 2: 横撇 — small horizontal then dropping pie
    line(t, -35, 95, 30, 95, w=5)
    curve(t, x0=30, y0=95, x1=-5, y1=35, bow_perp=-3.0, w_head=5, w_tail=2)

    # Stroke 3: 捺 — long diagonal from mid area sweeping down to bottom-right
    na_curve(t, x0=-5, y0=95, x1=110, y1=-100, bow_perp=8.0,
             w_head=2, w_belly=9, w_tail=2)

    # ========== BOTTOM 木 (lower zone, y from -15 down to -110) ==========
    # 横 — horizontal, centered in lower area
    line(t, -75, -20, 60, -20, w=5)
    # 竖 — vertical, from just above heng down to bottom
    line(t, -5, 5, -5, -110, w=5)
    # 撇 — from heng-shu crossing down to lower-left
    curve(t, x0=-5, y0=-20, x1=-85, y1=-115, bow_perp=-5.0, w_head=5, w_tail=2)
    # 捺 — small na to right of shu (short since main na from 夂 already covers right side)
    na_curve(t, x0=-5, y0=-20, x1=60, y1=-100, bow_perp=5.0,
             w_head=2, w_belly=7, w_tail=2)

    img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0333_条/01_条.png")

if __name__ == "__main__":
    draw_tiao()
