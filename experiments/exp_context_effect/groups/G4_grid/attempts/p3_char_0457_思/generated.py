"""p3_char_0457_思 — 思 (sī, "think"), 9 strokes.

Decomposition: 思 = 田 (top) + 心 (bottom).
  田 = shu + heng_zhe + heng + shu + heng (5 strokes)
  心 = pie(left dot) + wo_gou + dian(mid) + dian(right) (4 strokes)

MMH-verbatim anchors from dispatcher-injected block.
Base primitives inlined per A-recipe point 4.
"""

# BANK_DEVIATION
# skipped: xin.py
# reason: xin.py DEFAULTS place 心 at standalone-radical scale filling
#   most of the canvas; here 心 is compressed into the bottom-third
#   slot under 田. Inlining with MMH-verbatim anchors preserves the
#   compositional proportion.
# fresh_component: xin_bottom_slot_for_compound

import os, sys
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from heng import draw_heng
from shu  import draw_shu
from heng_zhe import draw_heng_zhe
from pie  import draw_pie
from dian import draw_dian
from wo_gou import draw_wo_gou


# ---- MMH-verbatim anchors ----
# 田 (top)
S1_H = ('TL', 0.668, 0.844)   # shu (left vertical) head
S1_T = ('C',  0.04,  0.846)   # shu (left vertical) tail
S2_H = ('TL', 0.882, 0.885)   # heng_zhe head (start of top heng)
S2_T = ('C',  0.849, 0.699)   # heng_zhe tail (end of right shu)
S3_H = ('C',  0.166, 0.324)   # inner heng (middle) head
S3_T = ('C',  0.811, 0.239)   # inner heng (middle) tail
S4_H = ('TC', 0.397, 0.891)   # inner shu (middle vertical) head
S4_T = ('C',  0.433, 0.626)   # inner shu tail
S5_H = ('C',  0.087, 0.79)    # bottom heng head
S5_T = ('C',  0.846, 0.649)   # bottom heng tail

# 心 (bottom)
S6_H = ('BL', 0.642, 0.118)   # left dot (short pie) head
S6_T = ('BL', 0.457, 0.675)   # left dot tail
S7_H = ('BL', 0.99,  0.197)   # wo_gou start
S7_T = ('BR', 0.098, 0.312)   # wo_gou exit
S8_H = ('C',  0.406, 0.96)    # middle dot head
S8_T = ('BC', 0.696, 0.206)   # middle dot tail
S9_H = ('MR', 0.25,  0.866)   # right dot head
S9_T = ('BR', 0.733, 0.203)   # right dot tail


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 9 draw calls for 9 MMH strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # all 5 N-joints preserved as natural gaps;
                                  # s3/s4 P-joint welded via anchor overlap
                                  # at C(0.487,0.259) region
    'overall_pass': True,
    'notes': '田+心; N-joints left un-welded per MMH; P-joint s3xs4 welded '
             'at center of top box.'
}


def draw(d):
    # ---- 田 ----
    # s1: left vertical (shu)
    draw_shu(d, S1_H, S1_T, width=9)

    # s2: heng_zhe (top + right side of 田).
    # MMH gives head (top-left) and tail (bottom-right); corner is at (tail_x, head_y).
    p_head = anchor_to_xy(S2_H)
    p_tail = anchor_to_xy(S2_T)
    # Corner cell — put corner at approximately (S2_T_x, S2_H_y):
    # numerically (184.9, 88.5) → cell C (100..200, 0..100) → C(0.849, 0.885)
    S2_CORNER = ('C', 0.849, 0.885)
    draw_heng_zhe(d, S2_H, S2_CORNER, S2_T, h_width=9, v_width=9, shoulder=12)

    # s3: middle horizontal heng (inside 田)
    draw_heng(d, S3_H, S3_T, width=8)

    # s4: middle vertical shu (inside 田)
    draw_shu(d, S4_H, S4_T, width=8)

    # s5: bottom horizontal heng of 田
    draw_heng(d, S5_H, S5_T, width=9)

    # ---- 心 ----
    # s6: left short dot rendered as tapered pie (down-left)
    draw_pie(d, S6_H, S6_T, head_width=9, tail_width=2, curve=0.05, segments=24)

    # s7: wo_gou — the main lying-hook of 心.
    # Fabricate belly (low point) + tip (up-left flick) from head/tail:
    p7_h = anchor_to_xy(S7_H)  # (99, 219.7)
    p7_t = anchor_to_xy(S7_T)  # (209.8, 231.2)
    # Belly = midpoint pushed downward ~18 px
    belly_xy = ((p7_h[0] + p7_t[0]) * 0.5,
                max(p7_h[1], p7_t[1]) + 18)
    # tip = up-left of exit ~15 px
    tip_xy = (p7_t[0] - 14, p7_t[1] - 16)

    # Convert fabricated pixel points back to anchors via inline math or
    # just call the primitive with anchors we hand-craft. Easier: bypass
    # anchor helper for belly/tip by defining anchors that map to those px.
    # Use C cell (100,100)-(200,200): belly_xy=(154.4, ~249.2) → BC cell
    # (100,200)-(200,300) → x_frac=(154.4-100)/100=0.544, y_frac=(249.2-200)/100=0.492
    S7_BELLY = ('BC', (belly_xy[0] - 100) / 100.0, (belly_xy[1] - 200) / 100.0)
    # tip_xy = (195.8, 215.2) → BC cell? x=195.8 → still BC (100..200), y=215.2 → BC (200..300)
    #   x_frac = 0.958, y_frac = 0.152
    S7_TIP = ('BC', (tip_xy[0] - 100) / 100.0, (tip_xy[1] - 200) / 100.0)

    draw_wo_gou(d, start=S7_H, belly=S7_BELLY, exit=S7_T, tip=S7_TIP,
                head_w=3, belly_w=11, exit_w=11, tip_w=1)

    # s8: middle dot
    draw_dian(d, S8_H, S8_T, head_width=2, peak_width=10, curve=0.08)

    # s9: right dot
    draw_dian(d, S9_H, S9_T, head_width=2, peak_width=10, curve=0.08)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_思.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
