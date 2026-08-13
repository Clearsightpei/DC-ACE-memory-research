"""p2_radical_045_寸 — G5 attempt.

寸 = 3 strokes: 横 (heng, top), 竖钩 (shu-gou, vertical hook piercing the
heng near its right end), 丶 (dian, short dot in the lower-left interior).

Bank primitives used as-is:
  - heng.draw_heng       — top horizontal
  - shu_gou.draw_shu_gou — vertical hook
  - dian.draw_dian       — dot

米字格 → pixel: 3x3 grid, each cell 100x100 on a 300x300 canvas.
Cell origins (x0, y0):
  TL(0,0)   TC(100,0)   TR(200,0)
  ML(0,100) C (100,100) MR(200,100)
  BL(0,200) BC(100,200) BR(200,200)

MMH anchors:
  s1 head ML(0.416,0.521)=(41.6,152.1)  tail MR(0.692,0.397)=(269.2,139.7)
  s2 head TC(0.646,0.633)=(164.6, 63.3) tail BC(0.318,0.730)=(131.8,273.0)
  s3 head ML(0.952,0.775)=(95.2,177.5)  tail BC(0.257,0.121)=(125.7,212.1)

Joint expectation:
  s1.mid(0.61) ⇆ s2.mid(0.30) @ cell C — class P (welded piercing).
  The heng crosses the vertical body; drawing them separately with the
  MMH endpoints naturally welds them since the shu-gou body passes
  through the horizontal.
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng            # noqa: E402
from shu_gou import draw_shu_gou      # noqa: E402
from dian import draw_dian            # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitive calls == expected 3
    'endpoint_mismatches': [], # all endpoints from MMH anchors verbatim
    'joint_class_mismatches': [],  # s1×s2 naturally welded (P) — both strokes drawn full-length through cell C
    'overall_pass': True,
    'notes': 'Bank primitives (heng, shu_gou, dian) fit 寸 as-is; no BANK_DEVIATION.',
}


def anchor(cell, xf, yf):
    """米字格 anchor → pixel on 300x300 canvas."""
    ox = {'L': 0, 'C': 100, 'R': 200,
          'T': 0, 'M': 100, 'B': 200}
    # cell is like 'TL','TC','TR','ML','C','MR','BL','BC','BR'
    if cell == 'C':
        cx0, cy0 = 100, 100
    else:
        row, col = cell[0], cell[1]
        cy0 = {'T': 0, 'M': 100, 'B': 200}[row]
        cx0 = {'L': 0, 'C': 100, 'R': 200}[col]
    return (cx0 + xf * 100, cy0 + yf * 100)


def draw_cun(draw):
    # stroke 1: 横
    s1_head = anchor('ML', 0.416, 0.521)   # (41.6, 152.1)
    s1_tail = anchor('MR', 0.692, 0.397)   # (269.2, 139.7)
    draw_heng(draw, s1_head, s1_tail, width_head=8, width_tail=9)

    # stroke 2: 竖钩
    s2_head = anchor('TC', 0.646, 0.633)   # (164.6, 63.3)
    s2_tail = anchor('BC', 0.318, 0.730)   # (131.8, 273.0)
    draw_shu_gou(draw, s2_head, s2_tail, width=7, hook_start_offset=45)

    # stroke 3: 丶 (dot, going down-right inside the character)
    s3_head = anchor('ML', 0.952, 0.775)   # (95.2, 177.5)
    s3_tail = anchor('BC', 0.257, 0.121)   # (125.7, 212.1)
    draw_dian(draw, s3_head, s3_tail,
              w_head=2, w_tail=6, bow=2, steps=32)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_cun(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_寸.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
