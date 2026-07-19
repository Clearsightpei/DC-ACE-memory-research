"""
Render the radical 山 (mountain, 3 strokes) to a 300x300 white PNG,
black ink, using PIL brush-dab technique.

Stroke order (MMH standard):
  1. 竖 (middle vertical) — tallest, centered around x=150.
  2. 竖折 (left down + horizontal right across bottom) — one compound stroke.
     Short 竖 on the left going down, then a shoulder-dab, then a 横
     going rightward all the way across (forms the base of 山).
  3. 竖 (right vertical) — shorter than the middle, on the right.

The three verticals sit on the base 横; the middle rises well above
the outer two. The outer two heights are comparable but the right may
be slightly shorter than the left down-beat of stroke 2 (per GT).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------------------------------------------------------------------------
# Stroke 1: middle 竖 (tallest vertical)
# Sits roughly at x=150, from top-ish down to (just above / meeting) the base.
# ---------------------------------------------------------------------------
mid_x = 150
mid_y_top = 55
mid_y_bot = 225
r_mid = 5
# subtle 顿 press at start (no visible ball — standalone scale)
dab(mid_x, mid_y_top, r_mid + 1)
line_dabs(mid_x, mid_y_top, mid_x, mid_y_bot, r_mid, r_mid)
# blunt terminal — meets the base 横, plain radius
dab(mid_x, mid_y_bot, r_mid)

# ---------------------------------------------------------------------------
# Stroke 2: 竖折 — left short 竖 down, shoulder, then long 横 across the base.
# The 横 forms the bottom line of 山 and extends all the way to the right side.
# ---------------------------------------------------------------------------
left_x = 70
top_y = 130           # left vertical starts partway down (shorter than middle)
corner_y = 235        # base of the character (bottom of the U)
right_x_end = 245     # where the 横 ends on the right (near right stroke)

r_body = 5
# subtle 顿 press at top of left 竖 (no visible ball)
dab(left_x, top_y, r_body + 1)
# left 竖 down
line_dabs(left_x, top_y, left_x, corner_y, r_body, r_body)
# shoulder dab at corner (real 折 — keep r+2 press per memory)
dab(left_x, corner_y, r_body + 2)
# 横 across bottom, slight upward tilt (traditional 横 tilts up ~2-3°)
line_dabs(left_x, corner_y, right_x_end, corner_y - 3, r_body, r_body)
# terminal press at right end of the 横 — subtle
dab(right_x_end, corner_y - 3, r_body)

# ---------------------------------------------------------------------------
# Stroke 3: right 竖 — sits on the right side, shorter than the middle,
# comparable height to the left down-beat, meets the base 横.
# ---------------------------------------------------------------------------
right_x = 235
right_y_top = 115
right_y_bot = corner_y - 3  # meets the base horizontal
r_right = 5
# subtle 顿 press at top (standalone — no visible ball)
dab(right_x, right_y_top, r_right + 1)
line_dabs(right_x, right_y_top, right_x, right_y_bot, r_right, r_right)
# join into the base (no extra dab needed — base terminal already sits here)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
out = "01_山.png"
img.save(out)
print(f"wrote {out}")
