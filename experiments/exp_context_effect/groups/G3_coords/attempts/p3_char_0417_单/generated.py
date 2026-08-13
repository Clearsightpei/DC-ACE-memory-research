# p3_char_0417_单 — 单 (dān), 8 strokes.
# Structure:
#   丷 top (mirror dot pair, 左点 + 右点)
#   Rectangular box (口) with one internal 横 (making it 田-like)
#   Long 横 extending BEYOND the box at the bottom
#   Long central 竖 piercing down through everything
# Inline fresh derivation (composition doesn't match any single bank fit;
# jia_first is closest but 单 adds the 丷 top and the long extending base 横).
import os
from PIL import Image, ImageDraw

_OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_单.png")


def draw(canvas):
    # ---- Box (upper 田-like) ----
    x_left = 100
    x_right = 200
    y_top = 78
    y_bot = 178          # bottom of the box (slightly taller)
    y_mid = 128          # middle horizontal inside box
    x_center = (x_left + x_right) // 2

    # ---- Long horizontal (base of 十, extends past box) ----
    y_base = 208
    x_base_left = 40
    x_base_right = 262

    # ---- Long central vertical (piercing) ----
    y_shu_top = y_top + 6
    y_shu_bot = 285

    # ---- Top 丷 (mirror dot pair) ----
    # Positioned closer to the box, tighter horizontal spread.
    # Left dot: leans down-left. Right dot: leans down-right (splayed 丷).
    left_dot_head = (130, 50)
    left_dot_tail = (118, 72)
    right_dot_head = (170, 50)
    right_dot_tail = (182, 72)

    w_box = 7
    w_mid = 6
    w_base = 8
    w_shu = 8
    w_dot = 7

    # Stroke 1: left dot 丶
    canvas.line([left_dot_head, left_dot_tail], fill=(0, 0, 0), width=w_dot)
    # Stroke 2: right dot 丶 (mirror)
    canvas.line([right_dot_head, right_dot_tail], fill=(0, 0, 0), width=w_dot)

    # Stroke 3: left 竖 (left side of box)
    canvas.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w_box)
    # Stroke 4: 横折 (top heng + right shu)
    canvas.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=(0, 0, 0), width=w_box)
    canvas.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w_box)
    # Stroke 5: middle heng inside box
    canvas.line([(x_left + 3, y_mid), (x_right - 3, y_mid)], fill=(0, 0, 0), width=w_mid)
    # Stroke 6: bottom heng of box
    canvas.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=(0, 0, 0), width=w_box)
    # Stroke 7: long 横 (十's horizontal, extends beyond box)
    canvas.line([(x_base_left, y_base), (x_base_right, y_base)], fill=(0, 0, 0), width=w_base)
    # Stroke 8: long central 竖 (piercing down through box + base heng)
    canvas.line([(x_center, y_shu_top), (x_center, y_shu_bot)], fill=(0, 0, 0), width=w_shu)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw(d)
    img.save(_OUT)
    print("wrote", _OUT)


if __name__ == "__main__":
    main()
