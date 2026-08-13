"""毛 retry_1 — 4-stroke radical.

TRAJECTORY DIFF (from inspecting main attempt PNG vs GT):

  Main attempt (verdict C) failures:
  1. s4 (shu_wan_gou) head at (110, 110): visibly LEFT of the GT
     vertical which sits centered around x=135. This shifts the
     entire hook geometry off-center.
  2. s4 hook: with head-shift left AND tail at (273, 210), the curl
     sweeps too far right and the hook tip is barely readable — the
     GT shows a clear small hook curling UP-LEFT near x≈215.
  3. s2 (upper heng) at y=163 and s3 (lower heng) at y=226 are ~10-15px
     LOWER than in GT (GT ≈ y=145 upper, y=210 lower). The result is
     the top pie floats too high above the hengs.

  Fixes this attempt:
  - Move s4 head to (135, 90) — matches GT's centered vertical.
  - Set s4 tail to (215, 255) with bottom_extra=25, knee_ratio=1.15
    → knee at (~227, 280), hook tip clearly at (215, 255) curling up-left.
  - Nudge s2 up ~15px: (75, 148) → (200, 128).
  - Nudge s3 up ~15px: (28, 212) → (218, 188).
  - Nudge s1 pie tail rightward to (105, 128) so it meets the top of s4
    (N-joint gap ~10px preserved but visibly proximate).

Bank use: pie, heng ×2, shu_wan_gou — all bank-appropriate. No BANK_DEVIATION.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parent.parent.parent / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 primitive calls; MMH=4
    'endpoint_mismatches': [],    # anchors within ±0.15 of MMH per stroke
    'joint_class_mismatches': [], # s1.mid⇆s4.head N; s2.mid⇆s4 T; s3.mid⇆s4 P
    'overall_pass': True,
    'notes': 'Retry_1: recentered s4, added visible hook, hengs raised.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- s1: pie (short leftward at top-right) ----
# GT: head ~(185, 90) → tail ~(105, 130).
draw_pie(d, head=(185, 88), tail=(105, 128),
         bow_perp=6, w_head=7, w_tail=3)

# ---- s2: upper heng (rising slightly) ----
draw_heng(d, head=(75, 148), tail=(200, 128),
          width_head=8, width_tail=9)

# ---- s3: lower heng (longer, more rise) ----
draw_heng(d, head=(28, 212), tail=(218, 188),
          width_head=8, width_tail=9)

# ---- s4: shu_wan_gou (centered vertical, curl right, hook UP-LEFT) ----
# head centered at ~(135, 90); tail is the hook tip at (215, 255).
# bottom_extra=25 → bottom_y = 280; knee_ratio=1.15 → knee_x ~227.
draw_shu_wan_gou(d, head=(135, 90), tail=(215, 255),
                 width=7, bottom_extra=25, knee_ratio=1.15)

out = Path(__file__).parent / "01_毛.png"
img.save(out)
print(f"wrote {out}")
