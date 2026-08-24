"""
p3_char_0283_传 — G2 attempt (revision)

传 = 亻 + 专. Strokes:
  亻 (2): 撇, 竖
  专 (4): 横, 竖-with-tiny-stem-into-second-横, 竖折折/横折 with sweep, 点

Fixed vs pass 1: reduced horizontal count in 专 to match GT which has
only 2 clean horizontals plus the sweeping folded body.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    d.line(pts, fill="black", width=width, joint="curve")
    for x, y in [pts[0], pts[-1]]:
        r = width // 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

def bezier(p0, p1, p2, steps=30):
    return [(
        (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
        (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1],
    ) for t in (i / steps for i in range(steps + 1))]

# ============== 亻 (left) ==============
# 撇 — from ~(100, 55) sweeping down-left to (55, 155)
stroke(bezier((100, 55), (88, 100), (55, 155), steps=30), width=9)
# 竖 — long vertical anchored on 撇's upper body
stroke([(95, 100), (92, 265)], width=9)

# ============== 专 (right) ==============
# 1) Top 横: (130, 90) → (275, 82)
stroke([(130, 90), (275, 82)], width=8)

# 2) Second 横 slightly below: shorter, (150, 145) → (255, 140)
#    then it becomes a 竖折 diving down and forming the main sweep
stroke([(150, 145), (255, 140)], width=8)

# 3) Main body — 竖折/横折弯钩 like shape:
#    start at right side around (255, 140), go down and left, then sweep out right
#    but since second 横 already ends there, we draw the fold as a separate stroke:
#    a horizontal a bit lower that curves down into the sweep with hook back
body_top = [(140, 195), (260, 190)]
stroke(body_top, width=9)
# curve down and out
sweep = bezier((258, 190), (255, 250), (185, 268), steps=40)
stroke(sweep, width=10)
# hook flick UP-and-LEFT
hook = bezier((185, 268), (180, 258), (172, 250), steps=15)
stroke(hook, width=8)

# 4) 点 (dot) at top-right of 专
dot = bezier((262, 55), (270, 68), (275, 82), steps=15)
stroke(dot, width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0283_传/01_传.png")
print("saved")
