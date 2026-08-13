"""p3_char_0230_亘 — 亘 = long top 一 + central 日 (compressed) + long bottom 一.

Composition: 6 strokes matching MMH anchors.
  s1: top 一          (TL 82,88 -> TR 216,79)
  s2: left 竖 of 日   (80,134 -> 111,233)   [box lean slightly right-bottom]
  s3: 横折 (top+right)(100,139 -> 191,227)
  s4: middle 横       (110,183 -> 170,174)
  s5: bottom close 横 (116,219 -> 177,214)
  s6: bottom long 一  (BL 33,268 -> BR 265,267)

Not calling draw_ri (ri_sun.py) directly: ri is designed as a full-canvas
radical (y=99..289 tall, near-vertical 竖). Here the middle box is
compressed to y=134..233 and both verticals of the box lean noticeably
rightward — a scale-only ri call doesn't reproduce that geometry. So the
middle 日 is inlined using the stroke primitives (shu, heng_zhe_box,
heng) with anchor-derived pixel coords. No BANK_DEVIATION per se — we
still lean on stroke primitives; only the whole-radical draw_ri is
skipped because scale-only wouldn't match.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from heng import draw_heng
from shu import draw_shu
from heng_zhe_box import draw_heng_zhe_box


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitive calls below
    'endpoint_mismatches': [], # all anchors used verbatim
    'joint_class_mismatches': [], # all 4 joints implemented as N (natural gap)
    'overall_pass': True,
    'notes': 'middle 日 inlined from stroke primitives; draw_ri not used '
             '(full-canvas geometry differs from compressed middle-box need).'
}


def draw(canvas: Image.Image):
    d = ImageDraw.Draw(canvas)

    # s1: top 一 (medium length, right-shifted, slight upward tail)
    draw_heng(d, (82, 88), (216, 79), width_head=9, width_tail=10)

    # s2: left 竖 of middle 日 (leans slightly right)
    draw_shu(d, (80, 134), (111, 233), width=7)

    # s3: 横折 top+right of middle 日
    # top_left near s2.head with N-gap (~13px); right vertical ends at s3.tail
    # heng_zhe_box takes (top_left, bottom_right); use s3 head as TL and tail as BR
    draw_heng_zhe_box(d, (100, 139), (191, 227), width=7)

    # s4: middle 横 inside box
    draw_heng(d, (110, 183), (170, 174), width_head=6, width_tail=7)

    # s5: bottom-close 横 of box (slightly inside; N-gap to s3.tail ~17px)
    draw_heng(d, (116, 219), (177, 214), width_head=7, width_tail=8)

    # s6: bottom long 一 (spans nearly full width)
    draw_heng(d, (33, 268), (265, 267), width_head=10, width_tail=11)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw(img)
    out = Path(__file__).parent / '01_亘.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
