"""p3_char_0053_下 — 下 (xià, "below"), 3 strokes.

Lookup checklist (MANDATORY per memory_index):
  1. success_bank/INDEX.md grep '下' → none (new char).
  2. errata.md grep '下' → not listed.
  3. form_catalog.md — 横 spans full-width top; 竖 mid-column; 点 short diag lower-right.
  4. principles_meta.md — TR1 override anchors from MMH; TR10 N-gap ~16-20px keep visible.
  5. joint_atlas.md — s1.mid ⇆ s2.head = N (small gap OK); s2.mid ⇆ s3.head = N.
  6. sandbox.md — n/a.

Primitives reused: draw_heng, draw_shu, draw_dian (all bank).
Joints:
  s1.mid ⇆ s2.head @ TC : N (natural gap, dot-of-heng meeting vertical top)
  s2.mid ⇆ s3.head @ C  : N (dot starts near vertical, small gap)
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from dian import draw_dian

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '3 strokes (heng, shu, dian) at MMH anchors; two N-class joints.'
}


def draw_xia(draw):
    # Stroke 1 — 横 across top: ML(0.331, 0.002) → TR(0.707, 0.92)
    draw_heng(draw, ('ML', 0.331, 0.002), ('TR', 0.707, 0.92), width=9)
    # Stroke 2 — 竖 vertical: C(0.427, 0.005) → BC(0.494, 1.006)
    draw_shu(draw, ('C', 0.427, 0.005), ('BC', 0.494, 1.006), width=9)
    # Stroke 3 — 点 diagonal dot: C(0.626, 0.479) → MR(0.191, 0.896)
    draw_dian(draw, ('C', 0.626, 0.479), ('MR', 0.191, 0.896),
              head_width=2, peak_width=10, curve=0.05, segments=24)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_xia(d)
    out = os.path.join(os.path.dirname(__file__), '01_下.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
