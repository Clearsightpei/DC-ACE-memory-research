"""盯 (dīng) — 7 strokes.

Decomposition: 盯 = 目 (left, 5 strokes) + 丁 (right, 2 strokes).
  目: 竖 + 横折 + 横 + 横 + 横  (all N-joints, small gap; not welded)
  丁: 横 + 竖钩

Following A-recipe: MMH-verbatim anchors, base primitives only
(_anchor + fat_line). No compound-primitive override.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 7 fat_line "strokes" (compound counted as 1)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all 9 joints class N — natural gaps preserved
    'overall_pass': True,
    'notes': '7 strokes MMH-verbatim; 目 middle bars intentionally short per GT; 丁 hook via 2-seg polyline.',
}

import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.normpath(os.path.join(_HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line

W = 10
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- 目 (left half) ----

# stroke 1 — 竖 (left vertical)
s1h = anchor_to_xy(('TL', 0.354, 0.976))
s1t = anchor_to_xy(('BL', 0.445, 0.663))
fat_line(d, s1h, s1t, W)

# stroke 2 — 横折 (top bar + right vertical)
s2h = anchor_to_xy(('ML', 0.527, 0.017))
s2t = anchor_to_xy(('BC', 0.008, 0.689))
corner = (s2t[0], s2h[1])                    # top-right corner (weld)
fat_line(d, s2h, corner, W)
fat_line(d, corner, s2t, W)

# stroke 3 — upper middle 横 (short — per GT, does not touch right wall)
s3h = anchor_to_xy(('ML', 0.554, 0.629))
s3t = anchor_to_xy(('ML', 0.803, 0.553))
fat_line(d, s3h, s3t, W)

# stroke 4 — lower middle 横 (short — per GT)
s4h = anchor_to_xy(('BL', 0.557, 0.010))
s4t = anchor_to_xy(('ML', 0.812, 0.939))
fat_line(d, s4h, s4t, W)

# stroke 5 — bottom 横
s5h = anchor_to_xy(('BL', 0.527, 0.558))
s5t = anchor_to_xy(('BL', 0.847, 0.467))
fat_line(d, s5h, s5t, W)

# ---- 丁 (right half) ----

# stroke 6 — top 横 (long, spans right two-thirds)
s6h = anchor_to_xy(('C', 0.248, 0.181))
s6t = anchor_to_xy(('MR', 0.774, 0.058))
fat_line(d, s6h, s6t, W)

# stroke 7 — 竖钩 (vertical + leftward hook)
s7h = anchor_to_xy(('C', 0.866, 0.187))
s7t = anchor_to_xy(('BC', 0.562, 0.692))
# vertical body straight down; hook = short diagonal to tail
body_end = (s7h[0], s7t[1] - 12)
fat_line(d, s7h, body_end, W)
fat_line(d, body_end, s7t, W)

img.save(os.path.join(_HERE, '01_盯.png'))
print("wrote", os.path.join(_HERE, '01_盯.png'))
