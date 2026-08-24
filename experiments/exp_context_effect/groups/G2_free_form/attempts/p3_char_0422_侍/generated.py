"""
侍 (p3_char_0422) — G2 render.

# SIGNATURE CHECK:
# Contains 土 as component (top-right of 寺). Row: BOTTOM 横 LONGER than top (~1.5x).
# Beware of not making it look like 士 (士 = top 横 longer).

Structure: 亻 (left) + 寺 (right = 土 top + 寸 bottom)
- 亻: 撇 + 竖
- 土: top短横 + 竖 + bottom长横
- 寸: 横 + 竖钩 (flick UP-LEFT) + 点
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=7):
    """Draw a smooth polyline through pts."""
    d.line(pts, fill="black", width=width, joint="curve")
    # Round the ends
    for (x, y) in [pts[0], pts[-1]]:
        r = width // 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")


# ---- 亻 (person radical, left) ----
# 撇: from upper-right diagonal down-left, tapered curve
pie = [(108, 65), (95, 100), (78, 140), (60, 185), (48, 215)]
stroke(pie, width=7)

# 竖: from top of 亻 straight down (ends around belt line, not full height)
stroke([(108, 120), (108, 240)], width=8)

# ---- 土 (top of 寺, right side) ----
# top 横 (shorter)
stroke([(165, 80), (240, 80)], width=7)
# 竖 (center vertical of 土)
stroke([(200, 80), (200, 148)], width=8)
# bottom 横 (LONGER than top — signature of 土, not 士)
stroke([(140, 148), (275, 148)], width=8)

# ---- 寸 (bottom of 寺) ----
# 横 of 寸 (crosses through the 竖钩)
stroke([(145, 195), (280, 195)], width=8)
# 竖钩: vertical descending then hook UP-and-LEFT
gou = [(215, 165), (215, 258), (204, 253), (192, 243)]
stroke(gou, width=8)
# 点: small dot on the right side of 寸, below the 横
dian = [(248, 210), (262, 228), (266, 238)]
stroke(dian, width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0422_侍/01_侍.png")
