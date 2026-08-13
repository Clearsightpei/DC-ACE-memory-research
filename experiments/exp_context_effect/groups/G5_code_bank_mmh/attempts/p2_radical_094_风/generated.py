# BANK_DEVIATION
# skipped: heng_zhe_gou.py
# reason: 风's stroke 2 is 横斜弯钩 — a single fluid curved sweep from
#   top-left across the top then curving down the right side to a hook
#   at ~2/3 height, NOT a rigid heng+corner+shu+hook with a boxy turn.
# fresh_component: heng_xie_wan_gou_for_feng — inline arc-then-hook
#   built from a chain of quadratic-bezier ellipses.

"""风 (feng) — 4-stroke outer-frame radical."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,           # side-by-side vs GT: 4 strokes, outer
                                 # frame + inner X, recognizable as 风
    'stroke_count_ok': True,     # exactly 4 stroke primitives called
    'endpoint_mismatches': [],   # all 4 endpoints use MMH anchors as given
    'joint_class_mismatches': [], # s1/s2 N (small gap ~15px), s3/s4 P (cross)
    'overall_pass': True,
    'notes': 's2 inlined via BANK_DEVIATION (heng-xie-wan-gou, single '
             'fluid arc not a boxy heng_zhe_gou). s3(pie) + s4(na) '
             'cross at BC forming inner 乂 (welded P joint).',
}


def _bezier_chain(draw, p0, p1, p2, steps, w_head, w_tail):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_heng_xie_wan_gou(draw, heng_head, top_right, hook_tip):
    """Inline 横斜弯钩 for 风: horizontal along top, then long curve down
    the right side, ending with a small upward-left hook flick.
    """
    # Segment A: heng (top) — heng_head across to top_right corner
    _bezier_chain(
        draw,
        heng_head,
        ((heng_head[0] + top_right[0]) / 2, heng_head[1] - 2),
        top_right,
        steps=70, w_head=6.0, w_tail=6.5,
    )
    # Segment B: curved wan (right side) — top_right down to hook_tip,
    # bowing slightly outward to the right.
    tx, ty = top_right
    hx, hy = hook_tip
    # control point pushed to the right of the chord for a rightward belly
    ctrl = (max(tx, hx) + 12, (ty + hy) / 2 + 8)
    _bezier_chain(
        draw,
        top_right,
        ctrl,
        hook_tip,
        steps=80, w_head=6.5, w_tail=4.0,
    )
    # Segment C: small hook flick — from hook_tip going up-left ~10px
    # ending in a fine point (this is the 钩 tip).
    fx, fy = hook_tip[0] - 12, hook_tip[1] - 10
    steps_c = 20
    for i in range(steps_c):
        t = i / (steps_c - 1)
        x = hook_tip[0] + (fx - hook_tip[0]) * t
        y = hook_tip[1] + (fy - hook_tip[1]) * t
        r = 4.0 * (1 - t) + 0.8
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ------------ Stroke 1: 撇 (left leg) ------------
    # head (ML, 0.715, 0.028) = (71.5, 102.8)
    # tail (BL, 0.401, 0.871) = (40.1, 287.1)
    draw_pie(d, head=(71.5, 102.8), tail=(40.1, 287.1),
             bow_perp=14, w_head=8, w_tail=3)

    # ------------ Stroke 2: 横斜弯钩 (outer top-right) ------------
    # head (ML, 0.958, 0.146) = (95.8, 114.6)
    # tail (BR, 0.748, 0.317) = (274.8, 231.7) — this is the hook tip
    # top-right corner ≈ (245, 100) inferred from the outer frame
    draw_heng_xie_wan_gou(
        d,
        heng_head=(95.8, 114.6),
        top_right=(245.0, 100.0),
        hook_tip=(274.8, 231.7),
    )

    # ------------ Stroke 3: 撇 (inner) ------------
    # head (C, 0.573, 0.28) = (157.3, 128.0)
    # tail (BL, 0.926, 0.625) = (92.6, 262.5)
    draw_pie(d, head=(157.3, 128.0), tail=(92.6, 262.5),
             bow_perp=8, w_head=6, w_tail=2)

    # ------------ Stroke 4: 捺 (inner, crosses s3 at BC) ------------
    # head (C, 0.075, 0.605) = (107.5, 160.5)
    # tail (BC, 0.808, 0.531) = (180.8, 253.1)
    draw_na(d, head=(107.5, 160.5), tail=(180.8, 253.1),
            bow_perp=6, w_head=3, w_tail=8)

    out = Path(__file__).parent / '01_风.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
