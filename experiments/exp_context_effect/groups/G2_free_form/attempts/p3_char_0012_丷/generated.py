"""Render 丷 (two small top strokes) as a 300x300 PNG.

Structure from GT:
- Left stroke: a small 点 curving down-left (like a comma), positioned
  around left-of-center, mid-vertical. Thin at top-right, ends bluntly
  down-left.
- Right stroke: a short 撇 (straight diagonal), positioned right-of-
  center, going from upper-right down to lower-left. Longer/straighter
  than the left mark.

Both strokes sit in the upper-middle region of the canvas with a
notable gap between them (this is the signature of 丷 vs 八 which is
larger and lower).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def brush_stroke(points, widths):
    """Draw a tapered stroke by dabbing circles along a polyline.
    points: list of (x, y). widths: list of radii, same length."""
    n = len(points)
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        # Interpolate many small circles along the segment
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = w0 + (w1 - w0) * t
            draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# LEFT stroke — 点 tilting DOWN-RIGHT (thin at top-left, thick at
# bottom-right). Tail points toward center. This is the mirror-partner
# of the right 撇. Roughly from (100, 145) down-right to (135, 178).
# Slight curve (concave-down) for calligraphic feel.
left_pts = [
    (100, 145),
    (108, 155),
    (117, 164),
    (127, 172),
    (135, 178),
]
left_widths = [1.5, 2.2, 3.0, 3.6, 3.0]
brush_stroke(left_pts, left_widths)

# RIGHT stroke — 撇 short and straight-ish, going from upper-right
# down to lower-left, positioned to the right. Roughly from (200, 130)
# down-left to (165, 180). Thick at top, tapering to a thin tip.
right_pts = [
    (200, 128),
    (192, 140),
    (183, 152),
    (174, 165),
    (166, 180),
]
right_widths = [4.0, 3.6, 3.0, 2.2, 1.2]
brush_stroke(right_pts, right_widths)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0012_丷/01_丷.png")
