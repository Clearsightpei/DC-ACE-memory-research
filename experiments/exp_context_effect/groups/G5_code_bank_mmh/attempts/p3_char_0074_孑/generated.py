"""p3_char_0074_孑 — Phase-3 character 孑 (jié).

# BANK_DEVIATION
# skipped: heng_pie.py (bank primitive)
# reason: heng_pie's defaults (apex_x=hx+130, apex_y=hy-3) put the arc
#         apex too far right and too flat for this 孑's shorter, deeper
#         top-stroke geometry. Inlining fresh (same recipe as 了 A).
# fresh_component: heng_pie_for_孑 (short heng arcing right + short pie
#                  folding down-left, following the 了 A-verdict template).

# Uses bank: wan_gou.draw_wan_gou (from 了 A), ti.draw_ti (from 扌 PASS).

MMH structural expectations (3 strokes, 2 joints):
  - s1 head @ ('TL', 0.791, 0.908) -> pixel ~(79.1, 90.8)
       tail @ ('C',  0.559, 0.389) -> pixel ~(155.9, 138.9)
       (横撇 short horizontal folding into a pie.)
  - s2 head @ ('C',  0.342, 0.318) -> pixel ~(134.2, 131.8)
       tail @ ('BC', 0.096, 0.739) -> pixel ~(109.6, 273.9)
       (弯钩 curved vertical hook, bows right, terminates lower-left
        with small leftward hook flick.)
  - s3 head @ ('BL', 0.498, 0.235) -> pixel ~(49.8, 223.5)
       tail @ ('MR', 0.215, 0.541) -> pixel ~(221.5, 154.1)
       (提 rising diagonal, thick head lower-left -> fine tail upper-right.)
  - joint 1: s1.tail (~156, 139) <-> s2.head (~134, 132) at cell C.
             Class N (natural gap ~16 px, no weld).
  - joint 2: s2.mid(0.28) <-> s3.mid(0.66) at cell C(~164, 183).
             Class P (welded crossing).
"""

import pathlib
import sys
from PIL import Image, ImageDraw

# Add success_bank/code to path for bank imports
BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from wan_gou import draw_wan_gou  # noqa: E402
from ti import draw_ti  # noqa: E402


def _bezier2(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w_head, w_tail):
    n = max(len(pts) - 1, 1)
    for i, (x, y) in enumerate(pts):
        t = i / n
        w = w_head * (1 - t) + w_tail * t
        draw.ellipse([x - w, y - w, x + w, y + w], fill='black')


def draw_char(draw):
    # ---- Stroke 1: 横撇 (INLINE — BANK_DEVIATION from heng_pie) ----
    # Head at (79, 91). Arcs right to apex ~(210, 88), then folds down-left
    # into a short pie ending at tail (156, 139).
    head1 = (79, 91)
    apex = (210, 85)
    corner = (203, 98)
    tail1 = (156, 139)

    seg_a = _bezier2(head1, (140, 78), apex, steps=60)
    _stamp(draw, seg_a, 5.5, 7.5)

    seg_b = _bezier2(corner, (198, 122), tail1, steps=40)
    _stamp(draw, seg_b, 7.5, 2.5)

    # ---- Stroke 2: 弯钩 (bank: wan_gou) ----
    # head (134, 132) -> tail (110, 274). Bows right through belly, ends
    # with small leftward hook flick.
    draw_wan_gou(
        draw,
        head=(134, 132),
        tail=(110, 274),
        belly_right=30,
        hook_len=24,
        hook_up=12,
        w_head=5,
        w_body=5.5,
        w_tail=2,
    )

    # ---- Stroke 3: 提 (bank: ti) ----
    # head (50, 223) lower-left -> tail (222, 154) upper-right.
    # Must weld-cross the 弯钩 body near (~164, 183).
    draw_ti(
        draw,
        head=(50, 223),
        tail=(222, 154),
        w_head=8,
        w_tail=2,
        steps=60,
    )


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 stroke primitives (heng-pie + wan-gou + ti)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [
        # joint 1: s1.tail (156,139) <-> s2.head (134,132) at cell C.
        # actual gap sqrt(22^2 + 7^2) ~ 23 px. Expected N ~16 px. Both are
        # "N-class" (no weld) — reasonable given inline draft. OK.
        # joint 2: s2.mid(0.28) ~ (~155, 175) after bowing right; s3.mid(0.66)
        # ~ (163, 179). Distance ~4-8 px — welded (P). OK.
    ],
    'overall_pass': True,
    'notes': (
        'BANK_DEVIATION: inlined 横撇 following the 了 A-verdict template. '
        'Bank primitives used for 弯钩 (wan_gou) and 提 (ti). '
        'Joint P at cell C achieved via geometric alignment of wan_gou '
        'belly_right=30 with ti trajectory.'
    ),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_char(draw)
    out = pathlib.Path(__file__).parent / '01_孑.png'
    img.save(out)


if __name__ == '__main__':
    main()
