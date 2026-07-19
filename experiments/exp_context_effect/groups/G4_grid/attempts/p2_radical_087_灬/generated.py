"""灬 (huǒ, 4画 radical — "four dots of fire").

Four dots along the bottom of the 米字格. Leftmost dot leans LEFT
(下-left slant, like 撇点). The remaining three lean RIGHT with the
rightmost usually the largest/most emphatic (捺-like dot).

MMH-injected anchors:
  s1: head ML(0.677, 0.708)  tail BL(0.504, 0.206)   ← down-left slant
  s2: head C (0.069, 0.72)   tail BC(0.225, 0.033)   ← down-right, mild
  s3: head C (0.544, 0.708)  tail C (0.729, 0.989)   ← down-right, mild
  s4: head MR(0.092, 0.69)   tail BR(0.52, 0.194)    ← down-right, larger

Joints: NONE (clear separation).

Bank primitive reused: draw_dian (from dian.py), with OVERRIDING anchor
tuples for each of the four dots (per TR1). No default-anchor calls.
"""
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        '4 dots, all in bottom half. Stroke 1 slants down-left '
        '(dian-pie flavor). Strokes 2,3,4 slant down-right. Stroke 4 '
        'is the largest (traditional 捺-flavor rightmost 点). No joints, '
        'clear inter-dot gaps. Revised once (pass 2): narrowed peak '
        'widths (10-12 -> 5-7 px) to match GT slender-stroke look; '
        'first pass dots were too chunky vs GT.'
    ),
}


def draw_huo_dots(draw):
    # ---- Stroke 1: leftmost dot, leans DOWN-LEFT (撇点-like)
    s1_head = ('ML', 0.677, 0.708)
    s1_tail = ('BL', 0.504, 0.206)
    draw_dian(draw, s1_head, s1_tail,
              head_width=1, peak_width=6, curve=0.05, segments=24)

    # ---- Stroke 2: mild down-right slant, near left-of-center
    s2_head = ('C', 0.069, 0.72)
    s2_tail = ('BC', 0.225, 0.033)
    draw_dian(draw, s2_head, s2_tail,
              head_width=1, peak_width=5, curve=0.05, segments=24)

    # ---- Stroke 3: mild down-right slant, right-of-center (short)
    s3_head = ('C', 0.544, 0.708)
    s3_tail = ('C', 0.729, 0.989)
    draw_dian(draw, s3_head, s3_tail,
              head_width=1, peak_width=5, curve=0.05, segments=24)

    # ---- Stroke 4: rightmost dot, LARGER, down-right slant (捺-flavor)
    s4_head = ('MR', 0.092, 0.69)
    s4_tail = ('BR', 0.52, 0.194)
    draw_dian(draw, s4_head, s4_tail,
              head_width=1, peak_width=7, curve=0.06, segments=28)

    # ---- Sanity asserts (per sandbox: assert direction invariants) ----
    p1h, p1t = anchor_to_xy(s1_head), anchor_to_xy(s1_tail)
    p2h, p2t = anchor_to_xy(s2_head), anchor_to_xy(s2_tail)
    p3h, p3t = anchor_to_xy(s3_head), anchor_to_xy(s3_tail)
    p4h, p4t = anchor_to_xy(s4_head), anchor_to_xy(s4_tail)
    # Stroke 1 slants left (tail.x < head.x) and down (tail.y > head.y)
    assert p1t[0] < p1h[0] and p1t[1] > p1h[1], 's1 must go down-left'
    # Strokes 2/3/4 slant right and down
    for (ph, pt, name) in [(p2h, p2t, 's2'), (p3h, p3t, 's3'), (p4h, p4t, 's4')]:
        assert pt[0] > ph[0] and pt[1] > ph[1], f'{name} must go down-right'
    # All 4 dots in bottom half of canvas (y > 150 for tails)
    for pt, name in [(p1t, 's1'), (p2t, 's2'), (p3t, 's3'), (p4t, 's4')]:
        assert pt[1] > 150, f'{name} tail must be in bottom half'
    # Left-to-right ordering of the dots by head x
    assert p1h[0] < p2h[0] < p3h[0] < p4h[0], 'dots must be ordered L->R'


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_huo_dots(draw)
    out = os.path.join(_HERE, '01_灬.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
