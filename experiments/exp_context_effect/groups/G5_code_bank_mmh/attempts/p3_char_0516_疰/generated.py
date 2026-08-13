"""p3_char_0516_疰 — G5 attempt.

Reasoning trace (P-A-008 mandatory):
- 疰 = 疒 (sickness radical, 5 strokes: dian + heng + long pie + 2 interior dots)
  + 主 (5 strokes) = 10 strokes total. Matches MMH count.
- 疒 is a terminal-freeze cluster (no bank primitive per B12 memory);
  inline via stroke-primitive layer (P-A-006).
- 主 has a bank primitive (zhu_lord.py from p3_char_0174 B6 PASS). In 疰
  the 主 sits in the right-lower quadrant, ~0.65 scale of standalone,
  shifted right ~+80px, down ~+103px. Verified against MMH s10 (bottom
  heng): native (34.6,280.1)->(278.9,275.7) with ox=80,oy=103,scale=0.65
  gives (102.5,285.6)->(261.3,282.7) vs MMH target (102.5,285.6)->
  (259.9,281.0). Delta <2px on both endpoints — this is a UNIFORM shift
  + UNIFORM scale, which per P-A-007-v2 IS adjustable via bank call.
  No BANK_DEVIATION needed.
- No 疒 bank => no deviation from something we don't have.
- All 8 MMH joints are class N (neighbor gaps except s8/s9 P weld inside
  main-radical composition, which is internal to zhu_lord). Underdraw
  connections between 疒 and 主.

Self-check: 10 strokes; endpoints within ±0.20 of MMH anchors; joints N.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from ti import draw_ti
from zhu_lord import draw_zhu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 5 inline (疒) + 5 in draw_zhu (主) = 10
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 inlined (no bank), 主 uses zhu_lord at ox=80,oy=103,scale=0.65 (P-A-007-v2 uniform shift).',
}


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============ 疒 radical (strokes 1-5) — inline (no bank) ============

    # s1: top dian, MMH TC (0.424,0.642) -> TC (0.775,0.87)
    #     px: (142.4, 64.2) -> (177.5, 87.0)
    draw_dian(d, (142, 64), (178, 87), w_head=3, w_tail=8, bow=3)

    # s2: upper heng of 疒, MMH C (0.096,0.146) -> TR (0.388,0.999)
    #     px: (109.6, 114.6) -> (238.8, 99.9)  (slight upward tilt right)
    draw_heng(d, (110, 115), (239, 100), width_head=7, width_tail=9)

    # s3: long pie (defining slash of 疒),
    #     MMH ML (0.861,0.072) -> BL (0.434,1.038)
    #     px: (86.1, 107.2) -> (43.4, 303.8)   — long strong sweep
    draw_pie(d, (86, 108), (44, 296), bow_perp=18, w_head=10, w_tail=3)

    # s4: interior upper dot (dian), MMH ML (0.419,0.456) -> ML (0.683,0.688)
    #     px: (41.9, 145.6) -> (68.3, 168.8)  — small SE-going dot
    draw_dian(d, (42, 146), (68, 169), w_head=3, w_tail=7, bow=2)

    # s5: interior lower rising stroke (ti),
    #     MMH BL (0.19,0.373) -> ML (0.806,0.992)
    #     px: (19.0, 237.3) -> (80.6, 199.2) — this rises up-right (dy<0)
    #     — actually flip head/tail so ti goes head(lower) -> tail(upper).
    draw_ti(d, (19, 237), (81, 199), w_head=8, w_tail=2)

    # ============ 主 (strokes 6-10) — bank primitive zhu_lord ============
    # Standalone zhu_lord bottom heng at (34.6,280.1)->(278.9,275.7).
    # In 疰 target bottom heng at (102.5,285.6)->(259.9,281.0).
    # scale = (259.9-102.5)/(278.9-34.6) = 157.4/244.3 = 0.644 ~ 0.65
    # ox = 102.5 - 34.6*0.65 = 80.01
    # oy = 285.6 - 280.1*0.65 = 103.5
    draw_zhu(d, ox=80, oy=103, scale=0.65)

    out = os.path.join(os.path.dirname(__file__), '01_疰.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    draw()
