# tu_cun_stacked_for_LR_right.py — 寺 (土 over 寸) right-column stack variant
# Promoted from p3_char_0422_侍 (B11 main PASS, BANK_DEVIATION).
# Curator B11 (2026-08-03, position 550).
#
# CONTEXT (v13 variant policy). Bank has separate `tu.py` (土) and
# `cun.py` (寸) but stacking them for a right-column slot in an L-R
# compound (侍 = 亻 + 寺, 待 = 彳 + 寺, 恃 = 忄 + 寺, 詩 = 訁 + 寺,
# 峙 = 山 + 寺, 特 = 牜 + 寺 has related 寺-family geometry) doesn't
# compose cleanly — bank primitives are turtle-based with hardcoded
# canvas-center offsets that don't nest under vertical stacking + shared
# L-R budget.
#
# This entry inlines the PIL-pixel recipe from 侍's B11 pass: 土 upper
# (top heng short, mid shu, wide bottom heng that also serves as 寸's
# transition), 寸 lower (heng + shu_gou with hook + dian).
#
# Use for 侍/待/恃/詩/峙 (any L-R char with 寺 on the right).

from PIL import Image, ImageDraw

CANVAS = 300
CX = CY = CANVAS // 2


def _to_px(x, y):
    return (CX + x, CY - y)


def _line_stroke(d, p0, p1, w_head, w_tail, n=25):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        cur = (x, y)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            d.line([prev, cur], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r],
                      fill=(0, 0, 0))
        prev = cur


def draw_tu_cun_stacked(draw, ox=0.0):
    """Draw 寺 (土 over 寸) in the right column with optional math-x offset.

    Defaults (ox=0) place 寺 in the right half of a 300x300 canvas
    where the character's math-x center is at +40 (already the case for
    the B11 侍 PASS). Adjust ox to slide the stack left/right.

    6 strokes total: 3 for 土 (heng + shu + heng), 3 for 寸 (heng + shu_gou + dian).
    """
    x0 = ox

    # ---- 土 upper part (strokes 1-3) ----
    # 1: short top heng
    _line_stroke(draw, _to_px(x0 + 5, 105), _to_px(x0 + 75, 105),
                 w_head=4, w_tail=4, n=25)
    # 2: 丨 shu through both 土 hengs
    _line_stroke(draw, _to_px(x0 + 40, 115), _to_px(x0 + 40, 40),
                 w_head=5, w_tail=5, n=25)
    # 3: LONG bottom heng of 土 (widest horizontal — transitions into 寸)
    _line_stroke(draw, _to_px(x0 - 15, 40), _to_px(x0 + 105, 40),
                 w_head=5, w_tail=5, n=40)

    # ---- 寸 lower part (strokes 4-6) ----
    # 4: heng of 寸 (slightly shorter than the widest above)
    _line_stroke(draw, _to_px(x0 + 5, -10), _to_px(x0 + 75, -10),
                 w_head=4, w_tail=4, n=25)
    # 5: 竖钩 of 寸 — straight down, then flick up-left near tail
    _line_stroke(draw, _to_px(x0 + 40, -10), _to_px(x0 + 40, -90),
                 w_head=5, w_tail=4, n=30)
    _line_stroke(draw, _to_px(x0 + 40, -90), _to_px(x0 + 25, -78),
                 w_head=4, w_tail=2, n=15)
    # 6: dian on the 竖钩 upper-shaft
    _line_stroke(draw, _to_px(x0 + 45, -45), _to_px(x0 + 60, -55),
                 w_head=5, w_tail=3, n=15)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_tu_cun_stacked(d)
    img.save("tu_cun_stacked_preview.png")
