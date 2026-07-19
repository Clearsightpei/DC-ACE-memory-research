"""Render 冫 (two-drops water radical) as a 300x300 PNG using PIL.

GT shows two strokes on the left side:
- Upper: short 点 (dot/diagonal), slanting down-right
- Lower: 提 (rising stroke), starting lower-left and curving/rising up-right
Both are positioned on the left half of the canvas.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def draw_stroke(points, widths):
    """Draw a variable-width stroke via connected tapered segments."""
    n = len(points)
    for i in range(n - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        w = (widths[i] + widths[i + 1]) / 2
        draw.line([(x1, y1), (x2, y2)], fill="black", width=int(round(w)))
    # Endpoint caps
    for (x, y), w in zip(points, widths):
        r = w / 2
        draw.ellipse([(x - r, y - r), (x + r, y + r)], fill="black")


# Upper 点 — short diagonal from upper-left to lower-right, thickening
# GT: starts around (135, 95) ends around (160, 130), curves slightly
upper = [
    (140, 100),
    (148, 112),
    (156, 122),
    (162, 132),
]
upper_w = [4, 6, 8, 8]
draw_stroke(upper, upper_w)

# Lower 提 — starts upper-right area, sweeps down-left then rises down-right end
# GT shows: starts around x=135 y=175, curves down-left to bottom, then a small
# tail going down-right (this is a 竖 with slight curve, ending in a pointed tail).
# Actually 冫 second stroke is 提 (rising): starts high-left, ends low-right rising up.
# Looking again at GT: the stroke starts around (140,175), sweeps down and slightly
# left to about (115, 240), continuing as a thin tail.
lower = [
    (140, 175),
    (132, 200),
    (125, 225),
    (118, 250),
    (115, 265),
]
lower_w = [8, 8, 7, 5, 3]
draw_stroke(lower, lower_w)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_012_冫/01_冫.png"
img.save(out)
print(f"Saved: {out}")
