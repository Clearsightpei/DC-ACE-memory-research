"""社 = 礻 (shows-sign radical, left) + 土 (right).

# SIGNATURE CHECK (from sibling_signature_checklist.md, applied to 土 sub-glyph):
#   土 : BOTTOM 横 LONGER than top (~1.5x). Enforced in right sub-glyph.
# Hook rules: 礻 has no hook; 土 has no hook.

Layout (300x300 canvas, 米字格 mental grid):
- Left sub-glyph 礻 occupies roughly x in [30, 130].
- Right sub-glyph 土 occupies roughly x in [155, 275].
- Vertical extent both ~ y in [55, 250].
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=6):
    d.line([p0, p1], fill="black", width=w)

def stroke(pts, w=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=w)

# --- Left: 礻 ---
# 1) top 点 (small tick), slanting down-right at very top
stroke([(65, 60), (80, 78)], w=6)

# 2) 横撇 : short horizontal then curving sweep down-left
stroke([(48, 100), (110, 100), (100, 108), (55, 165), (35, 195)], w=6)

# 3) central 竖 (through the horizontal), going straight down
stroke([(90, 100), (90, 250)], w=7)

# 4) right 点 (small tick beside the vertical, lower area)
stroke([(105, 175), (125, 195)], w=6)

# --- Right: 土 ---
# 5) top 横 (shorter)
line((175, 110), (245, 110), w=7)

# 6) 竖 (vertical through the two horizontals)
line((210, 110), (210, 230), w=7)

# 7) bottom 横 (LONGER, ~1.5x top)
line((155, 230), (275, 230), w=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0341_社/01_社.png")
print("saved")
