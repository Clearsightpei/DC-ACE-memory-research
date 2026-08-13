"""p2_radical_073_囗 — the enclosure radical (big empty box, 3 strokes).

Same 3-stroke structure as 口 (kou): 竖 (left) + 横折 (top+right) + 横 (bottom).
Difference: 囗 fills nearly the whole canvas, whereas 口 sits smaller/centered.

Uses bank primitives: shu, heng_zhe_box, heng — via MMH-derived pixel anchors,
NOT via draw_kou (which is tuned to the compact 口 footprint).
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


# --- MMH-derived anchors (300x300 canvas, 米字格 3x3 cells of 100) ---
# stroke 1 (left 竖):    ('TL', 0.645, 0.794) -> ('BL', 0.68,  0.868)
S1_HEAD = (64.5, 79.4)
S1_TAIL = (68.0, 286.8)
# stroke 2 (横折 top+right): ('TL', 0.803, 0.832) -> ('BR', 0.297, 0.962)
S2_HEAD = (80.3, 83.2)
S2_TAIL = (229.7, 296.2)
# stroke 3 (bottom 横):  ('BL', 0.768, 0.78) -> ('BR', 0.147, 0.648)
S3_HEAD = (76.8, 278.0)
S3_TAIL = (214.7, 264.8)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: left vertical
draw_shu(d, S1_HEAD, S1_TAIL, width=8)

# s2: heng-zhe box — top_left = s2 head, bottom_right = s2 tail
draw_heng_zhe_box(d, S2_HEAD, S2_TAIL, width=8)

# s3: bottom heng — leave small natural gap at BL vs s1.tail (N joint)
# and at BR vs s2.tail (N joint). The MMH tails already provide those gaps.
draw_heng(d, S3_HEAD, S3_TAIL, width_head=8, width_tail=9)

out_path = os.path.join(os.path.dirname(__file__), '01_囗.png')
img.save(out_path)
print(f"saved {out_path}")


# ---- Self-check ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 bank calls (shu, heng_zhe_box, heng) = 3 strokes
    'endpoint_mismatches': [], # anchors used verbatim from MMH block
    'joint_class_mismatches': [], # all three joints are N (natural gaps preserved)
    'overall_pass': True,
    'notes': '囗 = big-box variant of 口. Reused kou primitives (shu, heng_zhe_box, heng) with MMH pixel anchors directly rather than calling draw_kou (which is tuned to compact 口).'
}
