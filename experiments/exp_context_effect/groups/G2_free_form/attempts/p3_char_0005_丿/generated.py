"""Render 丿 (p3_char_0005) to 01_丿.png at 300×300.

GT analysis:
  - 8-px black border frame around the canvas (米字格 outer box).
  - Component A (main 丿): starts near (80, 92), runs nearly vertical
    through (~93, 122)–(~93, 172), then bows left, ending at (~40, 275).
    Width ~5-9 px, slightly widening at the tail.
  - Component B (upper-right small stroke): a short diagonal from
    (~124, 105) down-right to (~172, 165). Width ~6-8 px.
Note: 丿 as MMH-rendered here contains two components (single Unicode
codepoint but two visible strokes); we replicate both faithfully.
"""

import os
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# --- 1. Outer border frame (8 px thick, matches GT convention) ---
BORDER = 8
draw.rectangle([0, 0, W - 1, H - 1], fill="black")
draw.rectangle([BORDER, BORDER, W - 1 - BORDER, H - 1 - BORDER], fill="white")


def dab_stroke(path_points, r_start, r_end, steps_per_seg=80):
    """Draw a piecewise stroke via brush dabs with linear radius taper.

    path_points: list of (x, y). Radius interpolates linearly along
    cumulative arc length from r_start to r_end.
    """
    # compute segment lengths
    seg_len = []
    for i in range(len(path_points) - 1):
        (x0, y0), (x1, y1) = path_points[i], path_points[i + 1]
        seg_len.append(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5)
    total = sum(seg_len)
    if total == 0:
        return
    covered = 0.0
    for i in range(len(path_points) - 1):
        (x0, y0), (x1, y1) = path_points[i], path_points[i + 1]
        L = seg_len[i]
        n = max(2, int(steps_per_seg * L / 40))
        for k in range(n + 1):
            t_seg = k / n
            x = x0 + (x1 - x0) * t_seg
            y = y0 + (y1 - y0) * t_seg
            t_glob = (covered + t_seg * L) / total
            r = r_start + (r_end - r_start) * t_glob
            draw.ellipse((x - r, y - r, x + r, y + r), fill="black")
        covered += L


# --- 2. Main 丿 (component A) ---
# Path: starts thin at top (顿笔 press quickly), runs nearly vertical
# then bows left. Widens slightly toward the foot then tapers at very end.
# We break into a mostly-straight vertical + a leftward arc via samples.
main_path = [
    (81, 92),   # tip / start
    (94, 108),  # after initial press
    (94, 130),
    (93, 160),
    (93, 190),
    (90, 215),
    (86, 235),
    (78, 252),
    (65, 265),
    (50, 272),
    (40, 276),
]
# Start slim (thin tip), swell in middle, taper at very tail.
# Approximate with two passes: main body thick, then a slim tail overlay.
dab_stroke(main_path[:8], r_start=1.8, r_end=3.2)  # top→mid: builds up
dab_stroke(main_path[7:], r_start=3.2, r_end=1.0)  # curved tail: tapers to point

# --- 3. Upper-right diagonal (component B) ---
# Short thick down-right stroke, thin at top-left → thicker mid → tapered tip.
right_path = [
    (124, 106),
    (135, 120),
    (150, 138),
    (165, 155),
    (173, 166),
]
# Two overlapping passes: first pass thin→thick (build to belly),
# second pass thick→thin (taper to tip). Smooth, no lump.
dab_stroke(right_path[:3], r_start=1.8, r_end=3.2)
dab_stroke(right_path[2:], r_start=3.2, r_end=1.2)

# --- Save ---
out = os.path.join(os.path.dirname(__file__), "01_丿.png")
img.save(out)
print(f"wrote {out}")
