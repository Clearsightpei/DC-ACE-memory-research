"""
鸭 = 甲 (left) + 鸟 (right). LR compound, components must TOUCH.
Apply TIER-0.F 4-move: taper, shoulder dabs, bezier curves, hook up-left.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def dab(x, y, r):
    d.ellipse([x-r, y-r, x+r, y+r], fill="black")

def stroke(pts, widths):
    n = len(pts)
    if isinstance(widths, (int, float)):
        widths = [widths] * n
    for i in range(n - 1):
        x0, y0 = pts[i]; x1, y1 = pts[i+1]
        w0, w1 = widths[i], widths[i+1]
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(int(dist), 2)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + t * (x1 - x0); y = y0 + t * (y1 - y0)
            r = (w0 + t * (w1 - w0)) / 2
            dab(x, y, r)

def bez(p0, p1, p2, p3, n=40):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
        y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
        out.append((x, y))
    return out

# ============ 甲 (left) x~30..130, y~55..255 =============
# left vertical
stroke([(45, 70), (45, 175)], [7, 7])
# top horizontal + shoulder + right vertical (横折)
stroke([(45, 70), (130, 70)], [7, 7])
dab(130, 70, 4.5)
stroke([(130, 70), (130, 175)], [7, 7])
# middle horizontal
stroke([(45, 122), (130, 122)], [6.5, 6.5])
# bottom horizontal
stroke([(45, 175), (130, 175)], [7, 7])
# long central vertical extending down (the tail of 甲)
stroke([(87, 60), (87, 250)], [7.5, 6])

# ============ 鸟 (right) x~145..280, y~55..245, touches 甲 =============
# Stroke 1: 撇 — top downward flick, thick to thin, bezier
p1 = bez((200, 58), (196, 68), (185, 78), (168, 92), n=30)
w1 = [7 - 5*(i/(len(p1)-1)) for i in range(len(p1))]
stroke(p1, w1)

# Stroke 2: 横折钩 — head enclosure. Horizontal + right vertical curving inward + hook
stroke([(168, 92), (245, 92)], [7, 7])
dab(245, 92, 4.5)
arc = bez((245, 92), (248, 112), (243, 128), (232, 138), n=25)
stroke(arc, [7]*len(arc))
# hook UP-and-LEFT
stroke([(232, 138), (220, 128)], [6, 2.5])

# Stroke 3: 点 (eye dot) inside head
dab(215, 112, 5)
dab(212, 116, 3.5)

# Stroke 4: 竖折折钩 — the body sweep.
# Start from head-bottom-left area, go down, sweep right, curve back down with hook.
# Path: (168, 138) -> down to (168, 175) -> right to (250, 175) with corner shoulder ->
# down-curve sweeping to (255, 210) -> curve left to (220, 220) with hook up-left.
# Segment 1 down
stroke([(168, 138), (168, 175)], [7, 7])
dab(168, 175, 4.5)
# Segment 2 across (the belt under the head)
stroke([(168, 175), (250, 175)], [7, 7])
dab(250, 175, 4.5)
# Segment 3 down-curve (body right side sweeping down and back)
body = bez((250, 175), (258, 195), (255, 215), (235, 222), n=30)
stroke(body, [7]*len(body))
# Hook up-left
stroke([(235, 222), (222, 210)], [6, 2.5])

# Stroke 5: 横 (bottom foot horizontal) — spans under body, tucks under
stroke([(150, 235), (270, 235)], [7, 7])

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0563_鸭/01_鸭.png")
print("saved")
