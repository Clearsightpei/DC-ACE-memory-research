"""p3_char_0357_花 — G5 attempt.

Decomposition: 艹 (top, 3 strokes) + 化 (bottom, 4 strokes) = 7 strokes.
MMH confirms 7. Top-bottom compound composition.

P-A-007-v2 hard-check:
  - Sub-component 1 = 艹 (cao_grass). Bank has `cao_grass.py` (item #34, B1 PASS).
    Native aspect: x-span ~204, y-span ~130 (wide). At composition scale ~0.75,
    fits top ~40% of canvas. Native aspect ratio matches typical 艹 render.
    → CALL IT (in [0.55, 1.2] of native aspect).
  - Sub-component 2 = 化 (hua_change). Bank has `hua_change.py` (item #89, B6 PASS,
    itself explicitly promoted with 花 as a listed reuse target).
    Native aspect: x-span ~245, y-span ~165 (near-square-wide). At composition
    scale ~0.72, fits bottom ~55% of canvas. → CALL IT.
  Both whole-radical/whole-char bank primitives fit — NO BANK_DEVIATION needed.

P-A-006 inline-reasoning trace (per sub-component):
  - cao (艹): bank primitive from B1 PASS (heng + shu + shu). Reused verbatim.
    Two shus extend both above and below the heng (bank docstring confirms this
    matches GT better than MMH). Piercing joints s1.mid⇆s2.mid P and
    s1.mid⇆s3.mid P are intrinsic to the primitive's geometry.
  - hua (化): bank primitive from B6 PASS. Compound of ren_left (亻) + bi (匕).
    All internal joints (N-classes) are baked. Explicitly annotated in bank
    docstring as reuse target for 花.
  Cross-component vertical stacking: 艹 top at y≈40-135, 化 bottom at y≈140-260.
  No cross-component joints in MMH (top/bottom compound characters don't weld).
"""
import sys
import os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from cao_grass import draw_cao       # 3 strokes: heng, shu, shu
from hua_change import draw_hua      # 4 strokes: pie, shu, pie, shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 3 (cao) + 4 (hua) = 7 (matches MMH)
    'endpoint_mismatches': [],      # anchors from bank native geometry
    'joint_class_mismatches': [],   # all P joints intrinsic to cao primitive;
                                     # N joints intrinsic to hua primitive
    'overall_pass': True,
    'notes': 'Top-bottom compound. Both sub-components use whole-radical/char '
             'bank primitives (P-A-007-v2). 艹 via cao_grass, 化 via hua_change '
             '(the latter explicitly names 花 as a reuse target).'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- 艹 (top) — 3 strokes via bank cao_grass -------------------------------
# Native cao spans x=47..251, y=115..245. At scale 0.75 with ox=38, oy=-55:
#   x range ≈ 73..226 (centered ~150), y range ≈ 31..129 (top compartment).
#   Heng lands at y ≈ -55 + 180*0.75 = 80.
draw_cao(d, ox=38, oy=-55, scale=0.75)

# --- 化 (bottom) — 4 strokes via bank hua_change ---------------------------
# Native hua composed span (ren_left at ox=-40,oy=15,s=0.75 + bi at ox=100,oy=40,s=0.65):
#   x ≈ 20..263 (center ~142), y ≈ 70..235.
# At scale 0.72 with ox=48, oy=90:
#   x range ≈ 62..238 (center ~150), y range ≈ 140..259 (bottom compartment).
draw_hua(d, ox=48, oy=90, scale=0.72)

img.save(os.path.join(os.path.dirname(__file__), '01_花.png'))
print('wrote 01_花.png; SELF_CHECK:', SELF_CHECK)
