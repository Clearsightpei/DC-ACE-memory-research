"""Render 年 (year) at 300x300 for G2.

Stroke order (6 strokes):
1. 撇 (short flick top)
2. 横 (short horizontal, upper)
3. 横 (middle horizontal, medium)
4. 撇/竖 short down (small connector)
5. 横 (long horizontal, main crossbar, wide)
6. 竖 (long vertical through center to bottom)

Consulted memory_index: 年 is NOT on the sibling-signature list.
No hooks in 年 — so no flick-up-and-left rule applies.
Silhouette: tall-ish, main crossbar wide, vertical spine centered
slightly right-of-center. Center of mass mid-lower due to long tail.
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=10):
    """Draw a polyline with rounded joints using thick line + circles."""
    d.line(pts, fill="black", width=width, joint="curve")
    for x, y in pts:
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def taper_line(p0, p1, w0, w1, steps=None):
    """Line that tapers from w0 at p0 to w1 at p1 (dense ellipse dabs)."""
    dist = math.hypot(p1[0] - p0[0], p1[1] - p0[1])
    if steps is None:
        steps = max(int(dist * 6), 12)
    for i in range(steps):
        t = i / (steps - 1)
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = (w0 + (w1 - w0) * t) / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---- Stroke 1: 撇 (short, top) — from upper-right going down-left
# starts near (170, 55) ends near (110, 110)
taper_line((170, 55), (108, 108), 11, 6, steps=30)

# ---- Stroke 2: 短横 (short horizontal, upper) — from top-cross area
# roughly (135, 90) to (200, 82) slight upward tilt
taper_line((140, 92), (210, 85), 8, 9, steps=20)

# ---- Stroke 3: 短撇 second small flick / short 撇 — connector
# from top-right going down-left small
taper_line((175, 105), (135, 145), 9, 6, steps=20)

# ---- Stroke 4: 中横 (middle horizontal) — shorter than main
# roughly (105, 155) to (215, 148)
taper_line((105, 158), (218, 150), 8, 9, steps=22)

# ---- Stroke 5: 长横 (main long horizontal crossbar) — very wide
# from (40, 205) to (270, 200) slight upward tilt
taper_line((42, 208), (272, 202), 10, 11, steps=40)

# ---- Stroke 6: 长竖 (long vertical spine) — from top down through
# the crossbars, slightly right-of-center, extending to bottom
# from about (168, 90) to (168, 285), slight leftward drift at bottom
taper_line((170, 92), (168, 285), 11, 10, steps=50)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0227_年/01_年.png"
img.save(out)
print(f"Saved {out}")
