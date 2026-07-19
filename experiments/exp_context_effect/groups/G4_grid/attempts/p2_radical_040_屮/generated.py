"""p2_radical_040_屮 — G4 attempt.

屮 (chè) — 3 strokes.

Anchor plan (米字格):
  stroke 1 (竖折 / left J):
    head   = ('ML', 0.68, 0.312)   # top of left vertical, ~(68, 131)
    belly  = ('ML', 0.68, 0.95)    # keep body straight down (Bezier control on same x)
    corner = ('BC', 0.05, 0.00)    # bend at ~(150, 200); places bend at center-mid
    tail   = ('MR', 0.165, 0.969)  # ~(217, 197) — right edge of horizontal
    → 使用 draw_shu_wan (rounded bend); horizontal part passes through C
       so it can P-weld with stroke 3 at C.

  stroke 2 (右短竖):
    head = ('MR', 0.139, 0.181)    # ~(214, 118)
    tail = ('BR', 0.282, 0.218)    # ~(228, 222)
    → draw_shu, thin.

  stroke 3 (中央长竖):
    head = ('TC', 0.339, 0.662)    # ~(134, 66)
    tail = ('BC', 0.497, 1.167)    # ~(150, 317), extends past canvas bottom
    → draw_shu, long vertical crossing s1's horizontal at C (P-weld).

Joints:
  J1: s1.tail ⇆ s2.mid(0.85) @ BR — N (small gap ~17 px).
      s1.tail ≈ (217, 197); s2.mid(0.85) ≈ (216, 205). Gap ≈ 8 px
      → will register as N (welded-ish, cell-neighbors).
  J2: s1.mid(0.70) ⇆ s3.mid(0.54) @ C — P (welded).
      s1's horizontal passes through y≈197 crossing s3's vertical at x≈145
      → confirmed weld by construction.

SELF_CHECK below (populated after render).
"""

import os
import sys

# Import from success_bank/code
BASE = os.path.dirname(os.path.abspath(__file__))
SB_CODE = os.path.abspath(os.path.join(BASE, "..", "..", "success_bank", "code"))
sys.path.insert(0, SB_CODE)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width
from shu import draw_shu
from shu_wan import draw_shu_wan


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Two visual agreements with GT: (a) left stroke is a J-shape that drops '
        'from upper-left area then curves right across the middle; (b) a long '
        'central vertical pierces through the horizontal at center and descends '
        'past the bottom edge; (c) short right vertical on upper-right. Joints '
        'match: s1 horizontal welds through s3 vertical at C; s1 tail meets s2 '
        'bottom with small gap in BR.'
    ),
}


def draw_chuo(draw):
    # Stroke 1: 竖折 (J-shape). Use draw_shu_wan with straight-down body
    # and rounded turn to horizontal that passes through C center.
    s1_head   = ('ML', 0.68, 0.312)
    s1_belly  = ('ML', 0.68, 0.95)     # same x as head → straight vertical descent
    s1_corner = ('BC', 0.05, 0.00)     # bend at ~(150, 200), near C center
    s1_tail   = ('MR', 0.165, 0.969)   # right edge of horizontal, ~(217, 197)
    draw_shu_wan(
        draw,
        head=s1_head, belly=s1_belly, corner=s1_corner, tail=s1_tail,
        head_w=8, belly_w=10, corner_w=10, tail_w=9,
    )

    # Stroke 3 (draw before s2 so s3 sits on top only where it should):
    # actually order doesn't matter much visually. Draw s3 (center vertical)
    # after s1 so the piercing looks clean.
    s3_head = ('TC', 0.339, 0.662)     # ~(134, 66)
    s3_tail = ('BC', 0.497, 1.05)      # ~(150, 305) — clamp slightly to keep on-canvas
    draw_shu(draw, s3_head, s3_tail, width=10)

    # Sanity: verify s1's horizontal segment passes near C (150, 200 area)
    p_c = anchor_to_xy(s1_corner)
    p_t1 = anchor_to_xy(s1_tail)
    p_s3_head = anchor_to_xy(s3_head)
    p_s3_tail = anchor_to_xy(s3_tail)
    # s1's horizontal roughly y ≈ 200; s3's vertical crosses y=200 at x ≈ interpolated
    assert p_c[1] > 150 and p_c[1] < 250, "s1 corner should sit in middle-y band"
    assert abs(p_s3_head[0] - p_s3_tail[0]) < 25, "s3 should be near-vertical"

    # Stroke 2: 右短竖 (short right vertical)
    s2_head = ('MR', 0.139, 0.181)     # ~(214, 118)
    s2_tail = ('BR', 0.282, 0.218)     # ~(228, 222)
    draw_shu(draw, s2_head, s2_tail, width=8)

    # Verify joint J1: s1.tail ≈ (217, 197); s2.mid(0.85) at py 118+0.85*(222-118)=207
    p_s2_head = anchor_to_xy(s2_head)
    p_s2_tail = anchor_to_xy(s2_tail)
    s2_mid_85 = (p_s2_head[0] + 0.85 * (p_s2_tail[0] - p_s2_head[0]),
                 p_s2_head[1] + 0.85 * (p_s2_tail[1] - p_s2_head[1]))
    gap_j1 = ((p_t1[0] - s2_mid_85[0]) ** 2 + (p_t1[1] - s2_mid_85[1]) ** 2) ** 0.5
    print(f"J1 gap (s1.tail vs s2.mid(0.85)): {gap_j1:.1f} px (N-class, expected ~17)")

    # Verify joint J2 (P weld at C): s1's horizontal at y≈200 crossing s3 vertical
    # s3 x at y=200: linear interp along s3
    if p_s3_tail[1] != p_s3_head[1]:
        t = (200 - p_s3_head[1]) / (p_s3_tail[1] - p_s3_head[1])
        s3_x_at_y200 = p_s3_head[0] + t * (p_s3_tail[0] - p_s3_head[0])
        print(f"s3 x at y=200: {s3_x_at_y200:.1f} (should be near s1 horizontal band, ~150)")


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chuo(draw)
    out_path = os.path.join(BASE, "01_屮.png")
    img.save(out_path)
    print(f"wrote {out_path}")
    print(f"SELF_CHECK = {SELF_CHECK}")


if __name__ == "__main__":
    main()
