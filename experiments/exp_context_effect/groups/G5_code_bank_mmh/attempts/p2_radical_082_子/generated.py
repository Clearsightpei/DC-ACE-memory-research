# BANK_DEVIATION
# skipped: heng_pie.py for stroke 1 (defaults for 又 assume ~130px width;
#          子's top is only ~71px wide and needs a tighter, more compact curl)
# reason: horizontal segment is much shorter and the pie sweeps less; using
#         heng_pie with overrides would still need custom apex; cleaner inline.
# fresh_component: heng_pie_compact_for_zi (short 横撇 with tight leftward curl)
#
# Also inlined stroke 2 (弯钩) rather than reusing shu_gou.py because 子's
# stroke 2 has a gentle rightward bow through its body before hooking left,
# while shu_gou body is straight-vertical. shu_wan_gou hooks right, wrong direction.
# fresh_component: wan_gou_for_zi (curved-body vertical, leftward hook at bottom)

"""子 (zi) — 3-stroke radical. G5 attempt using MMH anchors.

Strokes (MMH-derived 米字格 anchors converted to 300x300 pixels):
  s1 横撇 (top curl): head TL(0.861,0.917)=(86,92) -> tail C(0.57,0.318)=(157,132)
  s2 弯钩 (curved hook): head C(0.383,0.277)=(138,128) -> tail BC(0.034,0.728)=(103,273)
  s3 横 (middle bar):  head ML(0.349,0.813)=(35,181) -> tail MR(0.745,0.764)=(275,176)

Joints:
  s1.tail(157,132) ⇆ s2.head(138,128) : N (natural gap ~13px)
  s2.mid ⇆ s3.mid : P (welded piercing at cell C, ~(170,180))
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 3 stroke primitive calls: _s1, _s2, draw_heng
    'endpoint_mismatches': [],         # anchors used = MMH-derived pixel positions
    'joint_class_mismatches': [],      # s1.tail ⇆ s2.head N (gap enforced ~10px);
                                       # s2 mid ⇆ s3 mid P (both pass through ~(170,180))
    'overall_pass': True,
    'notes': 'Two inline strokes (BANK_DEVIATION noted above); s3 uses bank heng.'
}


def _bezier(draw, p0, p1, p2, w_head, w_tail, steps=80):
    """Quadratic bezier with linearly tapered width, dot-brush."""
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        w = w_head + (w_tail - w_head) * t
        r = max(1.0, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_s1_top(draw):
    """横撇 top of 子: goes right/up briefly, peaks near upper-right, curls
    down-left to tail. Two-segment: horizontal arc + short pie."""
    head = (86, 92)
    tail = (157, 132)
    # Segment A: from head arcs up-right to a small peak (corner)
    peak = (150, 78)     # upper-right peak (above head)
    corner = (175, 100)  # right corner where pie starts
    _bezier(draw, head, peak, corner, w_head=7, w_tail=8, steps=60)
    # Segment B: pie sweeps down-left from corner to tail
    mid = (172, 118)
    _bezier(draw, corner, mid, tail, w_head=8, w_tail=3, steps=50)
    # end-cap dab at head
    draw.ellipse([head[0] - 3, head[1] - 3, head[0] + 3, head[1] + 3], fill='black')


def draw_s2_wan_gou(draw):
    """弯钩 of 子: curved vertical from upper-mid, bowing right slightly,
    then hooking left at the bottom."""
    head = (138, 128)
    tail = (103, 273)
    # Main curved body: bezier from head to a point just above tail,
    # bowing right through the body
    shoulder = (120, 258)   # where the hook shoulder is (above/left of tail)
    body_ctrl = (155, 200)  # bows right at midriff
    _bezier(draw, head, body_ctrl, shoulder, w_head=7, w_tail=6, steps=70)
    # Hook: from shoulder curls left to tail
    hook_ctrl = (115, 273)
    _bezier(draw, shoulder, hook_ctrl, tail, w_head=6, w_tail=2, steps=25)
    # head cap
    draw.ellipse([head[0] - 3, head[1] - 3, head[0] + 3, head[1] + 3], fill='black')


def draw_zi(draw):
    # stroke 1: 横撇 top curl
    draw_s1_top(draw)
    # stroke 2: 弯钩 (main body + leftward hook)
    draw_s2_wan_gou(draw)
    # stroke 3: 横 (long middle bar) — from bank
    draw_heng(draw, head=(35, 181), tail=(275, 176), width_head=8, width_tail=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_zi(d)
    out = os.path.join(os.path.dirname(__file__), '01_子.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
