"""伉 (kang) — 亻 (person radical) on left + 亢 on right.

Revised pass 2:
- 亻: 撇 clearly connects to 竖 at joint; 竖 hangs long below.
- 亢: 点 close to 横 (touching), 横 wide; below the 横 the
  bottom leg-pair emerges — 撇 on left, 横折弯钩 on right, both
  starting just under the 横 at the same y.
- Hook flick UP-and-LEFT per tier-0 rule.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=6):
    if len(pts) < 2:
        return
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for x, y in pts:
        d.ellipse([x - width / 2, y - width / 2, x + width / 2, y + width / 2], fill=BLACK)


def bezier(p0, p1, p2, n=30, width=6):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    stroke(pts, width=width)


# ==================== 亻 (left radical) ====================
# 撇: diagonal top-right to lower-left
bezier((100, 90), (90, 120), (72, 155), n=25, width=7)
# 竖: long vertical, starts at ~midpoint of 撇
stroke([(85, 130), (85, 255)], width=7)

# ==================== 亢 (right component) ====================
# 点 (short diagonal dot): top of 亢, slightly right of center
stroke([(198, 65), (210, 82)], width=8)

# 横 (long horizontal): touches the dot's bottom
stroke([(150, 100), (260, 98)], width=7)

# --- bottom leg-pair (几-shape under 亠) ---
# short 撇: from just under the 横, curving down-left, hangs long
bezier((175, 108), (155, 175), (135, 245), n=30, width=7)

# 横折弯钩: horizontal top starts at 撇's origin area, sweeps right
# horizontal:
stroke([(190, 128), (250, 126)], width=7)
# fold + descending curve down and rightward-curving:
bezier((250, 126), (255, 200), (260, 245), n=30, width=7)
# hook flick UP-and-LEFT at the terminal
stroke([(260, 245), (245, 228)], width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0250_伉/01_伉.png")
print("wrote 01_伉.png")
