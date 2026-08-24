"""Render 找 (zhao) at 300x300, white bg, black ink.
Left: 扌 (hand radical). Right: 戈 (dagger-axe).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5


def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")


# --- 扌 (left radical, narrow, occupies ~ x in [25,120]) ----------
# horizontal (heng)
line([(30, 118), (120, 110)])
# vertical hook (shu gou) — long vertical, small hook at bottom
line([(78, 70), (75, 235)])
line([(75, 235), (95, 248)])
# 提 (rising stroke) lower-left up to mid-right
line([(35, 195), (115, 172)])

# --- 戈 (right side, x in [130, 285]) ----------------------------
# heng (horizontal) — spans right side
line([(140, 130), (270, 122)])

# 斜钩 (xie gou) — the long curving diagonal.
# Starts near top of heng on the left side, curves down to bottom-right,
# then hook up-right at tail.
xie = [
    (170, 110),  # start upper-left near heng
    (185, 145),
    (200, 180),
    (215, 215),
    (235, 255),
    (260, 275),
]
line(xie)
# hook (up-right tick)
line([(260, 275), (278, 258)])

# 撇 (pie) — short slanting stroke from upper area down-left,
# crossing the heng on the left portion of 戈
line([(180, 110), (145, 190)])

# 点 (dot) — top-right dot, above the xie gou start
line([(245, 95), (262, 115)])

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p3_char_0353_找/01_找.png"
)
