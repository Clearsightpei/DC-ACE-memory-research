"""Render 花 (huā, flower) at 300x300.

Composition: 艹 (top, grass radical, 3 strokes) + 化 (bottom):
  化 = 亻 (left, person radical, 2 strokes) + 匕 (right, 2 strokes: 撇 + 竖弯钩)

# SIGNATURE CHECK (sibling protocol — 匕 as component):
#   匕 has a hook that flicks UP-and-LEFT at the end of the 竖弯钩.
#   Never flick DOWN. Never omit hook. Hook returns toward interior.
#   撇 crosses the vertical portion in upper-middle.

Total 7 strokes: 3 (艹) + 2 (亻) + 2 (匕).

Revision-1 fixes:
- 亻's 竖 shifted right + attached to the 撇 curve.
- 亻's 撇 gets more horizontal sweep (less steep).
- 匕's 撇 crosses cleanly through the vertical.
- 匕's hook made longer and clearly UP-LEFT.
- 艹 verticals shortened at top so bar sits near top of verticals.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=6):
    if len(pts) < 2:
        return
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    for (x, y) in pts:
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


# ---- 艹 grass radical on top (y ≈ 55 - 110) ----
# horizontal crossbar (slight rise to the right, classic)
stroke([(45, 82), (255, 74)], width=6)

# left short vertical (slight lean-left top, dropping through bar)
stroke(bezier((108, 58), (105, 82), (98, 112)), width=6)

# right short vertical (slight lean-right at top)
stroke(bezier((198, 58), (203, 82), (212, 112)), width=6)


# ---- 亻 person radical (bottom-left, x ~ 55-135) ----
# 撇 (sweeping curve top-right → bottom-left)
stroke(bezier((128, 128), (105, 195), (60, 285)), width=7)

# 竖 (vertical) — starts at the 撇 curve around y=170, goes to baseline
# At t≈0.45 on above bezier: x ≈ (0.30)(128)+(0.495)(105)+(0.2025)(60) ≈ 38.4+52.0+12.15 ≈ 102.6
stroke([(103, 172), (103, 285)], width=7)


# ---- 匕 (bottom-right, x ~ 145-250) ----
# 撇 (short slanted stroke going from upper-right down-left, crossing the vertical stem)
stroke(bezier((235, 158), (200, 172), (158, 200)), width=6)

# 竖弯钩: vertical → curve right → hook UP-and-LEFT
# Segment 1: vertical descent
v1 = bezier((190, 130), (188, 195), (192, 240))
stroke(v1, width=7)
# Segment 2: curve to lower-right
c1 = bezier((192, 240), (208, 262), (250, 260))
stroke(c1, width=7)
# Segment 3: hook flick UP-and-LEFT (clearly upward and leftward)
stroke([(250, 260), (235, 225)], width=7)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0357_花/01_花.png")
print("wrote 01_花.png")
