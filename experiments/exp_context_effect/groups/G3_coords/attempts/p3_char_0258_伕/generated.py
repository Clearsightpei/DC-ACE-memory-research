# 伕 (fu) — 亻 + 夫 (person + husband). 6 strokes total.
# Left: 亻 (pie + shu). Right: 夫 (heng-top + heng-mid + pie + na crossing).
# Per v8: bank primitives are REFERENCE ONLY; trust GT.
# GT observations:
#   - Left 亻 sits in the left ~30% of canvas, spans full height.
#   - Right 夫: top heng short, second heng longer (main horizontal),
#     pie starts above/on 2nd heng and sweeps down-left; na starts at
#     the pie/heng crossing and sweeps down-right.
#   - Thin ink ~4px per P12 (MMH weight).

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


# =========================================================
# LEFT: 亻 (person radical), occupies roughly x in [40, 100]
# =========================================================
# Pie: short curved sweep from top-right of radical to lower-left.
pie_top = (85, 55)
pie_c1  = (78, 100)
pie_c2  = (62, 140)
pie_end = (45, 175)
pie_seg = cubic_pts(pie_top, pie_c1, pie_c2, pie_end, steps=80)
tapered_polyline(pie_seg, w_head=5.0, w_tail=2.5)

# Shu: vertical from mid-pie down to lower portion.
shu_top = (85, 110)
shu_bot = (85, 265)
tapered_polyline([shu_top, shu_bot], w_head=4.5, w_tail=4.0)

# =========================================================
# RIGHT: 夫 (husband), occupies roughly x in [115, 285]
# =========================================================
# Top heng (short), near y ~ 90.
tapered_polyline([(150, 92), (240, 88)], w_head=4.0, w_tail=4.5)

# Second heng (longer main horizontal), near y ~ 145.
tapered_polyline([(125, 148), (270, 142)], w_head=4.0, w_tail=4.8)

# Pie: one continuous curve. Top starts above 2nd heng, passes
# through a crossing on the heng, sweeps to lower-left (stops before 亻).
cross = (198, 145)
pie2_top = (208, 108)   # top above second heng (between the two hengs)
pie2_c1  = (202, 128)
pie2_c2  = (180, 205)
pie2_end = (150, 265)   # keep clear of 亻 shu at x=85
pie2_seg = cubic_pts(pie2_top, pie2_c1, pie2_c2, pie2_end, steps=80)
tapered_polyline(pie2_seg, w_head=3.5, w_tail=2.2)

# Na: starts near the crossing on the 2nd heng, sweeps down-right.
na_head = (cross[0] + 2, cross[1] + 2)
na_c1   = (225, 195)
na_c2   = (255, 240)
na_end  = (283, 268)
na_seg = cubic_pts(na_head, na_c1, na_c2, na_end, steps=80)
tapered_polyline(na_seg, w_head=3.2, w_tail=5.5)


out_path = ("<REPO_ROOT>/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0258_伕/01_伕.png")
img.save(out_path)
print(f"wrote {out_path}")
