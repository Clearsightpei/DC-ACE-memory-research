"""G1 render for radical 亻 (人字旁, 2 strokes).

Stroke 1: 撇 (piě) — a slanted curve from upper-right (around top center)
          down to lower-left.
Stroke 2: 竖 (shù) — a vertical line starting from the mid-point of the
          撇 going down.
Output: 300x300 white background, black ink PNG.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
STROKE_W = 6


def draw_curve(points, width=STROKE_W):
    """Draw a smooth curve through points as connected line segments."""
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)
    # round the joints
    for p in points:
        draw.ellipse((p[0] - width // 2, p[1] - width // 2,
                      p[0] + width // 2, p[1] + width // 2), fill=INK)


# Stroke 1: 撇 — starts near the top, slightly right of center, curves
# down and to the left. Reference GT: top begins around (170, 65) with
# a tiny hook curl, sweeps down to about (95, 235).
piě_points = [
    (175, 70),
    (178, 76),   # small initial curl to the right
    (172, 84),
    (163, 105),
    (152, 132),
    (138, 160),
    (122, 190),
    (105, 220),
    (88, 245),
]
draw_curve(piě_points, width=6)

# Stroke 2: 竖 — vertical line, starts from roughly the lower half of
# the 撇 (around x=140, y=165) and drops straight down to y≈255.
shù_points = [
    (142, 165),
    (142, 190),
    (142, 220),
    (142, 258),
]
draw_curve(shù_points, width=6)

out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_029_亻/01_亻.png"
img.save(out_path)
print(f"Saved: {out_path}")
