"""Render radical 耂 (4 strokes) to a 300x300 PNG using PIL.

Revised after visual comparison with GT.

Strokes (based on GT):
1. 短横 (small upper horizontal) - top area
2. 竖 (vertical) - drops from just above the small horizontal down toward long horizontal
3. 长横 (long horizontal) - the main wide bar across the middle
4. 长撇 (long left-falling stroke) - starts near upper-middle-right, sweeps down to lower-left
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def line(p0, p1, width=6):
    draw.line([p0, p1], fill=BLACK, width=width)


def stroke_taper(points, w_start=8, w_end=3):
    n = len(points) - 1
    for i in range(n):
        t0 = i / max(1, n)
        t1 = (i + 1) / max(1, n)
        w0 = w_start + (w_end - w_start) * t0
        w1 = w_start + (w_end - w_start) * t1
        w = max(1, int(round((w0 + w1) / 2)))
        draw.line([points[i], points[i + 1]], fill=BLACK, width=w)


# --- Stroke 1: small upper horizontal (short bar) ---
# Sits high, roughly x 118-158, y ~ 95
line((118, 96), (162, 94), width=6)

# --- Stroke 2: vertical (short 竖) crossing the small horizontal, going down toward long 横 ---
line((140, 80), (140, 148), width=6)

# --- Stroke 3: main long horizontal (长横), slight tilt ---
line((45, 152), (250, 148), width=7)

# --- Stroke 4: long 撇 (piě) — starts near upper area a bit right of center
# curves down-left through mid to bottom-left corner. In GT it starts high near
# the top of the vertical and sweeps out very far to lower-left. ---
pie_points = [
    (175, 70),
    (168, 95),
    (160, 120),
    (150, 148),
    (135, 180),
    (115, 210),
    (90, 235),
    (60, 258),
]
stroke_taper(pie_points, w_start=8, w_end=3)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_102_耂/01_耂.png"
)
