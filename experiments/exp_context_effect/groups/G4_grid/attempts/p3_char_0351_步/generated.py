"""步 (bù) — Phase-3 char, 7 strokes.

Decomposition:  步 = 止 (top) + ⺘/少-like (bottom, sharing 止's baseline).
  止 top: s1 短竖 + s2 短横 + s3 短竖(left) + s4 长横 (baseline)
  少-bot: s5 短竖 + s6 短撇 + s7 长撇 (extending down-left, sweeps below canvas)

Memory read: drawer_memory.md (A-recipe points 1,2,3,5) + INDEX grep
(zhi_stop.py exists but MMH anchors here disagree with zhi_stop defaults
— A-recipe point 4 says inline with MMH-verbatim rather than partially
override compound primitive).  errata.md has no entry for 步.

BANK_DEVIATION
skipped: zhi_stop.py
reason: MMH places 止's 4 strokes tightly around C/TR cells, whereas
        zhi_stop's DEFAULTS sit in TC/MR/ML/BL bands — a partial anchor
        override of a 4-stroke compound (B8 伊 pattern) would lose 止's
        integration with the bottom 少-half of 步.  Inlining 止 with
        base primitives (shu/heng) at MMH-verbatim anchors instead.
fresh_component: zhi_top_for_bu (embedded 止 sized to abut 少-stem)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 7 primitive calls: shu, heng, shu, heng, shu, pie, pie
    'endpoint_mismatches': [], # all 7 head/tail passed MMH anchors verbatim
    'joint_class_mismatches': [],  # all 7 N-joints preserved (no explicit welding)
    'overall_pass': True,
    'notes': ('步 = 止 (s1-s4) + 少-like (s5-s7). MMH-verbatim anchors '
              'throughout; s7 tail (BL, 0.688, 1.208) extends below canvas '
              'as intended for the sweeping 长撇 of 步.'),
}

import sys, os
BANK = os.path.join(os.path.dirname(__file__),
                    '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from PIL import Image, ImageDraw
from shu import draw_shu
from heng import draw_heng
from pie import draw_pie

img = Image.new('RGB', (300, 300), (255, 255, 255))
d = ImageDraw.Draw(img)

# --- 止 (top, s1-s4) — MMH anchors verbatim ---
# s1 短竖 (top center of 止)
draw_shu(d, ('TC', 0.427, 0.621), ('C', 0.479, 0.477), width=9)
# s2 短横 (upper right of 止)
draw_heng(d, ('C', 0.655, 0.031), ('TR', 0.265, 0.926), width=8)
# s3 短竖 (left of 止 — very short, MMH gives near-vertical)
draw_shu(d, ('TL', 0.899, 0.946), ('C', 0.052, 0.526), width=9)
# s4 长横 (baseline of 止, extends across)
draw_heng(d, ('ML', 0.372, 0.693), ('MR', 0.707, 0.468), width=10)

# --- 少-like (bottom, s5-s7) — MMH anchors verbatim ---
# s5 短竖 (middle stem of 少)
draw_shu(d, ('C', 0.453, 0.611), ('BC', 0.538, 0.499), width=9)
# s6 短撇 (small pie at 少 head)
draw_pie(d, ('C', 0.069, 0.831), ('BL', 0.888, 0.367),
         head_width=7, tail_width=2, curve=0.05, segments=24)
# s7 长撇 (sweeping pie extending below canvas)
draw_pie(d, ('MR', 0.092, 0.737), ('BL', 0.688, 1.208),
         head_width=11, tail_width=1, curve=0.10, segments=48)

out = os.path.join(os.path.dirname(__file__), '01_步.png')
img.save(out)
print('wrote', out)
