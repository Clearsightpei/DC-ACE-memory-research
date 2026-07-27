"""Render 几 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE = 6


def stroke_path(draw, pts, width=STROKE):
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill=INK, width=width)
        draw.ellipse([x2 - width // 2, y2 - width // 2,
                      x2 + width // 2, y2 + width // 2], fill=INK)


# Stroke 1: 撇 (piě) — from just left of the top-horizontal's start,
# slanting down-left to about mid-height on the left side.
# GT shows this stroke ending around (60, 175) — it does NOT sweep all
# the way to the bottom.
pie_pts = [
    (110, 95),
    (100, 115),
    (88, 138),
    (75, 160),
    (62, 180),
]
stroke_path(draw, pie_pts, width=STROKE)

# Stroke 2: 横折弯钩 (héng-zhé-wān-gōu)
# héng: horizontal top from ~(105, 100) to ~(200, 95) — slight upward slant
# zhé: turn down at right corner (~200, 95)
# wān: curve rightward+down along the bottom-right,
#      then sweep out to the right and back up (the "elbow" hook).
# gōu: small tick upward at the end.

path = [
    # Horizontal top (slight upward slant like GT)
    (105, 100), (135, 98), (170, 96), (200, 94),
    # zhé corner turning downward
    (205, 100), (208, 115),
    # right leg descending, curving very slightly outward
    (212, 145), (215, 175), (218, 205),
    # wān — curve outward to the right and down
    (222, 225), (232, 240),
    # then the bottom sweep continues to the right
    (245, 248), (258, 248),
    # gōu — small hook going up
    (255, 240), (252, 232),
]
stroke_path(draw, path, width=STROKE)

out_path = os.path.join(os.path.dirname(__file__), "01_几.png")
img.save(out_path)
print(f"Saved {out_path}")
