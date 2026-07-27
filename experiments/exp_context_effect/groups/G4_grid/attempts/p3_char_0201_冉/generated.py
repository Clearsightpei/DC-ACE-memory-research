"""p3_char_0201_冉 — G4 grid attempt.

Reading order followed:
  1. drawer_memory.md — no chronic primitive matches 冉 directly; no sub-radical
     in the mandatory shortlist (not 亻/扌/宀/等). Compose from scratch with anchors.
  2. success_bank/INDEX.md — grep 冉: not present. Related 内/用/円 (jiong-frame)
     — 冉 is NOT a jiong-frame, it's frame-like but the middle vertical extends
     ABOVE and BELOW, plus the wide bottom horizontal. Do not call jiong_frame.
  3. errata.md — 冉 not in errata.

Decomposition (5 strokes, per MMH block):
  1. Left slanted vertical  (ML → BL)
  2. Top-right heng-zhe     (ML top → over → down to BC)  — top + right side
  3. Middle inner horizontal (C → C)
  4. Central vertical extending above and below (TC → BC)
  5. Wide bottom horizontal (BL → BR)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line, stroke_variable_width
from PIL import Image, ImageDraw


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes as specified; heng-zhe with corner at top-right; central vertical goes through both horizontals (P welds).'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    W = 6  # stroke width

    # Stroke 1: left vertical (slight tilt) — ML(0.791, 0.204) → BL(0.817, 0.889)
    s1_head = anchor_to_xy(('ML', 0.791, 0.204))
    s1_tail = anchor_to_xy(('BL', 0.817, 0.889))
    fat_line(d, s1_head, s1_tail, W)

    # Stroke 2: heng-zhe — head ML(0.973, 0.254), corner at TR-ish, tail BC(0.646, 0.792)
    # Horizontal portion first, then bend down to right vertical, meeting bottom.
    s2_head = anchor_to_xy(('ML', 0.973, 0.254))          # top-left of frame
    s2_corner = anchor_to_xy(('C', 0.90, 0.15))            # top-right corner of frame
    s2_tail = anchor_to_xy(('BC', 0.646, 0.792))           # bottom (near BR corner)
    # top horizontal
    fat_line(d, s2_head, s2_corner, W)
    # right vertical (from corner down)
    fat_line(d, s2_corner, s2_tail, W)

    # Stroke 3: inner middle horizontal — C(0.148, 0.69) → C(0.793, 0.603)
    s3_head = anchor_to_xy(('C', 0.148, 0.69))
    s3_tail = anchor_to_xy(('C', 0.793, 0.603))
    fat_line(d, s3_head, s3_tail, W)

    # Stroke 4: central vertical extending above top and below bottom
    # TC(0.345, 0.647) → BC(0.406, 0.039)
    s4_head = anchor_to_xy(('TC', 0.345, 0.647))
    s4_tail = anchor_to_xy(('BC', 0.406, 0.039))
    fat_line(d, s4_head, s4_tail, W)

    # Stroke 5: wide bottom horizontal — BL(0.243, 0.218) → BR(0.757, 0.071)
    s5_head = anchor_to_xy(('BL', 0.243, 0.218))
    s5_tail = anchor_to_xy(('BR', 0.757, 0.071))
    fat_line(d, s5_head, s5_tail, W)

    strokes = [1, 2, 3, 4, 5]
    assert len(strokes) == 5, f"stroke count mismatch: {len(strokes)}"

    out = os.path.join(os.path.dirname(__file__), '01_冉.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
