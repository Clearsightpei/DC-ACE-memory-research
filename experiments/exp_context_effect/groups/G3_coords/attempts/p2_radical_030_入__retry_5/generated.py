# p2_radical_030_入 — retry #5 (B7 v8 — bank REFERENCE ONLY, trust GT)
#
# RETRY MEMORY CHECKLIST
# Q1 (errata): 入 has failed r1..r4. B5 postmortem says X-crossing helpers
#   (kiss_apex + pie_point) with u_pie=0.30 kept producing shapes read as
#   symmetric 人 rather than 入. Fix idea: under v8, ABANDON kiss_apex
#   abstraction (it enforces head-on-shaft geometry that the GT does not
#   actually show); inline-fresh two thin curves per what the GT shows.
# Q2 (form_catalog): X-crossing rows exist but they parameterize an apex
#   kiss with na starting ON the pie shaft. GT for 入 shows na head
#   slightly BELOW-RIGHT of the pie apex, not on the shaft midpoint —
#   the catalog abstraction is the wrong abstraction for 入 specifically.
# Q3 (helpers): None. Per drawer_memory.md v8 guidance and B5 lesson
#   (丷 graduated by REJECTING the recommended helper), rendering
#   fresh with thin PIL curves that mirror the GT silhouette.
#
# GT observations (from /gt/phase2/入.png):
#   - Pie: top apex ~ (155, 85), curves DOWN-LEFT to ~ (60, 240),
#     with a modest leftward bow.
#   - Na: head ~ (168, 108) — slightly below-right of pie apex, NOT
#     on the shaft — sweeps DOWN-RIGHT to ~ (230, 225), gentle sag.
#   - Line weight uniform thin (~ 4-5 px), MMH style, not calligraphic.

import os
from PIL import Image, ImageDraw


def _bezier_pts(p0, p1, p2, n=64):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _stroke(draw, p0, p1, p2, width=5, n=80):
    pts = _bezier_pts(p0, p1, p2, n=n)
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill="black", width=width)
    # round end caps
    for p in (pts[0], pts[-1]):
        r = width / 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")


def draw_ru(draw):
    """入 radical, 2 strokes. Image coords (top-left origin, +y down).

    Fresh render — no bank helper. Two thin quadratic bezier strokes
    matching the GT silhouette:
      1. Pie (撇): apex top-center, down-left to bottom-left corner,
         gentle leftward bow.
      2. Na (捺): head slightly below-right of pie apex (does NOT sit
         on the pie shaft), down-right to lower-right, gentle sag.
    """
    # Stroke 1: pie
    pie_start = (155, 85)
    pie_ctrl  = (100, 175)   # pulls curve leftward
    pie_end   = (60, 240)
    _stroke(draw, pie_start, pie_ctrl, pie_end, width=5, n=100)

    # Stroke 2: na — head sits ON the pie shaft just below the apex
    # (revision: retry_5 first pass had na fully separated from pie; GT
    # shows a clear kiss where na head touches the pie shaft ~20px below
    # apex; move na head left onto the shaft).
    na_start = (148, 115)
    na_ctrl  = (200, 160)    # gentle sag / arc
    na_end   = (232, 226)
    _stroke(draw, na_start, na_ctrl, na_end, width=5, n=100)


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    draw_ru(d)
    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_入.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
