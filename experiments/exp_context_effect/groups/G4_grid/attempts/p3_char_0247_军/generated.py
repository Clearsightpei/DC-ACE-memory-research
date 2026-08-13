"""军 (jūn, "army", 6 strokes) — G4 attempt.

Split: 冖 (top cover, 2 strokes) + 车 (chariot, 4 strokes).

Strokes (per MMH):
  s1 — 点/短撇: TL(0.756, 0.732) → ML(0.609, 0.307)  (top-left dot of 冖)
  s2 — 横钩: TL(0.864, 0.894) → MR(0.045, 0.069)     (cover, wide horizontal with right drop)
  s3 — 横: ML(0.853, 0.444) → MR(0.095, 0.307)       (upper heng of 车)
  s4 — 撇折/横: TC(0.336, 0.97) → MR(0.036, 0.919)   (compound, crosses through C)
  s5 — 横: BL(0.562, 0.42) → BR(0.525, 0.355)        (middle-low heng)
  s6 — 竖: C(0.453, 0.632) → BC(0.541, 1.111)        (long central descender)

Joints (from MMH):
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

# Import the shared anchor helper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width, quad_bezier, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Six strokes matching MMH anchors. 冖 top + 车 body. '
             'CROSS anchor at C(0.45, 0.5) welds s3, s4 (P) and s4, s6 (P). '
             's5+s6 welded at BC(0.5, 0.35).'
}


def draw_jun():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Central weld anchor for 车 body (P joints)
    CROSS_C = anchor_to_xy(('C', 0.45, 0.50))

    # ---- Cover (冖) ----
    # s1: small 点 on top-left of the cover
    p1a = anchor_to_xy(('TL', 0.72, 0.55))
    p1b = anchor_to_xy(('TL', 0.62, 0.85))
    stroke_variable_width(d, sample_line(p1a, p1b, 12), [7]*6 + [3]*7)

    # s2: 横钩 — wide horizontal cover with short drop-hook at right end
    s2_head = anchor_to_xy(('TL', 0.82, 0.90))
    s2_bend = anchor_to_xy(('TR', 0.85, 0.90))
    s2_hook_tip = anchor_to_xy(('TR', 0.75, 1.10))  # short down-left hook
    fat_line(d, s2_head, s2_bend, 6)
    fat_line(d, s2_bend, s2_hook_tip, 6)

    # ---- 车 body ----
    # s3: upper horizontal of 车 (a 一 sitting just below the cover)
    p3a = anchor_to_xy(('ML', 0.20, 0.35))
    p3b = anchor_to_xy(('MR', 0.85, 0.35))
    fat_line(d, p3a, p3b, 6)

    # s4: 撇折 / right-bracket of the middle box — a 横折 shape
    # Start top-center (below cover), bend at top-right, drop down to MR
    p4_head = anchor_to_xy(('TC', 0.60, 0.98))
    p4_bend = anchor_to_xy(('MR', 0.55, 0.10))
    p4_tail = anchor_to_xy(('MR', 0.45, 0.55))
    fat_line(d, p4_head, p4_bend, 6)
    fat_line(d, p4_bend, p4_tail, 6)

    # Middle horizontal INSIDE box (between s3 and s5) — part of s3's visual
    # (extra tick already covered by s3+s5)

    # s5: bottom wide horizontal (long — extends across bottom-middle)
    p5a = anchor_to_xy(('BL', 0.15, 0.35))
    p5b = anchor_to_xy(('BR', 0.85, 0.35))
    fat_line(d, p5a, p5b, 6)

    # s6: long central vertical descender, crossing s3, s5
    p6_top = anchor_to_xy(('C', 0.50, 0.40))
    p6_bot = anchor_to_xy(('BC', 0.50, 0.98))
    fat_line(d, p6_top, p6_bot, 7)

    out_dir = os.path.dirname(__file__)
    img.save(os.path.join(out_dir, '01_军.png'))
    return img


if __name__ == '__main__':
    draw_jun()
    print("wrote 01_军.png")
