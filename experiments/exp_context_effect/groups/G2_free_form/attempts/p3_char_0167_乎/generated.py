"""
乎 — 5 strokes:
1. Top short 撇 (small flick from upper-right to lower-left, near top)
2. Left 点 (small dot below-left of the 撇)
3. Right 点 (small dot below-right)
4. Long 横 (horizontal bar crossing the middle)
5. 竖钩 (vertical descending from just above the 横 center, ending with UP-LEFT flick)

Memory notes consulted:
- TIER-0 B: hook flicks UP-and-LEFT (~-100 to -110). Applied to stroke 5.
- form_catalog "撇 as top-lid" — stroke 1 is short, ~40-60 px.
- 乎 not in sibling-signature list; free composition.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width_start=6, width_end=6):
    """Draw a tapered polyline via overlapping ellipses."""
    n = len(pts)
    if n < 2:
        return
    # Densify
    dense = []
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        seg_len = math.hypot(x1 - x0, y1 - y0)
        steps = max(2, int(seg_len))
        for s in range(steps):
            t = s / steps
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    total = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(1, total - 1)
        w = width_start + (width_end - width_start) * t
        r = w / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# 1) Top 撇 — longer curved flick from upper-right down to lower-left
stroke([(190, 50), (165, 75), (135, 105), (100, 130)], width_start=7, width_end=3)

# 2) Left 点 — small teardrop, slanting down-right (tucks under 撇 near top)
stroke([(125, 85), (140, 115)], width_start=3, width_end=8)

# 3) Right 点 — small teardrop on right, slanting down-right (matches GT which slants down-right)
stroke([(195, 95), (210, 130)], width_start=3, width_end=8)

# 4) Long 横 — sweeping horizontal across, slight upward tilt (calligraphic)
stroke([(40, 180), (260, 168)], width_start=7, width_end=8)

# 5) 竖钩 — vertical descending from just above 横 center, ending with UP-LEFT hook
# Main vertical body — slight rightward lean at top, straightens
stroke([(155, 140), (152, 260)], width_start=8, width_end=7)
# Hook flick UP-and-LEFT (~-115 deg) — pronounced hook curling back
stroke([(152, 260), (138, 252), (125, 238), (118, 222)], width_start=7, width_end=3)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0167_乎/01_乎.png")
print("Saved 01_乎.png")
