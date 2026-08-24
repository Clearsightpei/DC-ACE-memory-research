"""
p3_char_0197_矢 — retry_2

# TRAJECTORY DIFF (main FAIL, retry_1 FAIL vs GT)
#
# GT (矢, 5 strokes):
#   1. Short 撇 up top-left (small curl heading down-left).
#   2. Short 横 (tilted slightly up-right), sits just below the top 撇.
#   3. Long 横 (much wider than short 横), sits below the short 横
#      with visible vertical gap (~35 px between the two hengs).
#   4. 撇: one continuous curved stroke starting just above the long
#      heng, passing THROUGH the long heng near its midpoint, sweeping
#      to the lower-left corner.
#   5. 捺: separate stroke starting AT the pie/long-heng crossing,
#      sweeping down-right to lower-right corner.
#   Thin, uniform ~4 px MMH ink weight throughout.
#
# Prior main attempt (verdict FAIL):
#   - Rendered only 4 strokes: a top 厶-like squiggle, ONE heng, then
#     pie+na crossing. Missing the second heng entirely.
#   - Pie/na convergence formed an X, apex at heng — wrong topology.
#   - Ink weight uneven.
#
# Prior retry_1 (verdict FAIL):
#   - Similar 4-stroke composition, still missing the second heng.
#   - Top 撇 rendered as a scribble-cluster, not a clean single curl.
#   - Long heng was there but pie+na crossed above it, not through.
#
# Concrete fixes for retry_2:
#   (a) FIVE strokes, not four. Top 撇 + short 横 + long 横 + 撇 + 捺.
#   (b) 大-graduation recipe (B7 rerun) for the bottom body: pie is
#       ONE continuous curve above/through the long heng; na starts
#       AT the crossing (na head on heng, not above).
#   (c) MMH-thin ink ~4 px throughout (P12).
#   (d) Top 撇 as a single short tapered arc going down-left, not a
#       squiggle. Ends before the short heng starts.

# RETRY MEMORY CHECKLIST
# Q1 (errata): No dedicated 矢 entry; drawer_memory B7 note names 矢
#   in the X-crossing family, points at 大_char.py as the template
#   ("KNOWN-SOLVABLE if the drawer follows the 大 recipe").
# Q2 (form_catalog): X-crossing family — variant_pie/na with explicit
#   shared pixel; under v8 trust GT so pie is one continuous curve
#   through the crossing and na starts at the crossing pixel.
# Q3 (helpers): REJECT kiss_apex (helper apex geometry doesn't match
#   GT for 大 family). Inline tapered beziers per 大_char.py.
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
      1. top short 撇 (small curl down-left, high up)
      2. short 横 (below 撇, tilted slight up-right)
      3. long 横 (wider, below short heng — this is the crossbar)
      4. 撇 (continuous curve: above long heng -> through crossing -> LL)
      5. 捺 (starts at pie/long-heng crossing -> LR)
    Thin ~4 px MMH ink weight.
    """

    # (1) Top 短撇 — short tapered curl heading down-left
    pie_top_start = (162, 52)
    pie_top_ctrl1 = (158, 62)
    pie_top_ctrl2 = (152, 72)
    pie_top_end   = (140, 84)
    top_pie = cubic_pts(pie_top_start, pie_top_ctrl1, pie_top_ctrl2,
                        pie_top_end, steps=40)
    tapered_polyline(top_pie, w_head=3.5, w_tail=2.5)

    # (2) Short 横 — thin, sits below top pie
    short_heng_L = (118, 108)
    short_heng_R = (196, 100)   # tilted slightly up-right
    tapered_polyline([short_heng_L, (155, 104), short_heng_R],
                     w_head=3.5, w_tail=4.0)

    # (3) Long 横 — the crossbar, thin
    long_heng_L = (66, 158)
    long_heng_R = (232, 152)    # slight up-tilt
    tapered_polyline([long_heng_L, (150, 155), long_heng_R],
                     w_head=3.5, w_tail=4.2)

    # (4) Main 撇 — continuous curve, top above long heng, through
    #     crossing at long heng midpoint, sweep to lower-left corner.
    cross = (150, 155)                  # on the long heng
    pie_start = (162, 122)              # just above short-heng bottom / gap
    pie_ctrl_top = (158, 138)           # small right-lean before entering heng
    pie_neck = (150, 155)               # exactly at crossing
    pie_ctrl_body = (100, 220)
    pie_end = (58, 270)                 # lower-left

    seg_head = cubic_pts(pie_start, pie_ctrl_top, (152, 148), pie_neck,
                         steps=30)
    seg_body = cubic_pts(pie_neck, (140, 175), pie_ctrl_body, pie_end,
                         steps=80)
    tapered_polyline(seg_head, w_head=3.2, w_tail=4.2)
    tapered_polyline(seg_body, w_head=4.2, w_tail=2.2)

    # (5) 捺 — starts AT the crossing on the long heng, sweeps down-right
    na_head = (cross[0] + 2, cross[1] + 2)
    na_ctrl1 = (180, 200)
    na_ctrl2 = (220, 240)
    na_tail = (248, 268)
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(na_seg, w_head=3.2, w_tail=5.0)


draw_shi(draw)

out_path = ("<REPO_ROOT>/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0197_矢__retry_2/01_矢.png")
img.save(out_path)
print(f"wrote {out_path}")
