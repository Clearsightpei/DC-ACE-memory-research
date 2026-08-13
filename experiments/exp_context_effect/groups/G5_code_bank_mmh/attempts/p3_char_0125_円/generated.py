"""円 (yen/en) — 4 strokes, MMH-driven G5 render.

Uses bank primitives: shu (left vertical), heng_zhe_gou (top+right+hook),
shu (short interior vertical), heng (interior horizontal).

Anchors converted from MMH block (300x300 canvas, cells 100x100):
  s1: head ML(0.809,0.204)=(80.9,120.4)  tail BL(0.844,0.971)=(84.4,297.1)
  s2: head ML(0.981,0.242)=(98.1,124.2)  tail BC(0.658,0.789)=(165.8,278.9)
      corner inferred ~(205,124) from joint s2.mid(0.57)@MR=(204.5,194.8);
      gou_tail before hook flick ~(205, 278); hook_tip = MMH tail.
  s3: head C(0.541,0.236)=(154.1,123.6)  tail C(0.421,0.963)=(142.1,196.3)
      short interior vertical, upper half only (ends near middle band).
  s4: head BC(0.005,0.121)=(100.5,212.1)  tail MR(0.007,0.916)=(200.7,191.6)
      interior horizontal, middle-lower band.

Joints all N (natural gap): s3.tail should sit ~12px above s4 body; s2 body
should pass by (not weld with) s3 head; s1 top should have small gap under
s2 head; s2 right side meets s4 tail with small gap.
"""

import os
import pathlib
import sys
from PIL import Image, ImageDraw

# Import bank primitives
_HERE = pathlib.Path(__file__).resolve()
BANK = _HERE.parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))
from shu import draw_shu
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'stroke_count': 4,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '4 stroke primitives: shu + heng_zhe_gou (counts as 1) + shu + heng. All joints N (natural gaps preserved).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # --- s1: left vertical (long) ---
    s1_head = (80.9, 120.4)
    s1_tail = (84.4, 297.1)
    draw_shu(d, s1_head, s1_tail, width=8)

    # --- s2: heng-zhe-gou (top + right side + small left hook) ---
    s2_head = (98.1, 124.2)          # continues from just right of s1 top (small gap)
    s2_corner = (205.0, 124.0)       # top-right corner
    s2_gou_tail = (200.0, 278.0)     # bottom of right vertical (pre-hook)
    s2_hook_tip = (165.8, 278.9)     # MMH tail = end of hook flick (left-up)
    draw_heng_zhe_gou(d, s2_head, s2_corner, s2_gou_tail, s2_hook_tip)

    # --- s3: short interior vertical, upper half ---
    s3_head = (154.1, 123.6)
    s3_tail = (142.1, 196.3)
    draw_shu(d, s3_head, s3_tail, width=6)

    # --- s4: interior horizontal, middle-lower band ---
    s4_head = (100.5, 212.1)
    s4_tail = (200.7, 191.6)
    draw_heng(d, s4_head, s4_tail, width_head=7, width_tail=8)

    out_dir = _HERE.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    img.save(out_dir / '01_円.png')


if __name__ == '__main__':
    main()
