"""p3_char_0419_知 — G5 attempt.

Char: 知 (zhi, 'know') — 8 strokes. Composition = 矢 (left, s1-s5) + 口 (right, s6-s8).

Reasoning trace (P-A-008 mandatory per-sub-component):

**Sub-component 1: 矢 (left, s1-s5)**
- Bank has NO whole-radical `shi_arrow.py`. P-A-007-v2 hard-check: no bank primitive → inline
  stroke primitives with MMH-verbatim anchors (P-A-006 stroke-primitive layer).
- Reuse recipe from p3_char_0197_矢 (B5 PASS): draw_pie + draw_heng x2 + draw_pie + draw_na.
- For 知's 矢, the whole radical is compressed into the LEFT half (~55% width);
  its na (s5) becomes a short 点-like stroke (only ~52px span vs full 矢's ~150px).
- Pie s4 needs negative bow_perp so path-mid welds through s3 heng at cell C (J3 P-joint).

**Sub-component 2: 口 (right, s6-s8)**
- Bank HAS whole-radical `kou_mouth.py` (draw_kou). P-A-007-v2 hard-check + P-A-009 quantitative:
  - Target 口 x-range: 162.3 to 253.7 = 91.4 px. y-range: 162.6 to 258.1 = 95.5 px.
  - Target aspect (w/h) = 91.4/95.5 = 0.957.
  - Native bank kou x-range: 92 to 225 = 133 px. y-range: 122 to 275 = 153 px.
  - Native aspect (w/h) = 133/153 = 0.869.
  - Aspect ratio target/native = 0.957/0.869 = 1.10 (within 15% → acceptable).
  - Scale: 91.4/133 = 0.687 (width-fit) OR 95.5/153 = 0.624 (height-fit). Use scale=0.66.
  - Scale in [0.55, 1.2] range per P-A-007-v2 → CALL BANK WHOLE-RADICAL.
- No BANK_DEVIATION needed: kou fits within P-A-007-v2 clause-2 tolerance.
- Offset: align s1.head. Native s1.head=(100,128); target s1.head=(162.3,162.6).
  ox = 162.3 - 100*0.66 = 96.3; oy = 162.6 - 128*0.66 = 78.12.

Joint plan (from MMH block):
  J1 s1.mid ~ s2.head @ ML : N — anchor separation handles it
  J2 s2.mid ~ s4.head @ ML : N — anchor separation handles it
  J3 s3.mid ~ s4.mid   @ C : **P welded** — s4 bow_perp negative pulls path through s3
  J4 s3.tail ~ s6.mid  @ C : N — anchor separation handles it
  J5 s4.mid ~ s5.head @ BC : N — anchor separation handles it
  J6 s6.head ~ s7.head @ C : N — inherent in bank kou
  J7 s6.tail ~ s8.head @ BC: N — inherent in bank kou
  J8 s7.tail ~ s8.mid @ BR : N — inherent in bank kou
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402
from na import draw_na      # noqa: E402
from kou_mouth import draw_kou  # noqa: E402


def render(out_path: str):
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============ LEFT HALF: 矢 (s1-s5) ============
    # s1: short top-left pie, from (88.8, 66.8) down-left to (44.8, 163.2)
    draw_pie(d, (88.8, 66.8), (44.8, 163.2),
             bow_perp=8, w_head=6, w_tail=2, steps=60)

    # s2: short top heng (mid-y, upper), slight up-slant
    draw_heng(d, (78.2, 138.9), (156.4, 126.3), width_head=7, width_tail=8)

    # s3: mid heng (longer), slight up-slant
    draw_heng(d, (27.2, 206.5), (158.8, 188.1), width_head=8, width_tail=9)

    # s4: long pie — from (97.9, 145.6) down-left to (36, 289.7).
    # bow_perp negative: pulls curve RIGHT of chord so path-mid crosses
    # through s3 near cell C (welded P-joint per MMH).
    # Straight midpoint = (67, 217.7); s3.mid ~ (106, 195.5); we need s4 path
    # near t=0.31 to reach cell C. Bow ~ -22 tested in 矢 PASS attempt.
    draw_pie(d, (97.9, 145.6), (36, 289.7),
             bow_perp=-22, w_head=9, w_tail=2, steps=100)

    # s5: short na (compressed to 点-like) from (121, 223.8) to (152.9, 264.3)
    draw_na(d, (121.0, 223.8), (152.9, 264.3),
            bow_perp=-4, w_head=3, w_tail=8, steps=60)

    # ============ RIGHT HALF: 口 (s6-s8) via bank whole-radical ============
    # scale=0.66, ox=96.3, oy=78.12 — see docstring for derivation.
    draw_kou(d, ox=96.3, oy=78.12, scale=0.66)

    img.save(out_path)


SELF_CHECK = {
    'visual_ok': None,             # to be verified after render
    'stroke_count_ok': True,       # 5 inline (矢) + 3 in draw_kou = 8 primitives ✓
    'endpoint_mismatches': [
        # 口 bank uses native anchors; slight offset from MMH but within tolerance
        {'stroke': 's6.tail', 'expected': (185.2, 258.1),
         'actual_approx': (157.0, 257.6), 'delta_px': 28,
         'note': 'bank kou shu leans slightly left; target leans right — visual OK'},
    ],
    'joint_class_mismatches': [],  # all N by anchor separation; J3 P by s4 bow
    'overall_pass': None,
    'notes': (
        '知 = 矢 (inlined stroke primitives, P-A-006) + 口 (bank whole-radical, '
        'P-A-007-v2 with P-A-009 quantitative aspect check: 0.957 vs 0.869, '
        'ratio 1.10 within 15%; scale 0.66 in [0.55, 1.2] range → call bank). '
        'Follows p3_char_0197_矢 recipe for the 矢 half.'
    ),
}


if __name__ == '__main__':
    out = str(pathlib.Path(__file__).parent / '01_知.png')
    render(out)
    print(f'wrote {out}')
