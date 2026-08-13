"""Render 厄 (retry 2) — 4 strokes: 厂 outer + 㔾 inner.

TRAJECTORY DIFF (from reading GT + main + retry_1 PNGs):
- FAILED main: interior 㔾 rendered as disconnected boxy zig-zag; upper
  heng_zhe was too high and short, lower shu_wan_gou tail hooked too
  far up and did not close the enclosure.
- FAILED retry_1: outer 厂 improved but interior still not a clean
  heng_zhe + shu_wan_gou pair — the two strokes overlapped instead of
  nesting; bottom hook still weak and tail landed near the vertical of
  the heng_zhe instead of curving out to the right.
- FIX this attempt:
  1) Keep draw_chang from bank (worked in prior C-verdict attempts —
     shape was not the reported problem).
  2) Interior heng_zhe (s3): draw as a clean ⌐ — horizontal from
     (108,148) to (198,148), turn down to (198,238). Slight 顿笔 at
     turn.
  3) Interior shu_wan_gou (s4): use bank primitive with head at
     (112,175), tail at (215,255). Give it enough bottom_extra so it
     rounds under the heng_zhe's vertical tail, forming the closed
     enclosure the GT shows.
  4) Keep N-class gaps at both joints (do NOT weld).

BANK USAGE:
- Uses draw_chang (bank) for strokes 1-2.
- Uses draw_shu_wan_gou (bank) for stroke 4.
- Inlines stroke 3 as heng_zhe (no bank primitive matches this exact
  interior corner geometry cleanly at this scale).
"""

import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from chang_cliff import draw_chang  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def _stroke_line(d, p0, p1, w0, w1, steps=40):
    (x0, y0), (x1, y1) = p0, p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = (w0 + (w1 - w0) * t) / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_heng_zhe_interior(d):
    """Interior ⌐ of 厄: horizontal then down. Slight thickening at corner."""
    # horizontal segment (slight downslope like GT)
    _stroke_line(d, (108, 148), (198, 148), 6, 6, steps=45)
    # corner tick (顿笔)
    _stroke_line(d, (198, 145), (203, 152), 5, 7, steps=8)
    # vertical descent
    _stroke_line(d, (200, 148), (198, 238), 7, 5, steps=45)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # strokes 1-2: 厂 outer
    draw_chang(d, ox=0, oy=0, scale=1.0)

    # stroke 3: interior heng_zhe
    draw_heng_zhe_interior(d)

    # stroke 4: interior shu_wan_gou (closes the enclosure)
    # tighter: reduce bottom_extra so the curve stays close to the
    # heng_zhe's tail, matching GT's compact enclosure.
    draw_shu_wan_gou(d, head=(108, 178), tail=(210, 245),
                     width=6, bottom_extra=15, knee_ratio=0.88)

    out = os.path.join(HERE, '01_厄.png')
    img.save(out)
    print('wrote', out)


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,      # 4 strokes: 2 chang + heng_zhe + shu_wan_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'Retry 2 focuses on interior enclosure closing cleanly.',
}


if __name__ == '__main__':
    main()
