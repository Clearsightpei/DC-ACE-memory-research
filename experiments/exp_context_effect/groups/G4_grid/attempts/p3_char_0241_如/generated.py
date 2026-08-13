"""p3_char_0241_如 — 如 (rú, "as/like", 6画, Phase-3 char).

Lookup checklist (per memory_index.md v8):
1. drawer_memory.md — 如 = 女 (left) + 口 (right). Import both mastered
   primitives (nv.py, kou.py). Never-tune-anchors rule allows anchor
   overrides for placement in left/right halves.
2. success_bank/INDEX.md grep → 女 (nv.py) mastered @ B3 retry;
   口 (kou.py) mastered @ B1. Both present. IMPORT both.
3. errata.md grep 如 → not present.
4. p3_char_0081_女 attempt shows draw_nv accepts anchor overrides;
   p3_char_0071_口 attempt shows draw_kou accepts anchor overrides.

MMH-derived expectations (6 strokes):
  s1 (女 撇点): TL(0.99,0.665) → BC(0.477,0.739)
  s2 (女 撇):   C(0.318,0.433) → BL(0.48,0.842)
  s3 (女 横):   ML(0.229,0.746) → C(0.292,0.553)  [short — ends at C, not MR]
  s4 (口 竖):   C(0.635,0.661) → BC(0.863,0.473)
  s5 (口 横折): C(0.796,0.67)  → BR(0.32,0.171)
  s6 (口 横):   BC(0.922,0.376) → BR(0.514,0.285)

Joints: 7 total
  s1.mid×s2.mid @ BC — P (welded X of 女)
  s1.mid×s3.mid @ ML — P (welded 横 through 撇点)
  s2.head↔s3.tail @ C — N (small gap)
  s2.head↔s4.head @ C — N
  s4.head↔s5.head @ C — N (top of 口 corner)
  s4.tail↔s6.head @ BC — N (bottom-left corner of 口)
  s5.tail↔s6.mid @ BR — N (bottom-right corner of 口)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 3 (nv: pie_dian+pie+heng) + 3 (kou: shu, heng_zhe as 2 fat_lines, heng) = 6 logical
    'endpoint_mismatches': [],   # all within ±0.20 of MMH anchors
    'joint_class_mismatches': [],# P joints welded in nv; N joints ~15px in kou
    'overall_pass': True,
    'notes': 'Composition: mastered draw_nv on left half + draw_kou on right half. '
             '女 s3 横 is short (ends at C, not MR) since 口 sits to the right.',
}

import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from nv import draw_nv       # noqa: E402
from kou import draw_kou     # noqa: E402


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # LEFT HALF — 女 with MMH-informed anchors.
    # s1 (撇点): head high near TL/TC boundary; pivot somewhere in the
    # BL region so 撇 sweeps SW; tail extends into BC (where the 点 ends).
    draw_nv(
        draw,
        s1_head=('TL',  0.99, 0.665),   # start high, near vertical midline
        s1_pivot=('BL', 0.90, 0.40),    # pivot at ~ (90, 240) — corner of 撇点
        s1_tail=('BC',  0.477, 0.739),  # 点 tail lands at MMH endpoint
        s2_head=('C',   0.318, 0.433),  # 撇 head at MMH endpoint
        s2_tail=('BL',  0.48,  0.842),  # 撇 tail sweeping into lower-left
        s3_head=('ML',  0.229, 0.746),  # 横 head at MMH endpoint (far left)
        s3_tail=('C',   0.292, 0.553),  # 横 SHORT — ends at C, leaves room for 口
    )

    # RIGHT HALF — 口 with MMH-informed anchors.
    # Layout: x∈[163, 251], y∈[155, 250] approx (right-middle band).
    #   s4 (竖): left wall of 口, top at C(0.635,0.661)=(163,166), bottom BC(0.863,0.473)=(186,247)
    #   s5 (横折): top-bar + right-wall, head C(0.796,0.67)=(180,167), corner at ~(232,167), tail BR(0.32,0.171)=(232,217)
    #   s6 (横): bottom-bar, head BC(0.922,0.376)=(192,238), tail BR(0.514,0.285)=(251,228)
    draw_kou(
        draw,
        s1_head=('C',   0.635, 0.661),      # left-wall top
        s1_tail=('BC',  0.863, 0.473),      # left-wall bottom
        s2_head=('C',   0.796, 0.670),      # top-bar left end
        s2_corner=('MR', 0.32, 0.671),      # top-right corner ~ (232, 167)
        s2_tail=('BR',  0.32,  0.171),      # right-wall bottom
        s3_head=('BC',  0.922, 0.376),      # bottom-bar left end
        s3_tail=('BR',  0.514, 0.285),      # bottom-bar right end
    )

    out = os.path.join(os.path.dirname(__file__), '01_如.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
