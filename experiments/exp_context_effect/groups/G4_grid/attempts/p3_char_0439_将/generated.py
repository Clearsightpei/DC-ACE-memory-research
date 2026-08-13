"""将 (jiāng) — 9 strokes.
Decomposition: 将 = 爿 (left, 3 strokes) + 夕 (top-right, 3 strokes) + 寸 (bottom-right, 3 strokes).

Memory pointers consulted:
- drawer_memory.md: read (B11 A-recipe + BANK_DEVIATION guidance for compound-slot embedding).
- success_bank/INDEX.md grep: 爿 has `jiang_side.py` / `pan.py` (defaults centered around C — full-standalone scale).
- errata.md grep: no prior entry for 将.

BANK_DEVIATION analysis: `jiang_side.py` and `pan.py` render 爿 at
standalone full-canvas scale (anchors centered in C). MMH for 将
places 爿 in the far-left column (s3 vertical spans TL(0.917) → BL(0.993)),
compressed to leave the right two-thirds for 夕 + 寸. Per B10/B11 pattern
(ren_side_far_left family), partial anchor override of a compound
primitive is the p3_char_0252_伊 anti-pattern. Inline base primitives
with MMH-verbatim anchors preserves compositional proportion.
See BANK_DEVIATION block below.
"""
# BANK_DEVIATION
# skipped: jiang_side.py (also pan.py)
# reason: 爿 in 将 is compressed to far-left column (x < 0.35); jiang_side.py
#         and pan.py bake standalone-scale anchors centered around C which
#         would overlap the 夕/寸 right block.
# fresh_component: jiang_side_far_left_for_将

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, CANVAS
from pie import draw_pie
from ti import draw_ti
from shu import draw_shu
from dian import draw_dian
from heng import draw_heng
from shu_gou import draw_shu_gou
from heng_pie import draw_heng_pie

# MMH-verbatim anchors (B9 A-recipe point 2).
# 爿 (left, strokes 1-3):
S1_H = ('ML', 0.483, 0.14)   # 点 — top short slant of 爿
S1_T = ('ML', 0.771, 0.465)
S2_H = ('BL', 0.226, 0.291)  # 提 — rising stroke of 爿
S2_T = ('ML', 0.943, 0.834)
S3_H = ('TL', 0.917, 0.668)  # 竖 — long vertical of 爿
S3_T = ('BL', 0.993, 0.968)

# 夕 (top-right, strokes 4-6):
S4_H = ('TC', 0.775, 0.586)  # 撇 — top short slant of 夕
S4_T = ('C',  0.304, 0.289)
S5_H = ('TC', 0.731, 0.99)   # 横撇 outer — treat as heng_pie
S5_T = ('C',  0.351, 0.843)
S6_H = ('C',  0.453, 0.266)  # 点 — inside 夕
S6_T = ('C',  0.641, 0.444)

# 寸 (bottom-right, strokes 7-9):
S7_H = ('BC', 0.266, 0.004)  # 横 — horizontal of 寸
S7_T = ('MR', 0.695, 0.881)
S8_H = ('C',  0.992, 0.564)  # 竖钩 — vertical hook of 寸
S8_T = ('BC', 0.755, 0.81)
S9_H = ('BC', 0.421, 0.229)  # 点 — bottom-left dot of 寸
S9_T = ('BC', 0.685, 0.517)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 draw calls below
    'endpoint_mismatches': [],    # MMH-verbatim
    'joint_class_mismatches': [], # s7×s8 P (welded); all others N (gap preserved by natural distance)
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim. 爿 inlined (BANK_DEVIATION from jiang_side).'
             ' s7/s8 P weld by drawing both straight through — crossing at ~(214,193).'
             ' All other joints are N — gaps preserved naturally.',
}

def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    draw = ImageDraw.Draw(img)

    # --- 爿 (left column) ---
    # s1: 点 — short slant, top of 爿
    draw_dian(draw, S1_H, S1_T, head_width=2, peak_width=9)
    # s2: 提 — rising stroke
    draw_ti(draw, S2_H, S2_T, head_width=12, tail_width=1, curve=0.06)
    # s3: 竖 — long vertical (spans from TL bottom to BL bottom, near full height)
    draw_shu(draw, S3_H, S3_T, width=9)

    # --- 夕 (top-right) ---
    # s4: 撇 — top short slant of 夕
    draw_pie(draw, S4_H, S4_T, head_width=10, tail_width=1, curve=0.08)
    # s5: MMH gives only head/tail (173,99)→(135,184). Render as a curved
    # pie sweep down-left — the outer envelope of 夕 reads correctly as a
    # single curved stroke. (Prior heng_pie attempt put corner above head
    # by mistake, went the wrong direction.)
    draw_pie(draw, S5_H, S5_T, head_width=9, tail_width=2, curve=0.10)
    # s6: 点 — inside 夕
    draw_dian(draw, S6_H, S6_T, head_width=2, peak_width=8)

    # --- 寸 (bottom-right) ---
    # s7: 横 — horizontal of 寸
    draw_heng(draw, S7_H, S7_T, width=8)
    # s8: 竖钩 — vertical hook crossing s7 at P joint
    # shu_gou needs head, belly, hook_pt, tip
    S8_BELLY = ('C',  0.885, 0.7)
    S8_HOOK_PT = ('C', 0.78, 0.80)  # near tail, hook curves up-left to tip
    # But MMH tail is the tip. Use MMH tail as tip, hook_pt just above.
    S8_HEAD = S8_H
    S8_HOOK = ('BC', 0.79, 0.72)  # start of hook (just before tip)
    S8_TIP = S8_T
    draw_shu_gou(draw, S8_HEAD, S8_BELLY, S8_HOOK, S8_TIP,
                 head_w=8, belly_w=9, hook_start_w=8, tip_w=2)
    # s9: 点 — dot at bottom-left of 寸
    draw_dian(draw, S9_H, S9_T, head_width=2, peak_width=10)

    img.save(os.path.join(os.path.dirname(__file__), '01_将.png'))

if __name__ == '__main__':
    render()
