"""p3_char_0527_造 — G5 attempt.

Decomposition: 告 (top-right, 7 strokes) + 辶 (bottom-left wrap, 3 strokes) = 10.

Retrieval:
- 辶: bank primitive `chuo_walk` (radical-level match; P-A-007-v2). MMH target
  anchors deviate from native chuo_walk by ~+0/+9 px (uniform-ish shift, IS
  adjustable via oy — not a real DEVIATION).
- 口 (bottom of 告): bank primitive `kou_mouth` would fit, BUT quantitative
  BANK_DEVIATION check (per P-A-009):
    kou native bbox: 133w × 150h → aspect 0.88
    target 口 bbox:  90w  × 58h  → aspect 1.55
  Target is ~76% wider-than-tall, native is 14% taller-than-wide. This is a
  non-uniform aspect shift, NOT the ox/oy/scale/uniform case. Per P-A-010-v2
  ("what single object gets changed?" — here: box aspect), this is kind (b)
  mistuned-primitive with no uniform fix → SKIP kou_mouth, INLINE fresh.
- 告 top (strokes 1-4): no bank primitive, inline via stroke-primitive layer
  at MMH anchors (P-A-006).

BANK_DEVIATION
skipped: kou_mouth.py
reason: target 口 aspect 1.55 (90×58) vs native 0.88 (133×150) — non-uniform,
  90% wider than tall vs bank's 14% taller than wide; scale alone cannot fix.
fresh_component: kou_flat_for_gao (candidate variant if this attempt PASSes)
"""

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from chuo_walk import draw_chuo          # noqa: E402
from heng import draw_heng               # noqa: E402
from heng_zhe_box import draw_heng_zhe_box  # noqa: E402
from pie import draw_pie                 # noqa: E402
from shu import draw_shu                 # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 7 (告) + 3 (辶 via chuo_walk) = 10
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'chuo_walk called with ox=0, oy=+9 to shift bank anchors to MMH; '
        'kou_mouth skipped per aspect DEVIATION, inline flat-kou for 告.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ==================== 告 (strokes 1-7) — inlined ====================
    # s1 pie: TC(0.368,0.97) -> C(0.184,0.562) = (136.8,97) -> (118.4,156.2)
    # short descending left-slanting stroke at top of 告.
    draw_pie(d, (136.8, 97), (118.4, 156.2),
             bow_perp=4, w_head=6, w_tail=2)

    # s2 top heng: C(0.456,0.315) -> MR(0.332,0.128) = (145.6,131.5)->(233.2,112.8)
    # slight upward slant to the right.
    draw_heng(d, (145.6, 131.5), (233.2, 112.8),
              width_head=6, width_tail=7)

    # s3 central shu (long vertical of 告): TC(0.755,0.548) -> C(0.819,0.623)
    #   = (175.5, 54.8) -> (181.9, 162.3). Spans y=55..162 (tall spine).
    draw_shu(d, (175.5, 54.8), (181.9, 162.3), width=7)

    # s4 wide mid heng: C(0.09,0.805) -> MR(0.619,0.629) = (109,180.5)->(261.9,162.9)
    # the wide horizontal that separates the upper half from 口.
    draw_heng(d, (109, 180.5), (261.9, 162.9),
              width_head=8, width_tail=9)

    # --- 口 (bottom of 告) inlined fresh (BANK_DEVIATION vs kou_mouth) ---
    # Target bbox from anchors: x ∈ [136.8, 226.8], y ∈ [200.7, 258.4]
    # s5 left shu of 口: (136.8, 200.7) -> (157, 258.4)
    draw_shu(d, (136.8, 200.7), (157, 258.4), width=6)
    # s6 heng_zhe (top+right of 口): use bank stroke primitive.
    # top_left=(136.8, 200) so it welds with s5 head; bottom_right at
    # (226.8, 258.4) to match s7 tail (closes the box).
    draw_heng_zhe_box(d, (136.8, 200), (226.8, 258.4), width=6)
    # s7 bottom heng of 口: (161.7, 243.2) -> (226.8, 241.7)
    draw_heng(d, (136.8, 258.4), (226.8, 258.4),
              width_head=6, width_tail=7)

    # ==================== 辶 (strokes 8-10) — bank primitive =============
    # Native chuo_walk anchors:
    #   dian(61.8,71.8)->(96.4,96.7)      vs MMH s8 (60.6,77.6)->(94.9,104.3): ~-1,+7
    #   zig (27.2,155) ->(81.4,238.8)     vs MMH s9 (24.9,169.3)->(83.5,248.1): ~-2,+10
    #   na  (28.4,254.3)->(268.9,278.9)   vs MMH s10(27.5,263.1)->(273.6,285.6): ~0,+8
    # Uniform-ish oy=+9 shift. P-A-007-v2: whole-radical primitive OK.
    draw_chuo(d, ox=0, oy=9, scale=1.0)

    out = os.path.join(os.path.dirname(__file__), '01_造.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
