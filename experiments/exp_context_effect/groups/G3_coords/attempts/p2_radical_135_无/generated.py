# p2_radical_135_无 — 无 (wú, "not/none"), 4 strokes.
# Structure:
#   1. Top short 横 (upper-right area, above middle heng)
#   2. Long 横 (main horizontal, spans most of width)
#   3. Long 撇 (sweeps from upper-right, crosses down through the horizontals, exits lower-left)
#   4. 竖弯钩 (from mid-height on the right of the long heng, curves right and hooks up)
#
# G3 coord format: numeric offsets, no anchors.
# Uses bank primitives heng (top short heng) and shu_wan_gou (last stroke).
# 撇 and long 横 are inlined fresh (long heng needs custom length; the sweeping
# pie needs custom bow beyond bank-primitive defaults).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     '..', '..', 'success_bank', 'code')
_BANK = os.path.normpath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_bezier_px(draw, p0, pc, p1, w0, w1, n=48):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        w = w0 + (w1 - w0) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
        prev = (bx, by)


def _tapered_line_px(draw, p0, p1, w0, w1, n=24):
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        x0 = p0[0] + u0 * (p1[0] - p0[0])
        y0 = p0[1] + u0 * (p1[1] - p0[1])
        x1 = p0[0] + u1 * (p1[0] - p0[0])
        y1 = p0[1] + u1 * (p1[1] - p0[1])
        w = w0 + (w1 - w0) * ((u0 + u1) / 2)
        draw.line([(x0, y0), (x1, y1)],
                  fill=(0, 0, 0), width=max(1, int(round(w))))


def draw_wu(t, ox=0.0, oy=0.0, scale=1.0):
    """无 radical, 4 strokes."""
    # Stroke 1: top short 横 (upper-right area). GT shows it sits above and
    # right of center. Use bank heng at offset.
    draw_heng(t, ox=ox + 20.0 * scale, oy=oy + 50.0 * scale,
              scale=0.55 * scale)

    # Stroke 2: long main 横 (spans most of width, slightly above center).
    # Inline for full-width + slight taper + right-end 顿笔 blob.
    lh_left, lh_lY = _to_pixel(ox - 100.0 * scale, oy + 15.0 * scale)
    lh_right, lh_rY = _to_pixel(ox + 100.0 * scale, oy + 10.0 * scale)
    _tapered_line_px(t, (lh_left, lh_lY), (lh_right, lh_rY), 9.0, 8.0)
    # Right-end small 顿笔 blob
    t.ellipse([lh_right - 5, lh_rY - 5, lh_right + 5, lh_rY + 5],
              fill=(0, 0, 0))

    # Stroke 3: long 撇 — from above the top heng, sweeping down and
    # significantly leftward, exiting past the lower-left corner.
    # GT shows the head starts around the middle-upper area (about where
    # the top heng's left edge is) and sweeps in a bowed arc to lower-left.
    p_head = _to_pixel(ox + 5.0 * scale, oy + 85.0 * scale)
    p_ctrl = _to_pixel(ox - 55.0 * scale, oy - 30.0 * scale)
    p_tail = _to_pixel(ox - 105.0 * scale, oy - 115.0 * scale)
    _tapered_bezier_px(t, p_head, p_ctrl, p_tail, 8.0, 1.5)

    # Stroke 4: 竖弯钩 (bottom-right).
    # Its shaft head is at the right portion of the long heng and drops down,
    # curves right, hooks up.
    draw_shu_wan_gou(t, ox=ox + 20.0 * scale, oy=oy - 45.0 * scale,
                     scale=0.85 * scale)


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
