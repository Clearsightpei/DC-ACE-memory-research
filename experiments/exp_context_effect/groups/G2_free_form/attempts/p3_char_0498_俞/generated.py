"""Render 俞 (yú) — 亼 (人+一) top + body (月-like rectangle with inner strokes + right vertical hook).

Approx structure per GT:
- Upper third: 亼 = wide 人 apex ~ (150, 40); 撇 tip ~ (55, 130), 捺 tip ~ (250, 130);
  under-cap horizontal 一 at ~ y=140, spans x=65..240.
- Middle-upper small mark: short 短横 or 点 near center at ~ (140, 165).
- Body (lower half, ~y=160..275):
  - Left vertical 竖 from (95, 165) to (95, 275).
  - Top horizontal-plus-right-vertical (横折) forming the box: from (95, 165) → (215, 165) → (215, 265),
    with a small hook flick up-left at the bottom-right corner.
  - Two inner short 横 across the box: at y=200 and y=235, spanning x=110..200.
  - Bottom 横 closing the box: at y=270, from x=95..215.
- Canvas 300x300 white bg, black ink.

Uses PIL brush-dab taper (per drawer_memory principles).
Includes hook flick UP-and-LEFT (TIER-0 rule B).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def taper_stroke(pts, w_start, w_end, steps=120):
    seg_lens = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        seg_lens.append(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5)
    total = sum(seg_lens) or 1
    for s in range(steps + 1):
        t = s / steps
        target = t * total
        acc = 0
        x, y = pts[0]
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


# ===== 亼 top =====
# 撇 from apex down-left, tapered thick→thin with curve
apex = (152, 38)
pie_pts = [apex, (140, 65), (110, 95), (80, 120), (55, 138)]
taper_stroke(pie_pts, w_start=10, w_end=3, steps=140)
# 顿 dab at apex
draw.ellipse((apex[0] - 6, apex[1] - 5, apex[0] + 6, apex[1] + 6), fill="black")

# 捺 from apex down-right, thin→thick w/ terminal foot
na_pts = [(150, 48), (175, 75), (210, 105), (238, 130), (252, 140)]
taper_stroke(na_pts, w_start=4, w_end=12, steps=140)
# Terminal foot
draw.ellipse((252 - 9, 140 - 5, 252 + 11, 140 + 7), fill="black")

# 一 (under-cap horizontal), slight up-tilt
taper_stroke([(60, 158), (245, 152)], w_start=7, w_end=6, steps=80)
draw.ellipse((60 - 5, 158 - 5, 60 + 6, 158 + 6), fill="black")
draw.ellipse((245 - 6, 152 - 6, 245 + 7, 152 + 7), fill="black")

# ===== small center mark under 一 (短横) =====
taper_stroke([(130, 178), (175, 176)], w_start=5, w_end=5, steps=40)

# ===== body: box + inner horizontals =====
# Left vertical (竖) — from top-left corner down
taper_stroke([(90, 190), (90, 273)], w_start=7, w_end=7, steps=100)
draw.ellipse((90 - 5, 190 - 5, 90 + 6, 190 + 6), fill="black")

# 横折钩 — top horizontal + right vertical + hook flick
# Top horizontal
taper_stroke([(90, 190), (218, 190)], w_start=7, w_end=7, steps=100)
# Right vertical (starting at 折 corner)
taper_stroke([(218, 190), (218, 265)], w_start=7, w_end=7, steps=100)
# 折 shoulder dab
draw.ellipse((218 - 6, 190 - 6, 218 + 7, 190 + 7), fill="black")
# Hook flick UP-and-LEFT from bottom-right
taper_stroke([(218, 265), (205, 253)], w_start=7, w_end=2, steps=60)

# Inner horizontal 1
taper_stroke([(108, 218), (200, 218)], w_start=5, w_end=5, steps=80)

# Inner horizontal 2
taper_stroke([(108, 245), (200, 245)], w_start=5, w_end=5, steps=80)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0498_俞/01_俞.png")
