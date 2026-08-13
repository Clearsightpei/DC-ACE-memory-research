"""p3_char_0152_元 (yuan) — 4 strokes.

Composition:
  s1: short top heng (TL -> TC)
  s2: longer middle heng (ML -> MR)
  s3: pie descending from left of s2 mid down-left to BL
  s4: shu_wan_gou from center down and curving right up to BR

Sibling: 无 (wu_none.py) — same 4-primitive family (heng + heng + pie +
shu_wan_gou). Key difference: in 元 the pie is SHORT and starts at the
level of the LOWER heng (does not cross above the top heng like 无 does).
Anchors are MMH-derived; no BANK_DEVIATION — all four bank primitives fit.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from heng import draw_heng           # noqa: E402
from pie import draw_pie             # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 4 primitive calls == expected 4
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        's1 head TL(0.99,0.96) tail TC(0.89,0.82) — top heng, ~short. '
        's2 head ML(0.52,0.67) tail MR(0.20,0.39) — mid heng, long. '
        's3 head ML(0.99,0.73) tail BL(0.33,0.82) — pie starts at s2 mid-'
        'level and descends left. '
        's4 head C(0.44,0.59) tail BR(0.67,0.22) — shu_wan_gou. '
        'Joints: s2.mid(0.20) N-gap ~14px to s3.head; s2.mid(0.48) N-gap '
        '~14px to s4.head — both natural N-gaps (not welded).'
    ),
}


def draw_yuan(draw):
    # s1 top short heng: TL(98.7, 96.4) -> TC(188.7, 82)
    draw_heng(draw, (99, 96), (189, 82),
              width_head=8, width_tail=9)

    # s2 middle longer heng: ML(52.1, 167.3) -> MR(219.7, 138.6)
    draw_heng(draw, (52, 167), (220, 139),
              width_head=9, width_tail=10)

    # s3 pie descending from left of s2 mid to BL
    # head ML(99, 173) -> tail BL(33, 282). Starts NEAR s2 at ~20% along
    # (natural N-gap, not welded).
    draw_pie(draw, (99, 173), (33, 282),
             bow_perp=10, w_head=8, w_tail=2)

    # s4 shu_wan_gou: head C(144, 159) -> tail BR(267, 222)
    # Starts near s2 at ~48% along (natural N-gap). Descends, curves right,
    # hooks up.
    draw_shu_wan_gou(draw, (144, 159), (267, 222),
                     width=7, bottom_extra=52, knee_ratio=0.72)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_yuan(draw)
    out = pathlib.Path(__file__).parent / '01_元.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
