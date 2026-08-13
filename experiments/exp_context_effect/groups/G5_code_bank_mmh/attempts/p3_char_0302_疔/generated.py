"""p3_char_0302_疔 — G5 attempt.

Structure: 疒 (sickness radical, 5 strokes) + 丁 inside (2 strokes) = 7.
All 7 strokes rendered from MMH anchors using bank stroke-primitives:
dian, heng, pie, ti, shu_gou. This follows P-A-006 (MMH-anchor
verbatim + stroke-primitive layer, refuse whole-radical composition).

BANK check:
- No whole-radical primitive for 疒 in bank; 丁 has no direct entry
  either. Inline via stroke primitives per P-A-006.
- All bank primitives called by endpoint (TR1-TR7 compliant).
"""

import os
import sys

from PIL import Image, ImageDraw

# Bank primitives (callable from success_bank/code/)
_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from dian import draw_dian          # noqa: E402
from heng import draw_heng          # noqa: E402
from pie import draw_pie            # noqa: E402
from ti import draw_ti              # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 7 primitives = 7 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 4 joints are class N (neighbor gap)
    'overall_pass': True,
    'notes': ('7 strokes via stroke-primitive layer (P-A-006). '
              'All joints N — gaps preserved, no welding.'),
}


def draw(img_path):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top dot of 疒 — TC(0.462,0.545) → TC(0.781,0.809)
    draw_dian(d, head=(146, 55), tail=(178, 81),
              w_head=3, w_tail=7, bow=3)

    # s2: top heng of 疒 — C(0.037,0.128) → TR(0.335,0.993)
    draw_heng(d, head=(103, 113), tail=(233, 99),
              width_head=8, width_tail=10)

    # s3: long pie of 疒 — ML(0.844,0.081) → BL(0.41,1.003)
    draw_pie(d, head=(84, 108), tail=(41, 300),
             bow_perp=14, w_head=9, w_tail=3)

    # s4: small inside dot — ML(0.396,0.298) → ML(0.636,0.57)
    draw_dian(d, head=(40, 130), tail=(64, 157),
              w_head=3, w_tail=6, bow=2)

    # s5: inside ti (rising) — BL(0.193,0.124) → ML(0.791,0.901)
    # ti head is the heavy lower-left end; tail is fine upper-right end.
    draw_ti(d, head=(19, 212), tail=(79, 190),
            w_head=8, w_tail=2)

    # s6: heng of 丁 — C(0.104,0.685) → MR(0.52,0.591)
    draw_heng(d, head=(110, 168), tail=(252, 159),
              width_head=8, width_tail=10)

    # s7: shu-gou of 丁 — C(0.69,0.702) → BC(0.418,0.771)
    draw_shu_gou(d, head=(169, 170), tail=(141, 277),
                 width=7, hook_start_offset=32)

    img.save(img_path)


if __name__ == '__main__':
    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '01_疔.png',
    )
    draw(out)
    print('wrote', out)
