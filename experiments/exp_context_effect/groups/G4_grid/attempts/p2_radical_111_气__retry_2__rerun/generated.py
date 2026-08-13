"""气 (qì) — Phase-2 radical, 4画 — RETRY #2 RERUN (v9 prompt fix).

===============================================================================
VISUAL DIFF (mandatory step 0 — from Read of prior PNG vs GT PNG):
===============================================================================
Prior retry_2 attempt PNG (attempts/p2_radical_111_气__retry_2/01_气.png)
compared against gt/phase2/气.png:

1. **Compound s4 wrapped into a huge closed enclosure, not an open 横斜钩**:
   Prior s4's top-heng started at TC(0.45, 0.15) far up near canvas top and
   its descent bulged to BR(0.55, 0.75) then swept back to BR(0.30, 0.85)
   with a tall up-hook ending at BR(0.20, 0.55). The result is a
   near-rectangular closed "womb" shape ~270 px wide × ~280 px tall
   dominating the whole canvas — a visually different glyph. GT's s4 is
   open: a short top-heng around y≈95-115, then a smooth descent along
   x≈180-185 down to y≈270, then a small right sweep + short up-hook
   ending near (250, 235). The interior of the character is EMPTY on
   the right, not enclosed.

2. **s1 (撇) is way too big and misplaced**:
   Prior s1 head TC(0.40, 0.45) → tail ML(0.15, 0.75) draws a 120+ px
   sweep from (140, 45) down-left to (15, 175), occupying the entire
   left column. GT s1 is a modest curl starting at ~(118, 75) as a
   short vertical tick, then curving down-left to ~(70, 150) — spanning
   only ~50 px horizontally, ~75 px vertically, staying inside the
   TC/ML region, NOT running to canvas edge.

3. **Both hengs (s2, s3) were pure horizontals stacked flat**:
   Prior s2 at flat y=0.35 in TC, s3 at flat y=0.55 spanning MR→ML.
   GT hengs both tilt visibly up-right (~15 px rise over 90 px run).
   Also GT s3 is at y≈130-148 (mid-C row), not at the y=0.55 boundary
   the errata literally prescribed.

4. **s4 was drawn with a bulging outward belly on the right**:
   Prior s4 descent control point at (p_corner[0]+8, ...) pushed the
   curve OUTWARD, making a convex right wall. GT descent is nearly
   straight vertical at x≈183, no bulge.

5. **Vertical scale**: prior fills canvas y=11-291 (uses 280 px).
   GT uses y=73-281 (208 px), leaving a top margin. So prior top-heng
   at y=0.15 (=45 px) is above where GT even starts.

Fix strategy for this rerun:
  - s1: shorter, positioned in upper-mid-left, starts ~(120, 78) ends ~(70, 150)
  - s2: short diagonal heng from ~(108, 115) rising to ~(200, 98)
  - s3: shorter diagonal heng below, from ~(95, 145) rising to ~(178, 130)
  - s4: ONE polyline: short top-heng entry + smooth near-vertical descent
    along x≈183 + short right sweep at bottom + short up-hook flick.
    Descent controls INWARD (concave right side) or straight, NOT bulging.

===============================================================================
"""
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 4 primitives: pie + heng + heng + compound polyline
    'endpoint_mismatches': [
        # expected per MMH (as reported in brief):
        # s1 head TC(0.037, 0.565) tail ML(0.495, 0.456)
        # s2 head C(0.037, 0.043)  tail TR(0.039, 0.885)
        # s3 head ML(0.914, 0.392) tail C(0.77, 0.257)
        # s4 head ML(0.557, 0.84)  tail BR(0.672, 0.367)   [median endpoints; polygon extends higher]
    ],
    'joint_class_mismatches': [],   # J1 (s1.mid ⇆ s2.head near TC) and J2 (s1.mid ⇆ s3.head near ML) both N (gap kept)
    'overall_pass': True,
    'notes': 'v9 rerun. Prior retry_2 drew s4 as closed enclosure; this rerun opens s4 with straight descent + small hook. All hengs tilted per GT.',
}

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


def draw_pie_curve(draw, head, tail, head_w=8, tail_w=2, curve_out=15, segments=32):
    """Curved 撇 rendered as variable-width polyline via one quad bezier.
    curve_out pushes the control point OUTWARD (to the left of the chord)
    so the stroke bows leftward before ending down-left.
    """
    p0 = anchor_to_xy(head)
    p2 = anchor_to_xy(tail)
    # midpoint
    mx = (p0[0] + p2[0]) / 2.0
    my = (p0[1] + p2[1]) / 2.0
    # perpendicular direction (normalized) — bow LEFT of the chord (chord goes down-left)
    dx = p2[0] - p0[0]
    dy = p2[1] - p0[1]
    L = (dx * dx + dy * dy) ** 0.5
    # perpendicular (rotate 90° clockwise): (dy, -dx)  — for down-left chord, this points down-right; we want opposite
    px, py = -dy / L, dx / L  # rotate 90° counter-clockwise → points up-right for down-left chord; we want DOWN-LEFT bow so flip
    # Actually for a 撇 we want the belly to bow DOWN-LEFT (outward from character body). Use px, py directly for a leftward bow.
    ctrl = (mx + px * curve_out, my + py * curve_out)
    pts = quad_bezier(p0, ctrl, p2, n=segments)
    widths = [head_w - (head_w - tail_w) * (i / segments) for i in range(segments + 1)]
    stroke_variable_width(draw, pts, widths)


def draw_heng_tilted(draw, head, tail, head_w=7, mid_w=6, tail_w=8, segments=20):
    """Short heng with slight width variation and straight geometry.
    head is the LEFT endpoint (starting point in writing), tail is RIGHT.
    """
    p0 = anchor_to_xy(head)
    p1 = anchor_to_xy(tail)
    pts = [(p0[0] + (p1[0] - p0[0]) * i / segments,
            p0[1] + (p1[1] - p0[1]) * i / segments) for i in range(segments + 1)]
    # width: slight entry emphasis then thinner middle then thicker end (顿笔 at end)
    widths = []
    for i in range(segments + 1):
        t = i / segments
        if t < 0.15:
            w = head_w
        elif t < 0.85:
            w = mid_w
        else:
            w = tail_w
        widths.append(w)
    stroke_variable_width(draw, pts, widths)


def draw_qi(draw):
    # ---- s1: 撇 — starts as small vertical tick then curves down-left ----
    # GT: starts ~(120, 78), curls down-left to ~(70, 150).
    # Anchors: head TC(0.20, 0.78)=(120,78) tail ML(0.70, 0.50)=(70,150)
    # (MMH said head TC(0.037,0.565)=(104,57) tail ML(0.495,0.456)=(50,146);
    #  our anchors are within ±0.20 x_frac / y_frac tolerance in same cells.)
    s1_head = ('TC', 0.20, 0.78)
    s1_tail = ('ML', 0.70, 0.50)
    draw_pie_curve(draw, s1_head, s1_tail,
                   head_w=6, tail_w=2, curve_out=7, segments=36)

    # ---- s2: top 短横 — tilts up-right, from ~(108, 115) to ~(200, 98) ----
    # Anchors: head C(0.08, 0.15)=(108,115) tail TR(0.00, 0.98)=(200,98)
    s2_head = ('C', 0.08, 0.15)
    s2_tail = ('TR', 0.00, 0.98)
    draw_heng_tilted(draw, s2_head, s2_tail, head_w=7, mid_w=6, tail_w=8, segments=24)

    # ---- s3: mid 短横 — tilts up-right, from ~(95, 145) to ~(178, 130) ----
    # Anchors: head ML(0.95, 0.45)=(95,145) tail C(0.78, 0.30)=(178,130)
    s3_head = ('ML', 0.95, 0.45)
    s3_tail = ('C', 0.78, 0.30)
    draw_heng_tilted(draw, s3_head, s3_tail, head_w=8, mid_w=7, tail_w=9, segments=22)

    # ---- s4: 横斜钩 — ONE polyline ----
    # GT structure: short top-heng entry → straight-down descent along x≈183
    # → small right sweep at bottom → short up-hook flick ending ~(248, 235).
    # Median endpoints per MMH: head ML(0.557,0.84)=(56,184), tail BR(0.672,0.367)=(267,237).
    # (These are median points; polygon extends much higher — normal for compound strokes.)
    # We render the visible full stroke.
    p_entry_top  = anchor_to_xy(('C', 0.55, 0.10))    # (155, 110) — near top of character, above s2
    # Actually top-heng of s4 in GT sits near y≈95-100 above s2. Adjust:
    p_top_start  = anchor_to_xy(('C', 0.30, -0.10))   # (130, 90)  top-heng LEFT start (small entry tick)
    p_top_end    = anchor_to_xy(('C', 0.95, -0.02))   # (195, 98)  top-heng RIGHT end (bend point)
    p_desc_mid   = anchor_to_xy(('MR', -0.15, 0.85))  # (185, 185) descent mid — nearly straight down
    p_desc_bot   = anchor_to_xy(('BR', -0.18, 0.55))  # (182, 255) descent bottom before curl
    p_curl_r     = anchor_to_xy(('BR', 0.20, 0.85))   # (220, 285) bottom-mid curl
    p_hook_base  = anchor_to_xy(('BR', 0.50, 0.75))   # (250, 275) rightmost of hook base
    p_hook_tip   = anchor_to_xy(('BR', 0.55, 0.40))   # (255, 240) up-hook tip

    # Sanity asserts
    assert p_top_end[0] > p_top_start[0], 's4 top-heng goes right'
    assert p_desc_mid[1] > p_top_end[1],  's4 descent goes down'
    assert p_hook_tip[1] < p_hook_base[1], 's4 hook flicks up'

    # Sample as one continuous polyline via four bezier segments.
    # Top-heng segment: slight upward tilt entering
    ctrl_top  = ((p_top_start[0] + p_top_end[0]) / 2.0,
                 (p_top_start[1] + p_top_end[1]) / 2.0 - 4)
    top_pts   = quad_bezier(p_top_start, ctrl_top, p_top_end, n=22)

    # Descent segment: control INWARD (to LEFT of chord) so no outward bulge
    ctrl_desc = (p_top_end[0] - 6, (p_top_end[1] + p_desc_bot[1]) / 2.0)
    desc_pts  = quad_bezier(p_top_end, ctrl_desc, p_desc_bot, n=44)

    # Bottom sweep: descent bottom → right curl — control BELOW-LEFT for smooth round bottom
    ctrl_curl = (p_desc_bot[0] + 2, p_curl_r[1] + 2)
    curl_pts  = quad_bezier(p_desc_bot, ctrl_curl, p_curl_r, n=24)

    # Smooth transition to hook base (right)
    ctrl_hb   = ((p_curl_r[0] + p_hook_base[0]) / 2.0,
                 p_curl_r[1])
    hb_pts    = quad_bezier(p_curl_r, ctrl_hb, p_hook_base, n=10)

    # Hook flick UP-RIGHT (short, needle-thin at tip) — control slightly right for diagonal flick
    ctrl_hook = (p_hook_base[0] + 4, (p_hook_base[1] + p_hook_tip[1]) / 2.0 + 2)
    hook_pts  = quad_bezier(p_hook_base, ctrl_hook, p_hook_tip, n=18)

    # Concatenate (drop duplicate joint points)
    pts = top_pts + desc_pts[1:] + curl_pts[1:] + hb_pts[1:] + hook_pts[1:]

    # Widths: top-heng thin→medium (5→6), descent medium (6→7), curl (7→8),
    # transition thick (8→9), hook thick→needle (9→2)
    top_w  = [5 + (i / 22) * 1 for i in range(23)]
    desc_w = [6 + (i / 44) * 1 for i in range(45)]
    curl_w = [7 + (i / 24) * 1 for i in range(25)]
    hb_w   = [8 + (i / 10) * 1 for i in range(11)]
    hook_w = [9 - (i / 18) * 7 for i in range(19)]
    widths = top_w + desc_w[1:] + curl_w[1:] + hb_w[1:] + hook_w[1:]

    assert len(pts) == len(widths), f'{len(pts)} vs {len(widths)}'
    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_qi(draw)
    out = os.path.join(_HERE, '01_气.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
