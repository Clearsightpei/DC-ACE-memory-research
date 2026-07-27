"""
仇 = 亻 (left, compressed) + 九 (right).

# SIGNATURE CHECK (九 sibling row):
# 九 | 撇 + 横折弯钩 (2 strokes, 撇 CROSSES ABOVE the top 横) | vs 尢, 勺, 丸

Revision notes vs pass 1:
 - Pass 1 九 looked like 门 because the 横折弯钩's 弯 was too vertical.
   The 弯 must sweep down-and-RIGHTward in a bowl, then hook up-LEFT.
 - 亻 撇 was too short; extend and make less steep.
 - The 撇 of 九 must clearly START ABOVE the 横 (not on it).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def brush_line(draw, pts, width=8):
    if len(pts) < 2:
        return
    draw.line(pts, fill=BLACK, width=width, joint="curve")
    r = width // 2
    for x, y in [pts[0], pts[-1]]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def bezier(p0, p1, p2, n=50):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


def bezier3(p0, p1, p2, p3, n=60):
    out = []
    for i in range(n + 1):
        t = i / n
        x = ((1-t)**3)*p0[0] + 3*((1-t)**2)*t*p1[0] + 3*(1-t)*(t*t)*p2[0] + (t**3)*p3[0]
        y = ((1-t)**3)*p0[1] + 3*((1-t)**2)*t*p1[1] + 3*(1-t)*(t*t)*p2[1] + (t**3)*p3[1]
        out.append((x, y))
    return out


# ============ 亻 (left, ~x 45-115) ============

# 1) 撇: longer, less steep. Top ~(115, 70), curves down-left to (50, 220).
pie_ren = bezier((115, 70), (90, 130), (50, 225), n=60)
brush_line(d, pie_ren, width=7)

# 2) 竖: from apex/near-top of 撇 (~112, 95) straight down to y≈275.
brush_line(d, [(112, 95), (112, 275)], width=7)


# ============ 九 (right, ~x 140-275) ============

# 3) 撇 of 九: STARTS HIGH-LEFT ABOVE the 横 (which lives around y≈115).
#    Top at (185, 70) so it visibly crosses above the 横 line, then sweeps
#    down-left, curving out to (140, 245).
pie_jiu = bezier3((188, 68), (170, 130), (155, 195), (138, 250), n=70)
brush_line(d, pie_jiu, width=7)

# 4) 横折弯钩 of 九 — one flowing stroke:
#    a) 横: from (162, 115) rightward and slightly up to (258, 108)
#    b) 折: sharp turn — small down-right kick to (263, 130)
#    c) 弯: big bowl — sweeps DOWN and slightly LEFT, bottoms out around
#          (215, 260), then RISES rightward-up (bowl shape).
#          Actually for 九's 横折弯钩: the tail sweeps DOWN then RIGHTWARD
#          along the bottom, curling UP with a hook at the end. Terminus
#          is at the RIGHT of the bowl, hook pointing up-left.
#    d) 钩: at terminus, short flick up-left.

# a) 横 (slight upward tilt is fine)
brush_line(d, [(163, 115), (260, 108)], width=7)

# b) 折 shoulder — tiny corner turn
brush_line(d, [(260, 108), (265, 132)], width=7)

# c+d) 弯钩: a wide bowl arc.
#    Start at (265, 132). Sweep DOWN-LEFTward, bottom around (215, 262),
#    then curve UP-RIGHTward to end near (275, 220), where the hook flicks
#    up-left.
# Use cubic bezier to shape the bowl.
wan = bezier3((265, 132), (270, 240), (240, 270), (215, 262), n=70)
brush_line(d, wan, width=7)

# Now the sweeping return: from (215, 262) rising up-rightward.
# Actually the standard 横折弯钩 for 九 ends with the hook pointing
# UP-LEFT at the LOWER-RIGHT of the character. So the tail's terminus
# is roughly at (255-270, 245) with the flick going up-left.
# Simpler: draw a big single continuous curve from the fold down and
# rightward to a lower-right terminus, then hook up-left.

# Replace: use one bezier from 折 endpoint sweeping right and down and
# back up in an S bowl.

