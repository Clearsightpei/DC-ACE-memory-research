"""伪 = 亻 (left) + 为 (right). 6 strokes total per MMH.

Read order per memory_index v8:
  1. drawer_memory.md — component split, use ren_side for 亻; 为 drawn fresh
     (为 was FAIL in B2 errata; no bank primitive for 为-standalone).
  2. INDEX grep — ren_side.py exists (used by 化/他/仕/etc.).
  3. errata grep — 为 (p3_char_0096) errata note used for 横折钩 shape.

Split: 亻 = 撇 + 竖 (2 strokes); 为 = 点 + 撇 + 横折钩 + 点 (4 strokes).

MMH anchors:
  s1 pie:  ('TL', 0.967, 0.668) → ('ML', 0.231, 0.983)   [亻 撇]
  s2 shu:  ('ML', 0.712, 0.55)  → ('BL', 0.756, 0.895)   [亻 竖 — T on s1]
  s3 dian: ('TC', 0.321, 0.888) → ('C',  0.573, 0.192)   [为 top 点]
  s4 pie:  ('TC', 0.919, 0.636) → ('BL', 0.946, 0.751)   [为 主 撇]
  s5 hzg:  ('C',  0.075, 0.567) → ('BC', 0.764, 0.663)   [为 横折钩]
           corner inferred at ('C', 0.801, 0.498) from joint spec
  s6 dian: ('C',  0.729, 0.916) → ('BR', 0.001, 0.191)   [为 inner 点]

Joints (5):
  s1.mid ⇆ s2.head : N  (亻 T-style but MMH says N — leave small gap)
  s1.head ⇆ s3.head : N  (both up-top, small gap)
  s2.tail ⇆ s4.tail : N  (bottom-of-亻-shu near bottom-of-为-pie tail: gap ~29 px)
  s4.mid ⇆ s5.mid   : P  (welded crossing at C 0.801, 0.498)
  s4.mid ⇆ s6.head  : N  (s4 body near s6 head, gap ~14 px)
"""

SELF_CHECK = {
    'visual_ok': None,           # filled after render
    'stroke_count_ok': True,     # 6 primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 's5 corner inferred from P-joint anchor at C(0.801,0.498); '
             '横折钩 hook tip inferred at BC(0.55,0.50) (up-left from tail).'
}

import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import CANVAS
from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from heng_zhe_gou import draw_heng_zhe_gou


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    # ---- 亻 (left radical) ----
    # s1 撇
    draw_pie(d,
             from_anchor=('TL', 0.967, 0.668),
             to_anchor=('ML', 0.231, 0.983),
             head_width=12, tail_width=1, curve=0.10)

    # s2 竖 (short vertical dropping from mid-upper)
    draw_shu(d,
             from_anchor=('ML', 0.712, 0.55),
             to_anchor=('BL', 0.756, 0.895),
             width=9)

    # ---- 为 (right side) ----
    # s3 top 点 (short down-right from TC to C)
    draw_dian(d,
              from_anchor=('TC', 0.321, 0.888),
              to_anchor=('C', 0.573, 0.192),
              head_width=2, peak_width=10, curve=0.08)

    # s4 main 撇 (long down-left curve from TC top to BL bottom)
    draw_pie(d,
             from_anchor=('TC', 0.919, 0.636),
             to_anchor=('BL', 0.946, 0.751),
             head_width=13, tail_width=2, curve=0.12, segments=60)

    # s5 横折钩 (heng-zhe-gou) — spans C-left across to right, then down to BC
    # Corner welded to s4 body per P-joint spec. s4 chord passes through
    # (~152, 150) at that y-level; snap corner slightly right of chord so
    # the weld is visible (shoulder disc handles overlap). Extend horizontal
    # further right and add a visible hook flick per GT.
    draw_heng_zhe_gou(d,
                      head=('C', 0.075, 0.567),
                      corner=('MR', 0.30, 0.35),   # was ('C', 0.801, 0.498) — widen right
                      tail=('BC', 0.764, 0.663),
                      tip=('BC', 0.45, 0.35),      # bigger up-left hook
                      h_width=10, v_width=10, shoulder=14, tip_w=2)

    # s6 inner 点 (small right-down dot inside the belly of 为)
    draw_dian(d,
              from_anchor=('C', 0.729, 0.916),
              to_anchor=('BR', 0.001, 0.191),
              head_width=2, peak_width=10, curve=0.08)

    out = os.path.join(HERE, '01_伪.png')
    img.save(out)
    print(f'Wrote {out}')


if __name__ == '__main__':
    render()
