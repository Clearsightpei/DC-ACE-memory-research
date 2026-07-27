"""Render 亼 (jí) — a 人-apex over a 一 horizontal.

Structure (per GT):
- Top: wide 人 = 撇 (down-left from apex) + 捺 (down-right from apex).
  Apex ~ (150, 55), 撇 tip ~ (60, 180), 捺 tip ~ (240, 180).
  Per sibling table 人-vs-入: 人 has apex at same y (single meeting point).
- Bottom: 一 horizontal at ~y=245, spans ~x=70..230, slight up-tilt.
- Canvas 300x300 white bg, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def taper_stroke(pts, w_start, w_end, steps=60):
    """Draw a tapered stroke by sampling along a polyline and drawing dabs."""
    # Interpolate along the polyline
    # Compute cumulative length
    seg_lens = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        seg_lens.append(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5)
    total = sum(seg_lens)
    for s in range(steps + 1):
        t = s / steps  # 0..1 along total length
        target = t * total
        acc = 0
        for i, L in enumerate(seg_lens):
            if acc + L >= target or i == len(seg_lens) - 1:
                local = (target - acc) / L if L > 0 else 0
                (x0, y0), (x1, y1) = pts[i], pts[i + 1]
                x = x0 + (x1 - x0) * local
                y = y0 + (y1 - y0) * local
                break
            acc += L
        w = w_start + (w_end - w_start) * t
        r = max(1, w / 2)
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# 撇 (from apex down-left): 顿 dab at top → thin taper toward tip.
# Give a real curve — start nearly vertical then flare down-left.
apex_pie = (152, 65)
pie_c1 = (140, 100)   # early: still steep
pie_c2 = (105, 135)   # bow slightly right of straight line
pie_c3 = (75, 175)
pie_tip = (55, 200)
taper_stroke([apex_pie, pie_c1, pie_c2, pie_c3, pie_tip], w_start=10, w_end=3, steps=120)
# small 顿 dab at the start (top head of 撇)
draw.ellipse((apex_pie[0] - 6, apex_pie[1] - 5, apex_pie[0] + 6, apex_pie[1] + 6), fill="black")

# 捺 (from just below apex down-right): thin → thick with terminal foot.
# In 人 the 捺 meets 撇 at the apex; put it starting slightly below/right of apex.
apex_na = (150, 78)
na_c1 = (175, 105)
na_c2 = (205, 140)
na_c3 = (230, 175)
na_tip = (248, 195)
taper_stroke([apex_na, na_c1, na_c2, na_c3, na_tip], w_start=4, w_end=12, steps=120)
# Terminal foot (broad flat press)
draw.ellipse((na_tip[0] - 9, na_tip[1] - 5, na_tip[0] + 11, na_tip[1] + 7), fill="black")

# 一 horizontal below, slight up-tilt (right end slightly higher)
h_left = (55, 253)
h_right = (240, 246)
taper_stroke([h_left, h_right], w_start=7, w_end=6, steps=60)
# end dabs (顿)
draw.ellipse((h_left[0] - 5, h_left[1] - 5, h_left[0] + 6, h_left[1] + 6), fill="black")
draw.ellipse((h_right[0] - 6, h_right[1] - 6, h_right[0] + 7, h_right[1] + 7), fill="black")

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0054_亼/01_亼.png")
