"""
伕 = 亻 (left, person radical) + 夫 (right)
夫 = 一 (top short 横) + 一 (longer middle 横) + 撇 (through center) + 捺 (crossing 撇)

# SIGNATURE CHECK (from sibling_signature_checklist for 大/夫):
# 夫 vs 大: 夫 has TWO horizontals above the 大 body; 大 has one.
# Both 撇 and 捺 must cross the horizontals and reach further down than
# their intersection with the top 横.

Layout:
- 亻 in left ~1/3 of canvas
- 夫 in right ~2/3 of canvas, taking full height
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")
    for (x, y) in pts:
        d.ellipse([x - width/2, y - width/2, x + width/2, y + width/2], fill="black")

# ---- 亻 (left radical) ----
# 撇: from ~top of radical, curving down-left
stroke([(95, 60), (85, 90), (72, 130), (58, 175)], width=6)
# 竖: long vertical from junction down
stroke([(85, 95), (86, 260)], width=7)

# ---- 夫 (right side) ----
# top 横 (shorter, upper)
stroke([(155, 95), (245, 92)], width=6)
# middle 横 (longer, wider)
stroke([(135, 150), (270, 147)], width=7)
# 撇: starts at top 横, cuts through both 横s, sweeps down-left
stroke([(210, 92), (200, 130), (180, 175), (150, 220), (125, 265)], width=6)
# 捺: starts from around intersection with 撇 near top, curves down-right
stroke([(195, 100), (215, 150), (240, 200), (275, 265)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0258_伕/01_伕.png")
