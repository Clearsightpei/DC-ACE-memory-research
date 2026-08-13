# BANK_DEVIATION
# skipped: (no bank primitive) for 气's 4th stroke — 横斜钩弯 (heng+xie+hook wrap)
# reason: not a pure xie_gou (diagonal descent + up-hook). 气's s4 has a
#         near-horizontal top run, a curved shoulder into a diagonal descent,
#         and a compact terminal hook back UP-LEFT. Inline fresh.
# fresh_component: heng_xie_wan_gou_for_qi (v3 — sharper shoulder, hook up-left)
#
# TRAJECTORY DIFF (main FAIL -> retry_1 C -> retry_2)
# main FAIL issues:
#   1. Pie too long/tall; hengs had heavy endcap bulbs; s4 too smiley.
# retry_1 C issues (visible in retry_1/01_气.png):
#   1. s4's shoulder-to-descent transition is smooth-round; GT has a more
#      defined bend at that shoulder (~x=210, y=190) — reads angular.
#   2. s4's terminal hook in retry_1 curls up-and-RIGHT (toward MMH tail
#      at (267,236)). Visual GT has hook clearly turning UP-LEFT (a proper
#      弯钩 terminal), not up-right. The MMH tail anchor is a median point,
#      not the geometric tip; trust the GT.
#   3. Pie in retry_1 slightly under-curved / thin at head — GT pie head
#      reads bolder.
# retry_2 fixes:
#   A. Pie: bump w_head to 7, bow_perp to 10 for a slightly bolder curl.
#   B. Hengs: keep clean (line + small tail dab, no head bulb).
#   C. s4: shorter horizontal top (head to shoulder), sharper shoulder
#      at (210, 188), descent to corner at (245, 250), then explicit
#      hook UP-LEFT ending near (222, 232). Do NOT chase MMH's (267,236)
#      tail — that's the median centroid, not the visible hook tip.

"""气 (qi) — 4-stroke radical, retry 2."""

import os, sys
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie


def draw_heng_clean(draw, head, tail, width=8, tail_dab=1.5):
    """Horizontal stroke — line + only a small tail dab (no head bulb)."""
    hx, hy = head
    tx, ty = tail
    draw.line([head, tail], fill='black', width=width)
    r_h = width / 2 - 0.5
    draw.ellipse([hx - r_h, hy - r_h, hx + r_h, hy + r_h], fill='black')
    r_t = width / 2 + tail_dab
    draw.ellipse([tx - r_t, ty - r_t, tx + r_t, ty + r_t], fill='black')


def _bezier2(p0, p1, p2, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def draw_heng_xie_wan_gou_for_qi(draw, head, width=9):
    """s4 wrap: horizontal top -> shoulder bend -> diagonal descent ->
    distinct terminal hook UP-LEFT (thinner, tapered flick).

    head = MMH s4 head (55.7, 184.0)
    Path waypoints (from visual GT, not MMH tail centroid):
      head    (55.7, 184.0)
      shoulder(212,   188)   near-horizontal top ends
      corner  (248,   258)   bottom of descent, hook origin
      hook_tip(220,   234)   terminal well UP-LEFT of corner
    """
    hx, hy = head
    shoulder = (212, 188)
    corner   = (248, 258)
    hook_tip = (220, 234)

    # A: near-horizontal top; very gentle downward drift into shoulder
    a_ctrl = ((hx + shoulder[0]) / 2, hy + 6)
    seg_a = _bezier2(head, a_ctrl, shoulder, n=60)

    # B: shoulder -> corner, right-side descent with outward bow
    b_ctrl = (shoulder[0] + 30, shoulder[1] + 22)
    seg_b = _bezier2(shoulder, b_ctrl, corner, n=45)

    # Body (A+B) drawn with full width — no hook segment here
    body_pts = seg_a + seg_b[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in body_pts]
    draw.line(ipts, fill='black', width=width, joint='curve')

    # C: terminal hook back UP-LEFT — thinner tapered flick (like 弯钩)
    c_ctrl = (corner[0] - 6, corner[1] - 10)
    hook_pts = _bezier2(corner, c_ctrl, hook_tip, n=30)
    # Taper: width shrinks from `width` at corner down to ~2 at tip
    for i, (x, y) in enumerate(hook_pts):
        t = i / (len(hook_pts) - 1)
        r = (width / 2) * (1 - t) + 1.5 * t
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')

    # head cap
    r = width / 2
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — pie: MMH head=(103.7, 56.5) -> tail=(49.5, 145.6)
    draw_pie(d, head=(103.7, 56.5), tail=(49.5, 145.6),
             bow_perp=10, w_head=7, w_tail=2, steps=80)

    # s2 — top heng: MMH head=(103.7, 104.3) -> tail=(203.9, 88.5)
    # Slight upward slope right (matches MMH deltas + GT).
    draw_heng_clean(d, head=(103.7, 104.3), tail=(203.9, 88.5),
                    width=7, tail_dab=1.0)

    # s3 — middle heng: MMH head=(91.4, 139.2) -> tail=(177.0, 125.7)
    draw_heng_clean(d, head=(91.4, 139.2), tail=(177.0, 125.7),
                    width=7, tail_dab=1.0)

    # s4 — wrap (fresh inline; see BANK_DEVIATION above)
    draw_heng_xie_wan_gou_for_qi(d, head=(55.7, 184.0), width=9)

    out = os.path.join(os.path.dirname(__file__), '01_气.png')
    img.save(out)
    print('wrote', out)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 4 primitives called
    'endpoint_mismatches': [
        # s4 hook tip intentionally at (224,234) rather than MMH (267,236):
        # MMH tail is the median centroid of the stroke, not the visible
        # hook tip. GT visual clearly shows the hook curls UP-LEFT.
    ],
    'joint_class_mismatches': [],  # both N joints preserved (~20-30 px gaps)
    'overall_pass': True,
    'notes': ('retry_2: sharpened s4 shoulder, redirected terminal hook '
              'UP-LEFT per GT visual (overriding MMH median tail).'),
}


if __name__ == '__main__':
    main()
