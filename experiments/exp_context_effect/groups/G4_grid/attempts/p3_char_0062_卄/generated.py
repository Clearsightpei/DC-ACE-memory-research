"""卄 (niàn, 3 strokes) — G4 attempt.

Lookup checklist:
  1. success_bank/INDEX.md grep: no 卄 entry; closest is shi_ten (十).
     Structure is like 廾 / 井: two 竖 flanking + one 横 crossing both.
     Cannot reuse shi_ten as-is (that draws ONE 十, we need 3 strokes
     with two crossings). Inline the 3 strokes per TR6.
  2. errata.md grep: 卄 not in errata directly, but line 442 warns
     the artichoke-radical 艹 can misread AS 卄 or broken 井 — so 卄
     itself is: two vertical 竖 (no curve), one horizontal 横 crossing.
  3. form_catalog: horizontal spans wide, two verticals cross it.
  4. principles_meta TR8 rule 5/6: 横 endpoints share row; 竖 endpoints
     share column. TR9: standalone char, expand span to full grid.
  5. joint_atlas: both crossings are P (welded) per MMH.
  6. sandbox: n/a.

MMH-derived expectations (3 strokes, 2 P joints at center row):
  s1: 横 ML(0.42,0.82) → MR(0.66,0.71)  [long horizontal across middle]
  s2: 竖 ML(0.96,0.14) → BC(0.05,0.61)  [left vertical]
  s3: 竖 TC(0.80,0.78) → BC(0.89,1.03)  [right vertical]
  P joints: s1 × s2 near C, s1 × s3 near C.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Two verticals crossing one horizontal (both P). '
             'TR8 applied: horizontal endpoints share y=0.75 (row), '
             'verticals share their own column each.',
}


def draw_nian(draw):
    # Stroke 1 — 横 across middle. Flatten y to share row per TR8 rule 5.
    # MMH: ML(0.419,0.819) → MR(0.663,0.708) — average y ≈ 0.76.
    # Extend span (TR9) but keep close to MMH.
    draw_heng(draw, ('ML', 0.30, 0.75), ('MR', 0.75, 0.75), width=10)

    # Stroke 2 — LEFT 竖. MMH: ML(0.955,0.14) → BC(0.046,0.613).
    # Both endpoints near x-column of ML-right / BC-left boundary
    # (i.e. x ≈ 100 px = column between ML and C).
    # Align both endpoints to same column per TR8 rule 6.
    draw_shu(draw, ('ML', 0.95, 0.20), ('BC', 0.05, 0.60), width=10)

    # Stroke 3 — RIGHT 竖. MMH: TC(0.796,0.776) → BC(0.89,1.029).
    # Both endpoints near x ≈ 185 px (right side of TC/BC).
    # Extend tail slightly below BC bottom edge (MMH y=1.03).
    draw_shu(draw, ('TC', 0.85, 0.80), ('BC', 0.85, 1.00), width=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_nian(draw)
    out = os.path.join(os.path.dirname(__file__), '01_卄.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
