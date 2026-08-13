"""p3_char_0515_原 — G5 attempt.

# BANK_DEVIATION
# skipped: chang_cliff.py (厂), bai_white.py (白), xiao.py (小)
# reason: Native chang_cliff heng spans x=97..243 (width 146); target
#   厂 in 原 must span roughly x=60..285 (width ~225) to enclose the
#   full 白+小 stack inside. Native bai_white aspect is tall (150x223,
#   ratio 0.67); target 白 in 原 sits in ~120x90 box (aspect 1.33) —
#   quantitative aspect mismatch >2x, so uniform-scale bank call would
#   over-tall or over-narrow. Native xiao aspect is 1.08 (208x193);
#   target 小 in 原 sits in ~170x110 (aspect 1.55) — again quantitative
#   aspect mismatch. Per P-A-007-v2 clause: aspect deviation >20% is
#   NOT a uniform shift — inline via stroke-primitive layer (P-A-006).
# fresh_component: yuan_source_inline (厂-wrap + inline 白 + inline 小)
# quant math:
#   厂 heng: target 225 / native 146 = 1.54× scale would need — refused,
#     since bank pie also scales, going off-canvas.
#   白 aspect: target 1.33 / native 0.67 = 1.99× aspect ratio delta.
#   小 aspect: target 1.55 / native 1.08 = 1.44× aspect ratio delta.

Reasoning trace (P-A-008 mandatory):
- 原 = 厂 wrap + 白 (upper interior) + 小 (lower interior). 10 strokes.
- 厂 must span nearly full canvas width/height because it encloses two
  radicals stacked vertically. bai_white and xiao aspects don't fit
  compressed embed. Inline all three per P-A-006 stroke-primitive layer.
- MMH anchors show all 11 joint expectations are class N (neighbor gaps).
  No welded intersections — safer to underdraw than overdraw connections.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from shu_gou import draw_shu_gou
from heng_zhe_box import draw_heng_zhe_box

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,     # 2 (厂) + 5 (白) + 3 (小) = 10
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 11 joints class N — inlined w/ gaps
    'overall_pass': None,
    'notes': 'All joints class N; inlined per aspect deviation.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ─── 厂 wrap (strokes 1-2) ─────────────────────────────
    # s1: top heng — long, spans upper canvas
    draw_heng(d, (72, 52), (285, 42), width_head=8, width_tail=6)
    # s2: long left pie — sweeps from top-left down to lower-left
    # Inline as bowed pie (chang_cliff's bezier), scale customized
    draw_pie(d, (68, 46), (30, 285), bow_perp=16,
             w_head=10, w_tail=3, steps=100)

    # ─── 白 interior upper (strokes 3-7) ───────────────────
    # Compressed 白: fits inside ~x=95..215, y=72..165
    # s3: top pie of 白 — from upper-right to mid-left
    draw_pie(d, (152, 74), (105, 122), bow_perp=6,
             w_head=7, w_tail=3, steps=60)
    # s4: left 竖 of 白 box
    draw_shu(d, (105, 100), (105, 168), width=6)
    # s5: 横折 box (top + right)
    draw_heng_zhe_box(d, (105, 100), (210, 168), width=6)
    # s6: middle heng inside box
    draw_heng(d, (110, 133), (206, 130), width_head=5, width_tail=5)
    # s7: bottom heng closing box
    draw_heng(d, (110, 166), (206, 163), width_head=6, width_tail=6)

    # ─── 小 interior lower (strokes 8-10) ──────────────────
    # Wider 小 spans below 白, x ~85..265, y ~178..288
    # s8: center 竖钩 (small hook to lower-left)
    draw_shu_gou(d, (176, 178), (150, 285), width=7,
                 hook_start_offset=32)
    # s9: left 撇 of 小
    draw_pie(d, (118, 205), (85, 265), bow_perp=5,
             w_head=8, w_tail=3, steps=60)
    # s10: right 点 of 小
    draw_dian(d, (220, 205), (263, 275),
              w_head=3, w_tail=8, bow=4, steps=48)

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(os.path.dirname(__file__), '01_原.png')
    img.save(out)
    print(f'wrote {out}')
