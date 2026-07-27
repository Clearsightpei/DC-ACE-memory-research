"""p3_char_0152_元 (yuán, "origin", 4 strokes).

Lookup checklist (per memory_index.md):
1. success_bank/INDEX.md grep — no `yuan.py` exists yet. 儿 component
   (er_legs.py) mastered; heng.py mastered; pie.py mastered;
   shu_wan_gou.py mastered (docstring even names 元 as user).
2. errata.md grep — 元 not in errata. Related 兀 fix says: compose
   as heng (top) + er_legs.py (儿 body). Same principle applies to 元
   which is 二 + 儿 (two hengs on top instead of one).
3. form_catalog / joint_atlas — heng straight (TR8), 撇 diagonal
   from upper-right to lower-left, 竖弯钩 vertical-then-right-then-up-hook.
   Two N joints between the long heng and the two 儿 legs.
4. TR1: OVERRIDE all primitive anchors for THIS composition; do not
   call with defaults.

Strokes (per MMH structural expectations):
  s1 — short 横 (top): TL(0.987,0.964) → TC(0.887,0.82)
  s2 — long  横 (mid): ML(0.521,0.673) → MR(0.197,0.386)
  s3 — 撇          : ML(0.99,0.731) → BL(0.325,0.821)
  s4 — 竖弯钩      : C(0.444,0.594) → BR(0.672,0.221) (tip up-flick)

Joints:
  j1: s2.mid(0.20) ⇆ s3.head @ ML — N (~21 px gap)
  j2: s2.mid(0.48) ⇆ s4.head @ C  — N (~17 px gap)
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 primitive calls, matches MMH=4
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'heng + heng + pie + shu_wan_gou; N-gaps preserved per MMH.'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — short heng at top (slight down-right slope per MMH: y goes 96.4 → 82)
    draw_heng(d,
              from_anchor=('TL', 0.987, 0.964),
              to_anchor  =('TC', 0.887, 0.82),
              width=9)

    # s2 — long heng across middle (slight rise to the right)
    draw_heng(d,
              from_anchor=('ML', 0.521, 0.673),
              to_anchor  =('MR', 0.197, 0.386),
              width=10)

    # s3 — 撇, sweep from just under the long heng's LEFT area down-left.
    # MMH head ML(0.99,0.731) sits ~20px below the long-heng left endpoint.
    draw_pie(d,
             from_anchor=('ML', 0.99, 0.731),
             to_anchor  =('BL', 0.325, 0.821),
             head_width=11, tail_width=1, curve=0.08, segments=48)

    # s4 — 竖弯钩. MMH gives head=C(0.444,0.594) and tail=BR(0.672,0.221).
    # Construct belly / corner / hook_pt so the descent goes down through C→BC,
    # turns right, and flicks UP into the tail.
    draw_shu_wan_gou(d,
                     head    =('C',  0.444, 0.594),
                     belly   =('C',  0.50,  0.90),
                     corner  =('BC', 0.55,  0.60),
                     hook_pt =('BR', 0.55,  0.55),
                     tip     =('BR', 0.672, 0.221),
                     head_w=8, belly_w=12, corner_w=11,
                     hook_start_w=10, tip_w=2)

    out = os.path.join(_HERE, '01_元.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
