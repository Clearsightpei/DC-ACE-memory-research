"""
Retry #1 of 几.

Prior attempt problem (vs GT):
- Silhouette too small/compressed — GT fills more vertical extent.
- Right 横折弯钩's arc + hook was underscaled; hook barely visible.
- The 撇 stopped too high — GT's 撇 sweeps all the way to the lower-left corner.

Fix per errata "p3_char_0021_几":
- 2 strokes: 撇 (left) + 横折弯钩 (right, KEY PRIMITIVE).
- Enlarge everything vertically. Silhouette open at the bottom.
- Hook flicks decisively UP-LEFT with r=7→1 taper, ~50 px.
- Small gap between 撇 top and 横 left end (几 signature).

Brush-dab PIL renderer.
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


def bezier_dab(p0, p1, p2, r_start, r_end, steps=260):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def arc_tangent(x0, y0, R, r=6, steps=100, direction="right"):
    """Starts at (x0,y0) with downward tangent, curves to horizontal (right)."""
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
# Enlarged: starts high inside near (108, 78), belly-on-right bow,
# sweeps down-left to (48, 275). Fills vertical extent.
# ============================================================
dab(108, 80, 7)  # 顿 press at start
bezier_dab(
    p0=(108, 80),
    p1=(112, 190),   # control pulled right → belly-on-right bow
    p2=(48, 275),
    r_start=7.0,
    r_end=1.2,
    steps=280,
)

# ============================================================
# STROKE 2 — 横折弯钩 (KEY PRIMITIVE)
# Beat 1: 横 from (122, 74) → (238, 78) — wide top
# Beat 2: shoulder dab (right corner)
# Beat 3: 竖 straight down from (238, 78) to (238, 220)
# Beat 4: tangent arc, R=32, ends at (270, 252) — sweeps right
# Beat 5: hook flick decisively UP-LEFT ~55 px @ -140°
# ============================================================

# Beat 1: 横 (wide top bar)
dab(122, 74, 6.5)
line_dab(122, 74, 238, 78, r_start=6.0, r_end=6.5)

# Shoulder dab at right corner
dab(238, 78, 8)

# Beat 3: 竖 straight down (long)
line_dab(238, 78, 238, 220, r_start=6.8, r_end=6.8)

# Beat 4: tangent arc curving right
arc_end_x, arc_end_y = arc_tangent(238, 220, R=32, r=6.5, steps=110, direction="right")
# arc_end_x = 270, arc_end_y = 252

# Beat 5: hook flick decisively up-and-left
hx0, hy0 = arc_end_x, arc_end_y
hook_len = 55
hook_angle = math.radians(-140)  # up-left
hx1 = hx0 + hook_len * math.cos(hook_angle)
hy1 = hy0 + hook_len * math.sin(hook_angle)
line_dab(hx0, hy0, hx1, hy1, r_start=7.0, r_end=1.0, steps=170)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0021_几__retry_1/01_几.png")
print("wrote 01_几.png")
