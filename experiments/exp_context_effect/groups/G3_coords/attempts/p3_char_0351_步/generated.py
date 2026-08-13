# 步 (bù) — 7 strokes: 止 top (4) + modified 少 bottom (3).
# Inline PIL thin (~6px) recipe, bu_char-style helpers. No bank primitive
# for 止 or 少 exists; deriving fresh from GT observation.
# Structure:
#   Top 止: (1) short left vertical, (2) short right horizontal,
#            (3) main vertical, (4) long baseline heng
#   Bottom : (5) short vertical stub below baseline center,
#            (6) long pie sweeping down-left from mid-base,
#            (7) 乀-like curve (shu_wan) on right side

import math
from PIL import Image, ImageDraw


def _to_pixel(mx, my):
    return 150 + mx, 150 - my


def _heng(t, xc, yc, half_len, thickness=6):
    xL, yL = _to_pixel(xc - half_len, yc)
    xR, yR = _to_pixel(xc + half_len, yc)
    t.line([(xL, yL), (xR, yR)], fill=(0, 0, 0), width=thickness)


def _shu(t, xc, y_top, y_bot, thickness=6):
    xT, yT = _to_pixel(xc, y_top)
    xB, yB = _to_pixel(xc, y_bot)
    t.line([(xT, yT), (xB, yB)], fill=(0, 0, 0), width=thickness)


def _pie(t, x0, y0, x1, y1, w_head=8.0, w_tail=2.0, bow_perp=-8.0):
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 80
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


def _shu_wan(t, x_top, y_top, x_bot, y_bot, x_right, y_right,
             thickness=6):
    """Vertical that curves out to the right at the bottom (乀-like tail).
    Bezier control at (x_bot, y_bot); end at (x_right, y_right)."""
    n = 80
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x_top + 2 * (1 - u) * u * x_bot + u ** 2 * x_right
        by = (1 - u) ** 2 * y_top + 2 * (1 - u) * u * y_bot + u ** 2 * y_right
        px, py = _to_pixel(bx, by)
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=thickness)
        prev = (px, py)


def draw_bu_step(t):
    # === Top 止 ===
    # Stroke 1: short left vertical tick (top-left of 止)
    _shu(t, xc=-22, y_top=70, y_bot=25, thickness=6)
    # Stroke 2: short horizontal (crossbar spanning main vertical rightward)
    _heng(t, xc=15, yc=45, half_len=30, thickness=6)
    # Stroke 3: main vertical of 止 (longer, center, descends past baseline)
    _shu(t, xc=8, y_top=75, y_bot=-30, thickness=6)
    # Stroke 4: long baseline heng of 止 (wide, spans across)
    _heng(t, xc=-5, yc=-10, half_len=105, thickness=6)

    # === Bottom (少 without top-left dot) ===
    # Stroke 5: short bottom horizontal below baseline / descender tick
    # (in this glyph the main shu already descends; add a small tick if needed)
    # Stroke 6: long pie sweeping down-left from mid-baseline
    _pie(t, x0=20, y0=-25, x1=-105, y1=-120,
         w_head=8.0, w_tail=2.0, bow_perp=-14.0)
    # Stroke 7: 乀/shu_wan curve on the right — starts high, sweeps down
    # and curves right-and-up (like tail of 儿 / bottom of 少)
    _shu_wan(t,
             x_top=25, y_top=-25,
             x_bot=55, y_bot=-95,
             x_right=95, y_right=-55,
             thickness=6)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_bu_step(d)
    img.save("01_步.png")


if __name__ == "__main__":
    main()
