"""
Render 将 (jiāng) at 300x300, black ink on white.

Structural read from GT:
  Left: 丬 (simplified 爿) — 点 top-left, rising 提 middle-left, long 竖 down.
  Right-top: 夕 — 撇, 横折 with a small hook, 点 inside.
  Right-bottom: 寸 — long 横 (spans wide), 竖钩 (UP-LEFT flick), 点.

Uses calligraphic 4-move: teardrop taper (stroke helper), shoulder dabs
at 折 joints, bezier for curves, UP-LEFT hook flicks. Based on佘 template.
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
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# ============ LEFT: 丬 ============
# 点 top-left — short down-right dot
dot1 = bez((50, 60), (55, 70), (60, 82), (65, 95), n=30)
stroke(dot1, (4, 8))

# 提 (rising stroke, middle-left) — from lower-left up-and-right
ti = bez((35, 175), (55, 165), (75, 155), (95, 145), n=40)
stroke(ti, (9, 3))

# 竖 — long vertical from near top down past middle
shu_left = bez((75, 75), (75, 145), (75, 215), (75, 280), n=60)
stroke(shu_left, (7, 7))

# ============ RIGHT-TOP: 夕 ============
# 撇 — starts upper, sweeps down-left with curve
pie_xi = bez((175, 55), (168, 90), (155, 125), (135, 165), n=60)
stroke(pie_xi, (10, 4))

# 横折钩 (or 横折) — starts near top of 撇, goes right then curves down-left
h_top = bez((175, 65), (200, 62), (225, 62), (245, 68), n=40)
stroke(h_top, (5, 6))
# shoulder dab at 折
dab(245, 68, 4.5)
# folded segment going down-left with hook curve
fold = bez((245, 68), (240, 100), (220, 130), (195, 155), n=50)
stroke(fold, (6, 4))

# 点 inside 夕
inner_dot = bez((180, 115), (188, 122), (195, 130), (200, 138), n=25)
stroke(inner_dot, (3, 7))

# ============ RIGHT-BOTTOM: 寸 ============
# 横 — long horizontal spanning across bottom-right area
heng = bez((115, 200), (165, 198), (220, 198), (275, 202), n=60)
stroke(heng, (6, 6))

# 竖钩 — center-right vertical with UP-LEFT hook
sg = bez((200, 175), (200, 220), (200, 255), (200, 275), n=50)
stroke(sg, (7, 7))
# hook flick UP-and-LEFT
hook = bez((200, 275), (194, 270), (188, 263), (182, 255), n=25)
stroke(hook, (7, 3))

# 点 (right side of 寸)
dian = bez((220, 225), (228, 232), (236, 240), (244, 250), n=30)
stroke(dian, (3, 8))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0439_将/01_将.png")
