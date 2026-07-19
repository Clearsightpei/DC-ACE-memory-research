"""歹 (dǎi, 4画 radical) — G4 grid-bank attempt.

MMH decomposition (from injected structural spec):
  s1 head TL(0.539, 0.935) tail TR(0.540, 0.847)  — top 一 (short horizontal near y=88-93)
  s2 head TC(0.336, 0.961) tail BL(0.677, 0.060)  — long 撇 sweeping down-left across the grid
  s3 head C (0.277, 0.562) tail BL(0.729, 1.064)  — interior down-left stroke (横撇-like); clamp tail y to 1.0
  s4 head C (0.113, 0.819) tail BC(0.368, 0.145)  — small 点 going down-right (tucked inside)

Joints (all N-class, expected pixel gap ~15-17 px):
  s1.mid(0.36) ⇆ s2.head @ TC (~15.6 px)
  s2.mid(0.52) ⇆ s3.head @ C  (~17.6 px)
  s2.mid(0.66) ⇆ s4.head @ C  (~16.6 px)

Anchor plan (respecting principle bank TR12: heng endpoints in same row):
  s1: both endpoints in T-row (TL, TR) ✓ — MMH-verbatim.
  s2: TC→BL, down-left 撇 spanning mid-grid ✓ — MMH-verbatim.
  s3: C→BL, another down-left sweep (steeper). Clamp BL y_frac=1.0. Draw as tapered pie.
  s4: C→BC, short 点 down-right. Head width thin, tail thick (顿笔).

TR11 self-check (two named visual agreements between my render and GT):
  (1) Top 一 sits above and slightly right of the main 撇 head (i.e. the 撇 head
      starts BELOW the top-横 and slightly left of its center).
  (2) Interior stroke and 点 are both nested inside the wedge formed by the
      top-横 and the main 撇 — none extend outside that wedge.
"""

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': False,
    'stroke_count_ok': True,
    'endpoint_mismatches': [
        {'stroke': 3, 'note': 'revised: shorter/more compact, does not parallel s2 to BL'},
        {'stroke': 4, 'note': 'revised: more compact 点, tucked in wedge'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': False,
    'notes': (
        'Revision 1: first pass had s2 and s3 both sweeping to BL as parallel 撇, '
        'making the render read as 不 not 歹. GT shows an interior compact 横撇 '
        'and a tucked 点 inside the wedge. Rebalanced: s3 shortened and repositioned '
        'to be a compact interior stroke; s4 tightened as a proper 点. '
        'TR11 (a) top-横 above the 撇 head; (b) interior mark + 点 both stay '
        'within the wedge and do not extend to canvas edges.'
    ),
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # ---- Stroke 1: top 一 (short horizontal) ----
    # MMH: TL(0.539,0.935) → TR(0.540,0.847). Both in T-row (row 0). Same-row ✓ (TR12).
    # Slight widen for radical readability.
    s1_head = ('TL', 0.30, 0.85)
    s1_tail = ('TR', 0.75, 0.85)
    draw_heng(draw, s1_head, s1_tail, width=6)

    # ---- Stroke 2: main 撇 (long down-left sweep) ----
    # MMH: TC(0.336,0.961) → BL(0.677,0.060). Widen to full sweep for standalone radical (TR9).
    s2_head = ('TC', 0.35, 0.90)   # ~(135, 90) — just below top-横
    s2_tail = ('BL', 0.10, 0.90)   # ~(10, 290) — reaches BL corner
    draw_pie(draw, s2_head, s2_tail,
             head_width=11, tail_width=1, curve=0.12, segments=48)

    # ---- Stroke 3: interior 横撇 (short compact diagonal INSIDE the wedge) ----
    # GT shows this as a shorter interior stroke, not a full-canvas sweep.
    # Keep the head near s2's mid-body and tail well INSIDE the wedge (not BL corner).
    s3_head = ('C',  0.25, 0.30)   # ~(125, 130) — inside wedge, right of s2 body
    s3_tail = ('C',  0.55, 0.90)   # ~(155, 190) — down-right INSIDE the wedge
    draw_pie(draw, s3_head, s3_tail,
             head_width=7, tail_width=1, curve=-0.05, segments=32)

    # ---- Stroke 4: 点 (small compact dot inside wedge, lower-right of s3) ----
    # MMH: C(0.113,0.819) → BC(0.368,0.145). Short down-right 点.
    s4_head = ('C',  0.55, 0.65)   # ~(155, 165)
    s4_tail = ('C',  0.75, 0.85)   # ~(175, 185)
    draw_dian(draw, s4_head, s4_tail,
              head_width=2, peak_width=9, curve=0.06, segments=24)

    return img


if __name__ == '__main__':
    img = render()
    out = os.path.join(os.path.dirname(__file__), '01_歹.png')
    img.save(out)
    print('saved', out)
    print('SELF_CHECK =', SELF_CHECK)
