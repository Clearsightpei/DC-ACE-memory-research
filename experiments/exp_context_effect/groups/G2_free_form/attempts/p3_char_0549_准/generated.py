"""
p3_char_0549_准 — G2 render.

Structure (LR compound, per TIER-0 H = components MUST touch):
- Left radical: 冫 (two 点 dots on left column, upper + lower).
- Right body: 隹 = 亻 (撇 + 竖) + right sub-body with 撇, 横 top, then
  a central vertical crossed by four horizontals, terminating in a
  long bottom 横 that extends across the whole right region.

TIER-0 F 4-move applied:
  1. teardrop taper on all 撇 / 点 via stroke(widths=(a,b))
  2. shoulder dab at each 折 corner (none here, no 折 present)
  3. bezier for 撇 curvature
  4. no hooks in 准 (no 钩 stroke) — moot
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    """Tapered brush-dab stroke: interpolate widths across pts."""
    n = len(pts)
    if n < 2:
        return
    w0, w1 = widths
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        r = (w0 * (1 - t) + w1 * t) / 2.0
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dot(cx, cy, w0, w1, dx, dy):
    """A 点 stroke = short bezier with taper (thin->thick end)."""
    pts = bez((cx, cy), (cx + dx * 0.4, cy + dy * 0.4),
              (cx + dx * 0.7, cy + dy * 0.7), (cx + dx, cy + dy), n=24)
    stroke(pts, (w0, w1))


# ---------- 冫 (left, two dots) ----------
# upper 点: short flick from upper-right down to lower-left
dot(70, 75, 3, 8, -18, 22)
# lower 点 (提-like — actually 冫 second dot flicks up-right in some fonts,
# GT shows it as a small dot lower-left region ~y=175)
dot(50, 165, 3, 8, 20, 18)

# ---------- 亻 (left of 隹, human radical) ----------
# 撇: from top ~ (140, 55) sweeping down-left to (95, 205), curved
pie = bez((140, 55), (128, 110), (112, 165), (95, 210), n=70)
stroke(pie, (11, 3))
# 竖: from ~(140, 100) straight down to (140, 265)
shu = [(140, y) for y in range(100, 268, 2)]
stroke(shu, (7, 7))

# ---------- 隹 right sub-body ----------
# top small 撇 (short pie above right shoulder)
p_top = bez((175, 60), (172, 78), (168, 88), (162, 100), n=30)
stroke(p_top, (9, 3))
# top 横 (short horizontal above right body, y~95)
h_top = [(x, 95 + (x - 160) * 0.02) for x in range(160, 218, 2)]
stroke(h_top, (5, 6))
# central vertical of right body (from ~y=100 down to y=260)
v_right = [(195, y) for y in range(100, 262, 2)]
stroke(v_right, (7, 7))
# four horizontals crossing the vertical:
# 1) upper (y ~ 135)  short
h1 = [(x, 132) for x in range(158, 235, 2)]
stroke(h1, (5, 6))
# 2) mid-upper (y ~ 165)
h2 = [(x, 165) for x in range(158, 238, 2)]
stroke(h2, (5, 6))
# 3) mid-lower (y ~ 200)
h3 = [(x, 200) for x in range(158, 240, 2)]
stroke(h3, (5, 6))
# 4) BOTTOM long 横 — extends much further right past the vertical,
#    also anchoring the 亻 竖 base (components touch)
h_bot = [(x, 248 + (x - 130) * 0.005) for x in range(130, 275, 2)]
stroke(h_bot, (6, 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0549_准/01_准.png")
print("saved")
