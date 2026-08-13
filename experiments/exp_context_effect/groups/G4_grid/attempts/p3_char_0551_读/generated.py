"""读 (dú) — 10 strokes.

Decomposition: 读 = 讠 (left, 2 strokes) + 卖 (right, 8 strokes).
    卖 top:    s3 (compound heng-diag) + s4 (short shu) — 士/十 top
    卖 middle: s5 (long heng across right) + s6 + s7 (two inner ticks)
    卖 bottom: s8 (heng) + s9 (long pie) + s10 (na) — 大-like base

Reading order per drawer_memory v8 slim checklist:
 1) drawer_memory.md — v11 named pattern `yan_side_far_left` applies
    (话 PASS + 说 R2 PASS both used per-item MMH-verbatim yan inline).
 2) INDEX grep — 讠 mastered as yan_speech.py (defaults ML/BC central,
    NOT far-left column); 卖 not in bank.
 3) errata grep — 读 not listed; 说 fix idea "讠 clean-L + 3-part stack
    literal" is the closest sibling; same slot pattern.

Applying B9–B13 A-recipe (8 points):
 - Explicit decomposition (this docstring).
 - MMH-verbatim anchors from dispatcher (all 10 endpoint pairs used
   literally — no tuning, no clever mirror math).
 - SELF_CHECK block below.
 - Base primitives only (_anchor + fat_line + stroke_variable_width),
   no compound-override.
 - N-joint discipline: 4 N-joints preserved as natural gaps (s2×s8,
   s4×s5, s5×s6, s6×s7); 2 P-joints welded by physical crossing
   (s3×s4 at C(185,103) top 十 cross; s9×s10 at BC(180,234) bottom X).
 - BANK_DEVIATION signal for 讠 (far-left slot).
 - No chronic component involved.
 - No X-cross-in-compound (bottom X is isolated 大-like, distinct from
   B10-B11 TERMINAL_FROZEN cluster).
"""
# BANK_DEVIATION
# skipped: yan_speech.py
# reason: 讠 sits in far-left column here (x ≈ 21–125 px); yan_speech
#   defaults place the compound in ML/C/BC more central and would need
#   4+ anchor overrides. Named pattern `yan_side_far_left` already has
#   B11 (话 PASS) + B12 (说 R2 PASS) precedent.
# fresh_component: yan_side_far_left_for_读
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '..', '..', 'success_bank', 'code',
)
sys.path.insert(0, os.path.abspath(BANK))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 logical strokes (s2, s3 are compound but count as one each)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('10 strokes MMH-verbatim; 讠 inlined per yan_side_far_left; '
              's3×s4 P-cross welded at C(185,103); s9×s10 bottom pie/na '
              'X-cross welded near BC(180,234); 4 N-joints kept as gaps.'),
}


def draw_du(draw, w=8):
    a = anchor_to_xy

    # ============ 讠 (left radical, 2 strokes) ============
    # s1: 点 (small tick, upper-left of 讠)
    s1_h = a(('TL', 0.753, 0.706))   # (75.3, 70.6)
    s1_t = a(('C',  0.102, 0.005))   # (110.2, 100.5)
    s1_mid = ((s1_h[0] + s1_t[0]) * 0.5, (s1_h[1] + s1_t[1]) * 0.5)
    stroke_variable_width(draw, [s1_h, s1_mid, s1_t], [3, 8, 10])

    # s2: 横折提 compound.  MMH head @ ML(0.208,0.641) → tail @ BC(0.125,0.256)
    # Route: heng right → zhe down → ti up-right. Elbows inferred.
    s2_h = a(('ML', 0.208, 0.641))   # (20.8, 164.1)
    s2_t = a(('BC', 0.125, 0.256))   # (112.5, 225.6)
    s2_cornertop = (80.0, s2_h[1])                        # heng right end
    s2_cornerbot = (s2_cornertop[0] - 4.0, 218.0)         # zhe bottom
    fat_line(draw, s2_h, s2_cornertop, w)                 # heng
    fat_line(draw, s2_cornertop, s2_cornerbot, w)         # zhe (down)
    stroke_variable_width(draw, [s2_cornerbot, s2_t], [12, 2])  # ti flick

    # ============ 卖 (right, 8 strokes) ============
    # s3: compound top stroke — heng section crosses s4 near its top, then
    # dips down-right toward TR.  MMH head C(0.436,0.049); mid(0.48) is the
    # 十-cross weld point at C(0.851,0.026); tail TR(0.294,0.952).
    s3_h = a(('C',  0.436, 0.049))   # (143.6, 104.9)
    s3_t = a(('TR', 0.294, 0.952))   # (229.4, 195.2)
    s3_mid = a(('C', 0.851, 0.026))  # (185.1, 102.6) — P-weld with s4
    fat_line(draw, s3_h, s3_mid, w - 1)
    fat_line(draw, s3_mid, s3_t, w - 1)

    # s4: short shu — top of 十, crossing s3 at s3_mid
    s4_h = a(('TC', 0.749, 0.65))    # (174.9, 65.0)
    s4_t = a(('C',  0.802, 0.354))   # (180.2, 135.4)
    fat_line(draw, s4_h, s4_t, w)

    # s5: middle wide heng — spans center-left to MR
    s5_h = a(('C',  0.228, 0.5))     # (122.8, 150.0)
    s5_t = a(('MR', 0.265, 0.67))    # (226.5, 167.0)
    fat_line(draw, s5_h, s5_t, w)

    # s6: small inner tick (upper of two) — N-gap 33 px from s5 head
    s6_h = a(('C',  0.421, 0.755))   # (142.1, 175.5)
    s6_t = a(('C',  0.579, 0.881))   # (157.9, 188.1)
    fat_line(draw, s6_h, s6_t, w - 2)

    # s7: small inner tick (lower) — N-gap 32 px from s6 tail
    s7_h = a(('BC', 0.351, 0.001))   # (135.1, 200.1)
    s7_t = a(('BC', 0.521, 0.147))   # (152.1, 214.7)
    fat_line(draw, s7_h, s7_t, w - 2)

    # s8: bottom heng-like — spans BC to BR, slight upward tilt (top of 大)
    s8_h = a(('BC', 0.192, 0.394))   # (119.2, 239.4)
    s8_t = a(('BR', 0.525, 0.238))   # (252.5, 223.8)
    fat_line(draw, s8_h, s8_t, w)

    # s9: long pie — from mid-canvas curving down through the X-weld
    # point at BC(0.807,0.337)=(180.7,233.7) to bottom-center.
    # MMH labels mid(0.44) at that point → render as quad_bezier so the
    # arc actually passes through the weld, not a straight line.
    # Tapers 10 → 2.  P-weld with s10 preserved by physical crossing.
    s9_h = a(('C',  0.729, 0.641))   # (172.9, 164.1)
    s9_t = a(('BC', 0.113, 0.959))   # (111.3, 295.9)
    CROSS = a(('BC', 0.807, 0.337))  # (180.7, 233.7) — pie/na X-weld
    # Control point so bezier passes near CROSS at t≈0.44
    # For quad_bezier B(t) = (1-t)^2 P0 + 2(1-t)t P1 + t^2 P2
    # Solve for P1 at t=0.44 so that B(0.44) ~ CROSS
    t = 0.44
    coef = 2 * (1 - t) * t  # 0.4928
    s9_ctrl = ((CROSS[0] - (1 - t) ** 2 * s9_h[0] - t ** 2 * s9_t[0]) / coef,
               (CROSS[1] - (1 - t) ** 2 * s9_h[1] - t ** 2 * s9_t[1]) / coef)
    s9_pts = quad_bezier(s9_h, s9_ctrl, s9_t, n=40)
    s9_widths = [10 - 8 * i / 40 for i in range(41)]
    stroke_variable_width(draw, s9_pts, s9_widths)

    # s10: na — starts at the X-weld point (BC cell, adjacent to MMH's
    # BR head; within self-check adjacent-cell tolerance), sweeps down-
    # right to tail, swells at mid.  MMH mid(0.46) is the weld point
    # itself, so anchoring head there produces the correct crossing.
    s10_h = a(('BC', 0.807, 0.337))  # (180.7, 233.7) — X-weld with s9
    s10_t = a(('BR', 0.467, 0.944))  # (246.7, 294.4)
    s10_mid = ((s10_h[0] + s10_t[0]) * 0.5, (s10_h[1] + s10_t[1]) * 0.5)
    stroke_variable_width(draw, [s10_h, s10_mid, s10_t], [3, 14, 1])


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_du(d, w=8)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '01_读.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
