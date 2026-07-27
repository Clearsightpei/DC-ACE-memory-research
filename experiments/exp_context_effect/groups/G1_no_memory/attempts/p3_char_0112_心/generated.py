"""G1 render: 心 (heart) — 4 strokes.

Strokes (traditional order):
  1. 左点 (left dot): a short diagonal dot on the left.
  2. 卧钩 (lying hook): the big smooth curving bowl, hooking up at the right end.
  3. 中点 (middle dot): a short dot above the bowl.
  4. 右点 (right dot): a short diagonal dot on the upper right.

Output: 300x300 white PNG with black ink.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke_poly(points, width):
    draw.line(points, fill=INK, width=width, joint="curve")
    r = width / 2
    for x, y in (points[0], points[-1]):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def catmull_rom(pts, samples_per_seg=24):
    """Smooth curve through pts (Catmull-Rom). Returns dense point list."""
    if len(pts) < 2:
        return pts
    # pad ends
    p = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(len(p) - 3):
        p0, p1, p2, p3 = p[i], p[i + 1], p[i + 2], p[i + 3]
        for s in range(samples_per_seg):
            t = s / samples_per_seg
            t2 = t * t
            t3 = t2 * t
            x = 0.5 * ((2 * p1[0]) +
                       (-p0[0] + p2[0]) * t +
                       (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                       (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) +
                       (-p0[1] + p2[1]) * t +
                       (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                       (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    out.append(pts[-1])
    return out


# ---- Stroke 1: 左点 (left dot) — short diagonal, tapering down-left
s1 = catmull_rom([(92, 148), (88, 170), (80, 200)])
stroke_poly(s1, width=7)

# ---- Stroke 2: 卧钩 (lying hook) — smooth wide bowl w/ small upward hook at right end
bowl = catmull_rom([
    (108, 158),
    (112, 190),
    (128, 220),
    (160, 235),
    (195, 232),
    (218, 215),
    (225, 195),   # right end of bowl (bottom of hook)
    (220, 188),   # hook curls up-left
    (208, 188),
])
stroke_poly(bowl, width=8)

# ---- Stroke 3: 中点 (middle dot) — short vertical-ish dot above bowl
s3 = catmull_rom([(148, 115), (152, 140), (158, 162)])
stroke_poly(s3, width=7)

# ---- Stroke 4: 右点 (right dot) — short diagonal on upper right
s4 = catmull_rom([(232, 128), (222, 148), (210, 170)])
stroke_poly(s4, width=7)

out_path = os.path.join(os.path.dirname(__file__), "01_心.png")
img.save(out_path)
print(f"Wrote {out_path}")
