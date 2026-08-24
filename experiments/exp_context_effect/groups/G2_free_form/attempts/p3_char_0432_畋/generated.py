"""
畋 = 田 (left) + 攵 (right)

Component plan (300x300, image coords, y grows DOWN):
  LEFT  — 田 as compressed left-radical box:
          box roughly (40, 85) -> (140, 215), with internal cross.
          5 strokes: left竖, 横折(top+right), inner横, inner竖, bottom横.
  RIGHT — 攵 (4 strokes: 撇, 横, 撇, 捺):
          top 短撇 (upper-left throw around (200,80)->(175,110)),
          middle 横 (~x=155->240, y=125),
          long 撇 crossing from upper-right (225,110)->(155,240),
          捺 crossing from mid (185,150) sweeping to (275,240) with broad foot.

Sibling risk: 攵 vs 攴 — do NOT add extra 丶. Only 4 strokes on the right.
Left is a clean 田 box (no through-竖 like 甲/申/由).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r_start, r_end, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_bezier(p0, p1, p2, r_start, r_end, steps=200):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dot_dab(pt, r):
    x, y = pt
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---------------- LEFT: 田 (compressed left radical) ----------------
# Box corners
L, T, R, B = 40, 85, 140, 215

# 1) Left 竖 wall (top to bottom)
dab_line((L, T), (L, B), 3.5, 3.5)
dot_dab((L, T), 4.0)  # top-left corner dab

# 2) Top 横 (left to right, slight up-tilt) + shoulder + right 竖 (横折)
dab_line((L, T), (R, T - 2), 3.0, 3.5)  # top 横 with small up-tilt
dot_dab((R, T - 2), 4.5)                # shoulder press
dab_line((R, T - 2), (R, B), 3.5, 3.5)  # right 竖 wall

# 3) Inner 横 middle divider
midY = (T + B) // 2
dab_line((L + 3, midY), (R - 3, midY), 3.0, 3.0)

# 4) Inner 竖 middle divider
midX = (L + R) // 2
dab_line((midX, T + 3), (midX, B - 3), 3.0, 3.0)

# 5) Bottom 横 closer
dab_line((L, B), (R, B), 3.5, 3.5)


# ---------------- RIGHT: 攵 ----------------
# Stroke 1: short 撇 at top — starts higher/further-right, more visible splay
dab_bezier((218, 65), (198, 90), (170, 118), 3.8, 1.4)

# Stroke 2: 横 middle bar with tiny up-tilt, small end press
dab_line((155, 132), (250, 128), 2.8, 3.5)
dot_dab((250, 128), 3.8)

# Stroke 3: long 撇 from upper-right area, sweeping down-left, gentle bow.
# Start above/right of 横, cross through 横 around x=225, end lower-left.
dab_bezier((238, 105), (188, 190), (148, 250), 4.8, 1.2)

# Stroke 4: 捺 starting near the 撇/横 crossing (around 200,145),
# sweeping down-right with broad flat foot around (280, 245).
dab_bezier((200, 148), (240, 200), (282, 248), 1.6, 6.0)
# Broad foot terminal press (捺 signature)
dot_dab((282, 248), 6.5)
dot_dab((278, 246), 5.5)


img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/p3_char_0432_畋/01_畋.png"
)
print("wrote 01_畋.png")
