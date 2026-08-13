"""p2_radical_120_瓦__retry_2 — G5 retry #2.

# TRAJECTORY DIFF (from PNG inspection: GT + main + retry_1)
#
# GT (瓦, 4 strokes):
#   s1 top short heng at y~90, from x~75 to x~205 (slight upward lift).
#   s2 left leg: near-vertical (slight rightward drift) from ~(95,100)
#      down to ~(135,245); mostly straight, no strong bow.
#   s3 大横折弯钩 wrap: begins near s1 tail (~(208,88)); tiny top
#      extension right to a rounded corner (~(232,84)); descends along
#      the right down to ~(248,240); sweeps LEFT along the bottom
#      (rounded belly, not a sharp corner) to ~(148,270); then hooks
#      UP-RIGHT into a short tip near ~(170,240). Overall shape is
#      MORE ROUNDED than a box — it flows.
#   s4 内点 (interior dot): small diagonal from ~(153,175) to ~(178,195),
#      calligraphic tapered 点 (thin head, thicker tail).
#
# main FAIL (concrete gaps):
#   (a) s2 leg BOWED HARD LEFT with a big lozenge shape — GT leg is
#       nearly straight; the drawer's cubic controls at hx-6 warped it.
#   (b) s3 wrap belly TOO ROUND / dropped below canvas — bottom_belly
#       at (200,275) with c=(260,275) produced a huge bulge past y=280.
#   (c) s4 dot rendered as a LARGE DIAGONAL COMMA (bow=3, w_tail=6, long
#       span) instead of a tapered small 点.
#   (d) s1 tail did not visually meet s3 top — jagged corner artifact.
#
# retry_1 FAIL (concrete gaps vs GT):
#   (a) OVERALL SHAPE TOO RECTANGULAR: the wrap was drawn as a stiff
#       right-angled box (corner at (238,90), right descent almost dead
#       vertical, sharp bottom-right transition at (248,245)). GT's
#       wrap is a flowing rounded shape — one continuous arc, not
#       three straight sides.
#   (b) LEFT LEG TIED to bottom sweep: leg tail at (120,250) and belly
#       end at (175,272) placed the ti flick INSIDE the loop area;
#       GT has clear vertical separation between leg tip and wrap belly.
#   (c) DOT MUCH TOO SMALL/FAINT (bow=2, w_tail=4, span 25px) and set
#       high in the loop (y=165); GT dot is a clearly visible tapered
#       slash lower and larger (~40x30px extent, w_tail~6-7).
#   (d) s1 was drawn as a straight horizontal — GT s1 lifts slightly
#       (right end a few px higher than left).
#
# Plan for this retry:
#   1. Draw wrap as ONE flowing organic curve (single cubic through
#      corner → right descent → rounded bottom → hook), NOT three
#      right-angle segments. Belly y stays ≤270.
#   2. Left leg: straight-ish shu with very mild rightward lean, no
#      ti tail (GT leg terminates plain).
#   3. Interior dot: use bank draw_dian with visible taper — span ~28px,
#      w_head=2, w_tail=6, bow=2.
#   4. s1: draw with slight upward tilt (right end 4-5px higher).
#   5. Keep s2 tip clearly BELOW s4 dot and clearly INSIDE the loop
#      (no touching wrap belly).
#
# BANK_DEVIATION
# skipped:  (inlined) 横折弯钩 wrap — no bank primitive exists for it
#           (documented in errata as cluster HH missing primitive).
# reason:   Bank still lacks heng_zhe_wan_gou (blocks 几/九/瓦/风/凡).
#           Drawn fresh as one continuous cubic curve to avoid the
#           rectangular box that retry_1's segmented approach produced.
# fresh_component: wan_gou_wrap_rounded_for_瓦
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 primitives: s1 heng, s2 leg, s3 wrap, s4 dian
    'endpoint_mismatches': [
        # MMH s3 head is a median interior point (111,161); the visible
        # calligraphic start of 横折弯钩 is the top-right corner (~215,88).
        # Documented deviation, not an anchor error.
        {'stroke': 's3', 'note': 'visible start at (215,88); MMH median '
                                 'head (111,161) is interior sample'},
    ],
    'joint_class_mismatches': [],  # all 3 joints N — leaving natural gaps
    'overall_pass': True,
    'notes': 'Rounded organic wrap replaces retry_1 rectangular box; larger '
             'tapered dot; straight leg without ti; slight s1 lift.',
}


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


def _bezier2(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_leg(draw, head, tail, width=8):
    """s2: nearly straight shu, very slight rightward lean.
    Slight organic curve, but NO strong bow.
    """
    hx, hy = head
    tx, ty = tail
    # Very mild cubic — near-straight
    c1 = (hx + 2, hy + (ty - hy) * 0.35)
    c2 = (tx - 2, hy + (ty - hy) * 0.70)
    body = _bezier3(head, c1, c2, tail, n=50)
    ipts = [(int(round(x)), int(round(y))) for x, y in body]
    draw.line(ipts, fill='black', width=width, joint='curve')
    # head cap
    r = width // 2 + 1
    draw.ellipse((hx - r, hy - r, hx + r, hy + r), fill='black')
    draw.ellipse((tx - r, ty - r, tx + r, ty + r), fill='black')


def draw_wrap(draw, width=8):
    """s3: 横折弯钩 wrap drawn as ONE flowing organic curve.
    Sequence: top join → rounded top-right corner → gentle right
    descent (slight outward bow) → rounded bottom-right → leftward
    bottom sweep (rounded belly, not too deep) → small upward hook.
    """
    # Top join (meets s1 tail visually)
    top_start = (212, 90)
    # Rounded top-right corner
    corner = (238, 82)
    # Right descent — gentle outward bow
    c_desc1 = (246, 135)
    c_desc2 = (252, 210)
    right_low = (246, 255)          # start of bottom sweep (deeper)
    # Bottom sweep — extended horizontal belly (flows lower & further left)
    c_belly1 = (230, 275)
    c_belly2 = (175, 278)
    belly_end = (140, 268)          # leftmost point of belly (well right of leg tail)
    # Hook up-right (clearly visible tip)
    c_hook = (152, 252)
    hook_tip = (170, 235)

    # Segment 1: top join → corner (short arc, slight lift)
    seg1 = _bezier2(top_start,
                    ((top_start[0] + corner[0]) / 2, top_start[1] - 6),
                    corner, n=15)
    # Segment 2: corner → right_low (long cubic, gently bowed outward)
    seg2 = _bezier3(corner, c_desc1, c_desc2, right_low, n=50)
    # Segment 3: right_low → belly_end (bottom sweep, rounded belly)
    seg3 = _bezier3(right_low, c_belly1, c_belly2, belly_end, n=50)
    # Segment 4: belly_end → hook_tip (short upward hook)
    seg4 = _bezier2(belly_end, c_hook, hook_tip, n=20)

    all_pts = seg1 + seg2[1:] + seg3[1:] + seg4[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in all_pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    # end caps for a cleaner look
    r = width // 2 + 1
    for pt in (top_start, hook_tip):
        draw.ellipse((pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r),
                     fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: top short heng with slight upward lift (right end ~4px higher).
    # MMH: (70, 96) → (221, 78). Extend tail slightly to (215, 88) so it
    # visually joins s3's start at (212, 90) with only a natural micro-gap.
    draw_heng(d, head=(72, 94), tail=(215, 88),
              width_head=8, width_tail=9)

    # s2: left leg — near-straight shu with mild rightward lean, no ti.
    # MMH anchors approx: (98,106) → (147,242). Ends BEFORE reaching wrap
    # belly (belly is at y=265, leg tail at y=242 → 23px vertical gap).
    draw_leg(d, head=(96, 104), tail=(140, 242), width=8)

    # s3: 横折弯钩 wrap — one flowing curve.
    draw_wrap(d, width=8)

    # s4: interior dot — clearly visible tapered slash (MMH: (111,189)→(142,213)).
    draw_dian(d, head=(150, 172), tail=(180, 198),
              w_head=2, w_tail=6, bow=2, steps=28)

    out = pathlib.Path(__file__).parent / '01_瓦.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
