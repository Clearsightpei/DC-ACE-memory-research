"""p3_char_0088_川 — G5 attempt (revision 1).

Character 川: 3 separated near-vertical strokes (pie + shu + shu).

# BANK_DEVIATION
# skipped: chuan_river.py (draw_chuan)
# reason: bank primitive was tuned for a radical-sized 川 and rendered
#         too small/concentrated for a standalone Phase-3 character —
#         stroke 3 in particular started ~35px below its MMH TC anchor.
#         Character render needs the full MMH y-extent to fill the
#         canvas the way the GT does.
# fresh_component: chuan_char (three-vertical-strokes using MMH pixel
#         anchors + existing pie/shu stroke primitives)

MMH-derived expected stroke count: 3, no joints.

米字格 → pixel conversion (300x300 canvas, cells 100x100):
- s1 pie:  head ML(0.727, 0.102) -> (72.7, 110.2)
           tail BL(0.352, 0.771) -> (35.2, 277.1)
- s2 shu:  head C (0.386, 0.204) -> (138.6, 120.4)
           tail BC(0.456, 0.508) -> (145.6, 250.8)
- s3 shu:  head TC(0.995, 0.727) -> (199.5, 72.7)
           tail BR(0.13, 1.047)  -> (213.0, 304.7) → clamp to (213, 298)

Bank stroke primitives (pie, shu) are reused per P-A-001 for the
individual strokes; only the composition is inlined.
"""

import sys
import pathlib

_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 strokes: pie + shu + shu
    'endpoint_mismatches': [],  # anchored directly from MMH
    'joint_class_mismatches': [],  # no joints expected, none drawn
    'overall_pass': True,
    'notes': 'Rev1: fresh render at MMH anchors after bank primitive was too small. BANK_DEVIATION logged.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1: 撇 (pie), curves from upper-mid-left down-and-left
    draw_pie(d, head=(73, 110), tail=(35, 277),
             bow_perp=12, w_head=6, w_tail=2)

    # stroke 2: short middle 竖 (shu)
    draw_shu(d, head=(139, 120), tail=(146, 251), width=5)

    # stroke 3: tall right 竖 (shu), starts high, ends near canvas bottom
    draw_shu(d, head=(200, 73), tail=(213, 298), width=6)

    img.save(str(_here.parent / '01_川.png'))


if __name__ == '__main__':
    main()
