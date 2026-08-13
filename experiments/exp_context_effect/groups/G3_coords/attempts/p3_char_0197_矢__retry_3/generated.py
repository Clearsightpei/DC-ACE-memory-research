"""
p3_char_0197_矢 — retry_3

# TRAJECTORY DIFF (main / retry_1 / retry_2 all FAIL vs GT)
#
# GT (矢, 5 strokes):
#   1. Top 短撇: small tapered curl near top-center, starting around
#      (140, 55) sweeping down-left to about (108, 90). Head is a
#      small back-hook to the right; tail sweeps down-left.
#   2. Short 横: sits just below+right of the top pie's tail. Spans
#      about x=110..200, y ~ 95..90 (slight up-right tilt). Thin.
#   3. Long 横: the main crossbar, spans about x=48..248, y ~ 152..146
#      (slight up-right tilt). Thin ~4 px.
#   4. 撇: ONE continuous curve — starts above long heng near its
#      midpoint (~x=150, y=118), passes THROUGH the long-heng crossing,
#      then sweeps to lower-left corner (~66, 268).
#   5. 捺: SEPARATE stroke. Head sits AT the pie/long-heng crossing
#      on the long heng, sweeps down-right to (~245, 262). Belly bows
#      downward.
#
# Prior FAILS:
#   - main / retry_1: only 4 strokes (missing the second heng), top was
#     a scribble cluster.
#   - retry_2: 5 strokes, but top 撇 sat too high and too far right
#     (starts at x=162, above where the short heng ends at x=196), so
#     the top pie visually leans OUTSIDE the short heng rather than
#     tucking above its left end. Also the top pie tail (140,84) is
#     nearly the same y as the short heng, making them run into each
#     other instead of showing the clean tuck seen in GT.
#
# Fixes for retry_3 — copy the 大_char.py recipe verbatim for the
# BOTTOM body (bank #—see success_bank/code/da_char.py), then add:
#   (a) Top 短撇: centered around x=140 (not 162), starts ~y=55, tail
#       ~ (108, 90). Small head-hook to the right, then sweep down-left.
#       This puts the pie tail to the LEFT of the short heng's left
#       end (GT signature: the pie tail dives INTO the space above the
#       short heng from above-left).
#   (b) Short heng: (110, 96) -> (200, 90), slight up-right tilt, thin
#       ~4 px.
#   (c) Long heng: identical to 大's heng, but shifted down a bit to
#       give room for the top pie + short heng above.
#   (d) 撇 + 捺 (bottom body): 大_char.py recipe with long heng at
#       y≈152 (so shift pie/na down accordingly).

# RETRY MEMORY CHECKLIST
# Q1 (errata): 矢 is X-crossing family. drawer_memory B7 note points at
#   大_char.py as the KNOWN-SOLVABLE template. Do NOT re-invent — copy.
# Q2 (form_catalog): X-crossing family uses one continuous pie curve
#   above/through the long heng; na is a separate stroke starting AT
#   the pie/heng crossing pixel.
# Q3 (helpers): REJECT kiss_apex (helper apex geometry contradicts GT).
#   Hand-render tapered bezier per 大_char.py, plus a top 撇 + short
#   heng for the 矢-specific head.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(points, w_head=4.5, w_tail=3.5):
    if len(points) < 2:
        return
    seg_len = []
    total = 0.0
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        d = math.hypot(dx, dy)
        seg_len.append(d)
        total += d
    covered = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        L = seg_len[i]
        if L <= 0:
            continue
        steps = max(2, int(L * 2))
        for s in range(steps + 1):
            u_local = s / steps
            u_global = (covered + u_local * L) / max(1e-6, total)
            w = w_head * (1 - u_global) + w_tail * u_global
            x = x0 + (x1 - x0) * u_local
            y = y0 + (y1 - y0) * u_local
            _stamp(x, y, w / 2)
        covered += L


def cubic_pts(p0, p1, p2, p3, steps=80):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0]
             + 3 * (1 - u) * u ** 2 * p2[0] + u ** 3 * p3[0])
        y = ((1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1]
             + 3 * (1 - u) * u ** 2 * p2[1] + u ** 3 * p3[1])
        out.append((x, y))
    return out


def draw_shi(dr):
    """
    矢 in PIL pixel coords (y grows DOWN). 5 strokes:
      (1) top 短撇  — tapered curl near top-center
      (2) short 横 — thin, tilted up-right
      (3) long 横  — main crossbar (大's heng, shifted down)
      (4) 撇       — continuous curve through crossing to lower-left
      (5) 捺       — separate stroke from crossing to lower-right
    Thin ~4 px MMH ink weight throughout.
    """

    # (1) Top 短撇 — small curl heading down-left, centered ~ x=140.
    pie_top_start = (146, 52)
    pie_top_ctrl1 = (150, 62)   # slight right-hook at head
    pie_top_ctrl2 = (128, 78)   # bow to the left
    pie_top_end   = (106, 92)
    top_pie = cubic_pts(pie_top_start, pie_top_ctrl1,
                        pie_top_ctrl2, pie_top_end, steps=50)
    tapered_polyline(top_pie, w_head=3.6, w_tail=2.4)

    # (2) Short 横 — tucks under the top pie's tail; slight up-right tilt.
    short_heng_L = (108, 108)
    short_heng_R = (208, 100)
    tapered_polyline([short_heng_L, (155, 104), short_heng_R],
                     w_head=3.4, w_tail=4.0)

    # (3) Long 横 — 大's crossbar, shifted down to y~152 to fit top.
    heng_left  = (52, 158)
    heng_right = (248, 151)
    tapered_polyline([heng_left, (150, 155), heng_right],
                     w_head=3.5, w_tail=4.2)

    # (4) Main 撇 — 大's recipe. Top starts above heng with small
    #     rightward head-hook, curves through crossing, sweeps to LL.
    cross = (150, 155)          # on the long heng, near midpoint
    pie_top      = (156, 122)   # top of bottom-body pie, above heng
    pie_head_ctrl = (166, 134)  # small rightward head pull
    pie_neck      = (152, 152)  # come back left into crossing
    pie_tail_ctrl = (98, 220)
    pie_tail_end  = (60, 268)

    seg_head = cubic_pts(pie_top, pie_head_ctrl,
                         (156, 146), pie_neck, steps=40)
    seg_body = cubic_pts(pie_neck, (146, 175), pie_tail_ctrl,
                         pie_tail_end, steps=80)
    tapered_polyline(seg_head, w_head=3.4, w_tail=4.3)
    tapered_polyline(seg_body, w_head=4.3, w_tail=2.2)

    # (5) 捺 — separate stroke starting AT the crossing, sweeps DR.
    na_head  = (cross[0] + 2, cross[1] + 2)
    na_ctrl1 = (180, 200)
    na_ctrl2 = (222, 240)
    na_tail  = (246, 264)
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(na_seg, w_head=3.2, w_tail=5.0)


draw_shi(draw)

out_path = ("/Users/peilinwu/Documents/AI memory research/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0197_矢__retry_3/01_矢.png")
img.save(out_path)
print(f"wrote {out_path}")
