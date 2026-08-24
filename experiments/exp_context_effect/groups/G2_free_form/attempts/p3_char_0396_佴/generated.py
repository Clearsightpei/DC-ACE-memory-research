"""
佴 = 亻 (left) + 耳 (right)
Left: 亻 — 撇 (top diag), 竖 (vertical starting at 撇 midpoint)
Right: 耳 — top 横, then two 竖 (left short, right long) forming box,
        two internal 横 ticks, bottom 横 that extends beyond both
        sides (esp. right).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w=7):
    # Draw a polyline with rounded joints/ends using overlapping circles + lines
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)
    for x, y in pts:
        r = w // 2
        d.ellipse((x-r, y-r, x+r, y+r), fill="black")

# ---------- Left: 亻 ----------
# 撇: starts high, sweeps down-left
stroke([(95, 70), (88, 110), (60, 175)], w=7)
# 竖: from midpoint of 撇 going straight down
stroke([(95, 130), (95, 240)], w=7)

# ---------- Right: 耳 ----------
# Top 横 — top of the box, slight rise to the right
stroke([(140, 90), (240, 88)], w=7)
# Left 竖 — from top-横 left end down to bottom
stroke([(155, 90), (155, 230)], w=7)
# Right 竖 — from top-横 right end going down past bottom (long tail)
stroke([(225, 90), (225, 270)], w=7)
# Middle 横 1
stroke([(160, 135), (222, 135)], w=6)
# Middle 横 2
stroke([(160, 178), (222, 178)], w=6)
# Bottom 横 — long, extends past both sides
stroke([(120, 230), (260, 232)], w=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0396_佴/01_佴.png")
