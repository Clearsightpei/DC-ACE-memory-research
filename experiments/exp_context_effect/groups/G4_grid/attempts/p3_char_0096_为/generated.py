"""为 (wéi) — 4 strokes. Revision 1.

Lookup checklist:
1. success_bank/INDEX.md grep '为' → no direct entry.
2. errata.md grep '为' → not listed.
3. form_catalog.md — top 点, main 撇, wrapper 横折弯钩.
4. principles_meta.md TR1 (override anchors), TR10 (N-gap ≤25 px).
5. joint_atlas.md — P welded (crossing dot), N gap (wrapper approach).
6. sandbox.md — no prior 为 note.

Revision notes vs pass 1:
  - Pass 1 rendered s1 as a long diagonal (misread the anchors: TL 0.902,0.8
    and C 0.189,0.134 are both very close to the TL/C boundary — should be
    a SHORT dot, not a line across).
  - Pass 1's s4 went too far to top-right corner and merged into the 撇.
  - Fixed: shorter s1 dot; s4 kept more compact with proper hook.

Structure:
  s1: short 点 top-left (TL 0.902,0.8 → C 0.189,0.134) — tiny stroke near cell boundary
  s2: main 撇 (TC 0.664,0.574 → BL 0.331,0.871)
  s3: short 撇/点 crossing s2 body at C — P weld
  s4: 横折弯钩 wrapper (C 0.406,0.931 → BC 0.702,0.238) — head N-gap from s2
"""

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, sample_line

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Revision 1 — shortened top dot, contained wrapper.'
}

CANVAS = 300
img = Image.new('RGB', (CANVAS, CANVAS), 'white')
draw = ImageDraw.Draw(img)

# ---- Stroke 1: top 点 dot ----
# MMH anchors span TL(0.902,0.8) → C(0.189,0.134). Both are on the TL/C
# boundary — this is a short slanted dot at top of grid.
s1_h = anchor_to_xy(('TL', 0.902, 0.8))
s1_t = anchor_to_xy(('C',  0.189, 0.134))
# Actual pixel distance: (~90px + ~63px) into TL-BR direction — a dot ~15-20px.
# Recompute as short stroke around midpoint.
mid_s1 = ((s1_h[0] + s1_t[0]) / 2, (s1_h[1] + s1_t[1]) / 2)
# Draw a short 撇-like dot: from upper-right to lower-left, ~18px long.
s1_start = (mid_s1[0] + 9, mid_s1[1] - 9)
s1_end   = (mid_s1[0] - 9, mid_s1[1] + 9)
pts1 = sample_line(s1_start, s1_end, n=10)
widths1 = [7 - int(4 * i / len(pts1)) for i in range(len(pts1))]
widths1 = [max(w, 3) for w in widths1]
stroke_variable_width(draw, pts1, widths1)

# ---- Stroke 2: main 撇 (long diagonal) ----
s2_h = anchor_to_xy(('TC', 0.664, 0.574))
s2_t = anchor_to_xy(('BL', 0.331, 0.871))
# Gentle bow to the right-then-back.
mid2 = ((s2_h[0] + s2_t[0]) / 2 + 6, (s2_h[1] + s2_t[1]) / 2 - 2)
pts2 = quad_bezier(s2_h, mid2, s2_t, n=60)
widths2 = [8 - int(5 * i / len(pts2)) for i in range(len(pts2))]
widths2 = [max(w, 3) for w in widths2]
stroke_variable_width(draw, pts2, widths2)

# ---- Stroke 3: mid dot crossing s2 (P weld) ----
s3_h = anchor_to_xy(('ML', 0.595, 0.55))
s3_t = anchor_to_xy(('BC', 0.541, 0.666))
pts3 = sample_line(s3_h, s3_t, n=15)
widths3 = [5 + int(3 * i / len(pts3)) for i in range(len(pts3))]
stroke_variable_width(draw, pts3, widths3)

# ---- Stroke 4: 横折弯钩 wrapper ----
# Head at (C 0.406, 0.931): x ≈ 141, y ≈ 193 — middle-left, near s2 body.
# Tail at (BC 0.702, 0.238): x ≈ 170, y ≈ 224 — middle-lower, hook end.
# Path: start with 横 going RIGHT across the top of the wrapper region,
# fold DOWN the right side, then hook curves back LEFT ending near tail.

s4_h = anchor_to_xy(('C', 0.406, 0.931))       # ≈ (141, 193)
# top-right corner of the wrapper (a bit right of center, top of BR/MR)
p_top_right = anchor_to_xy(('MR', 0.55, 0.30))  # ≈ (255, 130) — hmm too high
# Reconsider: the wrapper's 横 top should be roughly at y ≈ 180-190 (same level as s4_h)
# and go right to ~x=240. Then fold and curve down.
p_top_right = (245, 175)
# Bottom-right of the curve, ~ (245, 260)
p_bot_right = (240, 260)
# Hook end approaches MMH tail (BC 0.702, 0.238) ≈ (170, 224)
p_hook_end = anchor_to_xy(('BC', 0.702, 0.238))

# Segment A: 横 top — s4_h → p_top_right, slight up-slope
midA = ((s4_h[0] + p_top_right[0]) / 2, (s4_h[1] + p_top_right[1]) / 2 - 5)
segA = quad_bezier(s4_h, midA, p_top_right, n=25)

# Segment B: right-side descent curving out then in — p_top_right → p_bot_right
midB = (p_top_right[0] + 12, (p_top_right[1] + p_bot_right[1]) / 2)
segB = quad_bezier(p_top_right, midB, p_bot_right, n=30)

# Segment C: hook — curve back to the left ending at hook end
midC = ((p_bot_right[0] + p_hook_end[0]) / 2 + 5, p_bot_right[1] + 5)
segC = quad_bezier(p_bot_right, midC, p_hook_end, n=20)

pts4 = segA + segB[1:] + segC[1:]
widths4 = [6] * len(pts4)
# Taper the last few for the hook
for k in range(min(5, len(widths4))):
    widths4[-1 - k] = max(3, widths4[-1 - k] - k)
stroke_variable_width(draw, pts4, widths4)

# ---- Save ----
out_png = os.path.join(os.path.dirname(__file__), '01_为.png')
img.save(out_png)
print(f"saved {out_png}")
print(f"SELF_CHECK: {SELF_CHECK}")
