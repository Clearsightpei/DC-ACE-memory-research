"""
之 (zhī) — 3 strokes:
  1) 点 (dot) at top-center-ish
  2) 横撇 (horizontal-then-down-left flick) forming the "z-shoulder"
  3) 平捺 (long swooping bottom stroke, ends horizontal-right foot)

Canvas: 300x300, white bg, black ink.
Uses PIL. Strokes rendered as tapered polylines via multiple line
segments with varying widths.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(points, widths):
    """Draw a variable-width polyline. widths is a list matching points."""
    for i in range(len(points) - 1):
        p0 = points[i]
        p1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        # subdivide for smooth width change
        steps = max(4, int(((p1[0]-p0[0])**2 + (p1[1]-p0[1])**2) ** 0.5 / 3))
        for s in range(steps):
            t0 = s / steps
            t1 = (s + 1) / steps
            x0 = p0[0] + (p1[0] - p0[0]) * t0
            y0 = p0[1] + (p1[1] - p0[1]) * t0
            x1 = p0[0] + (p1[0] - p0[0]) * t1
            y1 = p0[1] + (p1[1] - p0[1]) * t1
            w = w0 + (w1 - w0) * ((t0 + t1) / 2)
            draw.line([(x0, y0), (x1, y1)], fill="black", width=max(1, int(round(w))))
            # dab a circle at joint to smooth
            r = w / 2
            draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill="black")


# --- Stroke 1: top dot (点) — tilted down-right, like a short `\`
stroke(
    [(150, 50), (172, 82)],
    [3, 9],
)

# --- Stroke 2: 横撇 (horizontal then down-left flick)
# Horizontal part slightly bowed, then a downward-left flick that
# LANDS at the same joint where stroke 3 will begin.
JOINT_X, JOINT_Y = 110, 205  # meeting point with stroke 3
# horizontal top: gentle arc, ends at right shoulder
stroke(
    [(80, 128), (115, 118), (170, 112), (205, 118)],
    [3, 6, 8, 9],
)
# 撇 flick from shoulder down-left to JOINT
stroke(
    [(205, 118), (180, 145), (150, 175), (JOINT_X, JOINT_Y)],
    [9, 8, 6, 4],
)

# --- Stroke 3: 平捺 — starts at JOINT, dips down, flattens, and
# tail LIFTS to the right (rising foot).
stroke(
    [
        (JOINT_X, JOINT_Y),   # start (thin) at joint
        (140, 225),
        (175, 245),
        (210, 253),           # belly of the sweep (thickest)
        (245, 248),
        (272, 238),           # lifted tail (rising)
    ],
    [4, 7, 10, 12, 9, 4],
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0039_之/01_之.png"
)
print("wrote 01_之.png")
