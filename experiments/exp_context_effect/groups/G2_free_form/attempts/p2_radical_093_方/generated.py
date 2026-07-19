"""
Render 方 (radical, 4 strokes) at 300x300, PIL brush-dab technique.

Stroke order for 方:
  1. 点 (dian)   - top dot, angled down-right (short teardrop)
  2. 横 (heng)   - horizontal beneath the dot
  3. 横折钩      - starts as short 横 top-right (already implicit under top 横?)
     Actually 方 = 点 + 横 + 横折钩 + 撇 (stroke order per MMH).
     Wait: standard: 点, 横, 撇, 横折钩. Looking at GT more carefully:
     - top dot
     - top horizontal
     - long 撇 sweeping from top area to lower-left
     - the right side has a vertical dropping into a bottom hook (横折钩)
       BUT the top of that 横折钩 rides ON the top horizontal.

Actually the canonical order is 点、横、横折钩、撇 (4 strokes).
The 横折钩 shares its top-横 with the main top 横? No — the top 横
is stroke #2; then stroke #3 (横折钩) starts near the right end of
that 横 and drops down with a hook. The GT shows the top 横 extends
further left than the 横折钩's top; the 横折钩 sits under it.

Actually looking at GT again: there's a top dot, then a wide horizontal,
then a shape resembling 万 (which is 一 + 𠃌 + 丿). 方 = 亠 top +
万-like body. Let me render as:
  1. 点 top
  2. 横 (long horizontal)
  3. 撇 long from top-right sweeping to bottom-left
  4. 横折钩 starting from just under the top 横 on the right,
     going right briefly then vertical down with hook.

Wait — in 方 the 横折钩 is a single stroke that starts at TOP-RIGHT,
goes rightward a short bit (or is fused with the top 横?), turns down,
and hooks. In the GT the top 横 already exists as stroke 2. Stroke
3 (横折钩) probably starts from the top-横's right end position, goes
right slightly (making a mini shoulder), then drops down to hook.

BUT what I see in the GT is a horizontal top-横 that extends across,
under which there's an enclosed shape formed by:
- a 撇 from upper-right to lower-left
- a 横折钩 forming the right side and bottom-turn

I'll interpret and render conservatively.
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


# ---- Stroke 1: 点 (top dot), angled down-right teardrop
# small dot above the horizontal, roughly centered but slightly left
def draw_dot(x0, y0, x1, y1, r0=1.8, r1=7):
    steps = int(max(50, math.hypot(x1 - x0, y1 - y0) * 4))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        tt = t ** 1.4
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    dab(x1, y1, r1 + 1)

# top dot: from upper-left going down-right — smaller for standalone
draw_dot(148, 60, 170, 82, r0=1.3, r1=4.5)

# ---- Stroke 2: 横 (top horizontal) — thinner uniform, no big end-balls
h_x0, h_y0 = 55, 118
h_x1, h_y1 = 250, 108   # slight up-tilt
dab(h_x0, h_y0, 4.2)    # subtle 顿 start (r+1 only for standalone)
line_dabs(h_x0, h_y0, h_x1, h_y1, 3.2, 3.2)
dab(h_x1, h_y1, 4.2)    # subtle 顿 end

# ---- Stroke 3: 横折钩 — vertical dropping from a point on the top 横,
# leans slightly left, ends in an up-left hook flick.
zg_top_x, zg_top_y = 215, 108
zg_bot_x, zg_bot_y = 208, 245   # slight lean-left is characteristic
dab(zg_top_x, zg_top_y, 5)      # shoulder dab (small — this IS a real 折 corner)
line_dabs(zg_top_x, zg_top_y, zg_bot_x, zg_bot_y, 3.5, 3.5)
# hook flick up-and-left from bottom
hook_len = 32
hook_angle_deg = -125
ha = math.radians(hook_angle_deg)
hk_x = zg_bot_x + hook_len * math.cos(ha)
hk_y = zg_bot_y + hook_len * math.sin(ha)
line_dabs(zg_bot_x, zg_bot_y, hk_x, hk_y, 3.5, 1.0)

# ---- Stroke 4: 撇 — long sweep from upper-right (under top 横) to
# lower-left, thick→thin taper with gentle rightward bow.
p0 = (170, 115)
p2 = (65, 265)
p1 = (150, 180)
bezier_dabs(p0, p1, p2, r_start=5.5, r_end=1.2, steps=280)
# small 顿 start dab (standalone: keep it modest)
dab(p0[0], p0[1], 5.5)

out = os.path.join(os.path.dirname(__file__), "01_方.png")
img.save(out)
print(f"wrote {out} ({img.size})")
