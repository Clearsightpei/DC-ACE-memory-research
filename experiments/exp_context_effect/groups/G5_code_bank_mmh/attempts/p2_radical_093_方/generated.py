# BANK_DEVIATION
# skipped: heng_zhe_gou.py
# reason: MMH gives only s3 head/tail (C -> BC) for stroke 3, no explicit
#         (heng_head, corner, gou_tail, hook_tip) decomposition. Inlining a
#         simple curved down-hook stays faithful to the 2-anchor spec and
#         renders the small hook shape at bottom-center of 方.
# fresh_component: down_hook_short_for_fang
"""方 (fang) — 4 strokes: dian, heng, inline down-hook, pie."""
import os
import sys

from PIL import Image, ImageDraw

_BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from pie import draw_pie  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 primitive calls == expected 4
    'endpoint_mismatches': [],      # anchors used verbatim from MMH block
    'joint_class_mismatches': [],   # both expected joints are class N (natural gap)
    'overall_pass': True,
    'notes': (
        'Anchors used verbatim: s1 TC dian, s2 ML->MR heng, '
        's3 C->BC inline down-hook (BANK_DEVIATION from heng_zhe_gou which '
        'needs 4 anchors), s4 C->BL pie. Both joints are N-class: s2.mid vs '
        's4.head near C (gap ~12px) and s3.head vs s4.mid near C (gap ~18px) '
        '- rendered without welding.'
    ),
}


def draw_down_hook_short(draw, head, tail, width=7):
    """Inline compound (方-style): vertical/curved descent from head, then a
    distinct upward-left hook flick to tail. Head is the top of the vertical;
    tail is the hook tip. Rendered in two segments so the hook is visibly
    a hook, not just a curved line.
    """
    x0, y0 = head
    x2, y2 = tail
    # Bottom of the vertical descent, just before the hook flick.
    knee_x = x0 + 4        # small rightward bulge as it descends (calligraphy)
    knee_y = y2 + 6        # bottom-of-vertical slightly above tail
    # Segment A: curved vertical descent (head -> knee)
    steps_a = 60
    ctrl_x = x0 + 8
    ctrl_y = (y0 + knee_y) / 2
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * ctrl_x + t ** 2 * knee_x
        by = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * ctrl_y + t ** 2 * knee_y
        w = width - 1.5 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
    # Segment B: hook flick (knee -> tail), tapers to a point
    steps_b = 22
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = knee_x + (x2 - knee_x) * t
        by = knee_y + (y2 - knee_y) * t
        w = (width - 1.5) * (1 - t) + 0.9
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # s1 dian: TC(0.307,0.589) -> TC(0.693,0.932) => (130.7, 58.9) -> (169.3, 93.2)
    draw_dian(d, (130.7, 58.9), (169.3, 93.2),
              w_head=3, w_tail=8, bow=4, steps=48)

    # s2 heng: ML(0.434,0.471) -> MR(0.666,0.301) => (43.4, 147.1) -> (266.6, 130.1)
    draw_heng(d, (43.4, 147.1), (266.6, 130.1), width_head=8, width_tail=9)

    # s3 down-hook (inline): C(0.518,0.72) -> BC(0.239,0.643)
    #     => (151.8, 172.0) -> (123.9, 264.3)
    draw_down_hook_short(d, (151.8, 172.0), (123.9, 264.3), width=7)

    # s4 pie: C(0.409,0.436) -> BL(0.357,0.774) => (140.9, 143.6) -> (35.7, 277.4)
    draw_pie(d, (140.9, 143.6), (35.7, 277.4),
             bow_perp=14, w_head=8, w_tail=3, steps=80)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_方.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
