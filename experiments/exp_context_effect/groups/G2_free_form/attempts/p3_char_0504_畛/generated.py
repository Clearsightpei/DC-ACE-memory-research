"""p3_char_0504_畛 — G2 attempt.

畛 = 田 (left) + 㐱 (right).
㐱 = 人 (top: 撇 + 捺) + 彡 (three parallel 撇 strokes below).

Applying calligraphic-weight moves:
- Taper on 撇 (thick-to-thin) and 捺 (thin-to-thick with foot)
- Shoulder dab at 横折 joint of 田
- Components must touch: 田 right-edge and 㐱's 撇 sweep overlap region
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=6):
    """Uniform-width smooth stroke through pts."""
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill=BLACK)


def tapered(pts, widths):
    """Tapered stroke: per-point width array."""
    n = len(pts)
    for i in range(n - 1):
        w = (widths[i] + widths[i + 1]) / 2
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=max(1, int(round(w))))
    for i, p in enumerate(pts):
        r = widths[i] / 2
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=BLACK)


def shoulder_dab(cx, cy, r=5):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLACK)


# ------------------ 田 (left, x 35..130, y 95..215) ------------------
L, R, T, B = 40, 128, 100, 215
# stroke 1: left 竖
stroke([(L, T), (L, B)], width=6)
# stroke 2: 横折 (top then right down)
stroke([(L, T), (R, T + 2)], width=6)
shoulder_dab(R, T + 2, r=4)
stroke([(R, T + 2), (R + 1, B)], width=6)
# stroke 3: inner 竖 middle
mx = (L + R) // 2
stroke([(mx, T + 3), (mx, B - 2)], width=5)
# stroke 4: inner 横 middle
my = (T + B) // 2
stroke([(L + 3, my), (R - 2, my)], width=5)
# stroke 5: bottom 横 (close the box)
stroke([(L, B), (R, B)], width=6)

# ------------------ 㐱 (right, x 135..290, y 55..285) ----------------
# Top 人 (compact, occupies upper third):
#   撇 from apex sweeps down-left
#   捺 from apex sweeps down-right
# Below 人: 彡 — three parallel 撇 strokes cascading downward,
#   each starting further left and lower than the previous.

# Apex of 人
ax, ay = 215, 65

# 撇: tapered thick to thin
pie_pts = [(ax, ay), (200, 88), (185, 112), (170, 138), (155, 160)]
pie_ws = [9, 8, 6.5, 5, 2.5]
tapered(pie_pts, pie_ws)

# 捺: thin to thick with foot flare
na_pts = [(ax + 2, ay + 6), (230, 90), (248, 115), (267, 140), (285, 160), (290, 162)]
na_ws = [3, 5, 7, 9, 10.5, 4]
tapered(na_pts, na_ws)

# 彡 — three parallel 撇 strokes below 人, cascading down-left
# Each starts further left and lower — creating the diagonal cascade look
def draw_pie(x_top, y_top, length=58, dx=-30, thick=8.0):
    pts = [
        (x_top, y_top),
        (x_top + dx * 0.30, y_top + length * 0.30),
        (x_top + dx * 0.60, y_top + length * 0.60),
        (x_top + dx, y_top + length),
    ]
    ws = [thick, thick * 0.75, thick * 0.5, thick * 0.25]
    tapered(pts, ws)


# 彡 cascading: top-right → bottom-left
draw_pie(268, 180, length=50, dx=-28, thick=8.0)   # top pie
draw_pie(245, 210, length=55, dx=-30, thick=8.0)   # middle pie
draw_pie(220, 240, length=58, dx=-32, thick=8.0)   # bottom pie

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0504_畛/01_畛.png"
img.save(out)
print("saved", out)
