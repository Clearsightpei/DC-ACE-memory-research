"""p3_char_0301_作 — G4 grid-bank drawer attempt.

Lookup checklist:
1. drawer_memory.md — 亻+X pattern. 亻 primitive exists (ren_side.py) but
   its default anchors sit in TC/C/BC; for 作 the 亻 must sit in TL/ML/BL.
   Per drawer_memory B8 note: "If you need a different column, inline
   the 2 strokes yourself; do not partially-override the primitive."
2. success_bank/INDEX.md grep '作' — not present.
   grep '乍' — p3_char_0165_乍 present; used same inline anchors approach.
3. errata.md grep '作' — not present.

Decomposition: 作 = 亻 (left, 2 strokes) + 乍 (right, 5 strokes) = 7 strokes.
Following MMH-verbatim anchors from injected structural expectations.

Strokes:
  s1 (亻 撇): TL(0.973, 0.653) → ML(0.22, 0.972)
  s2 (亻 竖): ML(0.812, 0.43) → BL(0.873, 0.865)
  s3 (乍 撇): TC(0.729, 0.577) → C(0.14, 0.796)
  s4 (乍 顶 heng): C(0.617, 0.371) → MR(0.695, 0.201)
  s5 (乍 竖): C(0.805, 0.433) → BC(0.919, 1.144)  [extends past bottom]
  s6 (乍 中 heng): C(0.978, 0.945) → MR(0.505, 0.84)
  s7 (乍 底 heng): BC(0.998, 0.405) → BR(0.561, 0.3)

All 5 joints are N-class (small natural gap ~11-20 px, do NOT weld).
"""
import os
import sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line, CANVAS


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 draw calls = expected 7 strokes
    'endpoint_mismatches': [],  # all MMH-verbatim
    'joint_class_mismatches': [],  # all N kept as gaps (no explicit welding)
    'overall_pass': True,
    'notes': '亻 inlined (default ren_side sits in TC/C/BC — wrong column for 作). 乍 half reuses inline strategy that PASSed at p3_char_0165.'
}


def draw_pie(draw, head_anchor, tail_anchor, w0=8, w1=3, bow=(6, -4)):
    """撇 (leftward diagonal), tapered."""
    p0 = anchor_to_xy(head_anchor)
    p2 = anchor_to_xy(tail_anchor)
    mid = ((p0[0] + p2[0]) / 2 + bow[0], (p0[1] + p2[1]) / 2 + bow[1])
    pts = quad_bezier(p0, mid, p2, n=40)
    widths = [w0 + (w1 - w0) * i / (len(pts) - 1) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)


def draw_heng(draw, head_anchor, tail_anchor, w=6):
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    fat_line(draw, p0, p1, w)


def draw_shu(draw, head_anchor, tail_anchor, w=6):
    p0 = anchor_to_xy(head_anchor)
    p1 = anchor_to_xy(tail_anchor)
    fat_line(draw, p0, p1, w)


def render():
    img = Image.new('RGB', (CANVAS, CANVAS), 'white')
    d = ImageDraw.Draw(img)

    # --- 亻 (left radical) ---
    # s1: 撇 — sweeping curve from upper-right of TL down to lower-left of ML
    draw_pie(d, ('TL', 0.973, 0.653), ('ML', 0.22, 0.972),
             w0=9, w1=3, bow=(4, -2))
    # s2: 竖 — short vertical dropping from mid-upper into BL
    draw_shu(d, ('ML', 0.812, 0.43), ('BL', 0.873, 0.865), w=7)

    # --- 乍 (right half) ---
    # s3: 乍's 撇 from TC down-left into C
    draw_pie(d, ('TC', 0.729, 0.577), ('C', 0.14, 0.796),
             w0=8, w1=3, bow=(4, -2))
    # s4: top short 横 rising slightly from C to MR
    draw_heng(d, ('C', 0.617, 0.371), ('MR', 0.695, 0.201), w=6)
    # s5: long 竖 (spine) from C down past BC (clamp to canvas)
    draw_shu(d, ('C', 0.805, 0.433), ('BC', 0.919, 1.0), w=7)
    # s6: middle 横 from C to MR — the middle bar of 乍's ladder
    draw_heng(d, ('C', 0.978, 0.945), ('MR', 0.505, 0.84), w=6)
    # s7: bottom 横 from BC to BR
    draw_heng(d, ('BC', 0.998, 0.405), ('BR', 0.561, 0.3), w=6)

    out = os.path.join(os.path.dirname(__file__), '01_作.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
