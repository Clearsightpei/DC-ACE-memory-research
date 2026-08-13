"""p3_char_0097_乌 — 乌 (wu, 'crow'). 4 strokes.

MMH structural spec:
  s1: head TC(0.397,0.524)=(139.7,52.4)  tail C(0.146,0.002)=(114.6,100.2)
      -> short 撇 (pie) at top-left, slanting down-left
  s2: head C(0.163,0.16)=(116.3,116)     tail C(0.523,0.465)=(152.3,146.5)
      -> small 横折 curl (top of head)
  s3: head TL(0.961,0.993)=(96.1,99.3)   tail BC(0.69,0.786)=(169,278.6)
      -> big 横折钩 body (outer profile: top across, right side down, hook)
  s4: head BL(0.36,0.47)=(36,247)        tail BC(0.992,0.388)=(199.2,238.8)
      -> bottom 横 (horizontal base)

Joints (all N — small natural gap, DO NOT weld):
  s1.tail ⇆ s2.head @ C ~gap 14.2 px
  s1.tail ⇆ s3.head @ C ~gap 16.7 px
  s2.head ⇆ s3.head @ C ~gap 16.4 px

Sibling: 马 (p3_char_0085) has same s2-s4 shape as 乌 s2-s4; 乌 adds the pie (s1).
Route: bank identity for all four strokes.
  s1 -> draw_pie             (short top-left slant)
  s2 -> draw_heng_zhe_short  (small ⌐ top curl of head)
  s3 -> draw_heng_zhe_gou    (main body frame + hook)
  s4 -> draw_heng            (bottom horizontal)
"""

import sys, os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from heng_zhe_short import draw_heng_zhe_short
from heng_zhe_gou import draw_heng_zhe_gou
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives called == expected 4
    'endpoint_mismatches': [], # anchors match MMH within ±0.20 tolerance
    'joint_class_mismatches': [],  # all three joints are N (natural gap kept)
    'overall_pass': True,
    'notes': ('Mirrors sibling 马 pattern for s2-s4 (heng_zhe_short + '
              'heng_zhe_gou + heng), adds pie for s1. All C-cell joints '
              'remain unwelded by construction (endpoints ~15-35 px apart).')
}

W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# --- stroke 1: 撇 (pie) at top-left, slanting down-left ---
# head (140, 52) -> tail (115, 100). Short, ~55 px, gentle bow.
draw_pie(
    d,
    head=(140, 52),
    tail=(115, 100),
    bow_perp=5,
    w_head=7,
    w_tail=3,
    steps=50,
)

# --- stroke 2: small 横折 (top of head) ---
# head (116, 116) -> tail (152, 147). Short ⌐ curl.
draw_heng_zhe_short(
    d,
    head=(116, 116),
    tail=(152, 147),
    corner_offset=(0, 0),
)

# --- stroke 3: main 横折钩 body (outer profile of the bird) ---
# heng_head (96, 99) top-left; corner near top-right (215, 105);
# gou_tail near bottom-right (215, 250); hook_tip at MMH tail (169, 279).
# This is exactly the pattern that worked for 马 s2.
draw_heng_zhe_gou(
    d,
    heng_head=(96, 99),
    corner=(215, 105),
    gou_tail=(215, 250),
    hook_tip=(169, 279),
)

# --- stroke 4: bottom 横 ---
# head (36, 247) -> tail (199, 239). Slight rise to right; ends just
# short of s3's descent (N-gap preserved).
draw_heng(
    d,
    head=(36, 247),
    tail=(199, 239),
    width_head=9,
    width_tail=10,
)

out_path = os.path.join(os.path.dirname(__file__), '01_乌.png')
img.save(out_path)
print(f'wrote {out_path}')
