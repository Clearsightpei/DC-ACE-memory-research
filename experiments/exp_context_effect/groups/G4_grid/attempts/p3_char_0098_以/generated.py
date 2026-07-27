"""以 (yǐ, "with/by") — 4 strokes.

Memory lookups (mandatory checklist):
  1. success_bank/INDEX.md grep '以'  → not present.
  2. errata.md grep '以'                → not present.
  3. form_catalog.md                    → generic 撇/捺 rules apply.
  4. principles_meta.md                 → TR1 (override anchors),
     TR4 (shared anchor for joints), TR6 (inline if forced-fit),
     TR8 (row/col discipline for straight strokes).
  5. joint_atlas.md                     → N-class = small visible gap,
     T-class = tip touches body.
  6. sandbox.md                         → no 以-specific note.

Structure (per MMH-derived structural expectations):
  Left component (㠯-ish tiny left cluster):
    s1 — short 竖点 / 短撇: ML(0.586,0.236) -> C(0.43,0.646)
    s2 — 点/短撇 sweeping down-left: TC(0.295,0.981) -> C(0.579,0.239)
         (NOTE: MMH lists s2 head at TC lower edge with tail at C
          upper-left; this reads as a small 点 in the top-mid area.
          Interpreted as a short 长点 / 短竖点 anchoring the left cluster.)
  Right component (人-like):
    s3 — 撇: TR(0.109,0.841) -> BC(0.157,0.695)  [long diagonal down-left]
    s4 — 捺: BR(0.06,0.051) -> BR(0.581,0.666)   [short down-right,
         starting at mid of s3 → N-joint at BR corner cell]

Joints (from MMH):
  s3.mid(t≈0.54) ⇆ s4.head @ BR  →  N (small ~15 px gap; DO NOT weld)
"""

SELF_CHECK = {
    'visual_ok': True,             # rough silhouette matches GT: left mini-cluster + right 撇/捺
    'stroke_count_ok': True,       # 4 primitive calls
    'endpoint_mismatches': [],     # anchors used verbatim from MMH
    'joint_class_mismatches': [],  # s3.mid ⇆ s4.head kept as N-gap (no weld)
    'overall_pass': True,
    'notes': (
        'Revised once: s1 upgraded from thin 点 to a 竖点-style fuller '
        'body; s3 curve increased 0.10->0.14 to better match GT 撇 arc. '
        'Left cluster still reads a bit spread; right 人-half OK.'
    ),
}

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from pie import draw_pie
from na import draw_na
from dian import draw_dian


def draw_yi_with(draw):
    # --- Left cluster (小-like V shape) ---
    # s1 — short 竖 / 竖点: descends from upper-left area down into center.
    #      MMH head ML(0.586,0.236) -> tail C(0.43,0.646).
    #      Rendered as a fuller-bodied descending 竖点 (like 亅 without hook).
    s1_head = ('ML', 0.586, 0.236)
    s1_tail = ('C',  0.43,  0.646)
    draw_pie(draw, s1_head, s1_tail,
             head_width=10, tail_width=3, curve=0.05, segments=32)

    # s2 — 点: small dot at top-mid tilted down-right (top of left cluster).
    #      MMH head TC(0.295,0.981) -> tail C(0.579,0.239).
    s2_head = ('TC', 0.295, 0.981)
    s2_tail = ('C',  0.579, 0.239)
    draw_dian(draw, s2_head, s2_tail,
              head_width=3, peak_width=11, curve=0.08, segments=32)

    # --- Right cluster (人-like, 撇 + 捺 with N-joint at s3.mid ⇆ s4.head) ---
    # s3 — long 撇 sweeping from upper-right down-left to bottom-center.
    #      Add stronger curve to match GT's arcing 撇.
    s3_head = ('TR', 0.109, 0.841)
    s3_tail = ('BC', 0.157, 0.695)
    draw_pie(draw, s3_head, s3_tail,
             head_width=12, tail_width=1, curve=0.14, segments=48)

    # s4 — 捺 emerging near mid of s3, sweeping down-right into BR.
    #      MMH head BR(0.06,0.051), tail BR(0.581,0.666).
    #      N-joint: keep visible ~15 px gap between s4.head and s3.body.
    s4_head = ('BR', 0.06,  0.051)
    s4_tail = ('BR', 0.581, 0.666)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10, segments=48)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_yi_with(d)
    out = os.path.join(os.path.dirname(__file__), '01_以.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
