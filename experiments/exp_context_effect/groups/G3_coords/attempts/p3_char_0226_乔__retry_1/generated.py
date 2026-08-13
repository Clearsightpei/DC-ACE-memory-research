"""
p3_char_0226_乔 — retry_1

# VISUAL DIFF (prior 01_乔.png vs GT 乔.png)
#
# Prior attempt shows:
#   - A short pie above with a small stub, then a heng across at ~y=115,
#     an X-crossing of pie+na WHOSE APEX SITS ABOVE the middle heng
#     (same failure mode as pre-graduation 大: X-through-line).
#   - Bottom is a single long shu descending from the na body — no
#     clear separated bottom strokes; reads more like 亦 than 乔.
#   - Line weight uniform ~5-6 px, but the top-pie stub is disconnected
#     from the main pie (two short pieces instead of ONE continuous
#     curve above→through→below the heng).
#   - Bottom-right pie missing entirely; the top na sweeps too far
#     down doing double-duty.
# GT shows:
#   - A short 撇 at the very top (~y=55..90), a slight left-slanting
#     stub.
#   - A wide 一 (heng) across ~y=110 spanning ~80% of canvas.
#   - ONE continuous 撇: starts above the heng near the top-pie neck,
#     descends through heng at ~x=155, sweeps to lower-left corner
#     (~30, 260). Same recipe as bank #201 大 (da_char.py).
#   - A 捺 STARTING AT the crossing on the heng (not above it), sweeps
#     down-right, ending ~ (255, 175) with slight belly.
#   - Below the heng, two short bottom strokes:
#       * a 竖 (or 竖钩) at ~x=130 descending from ~y=140 to ~y=260,
#         slight hook to the left at the base.
#       * a 撇 at ~x=170 descending from ~y=140 sweeping to
#         ~(210, 255) — shorter than the main pie above.
#   - Thin, near-uniform ~4-5 px ink (MMH weight, P12).
#
# Concrete gaps to fix (≥2):
#   (a) APEX POSITION: prior places pie/na convergence ABOVE the
#       middle heng. Fix: pie is ONE continuous stroke through the
#       heng-crossing pixel; na *originates* at the crossing on the
#       heng. (Same fix as 大 graduation, per errata p3_char_0226_乔.)
#   (b) BOTTOM: prior has only one long descender. Fix: draw TWO
#       separated bottom strokes (竖 + 撇) below the heng.
#   (c) TOP: prior top-pie is disconnected. Fix: draw the top 撇 as
#       a short slanted stub whose visual rhythm reads as part of the
#       larger vertical rise, but keep it as its own stroke (GT does).

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): "6-stroke: 夭-top + 小-bottom. Drawer's top 夭 pie+na
#   crossing failed like 大. Fix: 夭 apex through top heng; bottom 小
#   needs 3 clear separated strokes." — Applied: pie continuous
#   through heng (bank #201 大 recipe); bottom drawn as separated
#   竖 + 撇.
# Q2 (form_catalog): X-crossing family (大/人/入) rows say: continuous
#   pie through the heng, na starts at the crossing. B7 v9 graduation
#   of 大 (bank #201) codifies this.
# Q3 (helpers): kiss_apex REJECTED here (B5 lesson: helper places apex
#   AT the crossing, GT has pie going ABOVE-through-BELOW). Hand-render
#   two continuous tapered bezier strokes at thin ~4-5 px, plus a thin
#   heng, plus two short bottom strokes. Same recipe class as
#   da_char.py (bank #201).
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


def draw_qiao(dr):
    """
    乔 (qiáo) — 6 strokes:
      1. top 撇 (short stub above upper heng)
      2. 一 (upper heng, wide)
      3. long continuous 撇 (above→through heng→lower-left)
      4. 捺 (starts at pie/heng crossing, sweeps lower-right)
      5. bottom 竖 (short, slight left hook at base)
      6. bottom 撇 (short, sweeping lower-right of shu)
    """
    # --- upper heng geometry ---
    heng_left = (55, 118)
    heng_mid = (150, 112)     # slight up-tilt to the right
    heng_right = (245, 108)
    tapered_polyline([heng_left, heng_mid, heng_right],
                     w_head=4.0, w_tail=4.5)

    # --- crossing pixel where the long pie descends through the heng ---
    cross = (158, 113)

    # --- Stroke 1: short top 撇 (stub above heng, centered over crossing) ---
    top_pie = cubic_pts((175, 60), (168, 72), (155, 82), (142, 95), steps=40)
    tapered_polyline(top_pie, w_head=4.2, w_tail=3.2)

    # --- Stroke 3: long continuous 撇 (above heng → cross → lower-left) ---
    # top segment: from a point above heng, descending into cross
    pie_top_start = (172, 82)
    pie_neck = (162, 100)
    seg_head = cubic_pts(pie_top_start, (169, 90), (165, 96), pie_neck,
                         steps=30)
    tapered_polyline(seg_head, w_head=3.5, w_tail=4.5)
    # body: through crossing, sweep to lower-left
    pie_tail_ctrl1 = (135, 165)
    pie_tail_ctrl2 = (75, 235)
    pie_tail_end = (32, 268)
    seg_body = cubic_pts(pie_neck, cross, pie_tail_ctrl1, pie_tail_end,
                         steps=90)
    tapered_polyline(seg_body, w_head=4.5, w_tail=2.2)
    # (control point re-plan for smoother tail)
    seg_body2 = cubic_pts(cross, pie_tail_ctrl1, pie_tail_ctrl2, pie_tail_end,
                          steps=90)
    tapered_polyline(seg_body2, w_head=4.5, w_tail=2.2)

    # --- Stroke 4: 捺 (starts at crossing on heng, sweeps lower-right) ---
    na_head = (cross[0] + 2, cross[1] + 2)
    na_ctrl1 = (200, 150)
    na_ctrl2 = (245, 178)
    na_tail = (272, 195)
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(na_seg, w_head=3.5, w_tail=5.0)

    # --- Stroke 5: bottom 竖 with slight left hook ---
    shu_top = (138, 152)
    shu_bot = (135, 258)
    shu_hook_end = (122, 260)
    shu_pts = [shu_top, (137, 200), shu_bot, shu_hook_end]
    tapered_polyline(shu_pts, w_head=4.2, w_tail=4.0)

    # --- Stroke 6: bottom 撇 (short pie, right of shu) ---
    pie2 = cubic_pts((180, 152), (188, 190), (200, 235), (212, 260),
                     steps=50)
    tapered_polyline(pie2, w_head=4.2, w_tail=2.5)


draw_qiao(draw)

out_path = ("/Users/peilinwu/Documents/AI memory research/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0226_乔__retry_1/01_乔.png")
img.save(out_path)
print(f"wrote {out_path}")
