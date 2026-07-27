"""
方 (Phase 3 character, 4 strokes).

Consulted memory:
- memory_index → HOT LOOKUP: no direct entry, but form_catalog line 49
  "撇 as top-lid (dot-撇, as in 亠, 户 top, 方 top)" — the top-of-方 is
  a stubby dot-撇, not a full 撇.
- Prior p2_radical_093_方__retry_1 attempt (same character as a radical)
  used a clean 4-stroke composition; adapting it here for Phase 3.

Stroke order (canonical MMH): 点、横、横折钩、撇.

Geometry vs GT:
1. 点 top dot — small teardrop slightly right-of-center, angling
   down-right, sits ABOVE the top 横 with ~15 px gap.
2. 横 top horizontal — moderate width (~170 px), slight up-tilt,
   with 顿 dabs at both ends.
3. 横折钩 — starts UNDER the top 横 at the right side, 折 shoulder at
   ~y=115, drops nearly-vertical leaning slightly left, terminates in
   an up-and-left hook.
4. 撇 — LONG body-crossing diagonal, starts ABOVE the top 横 so the
   crossing is visible, sweeps to lower-left with a gentle rightward
   bow, tapered tail.
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


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200, ease=None):
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


# ---- Stroke 1: 点 (top dot)
draw_dot(148, 55, 168, 82, r0=1.4, r1=4.2)

# ---- Stroke 2: 横 (top horizontal)
h_x0, h_y0 = 65, 108
h_x1, h_y1 = 235, 100
dab(h_x0, h_y0, 4.5)                       # 顿 start
line_dabs(h_x0, h_y0, h_x1, h_y1, 3.4, 3.4)
dab(h_x1, h_y1, 4.5)                       # 顿 end

# ---- Stroke 3: 横折钩
zg_top_x, zg_top_y = 218, 115
zg_bot_x, zg_bot_y = 205, 240
dab(zg_top_x, zg_top_y, 5.0)               # 折 shoulder dab
line_dabs(zg_top_x, zg_top_y, zg_bot_x, zg_bot_y, 3.6, 3.6)
# hook flick up-and-left ~-130°, ~34 px, taper r=3.6→1.0
hook_len = 34
hook_angle_deg = -128
ha = math.radians(hook_angle_deg)
hk_x = zg_bot_x + hook_len * math.cos(ha)
hk_y = zg_bot_y + hook_len * math.sin(ha)
line_dabs(zg_bot_x, zg_bot_y, hk_x, hk_y, 3.6, 1.0)

# ---- Stroke 4: 撇 — LONG body-crossing diagonal
p0 = (172, 70)      # top ABOVE the 横
p2 = (55, 265)      # lower-left tail
p1 = (145, 175)     # control pulled right for gentle bow
bezier_dabs(p0, p1, p2, r_start=5.5, r_end=1.2, steps=280)
dab(p0[0], p0[1], 5.5)                     # 顿 press at start

out = os.path.join(os.path.dirname(__file__), "01_方.png")
img.save(out)
print(f"wrote {out} ({img.size})")
