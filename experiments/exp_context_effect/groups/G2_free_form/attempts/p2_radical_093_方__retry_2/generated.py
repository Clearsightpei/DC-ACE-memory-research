"""
方 (radical, 4 strokes) — RETRY 2.

Retry_1 diagnosis (from errata B3 fix note):
"亠 top present but body 横折钩 + crossing 撇 imbalanced, reads too narrow.
Fix: increase body x-extent to fill ~70% width; the crossing 撇 must sweep
clearly outside the 横折钩's right wall on its way to lower-left."

Retry_1 observed problems from own PNG vs GT:
- 横折钩 rendered as a mostly-STRAIGHT vertical drop — GT has a clearly
  CURVED body (belly-on-right, arcs down and hooks up-left, enclosing a
  ㄉ-like area).
- 撇 started at x=172 (which was INSIDE the 横折钩's top-right corner at
  x=218), and its bezier path stayed roughly between the two 竖-line
  bodies — so the crossing didn't sweep clearly outside the right wall.
- Overall body compressed vertically; ended looking like 力 rather than 方.

This retry applies (from form_catalog + errata fix):
- 横折钩 as a proper CURVED enclose (belly-on-right, tangent arc into a
  bottom hook up-and-left). Uses bezier P1 pulled RIGHT of chord.
- 撇 crosses OUTSIDE the right wall on its way down — start high and
  right of the 横折钩 top corner, sweep left past the shoulder, then
  diagonally down-left past the arc's bottom.
- Body widened to ~x=55..250 span for the 横 (~195 px, ~65% width).

Stroke order (canonical MMH): 点、横、横折钩、撇.
"""

from PIL import Image, ImageDraw
import math, os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        steps = int(max(60, math.hypot(x1 - x0, y1 - y0) * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=240, ease=None):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = ease(t) if ease else t
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def draw_dot(x0, y0, x1, y1, r0=1.5, r1=5):
    steps = int(max(40, math.hypot(x1 - x0, y1 - y0) * 4))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        tt = t ** 1.4
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    dab(x1, y1, r1 + 0.5)


# ---- Stroke 1: 点 (top dot) — small teardrop angling down-right,
# sits ABOVE the top 横, centered a hair right of middle.
draw_dot(142, 42, 165, 74, r0=1.3, r1=4.4)

# ---- Stroke 2: 横 (top horizontal) — wider than retry_1: x=55..248 (193 px).
h_x0, h_y0 = 55, 100
h_x1, h_y1 = 248, 92
dab(h_x0, h_y0, 4.5)                       # 顿 start
line_dabs(h_x0, h_y0, h_x1, h_y1, 3.4, 3.4)
dab(h_x1, h_y1, 4.8)                       # 顿 end (bigger — this becomes shoulder anchor)

# ---- Stroke 3: 横折钩 — CURVED enclose (belly-on-right).
# Starts at the RIGHT end of the top 横 (shoulder), then arcs down and
# left, terminating in an up-and-left hook. This makes an enclosed
# ㄉ-like belly on the lower right — the signature of 方.
#
# Use a bezier from shoulder (x≈230, y≈100) — slightly inside the top
# 横's right endpoint (so shoulder reads as a joint, not an isolated
# stroke) — arcing to the bottom (x≈115, y≈258) with control point
# pulled RIGHT (belly-on-right): P1 at (255, 210).
sh_x, sh_y = 230, 100
bot_x, bot_y = 135, 258
ctl_x, ctl_y = 245, 205
dab(sh_x, sh_y, 5.0)  # shoulder dab
bezier_dabs((sh_x, sh_y), (ctl_x, ctl_y), (bot_x, bot_y),
            r_start=4.2, r_end=3.6, steps=280)
# Terminal 钩 flick up-and-slightly-left ~-125°, ~34 px, taper 3.6→1.0
hook_len = 34
hook_angle_deg = -125
ha = math.radians(hook_angle_deg)
hk_x = bot_x + hook_len * math.cos(ha)
hk_y = bot_y + hook_len * math.sin(ha)
line_dabs(bot_x, bot_y, hk_x, hk_y, 3.6, 1.0)

# ---- Stroke 4: 撇 — LONG body-crossing diagonal.
# MUST start ABOVE and OUTSIDE the 横折钩's shoulder so its top is
# visibly above the 横 and its body passes THROUGH the 横 then sweeps
# past the arc's right belly out to lower-left.
#
# Start high (y=52) and to the RIGHT of the shoulder (x=210), then bow
# with control pulled RIGHT of chord — so the middle of the 撇 arcs
# through the arc's right-belly region — and end at lower-left (y=272,
# x=42), well outside the arc's bottom endpoint (x=115).
p0 = (195, 55)
p2 = (48, 268)
p1 = (155, 175)   # control pulled right of chord midpoint (chord mid ≈ (122, 162))
                  # → gives the 撇 a modest rightward bow so it sweeps
                  # across the 横 and past the 横折钩's inner-belly to lower-left
dab(p0[0], p0[1], 5.5)  # 顿 press at start
bezier_dabs(p0, p1, p2, r_start=5.0, r_end=1.2, steps=320)

out = os.path.join(os.path.dirname(__file__), "01_方.png")
img.save(out)
print(f"wrote {out} ({img.size})")
