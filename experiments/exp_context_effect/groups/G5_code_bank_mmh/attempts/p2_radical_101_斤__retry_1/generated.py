"""G5 retry_1: p2_radical_101_斤 (radical, 4 strokes).

TRAJECTORY DIFF (visual inspection of main attempt vs GT):
  Main attempt (verdict C) failure modes I can SEE:
    1. s1 was rendered as a stubby flat heng at the top. In GT, s1 is a
       clearly SLANTED tick — head high-right, tail lower-left — reading
       as a short pie/tapered tick, not a horizontal bar. My retry uses
       draw_pie for s1 (tapered) instead of draw_heng.
    2. s2 (long pie) came out TOO THICK at the head (bulbous). GT's s2
       has a more moderate head with a long, clean taper. Reducing
       w_head from 9 to 7 and steps a bit higher.
    3. s2's bow was too shallow — GT shows a pronounced calligraphic
       arc. Bumping bow_perp from 10 to 14.
    4. s3 heng floated too far right, disconnected from s2. Nudge s3
       head left by ~10 px (from 107 to 97) so it visually threads
       through the "shoulder" region near s2's midpoint.
    5. s4 (shu) was fine in position; keeping it, extending slightly
       lower (y=310 pre-clip) so the tail reads as long-descending.

PLAN: pie(s1) + pie(s2, thinner head, more bow) + heng(s3, nudged left)
+ shu(s4, extended). No BANK_DEVIATION — all 4 strokes map cleanly.

MMH anchors (300x300, 米字格 100px cells):
  s1: TC(0.934, 0.727)=(193, 73)  →  TC(0.102, 0.97)=(110, 97)
  s2: TL(0.829, 0.935)=(83, 94)   →  BL(0.331, 0.818)=(33, 282)
  s3: C(0.069, 0.576)=(107, 158)  →  MR(0.587, 0.371)=(259, 137)
  s4: C(0.667, 0.535)=(167, 154)  →  BC(0.79, 1.199)=(179, 320)

Joints (all N):
  s1.tail ⇆ s2.head @ C, expected gap ~22px
  s2.mid(0.34) ⇆ s3.head @ C, expected gap ~15px
  s3.mid(0.33) ⇆ s4.head @ C, expected gap ~18px
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 primitive calls
    'endpoint_mismatches': [
        {'stroke': 3, 'expected': (107, 158), 'actual': (97, 160),
         'delta': (-10, +2), 'reason': 'nudge left to close visual N-gap at s2.mid'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry_1: s1 switched from heng to pie (tapered tick); s2 head thinned + more bow; '
             's3 nudged left; s4 extended.',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short slanted tick — nearly straight, slim; small pie taper
    s1_head = (193, 73)
    s1_tail = (110, 97)
    draw_pie(d, s1_head, s1_tail, bow_perp=1, w_head=5, w_tail=3, steps=48)

    # s2: long pie sweeping down-left, calligraphic bow
    s2_head = (83, 94)
    s2_tail = (33, 282)
    draw_pie(d, s2_head, s2_tail, bow_perp=14, w_head=7, w_tail=3, steps=90)

    # s3: middle heng, slight upward tilt, nudged left to bridge s2
    s3_head = (97, 160)
    s3_tail = (259, 137)
    draw_heng(d, s3_head, s3_tail, width_head=7, width_tail=9)

    # s4: vertical shu descending; clip to canvas
    s4_head = (167, 154)
    s4_tail = (179, 300)
    draw_shu(d, s4_head, s4_tail, width=7)

    return img


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_斤.png'
    render().save(out)
    print(f'wrote {out}')
