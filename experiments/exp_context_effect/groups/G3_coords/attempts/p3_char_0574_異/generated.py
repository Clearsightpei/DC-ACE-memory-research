# BANK_DEVIATION
# skipped: kou.py, gong_radical.py
# reason: 異's top田-box is thin uniform (MMH GT) not calligraphic like kou; bottom共 has a wide long crossbar + 八 dots not matching gong_radical geometry
# fresh_component: yi_different_top_tian_and_bottom_gong

from PIL import Image, ImageDraw

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
d = ImageDraw.Draw(img)

W = 6  # uniform thin stroke width (MMH-style)


def line(a, b, w=W):
    d.line([a, b], fill=(0, 0, 0), width=w)


def curve(p0, p1, p2, w=W, steps=48):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pts.append((x, y))
    d.line(pts, fill=(0, 0, 0), width=w)


def draw_yi_different(t):
    # === TOP: 田-like rectangle (approx y 25..135 = top; box) ===
    # Outer box corners
    box_L, box_R = 95, 205
    box_T, box_B = 35, 145
    # Left 竖
    line((box_L, box_T), (box_L, box_B))
    # Top + right 横折 (one stroke, sharp corner)
    line((box_L, box_T), (box_R, box_T))
    line((box_R, box_T), (box_R, box_B))
    # Bottom 横
    line((box_L, box_B), (box_R, box_B))
    # Interior vertical (splits box)
    mid_x = (box_L + box_R) // 2
    line((mid_x, box_T), (mid_x, box_B))
    # Interior horizontal (splits box mid)
    mid_y = (box_T + box_B) // 2
    line((box_L, mid_y), (box_R, mid_y))

    # === MIDDLE: long wide 横 under the box ===
    heng_y = 195
    line((45, heng_y), (255, heng_y), w=W + 1)

    # === BOTTOM: 共-lower — two vertical struts + 八 dots ===
    # Two vertical struts descending from the long heng
    line((105, heng_y - 3), (95, 245))
    line((195, heng_y - 3), (205, 245))
    # 八 — left 撇 and right 捺, at very bottom, splayed outward
    # Left 撇 (curved sweep down-left)
    curve((130, 245), (115, 265), (85, 285), w=W)
    # Right 捺 (curved sweep down-right)
    curve((170, 245), (195, 265), (225, 285), w=W)


draw_yi_different(d)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G3_coords/attempts/p3_char_0574_異/01_異.png"
)
