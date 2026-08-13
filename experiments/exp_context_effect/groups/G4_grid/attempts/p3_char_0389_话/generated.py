"""话 (huà) — 8 strokes.

Decomposition: 话 = 讠 (left, 2 strokes) + 舌 (right, 6 strokes)
               舌 = 千 (top 3: 丿 一 丨) + 口 (bottom 3)

Following B9/B10 A-recipe:
 - MMH-verbatim anchors from dispatcher (all 8 endpoint pairs used literally).
 - Base primitives only (_anchor + fat_line); no compound override.
 - Compound strokes (s2 讠's 横折提; s7 口's 横折) rendered as two segments
   sharing an elbow — MMH gives only head/tail, elbow is inferred at the
   corner cell.
 - N-joint discipline: 7 declared N-joints preserved as natural gaps;
   the single P-joint (s4.mid ⇆ s5.mid @ C cell 0.856, 0.652) welded
   by having the strokes physically cross.

Reading order: drawer_memory (top) → INDEX grep (讠 mastered as
yan_speech, 舌 not mastered) → errata grep (话 not listed). Deferring
to base-primitive inline path per B10 A-recipe point 4.
"""
# BANK_DEVIATION
# skipped: yan_speech.py
# reason: yan_speech defaults place 讠 across cells ML/C/BL/BC; MMH here
#   compresses 讠 into the far-left column (x≈22–124 px). Compound
#   primitive would need 3+ anchor overrides — inline base primitives
#   preserve MMH placement exactly.
# fresh_component: yan_speech_far_left_column
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))
from _anchor import anchor_to_xy, fat_line  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 8 logical strokes (s2 and s7 compound: elbow within one stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim; 7 N-joints preserved as gaps; s4×s5 P-cross welded by crossing lines.',
}


def draw_hua(draw, w=8):
    # ============ 讠 (left radical, 2 strokes) ============
    # s1: 点 (dian, upper-left tick)
    s1_head = anchor_to_xy(('TL', 0.803, 0.683))   # (80.3, 68.3)
    s1_tail = anchor_to_xy(('TC', 0.175, 0.996))   # (117.5, 99.6)
    fat_line(draw, s1_head, s1_tail, w)

    # s2: 横折提 compound — MMH head @ ML(0.22, 0.664) → tail @ BC(0.242, 0.241).
    # Route: heng right → zhe down → ti up-right. Two elbows inferred.
    s2_head = anchor_to_xy(('ML', 0.22, 0.664))    # (22, 166.4)
    s2_tail = anchor_to_xy(('BC', 0.242, 0.241))   # (124.2, 224.1)
    # heng corner: rightward horizontal segment ends near x=88 at y=166.
    s2_corner_top = (88.0, s2_head[1])             # (88, 166.4)
    # zhe elbow: vertical segment ends near bottom at y=222.
    s2_corner_bot = (s2_corner_top[0] - 4.0, 222.0)  # (84, 222)
    fat_line(draw, s2_head, s2_corner_top, w)      # heng
    fat_line(draw, s2_corner_top, s2_corner_bot, w)  # zhe (down)
    fat_line(draw, s2_corner_bot, s2_tail, w)      # ti (up-right)

    # ============ 舌 (right, 6 strokes) ============
    # s3: 丿 (pie) — from upper-right of 千 down-left to center
    s3_head = anchor_to_xy(('TR', 0.288, 0.923))   # (228.8, 92.3)
    s3_tail = anchor_to_xy(('C',  0.383, 0.28))    # (138.3, 128.0)
    fat_line(draw, s3_head, s3_tail, w)

    # s4: 一 (long heng, top of 千, extends across right half)
    s4_head = anchor_to_xy(('C',  0.178, 0.746))   # (117.8, 174.6)
    s4_tail = anchor_to_xy(('MR', 0.713, 0.597))   # (271.3, 159.7)
    fat_line(draw, s4_head, s4_tail, w)

    # s5: 丨 (shu, vertical stem of 千 extending down through the heng)
    # Note: MMH endpoints are both in C/BC around x≈175. The stroke should
    # physically span from the top of 千 (above the heng) down to 口's top.
    # MMH head y=119 is above s4 (y≈166–174), tail y=216 is below → P-cross
    # with s4 is preserved by construction.
    s5_head = anchor_to_xy(('C',  0.749, 0.192))   # (174.9, 119.2)
    s5_tail = anchor_to_xy(('BC', 0.758, 0.165))   # (175.8, 216.5)
    fat_line(draw, s5_head, s5_tail, w)

    # ============ 口 (bottom of 舌, 3 strokes) ============
    # s6: 左竖 (left vertical of 口)
    s6_head = anchor_to_xy(('BC', 0.351, 0.221))   # (135.1, 222.1)
    s6_tail = anchor_to_xy(('BC', 0.57,  0.883))   # (157.0, 288.3)
    fat_line(draw, s6_head, s6_tail, w)

    # s7: 横折 (top heng + right shu of 口) — compound; corner near TR.
    s7_head = anchor_to_xy(('BC', 0.518, 0.229))   # (151.8, 222.9)
    s7_tail = anchor_to_xy(('BR', 0.177, 0.587))   # (217.7, 258.7)
    s7_corner = (s7_tail[0], s7_head[1])           # (217.7, 222.9)
    fat_line(draw, s7_head, s7_corner, w)          # top heng
    fat_line(draw, s7_corner, s7_tail, w)          # right shu

    # s8: 底一 (bottom horizontal of 口)
    s8_head = anchor_to_xy(('BC', 0.626, 0.783))   # (162.6, 278.3)
    s8_tail = anchor_to_xy(('BR', 0.385, 0.704))   # (238.5, 270.4)
    fat_line(draw, s8_head, s8_tail, w)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_hua(d, w=8)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_话.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
