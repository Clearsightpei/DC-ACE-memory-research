# p3_char_0009_了 — G3 (coord-bank)
#
# 了 decomposes into 2 strokes:
#   1) 横钩 (horizontal + downward hook) at top — INLINED
#      because we need explicit control over hook direction/length.
#   2) 弯钩 (long curved hook descender) below — uses bank wan_gou.py
#
# Redraw against clean regenerated GT (previous GT was corrupted).
# GT observation (clean):
#   - Top: horizontal stroke spanning left-mid to right-mid area,
#     slight rise (right end a bit higher), ending in a clear
#     down-curl hook.
#   - Bottom: long S-like curved descender starting just below the
#     top's right end, sweeping down, ending in a leftward hook flick
#     at the very bottom.

from PIL import Image, ImageDraw
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

from wan_gou import draw_wan_gou   # math coord primitive; center (150,150)


def draw_top_hengou(draw, x_left, y_left, x_right, y_right, ink=11):
    """Inline 横钩: horizontal (tapered) then a down hook curl.
    Horizontal from (x_left, y_left) to (x_right, y_right)."""
    # Tapered horizontal: thin start, thicker at right (顿笔)
    steps = 24
    w_start, w_end = 5, ink
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x_left + (x_right - x_left) * t0
        ya = y_left + (y_right - y_left) * t0
        xb = x_left + (x_right - x_left) * t1
        yb = y_left + (y_right - y_left) * t1
        w = int(w_start + (w_end - w_start) * t0)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)
    # 顿笔 blob at corner
    r = 7
    draw.ellipse([x_right - r, y_right - r, x_right + r, y_right + r], fill="black")
    # Hook: down and slightly left, curved (quadratic bezier)
    hx_end = x_right - 14
    hy_end = y_right + 38
    hx_ctrl = x_right + 2
    hy_ctrl = y_right + 22
    hsteps = 20
    for i in range(hsteps):
        u0 = i / hsteps
        u1 = (i + 1) / hsteps
        def bez(u):
            x = (1-u)**2 * x_right + 2*(1-u)*u * hx_ctrl + u*u * hx_end
            y = (1-u)**2 * y_right + 2*(1-u)*u * hy_ctrl + u*u * hy_end
            return x, y
        xa, ya = bez(u0)
        xb, yb = bez(u1)
        w = max(3, int(ink - (ink - 3) * u0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)


def draw_liao(draw, ox=0, oy=0, scale=1.0):
    # Top 横钩 inline — spans a wide upper region
    # GT shows the horizontal stretches from ~x=60 to ~x=200 in upper canvas
    x_l = 60 + ox
    y_l = 85 + oy
    x_r = 205 + ox
    y_r = 80 + oy   # slight rise to right
    draw_top_hengou(draw, x_l, y_l, x_r, y_r, ink=11)

    # Bottom 弯钩 — descender hanging below the top's right area.
    # wan_gou natural body: start(5,110) end(-10,-95) math coords
    # rendered around canvas center (150,150) PIL.
    # For scale=0.95: PIL start ≈ (154.75, 45.5). We want start near
    # (180, 115). So ox_math = (180-154.75) ≈ 25;
    # oy_math offsets: PIL_y = 150 - (110*0.95 + oy) = 150 - 104.5 - oy
    # We want PIL_y ≈ 115 → oy_math ≈ -70. Hmm let's aim for start
    # PIL y ~115: 150 - (110*0.95) - oy = 115 → oy = -69.5.
    # End: math (-10,-95)*0.95 = (-9.5,-90.25) → PIL (150-9.5+25, 150+90.25-(-70))
    # = (165.5, 310) - way off canvas.
    # Reconsider: use scale ~0.85 so total descender fits.
    # scale=0.85: PIL start ≈ (154.25, 56.5). Target start (180, 118).
    # ox = 26, oy: 150 - 93.5 - oy = 118 → oy = -61.5.
    # End: math (-8.5, -80.75) → PIL (150-8.5+26, 150+80.75+61.5)
    # = (167.5, 292.25). Reaches bottom-ish. Good.
    # Hook tip: math (-38,-75)*0.85 = (-32.3, -63.75) → PIL (150-32.3+26, 150+63.75+61.5)
    # = (143.7, 275.25). Reasonable leftward hook.
    draw_wan_gou(draw, ox=ox + 26, oy=oy - 62, scale=0.85)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_liao(draw)
    out = os.path.join(HERE, "01_了.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
