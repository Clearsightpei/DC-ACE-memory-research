"""
仇 = 亻 (left, compressed) + 九 (right).  RETRY #1

Prior fail: 九 collapsed into a rectangle (looked like 门) because the
横折弯钩 lacked its characteristic bowl+hook and the 撇 didn't
cross above the 横.

Fix plan (from errata + TIER-0 hook rules):
  - 亻: standard 撇 + 竖.
  - 九 撇: STARTS HIGH (above the 横 line by 20+ px), sweeps down-left.
  - 九 横折弯钩 = ONE continuous stroke:
        short 横 (nearly flat) → sharp fold down → wide bowl arc
        sweeping DOWN-then-RIGHT along the bottom → terminal hook
        flicking UP-and-LEFT (~-110°) at the lower-right.
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


def bezier3(p0, p1, p2, p3, n=70):
    out = []
    for i in range(n + 1):
        t = i / n
        x = ((1-t)**3)*p0[0] + 3*((1-t)**2)*t*p1[0] + 3*(1-t)*(t*t)*p2[0] + (t**3)*p3[0]
        y = ((1-t)**3)*p0[1] + 3*((1-t)**2)*t*p1[1] + 3*(1-t)*(t*t)*p2[1] + (t**3)*p3[1]
        out.append((x, y))
    return out


W_STROKE = 7

# ============ 亻 (left column, x ~ 45-115) ============

# 1) 撇: from (110, 65) curving down-left to (48, 225).
pie_ren = bezier3((110, 65), (95, 120), (75, 175), (48, 225), n=60)
brush_line(d, pie_ren, width=W_STROKE)

# 2) 竖: from ~(108, 100) straight down to (108, 275).
brush_line(d, [(108, 100), (108, 275)], width=W_STROKE)


# ============ 九 (right, x ~ 145-278) ============

# 3) 撇 of 九: STARTS HIGH-LEFT well ABOVE where the 横 will sit (y~120).
#    Top at (190, 60), sweeps down-left, curving out to (145, 250).
pie_jiu = bezier3((190, 60), (178, 120), (168, 190), (148, 252), n=70)
brush_line(d, pie_jiu, width=W_STROKE)

# 4) 横折弯钩 — one continuous stroke drawn in segments:
#
#    a) 横: nearly flat, from (170, 120) rightward to (262, 115).
brush_line(d, [(170, 120), (262, 115)], width=W_STROKE)

#    b) 折: sharp downward shoulder, from (262, 115) sweeping down to (270, 200).
#       The 弯 (bend) makes the right side bow slightly outward as it descends.
wan_down = bezier3((262, 115), (275, 150), (278, 180), (270, 210), n=60)
brush_line(d, wan_down, width=W_STROKE)

#    c) 弯 continues — curls LEFT-and-DOWN along the bottom of the bowl,
#       then rises to the terminus at (245, 258).
wan_bot = bezier3((270, 210), (260, 260), (230, 268), (218, 255), n=60)
brush_line(d, wan_bot, width=W_STROKE)

#    d) 钩: terminal flick UP-and-LEFT from (218, 255) → (208, 238).
brush_line(d, [(218, 255), (208, 238)], width=W_STROKE)


img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0111_仇__retry_1/01_仇.png")
print("saved")
