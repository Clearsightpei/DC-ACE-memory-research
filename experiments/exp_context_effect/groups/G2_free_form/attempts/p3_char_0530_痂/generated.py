"""Render 痂 (jiā, scab) at 300x300, black on white.

TIER-0 F 4-move + TIER-0 H (components must touch).
Sibling-risk components: 力/口 are simple; 疒 is the ID-carrying canopy.

Structure (10 strokes total):
  疒 canopy (5 strokes) — decomposed per drawer_memory pos-900:
    1. 点 top-right (short slanted dot ABOVE the 横)
    2. 横 top (long horizontal spanning canopy width)
    3. 点 inside-upper-left (short flick, inside the canopy)
    4. 提 inside-lower-left (rising flick below the 点)
    5. 长撇 sweeping from top-横's left endpoint down to bottom-left

  加 body (5 strokes) tucked INSIDE the canopy (touching the 撇):
    力 (2 strokes) on the left of the interior:
      6. 横折钩 (top horizontal → down → up-left hook)
      7. 撇 sweeping from top-inside down-left
    口 (3 strokes) on the right of the interior:
      8. 竖 (left vertical of 口)
      9. 横折 (top + right side)
     10. 横 (bottom of 口)

Components MUST touch: 加's leftmost stroke (力's 撇) should tuck just
inside the 疒 撇 sweep; 力 and 口 sit shoulder-to-shoulder with no gap.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab_line(pts, width_start=8, width_end=8):
    """Variable-width polyline via overlapping circles (tapered stroke)."""
    if len(pts) < 2:
        return
    n_seg = len(pts) - 1
    for si in range(n_seg):
        x0, y0 = pts[si]
        x1, y1 = pts[si + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for t in range(steps + 1):
            u = t / steps
            global_u = (si + u) / n_seg
            w = width_start * (1 - global_u) + width_end * global_u
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            r = w / 2
            d.ellipse([x - r, y - r, x + r, y + r], fill="black")


# ============= 疒 CANOPY (5 strokes) =============
# Stroke 1: 点 top-right (above the 横)
dab_line([(140, 42), (158, 70)], width_start=4, width_end=8)

# Stroke 2: 横 top (long horizontal — spans canopy full width)
dab_line([(85, 92), (150, 90), (245, 96)], width_start=6, width_end=7)

# Stroke 3: 点 inside upper-left (below the 横, right of the 撇)
dab_line([(58, 128), (78, 148)], width_start=4, width_end=8)

# Stroke 4: 提 inside lower-left (rising flick)
dab_line([(48, 195), (85, 175)], width_start=8, width_end=3)

# Stroke 5: 长撇 (long sweeping descender from top-横's left end)
long_pie = [
    (88, 92),
    (86, 135),
    (80, 180),
    (65, 225),
    (45, 265),
    (30, 282),
]
dab_line(long_pie, width_start=9, width_end=4)


# ============= 加 BODY (5 strokes) — inside canopy, tucked under 撇 =============
# 力 on the left of the interior (compact, ~x=95-165)
# Stroke 6: 横折钩 — top horizontal → down → hook up-left
# Draw as connected polyline
lidh = [
    (110, 140),   # top-left corner of 力
    (168, 138),   # top-right corner
    (167, 165),   # small shoulder (顿笔 press)
]
dab_line(lidh, width_start=6, width_end=8)
# down segment
lidh_down = [(167, 165), (162, 235)]
dab_line(lidh_down, width_start=8, width_end=8)
# hook flick UP-and-LEFT (TIER-0 B rule)
hook_flick = [(162, 235), (146, 220)]
dab_line(hook_flick, width_start=8, width_end=3)

# Stroke 7: 撇 sweeping from top of 力 down-left to bottom
li_pie = [
    (138, 145),
    (132, 175),
    (122, 210),
    (108, 245),
    (95, 268),
]
dab_line(li_pie, width_start=7, width_end=3)

# 口 on the right of the interior (compact, ~x=180-255, y=155-250)
# Stroke 8: 竖 (left vertical of 口)
dab_line([(185, 165), (185, 250)], width_start=6, width_end=6)

# Stroke 9: 横折 (top + right side)
kou_hz = [(185, 165), (250, 163), (250, 250)]
dab_line(kou_hz, width_start=6, width_end=7)

# Stroke 10: 横 (bottom of 口)
dab_line([(185, 250), (250, 250)], width_start=7, width_end=7)


img.save("01_痂.png")
print("saved 01_痂.png")
