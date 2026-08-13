# BANK_DEVIATION
# skipped: bai_char.py, er_ren_char.py
# reason: bai_char.py is a full-canvas PIL renderer (fills ~y=95..265) and
#         er_ren_char.py is a turtle-primitive alias — 皃 needs 白 stacked
#         in the TOP half with 儿 stretched across the BOTTOM half; neither
#         primitive fits without re-scaling their internal coord ranges,
#         which is more brittle than a clean inline PIL render.
# fresh_component: bai_top_for_stack, er_ren_bottom_for_stack
#
# 皃 (7 strokes) = 白 top + 儿 bottom (like 貌's left half).
# GT decomposition:
#   Top 白 (5): 短撇 + 竖 + 横折 + 中横 + 底横 — compact, upper half
#   Bottom 儿 (2): 撇 (left leg) + 竖弯钩 (right leg) — wide, spreads bottom
from PIL import Image, ImageDraw


def draw_bai_top(d):
    """Compact 白 in top half of canvas (y ~ 40..155). Wider than v1."""
    x_left = 112
    x_right = 198
    y_top = 62
    y_bot = 155
    y_mid = 110
    w = 6
    w_mid = 5

    # Stroke 1: 短撇 (short pie above the body, tail dropping into top-left)
    d.line([(162, 38), (x_left + 4, y_top + 2)], fill=(0, 0, 0), width=5)

    # Stroke 2: 竖 (left vertical)
    d.line([(x_left, y_top), (x_left + 1, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 3: 横折 (top 横 + right 竖)
    d.line([(x_left, y_top), (x_right, y_top + 3)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top + 3), (x_right + 1, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 4: middle 横
    d.line([(x_left + 3, y_mid), (x_right - 4, y_mid)], fill=(0, 0, 0), width=w_mid)

    # Stroke 5: bottom 横 (closes body)
    d.line([(x_left + 1, y_bot), (x_right + 2, y_bot + 1)], fill=(0, 0, 0), width=w)


def draw_er_ren_bottom(d):
    """儿 spread wider than 白 across bottom half (y ~ 155..285)."""
    # Stroke 6: 撇 (left leg) — starts at 白 base-left, curves down and
    # outward to lower-left. Smoother 4-segment approx of a bowed pie.
    pie_pts = [
        (135, 155),
        (122, 195),
        (105, 232),
        (85, 265),
        (65, 288),
    ]
    for a, b in zip(pie_pts[:-1], pie_pts[1:]):
        d.line([a, b], fill=(0, 0, 0), width=6)

    # Stroke 7: 竖弯钩 (right leg) — starts at 白 base-right, drops
    # straight, sweeps right along bottom, small up-left hook.
    # Vertical portion:
    d.line([(180, 155), (182, 250)], fill=(0, 0, 0), width=6)
    # Bottom curve sweeping right (弯):
    curve_pts = [
        (182, 250),
        (192, 273),
        (215, 285),
        (250, 285),
    ]
    for a, b in zip(curve_pts[:-1], curve_pts[1:]):
        d.line([a, b], fill=(0, 0, 0), width=6)
    # 钩: small upward hook (points up, slight left)
    d.line([(250, 285), (247, 268)], fill=(0, 0, 0), width=6)


def draw_mao(canvas):
    draw_bai_top(canvas)
    draw_er_ren_bottom(canvas)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_mao(d)
    img.save("01_皃.png")
