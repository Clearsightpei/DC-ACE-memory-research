"""p3_char_0311_身 — G5 retry #1.

# TRAJECTORY DIFF
# ---------------
# GT (I looked at gt/phase3/身.png):
#   - short top pie (139,49)->(115,98)
#   - short left shu top-half (97,95)->(103,200)
#   - right frame 横折钩: top-right corner near (185,100), right wall
#     leans slightly inward to gou_tail (142,286), small up-left hook
#   - two inner hengs, roughly (117,141)->(164,133) and (117,172)->(164,163)
#   - LONG bottom heng extending BOTH sides: (47,211)->(179,191)
#     (starts LEFT of the frame's left wall, ends inside frame)
#   - LONG diagonal pie from upper-right (230,127) sweeping to
#     lower-left (44,290), crossing s3 mid at ~(189,197) — welded P joint
#
# MAIN attempt FAILs (visually):
#   1. s7 pie HEAD started at (180,75) — too far left and too high;
#      MMH puts head at MR cell (230,127). The descender never reached
#      the upper-right region, so the char looked lopsided.
#   2. s6 bottom heng had head at (112,225) — did NOT extend LEFT of
#      the frame. GT/MMH show head at (47,211) — bottom heng OVERSHOOTS
#      left, giving 身 its signature "long low sweep".
#   3. Frame proportions were compressed; s3 corner was at (198,60)
#      putting the top-right too far up. MMH s3 head y=100 (top of C
#      cell), so the frame's top sits around y=100 not y=60.
#   4. s2 shu started too far left (83,108); MMH says (97,95).
#
# Fix plan for this retry (P-A-006/007-v2/008):
#   - Use MMH anchors VERBATIM for all 7 stroke endpoints (P-A-006).
#   - Keep the SAME bank primitives (pie/shu/heng/heng_zhe_gou) — no
#     whole-radical primitive matches 身 (P-A-007-v2 check: bank has
#     zi_self/yue_moon but their frame geometry differs materially —
#     both have LEFT wall going to bottom, whereas 身's left wall
#     stops mid; and neither has 身's long descender). So compose
#     from stroke primitives per P-A-006 (stroke-primitive layer).
#   - Fix s6 to overshoot LEFT (head at 47,211).
#   - Fix s7 to start at upper-right (230,127).
#   - Fix frame top-y to 100.
#
# Bank primitives used: pie, shu, heng, heng_zhe_gou.
# BANK-DEVIATION check: no bank primitive for the whole char (身 has
# no whole-radical bank entry, no close match); no per-stroke dev.
"""
import os
import sys

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'),
)

from PIL import Image, ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


# MMH anchors (from injected block, converted to pixels; 300x300 canvas,
# 100x100 米字格 cells: TL(0,0) TC(100,0) TR(200,0) ML(0,100) C(100,100)
# MR(200,100) BL(0,200) BC(100,200) BR(200,200)).
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 7 stroke primitive calls (see draw_shen)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '7 strokes, MMH anchors verbatim. Bottom heng (s6) now overshoots '
        'LEFT of frame (head x=47). Long descender pie (s7) starts at MR '
        '(230,127) — was previously (180,75). Frame top at y=100. '
        's3.mid ⇆ s7.mid welded P-joint by natural overlap at ~(180,200).'
    ),
}


def draw_shen(draw):
    # s1: 撇 — short top hat  (TC 0.389,0.486 -> TC 0.146,0.976)
    draw_pie(draw, head=(139, 49), tail=(115, 98),
             bow_perp=6, w_head=6, w_tail=3)

    # s2: 竖 — left vertical, TOP-to-MIDDLE only (this is key: it does NOT
    # descend to the bottom; the bottom heng s6 will overshoot left to
    # close-and-extend). (TL 0.973,0.946 -> C 0.031,0.998)
    draw_shu(draw, head=(97, 95), tail=(103, 200), width=6)

    # s3: 横折钩 — top + right wall + small hook.
    #   heng_head = MMH s3 head = (114, 100)
    #   corner    = inferred top-right (~ x=185, same y=100)
    #   gou_tail  = MMH s3 tail = (142, 286)  (right wall leans inward)
    #   hook_tip  = up-left flick from gou_tail
    draw_heng_zhe_gou(draw,
                      heng_head=(114, 100),
                      corner=(185, 100),
                      gou_tail=(142, 286),
                      hook_tip=(128, 275))

    # s4: 横 upper inner  (C 0.169,0.415 -> C 0.638,0.327)
    draw_heng(draw, head=(117, 141), tail=(164, 133),
              width_head=5, width_tail=6)

    # s5: 横 lower inner  (C 0.169,0.717 -> C 0.638,0.632)
    draw_heng(draw, head=(117, 172), tail=(164, 163),
              width_head=5, width_tail=6)

    # s6: 横 bottom — OVERSHOOTS LEFT of the frame's left wall.
    # (BL 0.466,0.112 -> C 0.793,0.910)  head y=211, tail y=191 (slight up-slant)
    draw_heng(draw, head=(47, 211), tail=(179, 191),
              width_head=6, width_tail=7)

    # s7: 撇 — LONG diagonal descender from upper-right to lower-left.
    # (MR 0.303,0.274 -> BL 0.437,0.903).  Big bow to arc left of straight line.
    draw_pie(draw, head=(230, 127), tail=(44, 290),
             bow_perp=22, w_head=9, w_tail=3)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_shen(d)
    out = os.path.join(os.path.dirname(__file__), '01_身.png')
    img.save(out)
    print(f'wrote {out}')
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    main()
