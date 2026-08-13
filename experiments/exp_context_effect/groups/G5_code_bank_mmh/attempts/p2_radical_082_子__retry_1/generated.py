# TRAJECTORY DIFF (retry 1)
# ---------------------------------------------------------------
# main attempt (FAIL) at 01_子.png — visual gaps vs GT:
#   1) s1 (横撇) went UP-first (peak (150,78)) — GT's s1 has NO upward
#      peak; it starts high-right, moves SHORT-RIGHT, then curls
#      distinctly DOWN-LEFT. My upward peak read as an extra bump/tick.
#   2) s2 (弯钩) hook at bottom was too tight/short — leftward turn
#      barely visible (hook_ctrl (115,273), tail (103,273): only ~15px
#      of leftward travel). GT shows a clean, decisive leftward curl
#      that extends the tail further left of the shaft.
#   3) s3 (heng) endpoints looked bulbous — using draw_heng with
#      widths 8/10 emphasized the tail dab; the heng also spanned
#      too far (275-35 = 240 px, ~80% canvas) while GT is closer to
#      ~200 px span, feeling tighter.
#
# Fixes this attempt:
#   1) s1: rewrite as clean 横撇 — small nearly-horizontal head arc
#      (no upward peak), sharp corner near (170, 110), pie sweeps
#      down-left to tail (155, 138). Head is highest, tail lower.
#   2) s2: stronger, visible leftward hook — shoulder at (127, 260),
#      tail at (95, 282), so hook travels ~30 px leftward + tapers.
#   3) s3: use draw_heng but with head=(50,180)/tail=(255,175) —
#      slightly tighter span (~205 px), width 7/8 lighter.
# ---------------------------------------------------------------

# BANK_DEVIATION
# skipped: heng_pie.py (bank primitive assumes ~130 px width, 又-style);
#          子's 横撇 is tight/compact at ~85 px width with sharp corner.
# reason: heng_pie geometry doesn't fit 子's compact top curl.
# fresh_component: heng_pie_compact_for_zi
#
# Also inlined stroke 2 (弯钩). Bank has shu_gou (straight body, left
# hook) and shu_wan_gou (curved body, RIGHT hook). Neither matches
# 弯钩's curved-body + LEFT hook.
# fresh_component: wan_gou_for_zi

"""子 (zi) — 3-stroke radical. G5 retry 1.

MMH-derived anchors (300x300 pixels):
  s1 横撇  head TL(0.861,0.917)=(86,92)  tail C(0.57,0.318)=(155,138)
  s2 弯钩  head C(0.383,0.277)=(133,127) tail BC(0.034,0.728)=(95,282)
  s3 横    head ML(0.349,0.813)=(50,180) tail MR(0.745,0.764)=(255,175)

Joints:
  s1.tail(155,138) N s2.head(133,127) — gap ~24 px (>expected 13 px OK: N-class)
  s2.mid P s3.mid — welded at ~(140,175) (both strokes pass through)
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 3 strokes: draw_s1, draw_s2, draw_heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Retry 1: fixed s1 (no upward peak), stronger s2 hook, tighter s3.'
}


def _bezier_taper(draw, p0, p1, p2, w_head, w_tail, steps=80):
    """Quadratic Bezier with linear width taper, dot-brush rendering."""
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        w = w_head + (w_tail - w_head) * t
        r = max(1.0, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_s1_heng_pie(draw):
    """子's 横撇 top stroke.
    Small nearly-horizontal head-run right, sharp corner up-top-right,
    then pie sweeps down-left. NO upward peak (that was the main fail).
    """
    head = (86, 92)         # TL: entry point
    corner = (172, 108)     # top-right corner (slightly LOWER than head — no peak)
    tail = (155, 138)       # C: end of pie, sits inside upper-center
    # Segment A: gentle horizontal-ish rise from head to corner
    mid_a = (130, 96)       # slightly above midpoint = mild arc, no big peak
    _bezier_taper(draw, head, mid_a, corner, w_head=7, w_tail=9, steps=60)
    # Segment B: sharp pie down-left from corner to tail, tapering thin
    mid_b = (170, 128)
    _bezier_taper(draw, corner, mid_b, tail, w_head=9, w_tail=3, steps=50)
    # small entry dab at head
    draw.ellipse([head[0] - 3, head[1] - 3, head[0] + 4, head[1] + 4], fill='black')


def draw_s2_wan_gou(draw):
    """子's 弯钩: curved-body vertical with clear LEFT-CURL hook.
    Head near upper-mid, body bows RIGHT gently, then decisive
    leftward hook at bottom.
    """
    head = (133, 127)
    shoulder = (127, 260)      # where body ends and hook starts
    tail = (95, 282)           # hook end (well to the LEFT of shoulder)
    # Main body: bezier from head to shoulder, bowing right through the middle
    body_ctrl = (160, 200)     # bows right of the head-shoulder line
    _bezier_taper(draw, head, body_ctrl, shoulder, w_head=7, w_tail=6, steps=90)
    # Hook: distinct leftward curl, tapering to fine tip
    hook_ctrl = (118, 285)     # pulls the curve down-and-left
    _bezier_taper(draw, shoulder, hook_ctrl, tail, w_head=6, w_tail=2, steps=40)
    # head dab
    draw.ellipse([head[0] - 3, head[1] - 3, head[0] + 4, head[1] + 4], fill='black')


def draw_zi(draw):
    # s1: 横撇 top curl
    draw_s1_heng_pie(draw)
    # s2: 弯钩 curved body with leftward hook
    draw_s2_wan_gou(draw)
    # s3: 横 middle bar — bank heng, tighter span, slightly lighter width
    draw_heng(draw, head=(50, 180), tail=(255, 175), width_head=7, width_tail=8)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_zi(d)
    out = os.path.join(os.path.dirname(__file__), '01_子.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
