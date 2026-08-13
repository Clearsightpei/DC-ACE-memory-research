# generated.py — p3_char_0271_老 (lǎo, "old") — 6 strokes
# Structure: 耂 (top) + 匕 (bottom-right)
# Bank has lao_radical (耂) but GT is thin uniform lines — inline fresh PIL
# per P12 (MMH GT rendering thin), styled like bi_char.py.
#
# Strokes:
#   1) short top 横 (heng)
#   2) short 竖 (shu) crossing it
#   3) long slanted 横 (crossing horizontal)
#   4) long sweeping 撇 (pie) down-left from upper right
#   5) small 撇 (start of 匕 in bottom-right)
#   6) 竖弯钩 (shu wan gou) — vertical then curve right + hook up

from PIL import Image, ImageDraw

CANVAS = 300
W = 5

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)


def line(p0, p1, w=W):
    d.line([p0, p1], fill=(0, 0, 0), width=w)
    r = w / 2
    for (x, y) in (p0, p1):
        d.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def polyline(pts, w=W):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)


# ---- 耂 (top component) ----
# 1) Short top 横
line((125, 60), (180, 62))

# 2) Short 竖 crossing the top heng (slightly angled down-left)
line((155, 45), (145, 115))

# 3) Long slanted 横 (main crossing horizontal), tilts slightly down-right
line((45, 130), (255, 120))

# 4) Long sweeping 撇 — from upper right area, curves down-left to lower-left
polyline([(210, 90), (185, 140), (140, 200), (85, 260), (55, 280)])

# ---- 匕 (bottom-right component) ----
# 5) Small 撇 — short diagonal down-left, visible on left of shu
line((205, 170), (150, 220))

# 6) 竖弯钩 — vertical shaft (shifted right), curve right along bottom, hook up
line((195, 200), (195, 255))
polyline([(195, 255), (205, 270), (225, 278), (250, 273), (260, 258)])
# small hook up at end
line((260, 258), (260, 238))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0271_老/01_老.png")
