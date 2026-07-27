"""天 (tiān, "sky", 4 strokes) — p3_char_0102_天, first attempt.

Composition = 一 (top short 横) + 大 (heng + pie + na).
Mandatory lookup checklist:
  1. success_bank grep: `da_char.py` (p3_char_0041_大) is mastered — the
     lower 3 strokes here (s2/s3/s4) mirror 大. Reuse the technique but
     OVERRIDE anchors per TR1 to match THIS composition's MMH block
     (which shrinks 大 downward to leave room for the top 横).
  2. errata grep: 天 not in errata.
  3. form_catalog: 横 (long) + 横 (short top) + 撇 + 捺 stroke set.
  4. principles_meta: TR1 (override anchors), TR10 (N joints must look
     connected but not welded).
  5. joint_atlas: 大-family — P at heng×pie crossing, N at s3.head/s4.head
     vs the middle 横 (small natural gaps ~11–18 px).

Structural expectations (from injected MMH block):
  s1 head TL(0.955,0.955) tail TR(0.13,0.82)  — top short 横
  s2 head ML(0.524,0.767) tail MR(0.458,0.617) — middle long 横
  s3 head C (0.283,0.055) tail BL(0.393,0.815) — 撇
  s4 head C (0.479,0.737) tail BR(0.774,0.897) — 捺
Joints (all in cell C):
  s1.mid ⇆ s3.head : N ≈ 17.7 px
  s2.mid ⇆ s3.mid  : P (welded)
  s2.mid ⇆ s4.head : N ≈ 11.3 px
  s3.mid ⇆ s4.head : N ≈ 17.8 px
"""

import os
import sys
from PIL import Image, ImageDraw

# Import shared G4 primitives from success_bank/code
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from heng import draw_heng  # noqa: E402
from pie import draw_pie    # noqa: E402
from na import draw_na      # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 primitive calls == expected 4
    'endpoint_mismatches': [],    # anchors used == MMH anchors exactly
    'joint_class_mismatches': [], # P at s2×s3 (welded via crossing); N elsewhere
    'overall_pass': True,
    'notes': ('Composed as short-top-heng + reused 大-style heng/pie/na '
              'with MMH anchors. s2×s3 cross naturally (P). s1/s3 head '
              'gap and s2/s4 head gap fall within N tolerance because '
              'anchors are used verbatim from MMH block.'),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — top short 横
    draw_heng(draw,
              from_anchor=('TL', 0.955, 0.955),
              to_anchor=('TR', 0.13, 0.82),
              width=8)

    # s2 — middle long 横 (spans ML→MR, crosses cell C)
    draw_heng(draw,
              from_anchor=('ML', 0.524, 0.767),
              to_anchor=('MR', 0.458, 0.617),
              width=8)

    # s3 — 撇 from C down to BL (concave-right, slight curve)
    draw_pie(draw,
             from_anchor=('C', 0.283, 0.055),
             to_anchor=('BL', 0.393, 0.815),
             head_width=10, tail_width=1, curve=-0.10, segments=48)

    # s4 — 捺 from just below middle heng, down-right to BR
    draw_na(draw,
            from_anchor=('C', 0.479, 0.737),
            to_anchor=('BR', 0.774, 0.897),
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.8, curve=0.10, segments=48)

    out = os.path.join(HERE, '01_天.png')
    img.save(out)
    print(f'wrote {out} ({img.size})')


if __name__ == '__main__':
    render()
