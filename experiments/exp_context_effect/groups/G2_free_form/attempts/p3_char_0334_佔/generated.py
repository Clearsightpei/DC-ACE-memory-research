"""
佔 = 亻 (left, person radical) + 占 (right, 卜 on top + 口 on bottom)

Layout:
- Left third: 亻  (slanted 撇 from top-right of radical downward-left,
  then a vertical 竖 dropping from the joint area)
- Right two-thirds: 占
    - Top: 卜 (short horizontal 一, vertical 丨, and a dot 丶 on the right)
    - Bottom: 口 (rectangle box)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6


def stroke(pts, width=LW):
    """Draw a polyline with rounded joints."""
    d.line(pts, fill=INK, width=width, joint="curve")
    # dabs at endpoints for calligraphic feel
    for x, y in (pts[0], pts[-1]):
        d.ellipse((x - width / 2 + 0.5, y - width / 2 + 0.5,
                   x + width / 2 - 0.5, y + width / 2 - 0.5), fill=INK)


# ---------------- 亻 (left radical) ----------------
# 撇: from a point near top-center of left region, sweeping down-left
pie_pts = [(95, 55), (90, 90), (78, 135), (58, 200), (40, 255)]
stroke(pie_pts, width=6)

# 竖: vertical starting from just under the 撇's upper portion, dropping down
# The 亻 vertical typically starts on the 撇's midway and drops straight
stroke([(88, 115), (88, 260)], width=6)

# ---------------- 占 (right side) ----------------
# --- 卜 (top) ---
# Short horizontal 一 near the top of the right block
stroke([(155, 90), (240, 90)], width=6)
# Vertical 丨 going down from the horizontal (slightly left of center)
stroke([(180, 60), (180, 165)], width=6)
# Dot 丶 on the right side of the vertical (a short slanted stroke)
stroke([(210, 115), (230, 140)], width=7)

# --- 口 (bottom rectangle) ---
# Left vertical
stroke([(150, 180), (150, 265)], width=6)
# Top horizontal (with slight折 at right — done as two strokes)
stroke([(150, 180), (245, 180)], width=6)
# Right vertical (from top-right down)
stroke([(245, 180), (245, 265)], width=6)
# Bottom horizontal
stroke([(150, 265), (245, 265)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0334_佔/01_佔.png")
print("Saved.")
