"""p3_char_0102_天 — G5 attempt.

Char: 天 (tian, 'sky') — 4 strokes: short-heng + longer-heng + pie + na.
Composition = 大 (da) with an extra short heng on top (s1).

Bank retrieval:
- Considered draw_da (heng+pie+na) but 大's baked anchors DIFFER from 天's
  bottom-3 anchors: e.g. da s2 head at (121.9, 62.7) whereas 天 s3 head at
  (128.3, 105.5) — 天 pie starts LOWER (below the s2 heng). Inlining stroke
  primitives with MMH endpoints preserves anchor fidelity (per playbook
  'inline from stroke bank when MMH anchor spread differs from primitive's
  baked geometry', validated for 囗/日 in B2).
- Uses bank stroke primitives: draw_heng x2, draw_pie, draw_na — no
  BANK_DEVIATION needed.

MMH anchors (px):
  s1: heng head=(95.5, 95.5)  tail=(213.0, 82.0)  — short top heng, slight up-slant
  s2: heng head=(52.4, 176.7) tail=(245.8, 161.7) — longer middle heng, slight up-slant
  s3: pie  head=(128.3, 105.5) tail=(39.3, 281.5) — starts BELOW s1 (N-gap ~17px)
  s4: na   head=(147.9, 173.7) tail=(277.4, 289.7) — starts near s2 mid (N-gap ~11px)

Joints:
  J1 s1.mid ~ s3.head @ C : N (natural gap ~17px, s3.head y=105 vs s1.mid y=93)
  J2 s2.mid ~ s3.mid @ C  : P (welded — s3 pie curves through s2 at ~(138,167))
  J3 s2.mid ~ s4.head @ C : N (gap ~11px, s4.head y=174 vs s2 y=170 → tiny)
  J4 s3.mid ~ s4.head @ C : N (gap ~17px, pie and na both cross near C)
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402
from na import draw_na      # noqa: E402


def render(out_path: str):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short top heng — slight up-slant
    draw_heng(d, (95.5, 95.5), (213.0, 82.0), width_head=7, width_tail=8)

    # s2: longer mid heng — slight up-slant
    draw_heng(d, (52.4, 176.7), (245.8, 161.7), width_head=8, width_tail=9)

    # s3: pie — starts at (128, 106), sweeps down-left to (39, 282).
    # bow_perp negative bows the curve so at t~0.30 it crosses through
    # C (~138, 167) — needed for the P-joint with s2. Straight-line s3
    # at t=0.30 = (102, 158); we need to bow the curve RIGHT so path-mid
    # comes back through the crossing point of s2.
    draw_pie(d, (128.3, 105.5), (39.3, 281.5),
             bow_perp=-24, w_head=9, w_tail=2, steps=100)

    # s4: na — from (148, 174) to (277, 290), gentle flat na
    draw_na(d, (147.9, 173.7), (277.4, 289.7),
            bow_perp=-8, w_head=3, w_tail=11, steps=100)

    img.save(out_path)


SELF_CHECK = {
    'visual_ok': None,  # filled after render
    'stroke_count_ok': True,       # 4 primitives: heng, heng, pie, na
    'endpoint_mismatches': [],     # all four anchors used MMH verbatim
    'joint_class_mismatches': [],  # J1/J3/J4 N via anchor separation; J2 P via pie bow
    'overall_pass': None,
    'notes': (
        'Inlined stroke bank primitives with MMH-verbatim endpoints. '
        'Pie bow_perp=-24 tuned so path-mid crosses through the s2 heng '
        'near C (~138,167) for the P-joint. N-gaps at J1/J3/J4 are '
        'inherent from anchor separations (17/11/17 px expected).'
    ),
}


if __name__ == '__main__':
    out = str(pathlib.Path(__file__).parent / '01_天.png')
    render(out)
    print(f'wrote {out}')
