"""
伐 = 亻 (left) + 戈 (right). 6 strokes.
亻: 撇 (top diagonal), 竖 (vertical below).
戈: 短横 (upper mid), 斜钩 (main sweeping diagonal with UP-LEFT hook),
    撇 (through the crossbar), 点 (top-right dot).

Hook family rule (memory index Tier-0 B): 斜钩 (戈) terminal flicks
UP-and-LEFT (~-110° to -120°). Do NOT flick down.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def stroke(points, width=8):
    d.line(points, fill=BLACK, width=width, joint="curve")


def bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# ---- 亻 (left component, occupies ~x=50..110) ----
# 撇: from ~(95, 70) down-left curving to (55, 155)
pie_pts = bezier((95, 70), (85, 105), (55, 155))
stroke(pie_pts, width=8)

# 竖: vertical from where the 撇 meets, going straight down
# starts near (80, 130) down to (80, 255)
stroke([(80, 130), (80, 255)], width=8)


# ---- 戈 (right component, occupies ~x=125..270) ----
# 1) 短横: short horizontal upper. Slight upward slant.
stroke([(155, 100), (235, 90)], width=7)

# 2) 斜钩 (main sweeping diagonal): starts near upper-left of 戈,
#    curves down and rightward, ends with UP-LEFT flick hook.
xie_body = bezier((170, 75), (205, 175), (270, 250))
stroke(xie_body, width=9)
# hook flick: from end (270,250) up-and-left (~-115°) — must be visible
hx, hy = 270, 250
ang = math.radians(-115)
hlen = 30
tx = hx + hlen * math.cos(ang)
ty = hy + hlen * math.sin(ang)
stroke([(hx, hy), (tx, ty)], width=9)

# 3) 撇: crosses through the 横 crossbar. Start ABOVE the crossbar,
#    pass through it, end down-left.
pie2 = bezier((205, 80), (185, 150), (145, 225))
stroke(pie2, width=7)

# 4) 点: top-right dot
dot = bezier((250, 70), (260, 82), (255, 100))
stroke(dot, width=8)


out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0256_伐/01_伐.png"
img.save(out)
print("saved", out)
