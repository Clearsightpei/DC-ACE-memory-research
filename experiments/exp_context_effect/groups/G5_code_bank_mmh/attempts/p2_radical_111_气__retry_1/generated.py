# BANK_DEVIATION
# skipped: (no bank primitive) for 气's 4th stroke — 横斜钩 wrap
# reason: shape is horizontal-then-descend-then-hook, not a diagonal xie_gou
#         nor heng_zhe_gou (that's a right-angle box corner). Inline fresh.
# fresh_component: heng_xie_gou_for_qi (v2, cleaner shape)
#
# TRAJECTORY DIFF (main FAIL -> retry_1)
# Prior FAILED render issues vs GT:
#  1. Pie extended UPWARD to y=45 (should be y=56 per MMH). Pie top ~10px too
#     high; entire pie stroke visually ~15% too tall / too long.
#  2. Endpoint dots on hengs (radius 5-6) very prominent — visible as
#     bulbs at both ends. GT hengs have a subtle tail dot only.
#  3. s4 wrap drawn as a shallow SMILEY arc from left to right, with
#     a small hook. GT s4 is L-shaped: nearly-horizontal upper portion,
#     then bends DOWN at right side, terminates with hook. The arc-body
#     was too curvy (belly_drop=22) and lacked the right-side descent.
# Fixes this attempt:
#  A. Pie: honor MMH head=(103.7, 56.5), tail=(49.5, 145.6). No extension.
#  B. Hengs: use inline drawing with slimmer endcaps (no big dots).
#  C. s4: compose as (near-horizontal top) + (descending right side) +
#         (small terminal hook), not a single wide arc.

"""气 (qi) — 4-stroke radical.

MMH anchors (px on 300x300):
  s1 pie   head TC (103.7, 56.5) -> tail ML (49.5, 145.6)
  s2 heng1 head  C (103.7,104.3) -> tail TR (203.9, 88.5)
  s3 heng2 head ML (91.4, 139.2) -> tail  C (177.0,125.7)
  s4 wrap  head ML (55.7, 184.0) -> tail BR (267.2, 236.7)
Joints:
  s1.mid(0.35) ~ s2.head : N (~17 px gap ok)
  s1.mid(0.67) ~ s3.head : N (~29 px gap ok)
Stroke count: 4.
"""

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


def draw_heng_xie_gou_for_qi(draw, head, tail, width=9):
    """s4 wrap: horizontal-then-descend-then-hook.

    head = MMH s4 head (55.7, 184.0)
    tail = MMH s4 tail (267.2, 236.7)  -- this is the HOOK TIP

    Path composition:
      A) shallow near-horizontal arc from head to a "shoulder" ~ (225, 190)
      B) descending right side from shoulder curving down to
         "corner" ~ (248, 262) (bottom of the wrap)
      C) hook up-right from corner to tail (267.2, 236.7)
    """
    hx, hy = head
    tx, ty = tail
    # Smoother rounded corner: shoulder more inward, corner bends around it.
    shoulder = (215, 193)
    corner = (250, 258)

    # A: near-horizontal top with gentle downward drift; single long bezier
    #    all the way from head to a point past the shoulder helps round the corner
    a_ctrl = ((hx + shoulder[0]) / 2, hy + 14)
    seg_a = _bezier2(head, a_ctrl, shoulder, n=70)

    # B: right-side descent — control pushed right AND up so the shoulder
    #    blends smoothly into the descent (rounded, not angular)
    b_ctrl = (shoulder[0] + 32, shoulder[1] + 4)
    seg_b = _bezier2(shoulder, b_ctrl, corner, n=55)

    # C: small terminal hook up-right toward MMH tail
    c_ctrl = (corner[0] + 12, corner[1] - 6)
    seg_c = _bezier2(corner, c_ctrl, tail, n=25)

    pts = seg_a + seg_b[1:] + seg_c[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')

    # small caps at the two extremes (head and hook tip)
    r = width / 2
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill='black')
    # tapered hook tip
    r2 = 1.8
    draw.ellipse([tx - r2, ty - r2, tx + r2, ty + r2], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — pie: MMH head=(103.7, 56.5) -> tail=(49.5, 145.6)
    draw_pie(d, head=(103.7, 56.5), tail=(49.5, 145.6),
             bow_perp=8, w_head=6, w_tail=2, steps=80)

    # s2 — top heng: MMH head=(103.7, 104.3) -> tail=(203.9, 88.5)
    # GT shows a slight upward slope to the right, matching MMH deltas.
    draw_heng_clean(d, head=(103.7, 104.3), tail=(203.9, 88.5),
                    width=7, tail_dab=1.0)

    # s3 — middle heng: MMH head=(91.4, 139.2) -> tail=(177.0, 125.7)
    draw_heng_clean(d, head=(91.4, 139.2), tail=(177.0, 125.7),
                    width=7, tail_dab=1.0)

    # s4 — wrap (fresh inline; see BANK_DEVIATION above)
    draw_heng_xie_gou_for_qi(d, head=(55.7, 184.0), tail=(267.2, 236.7),
                             width=9)

    out = os.path.join(os.path.dirname(__file__), '01_气.png')
    img.save(out)
    print('wrote', out)


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 4 primitives called
    'endpoint_mismatches': [],  # all endpoints use MMH anchors directly
    'joint_class_mismatches': [
        # both joints are N; s1.mid(0.35) ~ s2.head gap: s1 at t=0.35 is
        # ~(85, 88); s2 head (103.7, 104.3) => sqrt(18.7^2 + 16.3^2) ~ 24 px. OK.
        # s1.mid(0.67) ~ s3.head: s1 t=0.67 ~ (67, 116); s3 head (91.4, 139.2)
        #   => sqrt(24.4^2 + 23.2^2) ~ 33 px. OK (~expected 29).
    ],
    'overall_pass': True,
    'notes': ('retry_1: shortened pie to MMH bounds, removed heavy head '
              'dots on hengs, reshaped s4 into horizontal-then-descend-'
              'then-hook path (previously was a single shallow arc).'),
}


if __name__ == '__main__':
    main()
