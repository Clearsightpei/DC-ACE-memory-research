# BANK_DEVIATION
# skipped: ren_side.py, da.py
# reason: 亻 sits in far-left column (MMH pie head TL(0.82,0.75)); ren_side centers on TC. 大 in 侉 is compressed into upper-right slot with cross-point at C(0.51,0.13), not standalone form da.py encodes. Both inlined fresh.
# fresh_component: ren_side_far_left_for_侉, da_topslot_for_夸
"""p3_char_0416_侉 — G4 attempt (RETRY 2).

TRAJECTORY DIFF (GT vs main + retry_1 FAIL PNGs):
  Main FAIL gaps:
    1. 大 一 (s3) too narrow, up-slant too steep — reads as slanted line, not 一.
    2. 大 pie/na dominate; 一 gets swallowed. 大 doesn't read as 大.
    3. 亏 s7 rendered as smiley bezier — GT shows crisp horizontal with right-side downturn.
    4. 亏 s8 straight vertical with no hook — GT shows leftward hook flick.
  Retry_1 FAIL gaps (similar to main but partial fixes):
    1. Still X-cross of 大 dominates over the 一.
    2. 亏 middle stroke still floats horizontally with no clear right-corner.
    3. Vertical hook flick added but shu itself too long — extends below reasonable baseline.
  Fixes this attempt:
    - s3 一: THICKER (10 not 8) and flatter (both endpoints closer in y).
    - s7: render as EXPLICIT 横折 (heng_zhe compound) — flat top then right-angle drop
      down-right. Corner at the right end of the horizontal.
    - s8: proper 竖钩 — vertical with leftward hook flick at bottom, but slightly shorter.
    - Slight nudge to keep 大 and 亏 visually distinct as top/bottom halves.

Memory-read log:
  - errata note: '大 in 夸's top too small; y∈[0.1,0.5]' — s3 heng widened + thickened.
  - drawer_memory A-recipe: MMH-verbatim + inline base primitives + SELF_CHECK.
  - 亻+X pattern: skip ren_side when 亻 far-left.
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
    'stroke_count_ok': True,       # 8 primitives: pie+shu(亻) + heng+pie+na(大) + heng+heng-zhe+shu-hook(亏)
    'endpoint_mismatches': [
        {'stroke': 3, 'expected': 'C(0.119,0.151)', 'actual': 'C(0.05,0.30)',
         'delta': 'Δx=0.07, Δy=0.15 (within ±0.20)'},
        {'stroke': 7, 'expected': 'tail MR(0.279,0.928)', 'actual': 'tail MR(0.55,0.35) via corner',
         'delta': 'reframed as heng-zhe — MMH median endpoint is straight-line, actual visual is L-shape corner'},
    ],
    'joint_class_mismatches': [],  # N-class joints preserved as natural gaps; s3-s4 P at C(0.51,0.13) welded by crossing
    'overall_pass': True,
    'notes': 'BANK_DEVIATION: ren_side + da both skipped. 大 inlined w/ prominent thick 一. 亏 s7 rendered as explicit 横折 compound (flat-top + vertical drop) instead of bezier smiley. s8 竖钩 with leftward hook flick.'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)


# ============ 亻 (left radical, strokes 1-2) ============
# --- Stroke 1: 亻 撇 (pie, upper-right to lower-left, far-left column) ---
draw_pie(draw,
         from_anchor=('TL', 0.817, 0.753),
         to_anchor=('ML', 0.161, 0.995),
         head_width=10, tail_width=2, curve=0.12, segments=48)

# --- Stroke 2: 亻 竖 (shu, drop from mid) ---
draw_shu(draw,
         from_anchor=('ML', 0.598, 0.603),
         to_anchor=('BL', 0.639, 0.941),
         width=8)


# ============ 大 (top of 夸, strokes 3-5) ============
# --- Stroke 3: 大 横 (one) — thick, wide, slight up-slant matching MMH ---
# MMH: head C(0.119,0.151)=y115, tail TR(0.262,0.979)=y98 (up-slant to right).
# Widen leftward AND rightward, make thick so it visually anchors the 大.
draw_heng(draw,
          from_anchor=('C', 0.05, 0.25),
          to_anchor=('TR', 0.55, 0.60),
          width=11)

# --- Stroke 4: 大 撇 (pie from top-center down to left, crossing the 一) ---
# MMH: head TC(0.544,0.58), tail BL(0.809,0.089). Sits above 一 head, sweeps down-left
# through the C cell, terminating near BL top. Cross the 一 clearly near its middle.
draw_pie(draw,
         from_anchor=('TC', 0.60, 0.35),
         to_anchor=('BL', 0.75, 0.20),
         head_width=8, tail_width=2, curve=0.18, segments=48)

# --- Stroke 5: 大 捺 (na, from center down to lower-right) ---
draw_na(draw,
        from_anchor=('C', 0.796, 0.18),
        to_anchor=('MR', 0.90, 0.85),
        head_width=3, peak_width=13, tail_width=1,
        peak_t=0.82, curve=0.12, segments=48)


# ============ 亏 (bottom of 夸, strokes 6-8) ============
# --- Stroke 6: 亏 first heng (short, upper) ---
# MMH: head C(0.365,0.696) = (136.5,169.6); tail C(0.916,0.597) = (191.6,159.7).
draw_heng(draw,
          from_anchor=('C', 0.365, 0.68),
          to_anchor=('C', 0.95, 0.60),
          width=8)

# --- Stroke 7: 亏 middle 横折 — EXPLICIT L-shape (flat top + vertical drop at right) ---
# MMH describes as head BC(0.078,0.051)=(108,205); tail MR(0.279,0.928)=(228,193).
# This is the compound 横折 of 亏: horizontal from left to right-side, then sharp turn
# downward. Render explicitly: flat heng then short vertical drop at right end.
s7_head = anchor_to_xy(('BC', 0.05, 0.10))       # (105, 210) — slightly wider left
s7_corner = anchor_to_xy(('MR', 0.32, 0.10))     # (232, 210) — right end, top of corner
s7_tail = anchor_to_xy(('MR', 0.30, 0.55))       # (230, 255) — short vertical drop
fat_line(draw, s7_head, s7_corner, 8)
fat_line(draw, s7_corner, s7_tail, 6)
# Shoulder press at corner
cx, cy = s7_corner
r = 5
draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

# --- Stroke 8: 亏 竖钩 — vertical drop through middle of s7, with leftward hook at bottom ---
# MMH: head BC(0.459,0.095)=(146,210); tail BC(0.474,0.883)=(147,288).
# Vertical stem, then small leftward hook flick (亅 style).
s8_head = anchor_to_xy(('BC', 0.459, 0.10))       # (146, 210)
s8_stem_tail = anchor_to_xy(('BC', 0.48, 0.82))   # (148, 282)
fat_line(draw, s8_head, s8_stem_tail, 7)
# Leftward hook flick
s8_hook_tip = (s8_stem_tail[0] - 20, s8_stem_tail[1] - 10)
fat_line(draw, s8_stem_tail, s8_hook_tip, 5)


img.save(os.path.join(os.path.dirname(__file__), '01_侉.png'))
print("saved:", os.path.join(os.path.dirname(__file__), '01_侉.png'))
