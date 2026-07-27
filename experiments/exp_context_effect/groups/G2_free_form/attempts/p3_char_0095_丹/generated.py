"""
p3_char_0095_丹 — 4 strokes

Structure from GT:
  1. 撇 (left slanting stroke): starts high, curves down and left
  2. 横折钩 (top horizontal + right down + small hook): forms top and right side
  3. 点 (inner dot): short slanted dot inside upper part of frame
  4. 横 (long horizontal cross-bar): extends BEYOND frame on both sides,
     passes through the middle of the frame

Canvas: 300x300 white background, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(pts, width=6):
    """Draw a polyline with rounded joints."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill=BLACK)


# ----- Stroke 1: 撇 (left slanting curve) -----
# Starts near top-center, curves down and out to the left
pie = [
    (140, 55),
    (130, 95),
    (115, 140),
    (98, 185),
    (82, 230),
    (72, 265),
]
brush_line(pie, width=6)

# ----- Stroke 2: 横折钩 (top-horizontal + right-vertical + hook) -----
# Top horizontal from just right of pie's top to right side
top_h = [(138, 60), (205, 62)]
brush_line(top_h, width=6)
# Right vertical (折) going down
right_v = [(205, 62), (210, 130), (208, 200), (200, 255)]
brush_line(right_v, width=6)
# Small hook (钩) flicking left at bottom
hook = [(200, 255), (180, 258)]
brush_line(hook, width=5)

# ----- Stroke 3: 点 (inner dot) - short slanted dot -----
dot = [(150, 118), (162, 132)]
brush_line(dot, width=7)

# ----- Stroke 4: 横 (long horizontal cross-bar extending beyond frame) -----
cross = [(35, 165), (260, 162)]
brush_line(cross, width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0095_丹/01_丹.png")
