"""
Render 你 = 亻 (left) + 尔 (right).

Composition:
  Left 亻 (compressed to ~35% width):
    - 撇 from ~(95, 65) down-left to ~(55, 175)
    - 竖 from ~(85, 110) straight down to ~(85, 255)

  Right 尔:
    - Top 丿 (small pie): from ~(180, 80) down-left to ~(150, 120)
    - 横折 roof: from ~(160, 118) horizontal right to ~(245, 118),
      then a short 折 down-left to ~(240, 138)
    - Central 亅 (vertical hook): from ~(200, 128) down to ~(200, 240),
      hook flicking UP-and-LEFT
    - Left leg 撇: from ~(175, 165) down-left to ~(150, 220)
    - Right leg 点: from ~(220, 165) down-right to ~(245, 220)
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


# ==================== LEFT: 亻 ====================
# 撇
pie_L = [(100, 62), (95, 85), (85, 115), (72, 145), (58, 178)]
pie_LW = [5.0, 4.8, 4.3, 3.5, 1.8]
brush_stroke(pie_L, pie_LW)
# tiny head curl
brush_stroke([(100, 62), (106, 68), (103, 76)], [5.0, 3.8, 2.4])

# 竖
shu_L = [(88, 115), (88, 165), (88, 215), (88, 258)]
shu_LW = [5.2, 5.2, 5.2, 4.8]
brush_stroke(shu_L, shu_LW)
d.ellipse((84, 112, 93, 121), fill="black")


# ==================== RIGHT: 尔 ====================

# --- Top 丿 (small slanting pie above the roof) ---
top_pie = [(185, 72), (176, 88), (162, 108), (148, 125)]
top_pie_w = [4.5, 4.2, 3.4, 1.8]
brush_stroke(top_pie, top_pie_w)

# --- 横折 (roof horizontal + short down-right fold) ---
# horizontal segment
roof_h = [(155, 120), (185, 118), (220, 118), (248, 120)]
roof_hw = [4.8, 4.5, 4.5, 4.8]
brush_stroke(roof_h, roof_hw)
# short fold: at right end, drop down-left
roof_fold = [(248, 120), (246, 130), (241, 140)]
roof_fw = [4.8, 4.0, 2.5]
brush_stroke(roof_fold, roof_fw)
# top dab
d.ellipse((151, 116, 161, 126), fill="black")

# --- 亅 (central vertical with hook) ---
gou = [(200, 128), (200, 175), (200, 225), (200, 245)]
gou_w = [5.2, 5.2, 5.2, 4.6]
brush_stroke(gou, gou_w)
# hook: flick UP-and-LEFT from bottom
hook = [(200, 245), (192, 240), (183, 232)]
hook_w = [4.6, 3.8, 2.2]
brush_stroke(hook, hook_w)
# top dab
d.ellipse((196, 124, 205, 133), fill="black")

# --- Left leg 撇 (attaches under roof, sweeps down-left) ---
leg_L = [(178, 160), (168, 180), (156, 205), (143, 225)]
leg_LW = [4.6, 4.2, 3.4, 1.8]
brush_stroke(leg_L, leg_LW)

# --- Right leg 点 (down-right diagonal dot) ---
leg_R = [(218, 160), (228, 178), (240, 200), (250, 220)]
leg_RW = [3.2, 4.0, 4.8, 5.2]
brush_stroke(leg_R, leg_RW)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0297_你/01_你.png"
)
