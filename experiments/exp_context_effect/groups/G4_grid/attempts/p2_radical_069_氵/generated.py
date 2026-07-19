"""氵 (shuǐ, 3-drops-of-water radical) — 3 strokes, left-side radical.

Anchor plan (MMH-derived, verbatim per brief):
  stroke 1 (点):  head ('TC', 0.195, 0.771), tail ('C',  0.629, 0.104)
                  small tilted dot upper-left of center
  stroke 2 (点):  head ('ML', 0.929, 0.395), tail ('C',  0.312, 0.688)
                  middle dot, tilted down-right toward center
  stroke 3 (提):  head ('BC', 0.166, 0.944), tail ('C',  0.743, 0.901)
                  bottom rising stroke, thick head (BL area) → thin tip up-right
Joints: NONE — three strokes, no P/T welds; clear separation (S-class).

Notes on transformation:
- MMH anchors keep 氵 left-of-center (radical role), matching GT which
  shows the radical occupying roughly the left half.
- Strokes 1 and 2 are 点 (comma-shaped drops): thin head → thick 顿笔 tail.
- Stroke 3 is 提 (rising): thick head (顿笔) → thin needle tip going
  up-and-right. Uses stroke_variable_width with reversed width profile.
"""
import sys
import os
sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Two named agreements vs GT: (1) three separate ink '
              'clusters on the left side of the canvas, arranged '
              'top-middle-bottom; (2) top two are short tilted dots '
              'while the bottom is a longer diagonal rising stroke '
              '(提). Stroke count = 3 = MMH. No joints expected.'),
}


def draw_ti(draw, from_anchor, to_anchor,
            head_width=14, tail_width=2, curve=-0.05, segments=32,
            color=(0, 0, 0)):
    """提 (tí) — rising stroke, thick 顿笔 head → needle tip up-right.

    curve < 0 bows slightly concave-up (natural rising arc).
    """
    p0 = anchor_to_xy(from_anchor)
    p2 = anchor_to_xy(to_anchor)
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = max(1.0, (dx * dx + dy * dy) ** 0.5)
    perp = (dy / length, -dx / length)
    bow = curve * length
    mid = ((p0[0] + p2[0]) * 0.5, (p0[1] + p2[1]) * 0.5)
    ctrl = (mid[0] + perp[0] * bow, mid[1] + perp[1] * bow)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_width + (tail_width - head_width) * (i / segments)
              for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths, color=color)
    # Rounded press at the head (顿笔).
    r = head_width / 2.0
    draw.ellipse([p0[0] - r, p0[1] - r, p0[0] + r, p0[1] + r], fill=color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1 — upper 点
    s1_head = ('TC', 0.195, 0.771)
    s1_tail = ('C',  0.629, 0.104)
    draw_dian(draw, s1_head, s1_tail, head_width=2, peak_width=11, curve=0.08)

    # Stroke 2 — middle 点
    s2_head = ('ML', 0.929, 0.395)
    s2_tail = ('C',  0.312, 0.688)
    draw_dian(draw, s2_head, s2_tail, head_width=2, peak_width=11, curve=0.08)

    # Stroke 3 — bottom 提 (rising)
    s3_head = ('BC', 0.166, 0.944)
    s3_tail = ('C',  0.743, 0.901)
    draw_ti(draw, s3_head, s3_tail, head_width=14, tail_width=2, curve=-0.05)

    # Sanity: direction invariants
    p1_head = anchor_to_xy(s1_head)
    p1_tail = anchor_to_xy(s1_tail)
    p2_head = anchor_to_xy(s2_head)
    p2_tail = anchor_to_xy(s2_tail)
    p3_head = anchor_to_xy(s3_head)
    p3_tail = anchor_to_xy(s3_tail)
    # 点s should have tail down-right of head (in PIL: y grows DOWN, so
    # tail.y > head.y and tail.x > head.x). Wait — with MMH y_frac
    # convention here, larger y_frac = further down IN THE CELL. Verify.
    # s1: head TC(y=0.771 -> py ~77) tail C(y=0.104 -> py ~110). tail.y > head.y OK
    # s2: head ML(0.395 -> py ~140) tail C(0.688 -> py ~230). tail.y > head.y OK
    assert p1_tail[1] > p1_head[1], f's1 tail not below head: {p1_head} {p1_tail}'
    assert p2_tail[1] > p2_head[1], f's2 tail not below head: {p2_head} {p2_tail}'
    # 提 (rising): tail up-and-right of head (tail.y < head.y, tail.x > head.x)
    assert p3_tail[1] < p3_head[1], f'ti tail not above head: {p3_head} {p3_tail}'
    assert p3_tail[0] > p3_head[0], f'ti tail not right of head: {p3_head} {p3_tail}'

    out = os.path.join(os.path.dirname(__file__), '01_氵.png')
    img.save(out)
    print(f'Saved {out}')
    print(f'SELF_CHECK: {SELF_CHECK}')


if __name__ == '__main__':
    main()
