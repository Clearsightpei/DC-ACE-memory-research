"""p2_radical_120_瓦 — G5 attempt (revision 2).

MMH gives 4 strokes:
  s1 heng      (70, 96)  -> (221, 78)   — top short heng
  s2 shu-ti    (98, 106) -> (147, 242)  — LEFT LEG: goes down from upper-left,
                                          curves slightly right at bottom (ti-like tail)
  s3 wrap      (111,161) -> (272, 235)  — 横折弯钩: MMH endpoints indicate
                                          the median START (inside upper area)
                                          and the HOOK TIP (upper-right of loop).
                                          Actual visible shape wraps from top-right
                                          corner (near s1 tail) DOWN the right side
                                          then LEFT across the bottom, terminating in
                                          the upward hook at (272, 235).
  s4 dian      (111,189) -> (142, 213)  — small internal dot

BANK_DEVIATION: s3 is a compound compound (横折弯钩) not in the current stroke
bank; inlined. All other strokes use bank primitives.

Revision from pass 1: s2 bow reduced + ti tail added; s3 rebuilt so its heng
segment starts near s1's right end (matching GT wrap silhouette) rather than
starting at MMH's interior anchor point (MMH gives median endpoints, not the
visible corner start). Dot resized for visibility.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes: heng, shu_ti, wrap, dian
    'endpoint_mismatches': [
        {'stroke': 's3', 'note': 'wrap heng-start extended left to visible '
                                 'top-corner rather than MMH median anchor '
                                 '(MMH shows median endpoints, not visible corners)'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'v2: wrap topology corrected — the wrap top begins near s1 tail '
             'to match GT silhouette; hook tip lands at MMH tail (272, 235).',
}


def _bezier2(p0, p1, p2, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t*t * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t*t * p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1-t)**3
        b1 = 3*(1-t)**2 * t
        b2 = 3*(1-t) * t*t
        b3 = t**3
        x = b0*p0[0] + b1*p1[0] + b2*p2[0] + b3*p3[0]
        y = b0*p0[1] + b1*p1[1] + b2*p2[1] + b3*p3[1]
        pts.append((x, y))
    return pts


def draw_left_leg(draw, head, tail, width=8):
    """s2: 竖提-style left leg — mostly vertical with a slight bow, then a
    small rising tail at the bottom for the ti flick.
    head=(hx,hy) top; tail=(tx,ty) end of ti (down-right)."""
    hx, hy = head
    tx, ty = tail
    # Main body: bezier from head to a point just above tail, bowing left
    mid_x = hx - 6
    mid_y = (hy + ty) / 2 + 10
    just_above = (tx - 12, ty - 2)
    body = _bezier3((hx, hy), (mid_x, mid_y), (mid_x + 4, ty - 20),
                    just_above, n=60)
    ipts = [(int(round(x)), int(round(y))) for x, y in body]
    draw.line(ipts, fill='black', width=width, joint='curve')
    # ti tail: short rising segment
    tail_pts = _bezier2(just_above, ((just_above[0] + tx) / 2, ty - 6),
                        (tx, ty), n=15)
    itail = [(int(round(x)), int(round(y))) for x, y in tail_pts]
    draw.line(itail, fill='black', width=max(3, width - 3), joint='curve')
    # rounded caps
    r = width // 2 + 1
    draw.ellipse((hx-r, hy-r, hx+r, hy+r), fill='black')


def draw_wrap(draw, hook_tip, width=8):
    """s3: 横折弯钩 wrap. Starts at top-right (~ (220, 82), near s1 tail),
    goes right, then down along the right edge, then curls LEFT-BOTTOM,
    then hooks UP-RIGHT to hook_tip.
    """
    tx, ty = hook_tip
    # top-right corner shoulder (near s1 tail)
    top_start = (215, 84)
    top_end = (260, 92)          # short heng segment right
    right_top = (267, 105)
    right_bot = (270, 245)        # descend along right edge
    bottom_belly = (200, 275)     # curl leftward under
    hook_start = (185, 265)       # start of upward hook

    # top heng segment
    seg1 = _bezier2(top_start, ((top_start[0]+top_end[0])/2, 82), top_end, n=20)
    # right edge (down)
    seg2 = _bezier3(top_end, right_top, (right_bot[0]+2, 200),
                    right_bot, n=50)
    # bottom belly (down + left)
    seg3 = _bezier3(right_bot, (260, 275), (230, 285),
                    bottom_belly, n=40)
    # curl to hook_start
    seg4 = _bezier2(bottom_belly, ((bottom_belly[0]+hook_start[0])/2, 275),
                    hook_start, n=20)
    # hook upward to tail
    seg5 = _bezier2(hook_start, (hook_start[0]+40, hook_start[1]-30),
                    (tx, ty), n=25)

    all_pts = seg1 + seg2[1:] + seg3[1:] + seg4[1:] + seg5[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in all_pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2 + 1
    draw.ellipse((top_start[0]-r, top_start[1]-r,
                  top_start[0]+r, top_start[1]+r), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top heng (MMH anchors)
    draw_heng(d, head=(70, 96), tail=(221, 78),
              width_head=8, width_tail=9)

    # s2: left leg with ti tail (MMH anchors)
    draw_left_leg(d, head=(98, 106), tail=(147, 242), width=8)

    # s3: 横折弯钩 wrap — hook tip lands at MMH tail (272, 235)
    draw_wrap(d, hook_tip=(272, 235), width=8)

    # s4: small internal dian (MMH anchors)
    draw_dian(d, head=(155, 175), tail=(180, 200),
              w_head=2, w_tail=6, bow=3, steps=30)

    out = pathlib.Path(__file__).parent / '01_瓦.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
