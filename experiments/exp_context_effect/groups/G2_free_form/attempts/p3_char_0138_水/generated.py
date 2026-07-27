"""
p3_char_0138_水 (water) — G2 attempt.

Decomposition (4 strokes, per errata p2_radical_119_水 + form_catalog):
  1. Central 竖钩: vertical from top center → down → hook up-and-LEFT at bottom.
  2. Upper-left 横撇: short 横 + shoulder + down-left 撇, crossing the 竖 near the top.
  3. Left leg 撇: sweeping curve from mid-height of 竖钩 down-left, ~150 px sweep.
  4. Right leg 捺: sweeping curve from mid-height of 竖钩 down-right, ~150 px sweep.

Canvas 300x300, white bg, black ink. PIL brush-dabs for calligraphic feel.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab_line(pts, width_start, width_end):
    """Draw a variable-width polyline by dabbing circles along a bezier-ish path."""
    n = 120
    for i in range(n + 1):
        t = i / n
        # linear interp along pts (assume 2 or 3 control points)
        if len(pts) == 2:
            (x0, y0), (x1, y1) = pts
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
        elif len(pts) == 3:
            (x0, y0), (x1, y1), (x2, y2) = pts
            x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2
            y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2
        else:
            # cubic-ish: sample piecewise
            seg = min(int(t * (len(pts) - 1)), len(pts) - 2)
            local_t = t * (len(pts) - 1) - seg
            (x0, y0) = pts[seg]
            (x1, y1) = pts[seg + 1]
            x = x0 + (x1 - x0) * local_t
            y = y0 + (y1 - y0) * local_t
        w = width_start + (width_end - width_start) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# 1. Central 竖钩: from (150, 55) straight down to (150, 245), then hook up-left to (128, 232).
dab_line([(150, 55), (150, 245)], 7, 7)
# hook flick up-and-left
dab_line([(150, 245), (135, 240), (118, 228)], 7, 3)

# 2. Upper-left 横撇: short 横 from (95, 110) to (135, 105) (slight rise),
#    then shoulder + short 撇 flicking down-left to (110, 135).
dab_line([(95, 110), (135, 105)], 5, 6)
dab_line([(135, 105), (138, 115), (108, 138)], 6, 3)

# 3. Left leg 撇: sweeping curve from (140, 135) mid-body area, down-left to (50, 240).
dab_line([(140, 135), (95, 195), (48, 245)], 7, 3)

# 4. Right leg 捺: sweeping curve from (155, 155) mid-body, down-right to (255, 230).
dab_line([(158, 150), (200, 190), (255, 232)], 4, 8)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0138_水/01_水.png"
)
