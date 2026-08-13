"""
p2_radical_046_大 — retry_5_rerun (v9 rerun after v8 un-freeze)

# VISUAL DIFF (comparing prior retry_5 PNG vs GT PNG)
#
# Prior retry_5 shows:
#   - A horizontal heng across the middle
#   - Pie+na drawn as an X whose APEX SITS ABOVE THE HENG and whose
#     legs pass THROUGH the heng, continuing to the bottom corners.
#   - Uniform, calligraphically-textured line weight (~7-9 px look).
#   - The heng has visible turtle-render stipple/seam artifacts.
# GT shows:
#   - Heng slightly tilted (right end a touch higher), thin ~4 px.
#   - A short 撇 head that rises ABOVE the heng ~ 45-55 px, curving
#     down-left, then the SAME pie continues DOWN THROUGH the heng
#     and sweeps out to lower-LEFT — one continuous curved stroke.
#   - The 捺 starts AT the pie/heng crossing point (not above it)
#     and sweeps DOWN-RIGHT to the lower-right corner. So the na is
#     BELOW the heng only; its head is ON the heng, not above.
#   - Thin, near-uniform ~4 px ink (MMH weight, per P12).
#
# Concrete gaps to fix (>=2):
#   (a) APEX POSITION: prior places the pie/na convergence ABOVE the
#       heng (making an X-through-line). GT has: pie continues past
#       the heng, and na *originates* at the crossing on the heng.
#       Move na_head to the pie/heng intersection point on the heng,
#       not above.
#   (b) LINE WEIGHT: prior ~8 px calligraphic; GT thin ~4 px MMH
#       weight. Drop widths to 4-5 px throughout (P12 violation
#       persisted across prior retries — this is the ceiling item's
#       recurring root cause).
#   (c) PIE ABOVE HENG: GT has a short curved 撇-head visible above
#       heng ~ 45 px. Prior drew a symmetric X apex tip. Draw the
#       upper section as part of the SAME continuous pie curve.

# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): The B4 rescue lever is "apex at heng-midpoint pixel
#   FIRST, then continue pie down-left; na starts at that pixel".
#   B5 terminal-freeze meta says kiss_apex helper's abstraction places
#   apex AT heng but drawer needed apex ABOVE heng (that turned out
#   backwards — GT actually has NA HEAD ON HENG, not above; the
#   PIE goes above heng but comes back through the crossing).
# Q2 (form_catalog): X-crossing family (大/人/入) rows recommend
#   variant_pie/variant_na with an explicit shared pixel. Under v8,
#   we trust GT over the helper: pie is ONE continuous curve
#   (top-above-heng -> through crossing -> lower-left); na is a
#   SEPARATE stroke starting AT the crossing.
# Q3 (helpers): X-crossing helpers are REJECTED here (B5 lesson: when
#   helper contradicts GT, trust GT; see 丷 graduation). Hand-render
#   two continuous tapered bezier strokes at MMH-thin weight ~4 px
#   plus a thin heng.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _stamp(x, y, r):
    """Stamp a filled black disk (anti-aliasing via oversampling)."""
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(points, w_head=4.5, w_tail=3.5):
    """Draw a tapered stroke through points, width lerps head->tail
    along cumulative arc length. Uses stamped-circle rasterization."""
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


def bezier_pts(p0, p1, p2, steps=60):
    """Quadratic bezier sample points."""
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        out.append((x, y))
    return out


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


def draw_da(dr):
    """
    大 in PIL pixel coords (y grows DOWN).
    Match GT: heng slight up-right tilt; pie is one continuous curve
    starting above heng, passing through heng-crossing, sweeping to
    lower-left; na starts at the pie/heng crossing, sweeps to
    lower-right.
    """
    # --- geometry (pixel coords, y-down) ---
    heng_left = (72, 150)
    heng_right = (222, 143)   # slight up-tilt

    # Crossing pixel where pie descends through heng.
    cross = (146, 147)        # ~midpoint of heng, slight left of center

    # Pie: one continuous stroke. Top starts above heng with a
    # small backward hook to the LEFT (GT signature), curves down
    # through `cross`, then sweeps out to lower-left.
    pie_top_start = (152, 82)   # top of the character, above heng
    pie_head_ctrl = (163, 96)   # small rightward pull for the top hook curl
    pie_neck      = (152, 118)  # come back left into the shaft
    pie_tail_ctrl = (100, 210)  # bow the tail leftward
    pie_tail_end  = (66, 262)   # lower-left corner

    # Na: separate stroke starting AT the crossing on the heng,
    # sweeping down-right with a subtle belly (bows downward).
    na_head = (cross[0] + 2, cross[1] + 2)   # essentially on the crossing
    na_ctrl1 = (175, 195)
    na_ctrl2 = (215, 235)
    na_tail  = (240, 258)                    # lower-right terminus

    # --- render heng (thin, tapered) ---
    tapered_polyline([heng_left, (147, 146), heng_right],
                     w_head=3.5, w_tail=4.2)

    # --- render pie in two arcs so we can bend the top hook ---
    seg_head = cubic_pts(pie_top_start, pie_head_ctrl,
                         (158, 108), pie_neck, steps=40)
    seg_body = cubic_pts(pie_neck, (144, 145), pie_tail_ctrl,
                         pie_tail_end, steps=80)
    tapered_polyline(seg_head, w_head=3.5, w_tail=4.5)
    tapered_polyline(seg_body, w_head=4.5, w_tail=2.2)

    # --- render na (cubic, thin head -> belly -> tapered tail) ---
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(na_seg, w_head=3.2, w_tail=4.8)


draw_da(draw)

out_path = ("/Users/peilinwu/Documents/AI memory research/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p2_radical_046_大__retry_5__rerun/01_大.png")
img.save(out_path)
print(f"wrote {out_path}")
