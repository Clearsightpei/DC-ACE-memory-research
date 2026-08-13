"""p3_char_0496_俜 — 亻 (left) + 甹 (right).

Decomposition (9 strokes per MMH):
- s1,s2 = 亻 → use bank primitive `draw_ren_left` with uniform shift.
- s3-s7 = top part of 甹 (由-like box + spike above): left-竖, 横折 (top+right),
  interior 横, interior 竖 that extends above box as spike, bottom 横.
- s8,s9 = bottom of 甹 (long 横 + 竖 hook / interior 竖).

P-A-007-v2: bank ren_left hard-check.
  bank s1_head=(158.8,73.8), target s1 anchor=(93.5,68.3) → delta ≈(-65,-5).
  bank s2_head=(138.9,158.2), target s2 anchor=(66.2,164.6) → delta ≈(-73,+6).
  Not perfectly uniform but small; use ox=-68, oy=0 (uniform shift adjustable,
  per P-A-007-v2 whole-radical hard-check — no BANK_DEVIATION needed).

P-A-008 reasoning trace:
  - single object changed for 亻: bank position → shifted (ox=-68,oy=0). Kind (a)/(b).
  - right side inline from MMH anchors — no matching whole-radical bank for 甹.
"""

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'ren_left(2) + 7 inline right-side strokes = 9 total.'
}

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from ren_left import draw_ren_left  # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1, s2: 亻 via bank primitive (2 strokes internally) — shift less to left
    draw_ren_left(d, ox=-50, oy=-5)

    # RIGHT SIDE (7 strokes) — 由 box + spike + 丂 hook
    # Box occupies roughly x=140..245, y=95..175. Spike goes up to y=45.
    # s3: 由 box left 竖
    d.line([(140, 95), (140, 175)], fill='black', width=7)

    # s4: 横折 (top + right side of 由 box)
    d.line([(140, 95), (245, 95), (245, 175)], fill='black', width=7)

    # s5: interior 横 (top interior horizontal)
    d.line([(140, 135), (245, 135)], fill='black', width=6)

    # s6: interior 竖 spike (extends above box, pierces top+middle horizontals)
    d.line([(190, 45), (190, 175)], fill='black', width=6)

    # s7: bottom of 由 box (closes it)
    d.line([(140, 175), (245, 175)], fill='black', width=7)

    # s8: long bottom 横 with hook curl down (丂/甹 bottom stroke)
    d.line([(80, 215), (275, 210), (275, 250), (255, 265)], fill='black', width=7)

    # s9: bottom 竖 (interior vertical descending from bottom of box)
    d.line([(190, 215), (192, 290)], fill='black', width=7)

    out = os.path.join(os.path.dirname(__file__), '01_俜.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
