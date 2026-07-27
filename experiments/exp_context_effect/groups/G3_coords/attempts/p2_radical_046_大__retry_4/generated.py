"""p2_radical_046_大 (dà) — retry #4

# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   FAIL mode SAME across retries: "heng + crossing pie+na still don't
#   converge on heng midpoint". Fix table (B4->B5): "apex at heng-midpoint
#   pixel FIRST, then kiss_apex". ALSO retry_3 nearly worked geometrically
#   but violated P12 (calligraphic heavy widths ~10 vs MMH GT ~4-5 thin
#   uniform). Back-port learning from wu_char (lighter widths).
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   X-crossing family (大, 人, 入, 火, 犬, 父) — the specific 大 recipe
#   is "heng first, then pie head starts ABOVE heng with a small entry
#   tick (顿笔), sweeps through heng midpoint to lower-left; na starts
#   ON the pie shaft slightly above the heng (apex-kiss on pie shaft,
#   NOT on heng), sweeps to lower-right with a foot flick." Widths:
#   for MMH radical GT (thin lines), use w~4-5 uniform, NOT calligraphic
#   variant_pie/na defaults.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - kiss_apex: applicable but retry_3 already did it manually
#     (pie starts above heng, na starts on pie shaft above heng).
#     Reusing the manual weld here because we need the pie head to be
#     ABOVE the heng, not AT the heng crossing.
#   - Per-stroke form: use thin uniform widths (P12) — this is the
#     PRIMARY new lever for retry_4. Widths 4-5 uniform, not tapered
#     to 10px belly.
#   Approach: inline PIL rendering with the retry_3 geometry but
#   MMH-thin widths and a small entry tick on 撇.

Retry_3 got the geometry roughly right (heng midpoint crossed properly,
apex-kiss on pie shaft). Two things to fix for retry_4:
  1. WIDTHS: retry_3 used w_belly=10 for na, w_head=7 for pie — too
     calligraphic. GT is thin uniform ~4-5px throughout. Match GT.
  2. 撇 ENTRY TICK: GT shows a small hook/顿笔 at the top of 撇 pointing
     down-left. retry_3 had a plain tapered head. Add a 3-4px tick.
"""
from PIL import Image, ImageDraw


W, H = 300, 300


def _tapered_bezier(draw, x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
                    w_head=5, w_tail=5, belly_pos=1.0, w_belly=None, n=80):
    """Quadratic tapered bezier in PIL pixels."""
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
    # ---- 1. 横 (heng): thin horizontal, spans wide.
    # GT: from ~x=70 to ~x=225, y ~ 138, roughly flat / very slight rise.
    # Uniform thin ~5px per P12 (MMH GT).
    _tapered_bezier(draw, 65, 142, 228, 138,
                    ctrl_perp=0.0, ctrl_along=0.0,
                    w_head=5, w_tail=5, n=40)

    # ---- 2. 撇 (pie): head at top with small 顿笔 tick, sweeps down
    # through heng midpoint (~150, 140), continues to lower-left tail.
    # GT head y ~ 55-65, tail y ~ 260, tail x ~ 60. Uniform thin ~5px
    # tapering slightly to 3 at tail. Curvature: gentle left bow.
    # Head at (158, 62), through (150, 140) approx, tail (60, 262).
    #
    # Smaller subtler 顿笔 tick at the top: short tick from (166, 58)
    # to (160, 66), pointing down-left. Kept short so it merges with
    # the main body rather than reading as a separate protrusion.
    _tapered_bezier(draw, 166, 58, 160, 66,
                    ctrl_perp=0.0, ctrl_along=0.0,
                    w_head=3, w_tail=5, n=10)

    # Main 撇 body from (160, 63) down-left through (150,140) to (60,262).
    # ctrl_perp negative -> curve bulges to the LEFT of the chord (as
    # viewed going head->tail down-left). Widths uniform-thin.
    _tapered_bezier(draw, 160, 63, 60, 262,
                    ctrl_perp=-10, ctrl_along=0,
                    w_head=5, w_tail=3, n=90)

    # ---- 3. 捺 (na): starts on the pie shaft slightly ABOVE the heng
    # (apex-kiss on the pie shaft, not on the heng). Head at ~(155, 108),
    # sweeps down-right with a subtle belly bow, ending in a foot at
    # (245, 255). Widths thin-uniform ~4-5 (NOT calligraphic 10).
    _tapered_bezier(draw, 155, 108, 245, 255,
                    ctrl_perp=6, ctrl_along=0,
                    w_head=3, w_tail=4, n=80)

    # Short 捺 foot flick — small outward tick at the tail, thin.
    _tapered_bezier(draw, 245, 255, 262, 250,
                    ctrl_perp=0, ctrl_along=0,
                    w_head=4, w_tail=2, n=15)


def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_da(draw)
    out = "01_大.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
