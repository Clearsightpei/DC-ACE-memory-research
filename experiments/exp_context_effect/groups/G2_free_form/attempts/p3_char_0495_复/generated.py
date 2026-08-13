"""
Render 复 (fu4) at 300x300, black ink on white.

Structural read from GT:
  Top:    丿 (short pie, upper-left) + 一 (long horizontal).
  Middle: small 曰/日 box (top-H, left-V, right-V, mid-H, bottom-H) tucked
          under the top horizontal, centered slightly left of middle.
  Bottom: 夂 — a short 撇 dropping from upper right of the box,
          then a long 横撇 sweep (horizontal then curving down-left)
          crossed by a big 捺 sweeping down-right with a flat foot.

TIER-0 checks:
  - No sibling-checklist match for 复 itself.
  - Contains no frozen-cohort radicals (讠, 戈, 攵, 匕, 纟, 弓, 疒).
  - Applies 4-move: bezier curves, variable widths, shoulder dabs, no hooks needed.
  - Components must TOUCH: the 曰 box's bottom must sit right at the top
    of the 夂 sweep; the top 一 must touch the top of the 曰 box.
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


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- 1. 丿 short pie at top ---
pie_top = bez((150, 25), (140, 40), (125, 55), (108, 70), n=50)
stroke(pie_top, (7, 3))

# --- 2. 一 long horizontal ---
h_top = bez((80, 68), (130, 66), (185, 66), (230, 70), n=50)
stroke(h_top, (6, 6))

# --- 3. 曰 box (small rectangle w/ middle horizontal) ---
# top-H of box
box_top = bez((100, 90), (135, 89), (170, 89), (200, 92), n=40)
stroke(box_top, (5, 5))
dab(100, 90, 4)
dab(200, 92, 4)
# left-V
box_left = bez((102, 90), (102, 115), (102, 140), (102, 158), n=40)
stroke(box_left, (5, 5))
# right-V (with a small 折 shoulder at top)
box_right = bez((200, 92), (200, 115), (200, 140), (198, 158), n=40)
stroke(box_right, (5, 5))
# middle-H
box_mid = bez((108, 122), (140, 121), (170, 121), (196, 123), n=40)
stroke(box_mid, (4, 4))
# bottom-H
box_bot = bez((105, 158), (140, 157), (170, 157), (198, 158), n=40)
stroke(box_bot, (5, 5))

# --- 4. 夂 bottom ---
# short 撇 dropping from upper-right down-left (starts near box top-right area)
pie_low = bez((175, 160), (168, 175), (155, 190), (140, 205), n=60)
stroke(pie_low, (8, 3))

# 横撇 (horizontal then curving down-left) — starts left, goes right w/ slight rise,
# then sweeps down and left to the lower-left
# horizontal top segment
hp_h = bez((85, 195), (130, 192), (175, 190), (215, 193), n=60)
stroke(hp_h, (6, 5))
# shoulder dab at the fold
dab(215, 193, 5)
# curving pie down-left
hp_curve = bez((215, 193), (200, 220), (160, 250), (95, 275), n=80)
stroke(hp_curve, (7, 3))

# 捺 — big sweep from mid down-right, ending with a flat foot
na_main = bez((150, 210), (175, 235), (210, 260), (245, 275), n=80)
stroke(na_main, (5, 12))
# foot flare
foot = bez((245, 275), (252, 276), (258, 277), (265, 278), n=20)
stroke(foot, (12, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0495_复/01_复.png")
