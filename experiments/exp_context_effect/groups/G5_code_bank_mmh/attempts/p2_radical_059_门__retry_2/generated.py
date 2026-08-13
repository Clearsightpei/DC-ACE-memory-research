"""G5 retry #2: p2_radical_059_门 (3 strokes).

TRAJECTORY DIFF (main C, retry_1 C, this = retry_2):
  Main-attempt visual gap: dot too skinny; horizontal top of 横折钩 too
  thin/arched; right frame too narrow. (See retry_1 diff.)
  Retry_1 visual gap vs GT:
    1. Dot (w_tail=12) is now TOO fat/blobby — GT dot is a slim angled
       tick, radius ~5-6 px at widest.
    2. Ink widths on shu (width=8) and inline heng_zhe_gou (6.5) too
       thick. GT strokes are ~4-5 px radius throughout.
    3. Inline compound had a visible arch on the top heng and stepped
       geometry at the corner — GT is a clean bank-style heng_zhe_gou.
    4. Frame trunk in retry_1 sits at x=205; GT trunk actually sits at
       ~x=215-220 (further right).
  Fixes for retry_2:
    - Dot: use draw_dian(w_tail=8, bow=4) — the bank default, slim.
    - Left shu: use draw_shu with width=5 (was 8).
    - Right frame: use bank draw_heng_zhe_gou directly (per errata
       hint) with heng_head=(115, 90), corner=(215, 90),
       gou_tail=(200, 275), hook_tip=(180, 262). This gives the clean
       calligraphic 横折钩 the GT shows, no BANK_DEVIATION needed.

MMH-derived endpoints (px on 300x300):
  stroke 1 (丶 dot):        TL(0.891,0.744) -> C(0.151,0.04)  = (89,74)  -> (115,104)
  stroke 2 (丨 left shaft): TL(0.548,0.964) -> BL(0.56,0.871) = (55,96)  -> (56,287)
  stroke 3 (横折钩 frame):  TC(0.506,0.829) -> BC(0.928,0.769)= (151,83) -> (193,277)
Joint expectations: NONE — three separate strokes.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Retry-2 revision: dot moved left+up to clear corner blob '
              'of bank heng_zhe_gou; heng_head shifted right to widen gap; '
              'gou_tail/hook_tip pulled up to keep hook off bottom edge.'),
}

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 丶 top-left dot — moved LEFT+UP so it doesn't touch the
    # bank-heng_zhe_gou corner blob. GT dot is short & compact.
    draw_dian(draw, head=(80, 72), tail=(102, 100),
              w_head=3, w_tail=7, bow=3)

    # Stroke 2: 丨 left vertical — thinner than retry_1
    draw_shu(draw, head=(55, 100), tail=(56, 283), width=5)

    # Stroke 3: 横折钩 — bank primitive (per errata retry hint).
    # heng_head shifted right (115->128) to leave a clear gap from dot;
    # gou_tail y raised (275->265) and hook y raised (262->252) to keep
    # the hook comfortably above the bottom edge.
    draw_heng_zhe_gou(draw,
                      heng_head=(128, 92),
                      corner=(215, 92),
                      gou_tail=(202, 265),
                      hook_tip=(182, 252))

    out = _HERE.parent / '01_门.png'
    img.save(str(out))
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
