"""
Draw 已 (yǐ) — 3 strokes.

Sibling identity per form_catalog.md:
  己: middle 横 FLOATS (doesn't touch left wall)
  已: middle 横 TOUCHES left wall midway    <-- THIS ONE
  巳: middle 横 TOUCHES at top

Strokes:
  1. 横折 (top): horizontal from upper-left, turns down on right
  2. 横 (middle): originates from the left wall (midway), extends right
  3. 竖弯钩 (bottom): begins where stroke 1 started (upper-left),
     drops down as a vertical, curves right along bottom, terminates
     with an up-left hook flick.

Renderer: PIL, 300x300, white background, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
WIDTH = 8  # main stroke width


def line(p0, p1, w=WIDTH):
    draw.line([p0, p1], fill=BLACK, width=w)


def dot(p, r):
    x, y = p
    draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def polyline(pts, w=WIDTH):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w=w)
    for p in pts:
        dot(p, w // 2)


def bezier(p0, p1, p2, w=WIDTH, steps=120):
    """Quadratic Bezier sampled and drawn as short line segments."""
    prev = p0
    for i in range(1, steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        line(prev, (x, y), w=w)
        prev = (x, y)
    dot(p0, w // 2)


# ---- Layout for 已 -----------------------------------------------------
# Canvas 300x300. Use a compact 己/已-family layout occupying roughly
#   x: 70..230   (width ~160)
#   y: 75..245   (height ~170)
# Top-box (from stroke 1) roughly y=75..135, x=70..200
# Middle 横 at y ~= 145
# Bottom curve reaches y ~= 240

# Stroke 1: 横折
#   Horizontal segment: (75,80) -> (200,80)   顿笔 slight at start
#   Fold down:          (200,80) -> (200,140) then eases slightly right
p1_h_start = (75, 80)
p1_h_end   = (200, 82)
p1_v_start = (200, 82)
p1_v_end   = (203, 138)
# little starting 顿笔 dab
dot(p1_h_start, WIDTH // 2 + 1)
line(p1_h_start, p1_h_end, w=WIDTH)
line(p1_v_start, p1_v_end, w=WIDTH)
dot(p1_v_end, WIDTH // 2)

# Stroke 2: middle 横 — TOUCHES the left wall (stroke 3's vertical)
# Left wall x = 75 (matches stroke 3 start). Midway y = 145.
# Keep it shorter than stroke 1's horizontal — stops well before right wall.
p2_start = (75, 145)
p2_end   = (175, 145)
dot(p2_start, WIDTH // 2 + 1)
line(p2_start, p2_end, w=WIDTH)
dot(p2_end, WIDTH // 2)

# Stroke 3: 竖弯钩
# Starts at upper-left where stroke 1 originated: (75, 80)
# Runs down as a straight vertical to about (75, 210), then curves
# right along the bottom to about (220, 245), then hook flick
# up-and-slightly-left ending near (225, 218) (flick ~30 px, angled
# about -110° in image coords).
p3_v_start = (75, 80)
p3_v_end   = (75, 210)
# vertical
line(p3_v_start, p3_v_end, w=WIDTH)
dot(p3_v_start, WIDTH // 2 + 1)

# Curve from (75,210) sweeping right and slightly down to (225,245)
# Use a quadratic Bezier with control at (75, 245) for a smooth
# "L" corner that curves rather than bends sharply.
curve_p0 = (75, 210)
curve_p1 = (75, 250)   # control: hold left then release right
curve_p2 = (225, 245)
bezier(curve_p0, curve_p1, curve_p2, w=WIDTH, steps=140)

# Hook flick: from end of curve up-and-slightly-left ~30 px, ~ -110°
import math
hx, hy = 225, 245
angle_deg = -100  # image coords: -90 is straight up; -100 = slightly left
L = 45  # longer flick so it reads as a swept hook
hx2 = hx + L * math.cos(math.radians(angle_deg))
hy2 = hy + L * math.sin(math.radians(angle_deg))
# Taper the flick by drawing successively thinner segments
steps = 24
prev = (hx, hy)
for i in range(1, steps + 1):
    t = i / steps
    x = hx + (hx2 - hx) * t
    y = hy + (hy2 - hy) * t
    w = max(1, int(WIDTH * (1 - 0.75 * t)))
    line(prev, (x, y), w=w)
    prev = (x, y)


out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0079_已/01_已.png"
img.save(out)
print(f"wrote {out}")
