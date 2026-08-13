"""p3_char_0182_正 (zheng — "correct/upright"). 5 strokes.

Composition: 一 on top (long heng) + 止 below (zhi_stop shape).
Reuses bank primitives `draw_heng` and `draw_shu`. 止 is a
reused-radical sibling; here we inline the 4 sub-strokes of 止
with y coordinates shifted DOWN to make room for the top heng.

Anchor plan (per MMH block, 300x300):
  s1 top heng  : x ~55->232, y ~82 (long)
  s2 upper shu : x ~146, y 108->242 (drops from just under top heng)
  s3 mid heng  : x ~160->236, y ~172 (short, right-of-center)
  s4 left shu  : x ~78->102, y 170->255 (short, drops to baseline)
  s5 bot heng  : x ~30->272, y ~268 (longest, baseline)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] /
                       'success_bank' / 'code'))

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 5 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 4 joints are class N (natural gap)
    'overall_pass': True,
    'notes': ('5-stroke composition: top heng + 止. All 4 MMH joints '
              'are class N — no welds. Small natural gaps at '
              's1-s2 (top-heng ↔ upper-shu), s2-s3 (upper-shu ↔ '
              'mid-heng), s2-s5 (upper-shu tail ↔ bot-heng), '
              's4-s5 (left-shu tail ↔ bot-heng).')
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — top heng (a bit thicker; the crown of 正)
    draw_heng(d, (55, 84), (232, 76),
              width_head=8, width_tail=10)

    # s2 — upper shu, drops from just under s1 down toward the bottom heng.
    # Small gap above (natural N joint with s1) and small gap below (N with s5).
    draw_shu(d, (145, 108), (150, 250), width=7)

    # s3 — short middle heng (right of s2), slight gap from s2's midline (N).
    draw_heng(d, (160, 172), (236, 164),
              width_head=7, width_tail=8)

    # s4 — left short shu, drops toward baseline. Small N gap over the
    # bottom heng.
    draw_shu(d, (78, 172), (102, 253), width=7)

    # s5 — long baseline heng, widest of the three.
    draw_heng(d, (30, 270), (272, 262),
              width_head=9, width_tail=11)

    out = pathlib.Path(__file__).parent / '01_正.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
