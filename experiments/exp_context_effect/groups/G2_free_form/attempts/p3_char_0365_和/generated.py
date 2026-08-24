"""Render 和 (p3_char_0365) at 300x300.

Structure: left/right compound
  Left  = 禾 (~55% width, full height): 撇 top, 横 upper, 竖 spine, 撇 middle-left, 捺 middle-right
  Right = 口 (~35% width, lower-middle band): 竖 | 横折 | 横 bottom

Consulted memory_index TIER-0: 和 is not in sibling-risk list. No hooks.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def stroke(pts, width=6):
    # simple polyline with round caps
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=width)
    for p in pts:
        d.ellipse((p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2), fill=INK)


def bezier(p0, p1, p2, n=24):
    out = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


# ============ LEFT: 禾  (occupies x=30..175, y=40..280) ============
# 1) top 撇 (short flick, going down-left from upper spine)
stroke(bezier((115, 45), (100, 55), (78, 78)), width=6)

# 2) upper 横 (crossbar under the top flick)
stroke([(45, 92), (170, 88)], width=6)

# 3) vertical spine 竖 (long, from top of crossbar to bottom)
stroke([(108, 65), (108, 275)], width=7)

# 4) middle 撇 (from just under crossbar going down-left, curved)
stroke(bezier((108, 108), (75, 170), (32, 265)), width=6)

# 5) middle 捺 (from just under crossbar going down-right, curved, widening tail)
stroke(bezier((108, 108), (145, 180), (188, 260)), width=6)
# short thickening dab at end of 捺
stroke([(182, 254), (197, 265)], width=5)

# ============ RIGHT: 口  (occupies x=200..275, y=140..245) ============
LX, RX = 200, 273
TY, BY = 145, 240

# left 竖
stroke([(LX, TY + 4), (LX, BY)], width=6)
# 横折 (top horizontal + right vertical, single stroke)
stroke([(LX - 2, TY), (RX, TY), (RX, BY)], width=6)
# bottom 横 (slightly extends past both sides)
stroke([(LX - 2, BY), (RX + 2, BY)], width=6)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0365_和/01_和.png")
print("saved 01_和.png")
