"""G1 render of radical 冖 (cover / 秃宝盖).

Two strokes:
  1. Small left 点 (dot / short downward stroke) at top-left.
  2. Horizontal 横 sweeping right, ending in a short downward 钩/竖 hook
     at the right end (横钩 shape).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(points, width_start, width_end, steps=40):
    """Draw a polyline with linearly tapering width across the whole path."""
    # Precompute cumulative arc length so taper follows length, not segments.
    seg_lens = []
    total = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        d = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        seg_lens.append(d)
        total += d
    if total == 0:
        return
    # Walk the path in equal-length steps and draw thick dots.
    n = steps
    for i in range(n + 1):
        t = i / n  # 0..1
        target = t * total
        # find segment
        acc = 0.0
        for si, sl in enumerate(seg_lens):
            if acc + sl >= target or si == len(seg_lens) - 1:
                local = (target - acc) / sl if sl > 0 else 0.0
                x0, y0 = points[si]
                x1, y1 = points[si + 1]
                x = x0 + (x1 - x0) * local
                y = y0 + (y1 - y0) * local
                break
            acc += sl
        w = width_start + (width_end - width_start) * t
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# Stroke 1: 点 — small downward diagonal dot on left side.
# In the GT it looks like a short slanted mark going down-left.
stroke(
    [(112, 118), (104, 138)],
    width_start=4,
    width_end=8,
    steps=20,
)

# Stroke 2: 横钩 — horizontal top starting a bit right of the dot,
# sweeping right, then a short vertical hook down at the right end.
# Horizontal part
stroke(
    [(120, 118), (128, 116), (215, 118), (222, 122)],
    width_start=6,
    width_end=7,
    steps=60,
)
# Hook down at the right end
stroke(
    [(222, 122), (218, 145)],
    width_start=7,
    width_end=3,
    steps=20,
)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p2_radical_026_冖/01_冖.png"
)
