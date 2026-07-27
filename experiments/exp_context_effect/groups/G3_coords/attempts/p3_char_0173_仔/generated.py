# p3_char_0173_仔 — 仔 (zǐ), 5 strokes: 亻 (left) + 子 (right).
# Revised: left ren_pang from bank; right 子 INLINED (top 横钩 + wan_gou
# descender + crossing 横) at controlled pixel size, because zi_char.py
# has hard-coded pixel positions that don't shrink with `scale`.
# Layout target from GT: 亻 fills left ~35% (upper), 子 fills right ~55%
# with descender dropping to lower-mid, crossbar spanning right-half only.
import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from wan_gou import draw_wan_gou    # noqa: E402


def _inline_hengou(draw, x_l, y_l, x_r, y_r, ink=9):
    """Inline 横钩 top of 子 — heng with a downward hook at the right end."""
    steps = 24
    w_start, w_end = 4, ink
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x_l + (x_r - x_l) * t0
        ya = y_l + (y_r - y_l) * t0
        xb = x_l + (x_r - x_l) * t1
        yb = y_l + (y_r - y_l) * t1
        w = int(w_start + (w_end - w_start) * t0)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)
    r = 6
    draw.ellipse([x_r - r, y_r - r, x_r + r, y_r + r], fill="black")
    # Hook flick down-left.
    hx_end = x_r - 10
    hy_end = y_r + 28
    hx_ctrl = x_r + 1
    hy_ctrl = y_r + 16
    hsteps = 18
    for i in range(hsteps):
        u0 = i / hsteps
        u1 = (i + 1) / hsteps

        def bez(u):
            x = (1 - u) ** 2 * x_r + 2 * (1 - u) * u * hx_ctrl + u * u * hx_end
            y = (1 - u) ** 2 * y_r + 2 * (1 - u) * u * hy_ctrl + u * u * hy_end
            return x, y
        xa, ya = bez(u0)
        xb, yb = bez(u1)
        w = max(3, int(ink - (ink - 3) * u0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)


def _inline_heng(draw, x_l, y_l, x_r, y_r, ink=8):
    """Inline crossing 横 of 子."""
    steps = 16
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x_l + (x_r - x_l) * t0
        ya = y_l + (y_r - y_l) * t0
        xb = x_l + (x_r - x_l) * t1
        yb = y_l + (y_r - y_l) * t1
        draw.line([(xa, ya), (xb, yb)], fill="black", width=ink)


def draw(t, ox=0, oy=0, scale=1.0):
    # ---- 亻 on left (from bank, PASSed proportions) ----
    # ren_pang uses math-coord ox/oy (center=(150,150), +y up).
    # Shift left about -70 math-x, compress to scale 0.75.
    draw_ren_pang(t, ox=ox + (-70) * scale, oy=oy + 10 * scale,
                  scale=0.75 * scale)

    # ---- 子 on right, INLINED at pixel coordinates ----
    # Right half of canvas roughly x = 150..270. Top ~y=80, bottom ~y=245.
    # Top 横钩: horizontal bar, then downward hook.
    top_xL, top_yL = 155, 90
    top_xR, top_yR = 260, 88
    _inline_hengou(t, top_xL, top_yL, top_xR, top_yR, ink=9)

    # Descender (弯钩) — use wan_gou primitive in math-coords.
    # wan_gou natural range: y ~ +110..-95 (205 units tall in math),
    # x ~ +40..-38. At scale 0.55, height ~113 px, which spans upper-mid
    # down to lower-mid on the right side. Place its origin at math
    # (+55, +5) so the top of its arc meets the hook end (~ pixel
    # 245, 118) and the tip flicks near pixel (195, 220).
    draw_wan_gou(t, ox=ox + 55 * scale, oy=oy + 5 * scale,
                 scale=0.55 * scale)

    # Crossing 横 — spans right-side only, narrower than before.
    cross_xL, cross_yL = 148, 170
    cross_xR, cross_yR = 268, 168
    _inline_heng(t, cross_xL, cross_yL, cross_xR, cross_yR, ink=8)


def main():
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw(t)
    out = os.path.join(os.path.dirname(__file__), "01_仔.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
