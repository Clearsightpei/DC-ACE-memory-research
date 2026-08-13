"""
p3_char_0216_失 — retry_1 (v9 visual-diff retry, citing 大_char.py recipe)

# VISUAL DIFF (comparing prior p3_char_0216_失/01_失.png vs GT phase3/失.png)
#
# Prior attempt shows:
#   - Top region reads like a small tilted "L" / 上 shape at upper-center
#     (a short vertical + a small hook). It is NOT the 失 top signature.
#   - A single middle heng across the middle at ~y=150.
#   - A long pie descending from upper-center THROUGH the heng down to
#     lower-left corner (this arm is roughly right).
#   - A na that starts LOW (well below the heng) and is short/detached,
#     forming a big open V at the bottom rather than crossing on the heng.
#   - Uniform ~6-7 px line weight (calligraphic look).
#
# GT shows:
#   - A short 撇 tick at upper-left of the top block, angled down-left
#     (small ~30-40 px stroke).
#   - A short top heng at the top (~y=90-95), spanning roughly the
#     center-right portion (from ~x=145 to ~x=210). This is 失's
#     distinguishing feature over 大.
#   - A long middle heng (~y=145) similar to 大 but a touch lower.
#   - A long continuous pie starting ABOVE the middle heng (with a small
#     head above heng), curving DOWN THROUGH the crossing, sweeping
#     down-LEFT to lower-left corner.
#   - A separate na originating AT the pie/heng crossing on the middle
#     heng, sweeping DOWN-RIGHT to lower-right corner.
#   - Thin ~4 px MMH line weight throughout (P12).
#
# Concrete gaps to fix (>=2):
#   (a) TOP BLOCK: prior drew an L-shape; GT has a short 撇 tick +
#       short top heng. Replace with two clean strokes.
#   (b) NA ORIGIN: prior na starts LOW and detached; GT na starts AT
#       the crossing pixel ON the middle heng. Move na_head to the
#       crossing.
#   (c) LINE WEIGHT: prior ~6-7 px; GT ~4 px thin. Drop widths per P12.

# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): errata says "apex on middle heng" — same fix as 矢/大.
#   B7 curator promoted 大_char.py as the reference recipe: continuous
#   pie curve above/through heng + separate na originating AT crossing;
#   REJECT kiss_apex helper (v9 rerun graduate lesson).
# Q2 (form_catalog): X-crossing family (大/人/入/矢/失/乔) — the recipe
#   is one continuous pie stroke that passes through the heng crossing,
#   with na starting ON heng at that crossing. Thin ~4 px MMH weight.
# Q3 (helpers): kiss_apex REJECTED (per 大_char.py B7 note). Hand-render
#   tapered bezier strokes at ~4 px. Adopt da_char.py's structure and
#   overlay the 失-specific top (short pie tick + short top heng).
"""

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


def draw_shi_lose(dr):
    """
    失 = 大 body + short top-pie tick + short top-heng above middle heng.
    Body layout borrowed directly from da_char.py (B7 v9 graduate),
    just shifted slightly down to leave room for the top block.
    """
    # --- top block (失 signature) ---
    # Short 撇 tick — down-left slash from upper area.
    top_pie = [(158, 62), (152, 72), (144, 88), (138, 100)]
    tapered_polyline(top_pie, w_head=4.0, w_tail=2.5)

    # Short top heng — slight up-right tilt, spans right portion.
    top_heng_left = (148, 96)
    top_heng_right = (208, 92)
    tapered_polyline([top_heng_left, (178, 94), top_heng_right],
                     w_head=3.5, w_tail=4.0)

    # --- middle heng (main crossbar) ---
    heng_left = (60, 158)
    heng_right = (238, 150)
    tapered_polyline([heng_left, (150, 154), heng_right],
                     w_head=3.5, w_tail=4.2)

    # Crossing pixel where pie descends through middle heng.
    cross = (150, 154)

    # --- long pie: one continuous stroke, top-above-heng through
    #     crossing to lower-left ---
    pie_top_start = (162, 108)   # just below top heng, above middle heng
    pie_head_ctrl = (168, 122)
    pie_neck      = (158, 138)
    pie_tail_ctrl = (95, 220)
    pie_tail_end  = (52, 268)

    seg_head = cubic_pts(pie_top_start, pie_head_ctrl,
                         (160, 145), pie_neck, steps=40)
    seg_body = cubic_pts(pie_neck, (146, 158), pie_tail_ctrl,
                         pie_tail_end, steps=80)
    tapered_polyline(seg_head, w_head=3.5, w_tail=4.5)
    tapered_polyline(seg_body, w_head=4.5, w_tail=2.2)

    # --- na: separate stroke starting AT crossing, sweeping down-right ---
    na_head = (cross[0] + 2, cross[1] + 2)
    na_ctrl1 = (180, 200)
    na_ctrl2 = (222, 240)
    na_tail  = (250, 265)
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(na_seg, w_head=3.2, w_tail=4.8)


draw_shi_lose(draw)

out_path = ("/Users/peilinwu/Documents/AI memory research/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0216_失__retry_1/01_失.png")
img.save(out_path)
print(f"wrote {out_path}")
