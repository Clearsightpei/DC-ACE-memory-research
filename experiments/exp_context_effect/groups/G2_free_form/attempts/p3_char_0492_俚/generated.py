"""俚 (lǐ) — 亻 (left radical) + 里 (right body). 9 strokes total.

# SIGNATURE CHECK:
# - 亻 as LEFT radical: compressed, tall-narrow; the 竖 touches or begins
#   within the 撇 body (no detached column).
# - 里 body on right occupies ~cols 110..270; the LAST horizontal is the
#   WIDEST stroke; 日 (top) is narrower than 土-bottom.
# - Components TOUCH: 亻's 竖 (x~90) must nearly touch 里's left column
#   (x~120). No visible white gap between components.
# - Calligraphic weight: teardrop taper on 撇, uniform 竖, slight 顿 dabs
#   at horizontal starts/ends; no ruler-square corners.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
    """Variable-width stroke by dabbing ellipses along the path."""
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        dx = x1 - x0
        dy = y1 - y0
        seg = max(abs(dx), abs(dy))
        steps = max(int(seg) * 2, 8)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + dx * t
            y = y0 + dy * t
            r = w0 * (1 - t) + w1 * t
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke(pts, width=9):
    """Uniform-width polyline with end caps."""
    r = width / 2
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    for (x, y) in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ================== 亻 (left radical, compressed) ==================
# 撇: head ~upper-right of the radical, tail down-left, teardrop taper.
pie_points = [
    (95, 55),
    (88, 85),
    (78, 115),
    (65, 150),
    (48, 185),
    (30, 215),
]
pie_widths = [5.5, 5.2, 4.6, 4.0, 3.0, 1.6]
brush_stroke(pie_points, pie_widths)

# small head 顿 curl
brush_stroke([(95, 55), (100, 62), (96, 72)], [5.2, 4.0, 2.5])

# 竖: straight vertical drop, starts within pie body, no hook
shu_points = [(85, 115), (85, 165), (85, 215), (85, 260)]
shu_widths = [5.4, 5.4, 5.4, 5.0]
brush_stroke(shu_points, shu_widths)
d.ellipse((81, 112, 90, 121), fill="black")

# ================== 里 (right body) ==================
# Occupies cols ~118..270. Top 日 narrower; bottom 土 wider.
# ---- 日 (top box) ----
LX, RX = 130, 235       # left and right cols of 日
T = 55                  # top of 日
MID = 108               # middle bar
BOT = 160               # bottom of 日 / above 土-portion
CX = (LX + RX) // 2     # center vertical anchor

# 1. 竖 left of 日
stroke([(LX, T + 3), (LX, BOT)], width=8)

# 2. 横折 top + right vertical
stroke([(LX - 4, T), (RX, T + 4), (RX, BOT)], width=8)

# 3. 横 middle inside 日
stroke([(LX + 3, MID), (RX - 3, MID)], width=7)

# 4. 横 bottom of 日 (== top boundary of 土 area)
stroke([(LX - 2, BOT), (RX + 2, BOT)], width=8)

# 5. 竖 central long vertical, from top of 日 through 土
stroke([(CX, T + 14), (CX, 250)], width=9)

# 6. 横 middle horizontal of 土
stroke([(118, 208), (248, 208)], width=8)

# 7. 横 bottom horizontal — the WIDEST stroke
stroke([(105, 262), (270, 260)], width=10)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0492_俚/01_俚.png"
)
print("saved")
