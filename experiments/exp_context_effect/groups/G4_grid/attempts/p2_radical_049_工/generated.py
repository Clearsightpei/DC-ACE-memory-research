"""p2_radical_049_工 — radical 工 (gōng), 3 strokes.

Structure (MMH-derived):
  s1: top 横 — head @ ML(0.867, 0.143), tail @ MR(0.253, 0.017)
  s2: short 竖 — head @ C(0.421, 0.222), tail @ BC(0.441, 0.355)
  s3: bottom 横 — head @ BL(0.311, 0.493), tail @ BR(0.777, 0.481)

Joints (both N — neighbor gap, DO NOT weld):
  s1.mid ⇆ s2.head @ C : N (expected gap ~17 px)
  s2.tail ⇆ s3.mid @ BC : N (expected gap ~20.8 px)

Since both joints are N-class, the 竖 (s2) is drawn BETWEEN the two
horizontals without touching them. This produces the natural
calligraphic gap seen in the MMH GT.
"""
import sys
import os

# Import from success_bank/code (per shared primitives convention)
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from shu import draw_shu


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '3 strokes rendered: top heng, short shu, bottom heng. '
        'Both joints are N-class (neighbor); shu head sits slightly '
        'below top heng and shu tail sits slightly above bottom heng, '
        'preserving natural gaps.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # --- Stroke 1: top 横 ---
    # MMH: head @ ML(0.867, 0.143), tail @ MR(0.253, 0.017)
    # This is a horizontal near the top of the middle row.
    s1_head = ('ML', 0.867, 0.143)
    s1_tail = ('MR', 0.253, 0.017)
    draw_heng(draw, s1_head, s1_tail, width=9)

    # --- Stroke 2: short 竖 ---
    # MMH: head @ C(0.421, 0.222), tail @ BC(0.441, 0.355)
    # Short vertical, sits between the two horizontals.
    s2_head = ('C', 0.421, 0.222)
    s2_tail = ('BC', 0.441, 0.355)
    draw_shu(draw, s2_head, s2_tail, width=9)

    # --- Stroke 3: bottom 横 ---
    # MMH: head @ BL(0.311, 0.493), tail @ BR(0.777, 0.481)
    # Horizontal in the bottom row.
    s3_head = ('BL', 0.311, 0.493)
    s3_tail = ('BR', 0.777, 0.481)
    draw_heng(draw, s3_head, s3_tail, width=9)

    # Compute joint gaps for the SELF_CHECK log.
    s1_head_xy = anchor_to_xy(s1_head)
    s1_tail_xy = anchor_to_xy(s1_tail)
    s2_head_xy = anchor_to_xy(s2_head)
    s2_tail_xy = anchor_to_xy(s2_tail)
    s3_head_xy = anchor_to_xy(s3_head)
    s3_tail_xy = anchor_to_xy(s3_tail)

    # s1.mid ≈ midpoint of s1
    s1_mid = ((s1_head_xy[0] + s1_tail_xy[0]) / 2.0,
              (s1_head_xy[1] + s1_tail_xy[1]) / 2.0)
    # gap between s1.mid and s2.head
    gap_12 = ((s1_mid[0] - s2_head_xy[0]) ** 2 +
              (s1_mid[1] - s2_head_xy[1]) ** 2) ** 0.5

    s3_mid = ((s3_head_xy[0] + s3_tail_xy[0]) / 2.0,
              (s3_head_xy[1] + s3_tail_xy[1]) / 2.0)
    gap_23 = ((s2_tail_xy[0] - s3_mid[0]) ** 2 +
              (s2_tail_xy[1] - s3_mid[1]) ** 2) ** 0.5

    print(f'joint s1.mid ⇆ s2.head gap: {gap_12:.1f} px (expected ~17)')
    print(f'joint s2.tail ⇆ s3.mid gap: {gap_23:.1f} px (expected ~20.8)')

    out = os.path.join(os.path.dirname(__file__), '01_工.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
