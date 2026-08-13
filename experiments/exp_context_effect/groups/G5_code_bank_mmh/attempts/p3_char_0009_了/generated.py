"""p3_char_0009_了 — Phase-3 character 了.

# BANK_DEVIATION
# skipped: shu_wan_gou.py, yi_hook.py
# reason: 了's second stroke is 弯钩 (bends down-left with tiny leftward
#         hook), not 竖弯钩 (which curves right and hooks up-right).
#         Orientation is fundamentally different — inlining fresh.
# fresh_component: wan_gou_for_了 (curved vertical hook, bows right,
#                  terminates bottom-left with small hook to the left)

MMH structural expectations (2 strokes, 1 N-joint):
  - s1 head @ ('TL', 0.668, 0.935) -> pixel ~(66.8, 93.5)
       tail @ ('C',  0.503, 0.351) -> pixel ~(150.3, 135.1)
       (a 横撇: short horizontal that folds down into a small pie.)
  - s2 head @ ('C',  0.351, 0.318) -> pixel ~(135.1, 131.8)
       tail @ ('BC', 0.075, 0.587) -> pixel ~(107.5, 258.7)
       (弯钩 curved vertical hook, bows right, terminates lower-left
        with small leftward hook.)
  - joint: s1.tail <-> s2.head @ C, class N (natural gap ~13 px, no weld)
"""

import pathlib
from PIL import Image, ImageDraw


def _bezier2(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, steps=80):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w_head, w_tail):
    n = max(len(pts) - 1, 1)
    for i, (x, y) in enumerate(pts):
        t = i / n
        w = w_head * (1 - t) + w_tail * t
        draw.ellipse([x - w, y - w, x + w, y + w], fill='black')


def draw_char(draw):
    # ---- Stroke 1: 横撇 (horizontal into short pie) ----
    # Head at (67, 93). Horizontal arcs right to apex ~(200, 88), then
    # folds down-left into a short pie ending at tail ~(150, 135).
    head1 = (67, 93)
    apex = (205, 88)
    corner = (198, 100)
    tail1 = (150, 135)

    seg_a = _bezier2(head1, (130, 82), apex, steps=60)
    _stamp(draw, seg_a, 5.5, 7.5)

    seg_b = _bezier2(corner, (192, 122), tail1, steps=40)
    _stamp(draw, seg_b, 7.5, 2.5)

    # ---- Stroke 2: 弯钩 (curved vertical with tiny left hook) ----
    # Head at (135, 132), bows right through belly ~(158, 200), returns
    # left, tail at (108, 259), then a small hook curling to the left.
    head2 = (135, 132)
    belly = (162, 195)
    lower = (140, 245)
    tail2 = (108, 259)

    body = _bezier3(head2, belly, lower, tail2, steps=80)
    _stamp(draw, body, 5.0, 5.5)

    hook = _bezier2(tail2, (95, 258), (82, 246), steps=20)
    _stamp(draw, hook, 5.0, 2.0)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 stroke primitives (heng-pie + wan-gou)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [
        # s1.tail (150,135) <-> s2.head (135,132) at cell C.
        # actual pixel gap sqrt(15^2+3^2) ~ 15.3 px, close to expected 13.4.
        # Class N (no weld). Match.
    ],
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: inlined 横撇 + 弯钩 (no matching wan-gou bank primitive).',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = pathlib.Path(__file__).parent / '01_了.png'
    img.save(out)


if __name__ == '__main__':
    main()
