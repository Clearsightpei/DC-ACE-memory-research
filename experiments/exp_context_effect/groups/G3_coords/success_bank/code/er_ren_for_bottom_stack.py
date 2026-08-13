# er_ren_for_bottom_stack.py — 儿 variant (wide, bottom-half spread)
# Promoted from p3_char_0356_皃 (B10 main PASS, BANK_DEVIATION).
# Curator B10 (2026-07-31, position 500).
#
# CONTEXT (v13 variant policy). The bank's `er_ren_char.py` is a
# turtle-primitive alias sized for standalone-radical proportions.
# For top+底 stack compositions where 儿 anchors the BOTTOM (皃, 兒,
# 兄, 光, 見), 儿's legs need to spread WIDE and sit low, and the
# widths need to stay thin (~6px MMH-style) so it doesn't visually
# overweight the top radical.
#
# This variant spans y≈155..288 with legs anchoring at x≈65 (pie tail)
# and x≈250 (shu-wan-gou tail) — the exact recipe that PASSed for 皃.
# Same "reject-bank-for-weight" family as B7/B8's 大/主/疒/兇 lesson:
# the bank er_ren carries too much calligraphic weight for MMH-thin GTs.
#
# The original `er_ren_char.py` remains untouched.

from PIL import Image, ImageDraw


def draw_er_ren_bottom(canvas,
                       pie_head=(135, 155), pie_tail=(65, 288),
                       shu_top=(180, 155), shu_bend=(182, 250),
                       sweep_end=(250, 285), hook_end=(247, 268),
                       w=6):
    """Draw a wide bottom-stack 儿 (2 strokes).

    Stroke 1: 撇 (left leg) — 4-segment bowed pie from pie_head to pie_tail.
    Stroke 2: 竖弯钩 (right leg) — vertical drop + right sweep + up-left hook.
    """
    # Stroke 1: 撇 — 4-segment polyline for a gentle bow.
    ph_x, ph_y = pie_head
    pt_x, pt_y = pie_tail
    # Interpolate 3 interior points along a slight bow.
    mid_pts = [
        (ph_x + (pt_x - ph_x) * 0.20 - 4, ph_y + (pt_y - ph_y) * 0.30),
        (ph_x + (pt_x - ph_x) * 0.50 - 8, ph_y + (pt_y - ph_y) * 0.58),
        (ph_x + (pt_x - ph_x) * 0.80 - 4, ph_y + (pt_y - ph_y) * 0.85),
    ]
    pts = [pie_head, *mid_pts, pie_tail]
    for a, b in zip(pts[:-1], pts[1:]):
        canvas.line([a, b], fill=(0, 0, 0), width=w)

    # Stroke 2: 竖弯钩
    # Vertical portion
    canvas.line([shu_top, shu_bend], fill=(0, 0, 0), width=w)
    # Bottom sweep — 3-segment polyline for gentle wan
    bx, by = shu_bend
    ex, ey = sweep_end
    curve_pts = [
        shu_bend,
        (bx + (ex - bx) * 0.20, by + (ey - by) * 0.40 - 3),
        (bx + (ex - bx) * 0.60, ey),
        sweep_end,
    ]
    for a, b in zip(curve_pts[:-1], curve_pts[1:]):
        canvas.line([a, b], fill=(0, 0, 0), width=w)
    # 钩: small upward hook
    canvas.line([sweep_end, hook_end], fill=(0, 0, 0), width=w)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_er_ren_bottom(d)
    img.save("01_er_ren_bottom.png")
