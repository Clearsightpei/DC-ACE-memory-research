"""Render 入 (rù) — 'to enter'. Two strokes:
  1) 撇 (left-falling): starts near top-center, sweeps down-left.
  2) 捺 (right-falling): joins the 撇 slightly BELOW its top
     (distinguishes 入 from 人), sweeps down-right, flaring at the foot.

Key structural feature: the top of the 撇 pokes ABOVE the join point of
the 捺, producing the characteristic little upper-left 'flag' of 入.

Proportions tuned to match GT at gt/phase3/入.png: peak near (140, 90),
piě tail ~ (50, 245), nà foot ~ (250, 240), moderate width, gentle curves.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def draw_stroke(points, w_start, w_end):
    """Draw a smoothly-varying-width polyline through `points`."""
    # subdivide each segment for smooth width taper
    subdiv = 12
    fine = []
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        for t in range(subdiv):
            tt = t / subdiv
            fine.append((x0 + (x1 - x0) * tt, y0 + (y1 - y0) * tt))
    fine.append(points[-1])
    n = len(fine) - 1
    for i in range(n):
        tt = i / n
        w = w_start + (w_end - w_start) * tt
        wi = max(1, int(round(w)))
        draw.line([fine[i], fine[i + 1]], fill="black", width=wi)
        r = max(1, wi // 2)
        x, y = fine[i]
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# Stroke 1: 撇 — left-falling. Top of 撇 at ~(145, 78). Curves down-left
# to tail near (55, 245). Thicker at top, tapers to fine point.
pie_pts = [
    (145, 78),
    (135, 105),
    (120, 140),
    (100, 178),
    (78, 215),
    (55, 245),
]
draw_stroke(pie_pts, 8, 3)

# Stroke 2: 捺 — right-falling. Joins the 撇 at ~(130, 105) (below its top,
# so the 撇 tip pokes up as the little 'flag'). Sweeps down-right, widening
# toward the foot ~(252, 242).
na_pts = [
    (130, 105),
    (155, 140),
    (185, 175),
    (215, 208),
    (252, 242),
]
draw_stroke(na_pts, 5, 10)

# Small foot flare at end of 捺 (a rightward tick / 捺's 出锋)
draw.polygon(
    [(252, 238), (270, 246), (262, 254), (250, 250)],
    fill="black",
)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_入.png")
img.save(out_path)
print(f"Saved {out_path} ({img.size})")
