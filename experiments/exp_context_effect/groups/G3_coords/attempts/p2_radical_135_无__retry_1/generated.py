# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   Errata says: "Distinctive top-heng + 撇 + 竖弯钩. No primitive fit."
#   No explicit fix idea line, but B4 retry_priority says B5 must
#   apply P12 (MMH-thin widths, ~4-5px not calligraphic 9-10px) —
#   this was the 兀/尢 family lesson. Prior attempt used ~9px widths
#   with bank shu_wan_gou at scale 0.85 — widths too heavy, hook
#   too big, 撇 tail extended past canvas edge.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   Long heng: use MMH-thin widths (~4-5px uniform, not tapered
#   calligraphic). 撇 in top-right sweeping down-left: variant_pie
#   with thin w_head=5, w_tail=2, bow_perp moderate. 竖弯钩:
#   inline thin ~4px consistent with GT MMH weight.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - Uniform thin lines (MMH GT) → thin widths per P12, NOT
#     calligraphic. THIS IS THE PRIMARY FIX. All 4 strokes get
#     uniform thin ~4-5px widths. No bank primitives (they render
#     too thick for MMH-thin radicals; wu_char.py evidence shows
#     even scale=0.85 bank heng is too heavy for a compact radical
#     when it must coexist with thin 撇 and 竖弯钩).
#   - Inline all four strokes fresh with matched thin widths.

import os
from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _thin_line(draw, p0, p1, w=4):
    draw.line([p0, p1], fill=(0, 0, 0), width=w)


def _thin_bezier(draw, p0, pc, p1, w=4, n=48):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
        prev = (bx, by)


def _tapered_bezier(draw, p0, pc, p1, w0, w1, n=48):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
        prev = (bx, by)


def draw_wu(t, ox=0.0, oy=0.0, scale=1.0):
    """无 radical, 4 strokes (per GT):
       1. Top short 横 (upper area, slightly right of center)
       2. Long 横 (main horizontal, spans width, mid-upper)
       3. Long 撇 (sweeps from top area down-left through both hengs)
       4. 竖弯钩 (from mid-right of long heng, drops, curves right, hook up)
       All strokes uniform thin ~4-5px to match MMH GT (P12).
    """
    W_THIN = 4

    # Stroke 1: top short 横. GT: sits at ~upper-third, roughly centered
    # with slight right lean. Short — about 40% of canvas width.
    s1_left = _to_pixel(ox - 30 * scale, oy + 60 * scale)
    s1_right = _to_pixel(ox + 35 * scale, oy + 58 * scale)
    _thin_line(t, s1_left, s1_right, w=W_THIN)

    # Stroke 2: long 横. Spans ~85% width, slightly above vertical center.
    s2_left = _to_pixel(ox - 90 * scale, oy + 15 * scale)
    s2_right = _to_pixel(ox + 90 * scale, oy + 12 * scale)
    _thin_line(t, s2_left, s2_right, w=W_THIN)

    # Stroke 3: long 撇. Starts above the top short heng (at ~center),
    # sweeps down-left through both hengs, ends inside frame lower-left.
    # Bring head more central and tail less extreme.
    p_head = _to_pixel(ox + 5 * scale, oy + 85 * scale)
    p_ctrl = _to_pixel(ox - 35 * scale, oy - 5 * scale)
    p_tail = _to_pixel(ox - 70 * scale, oy - 65 * scale)
    _tapered_bezier(t, p_head, p_ctrl, p_tail, w0=5, w1=2)

    # Stroke 4: 竖弯钩. Anchored on the RIGHT portion of the long heng.
    # Larger, more visible curve and hook.
    # Shaft: from (30, +13) down to (30, -50)
    shaft_top = _to_pixel(ox + 30 * scale, oy + 13 * scale)
    shaft_bot = _to_pixel(ox + 30 * scale, oy - 50 * scale)
    _thin_line(t, shaft_top, shaft_bot, w=W_THIN)

    # Curve: from (30, -50) sweeping down-right with wide arc to (75, -80).
    curve_start = shaft_bot
    curve_ctrl = _to_pixel(ox + 30 * scale, oy - 85 * scale)
    curve_end = _to_pixel(ox + 78 * scale, oy - 80 * scale)
    _thin_bezier(t, curve_start, curve_ctrl, curve_end, w=W_THIN)

    # Hook: from (78, -80) larger flick up to (80, -55).
    hook_base = curve_end
    hook_tip = _to_pixel(ox + 80 * scale, oy - 55 * scale)
    _thin_line(t, hook_base, hook_tip, w=W_THIN)


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_wu(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_无.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
