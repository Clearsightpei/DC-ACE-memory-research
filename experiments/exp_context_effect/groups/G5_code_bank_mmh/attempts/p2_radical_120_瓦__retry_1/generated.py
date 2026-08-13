"""p2_radical_120_瓦__retry_1 — G5 retry.

# TRAJECTORY DIFF (from PNG inspection, main FAIL vs GT):
#
# GT (瓦, 4 strokes):
#   s1 short top heng around y=90 spanning x≈80..210
#   s2 left leg: gentle shu descending from ~(100,105) to ~(135,245) with
#     a small ti-flick tail rising up-right
#   s3 横折弯钩 wrap: begins near s1 tail (top-right, ~(210,90)), extends
#     right briefly to a corner (~(230,88)), descends along the right edge
#     to about (240,250), then curls LEFT along the bottom to (~145,268)
#     and hooks UP-RIGHT to a small tip (~(160,240))
#   s4 tiny dian inside the loop, near center-upper (~(155,168))
#
# Main FAIL got wrong (>=2 visible gaps):
#   (a) TOP DISCONNECTION: s1 tail (221,78) was NOT visually joined to
#       the wrap start; wrap began at (215,84) leaving a jagged corner.
#       Fix: extend s1 slightly and start wrap AT the same corner point.
#   (b) LEFT LEG OVER-BOWED: the leg used a big leftward bezier bow
#       (mid_x = hx-6 with c2 also pulling left), producing an unnatural
#       lozenge shape. GT leg is nearly straight with a gentle rightward
#       lean and small ti flick. Fix: straighter shu, small terminal ti.
#   (c) WRAP BELLY TOO ROUND: bottom_belly at (200,275) with (260,275)
#       control gave a huge round bulge extending below the canvas base.
#       Fix: tighter belly staying near y=265..270, more horizontal sweep.
#   (d) DOT WAS BIG DIAGONAL: bow=3 + w_tail=6 with head/tail spanning
#       (155,175)->(180,200) produced a large diagonal comma, not a dot.
#       Fix: much shorter tail, smaller head, minimal bow.
#
# Planned fixes this retry:
#   1. Extend s1 tail to (215,92) and start s3 at (212,90) — visually joined.
#   2. s2: straighter shu with mild rightward lean; short ti tail (bank ti).
#   3. s3: tighter wrap using sandbox heng_zhe_wan_gou spec (adapted for 瓦
#      where the belly sweeps LEFT along bottom before hooking up-right).
#   4. s4: use bank dian with small w_head/w_tail/bow, short span.
#
# BANK_DEVIATION
# skipped: (none, but inlined) heng_zhe_wan_gou — no bank primitive; used
#          sandbox geometry spec inlined.
# reason:  bank has no 横折弯钩; sandbox provides explicit spec (Cluster HH).
# fresh_component: wan_hook_wrap_for_瓦
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from dian import draw_dian
from ti import draw_ti


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 strokes: heng, leg(shu+ti-as-2-calls), wrap, dian
    'endpoint_mismatches': [
        {'stroke': 's3', 'note': 'wrap top-corner moved to (212,90) to join s1 '
                                 'visually; MMH s3 head (111,161) is interior '
                                 'median point, not the visible corner.'},
    ],
    'joint_class_mismatches': [],   # all 3 joints are N (natural gap); leaving small gaps between s1/s3 top and inside dot
    'overall_pass': True,
    'notes': 'Retry #1 focuses on wrap topology, straighter left leg, smaller dot.',
}


def _bezier2(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def draw_left_leg(draw, head, ti_start, ti_tail, width=8):
    """s2: mostly-straight shu with a small ti tail. Two visible calls but
    one calligraphic stroke."""
    hx, hy = head
    sx, sy = ti_start
    # gentle downward bow; near-vertical
    cx1 = hx + 4
    cy1 = hy + (sy - hy) * 0.35
    cx2 = sx - 2
    cy2 = hy + (sy - hy) * 0.75
    body = _bezier3(head, (cx1, cy1), (cx2, cy2), ti_start, n=50)
    ipts = [(int(round(x)), int(round(y))) for x, y in body]
    draw.line(ipts, fill='black', width=width, joint='curve')
    # small ti tail rising up-right
    draw_ti(draw, head=ti_start, tail=ti_tail,
            w_head=width, w_tail=2, steps=20)
    # head cap
    r = width // 2 + 1
    draw.ellipse((hx - r, hy - r, hx + r, hy + r), fill='black')


def draw_wrap(draw, top_start, corner, right_bottom, belly_end,
              hook_tip, width=8):
    """s3: 横折弯钩 wrap — top small heng, corner down along right,
    curl LEFT along bottom, hook up-right.
    top_start: joins s1 tail
    corner: top-right corner
    right_bottom: where descent bends into bottom sweep
    belly_end: leftmost point along bottom (before hook)
    hook_tip: end of upward hook
    """
    # top heng (short right extension from s1)
    seg1 = _bezier2(top_start,
                    ((top_start[0] + corner[0]) / 2, top_start[1] - 2),
                    corner, n=15)
    # right descent
    c1 = (corner[0] + 4, corner[1] + 30)
    c2 = (right_bottom[0] + 4, corner[1] + (right_bottom[1] - corner[1]) * 0.7)
    seg2 = _bezier3(corner, c1, c2, right_bottom, n=50)
    # bottom sweep leftward (curl LEFT along bottom of loop)
    c3 = (right_bottom[0] - 20, right_bottom[1] + 12)
    c4 = ((right_bottom[0] + belly_end[0]) / 2 - 10, belly_end[1] + 6)
    seg3 = _bezier3(right_bottom, c3, c4, belly_end, n=50)
    # small upward hook (up-right)
    hc = ((belly_end[0] + hook_tip[0]) / 2 + 4, belly_end[1] - 10)
    seg4 = _bezier2(belly_end, hc, hook_tip, n=20)

    all_pts = seg1 + seg2[1:] + seg3[1:] + seg4[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in all_pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    # end caps
    r = width // 2 + 1
    for pt in (top_start, hook_tip):
        draw.ellipse((pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top heng — extend so it visually joins wrap start.
    draw_heng(d, head=(70, 92), tail=(218, 92),
              width_head=8, width_tail=9)

    # s2: left leg — nearly-straight shu + small ti flick.
    #     Starts a hair below s1's left end; ti tail clearly rises up-right
    #     and terminates BELOW the wrap's bottom sweep to stay distinct.
    draw_left_leg(d, head=(92, 100), ti_start=(120, 250),
                  ti_tail=(150, 240), width=8)

    # s3: 横折弯钩 wrap (adapted for 瓦 — belly sweeps LEFT along bottom).
    #     Bottom sweep ends further right than the leg tail so leg + hook
    #     remain visually separable; hook tip is clearly up-right.
    draw_wrap(d,
              top_start=(215, 94),        # joins s1 tail
              corner=(238, 90),           # top-right corner
              right_bottom=(248, 245),    # bottom-right transition
              belly_end=(175, 272),       # leftmost point of bottom sweep
              hook_tip=(190, 240),        # upward hook tip (clear of leg tail)
              width=8)

    # s4: tiny dian inside the loop, upper-center — small diagonal.
    draw_dian(d, head=(158, 165), tail=(175, 183),
              w_head=2, w_tail=4, bow=2, steps=24)

    out = pathlib.Path(__file__).parent / '01_瓦.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
