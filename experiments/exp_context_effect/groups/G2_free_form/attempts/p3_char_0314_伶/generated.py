"""
Render 伶 (亻 + 令) to a 300x300 PNG.

Composition:
  Left ~30% (亻): compressed version of past PASS render (p3_char_0022).
    - 撇: head (75,70) -> tail (35,205), thick->thin
    - 竖: (75, 130) -> (75, 260), no hook
  Right ~65% (令):
    - 人 roof: apex (185,60); 撇 to (135,150); 捺 to (250,155)
    - 、 middle tick under apex, around (185,170)
    - 亅/hook bottom: horizontal shoulder from (155,190) to (215,190),
      then diagonal drop and small hook flick UP-LEFT at end.

Sibling watch: 令 vs 今 — 令 has hook at bottom (亅), 今 has plain 点.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def brush_stroke(points, widths):
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


# ================= 亻 (left) =================
pie_points = [
    (85, 65),
    (80, 90),
    (72, 120),
    (60, 150),
    (48, 180),
    (32, 210),
]
pie_widths = [4.5, 4.5, 4.2, 3.8, 3.0, 1.6]
brush_stroke(pie_points, pie_widths)

# tiny top curl
head_curl = [(85, 65), (91, 72), (87, 82)]
head_widths = [4.5, 3.5, 2.2]
brush_stroke(head_curl, head_widths)

# 竖 vertical
shu_points = [
    (72, 125),
    (72, 170),
    (72, 220),
    (72, 265),
]
shu_widths = [5.0, 5.0, 5.0, 4.5]
brush_stroke(shu_points, shu_widths)
d.ellipse((68, 122, 77, 131), fill="black")


# ================= 令 (right) =================

# ---- 人 roof ----
# 撇 from apex down-left
roof_pie = [
    (190, 55),
    (180, 75),
    (165, 100),
    (150, 125),
    (130, 155),
]
roof_pie_w = [5.5, 5.5, 5.0, 4.0, 2.0]
brush_stroke(roof_pie, roof_pie_w)

# 捺 from apex down-right (thickens then tapers with a foot flare)
roof_na = [
    (190, 55),
    (205, 80),
    (222, 108),
    (240, 135),
    (255, 158),
    (265, 168),
]
roof_na_w = [3.8, 4.3, 4.8, 5.2, 4.0, 1.5]
brush_stroke(roof_na, roof_na_w)

# ---- middle 点 tick under apex ----
tick = [(178, 165), (192, 178)]
tick_w = [2.0, 4.5]
brush_stroke(tick, tick_w)

# ---- bottom 横撇 + 竖钩 (龴/亅 assembly) ----
# short 横 shoulder
h_shoulder = [(155, 195), (215, 195)]
h_shoulder_w = [3.5, 4.0]
brush_stroke(h_shoulder, h_shoulder_w)

# 折 corner + 竖 drop with hook UP-LEFT
drop = [
    (213, 192),
    (210, 220),
    (205, 245),
    (198, 268),
]
drop_w = [4.5, 4.5, 4.5, 4.5]
brush_stroke(drop, drop_w)

# hook flick UP-and-LEFT (per TIER-0 hook rule)
hook = [(198, 268), (188, 260), (180, 256)]
hook_w = [4.5, 3.5, 2.0]
brush_stroke(hook, hook_w)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0314_伶/01_伶.png"
)
