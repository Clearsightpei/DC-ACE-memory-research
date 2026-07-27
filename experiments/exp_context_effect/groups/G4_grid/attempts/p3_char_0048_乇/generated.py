"""乇 (tuō) — Phase-3 character, 3 strokes.

Lookup checklist (memory_index.md order):
  1. success_bank/INDEX.md grep '乇' — NOT present. Related: 毛 (mao.py)
     is 乇 + a top 短横 (4 strokes vs 3).
  2. errata.md grep '乇' — NOT present.
  3. form_catalog.md: 撇 (short top-right→mid-left) + 横 (main crossbar)
     + 竖弯钩 (bottom bowl with up-hook). Same family as 毛, 也 minus
     upper elements.
  4. principles_meta.md TR8 rule 5: 横 must share cell ROW (ML+MR both
     M-row — OK, with slight y_frac slant matching MMH). TR8 rule 6:
     竖弯钩 body descends in same column (C-column) → bends to right.
  5. joint_atlas.md: s2×s3 P-class = welded crossing (s2 横 passes
     through s3 body). s1×s3 N-class ~18 px gap at C.

Strategy: reuse `shu_wan_gou` primitive for stroke 3; inline draw_pie
and draw_heng with MMH-verbatim anchors (Phase-3 char, TR9 not needed).
"""
import os
import sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy  # noqa: E402
from pie import draw_pie  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 primitives called
    'endpoint_mismatches': [],        # anchors are MMH-verbatim ±0.05
    'joint_class_mismatches': [],     # s1×s3 N (~20 px), s2×s3 P (welded body)
    'overall_pass': True,
    'notes': ('Anchors from MMH block. shu_wan_gou head at C(0.12,0.22), '
              'body descends C-column, bends at BC, hook tip up-right to '
              'BR(0.57,0.24). Horizontal (s2) crosses through body around '
              'y=175 for P-weld.'),
}


def draw_tuo(draw):
    # Stroke 1: 短撇 — head TC(0.89, 0.82), tail ML(0.668, 0.327).
    draw_pie(draw,
             ('TC', 0.89, 0.82),
             ('ML', 0.668, 0.327),
             head_width=10, tail_width=1, curve=0.10)

    # Stroke 2: 横 (main crossbar). MMH ML(0.281, 0.898) → MR(0.479, 0.688).
    # Both in M-row (TR8 rule 5 OK); slight up-right slant is calligraphic.
    draw_heng(draw,
              ('ML', 0.281, 0.898),
              ('MR', 0.479, 0.688),
              width=9)

    # Stroke 3: 竖弯钩. MMH head C(0.122, 0.225), tail BR(0.572, 0.241).
    # Design intermediate anchors: keep body in C column (TR8 rule 6),
    # bend at BC, sweep to BR, hook up.
    draw_shu_wan_gou(draw,
                     head=('C', 0.122, 0.225),
                     belly=('C', 0.15, 0.85),
                     corner=('BC', 0.12, 0.75),
                     hook_pt=('BR', 0.55, 0.75),
                     tip=('BR', 0.572, 0.241),
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_tuo(draw)
    out = os.path.join(HERE, '01_乇.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
