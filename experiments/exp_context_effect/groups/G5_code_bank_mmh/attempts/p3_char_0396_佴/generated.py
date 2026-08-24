"""p3_char_0396_佴 — G5 attempt.

Decomposition: 亻 (2 strokes: pie + shu) + 耳 (6 strokes:
top-heng, left-shu, right-shu-extending-below-bottom, upper mid-heng,
lower mid-heng, long bottom heng crossing through).

Total: 8 strokes — matches MMH block.

BANK DEVIATION reasoning (P-A-009 quantitative):
 - 亻 (dong_person.py pie+shu piece): reused verbatim from dan_but s1-s2
   as inline calls to draw_pie/draw_shu — pie is a good fit
   for a left-占 亻 (native aspect matches). Keep inline (no BANK_DEVIATION
   block needed; pie+shu ARE bank primitives).
 - 耳 (right radical, 6 strokes): NO bank entry for whole 耳 yet.
   Inline from strokes: 5 hengs + 2 shus. The distinguishing feature of
   佴's 耳 is the RIGHT shu extending well below the canvas bottom and
   the long bottom heng that spans past both sides — GT shows this
   clearly. Native aspect of 耳 target column ≈ 150w × 260h (0.58);
   this matches inline rendering scale=1.0 in a 150w column. No
   whole-radical primitive to compare against, so no BANK_DEVIATION
   block strictly required (P-A-006 stroke-primitive layer route).

Structural self-check dict below.
"""

SELF_CHECK = {
    'visual_ok': None,  # filled after render
    'stroke_count_ok': True,  # 8 strokes rendered
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'P-A-006 stroke-primitive layer route; no whole-radical bank for 耳.'
}

import os
import sys
from PIL import Image, ImageDraw

# Bank imports
BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from heng import draw_heng  # noqa
from pie import draw_pie  # noqa
from shu import draw_shu  # noqa


def render(out_path):
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # ===== 亻 (person radical, left side) =====
    # s1: pie of 亻 (top-right down to mid-left)
    draw_pie(d, (91, 61), (18, 195), bow_perp=13, w_head=9, w_tail=3, steps=90)
    # s2: shu of 亻 (long vertical)
    draw_shu(d, (76, 141), (76, 289), width=7)

    # ===== 耳 (ear radical, right side, 6 strokes) =====
    # Column occupies roughly x=125..270, y=95..260.
    # MMH stroke order for 耳: 横 竖 竖 横 横 横
    # But the MMH block for 佴 shows s3=long vertical, s4=short heng near top,
    # s5=very long right shu extending past bottom, s6=mid heng, s7=mid heng, s8=long bottom heng.

    # s3: 耳 left shu (long, from top-left of ear down to just above bottom heng)
    draw_shu(d, (140, 100), (152, 240), width=7, top_curl=False)

    # s4: 耳 top short heng (small top piece connecting)
    draw_heng(d, (140, 105), (245, 100), width_head=8, width_tail=8)

    # s5: 耳 right shu (very long — extends past bottom of canvas)
    draw_shu(d, (245, 95), (263, 300), width=7, top_curl=False)

    # s6: 耳 upper middle heng
    draw_heng(d, (152, 152), (238, 148), width_head=7, width_tail=8)

    # s7: 耳 lower middle heng
    draw_heng(d, (152, 200), (238, 196), width_head=7, width_tail=8)

    # s8: 耳 long bottom heng (crosses through, spans left of left-shu to right of right-shu)
    draw_heng(d, (108, 245), (287, 240), width_head=9, width_tail=10)

    img.save(out_path)


if __name__ == "__main__":
    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0396_佴/01_佴.png"
    render(out)
    print("wrote", out)
