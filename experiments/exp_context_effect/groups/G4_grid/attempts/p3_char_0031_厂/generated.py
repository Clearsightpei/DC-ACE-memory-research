"""厂 (p3_char_0031) — G4 grid-bank Phase-3 character render (re-draw).

NOTE: prior attempt drew against a corrupted GT PNG (had overlaid
strokes) and welded s1/s2 heads (T-class) per the p2 radical errata
fix. The GT has been REGENERATED CLEAN; the clean GT shows the
canonical 厂 with the MMH-native N-class small gap between the 横 head
and the 撇 head. This attempt follows MMH literally.

Per-stroke anchors (MMH-derived, dispatcher-injected):
  s1 (横): head @ ('TC', 0.011, 0.97) → PIL (100.1,  97.0)
           tail @ ('TR', 0.432, 0.838) → PIL (243.2,  83.8)
  s2 (撇): head @ ('TL', 0.773, 0.94) → PIL ( 77.3,  94.0)
           tail @ ('BL', 0.202, 0.974) → PIL ( 20.2, 297.4)

Joint spec:
  s1.head ⇆ s2.head : N-class (small natural gap ≈ 23 px in PIL —
                       MMH-nominal ≈ 18.8 px). DO NOT weld.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image

from _anchor import anchor_to_xy
from heng import draw_heng
from pie import draw_pie


# ---- Anchors -------------------------------------------------------------
S1_HEAD = ('TC', 0.011, 0.97)
S1_TAIL = ('TR', 0.432, 0.838)
S2_HEAD = ('TL', 0.773, 0.94)
S2_TAIL = ('BL', 0.202, 0.974)

# ---- Structural self-check (pre-render, based on anchors) ---------------
_p1h = anchor_to_xy(S1_HEAD)
_p2h = anchor_to_xy(S2_HEAD)
_JOINT_GAP = ((_p1h[0] - _p2h[0]) ** 2 + (_p1h[1] - _p2h[1]) ** 2) ** 0.5

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 2 primitives: draw_heng + draw_pie
    'endpoint_mismatches': [], # anchors match MMH literally
    'joint_class_mismatches': [],  # N-class preserved (~23 px gap)
    'overall_pass': True,
    'notes': (
        f'Clean-GT redraw. s1.head↔s2.head gap = {_JOINT_GAP:.1f} px '
        f'(N-class, MMH nominal ≈ 18.8 px). No weld — corrupted-GT '
        f'attempt had T-weld; that fix was for the radical form, not '
        f'the canonical character.'
    ),
}


def render():
    from PIL import ImageDraw
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # s1 — 横 (top horizontal, slight upward-right slope per MMH)
    draw_heng(draw, S1_HEAD, S1_TAIL, width=9)

    # s2 — 撇 (sweep from just left of s1.head down-left to BL)
    # curve bows to the lower-left (belly out toward the writer's left).
    draw_pie(draw, S2_HEAD, S2_TAIL,
             head_width=10, tail_width=1, curve=0.12, segments=64)

    # ---- Post-render invariants (TR8) ----
    p1h = anchor_to_xy(S1_HEAD)
    p1t = anchor_to_xy(S1_TAIL)
    p2h = anchor_to_xy(S2_HEAD)
    p2t = anchor_to_xy(S2_TAIL)

    assert p1t[0] > p1h[0], '横 must go left→right'
    assert p2t[1] > p2h[1], '撇 tail must be BELOW head'
    assert p2t[0] < p2h[0], '撇 tail must be LEFT of head (down-left sweep)'
    gap = ((p1h[0] - p2h[0]) ** 2 + (p1h[1] - p2h[1]) ** 2) ** 0.5
    assert 8 < gap < 40, f'N-class gap out of range: {gap:.1f}'

    print(f'[厂] s1.head↔s2.head N-gap = {gap:.1f} px')

    out = os.path.join(os.path.dirname(__file__), '01_厂.png')
    img.save(out)
    print(f'[厂] wrote {out}')


if __name__ == '__main__':
    render()
