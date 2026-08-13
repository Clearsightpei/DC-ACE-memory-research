# BANK_DEVIATION
# skipped: chang.py, bai_char_for_top_stack.py
# reason: chang.py heng uses w=11 tapered — far heavier than GT's thin ~4px uniform lines;
#         bai_top has hardcoded 撇 coords that don't shift with x_left, misplacing the top pie.
# fresh_component: yuan_thin_envelope + yuan_bai_inner + yuan_xiao_inner (all inline, uniform ~4-5px)
#
# 原 (yuán) — 10 strokes: 厂 envelope (2) + 白 upper-interior (5) + 小 lower-interior (3).
# GT shows thin uniform lines throughout — inline fresh with w=4-5 across all strokes.
import os
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))


def draw_yuan(d):
    W_MAIN = 5
    W_THIN = 4
    BLACK = (0, 0, 0)

    # ---- 厂 envelope ----
    # Stroke 1: top 横 — spans wide, slight downward tilt on right end.
    d.line([(58, 42), (272, 48)], fill=BLACK, width=W_MAIN)

    # Stroke 2: long 丿 (nearly vertical, gentle scoop at tail).
    # Approximate as polyline for a soft curve.
    pie_pts = [(65, 45), (55, 110), (43, 175), (28, 235), (14, 285)]
    for a, b in zip(pie_pts, pie_pts[1:]):
        d.line([a, b], fill=BLACK, width=W_MAIN)

    # ---- 白 in upper interior ----
    # Body rectangle sits inside envelope, upper area.
    bx_l = 118
    bx_r = 208
    by_t = 95
    by_b = 175
    by_m = 138

    # Stroke 3: 短撇 above 白's body, tail kissing top-left corner.
    d.line([(160, 68), (bx_l + 3, by_t + 2)], fill=BLACK, width=W_THIN)

    # Stroke 4: 竖 (left vertical of body)
    d.line([(bx_l, by_t), (bx_l + 1, by_b)], fill=BLACK, width=W_THIN)

    # Stroke 5: 横折 (top 横 + right 竖 as one calligraphic stroke)
    d.line([(bx_l, by_t), (bx_r, by_t + 2)], fill=BLACK, width=W_THIN)
    d.line([(bx_r, by_t + 2), (bx_r + 1, by_b)], fill=BLACK, width=W_THIN)

    # Stroke 6: middle 横 (with small right gap per 白 convention)
    d.line([(bx_l + 3, by_m), (bx_r - 4, by_m)], fill=BLACK, width=W_THIN)

    # Stroke 7: bottom 横 (closes body)
    d.line([(bx_l + 1, by_b), (bx_r + 2, by_b + 1)], fill=BLACK, width=W_THIN)

    # ---- 小 in lower interior ----
    cx = 165
    xy_top = 190
    xy_bot = 282

    # Stroke 8: 竖钩 (center vertical + short hook up-left at tail)
    d.line([(cx, xy_top), (cx + 1, xy_bot - 6)], fill=BLACK, width=W_MAIN)
    d.line([(cx + 1, xy_bot - 6), (cx - 10, xy_bot - 16)],
           fill=BLACK, width=W_THIN)

    # Stroke 9: left 撇 (short pie descending)
    d.line([(cx - 18, xy_top + 8), (cx - 58, xy_bot - 8)],
           fill=BLACK, width=W_THIN)

    # Stroke 10: right 点 (descending stroke to lower-right)
    d.line([(cx + 18, xy_top + 12), (cx + 55, xy_bot - 12)],
           fill=BLACK, width=W_THIN)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_yuan(d)
    out = os.path.join(_HERE, "01_原.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
