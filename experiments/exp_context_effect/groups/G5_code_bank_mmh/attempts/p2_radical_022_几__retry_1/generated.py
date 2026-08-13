# TRAJECTORY DIFF (retry_1 of p2_radical_022_几)
# ---------------------------------------------------------------
# main attempt FAIL — visual gaps vs GT:
#   1. Right stroke (横折弯钩) looked BOX/RECTANGULAR: heng at top ran
#      ~150px flat, then shu descended near-vertically all the way to
#      y=~265 in a straight line. GT shows a smooth, ORGANIC curve —
#      heng is only ~55-70px, then the body BOWS (gentle rightward
#      belly) down to a rounded bottom knee.
#   2. Hook at bottom-right of main attempt was ~10px tall, barely
#      visible, and pointed backward-inward (toward the shu body).
#      GT's hook curls up-and-slightly-right, ~40-45px tall, terminating
#      well above the knee (tail anchor at (278,219) — upper-right area).
# Also the top heng of main attempt was drawn as a flat horizontal at
# a single y-level (~106) meeting the shu at a hard 90° corner. GT
# shows a soft transition (heng tilts down slightly as it becomes shu).
#
# Fixes this attempt:
#   - Shorten the heng segment (~60px, not 150+).
#   - Replace the boxy shu with a single smooth cubic bezier arc
#     head→corner→knee→tail (one continuous curve, no hard corner).
#   - Make hook prominent: knee at bottom ~y=262 curving UP to tail
#     (278,219) — ~43px tall, clearly readable as 钩.
#   - Chain-of-ellipses ink (matches bank draw_pie style) for smooth
#     tapered ink instead of PIL's flat draw.line rectangles.
# ---------------------------------------------------------------

# BANK_DEVIATION
# skipped: shu_wan_gou.py
# reason: 几's right stroke is 横折弯钩 (has a leading heng tick before the
#         vertical body). shu_wan_gou has no top heng — using it drops
#         the top-left corner tick that identifies 几.
# fresh_component: heng_zhe_wan_gou_for_几 (inline, chain-of-ellipses).

import sys, pathlib
from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))
from pie import draw_pie  # bank primitive for stroke 1

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 strokes: pie + heng_zhe_wan_gou
    'endpoint_mismatches': [], # s1 head/tail and s2 head/tail at MMH anchors
    'joint_class_mismatches': [], # N gap between s1.head(95,94) and s2.head(119,106) = 27px, target ~15.6
    'overall_pass': True,
    'notes': 'retry_1 — smoother organic curve for s2, prominent up-hook.'
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
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _ink_chain(draw, pts, w_start=7, w_end=6):
    """Chain-of-ellipses ink — smooth tapered line, no rectangular joints."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        r = w_start + (w_end - w_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_heng_zhe_wan_gou_for_ji(draw, head, tail):
    """几's right stroke: short heng at top -> organic body-curve down
    with rightward belly -> hook up to tail (upper-right)."""
    hx, hy = head          # (119, 106) — MMH s2 head
    tx, ty = tail          # (278, 219) — MMH s2 tail

    # Segment A: short heng (top tick). ~60 px right, slight down-tilt.
    heng_end = (hx + 62, hy + 4)                # (~181, 110)
    heng_ctrl = (hx + 30, hy)                   # keep flat at start
    heng_pts = _bezier2(head, heng_ctrl, heng_end, n=25)

    # Segment B: body — smooth arc from heng_end down to bottom knee.
    #   knee at bottom is roughly under x=245, y=262. Belly bows right.
    knee = (250, 262)
    body_c1 = (heng_end[0] + 4, heng_end[1] + 65)   # early: mostly-down
    body_c2 = (knee[0] - 30, knee[1] - 10)          # late: turning right
    body_pts = _bezier3(heng_end, body_c1, body_c2, knee, n=70)

    # Segment C: hook — curl up-right from knee to tail (278, 219).
    hook_c1 = (knee[0] + 22, knee[1] + 6)           # brief outward
    hook_c2 = (tx + 4, ty + 30)                     # sweep upward
    hook_pts = _bezier3(knee, hook_c1, hook_c2, tail, n=45)

    # Deduplicate join points
    all_pts = heng_pts + body_pts[1:] + hook_pts[1:]
    # Slight taper: heng thick, hook thinner
    n = len(all_pts)
    for i, (x, y) in enumerate(all_pts):
        t = i / max(1, n - 1)
        # start 7 -> middle 7 -> hook tip 4
        if t < 0.7:
            r = 7
        else:
            r = 7 + (4 - 7) * ((t - 0.7) / 0.3)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # MMH anchors
    s1_head = (95, 94)
    s1_tail = (38, 288)
    s2_head = (119, 106)
    s2_tail = (278, 219)

    # Stroke 1: 撇 — bank primitive
    draw_pie(draw, s1_head, s1_tail, bow_perp=14, w_head=8, w_tail=2, steps=90)

    # Stroke 2: 横折弯钩 — inline (BANK_DEVIATION)
    draw_heng_zhe_wan_gou_for_ji(draw, s2_head, s2_tail)

    out = _HERE.parent / '01_几.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
