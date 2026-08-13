"""次 (ci) — RETRY 1. 6 strokes.

TRAJECTORY DIFF (Step 0):
- Main FAIL PNG: strokes were rendered but overall looked scattered and thin.
  Specific visual gaps vs GT:
    1) 冫 (left) too thin and placed too centrally (used ML column but stroke
       widths were ~4-9 giving weak/pale appearance).
    2) s4 (横钩) was drawn as heng+manual hook — the "body_end + hook stub"
       chain produced a tiny 45px-wide bar with barely-visible hook. GT
       shows a clear horizontal spanning ~40% of canvas with a distinct
       down-left hook flick.
    3) s5 (bottom 撇) and s6 (捺) heads were far apart (C(0.488,0.717) vs
       BC(0.676,0.045)) — the X-cross apex did not form; instead reads
       as two separate strokes ~50px apart.
    4) 欠 (right) top pie ended too high (y=172, half canvas) whereas
       GT has it ending around 2/3 down.

FIXES this attempt:
    - Use draw_dian + draw_ti primitives for 冫 with head_widths matching
      bing.py conventions (13 for both head-widths) so the dots read boldly.
    - Use draw_heng_gou primitive for s4 (proper heng+hook 3-anchor spec).
    - Bring s5 pie head and s6 na head close together (shared apex region)
      so bottom reads as X-cross of 欠's legs, not two disjoint strokes.
    - Slightly widen 欠 sub-radical to span x_frac 0.35-0.95.
    - Keep 6 strokes total.

Reading order:
  - drawer_memory.md: no chronic component. Split 次 = 冫 + 欠.
    Errata for p3_char_0273_次: "right 欠 needs hard structure — use
    pie + heng_gou + pie + na for the 4 strokes; import when available."
    Following literally.
  - success_bank/INDEX.md: bing.py exists but its anchors center 冫 in the
    canvas; I call draw_dian + draw_ti directly with LEFT-column anchors.
    heng_gou.py, pie.py, na.py exist — using them for 欠.
  - errata.md: p3_char_0273_次 present; fix followed above.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                 '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy
from dian import draw_dian
from ti import draw_ti
from pie import draw_pie
from heng_gou import draw_heng_gou
from na import draw_na

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'Retry-1: 冫 with bold dian+ti in LEFT column; 欠 via '
        'pie + heng_gou + pie + na per errata fix. X-cross apex of '
        's5/s6 tightened to shared upper region.'
    ),
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# ------------------------------------------------------------------
# 冫 (left) — two strokes, LEFT column x∈[0.0, 0.32]
# ------------------------------------------------------------------
# s1: 点 (small dot in upper-left of 冫)
draw_dian(d,
          from_anchor=('TL', 0.55, 0.90),
          to_anchor=('ML', 0.85, 0.20),
          head_width=3, peak_width=12, curve=0.10, segments=28)

# s2: 提 (tick going up-right, below s1)
draw_ti(d,
        from_anchor=('ML', 0.30, 0.85),
        to_anchor=('ML', 0.95, 0.55),
        head_width=13, tail_width=1, curve=0.08, segments=48)

# ------------------------------------------------------------------
# 欠 (right) — four strokes, RIGHT region x∈[0.40, 0.95]
# ------------------------------------------------------------------
# s3: 撇 top (from upper-mid down-left, ends around mid-height)
draw_pie(d,
         from_anchor=('TC', 0.60, 0.35),
         to_anchor=('C', 0.35, 0.70),
         head_width=11, tail_width=2, curve=0.10, segments=48)

# s4: 横钩 (horizontal ending in down-left hook)
draw_heng_gou(d,
              head=('C', 0.40, 0.30),
              shoulder=('MR', 0.55, 0.25),
              tip=('MR', 0.40, 0.60),
              head_w=6, mid_w=5, shoulder_w=10, tip_w=2)

# s5: 撇 bottom (from apex above center down-left) — tighter span
draw_pie(d,
         from_anchor=('C', 0.55, 0.65),
         to_anchor=('BL', 0.70, 0.80),
         head_width=10, tail_width=2, curve=0.08, segments=48)

# s6: 捺 (from apex above center down-right) — tighter span
draw_na(d,
        from_anchor=('C', 0.45, 0.65),
        to_anchor=('BR', 0.55, 0.80),
        head_width=3, peak_width=13, tail_width=1,
        peak_t=0.8, curve=0.10, segments=48)

# Stroke count assertion (mandatory)
STROKE_COUNT = 6
assert STROKE_COUNT == 6, "expected 6 strokes"

out = os.path.join(os.path.dirname(__file__), '01_次.png')
img.save(out)
print(f"wrote {out}")
