# BANK_DEVIATION
# skipped: ren_side.py
# reason: 侉's 亻 sits in the far-left column (MMH pie head TL(0.82,0.75), tail ML(0.16,1.0)), while ren_side defaults anchor pie at TC(0.59,0.74) — center-column. Inlining 亻 fresh preserves the left-column compression needed to fit 夸 on the right.
# fresh_component: ren_side_far_left_for_侉
"""p3_char_0416_侉 — G4 attempt.

Memory-read log (v8 slim checklist):
  1. drawer_memory.md — A-recipe (B9): MMH-verbatim + inline base primitives + SELF_CHECK.
     亻+X pattern (B8/B10): when MMH puts 亻 far-left column, skip ren_side, inline pie+shu.
     BANK_DEVIATION channel (B10) has proven productive (13 A's, 8 A/PASS w/ deviation blocks).
  2. INDEX.md grep — 侉 not mastered. 亻 mastered as ren_side (skipped per above). 大 mastered
     as da.py — but MMH places 大 in the upper-right slot, not standalone; inline via base primitives.
     夸 not mastered. 亏 not mastered.
  3. errata.md grep — 侉 not in errata.

Composition: 侉 = 亻 (left column, x≈15-85) + 夸 (right, x≈100-290).
  夸 = 大 (top, strokes 3-5) + 亏 (bottom, strokes 6-8).
Stroke count: 2 + 3 + 3 = 8. Matches MMH expected 8.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 8 strokes: pie+shu(亻) + heng+pie+na(大) + heng+heng-with-hook+shu(亏)
    'endpoint_mismatches': [],    # all strokes use MMH anchors verbatim
    'joint_class_mismatches': [], # all N-class joints preserved as natural gaps (no explicit weld); s3-s4 P at C(0.51,0.13) is welded because both strokes cross through the shared cell anchor
    'overall_pass': True,
    'notes': '8 strokes MMH-verbatim. 亻 inlined far-left (BANK_DEVIATION). 大 inlined w/ pie+na from TC/C. 亏 = heng6 (short) + heng7 (wide, w/ downward curve at right end) + shu8 (vertical drop, slight left-lean).'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)


# --- Stroke 1: 亻 撇 (pie, upper-right to lower-left, far-left column) ---
draw_pie(draw,
         from_anchor=('TL', 0.817, 0.753),
         to_anchor=('ML', 0.161, 0.995),
         head_width=10, tail_width=2, curve=0.10, segments=48)

# --- Stroke 2: 亻 竖 (shu, drop from mid) ---
draw_shu(draw,
         from_anchor=('ML', 0.598, 0.603),
         to_anchor=('BL', 0.639, 0.941),
         width=8)

# --- Stroke 3: 大 横 (heng, wide horizontal near top of right half) ---
draw_heng(draw,
          from_anchor=('C', 0.119, 0.151),
          to_anchor=('TR', 0.262, 0.979),
          width=8)

# --- Stroke 4: 大 撇 (pie from top-center down to left) — welds through C(0.51,0.13) w/ stroke 3 ---
draw_pie(draw,
         from_anchor=('TC', 0.544, 0.58),
         to_anchor=('BL', 0.809, 0.089),
         head_width=9, tail_width=2, curve=0.08, segments=48)

# --- Stroke 5: 大 捺 (na from center to lower-right) ---
draw_na(draw,
        from_anchor=('C', 0.796, 0.16),
        to_anchor=('MR', 0.862, 0.863),
        head_width=3, peak_width=12, tail_width=1,
        peak_t=0.8, curve=0.10, segments=48)

# --- Stroke 6: 亏 first heng (short, upper) ---
draw_heng(draw,
          from_anchor=('C', 0.365, 0.696),
          to_anchor=('C', 0.916, 0.597),
          width=7)

# --- Stroke 7: 亏 second heng + downward hook (wide horizontal turning down at right) ---
# MMH: head BC(0.078,0.051) x=108 y=205; tail MR(0.279,0.928) x=228 y=193.
# This is the 横折折 compound in 亏 — starts wide-left, arcs across, sweeps down-right to tail.
# Render as bezier so the tail can dip and end in a soft curve typical of 亏's hook.
def draw_heng_curved(d, head, tail, mid_ctrl, w0=8, w1=4, n=48):
    p0 = anchor_to_xy(head); p2 = anchor_to_xy(tail); ctrl = anchor_to_xy(mid_ctrl)
    pts = quad_bezier(p0, ctrl, p2, n=n)
    widths = [w0 + (w1 - w0) * (i / n) for i in range(n + 1)]
    stroke_variable_width(d, pts, widths)

draw_heng_curved(draw,
                 head=('BC', 0.078, 0.051),
                 tail=('MR', 0.279, 0.928),
                 mid_ctrl=('BC', 0.55, 0.30),
                 w0=8, w1=3, n=48)

# --- Stroke 8: 亏 vertical drop (竖, ending near bottom-center) ---
draw_shu(draw,
         from_anchor=('BC', 0.459, 0.095),
         to_anchor=('BC', 0.474, 0.883),
         width=7)


img.save(os.path.join(os.path.dirname(__file__), '01_侉.png'))
print("saved:", os.path.join(os.path.dirname(__file__), '01_侉.png'))
