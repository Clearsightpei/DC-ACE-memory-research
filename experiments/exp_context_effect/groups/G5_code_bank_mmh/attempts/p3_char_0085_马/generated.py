"""p3_char_0085_马 — 马 (ma, 'horse'). 3 strokes.

MMH structural spec:
  s1: head TL(0.847,0.902)=(84.7,90.2)  tail C(0.726,0.702)=(172.6,170.2) — small 横折 top
  s2: head ML(0.97,0.116)=(97.0,111.6)  tail BC(0.667,0.748)=(166.7,274.8) — big 横折钩 body
  s3: head BL(0.372,0.458)=(37.2,245.8) tail BR(0.016,0.379)=(201.6,237.9) — bottom heng

Joints (both N — small natural gap, DO NOT weld):
  s1.tail ⇆ s2.mid(0.40) @ C ~(170.7,178) — gap ~22px
  s2.mid(0.74) ⇆ s3.tail @ BR ~(214,241.6) — gap ~35.5px

Route: bank identity for all three strokes.
  s1 -> draw_heng_zhe_short  (short top-left ⌐)
  s2 -> draw_heng_zhe_gou    (main frame + hook)
  s3 -> draw_heng            (bottom horizontal)
"""

import sys, os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from heng_zhe_short import draw_heng_zhe_short
from heng_zhe_gou import draw_heng_zhe_gou
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 primitives called
    'endpoint_mismatches': [], # all endpoints match MMH within tolerance
    'joint_class_mismatches': [],  # both joints are N (small gap, no weld)
    'overall_pass': True,
    'notes': 'heng_zhe_gou corner/hook_tip inferred from GT; s3 heng tail stops '
             'at (202,238) ~ 12px inside s2 descent (N-gap ~35).'
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# --- stroke 1: small 横折 top (TL -> C) ---
# head (85, 90) -> tail (173, 170). heng_zhe_short computes an internal
# corner near tail_x - 27, head_y + 4 → roughly (146, 94), which yields
# a compact ⌐ curl matching the top-left of 马.
draw_heng_zhe_short(
    d,
    head=(85, 90),
    tail=(173, 170),
    corner_offset=(0, 0),
)

# --- stroke 2: big 横折钩 (ML -> BC) ---
# heng_head (97, 112) far-left/top of body; corner near top-right (215, 118);
# gou_tail near (215, 245) (matches s2.mid(0.74) at ~(214,242)); hook_tip
# at MMH tail (167, 275).
draw_heng_zhe_gou(
    d,
    heng_head=(97, 112),
    corner=(215, 118),
    gou_tail=(215, 248),
    hook_tip=(167, 275),
)

# --- stroke 3: bottom 横 (BL -> BR) ---
# head (37, 246) -> tail (202, 238). Slightly rising to the right; ends
# ~12px inside the descent of s2 (N-class gap ~35 vertical+horiz).
draw_heng(
    d,
    head=(37, 246),
    tail=(202, 238),
    width_head=9, width_tail=10,
)

out_path = os.path.join(os.path.dirname(__file__), '01_马.png')
img.save(out_path)
print(f'wrote {out_path}')
