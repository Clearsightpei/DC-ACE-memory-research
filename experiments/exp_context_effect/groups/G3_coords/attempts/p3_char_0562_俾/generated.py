# p3_char_0562_俾 — 俾 (bǐ) = 亻 (left) + 卑 (right).
#
# Left: canonical 亻 via ren_pang_pil_for_LR_left (v13 PIL bank).
# Right (卑): drawn inline in PIL px coords. Composition:
#   - short 丿 (pie) at top
#   - 田-like rectangular box (with middle horizontal)
#   - central 竖 extending below the box
#   - long 横 at the bottom crossing the central 竖 (the 十 base of 卑)
#
# Right slot compressed into x~130-260, y~55-275.

import os
import sys
from PIL import Image, ImageDraw

CANVAS = 300
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PNG = os.path.join(OUT_DIR, "01_俾.png")

# Import the PIL 亻 primitive from bank.
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))
from ren_pang_pil_for_LR_left import draw_ren_pang_pil_for_LR_left  # noqa


def _bezier(d, p0, p1, p2, w_head, w_tail, n=45, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r],
                      fill=black)
        prev = cur


def _line(d, p0, p1, w, black=(0, 0, 0)):
    d.line([p0, p1], fill=black, width=w)


def draw_bei_right(d):
    """卑 in right slot of 俾."""
    # Box: 田-like rectangle
    x_left = 150
    x_right = 250
    y_top = 90
    y_bot = 180
    y_mid = 138  # middle horizontal in box

    w_box = 5
    w_mid = 4
    w_shu = 5

    # Stroke 1: 丿 short pie above box (tilts down-left)
    _bezier(
        d,
        (x_left + 55, 55),      # head upper-right
        (x_left + 40, 70),      # control
        (x_left + 20, 88),      # tail
        w_head=6, w_tail=2, n=30,
    )

    # Stroke 2: left 竖 of box
    _line(d, (x_left, y_top), (x_left, y_bot), w_box)

    # Stroke 3: 横折 top+right of box
    _line(d, (x_left, y_top), (x_right, y_top), w_box)
    _line(d, (x_right, y_top), (x_right, y_bot), w_box)

    # Stroke 4: middle horizontal inside box
    _line(d, (x_left + 2, y_mid), (x_right - 2, y_mid), w_mid)

    # Stroke 5: bottom of box
    _line(d, (x_left, y_bot), (x_right, y_bot), w_box)

    # Central 竖 — extends from top of box down through and below
    x_center = (x_left + x_right) // 2
    y_shu_top = y_top + 3
    y_shu_bot = 275
    _line(d, (x_center, y_shu_top), (x_center, y_shu_bot), w_shu)

    # Bottom long 横 — spans wider than the box, crosses the shu
    y_hen = 235
    _line(d, (x_left - 20, y_hen), (x_right + 15, y_hen), w_box)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    # Left: 亻 canonical
    draw_ren_pang_pil_for_LR_left(d, cx=70, y_top=95, y_bot=230)
    # Right: 卑
    draw_bei_right(d)
    img.save(OUT_PNG)
    print("wrote", OUT_PNG)


if __name__ == "__main__":
    main()
