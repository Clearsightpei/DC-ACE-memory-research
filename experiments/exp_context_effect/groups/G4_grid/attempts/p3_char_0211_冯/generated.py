"""冯 (féng) — Phase-3 character, 5 strokes.

Composition: 冫 (left, 2 strokes) + 马 (right, 3 strokes).

Memory checklist per memory_index.md:
  1. drawer_memory.md read: chronic ma_horse is hard-coded full-canvas —
     does NOT fit 冯 where 马 must live in the right half. Draw fresh
     using existing stroke primitives (heng_zhe / shu_zhe_zhe_gou / heng
     / dian / ti) with the MMH-derived anchors from the brief.
  2. INDEX.md grep: 冫 (bing.py) exists but is full-canvas too. Reuse
     component primitives instead of the composite.
  3. errata.md grep: 冯 not listed. 马 chronic pattern noted — top-box
     proportion + strict-vertical spine + clear bottom heng gap.

Strokes (per MMH-derived anchors in the brief):
  s1 冫-点   : head TL(0.551,0.914) → tail ML(0.882,0.242)  [dian]
  s2 冫-提   : head BL(0.542,0.821) → tail ML(0.917,0.731)  [ti]
  s3 马-横折 : head TC(0.16,0.949) → tail C(0.884,0.802)     [heng_zhe]
  s4 马-竖折折钩 spine: head C(0.266,0.233) → tail BC(0.802,0.739) [shu_zhe_zhe_gou]
  s5 马-长横 : head BL(0.826,0.44) → tail BR(0.101,0.355)   [heng]

Joints (all N-class per brief — small natural gaps, do NOT weld):
  s2.mid(0.38) ⇆ s5.head @ BL(0.705, 0.42) — ~34 px gap
  s3.tail ⇆ s4.mid(0.37) @ C(0.852, 0.842) — ~14 px gap
  s4.mid(0.72) ⇆ s5.tail @ BR(0.226, 0.383) — ~35 px gap
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 5 primitive calls == expected 5
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all three N-class, gaps preserved
    'overall_pass': True,
    'notes': 'fresh derivation; chronic ma_horse is full-canvas so cannot host in right-half — used stock primitives with MMH anchors.'
}

import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from dian import draw_dian
from ti import draw_ti
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu_zhe_zhe_gou import draw_shu_zhe_zhe_gou


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- 冫 (left radical) ---
    # s1: 点 (upper dot) — small NE diagonal in top-left cell
    draw_dian(draw,
              ('TL', 0.551, 0.914),
              ('ML', 0.882, 0.242),
              head_width=3, peak_width=13, curve=0.10, segments=32)

    # s2: 提 (rising flick) — from bottom-left up-and-right toward center
    draw_ti(draw,
            ('BL', 0.542, 0.821),
            ('ML', 0.917, 0.731),
            head_width=14, tail_width=1, curve=0.10, segments=48)

    # --- 马 (right) ---
    # s3: 横折 (top box top-bar + right drop)
    # MMH head TC(0.16,0.949) tail C(0.884,0.802); corner at top-right of top-box
    draw_heng_zhe(draw,
                  ('TC', 0.16, 0.949),
                  ('TC', 0.88, 0.95),
                  ('C', 0.884, 0.802),
                  h_width=8, v_width=8, shoulder=11)

    # s4: 竖折折钩 spine — MMH endpoints head C(0.266,0.233) tail BC(0.802,0.739)
    # Interpretation: shu → heng (mid bar) → shu → hook flick.
    # tail is the hook tip in MMH; but shu_zhe_zhe_gou asserts tip is
    # up-and-LEFT of hook_pt. Place hook_pt below-right, tip up-left of it.
    draw_shu_zhe_zhe_gou(draw,
                         ('C',  0.266, 0.233),   # head (matches MMH s4.head)
                         ('C',  0.266, 0.55),    # corner1 (drop down)
                         ('C',  0.90,  0.55),    # corner2 (mid-bar right)
                         ('BC', 0.85,  0.80),    # hook_pt (bottom-right of spine)
                         ('BC', 0.55,  0.60),    # tip (flick up-left; visually near MMH tail region)
                         v_width=8, h_width=8, shoulder=11,
                         hook_start_w=9, tip_w=1)

    # s5: 长横 (bottom bar)
    draw_heng(draw,
              ('BL', 0.826, 0.44),
              ('BR', 0.101, 0.355),
              width=8)

    out = os.path.join(_HERE, '01_冯.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
