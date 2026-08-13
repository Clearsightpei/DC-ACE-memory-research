# zhu_master_for_LR_right.py — 主 variant (shifted+scaled for L-R right slot)
# Promoted from p3_char_0399_往 (B11 main PASS, BANK_DEVIATION).
# Curator B11 (2026-08-03, position 550).
#
# CONTEXT (v13 variant policy). The bank's `zhu_master.py` is a
# canvas-centered 5-stroke 主 with hard-coded pixel coords and no
# (ox, oy, scale) hooks. When 主 is the RIGHT component of an L-R char
# (往 = 彳+主, and future 住/注/柱/驻/柱 all share this shape), the
# canvas-centered recipe overlaps the left radical.
#
# This variant re-parametrizes zhu_master's recipe with a horizontal
# offset and uniform scale applied to the math coordinates, so callers
# can slot 主 into any right-column position. The recipe geometry
# (dot lean, graduated heng ladder, shu-starts-at-top-heng, thin P12
# ink) is preserved verbatim from the B7 v9 graduate.
#
# The original `zhu_master.py` remains untouched. Use this variant when
# 主 sits in the right column of an L-R composition.

from PIL import Image, ImageDraw

CANVAS = 300


def _p(mx, my, size=CANVAS):
    return size / 2 + mx, size / 2 - my


def draw_zhu_for_lr_right(t, mx_off=55.0, scale=0.85, ink=4):
    """Draw 主 shifted by mx_off math-units and uniformly scaled.

    Defaults (mx_off=55, scale=0.85) are the exact values that PASSed
    for 往 in B11. Override for other L-R compounds:
      - 住 / 注 (亻/氵 on left, both ~2-stroke narrow radicals):
        try mx_off ~ +55, scale ~ 0.85 (same as 往).
      - 柱 / 驻 (木 / 马 on left, both wider): try mx_off ~ +65, scale ~ 0.80.
    """
    s = scale
    ox = mx_off

    # 1. top dot 丶 (canonical lean: upper-left DOWN to lower-right)
    t.line([_p(-6 * s + ox, 85 * s), _p(6 * s + ox, 72 * s)],
           fill=(0, 0, 0), width=ink + 1)

    # 2. top heng (shortest of ladder)
    t.line([_p(-30 * s + ox, 55 * s), _p(30 * s + ox, 55 * s)],
           fill=(0, 0, 0), width=ink)

    # 3. middle heng (wider)
    t.line([_p(-40 * s + ox, 5 * s), _p(40 * s + ox, 5 * s)],
           fill=(0, 0, 0), width=ink)

    # 4. shu 丨 (starts AT top heng, ends AT bottom heng)
    t.line([_p(0 * s + ox, 55 * s), _p(0 * s + ox, -55 * s)],
           fill=(0, 0, 0), width=ink)

    # 5. bottom heng (widest)
    t.line([_p(-65 * s + ox, -55 * s), _p(65 * s + ox, -55 * s)],
           fill=(0, 0, 0), width=ink)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_zhu_for_lr_right(d)
    img.save("zhu_for_lr_right_preview.png")
