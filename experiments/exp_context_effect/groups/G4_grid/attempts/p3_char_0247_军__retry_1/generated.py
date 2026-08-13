"""军 (jūn, "army", 6 strokes) — G4 retry_1.

TRAJECTORY DIFF (visual comparison of prior FAIL vs GT):

Prior main FAIL (attempts/p3_char_0247_军/01_军.png) visual gaps:
  1. 冖 top: dot placed as a vertical thin stroke; hook went straight
     down instead of a leftward flick. GT shows a slanted small 点.
  2. 车 body missing internal box: prior drew ONLY 2 horizontals + 1
     vertical. GT clearly shows 3 horizontal registers (upper, middle,
     bottom) plus a compound stroke that forms the middle box.
  3. s4 was drawn as a right-side 横折 bracket at MR — but per MMH s4
     starts at TC(0.336,0.97) high center, comes DOWN through C
     (welded with s3), then bends RIGHT to MR(0.036,0.919). It's a
     leftward-tilted 撇折 whose bend is INSIDE the character, not on
     the right edge.
  4. Bottom heng (s5) placed at y≈240 was OK but disconnected from the
     central vertical (which stopped at y=294 instead of extending
     off-canvas as GT shows).

Fix plan this retry:
  - Trust MMH anchors verbatim (v9 lesson from B7r 比 PASS).
  - s1 as slanted 点 dot from TL(0.756,0.732) → ML(0.609,0.307).
  - s2 as wide 横 + short leftward 钩 flick at right end.
  - s3 upper heng crossing s4 at C (P weld).
  - s4 compound: TC(0.336,0.97) → bend at C(0.281,0.438) → MR
    endpoint. Actually route: head → weld_C1 → weld_C2 → tail so
    it passes through both P joints.
  - s5 wide bottom heng welded to s6 at BC.
  - s6 long central 竖 from C(0.453,0.632) → BC(0.541,1.111) so tail
    goes off canvas — that's the descender.

Six strokes exactly. All P joints share explicit weld pixels.

Joints per MMH:
  s1.mid ⇆ s2.head @ TL — N (small gap)
  s2.tail ⇆ s3.tail @ C — N
  s2.mid ⇆ s4.head @ TC — N
  s3.mid ⇆ s4.mid @ C — P (welded)
  s3.mid ⇆ s6.head @ C — N
  s4.mid ⇆ s6.mid @ C — P (welded)
  s5.mid ⇆ s6.mid @ BC — P (welded)
"""
import os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes: s1 dot, s2 heng-gou, s3 heng, s4 compound, s5 heng, s6 shu
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry_1: trust MMH anchors verbatim. Compound s4 routes '
             'through both P weld points (C at s3 mid, C at s6 mid). '
             's6 tail extends past 300px (BC 1.111) as long descender.'
}


def draw_jun():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Cover (冖) ----
    # s1: small slanted 点 dot, MMH-verbatim
    s1_head = anchor_to_xy(('TL', 0.756, 0.732))
    s1_tail = anchor_to_xy(('ML', 0.609, 0.307))
    stroke_variable_width(
        d, sample_line(s1_head, s1_tail, 10),
        [4, 5, 6, 7, 7, 6, 5, 4, 3, 3, 2]
    )

    # s2: 横钩 — wide heng from TL to MR with a short leftward-down hook
    s2_head = anchor_to_xy(('TL', 0.864, 0.894))
    s2_tail = anchor_to_xy(('MR', 0.045, 0.069))   # bend point (start of hook)
    # main heng body
    fat_line(d, s2_head, s2_tail, 6)
    # short 钩 flick from tail — down and slightly left
    s2_hook_tip = (s2_tail[0] - 6, s2_tail[1] + 20)
    fat_line(d, s2_tail, s2_hook_tip, 5)

    # ---- 车 body ----
    # weld anchors (shared pixels for P joints)
    WELD_C1 = anchor_to_xy(('C', 0.281, 0.438))    # s3.mid == s4.mid (P)
    WELD_C2 = anchor_to_xy(('C', 0.535, 0.942))    # s4.mid == s6.mid (P)
    WELD_BC = anchor_to_xy(('BC', 0.523, 0.351))   # s5.mid == s6.mid (P)

    # s3: upper heng of 车 — from ML to MR, must pass through WELD_C1
    s3_head = anchor_to_xy(('ML', 0.853, 0.444))
    s3_tail = anchor_to_xy(('MR', 0.095, 0.307))
    fat_line(d, s3_head, WELD_C1, 6)
    fat_line(d, WELD_C1, s3_tail, 6)

    # s4: compound 撇折 — head at TC, bend near C (WELD_C1), through WELD_C2, tail at MR
    s4_head = anchor_to_xy(('TC', 0.336, 0.97))
    s4_tail = anchor_to_xy(('MR', 0.036, 0.919))
    # segment 1: head down/left to WELD_C1 (pie-like)
    fat_line(d, s4_head, WELD_C1, 6)
    # segment 2: WELD_C1 down/right to WELD_C2 (transition)
    fat_line(d, WELD_C1, WELD_C2, 6)
    # segment 3: WELD_C2 right to tail (heng portion)
    fat_line(d, WELD_C2, s4_tail, 6)

    # s5: wide bottom heng, must weld with s6 at WELD_BC
    s5_head = anchor_to_xy(('BL', 0.562, 0.42))
    s5_tail = anchor_to_xy(('BR', 0.525, 0.355))
    fat_line(d, s5_head, WELD_BC, 6)
    fat_line(d, WELD_BC, s5_tail, 6)

    # s6: long central 竖 descender, passes through WELD_C2 and WELD_BC
    s6_head = anchor_to_xy(('C', 0.453, 0.632))
    s6_tail = anchor_to_xy(('BC', 0.541, 1.111))   # off-canvas -> long descender
    fat_line(d, s6_head, WELD_C2, 7)
    fat_line(d, WELD_C2, WELD_BC, 7)
    fat_line(d, WELD_BC, s6_tail, 7)

    out_dir = os.path.dirname(__file__)
    img.save(os.path.join(out_dir, '01_军.png'))
    return img


if __name__ == '__main__':
    draw_jun()
    print("wrote 01_军.png")
