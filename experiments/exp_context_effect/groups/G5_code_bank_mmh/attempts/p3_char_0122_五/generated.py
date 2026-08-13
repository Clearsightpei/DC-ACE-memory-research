"""G5 attempt: p3_char_0122_五 (wu, 'five').

Structure (from MMH block, 4 strokes):
  s1: short top heng           TL(89,97) -> TR(220,85)
  s2: pie/shu (slight left)    C (135,106) -> BC(106,251)
  s3: heng-zhe (turn down)     ML(80,173) -> BC(173,248)
      mid(25%) welds to Center ~ (132,169)  (P joint with s2.mid)
  s4: long bottom heng         BL(37,265) -> BR(283,268)

Bank usage:
  - draw_heng x2 (s1, s4)
  - draw_pie   x1 (s2 — small right-bow for a shu-pie)
  - s3 inlined as heng-then-shu with a sharp corner (BANK_DEVIATION:
    heng_zhe_short is tuned for a tiny 乛 shape at the top of 冖/宀,
    not the wide mid-body turn 五 needs.)
"""
# BANK_DEVIATION
# skipped: heng_zhe_short.py
# reason: heng_zhe_short is a small top-of-radical 乛 shape (curved
#         bezier bend); 五's s3 wants a wide horizontal segment with a
#         near-square corner and a straight vertical drop.
# fresh_component: heng_zhe_wide_inline_for_wu (heng segment + shu segment,
#         sharp corner, thicker weight)

import sys
import pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw

from heng import draw_heng
from pie import draw_pie


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes drawn (heng, pie, inline heng-zhe, heng)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's3 uses inline heng+shu (BANK_DEVIATION); joints s1/s2 gap ~ok, s2.mid/s3.mid weld at C, s3.tail/s4.mid gap ~ok.',
}


def _draw_shu(draw, head, tail, width=8):
    """Simple straight thick line (for the vertical part of s3)."""
    hx, hy = head
    tx, ty = tail
    draw.line([head, tail], fill='black', width=width)
    r = width / 2 + 1
    draw.ellipse([tx - r, ty - r, tx + r, ty + r], fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top short heng
    draw_heng(d, (89, 97), (220, 88), width_head=8, width_tail=9)

    # s2: pie/shu, slight right-bow
    draw_pie(d, (135, 106), (106, 251),
             bow_perp=6, w_head=7, w_tail=4, steps=80)

    # s3: heng-zhe inline (wide horizontal + straight drop)
    #     head (80,173) -> corner (172,171) -> tail (173,248)
    corner = (172, 171)
    # Horizontal (heng) segment as thick line
    d.line([(80, 173), corner], fill='black', width=8)
    # small end-cap at head
    d.ellipse([80 - 4, 173 - 4, 80 + 4, 173 + 4], fill='black')
    # 顿笔 dab at corner
    d.ellipse([corner[0] - 6, corner[1] - 6,
               corner[0] + 6, corner[1] + 6], fill='black')
    # Vertical (shu) segment down from corner
    _draw_shu(d, corner, (173, 248), width=8)

    # s4: long bottom heng
    draw_heng(d, (37, 265), (283, 268), width_head=10, width_tail=11)

    out = pathlib.Path(__file__).with_name('01_五.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
