"""
Render 几 (jǐ) — 2 strokes: 撇 (left) + 横折弯钩 (right).

Redraw against the CLEAN GT (regenerated).

Design from GT observation:
- Silhouette: taller than wide, occupying the middle-top ~70% of canvas.
- Stroke 1 (撇): starts high near upper-left interior at ~(115, 85), sweeps
  down and left with belly-on-right bow, ending near (60, 260). Tapered end.
- Stroke 2 (横折弯钩): 横 across top from ~(125, 80) to ~(220, 85), light
  shoulder dab, 竖 straight down to ~(220, 210), tangent arc curving right
  to ~(245, 235), then a big up-left hook flick to ~(215, 210).
- Small gap between 撇's top and 横's left end (a signature of 几).

Brush-dab renderer with taper.
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dab(x0, y0, x1, y1, r_start, r_end, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(int(dist * 2.5), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dab(p0, p1, p2, r_start, r_end, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def arc_tangent(x0, y0, R, r=6, steps=90, direction="right"):
    """Starts at (x0,y0) with downward tangent, curves to horizontal."""
    for i in range(steps + 1):
        t = i / steps
        if direction == "right":
            x = x0 + R * (1 - math.cos(t * math.pi / 2))
        else:
            x = x0 - R * (1 - math.cos(t * math.pi / 2))
        y = y0 + R * math.sin(t * math.pi / 2)
        dab(x, y, r)
    end_x = x0 + R if direction == "right" else x0 - R
    end_y = y0 + R
    return end_x, end_y


# ============================================================
# STROKE 1 — 撇 (left stroke of 几)
# Starts high at ~(115, 85), belly-on-right, ends tapered at ~(60, 260)
# ============================================================
dab(115, 88, 7)  # 顿 press at start
bezier_dab(
    p0=(115, 88),
    p1=(120, 180),   # control pulled right → belly-on-right bow
    p2=(58, 262),
    r_start=6.5,
    r_end=1.2,
    steps=260,
)

# ============================================================
# STROKE 2 — 横折弯钩
# Beat 1: 横 from (125, 82) → (222, 86) — subtle slight down-tilt
# Beat 2: shoulder dab
# Beat 3: 竖 down to (222, 208)
# Beat 4: tangent arc, R=28, ends at (250, 236)
# Beat 5: hook flick up-and-left ~55 px
# ============================================================

# Beat 1: 横 — with slight starting dab, uniform width
dab(125, 82, 6.5)
line_dab(125, 82, 222, 86, r_start=5.8, r_end=6.2)

# Shoulder dab
dab(222, 86, 8)

# Beat 3: 竖 straight down
line_dab(222, 86, 222, 208, r_start=6.8, r_end=6.8)

# Beat 4: tangent arc into rightward
arc_end_x, arc_end_y = arc_tangent(222, 208, R=28, r=6.5, steps=100, direction="right")
# arc_end_x = 250, arc_end_y = 236

# Beat 5: hook flick up-and-left ~55 px @ ~-145°
hx0, hy0 = arc_end_x, arc_end_y
hook_len = 55
hook_angle = math.radians(-145)
hx1 = hx0 + hook_len * math.cos(hook_angle)
hy1 = hy0 + hook_len * math.sin(hook_angle)
line_dab(hx0, hy0, hx1, hy1, r_start=7.0, r_end=1.2, steps=160)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0021_几/01_几.png")
print("wrote 01_几.png")
