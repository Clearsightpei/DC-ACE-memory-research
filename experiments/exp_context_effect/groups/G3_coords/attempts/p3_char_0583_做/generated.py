# BANK_DEVIATION
# skipped: kou.py (turtle math-coord — mixing with PIL is a bug source
#   for L-M-R composition; also kou here needs a tight thin box inside 古)
# reason: 做 is a 3-column L-M-R (亻 + 古 + 攵). The middle 古 = 十 + 口
#   and the right 攵 (4 strokes) have no PIL bank primitives; entire
#   middle+right must be inlined in PIL. Mixing turtle 口 (with its
#   own origin math) into the same script fights the coord system.
# fresh_component: gu_ancient_inline_thin (十 + 口, MMH-thin PIL) and
#   pu_tap_inline_thin (4-stroke 攵, MMH-thin PIL)

import os
import math
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
import sys
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from ren_pang_pil_for_LR_left import draw_ren_pang_pil_for_LR_left  # noqa: E402


def bezier_stroke(d, p0, p1, p2, w_head, w_tail, n=50, black=(0, 0, 0)):
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
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def tapered_line(d, p0, p1, w_head, w_tail, n=30, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def draw_gu_inline(d, x_left=115, x_right=180, y_top=95, y_bot=225, w=5):
    """古 = 十 (top) + 口 (bottom). MMH thin ink."""
    cx = (x_left + x_right) // 2
    # 十 top part
    # 横 (crossbar of 十): full-width across top area
    y_heng = y_top + 30  # ~y=125
    tapered_line(d, (x_left - 3, y_heng), (x_right + 3, y_heng),
                 w_head=w, w_tail=w, n=25)
    # 竖 (vertical of 十): from y_top down through the 横 into the top of 口
    y_shu_top = y_top + 5   # ~y=100
    y_shu_bot = y_top + 60  # ~y=155 (just above 口)
    tapered_line(d, (cx, y_shu_top), (cx, y_shu_bot),
                 w_head=w, w_tail=w, n=25)
    # 口 (bottom): rectangle from y=160 to y=225
    y_kt = y_top + 65   # ~y=160
    y_kb = y_bot        # ~y=225
    # 竖 left
    tapered_line(d, (x_left + 5, y_kt), (x_left + 5, y_kb),
                 w_head=w, w_tail=w, n=20)
    # 横折 (top + right): top horizontal then down
    tapered_line(d, (x_left + 5, y_kt), (x_right - 5, y_kt),
                 w_head=w, w_tail=w, n=20)
    tapered_line(d, (x_right - 5, y_kt), (x_right - 5, y_kb),
                 w_head=w, w_tail=w, n=20)
    # 横 (bottom)
    tapered_line(d, (x_left + 5, y_kb), (x_right - 5, y_kb),
                 w_head=w, w_tail=w, n=20)


def draw_pu_tap(d, x_left=195, x_right=290, y_top=85, y_bot=250, w=5):
    """攵 (rap radical): 短撇 + 横 + 撇 + 捺, 4 strokes.

    Structure (based on MMH-thin GT):
      S1 短撇: short pie top-left, from upper-right to lower-left, small.
      S2 横: short horizontal, mid-upper area, right of S1's tail.
      S3 撇: long pie starting near S2 mid, sweeping down-left to bottom-left.
      S4 捺: long na starting near S3 mid-upper, sweeping down-right to bottom-right.
    """
    cx = (x_left + x_right) // 2  # ~242
    # S1: 短撇 top — slightly larger diagonal, visible
    bezier_stroke(d,
                  (cx + 22, y_top),            # head upper-right
                  (cx + 8, y_top + 20),         # control
                  (cx - 20, y_top + 40),       # tail lower-left
                  w_head=w + 2, w_tail=w - 1, n=30)
    # S2: 横 short — a horizontal bar around y_top+50, right of pie tail
    y_heng = y_top + 52
    tapered_line(d,
                 (cx - 15, y_heng),
                 (cx + 32, y_heng),
                 w_head=w, w_tail=w, n=20)
    # S3: 撇 long — from crossing area sweeping down-left
    mid_x = cx + 5
    mid_y = y_top + 55
    bezier_stroke(d,
                  (mid_x + 5, mid_y - 5),      # head near crossing
                  (mid_x - 15, mid_y + 40),    # control
                  (x_left - 5, y_bot),         # tail bottom-left
                  w_head=w + 1, w_tail=w - 2, n=55)
    # S4: 捺 long — from near S3 upper mid sweeping down-right
    bezier_stroke(d,
                  (mid_x - 5, mid_y + 5),      # head near S3 upper-mid
                  (mid_x + 20, mid_y + 50),    # control
                  (x_right + 2, y_bot - 5),    # tail bottom-right
                  w_head=w - 1, w_tail=w + 3, n=55)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 in the LEFT slot (~x 30-90)
    draw_ren_pang_pil_for_LR_left(d, cx=60, y_top=95, y_bot=225,
                                  w_pie_head=6, w_pie_tail=2, w_shu=5)

    # 古 in the MIDDLE slot (~x 110-180)
    draw_gu_inline(d, x_left=112, x_right=180, y_top=95, y_bot=225, w=5)

    # 攵 in the RIGHT slot (~x 195-290)
    draw_pu_tap(d, x_left=195, x_right=288, y_top=85, y_bot=245, w=5)

    out = os.path.join(os.path.dirname(__file__), "01_做.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
