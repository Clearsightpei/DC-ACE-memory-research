"""
Render 佇 (p3_char_0326_佇) at 300x300 with PIL.

Composition: 亻 (left ~30%) + 宁 (right ~65%).
  宁 = 宀 (roof, top) + 丁 (horizontal + 竖钩, bottom).

Strokes (7 total):
  亻:  1. 撇  2. 竖
  宀:  3. 点 (top-of-roof dot)  4. 横钩 (roof: 横 + hook down-left)
  丁:  5. 短点 or 横 across roof — wait no; 宁 has 宀 with dot on top,
        roof-横钩, then 丁 = 横 + 竖钩.
       Actually MMH 宁 = 6 strokes (宀=3: 点+点+横钩; 丁=2: 横+竖钩)
       BUT looking at GT: 宀 shows one top-dot + roof-shape (横钩).
       We render: 亻(2) + 宀(3: dot, dot?, 横钩) + 丁(2) = 7 total.
       Simplify: single top dot + 横钩 roof + 横 + 竖钩.

Hook flick rule (TIER-0 B): 竖钩 flicks UP-and-LEFT (~-105°).
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=7):
    d.line(points, fill=BLACK, width=width, joint="curve")
    for (x, y) in (points[0], points[-1]):
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def dab(cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLACK)


# ---------- 亻 (left radical, ~x=40..115) ----------
# 1. 撇
pie = [(105, 60), (95, 95), (80, 130), (62, 165), (45, 195)]
stroke(pie, width=7)
dab(105, 60, 4)

# 2. 竖 (from mid-撇 down)
shu = [(97, 110), (97, 165), (97, 220), (97, 255)]
stroke(shu, width=7)
dab(97, 110, 4)


# ---------- 宁 (right, ~x=125..280) ----------
# 3. 点 on top of 宀 (small dot centered around x=195)
dab(195, 55, 6)
# Slight slant tail on the dot
stroke([(193, 52), (200, 62)], width=5)

# 4. 横钩 (roof): 横 from left to right, then hook down-left inward
roof = [(135, 88), (200, 82), (265, 85)]
stroke(roof, width=7)
dab(135, 88, 4)
# hook: down and slightly left from right end
hook = [(265, 85), (263, 100), (255, 112)]
stroke(hook, width=7)

# 5. 横 (crossbar of 丁, sits under the roof)
hbar = [(145, 155), (215, 152), (275, 155)]
stroke(hbar, width=7)
dab(145, 155, 4)
dab(275, 155, 5)  # right-end 顿

# 6. 竖钩 (vertical hook of 丁 — center-right, hook flicks UP-LEFT)
vhook = [
    (208, 158),
    (208, 195),
    (208, 230),
    (208, 258),
    (198, 268),   # start hook curl
    (183, 262),   # flick UP-LEFT
    (172, 250),
]
stroke(vhook, width=8)
dab(208, 158, 5)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0326_佇/01_佇.png"
)
