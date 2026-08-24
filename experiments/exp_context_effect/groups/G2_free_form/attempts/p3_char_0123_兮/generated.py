"""
p3_char_0123_兮 — 4 strokes

Structure (from GT):
  1. 撇 — short left-flick, upper-left of top region (~x=90 y=100 → x=55 y=175)
  2. 长横/斜捺-like — starts mid-upper (~x=125 y=95), slight arc up over the top,
     ends far-right and slightly down (~x=245 y=140). This is the wide top "cover".
     Actually per 兮 canonical: it's 横撇 or long slanting-捺 forming the top over the 丂.
     Looking at GT more carefully: a wide slightly-downward stroke from mid-top-left
     out to top-right, ending with a slight hook back down.
  3. 横 — middle horizontal, moderate length (~x=80 y=175 → x=225 y=175)
  4. 亅 (small hook) — short vertical from (~x=155 y=180) going down to (~x=155 y=245),
     ending in a small leftward hook.

Uses PIL with brush-dab technique for ink-like strokes.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def stroke(points, widths):
    """Draw a stroke as densely dabbed circles interpolated along polyline.
    points: list of (x,y). widths: list of half-widths at each point (same len).
    """
    N = len(points)
    for i in range(N - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        w1, w2 = widths[i], widths[i + 1]
        seg_len = math.hypot(x2 - x1, y2 - y1)
        steps = max(2, int(seg_len * 2))
        for s in range(steps + 1):
            t = s / steps
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            w = w1 + (w2 - w1) * t
            dab(x, y, w)


# Stroke 1: 撇 — short left-flick top
stroke(
    [(95, 100), (80, 130), (60, 165), (48, 180)],
    [5.5, 5.0, 4.0, 2.0],
)

# Stroke 2: long slanting top "cover" — starts around mid-upper, arcs to upper right,
# then curves down slightly to right side. Ends with a tiny down-flick.
stroke(
    [(115, 105), (145, 88), (185, 80), (225, 90), (255, 120), (262, 145)],
    [4.5, 5.0, 5.5, 5.5, 4.5, 3.0],
)

# Stroke 3: middle 横 (wide)
stroke(
    [(60, 178), (120, 173), (180, 174), (240, 180)],
    [4.0, 5.0, 5.0, 4.0],
)

# Stroke 4: small 亅 vertical with left hook at bottom
stroke(
    [(158, 185), (158, 220), (156, 245), (145, 252), (130, 250)],
    [5.0, 5.0, 4.5, 3.5, 2.5],
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0123_兮/01_兮.png"
)
print("saved 01_兮.png")
