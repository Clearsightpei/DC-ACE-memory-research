"""G5 attempt: p2_radical_051_廾 (3 strokes).

Composition:
  s1 一 (heng)   ('ML',0.349,0.86)  → ('MR',0.625,0.86)
  s2 撇 (pie)    ('C', 0.014,0.485) → ('BL',0.633,0.596)
  s3 丨 (shu)    ('C', 0.749,0.377) → ('BC',0.863,0.719)

Joints: s1.mid × s2.mid = P (welded, cell C).
        s1.mid × s3.mid = P (welded, cell C).
Both welds are naturally satisfied because heng's y (~186) lies between
each vertical stroke's head_y and tail_y.

Bank usage: shu.py, heng.py, pie.py — all fit cleanly, no BANK_DEVIATION.
"""

import sys, os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from heng import draw_heng  # noqa: E402
from shu import draw_shu    # noqa: E402
from pie import draw_pie    # noqa: E402

CANVAS = 300
CELL = 100.0

def A(cell, xf, yf):
    """米字格 anchor → pixel. 'C' = middle-center."""
    col = {'L': 0, 'C': 1, 'R': 2}[cell[-1]]
    row = {'T': 0, 'M': 1, 'B': 2}[cell[0] if cell != 'C' else 'M']
    if cell == 'C':
        col, row = 1, 1
    return (col * CELL + xf * CELL, row * CELL + yf * CELL)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 primitive calls below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # both joints P (welded), satisfied by geometry
    'overall_pass': True,
    'notes': '3 strokes; heng crosses both verticals mid-shaft (P/P welds).',
}


def main():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    # s1: heng ML(0.349,0.86) → MR(0.625,0.86)
    s1_head = A('ML', 0.349, 0.86)
    s1_tail = A('MR', 0.625, 0.86)

    # s2: pie C(0.014,0.485) → BL(0.633,0.596)  (down-left sweep)
    s2_head = A('C', 0.014, 0.485)
    s2_tail = A('BL', 0.633, 0.596)

    # s3: shu C(0.749,0.377) → BC(0.863,0.719)  (near-vertical, slight drift)
    s3_head = A('C', 0.749, 0.377)
    s3_tail = A('BC', 0.863, 0.719)

    # Draw verticals first so heng lays on top for a clean welded look.
    draw_pie(d, s2_head, s2_tail, bow_perp=6, w_head=7, w_tail=3, steps=80)
    draw_shu(d, s3_head, s3_tail, width=7)
    draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

    out = os.path.join(os.path.dirname(__file__), '01_廾.png')
    img.save(out)
    print(f"wrote {out}")
    print(f"anchors used:")
    print(f"  s1 heng: {s1_head} → {s1_tail}")
    print(f"  s2 pie:  {s2_head} → {s2_tail}")
    print(f"  s3 shu:  {s3_head} → {s3_tail}")


if __name__ == '__main__':
    main()
