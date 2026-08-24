"""
仝 — 5 strokes: 人 (撇 + 捺) as a wide roof / lid, then 工 below (top 一, 竖, bottom 一).
Layout: 人 lid covers full width of the 工 below; apex around top-center.
Signature: 人 = apex SHARED at same y; both strokes throw outward.
工 = matched-length top and bottom 横 with a through-竖.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=9):
    """Draw a smooth polyline stroke."""
    d.line(points, fill=BLACK, width=width, joint="curve")
    # dab endpoints for a rounder look
    r = width // 2
    for x, y in (points[0], points[-1]):
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ---------- 人 lid (top half) ----------
# Apex near top-center, shared. Lid narrower than bottom 一.
apex = (150, 50)

# 撇 — from apex, curve down-left, slight bow, ending around x=80
piegu = [
    apex,
    (132, 75),
    (110, 105),
    (90, 135),
    (78, 158),
]
stroke(piegu, width=8)

# 捺 — from apex, sweep down-right, thicker foot
na = [
    apex,
    (168, 78),
    (188, 108),
    (208, 135),
    (222, 158),
]
stroke(na, width=8)
# Thickened foot for 捺
foot = [(200, 138), (218, 155), (228, 162)]
d.line(foot, fill=BLACK, width=12)
d.ellipse([224, 158, 234, 168], fill=BLACK)

# ---------- 工 (bottom half) ----------
# Top 一 — narrower than the 人 lid span, sits under the lid apex vertically
stroke([(108, 178), (192, 178)], width=9)

# Middle 竖 (through)
stroke([(150, 180), (150, 242)], width=9)

# Bottom 一 — WIDEST element (wider than 人 lid)
stroke([(60, 248), (250, 250)], width=10)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0181_仝/01_仝.png")
