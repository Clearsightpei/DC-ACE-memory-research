"""Render 小 (xiǎo) at 300x300, white bg, black ink.

Structure (3 strokes):
  1) Center 竖钩 — vertical descending, with left-flick hook at bottom.
  2) Left 点 — short diagonal from upper-right to lower-left.
  3) Right 点 — short diagonal from upper-left to lower-right.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(pts, width=10):
    """Draw a thick smooth polyline with rounded ends and joints."""
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill="black", width=width)
    for p in pts:
        r = width / 2
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")


# --- Stroke 1: center 竖钩 ---
# Vertical shaft from top-center-ish down, then hook flicks left.
shaft_top = (155, 100)
shaft_bot = (152, 220)
hook_end = (125, 230)
stroke([shaft_top, shaft_bot, hook_end], width=9)

# --- Stroke 2: left 点 (short 撇-like flick from upper-right to lower-left) ---
# Starts thicker at top-right end, tapers toward bottom-left.
left_pts = [(105, 130), (85, 170)]
# Emulate a taper by drawing decreasing-width segments
for i, w in enumerate([11, 10, 9, 8, 7, 6]):
    t0 = i / 6
    t1 = (i + 1) / 6
    x0 = left_pts[0][0] + (left_pts[1][0] - left_pts[0][0]) * t0
    y0 = left_pts[0][1] + (left_pts[1][1] - left_pts[0][1]) * t0
    x1 = left_pts[0][0] + (left_pts[1][0] - left_pts[0][0]) * t1
    y1 = left_pts[0][1] + (left_pts[1][1] - left_pts[0][1]) * t1
    draw.line([(x0, y0), (x1, y1)], fill="black", width=w)

# --- Stroke 3: right 点 (short diagonal from upper-left to lower-right) ---
right_pts = [(195, 135), (220, 175)]
for i, w in enumerate([7, 8, 9, 10, 11, 12]):
    t0 = i / 6
    t1 = (i + 1) / 6
    x0 = right_pts[0][0] + (right_pts[1][0] - right_pts[0][0]) * t0
    y0 = right_pts[0][1] + (right_pts[1][1] - right_pts[0][1]) * t0
    x1 = right_pts[0][0] + (right_pts[1][0] - right_pts[0][0]) * t1
    y1 = right_pts[0][1] + (right_pts[1][1] - right_pts[0][1]) * t1
    draw.line([(x0, y0), (x1, y1)], fill="black", width=w)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0057_小/01_小.png")
