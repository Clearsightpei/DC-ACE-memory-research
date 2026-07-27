"""p2_radical_046_大 (dà) — retry #3

Retry_1 diagnosis vs GT:
  - 撇 started too LOW (y=88); GT's 撇 starts near y=60 (well above 横).
  - 撇 had a detached "entry tick" — awkward. The real 撇 is ONE continuous
    tapered curve from a THICK head (顿笔) at the top down through the
    heng crossing and out to lower-left.
  - 横 was slightly too narrow and thick; GT 横 spans ~45 to ~255, thin
    (~6 px), slight upward slant.
  - 捺's belly location OK but taper could be more graceful; foot flick
    was too small.

Retry_3 recipe (X-crossing template per fu.py, adapted for 大 = heng +
big pie + big na, NO shu):
  1. 横 (heng): thin horizontal from (45, 145) to (255, 145), slight
     upward-right tilt, thickness ~6.
  2. 撇 (pie): tapered bezier from a THICK head at (162, 62) — sitting
     above the heng — curving down through the heng crossing near
     (150, 145) and sweeping to a thin tail at (52, 268). Head width
     10, tail width 1. This is ONE stroke, no detached ticks.
  3. 捺 (na): tapered bezier starting on the pie shaft ABOVE the heng
     at (158, 105) — apex-kiss with pie per fu.py — thin head 2 px,
     belly 14 px at u=0.72, sweeping right to a foot at (258, 258).
     Then a short outward flick from the foot for the 捺's terminal.

Uses PIL pixel coordinates directly (fu.py convention) — no math-coord
conversion needed.
"""
from PIL import Image, ImageDraw


W, H = 300, 300


def _tapered_bezier(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
                    w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=70):
    """Quadratic tapered bezier in PIL pixels (fu.py's _tb helper)."""
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_da(draw):
    # 1. 横 (heng): thin horizontal spanning canvas mid-width.
    #    From (48, 148) to (252, 143) — slight up-right slant, thickness 6.
    _tapered_bezier(draw, 48, 148, 252, 143,
                    ctrl_perp=0.0, ctrl_along=0.0,
                    w_head=5, w_tail=6, n=40)

    # 2. 撇 (pie): moderate-thick head above heng, curving down through
    #    heng crossing at ~(150, 145), sweeping left to thin tail
    #    near (55, 262). ONE continuous tapered stroke.
    #    Head at (160, 65), tail at (55, 262). Lighter head (7 vs 10)
    #    so it doesn't read as a slab; more curvature (-14) for graceful
    #    left sweep.
    _tapered_bezier(draw, 160, 65, 55, 262,
                    ctrl_perp=-14, ctrl_along=0,
                    w_head=7, w_tail=1, n=80)

    # 3. 捺 (na): starts ON the pie shaft slightly above heng at
    #    (156, 110), thin head 2, belly 10 at u=0.72, ending at foot
    #    (250, 258). Slightly reduced belly & no separate foot-flick
    #    (GT 捺 is subtle at radical scale).
    _tapered_bezier(draw, 156, 110, 250, 258,
                    ctrl_perp=6, ctrl_along=0,
                    w_head=2, w_tail=2, w_belly=10, belly_pos=0.75, n=75)
    # Small terminal foot flick — very short outward-right taper
    _tapered_bezier(draw, 250, 258, 268, 253,
                    ctrl_perp=0, ctrl_along=0,
                    w_head=6, w_tail=1, n=20)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_da(draw)
    out = "01_大.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
