"""
p3_char_0216_失 retry_2 — G3

TRAJECTORY DIFF:
- main FAIL: X-crossing pie+na drawn but the top area had only ONE
  short mark and ONE heng (missing the second heng); pie/na apex
  hovered above the heng. Overall body drifts too "夂-like".
- retry_1 FAIL: same fail mode — still missing the second heng.
  There is a small top slash, then a single long horizontal crossed
  by pie/na, but the classic 失 signature (short 撇 + top heng +
  middle heng + big X body) never resolves. Apex still sits above
  the crossing heng.
- Fix plan (this attempt):
  (1) Render TWO distinct hengs — a short top heng at y~105 and a
      longer middle heng at y~150. This is the critical missing
      element on both prior fails.
  (2) Small top 撇 above the top heng, y~65..95.
  (3) Reuse the 大 v9-graduate recipe for the long pie + long na:
      pie is ONE continuous curve above/through middle heng sweeping
      to lower-left; na is a SEPARATE stroke starting AT the
      pie/heng crossing on the middle heng, sweeping to lower-right.
  (4) Thin MMH weight (~4 px) per P12.

# RETRY MEMORY CHECKLIST
# Q1 (errata): errata.md p3_char_0216_失 says "apex on middle heng"
#   (same fix as 矢). Applied — na_head sits ON the middle heng.
# Q2 (form_catalog): X-crossing family — use continuous pie-through-
#   heng + separate na-from-crossing recipe (大 template).
# Q3 (helpers): kiss_apex REJECTED (contradicts GT; 大 graduation
#   lesson). Hand-render tapered bezier strokes.
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
    """失 — 5 strokes: 丿 短 + 一 短 + 一 长 + 丿 长 + 乀."""
    # --- Stroke 1: short top 撇 — piercing through the top heng
    # (this is 失's key signature vs 矢: the pie protrudes above the
    # top heng and extends down through it). ---
    pie_top_start = (168, 58)   # well above top heng
    pie_top_ctrl  = (155, 88)
    pie_top_end   = (138, 122)  # extends below top heng (y=105)
    tapered_polyline([pie_top_start, pie_top_ctrl, pie_top_end],
                     w_head=4.0, w_tail=2.4)

    # --- Stroke 2: TOP heng (short) ---
    top_heng_left  = (108, 108)
    top_heng_right = (198, 105)  # slight up-tilt
    tapered_polyline([top_heng_left, (152, 107), top_heng_right],
                     w_head=3.2, w_tail=4.0)

    # --- Stroke 3: MIDDLE heng (longer crossbar) ---
    mid_heng_left  = (62,  155)
    mid_heng_right = (232, 148)  # slight up-tilt
    tapered_polyline([mid_heng_left, (147, 152), mid_heng_right],
                     w_head=3.5, w_tail=4.4)

    # Crossing pixel on the middle heng where pie descends through
    cross = (150, 152)

    # --- Stroke 4: long 撇 (one continuous curve from above middle
    # heng, through the crossing, sweeping to lower-left) ---
    pie_top    = (162, 120)      # slightly right of crossing, above middle heng
    pie_ctrl1  = (156, 138)
    pie_neck   = (150, 152)      # crossing pixel
    pie_ctrl2  = (105, 215)
    pie_tail   = (60,  268)      # lower-left corner

    seg_head = cubic_pts(pie_top, pie_ctrl1, (152, 145), pie_neck, steps=40)
    seg_body = cubic_pts(pie_neck, (140, 175), pie_ctrl2, pie_tail, steps=80)
    tapered_polyline(seg_head, w_head=3.4, w_tail=4.4)
    tapered_polyline(seg_body, w_head=4.4, w_tail=2.2)

    # --- Stroke 5: 捺 starting AT the pie/heng crossing, sweeping
    # down-right with a subtle downward belly ---
    na_head  = (cross[0] + 2, cross[1] + 2)
    na_ctrl1 = (180, 200)
    na_ctrl2 = (220, 240)
    na_tail  = (245, 262)
    na_seg = cubic_pts(na_head, na_ctrl1, na_ctrl2, na_tail, steps=80)
    tapered_polyline(na_seg, w_head=3.2, w_tail=4.8)


draw_shi(draw)

out_path = ("/Users/peilinwu/Documents/AI memory research/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0216_失__retry_2/01_失.png")
img.save(out_path)
print(f"wrote {out_path}")
