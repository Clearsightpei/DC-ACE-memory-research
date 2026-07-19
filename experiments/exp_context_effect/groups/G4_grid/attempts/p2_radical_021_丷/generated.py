"""p2_radical_021_丷 — G4 attempt.

丷 (2画 radical) — "opposing dots". 2 strokes:
  stroke 1 (LEFT):  丶-like 点 sloping DOWN-RIGHT (thin head upper-left → 顿笔 press lower-right)
  stroke 2 (RIGHT): short 撇 sloping DOWN-LEFT (thick 起笔 upper-right → needle tip lower-left)

MMH-derived expected anchors (from brief):
  s1: head @ ('ML', 0.952, 0.447)  tail @ ('C',  0.254, 0.717)
        pixel head ≈ (95.2, 144.7)   tail ≈ (125.4, 171.7)   → down-RIGHT, ~40 px
  s2: head @ ('C',  0.904, 0.266)  tail @ ('C',  0.567, 0.764)
        pixel head ≈ (190.4, 126.6)  tail ≈ (156.7, 176.4)   → down-LEFT, ~60 px
Joints: NONE (clear separation between the two dots). Class = S.

Anchor plan (kept close to MMH; radical is inherently small — even in
characters like 兴/学/曾 丷 appears as two small marks. Per TR9, slight
expansion so the standalone reads as prominent, but not full-grid — the
GT PNG confirms 丷 sits in the middle third with a small gap between
strokes):

  s1 (点, left): head=('ML', 0.90, 0.40), tail=('C', 0.30, 0.75)
       → thin needle upper-left → rounded press lower-right; using draw_dian.
  s2 (撇, right): head=('C', 0.90, 0.25), tail=('C', 0.55, 0.80)
       → thick 顿笔 upper-right → needle tip lower-left; using draw_pie
         with reduced head_width (component-scale) and short segments.

Both strokes near vertical middle. Their tails at y≈220/240 are
horizontally ~40 px apart (s1 tail x≈130, s2 tail x≈155) with no
overlap — S-class separation.

Visual features that should agree with GT (per TR11 — name two):
  1. Left stroke slopes DOWN-RIGHT (top-left thin → bottom-right thick),
     matching GT's left mark.
  2. Right stroke slopes DOWN-LEFT (top-right thick → bottom-left thin),
     matching GT's right mark; the two strokes lean OUTWARD (away from
     each other), forming the ⺍-like signature of 丷.
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
from pie import draw_pie  # noqa: E402


# ------------------------- self check -------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 2 primitive calls below
    'endpoint_mismatches': [],  # anchors within tolerance of MMH expected
    'joint_class_mismatches': [],  # no joints expected (S class)
    'overall_pass': True,
    'notes': (
        's1 (左点) head=ML(0.90,0.40) tail=C(0.30,0.75): matches MMH '
        's1 head ML(0.952,0.447) tail C(0.254,0.717) within ±0.10. '
        's2 (右撇) head=C(0.90,0.25) tail=C(0.55,0.80): matches MMH '
        's2 head C(0.904,0.266) tail C(0.567,0.764) within ±0.05. '
        'S-class: no joint expected, no joint drawn. '
        'Visual agreement w/ GT: (a) left stroke slopes down-right, '
        '(b) right stroke slopes down-left; two marks lean OUTWARD.'
    ),
}


# ------------------------- render -------------------------
def render(out_path):
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: 左点 (like 丶) — thin upper-left head → thick lower-right press
    s1_head = ('ML', 0.90, 0.40)
    s1_tail = ('C',  0.30, 0.75)
    draw_dian(
        draw, s1_head, s1_tail,
        head_width=2, peak_width=12, curve=0.08, segments=24,
    )

    # Stroke 2: 右撇 — thick upper-right 起笔 → thin lower-left needle tip
    s2_head = ('C',  0.90, 0.25)
    s2_tail = ('C',  0.55, 0.80)
    draw_pie(
        draw, s2_head, s2_tail,
        head_width=11, tail_width=1, curve=0.10, segments=48,
    )

    # ------ direction / joint sanity asserts ------
    p_s1h = anchor_to_xy(s1_head)
    p_s1t = anchor_to_xy(s1_tail)
    p_s2h = anchor_to_xy(s2_head)
    p_s2t = anchor_to_xy(s2_tail)

    # s1 goes down-right
    assert p_s1t[0] > p_s1h[0], "s1 tail should be RIGHT of head (down-right dot)"
    assert p_s1t[1] > p_s1h[1], "s1 tail should be BELOW head"
    # s2 goes down-left
    assert p_s2t[0] < p_s2h[0], "s2 tail should be LEFT of head (down-left pie)"
    assert p_s2t[1] > p_s2h[1], "s2 tail should be BELOW head"
    # Two strokes should NOT overlap: s2 head is right of s1 tail
    assert p_s2h[0] > p_s1t[0], "s2 head must be right of s1 tail (S-class gap)"

    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), '01_丷.png')
    render(out)
    print(f"Wrote {out}")
