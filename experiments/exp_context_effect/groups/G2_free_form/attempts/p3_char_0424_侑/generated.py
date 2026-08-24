"""
侑 (yòu) = 亻 (left, compressed) + 有 (right, compressed).

Composition:
  Left 亻 (~30% width): 撇 down-left + 竖 down
  Right 有 (~65% width):
    - 横 (top horizontal)
    - 撇 (from horizontal, curving down-left)
    - 月 body: 横折钩 outer, 竖 inner-left, two inner 横
Hooks flick UP-and-LEFT.
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
pie_L = [(78, 65), (73, 90), (63, 125), (48, 165), (35, 195)]
pie_LW = [5.0, 4.8, 4.3, 3.2, 1.8]
brush_stroke(pie_L, pie_LW)
# tiny head curl
brush_stroke([(78, 65), (84, 71), (81, 79)], [5.0, 3.8, 2.4])

# 竖
shu_L = [(65, 128), (65, 180), (65, 230), (65, 270)]
shu_LW = [5.2, 5.2, 5.2, 4.8]
brush_stroke(shu_L, shu_LW)
d.ellipse((61, 125, 70, 134), fill="black")


# ==================== RIGHT: 有 ====================
# Stroke 1: 横 (top horizontal), slight rise right
top_h = [(115, 108), (170, 102), (225, 96), (270, 92)]
top_hw = [5.0, 4.8, 4.8, 5.2]
brush_stroke(top_h, top_hw)

# Stroke 2: 撇 — starts on 横 (left side), curves down-left
pie_R = [(165, 78), (150, 115), (130, 165), (110, 225), (98, 265)]
pie_RW = [5.2, 4.8, 4.2, 3.2, 1.8]
brush_stroke(pie_R, pie_RW)

# ---- 月 body ----
# Stroke 3: 横折钩 — top horizontal + right vertical + hook up-left
top_left = (155, 148)
top_right = (255, 148)
right_top = (255, 148)
right_bot = (245, 275)
# horizontal segment
brush_stroke([top_left, (200, 148), top_right], [5.0, 4.8, 5.0])
# right vertical (fold + down)
brush_stroke([(255, 148), (252, 200), (248, 240), (245, 275)],
             [5.0, 5.0, 5.0, 5.0])
# hook flick up-left
brush_stroke([(245, 275), (236, 268), (228, 262)], [5.0, 3.8, 2.2])

# Stroke 4: 竖 — left side of 月
brush_stroke([(158, 158), (158, 210), (158, 260), (158, 278)],
             [5.0, 5.0, 5.0, 4.6])

# Stroke 5: 横 inside (upper)
brush_stroke([(170, 190), (245, 188)], [4.5, 4.5])

# Stroke 6: 横 inside (lower)
brush_stroke([(170, 232), (245, 230)], [4.5, 4.5])


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0424_侑/01_侑.png"
)
