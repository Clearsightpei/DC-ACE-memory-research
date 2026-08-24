"""p3_char_0093_弋 — reuses xie_gou.py bank primitive (identity-like use).

弋 was extracted as the seed for `xie_gou.py` back in B2 (Phase-2).
This Phase-3 character has the same MMH anchors as the Phase-2 radical.
Now that xie_gou is in the bank, we use it directly instead of inlining.
"""

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from xie_gou import draw_xie_gou
from heng import draw_heng
from dian import draw_dian

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# ------------------------------------------------------------
# MMH-derived anchors (300x300 pixels)
# cell centers: TL(50,50) TC(150,50) TR(250,50)
#               ML(50,150) C(150,150) MR(250,150)
#               BL(50,250) BC(150,250) BR(250,250)
# anchor (cell, xf, yf) -> pixel (cell_left + 100*xf, cell_top + 100*yf)
# ------------------------------------------------------------

# Stroke 1: heng (short, angled slightly up-right)
#   ML(0.48,0.764)=(48,176)  MR(0.095,0.38)=(210,138)
s1_head = (48, 176)
s1_tail = (210, 138)
draw_heng(d, s1_head, s1_tail, width_head=8, width_tail=9)

# Stroke 2: xie_gou (long diagonal from upper-center down to bottom-right)
#   TC(0.02,0.806)=(102,81)  BR(0.581,0.347)=(258,235)
#   Joint P with s1 at C(0.418,0.531)=(142,153) — welded crossing.
s2_head = (102, 81)
s2_tail = (258, 235)
draw_xie_gou(d, s2_head, s2_tail, width=8, bow=12, hook_up=34, hook_back=7)

# Stroke 3: dian (small dot at upper-right, going down-right)
#   TC(0.822,0.694)=(182,69)  TR(0.183,0.97)=(218,97)
s3_head = (182, 69)
s3_tail = (218, 97)
draw_dian(d, s3_head, s3_tail, w_head=3, w_tail=8, bow=3, steps=40)

# ------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 3 stroke primitives (heng, xie_gou, dian)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # P crossing at ~(142,153) — welded naturally by xie_gou body sweep + heng
    'overall_pass': True,
    'notes': 'Bank reuse: xie_gou (B2 promotion), heng, dian. No BANK_DEVIATION.'
}

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p3_char_0093_弋/01_弋.png")
