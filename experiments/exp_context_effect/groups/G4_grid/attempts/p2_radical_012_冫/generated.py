"""p2_radical_012_冫 — G4 attempt.

冫 (bīng) — "two-drops water" radical. 2 strokes:
  stroke 1: 点 (upper dot) — thin head upper-left → thick press lower-right
  stroke 2: 提 (lower rising flick) — thick head lower-left → thin tail upper-right

MMH-derived expected anchors:
  s1: head @ ('TC', 0.245, 0.976) tail @ ('C', 0.638, 0.395)
  s2: head @ ('BC', 0.315, 0.780) tail @ ('C', 0.734, 0.781)
Joints: NONE (strokes clearly separated — S class per principle bank).

Anchor plan:
  s1 (点) head=('TC',0.245,0.976), tail=('C',0.638,0.395)
         → pixel head ~(124.5, 97.6), tail ~(163.8, 139.5)
         short down-right dot, thin→thick, using draw_dian.
  s2 (提) head=('BC',0.315,0.780), tail=('C',0.734,0.781)
         → pixel head ~(131.5, 278.0), tail ~(173.4, 178.1)
         thick lower-left → thin upper-right rising flick, using draw_ti.
  Vertical clearance between s1.tail y=139 and s2.tail y=178 ≈ 39px gap
  through center; strokes do not intersect.

SELF_CHECK filled at bottom after render.
"""
import os
import sys
from PIL import Image, ImageDraw

# Make G4 primitives importable.
CODE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
))
sys.path.insert(0, CODE_DIR)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian  # noqa: E402
from ti import draw_ti  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': (
        's1 uses draw_dian with expected TC->C anchors; '
        's2 uses draw_ti with expected BC->C anchors. '
        'No joints (S). Both strokes near center per MMH.'
    ),
}


def render(out_path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: upper 点
    s1_head = ('TC', 0.245, 0.976)
    s1_tail = ('C', 0.638, 0.395)
    draw_dian(draw, s1_head, s1_tail,
              head_width=3, peak_width=13, curve=0.10, segments=32)

    # Stroke 2: lower 提 (rising)
    s2_head = ('BC', 0.315, 0.780)
    s2_tail = ('C', 0.734, 0.781)
    draw_ti(draw, s2_head, s2_tail,
            head_width=14, tail_width=1, curve=0.10, segments=48)

    # Direction invariants.
    p_s1h = anchor_to_xy(s1_head)
    p_s1t = anchor_to_xy(s1_tail)
    p_s2h = anchor_to_xy(s2_head)
    p_s2t = anchor_to_xy(s2_tail)
    assert p_s1t[0] > p_s1h[0] and p_s1t[1] > p_s1h[1], "s1 must go down-right"
    assert p_s2t[0] > p_s2h[0] and p_s2t[1] < p_s2h[1], "s2 must rise up-right"
    # No-intersection sanity: s1.tail below is well above s2.tail.
    assert p_s1t[1] < p_s2t[1], "s1 tail must sit above s2 tail (clear gap)"

    img.save(out_path)


if __name__ == '__main__':
    out = os.path.join(os.path.dirname(__file__), '01_冫.png')
    render(out)
    print(f"wrote {out}")
