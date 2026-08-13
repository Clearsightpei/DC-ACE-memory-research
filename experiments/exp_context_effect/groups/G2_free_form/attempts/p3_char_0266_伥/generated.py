"""
伥 = 亻 (left) + 长 (right)
长 stroke order (4 strokes):
  1. 撇 short at top going down-left
  2. 横 short horizontal near upper middle
  3. 竖提 vertical then flick UP-and-RIGHT (short 提)
  4. 捺 long diagonal from upper-mid to lower-right
No sibling row for 伥; treat as compound with 亻 on left.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bezier(p0, p1, p2, n=60):
    return [
        (
            (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1],
        )
        for t in (i / n for i in range(n + 1))
    ]


def brush(pts, w0, w1):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        r = (w0 * (1 - t) + w1 * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")


def line(p0, p1, w0, w1, n=40):
    pts = [
        (p0[0] + (p1[0] - p0[0]) * i / n, p0[1] + (p1[1] - p0[1]) * i / n)
        for i in range(n + 1)
    ]
    brush(pts, w0, w1)


# ==========================================================
# LEFT: 亻 (person radical) — x ~ [40, 110]
# ==========================================================
# 撇 — from upper right curving down-left
pie_left = bezier((95, 60), (78, 135), (48, 210), n=80)
brush(pie_left, 9, 5)
# 竖 — vertical from mid of 撇 downward
line((85, 135), (85, 245), 9, 8, n=60)

# ==========================================================
# RIGHT: 长 — x ~ [125, 275], y ~ [55, 260]
# ==========================================================
# 1. 撇 short at top — from upper-right going down-left
pie_top = bezier((180, 60), (168, 82), (150, 105), n=50)
brush(pie_top, 8, 4)

# 2. 横 — horizontal near top, crosses through where 撇 ended
line((140, 105), (230, 100), 6, 7, n=50)

# 3. 竖提 — vertical from top-right of 横 straight down, then short flick up-right
# vertical part
line((188, 75), (188, 215), 8, 8, n=60)
# 提 flick UP-and-RIGHT from bottom of vertical
line((188, 215), (232, 195), 8, 3, n=30)

# 4. 捺 — long sweeping diagonal from upper mid to lower-right, thickening
na_pts = bezier((175, 110), (215, 175), (275, 250), n=90)
brush(na_pts, 5, 12)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0266_伥/01_伥.png"
)
print("saved")
