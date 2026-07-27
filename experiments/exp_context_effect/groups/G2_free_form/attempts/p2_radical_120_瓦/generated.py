"""瓦 — 4-stroke radical (revised).
Stroke order:
  1) 横 (top horizontal, thin, slight up-tilt, dabs at ends)
  2) 竖提 (short slanted 撇 down-left from left area, then upward flick)
  3) 横折弯钩 (from top-right area: down along right side, curving out along bottom,
     ending with a hook-up on the bottom-left of the bowl)
  4) 点 (small dot inside upper part of the bowl)

Silhouette notes vs GT:
  - open shape, NOT a closed box
  - right side sweeps down then rightward-out at bottom, so bottom is a broad curve
  - left leg is short/steep and ends higher than the right sweep's bottom
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def taper_stroke(points, w_start=8, w_end=8, steps=60):
    """Dab circles along a polyline; width linearly interpolated by arc length."""
    dens = []
    total = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        seg = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        dens.append((total, total + seg, (x1, y1), (x2, y2)))
        total += seg
    if total == 0:
        return
    for k in range(steps + 1):
        t = k / steps
        d = t * total
        for s0, s1, p0, p1 in dens:
            if d <= s1:
                if s1 == s0:
                    x, y = p1
                else:
                    u = (d - s0) / (s1 - s0)
                    x = p0[0] + u * (p1[0] - p0[0])
                    y = p0[1] + u * (p1[1] - p0[1])
                w = w_start + (w_end - w_start) * t
                r = w / 2
                draw.ellipse([x - r, y - r, x + r, y + r], fill="black")
                break


# --- Stroke 1: top 横 --- longish, thin, slight up-tilt, small 顿 dabs at ends
taper_stroke([(65, 92), (140, 85), (215, 82)], w_start=5, w_end=6, steps=40)
# little 顿 dabs at both ends
draw.ellipse([59, 87, 71, 99], fill="black")
draw.ellipse([210, 76, 224, 90], fill="black")

# --- Stroke 2: 撇 / 竖提 --- steep slant from under top 横, going down-left, ending in a small up-right flick
# main descent (撇 body)
taper_stroke([(115, 100), (95, 155), (75, 215)], w_start=7, w_end=5, steps=40)
# upward flick (提)
taper_stroke([(75, 215), (108, 200)], w_start=6, w_end=2, steps=15)

# --- Stroke 3: 横折弯钩 --- starts near the top 横 on the right, drops, curves out along bottom, hooks up
# tiny top-horizontal at start (shoulder inside the top area)
taper_stroke([(160, 118), (215, 118)], w_start=5, w_end=6, steps=15)
# down the right side with slight outward bow
taper_stroke([(215, 118), (225, 170), (222, 220)], w_start=7, w_end=8, steps=40)
# curve along the bottom outward — the "bowl"
taper_stroke([(222, 220), (205, 255), (170, 270), (130, 268), (105, 258)], w_start=8, w_end=7, steps=60)
# hook up at end
taper_stroke([(105, 258), (100, 235)], w_start=7, w_end=2, steps=15)

# --- Stroke 4: 点 --- small teardrop inside upper part of bowl
taper_stroke([(158, 148), (175, 172)], w_start=3, w_end=8, steps=15)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_120_瓦/01_瓦.png")
print("Saved 01_瓦.png")
