# p3_char_0197_矢 — retry_1 (v9 visual-diff, referencing bank #201 大_char.py recipe)
#
# VISUAL DIFF (prior attempts/p3_char_0197_矢/01_矢.png vs gt/phase3/矢.png)
#
# Prior render shows:
#   - Top nick: a small pie + a short upper heng. OK-ish but the pie
#     ended too far left and the short heng was tilted; upper "nick"
#     reads a bit disconnected. Weight ~5-6 px calligraphic.
#   - Middle heng: horizontal-ish, y≈155, OK-ish.
#   - Bottom X: pie and na both ORIGINATE from ~(150, 150)-(150, 156),
#     i.e. AT/ABOVE the middle heng — apex-through-line pattern.
#     Symmetric X apex; both legs descend from ABOVE the heng.
#   - Widths ~7-8 px, calligraphic look, not MMH-thin.
#
# GT shows (matching the 大-family lesson in bank #201):
#   - Top nick: short pie curling down-left (~155,58 → ~118,90) + a
#     small heng emerging from the pie neck rightward (~118,92 →
#     ~195,90). Thin ink.
#   - Middle heng: thin, slight up-right tilt (~62,155 → ~232,148),
#     ~4 px.
#   - Long pie: ONE continuous curved stroke. Starts a bit ABOVE the
#     middle heng (top head ~(160, 128)), passes through the crossing
#     on the middle heng (~150, 152), sweeps out to lower-left
#     (~65, 268). Tapered head-thick to tail-thin.
#   - Long na: SEPARATE stroke starting AT the crossing on the middle
#     heng (~150, 152) — NOT above it — sweeping down-right with belly
#     to lower-right (~245, 268). Thin head, tapered belly.
#   - All ink thin ~4 px per P12/MMH GT convention.
#
# Concrete gaps to fix (>=2):
#   (a) APEX POSITION: prior placed both pie head AND na head at/above
#       the middle heng making a symmetric X apex. Fix: pie is ONE
#       continuous curve passing THROUGH the crossing on the heng (top
#       above, tail below-left); na is a SEPARATE stroke ORIGINATING
#       AT the crossing on the heng. Bank #201 recipe verbatim.
#   (b) LINE WEIGHT: prior ~7 px calligraphic. GT is thin ~4 px MMH
#       weight. Drop widths throughout.
#   (c) TOP NICK CONNECTIVITY: prior top pie ended at (125,92) and
#       heng started at (115,102) — 10 px gap looks disconnected.
#       Land the heng near the pie's neck (~120, 92).
#
# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): "apex needs to sit ON the middle heng, not above" —
#   the 大-family bottom-X failure mode. Same lesson as 大 retry_5
#   rerun graduate (bank #201). Pie continuous through crossing;
#   na originates at crossing.
# Q2 (form_catalog): X-crossing family (大/人/入/矢/失/乔). Under v8
#   trust GT: pie is one continuous curve, na is separate starting
#   AT the crossing.
# Q3 (helpers): kiss_apex REJECTED (B5 lesson — helper contradicts
#   GT here). Hand-render tapered bezier strokes at MMH-thin ~4 px,
#   directly mirroring bank #201's tapered_polyline + cubic_pts recipe.

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(points, w_head=4.0, w_tail=3.5):
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


def quad_pts(p0, p1, p2, steps=50):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        out.append((x, y))
    return out


def draw_shi(dr):
    """矢 in PIL pixel coords (y-down), MMH-thin ~4 px, bank #201 recipe.

    Strokes (5):
      1. Top short pie (curl down-left from top)
      2. Top short heng (from pie neck outward to the right)
      3. Middle heng (main horizontal, slight up-tilt)
      4. Long pie (continuous curve: above middle heng -> crossing on
         heng -> lower-left)
      5. Long na (separate, starts AT the crossing on the middle heng
         -> lower-right)
    """
    # --- middle heng geometry (used by pie + na to anchor crossing) ---
    heng_left = (62, 156)
    heng_right = (232, 148)
    # crossing pixel: pie descends through here, na originates here
    cross = (150, 152)

    # --- top nick geometry ---
    # short pie curls from top-right down to left
    pie_top_start = (160, 60)
    pie_top_neck = (140, 82)
    pie_top_end = (118, 96)
    # short upper heng emerges near the pie neck rightward
    heng_top_left = (118, 90)
    heng_top_right = (200, 88)

    # --- long pie: one continuous curve ---
    # short section above heng (small tick above), then long body
    # descending through cross to lower-left corner
    pie_top_above = (163, 128)   # top of the shaft, slightly above cross
    pie_tail_ctrl = (100, 220)   # bow left
    pie_tail_end = (60, 268)

    # --- long na: from crossing, sweeps down-right with belly ---
    na_head = (cross[0] + 2, cross[1] + 2)
    na_ctrl1 = (180, 195)
    na_ctrl2 = (222, 240)
    na_tail = (250, 270)

    # 1. top pie (short curl down-left, MMH-thin)
    seg1 = quad_pts(pie_top_start, pie_top_neck, pie_top_end, steps=40)
    tapered_polyline(seg1, w_head=4.0, w_tail=2.8)

    # 2. top heng (thin, near-horizontal)
    tapered_polyline([heng_top_left, heng_top_right],
                     w_head=3.5, w_tail=3.8)

    # 3. middle heng (thin, slight up-tilt right)
    tapered_polyline([heng_left, (150, 153), heng_right],
                     w_head=3.6, w_tail=4.2)

    # 4. long pie: one continuous curve, top -> cross -> lower-left
    seg_head = quad_pts(pie_top_above, (158, 138), cross, steps=30)
    seg_body = cubic_pts(cross, (135, 190), pie_tail_ctrl, pie_tail_end,
                         steps=80)
    tapered_polyline(seg_head, w_head=4.0, w_tail=4.4)
    tapered_polyline(seg_body, w_head=4.4, w_tail=2.4)

    # 5. long na (separate, starts AT crossing, sweeps down-right)
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(na_seg, w_head=3.0, w_tail=5.0)


draw_shi(draw)

out_path = ("<REPO_ROOT>/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0197_矢__retry_1/01_矢.png")
img.save(out_path)
print(f"wrote {out_path}")
