"""例 (lì) — 8 strokes. RETRY_1 from B11 C-verdict.

TRAJECTORY DIFF (main C -> retry_1):
  Prior attempt (main, C):
    - 亻 (s1 pie + s2 shu): fine, kept as-is.
    - 歹 top 一 (s3): fine.
    - 歹 s4 pie: drawn as straight diagonal — acceptable.
    - 歹 s5: drawn as STRAIGHT diagonal fat_line from (122,171) to (88,277) —
      this is the 横撇 (heng-fold-pie), its endpoints span a bend.
      Rendering as a straight line collapsed the fold; reads as another pie.
    - 歹 s6 dot: drawn with 3 waypoints spanning ~(105,194)->(125,214)
      with intermediate curved control — became a long streak, not a dot.
    - 刂 s8 竖钩: hook was over-flicked to a distant tip.

  Fixes applied here (per errata: "歹 = 一 (top) + 夕 (bottom =
                                    pie + horizontal + point)"):
    - s5 rebuilt as heng-then-pie (横撇) with an EXPLICIT corner: heng
      segment right from (122,171) to ~(158,168) then pie down-left
      to (88,277). Corner is visible.
    - s6 rebuilt as a compact 点 dot: short thickened line ~20px long,
      NOT a long pie.
    - s8 hook shortened; flicks only ~18px up-left at the tail.
    - Everything else kept — 亻, s3, s4 were the OK parts.

Decomposition: 例 = 亻 (left) + 列 (right); 列 = 歹 (middle) + 刂 (right).
Slots (from MMH):
  亻: far-left column   — s1 pie + s2 shu
  歹: center column     — s3 heng, s4 pie, s5 heng-pie, s6 dot
  刂: right column      — s7 短竖, s8 长竖钩
"""
# BANK_DEVIATION
# skipped: ren_side.py
# reason: ren_side defaults sit at TC/C/BC (mid-column); MMH places 亻 at
#   TL/ML/BL — far-left column slot for a 3-radical char.
# fresh_component: ren_side_far_left_column_for_3radical
#
# skipped: dao_side.py
# reason: dao_side default spacing between 短竖 and 竖钩 is wider than the
#   tight right-column pair MMH puts here (~15px vs bank ~50px).
# fresh_component: dao_side_tight_pair_for_3radical

from PIL import Image, ImageDraw
import os, sys

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "success_bank", "code"))
sys.path.insert(0, _BANK)
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 8 stroke units
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # all 6 joints are N; gaps preserved
    'overall_pass': True,
    'notes': ('retry_1: s5 rebuilt as heng-pie with explicit corner, '
              's6 shrunk to a compact dot per errata fix.'),
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ============ 亻 (left, far-left column) ============
# s1 撇 pie: TL(0.79,0.65) -> ML(0.17,0.95), bowed slightly left.
s1_h = anchor_to_xy(('TL', 0.791, 0.645))
s1_t = anchor_to_xy(('ML', 0.170, 0.948))
mx = (s1_h[0] + s1_t[0]) / 2 - 8
my = (s1_h[1] + s1_t[1]) / 2
pts = quad_bezier(s1_h, (mx, my), s1_t, n=48)
widths = [12 - 11 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s2 竖 shu: ML(0.62,0.49) -> BL(0.66,0.84).
s2_h = anchor_to_xy(('ML', 0.624, 0.491))
s2_t = anchor_to_xy(('BL', 0.662, 0.836))
fat_line(d, s2_h, s2_t, width=9)

# ============ 歹 (middle, upper-center) ============
# s3 一 top heng of 歹 (slight upward tilt).
s3_h = anchor_to_xy(('C', 0.052, 0.160))
s3_t = anchor_to_xy(('C', 0.799, 0.040))
fat_line(d, s3_h, s3_t, width=7)

# s4 撇 of 夕 (long pie down-left through 歹 interior).
s4_h = anchor_to_xy(('C', 0.257, 0.245))
s4_t = anchor_to_xy(('BL', 0.911, 0.013))
mx = (s4_h[0] + s4_t[0]) / 2 - 6
my = (s4_h[1] + s4_t[1]) / 2 + 3
pts = quad_bezier(s4_h, (mx, my), s4_t, n=40)
widths = [9 - 7 * (i / len(pts)) for i in range(len(pts))]
stroke_variable_width(d, pts, widths)

# s5 横撇 of 夕 — HENG then PIE with an explicit corner.
# MMH endpoints span the fold: head at heng-left, tail at pie-end.
# Reconstruct: heng right to a corner near (158, 168), then pie down-left
# to the MMH tail (88, 277).
s5_h = anchor_to_xy(('C', 0.225, 0.708))          # (122.5, 170.8)
s5_t = anchor_to_xy(('BL', 0.885, 0.774))          # ( 88.5, 277.4)
s5_corner = (s5_h[0] + 36, s5_h[1] - 3)            # (~158.5, 167.8)
# heng segment (horizontal, slight upward)
fat_line(d, s5_h, s5_corner, width=7)
# pie segment (down-left, tapering)
pts_pie = quad_bezier(s5_corner,
                      ((s5_corner[0] + s5_t[0]) / 2 - 4,
                       (s5_corner[1] + s5_t[1]) / 2),
                      s5_t, n=36)
widths_pie = [8 - 6 * (i / len(pts_pie)) for i in range(len(pts_pie))]
stroke_variable_width(d, pts_pie, widths_pie)

# s6 点 dot of 夕 — short thickened diagonal (~20 px), NOT a long pie.
s6_h = anchor_to_xy(('C', 0.058, 0.937))           # (105.8, 193.7)
s6_t = anchor_to_xy(('BC', 0.251, 0.139))          # (125.1, 213.9)
# Compact dot: 3 sample points, taper from thin -> fat -> thin.
mid = ((s6_h[0] + s6_t[0]) / 2, (s6_h[1] + s6_t[1]) / 2)
pts_dot = [s6_h, mid, s6_t]
widths_dot = [3, 9, 4]
stroke_variable_width(d, pts_dot, widths_dot)

# ============ 刂 (right column pair) ============
# s7 短竖 (short vertical, inner-right).
s7_h = anchor_to_xy(('C', 0.872, 0.348))
s7_t = anchor_to_xy(('BC', 0.948, 0.191))
fat_line(d, s7_h, s7_t, width=7)

# s8 竖钩 (long vertical with small hook up-left at the bottom).
s8_h = anchor_to_xy(('TR', 0.268, 0.677))          # (226.8,  67.7)
s8_t = anchor_to_xy(('BR', 0.027, 0.710))          # (202.7, 271.0)
# straight body down to just above the tail
hook_start = (s8_h[0] - 2, s8_t[1] - 14)           # near the bottom of body
fat_line(d, s8_h, hook_start, width=10)
# small hook flick up-left
pts_hook = quad_bezier(hook_start,
                       (hook_start[0] - 6, hook_start[1] + 4),
                       s8_t, n=14)
widths_hook = [9 - 7 * (i / len(pts_hook)) for i in range(len(pts_hook))]
stroke_variable_width(d, pts_hook, widths_hook)

out_path = os.path.join(os.path.dirname(__file__), "01_例.png")
img.save(out_path)
print("wrote", out_path)
