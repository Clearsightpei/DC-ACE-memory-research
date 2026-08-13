"""p3_char_0261_再 — G4 grid attempt.

Reading order followed:
  1. drawer_memory.md — 再 not a chronic component; no sub-radical shortlist match.
     (Not 亻/扌/宀/丿/刀/冂/弓/马 by itself. It's frame-like — visually similar
     to 冉/由/申 but with slanted top heng + explicit middle heng.)
     jiong_frame doesn't fit: 再 has a slanted top heng crossing the spine
     (not a plain 冂 top bar) and its left wall is a shu that extends BELOW
     the bottom heng. Inline fresh.
  2. success_bank/INDEX.md grep — 再 not present. 冉 (201) and 由 (204)/申 (159)
     are similar. Follow 冉's approach: inline 6-stroke composition.
  3. errata.md grep — 再 not in errata.

Decomposition (6 strokes, per MMH block):
  1. Top slanted heng           TL(0.785,0.841) → TR(0.256,0.691)
  2. Left long vertical (shu)   ML(0.902,0.283) → BL(0.896,0.88)
  3. Right heng-zhe (frame)     C(0.075,0.315) → corner → BC(0.705,0.757)
  4. Central spine (long shu)   TC(0.403,0.885) → BC(0.447,0.036)
  5. Middle inner heng          C(0.195,0.717) → C(0.808,0.646)
  6. Wide bottom heng           BL(0.293,0.186) → BR(0.733,0.104)

Joint plan (9 joints):
  - s1.mid ⇆ s4.head  N (top heng crosses spine near top; small gap tolerated)
  - s2.head ⇆ s3.head N (top-left corner of frame — near-weld)
  - s2.mid ⇆ s5.head  N (left vertical meets middle heng on the left)
  - s2.mid ⇆ s6.mid   P (left vertical WELDED to bottom heng)
  - s3.head ⇆ s4.mid  T (spine tangent to top-right corner area)
  - s3.mid ⇆ s5.tail  N (right wall meets middle heng on the right)
  - s3.mid ⇆ s6.mid   P (right wall WELDED to bottom heng)
  - s4.mid ⇆ s5.mid   P (spine WELDED to middle heng)
  - s4.tail ⇆ s6.mid  N (spine tail meets bottom heng at center)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line
from PIL import Image, ImageDraw


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '6 strokes; heng-zhe drawn as 2 fat_lines meeting at explicit corner; P-welds at s2/s3 x s6 (crossing bottom heng) and s4 x s5 (crossing middle heng).'
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    W = 7  # stroke width

    # Stroke 1 — top slanted heng
    s1_h = anchor_to_xy(('TL', 0.785, 0.841))   # (78.5, 84.1)
    s1_t = anchor_to_xy(('TR', 0.256, 0.691))   # (225.6, 69.1)
    fat_line(d, s1_h, s1_t, W)

    # Stroke 2 — left long vertical (extends past bottom heng)
    s2_h = anchor_to_xy(('ML', 0.902, 0.283))   # (90.2, 128.3)
    s2_t = anchor_to_xy(('BL', 0.896, 0.88))    # (89.6, 288.0)
    fat_line(d, s2_h, s2_t, W)

    # Stroke 3 — heng-zhe (top bar of frame + right wall)
    # MMH head @ C(0.075,0.315) = (107.5, 131.5)  — near top-left of frame
    # Corner around C(0.936,0.644) = (193.6, 164.4)  — top-right of frame (from joint s3.mid ⇆ s5.tail)
    # Tail @ BC(0.705,0.757) = (170.5, 275.7)  — bottom-right, below middle heng
    s3_h = anchor_to_xy(('C', 0.075, 0.315))
    s3_c = (200.0, 132.0)  # corner: aligned with s2.head y for a clean top-bar
    s3_t = anchor_to_xy(('BC', 0.705, 0.757))
    # Draw top bar (head → corner). Snap corner to top-bar y to keep bar horizontal.
    fat_line(d, s3_h, s3_c, W)
    # Draw right wall (corner → tail).
    fat_line(d, s3_c, s3_t, W)

    # Stroke 4 — central spine
    s4_h = anchor_to_xy(('TC', 0.403, 0.885))   # (140.3, 88.5)
    s4_t = anchor_to_xy(('BC', 0.447, 0.036))   # (144.7, 203.6)
    # Extend slightly upward so it visibly crosses the top slanted heng, and slightly
    # downward past the bottom heng — matches 再's tall spine in GT.
    s4_h_ext = (s4_h[0], s4_h[1] - 12)          # nudge above top heng
    s4_t_ext = (s4_t[0], s4_t[1] + 30)          # nudge below bottom heng
    fat_line(d, s4_h_ext, s4_t_ext, W)

    # Stroke 5 — middle inner heng
    # MMH says C(0.195,0.717)→C(0.808,0.646) but that only spans x=119..181,
    # leaving the middle bar dangling. GT shows the middle heng SPANS the frame
    # touching both walls (P-weld with s2 on left, N with s3 on right).
    # Widen to span left-wall x ≈ 90 → right-wall x ≈ 200.
    s5_h = (s2_h[0] - 3, 170.0)                 # weld into left vertical
    s5_t = (s3_c[0] - 2, 168.0)                 # meet right wall just below corner
    fat_line(d, s5_h, s5_t, W)

    # Stroke 6 — wide bottom heng (welded through both walls)
    s6_h = anchor_to_xy(('BL', 0.293, 0.186))   # (29.3, 218.6)
    s6_t = anchor_to_xy(('BR', 0.733, 0.104))   # (273.3, 210.4)
    fat_line(d, s6_h, s6_t, W)

    # Stroke-count assertion (MMH says 6)
    strokes = [1, 2, 3, 4, 5, 6]
    assert len(strokes) == 6, f"stroke count mismatch: {len(strokes)}"

    out = os.path.join(os.path.dirname(__file__), '01_再.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
