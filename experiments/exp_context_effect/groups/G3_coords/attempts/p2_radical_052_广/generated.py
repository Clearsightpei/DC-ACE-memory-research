"""广 (guang, 3-stroke radical) — G3 coord-format render.

Strokes (in stroke order):
  1. 点 (dian): small dot at top-center, slightly right of vertical axis.
  2. 横 (heng): horizontal spanning right-of-center, at upper-third height.
     Left end of the heng is the joint with the pie's head.
  3. 撇 (pie): long left-falling sweep starting AT the heng's left end
     (welded corner join), curving down-left to lower-left of canvas.

Design notes (per TR1-TR7 + P1-P10):
- TR4: heng.left_end == pie.head (weld). Both computed explicitly below.
- TR5: bank pie is +65 head / -45 tail (110-px canvas-x span, 175-px y
  span). 广's pie has a shorter horizontal span but LONGER vertical drop
  than the standalone bank pie — so inline the pie curve with custom
  endpoints rather than call draw_pie() (extreme scale would distort
  taper per TR5).
- Bank dian call: dian standalone runs from (-15,+25) to (+18,-20) —
  size ~35 px. For 广's top-dot, use scale ~0.55 to shrink to ~19 px,
  positioned above and slightly LEFT of the heng's mid.
- Bank heng call: standalone heng is 200 px wide, uniform 12 px thick.
  广's heng is shorter (~120 px). Use scale 0.60 -> 120-px heng.
"""

import os
import sys
from PIL import Image, ImageDraw

# Make bank primitives importable.
BANK_CODE = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, BANK_CODE)

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_pie_inline(draw, x0, y0, x1, y1, ctrl_dx=-8.0, ctrl_dy=+15.0,
                    w_head=11.0, w_tail=1.0, n_segments=80):
    """Inline tapered pie curve with custom endpoints.

    Head at (x0,y0), tail at (x1,y1). Control point offset from chord
    midpoint by (ctrl_dx, ctrl_dy) — positive ctrl_dy bulges the belly
    UP relative to chord (for a 广/厂-style pie that curls out to the
    LOWER-LEFT, we want the belly bulging LEFT+DOWN i.e. ctrl_dx<0,
    ctrl_dy small positive to make the curve concave from the ink side).
    """
    mx = (x0 + x1) / 2.0 + ctrl_dx
    my = (y0 + y1) / 2.0 + ctrl_dy

    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            draw.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def render():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # ------------------------------------------------------------------
    # Stroke 1: 点 — top-center dot, slightly LEFT-of-heng-midpoint.
    # ------------------------------------------------------------------
    # Bank dian standalone: head (-15,+25) tail (+18,-20) at scale 1.0.
    # We want a small dot centered around math-coord (+10, +95):
    # scale 0.55 gives head (-8, +14) tail (+10, -11) — a ~25-px dot.
    # Offset by (ox=+10, oy=+95) places it near canvas top-center.
    #
    # TR3 check: dian primitive's default center ≈ (0,0). Target center
    # ≈ (+10, +95). So ox=+10, oy=+95 lands the dot centered there.
    draw_dian(draw, ox=+10.0, oy=+95.0, scale=0.55)

    # ------------------------------------------------------------------
    # Stroke 2: 横 — horizontal, ~120 px long, upper-third of canvas.
    # ------------------------------------------------------------------
    # Bank heng standalone: 200 px long at scale 1.0, centered on origin.
    # 广's heng: ~120 px long -> scale 0.60. Its horizontal center at
    # math-coord (+30, +40) puts left end at x=-30, right end at x=+90,
    # y=+40 (upper region). This leaves the left end at x=-30, which is
    # the pie's head-anchor.
    #
    # TR3 check: heng primitive's default center = (0,0). Target center
    # (+30, +40). So ox=+30, oy=+40.
    heng_scale = 0.60
    heng_center_x = +30.0
    heng_center_y = +40.0
    heng_half_len = 100.0 * heng_scale  # = 60 px in math coords
    heng_left_end_x = heng_center_x - heng_half_len   # = -30
    heng_left_end_y = heng_center_y                    # = +40
    draw_heng(draw, ox=heng_center_x, oy=heng_center_y, scale=heng_scale)

    # ------------------------------------------------------------------
    # Stroke 3: 撇 — long left-falling sweep, head welded to heng-left-end.
    # ------------------------------------------------------------------
    # TR4 weld: pie head = (heng_left_end_x, heng_left_end_y) = (-30, +40).
    # Pie tail: sweeps down-left, ending near lower-left of canvas.
    # Choose tail at (-85, -115) — 55 px left, 155 px down of head.
    # This gives a strong VERTICAL pie (广's pie is much more vertical
    # than diagonal — see sandbox 厂 diagnosis: "almost-vertical with
    # only a shallow scoop near the tail").
    # Control point offset (-8, +15): pulls belly slightly left and up,
    # so the pie is nearly straight in its upper 2/3 and curls left in
    # its lower 1/3 — matches GT silhouette.
    # Revision (self-check pass 2): GT's pie has a stronger, more
    # visible LEFT curl in its lower third. Increase leftward bow via
    # ctrl_dx=-20 and lower the belly-height slightly (ctrl_dy=+5) so
    # the curvature concentrates around the middle-to-lower portion of
    # the stroke (matches GT silhouette where the pie is straight-ish
    # for its top half then arcs left near the tail).
    pie_head = (heng_left_end_x, heng_left_end_y)          # (-30, +40)
    pie_tail = (-90.0, -115.0)
    draw_pie_inline(
        draw,
        x0=pie_head[0], y0=pie_head[1],
        x1=pie_tail[0], y1=pie_tail[1],
        ctrl_dx=-22.0,   # stronger leftward bow -> visible bottom curl
        ctrl_dy=+5.0,    # belly slightly above chord mid -> curl in bottom half
        w_head=11.0,
        w_tail=1.5,
        n_segments=90,
    )

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_广.png"
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    render()
