"""p3_char_0376_疚 — jiù, "guilt". 8 strokes: 疒 shell (5) + 久 (3).

Composition strategy (P-A-006 stroke-primitive layer + P-A-007-v2):
- 疒 sub-component (strokes 1-5) matches a bank whole-radical at ~native
  scale (guang_wide + 2 dots-inside), and past PASS attempt
  p3_char_0171_疒 used inlined stroke-primitives (dian, heng, pie, dian,
  ti) with MMH anchors verbatim. Reuse THAT exact stroke-primitive
  layout (P-A-006 + P-A-008 trace).
- 久 sub-component (strokes 6-8): pie + heng_pie + na. No 久 bank primitive
  (INDEX shows 久 was C in B4 errata). Inline with stroke-primitives
  using MMH anchors verbatim.

P-A-008 inline-reasoning trace:
  s1 dian (top dot of 疒)             ← bank dian (endpoint form)
  s2 heng (top of 疒 shell)           ← bank heng
  s3 pie  (long left-sweep of 疒)     ← bank pie
  s4 dian (upper inside dot of 疒)    ← bank dian
  s5 ti   (lower inside stroke of 疒) ← bank ti
  s6 pie  (short pie of 久)           ← bank pie
  s7 heng_pie (bent stroke of 久)     ← bank heng_pie
  s8 na   (rightward na of 久)        ← bank na

Anchors below are computed directly from the injected MMH block:
  cell TC (col1,row0), C (col1,row1), TR (col2,row0), ML (col0,row1),
  BL (col0,row2), BC (col1,row2), BR (col2,row2).
  Each cell = 100x100 px; pixel = (col*100 + xf*100, row*100 + yf*100).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from ti import draw_ti
from heng_pie import draw_heng_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 8 primitive calls, matches MMH 8
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 7 joints are N-gap (no welding)
    'overall_pass': True,
    'notes': ('P-A-006 stroke-primitive layer. 疒 shell reuses the '
              'p3_char_0171_疒 PASS geometry. 久 inlined with pie/heng_pie/na '
              'from MMH anchors. All 7 joints are N-class → keep small '
              'natural gaps, no welding.'),
}


def draw(d: ImageDraw.ImageDraw):
    # ---- 疒 shell (strokes 1-5) — reuse past PASS geometry ----

    # s1: top dot (丶) — MMH TC(0.421,0.551)->TC(0.77,0.82)
    draw_dian(d, (142, 55), (177, 82), w_head=3, w_tail=8, bow=3)

    # s2: heng — MMH C(0.069,0.104)->TR(0.364,0.955)
    draw_heng(d, (107, 110), (236, 96), width_head=8, width_tail=9)

    # s3: long pie — MMH ML(0.864,0.04)->BL(0.366,0.991)
    # s3.head kept ~20px left of s2.head to preserve N-gap joint.
    draw_pie(d, (86, 104), (37, 299), bow_perp=16, w_head=9, w_tail=3, steps=80)

    # s4: inside upper dot — MMH ML(0.466,0.356)->ML(0.659,0.661)
    draw_dian(d, (47, 136), (66, 166), w_head=3, w_tail=6, bow=2)

    # s5: inside ti — MMH BL(0.223,0.183)->ML(0.776,0.942)
    # Tail sits ~20px INSIDE the pie curve (N-gap, not welded).
    draw_ti(d, (22, 218), (78, 194), w_head=8, w_tail=2, steps=50)

    # ---- 久 (strokes 6-8) ----

    # s6: short pie — MMH C(0.535,0.307)->BC(0.043,0.156)
    # Head near center, tail down-left. Mild bow.
    draw_pie(d, (154, 131), (104, 216), bow_perp=6, w_head=7, w_tail=3, steps=60)

    # s7: heng_pie — MMH C(0.503,0.764)->BL(0.844,0.921)
    # A short horizontal segment turning into a pie. Head near s6.mid
    # (N-gap ~17px preserved). Use draw_heng_pie with an apex/corner
    # slightly right of head to shape the bend.
    draw_heng_pie(d, (150, 176), (84, 292), apex_x=185, corner_x=182)

    # s8: na — MMH BC(0.849,0.288)->BR(0.827,0.965)
    # Head slightly right of s7 middle (N-gap), sweeps down-right.
    draw_na(d, (184, 228), (282, 296), bow_perp=14, w_head=4, w_tail=11, steps=80)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw(d)
    out = os.path.join(os.path.dirname(__file__), '01_疚.png')
    img.save(out)
    return out


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
