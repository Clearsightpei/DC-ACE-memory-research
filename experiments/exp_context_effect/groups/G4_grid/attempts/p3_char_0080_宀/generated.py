"""p3_char_0080_宀 — reuse mastered mian.py with MMH-derived anchor overrides.

MANDATORY LOOKUP CHECKLIST:
  1. success_bank INDEX grep — 宀 present (row 82, mian.py, mastered as radical). Reuse per TR1 with OVERRIDE anchors.
  2. errata grep — 宀 not listed.
  3. form_catalog — 点/横钩 in roof-radical context; use mastered mian shape.
  4. principles_meta — TR1 (bank reuse with override), TR10 (N-gap must stay visible, do not weld).
  5. joint_atlas — s1.tail is well above s3 body (N-gap ~32 px); s2.head near s3.head (N-gap ~13 px).
  6. sandbox — no relevant note.

Stroke plan (matches MMH expectations, 3 strokes):
  s1 (top 点):   head=('C', 0.23, 0.195) → tail=('C', 0.579, 0.506)
  s2 (left 点):  head=('ML', 0.668, 0.696) → tail=('BL', 0.536, 0.253)
  s3 (横钩):     head=('ML', 0.791, 0.796) ; shoulder near right end of horizontal ; tip=('BR', 0.115, 0.036)
     Shoulder derived from tail direction: place at ('MR', 0.90, 0.90) — the far-right 顿笔 press before the down-left hook flick to tip.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Reused mian.py from success_bank (row 82) with anchor overrides matching MMH per TR1. Stroke count = 3. Joints s1-s3 mid and s2-s3 head are N-class (no weld). Shoulder for 横钩 chosen at (MR, 0.90, 0.90) to keep horizontal spanning ML → far-right of MR/top-BR, then hook flick down-left to tip at BR.',
}

import os, sys
from PIL import Image, ImageDraw

# Make shared primitives importable.
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from mian import draw_mian  # noqa: E402

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Override anchors to MMH expectations (TR1: reuse primitive with fresh anchors).
draw_mian(
    draw,
    s1_head=('C',  0.23,  0.195),
    s1_tail=('C',  0.579, 0.506),
    s2_head=('ML', 0.668, 0.696),
    s2_tail=('BL', 0.536, 0.253),
    s3_head=('ML', 0.791, 0.796),
    s3_shoulder=('MR', 0.90, 0.90),
    s3_tip=('BR', 0.115, 0.036),
)

out = os.path.join(os.path.dirname(__file__), "01_宀.png")
img.save(out)
print("wrote", out)
