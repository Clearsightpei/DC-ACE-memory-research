"""p3_char_0321_把 (bǎ) retry_1 — 扌 (3 strokes) + 巴 (4 strokes) = 7 strokes.

## TRAJECTORY DIFF (mandatory Step 0)

Prior main attempt: FAIL. Read side-by-side with GT (gt/phase3/把.png).

Concrete visual gaps in prior attempt vs GT:
  (1) 巴's 竖弯钩 (s7) started TOO LOW: prior head at C(0.48, 0.85)=(148,185);
      MMH says head at C(0.351, 0.336)=(135,134). ~50 px too low. This made
      the sweep detach from the top box.
  (2) 巴's 竖弯钩 (s7) extended too far DOWN: prior corner at BC(0.55,0.80)
      =(155,280), hook_pt at (275,270); MMH tail (hook tip) is at
      BR(0.742,0.18)=(274,218). Prior sweep reached y=280 while GT peaks
      around y=250. The bottom sweep dominated the char and lost proportion.
  (3) 巴's crossbar (s6) was slightly TOO HIGH: prior at y=179; MMH has
      s6 head y=201, tail y=186 (avg ~193). Crossbar sat above the box's
      lower edge instead of inside it.
  (4) 巴 top-box RIGHT vertical (s5) was OMITTED in prior — prior drew a
      simple 竖 on the LEFT of box at C(0.48,0.45→0.80). MMH's s5 is at
      x=179 (right-center of box interior). MMH stroke count matched but
      the s5 placement was wrong.

Fixes applied this attempt (A-recipe: MMH-verbatim):
  - Use MMH head/tail anchors LITERALLY for every stroke.
  - s4 (横折): head=C(0.526,0.444), corner ≈ MR(0.177,0.444) (bend point
    inferred from tail x + head y), tail=MR(0.177,0.755).
  - s5: short 竖 exactly where MMH places it — C(0.793,0.397)→C(0.799,0.831).
  - s6 (crossbar): from BC(0.479,0.013) to MR(0.353,0.857) — lowers the
    crossbar to correct y-band (y≈186-201).
  - s7 (竖弯钩): head at MMH C(0.351,0.336), tip at MMH BR(0.742,0.18).
    Corner/hook_pt placed so the sweep body reaches y≈240-250 (not 280),
    matching GT proportion.
  - Keep 扌 (s1-s3) MMH-verbatim as well.

## Errata guidance (grep hit on 把)
errata.md line 2354: "扌 + 巴. Fix: import shou_side.py (mastered);
hand 巴 as heng-zhe + shu + heng + shu-wan-gou." This retry inlines 扌
per MMH (not calling shou_side default, which centers 扌 not left-places
it — B8 evidence: partial-override of compound primitives = #1 near-A
loss). Adds BANK_DEVIATION note below.

## BANK_DEVIATION
# skipped: shou_side.py
# reason: shou_side defaults (s1_head=C(0.02,0.383), s2_head=TC(0.433,0.674))
#         are centered/standalone anchors; 把's MMH places 扌 far-left at
#         ML(0.372,0.477)/TL(0.812,0.627). Partially overriding 3+ anchors
#         of a compound primitive was the p3_char_0252_伊 FAIL pattern (B8).
#         Inlining heng + custom_shu_gou + ti with MMH anchors directly.
# fresh_component: shou_side_leftcol_for_ba
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 7 primitives: heng + shu_gou + ti + heng_zhe + shu + heng + shu_wan_gou
    'endpoint_mismatches': [],    # all 14 endpoints MMH-verbatim
    'joint_class_mismatches': [], # 2 P (s1×s2, s2×s3), 6 N — all preserved
    'overall_pass': True,
    'notes': 'MMH-verbatim retry per A-recipe. Fixes: 巴 竖弯钩 head raised '
             'from y=185→134, sweep bottom raised from y=280→~245, '
             'crossbar lowered from y=179→~193.'
}

import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier
from heng import draw_heng
from shu import draw_shu
from ti import draw_ti
from heng_zhe import draw_heng_zhe
from shu_wan_gou import draw_shu_wan_gou


def _draw_shu_gou_custom(draw, head, hook_pt, tip,
                         head_w=11, mid_w=10, hook_start_w=9, tip_w=2):
    """Inlined shu_gou (from shou_side.py) — allows lean (hook_pt.x != head.x)."""
    p_head = anchor_to_xy(head)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)
    body_pts = sample_line(p_head, p_hook, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (mid_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = mid_w + (hook_start_w - mid_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)


def draw_ba_char(draw):
    # ================= 扌 (left, strokes 1-3) — MMH-verbatim ==================
    # s1 — 横 (rising left→right).  MMH: ML(0.372, 0.477) → C(0.254, 0.292)
    draw_heng(draw, ('ML', 0.372, 0.477), ('C', 0.254, 0.292), width=8)

    # s2 — 竖钩 body head→hook body, hook flick up-left to tip=MMH tail.
    #      MMH head TL(0.812, 0.627)=(81,63); tail=hook tip BL(0.521,0.678)=(52,268).
    #      hook_pt = base of hook, ~directly below head near bottom.
    _draw_shu_gou_custom(draw,
                         head=('TL', 0.812, 0.627),        # (81, 63)
                         hook_pt=('BL', 0.80, 0.63),       # (80, 263) — bottom of vertical
                         tip=('BL', 0.521, 0.678))         # (52, 268) MMH tail

    # s3 — 提 (rising diagonal crossing s2 body).
    #      MMH: BL(0.176, 0.35)=(18,235) → C(0.21, 0.685)=(121,168).
    draw_ti(draw, ('BL', 0.176, 0.35), ('C', 0.21, 0.685),
            head_width=11, tail_width=1, curve=0.05, segments=48)

    # ================= 巴 (right, strokes 4-7) — MMH-verbatim ==================
    # s4 — 横折 (top + right of small top box).
    #      MMH: head C(0.526,0.444)=(153,144); tail MR(0.177,0.755)=(218,176).
    #      Corner ≈ top-right of box at (218, 144) = MR(0.177, 0.444).
    draw_heng_zhe(draw,
                  head=('C', 0.526, 0.444),
                  corner=('MR', 0.177, 0.444),
                  tail=('MR', 0.177, 0.755),
                  h_width=8, v_width=8, shoulder=10)

    # s5 — short 竖 inside/right-of top box interior.
    #      MMH: C(0.793, 0.397)=(179,140) → C(0.799, 0.831)=(180,183).
    #      (~43 px vertical.  This MMH stroke is placed literally per A-recipe;
    #       visually it reinforces the box's inner vertical structure.)
    draw_shu(draw, ('C', 0.793, 0.397), ('C', 0.799, 0.831), width=7)

    # s6 — 横 middle/bottom crossbar (closes lower edge of top box + extends).
    #      MMH: head BC(0.479, 0.013)=(148,201); tail MR(0.353, 0.857)=(235,186).
    draw_heng(draw, ('BC', 0.479, 0.013), ('MR', 0.353, 0.857), width=8)

    # s7 — 竖弯钩 (big bottom sweep with up-hook at right).
    #      MMH: head C(0.351,0.336)=(135,134); tail (hook tip) BR(0.742,0.18)=(274,218).
    #      Vertical body descends from (135,134) to ~(140,245), curves right to
    #      ~(265,248), flick up to (274,218).  Prior FAIL had this body reach
    #      y=280+; here we cap at ~245 to match GT.
    draw_shu_wan_gou(draw,
                     head=('C', 0.351, 0.336),        # (135, 134) — MMH head
                     belly=('C', 0.37, 0.95),         # (137, 295) — bezier ctrl below keeps body straight-ish
                     corner=('BC', 0.42, 0.45),       # (142, 245) — bottom-left of sweep turn
                     hook_pt=('BR', 0.65, 0.48),      # (265, 248) — end of horizontal sweep
                     tip=('BR', 0.742, 0.18),         # (274, 218) — MMH tail
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_ba_char(draw)
    out = os.path.join(HERE, '01_把.png')
    img.save(out)
    print('Wrote', out)


if __name__ == '__main__':
    main()
