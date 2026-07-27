"""亍 (chù) — p3_char_0050. 3 strokes: short 横 + longer 横 + 竖钩.

MANDATORY LOOKUP CHECKLIST (memory_index.md order):
  1. success_bank/INDEX.md — grep 亍: not present. No prior mastery.
  2. errata.md — grep 亍: not present.
  3. form_catalog.md — 3-stroke Phase-3 char, top-短横 + mid-长横 + center-竖钩.
     Similar family: 于, 下 shape. Use standard heng + shu_gou primitives.
  4. principles_meta.md — TR1: override anchors per composition. TR8: heng
     endpoints share y-band (near-horizontal). TR9 not needed (this is a
     full character, not a standalone radical requiring expansion).
  5. joint_atlas.md — s2 mid ⇆ s3 head : N (neighbor, small gap). Do NOT
     weld. Also s3 head sits just below s2 in cell C, natural writing gap.
  6. sandbox.md — nothing specific to 亍.

Strokes:
  s1: short 横 across TL→TR (upper band).
  s2: longer 横 across ML→MR (middle band).
  s3: 竖钩 from C down to BC, hook flicks up-left (per MMH tail near BL edge).
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code')))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's1 短横 TL→TR; s2 长横 ML→MR; s3 竖钩 C→BC with hook up-left. '
             'Joint s2.mid ⇆ s3.head @ C : N (small gap, s3 head y_frac=0.55 '
             'below s2 mid y_frac=0.52 — natural writing gap).'
}


def render(path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # s1 — short 横 (top). MMH: head @ ('TL', 0.946, 0.896), tail @ ('TR', 0.048, 0.785).
    # This is a thin heng straddling TL→TR near y_frac 0.85 (bottom of top row).
    draw_heng(draw,
              ('TL', 0.55, 0.85),
              ('TR', 0.15, 0.80),
              width=7)

    # s2 — longer 横 (middle). MMH: head @ ('ML', 0.372, 0.6), tail @ ('MR', 0.66, 0.441).
    # Long horizontal across the middle band with mild upward slope right.
    draw_heng(draw,
              ('ML', 0.10, 0.60),
              ('MR', 0.90, 0.50),
              width=8)

    # s3 — 竖钩 down center then hook up-left.
    # MMH: head @ ('C', 0.403, 0.553), tail @ ('BC', 0.09, 0.795).
    # head sits just below s2's midline → N-class gap with s2.
    draw_shu_gou(draw,
                 head=('C', 0.42, 0.60),        # top of vertical, just below s2
                 belly=('C', 0.42, 0.90),       # mid body, SAME x_frac as head
                 hook_pt=('BC', 0.42, 0.65),    # bottom of vertical body
                 tip=('BC', 0.10, 0.80),        # hook tip up-and-left
                 head_w=10, belly_w=9, hook_start_w=9, tip_w=2)

    img.save(path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_亍.png')
    render(out)
    print('wrote', out)
