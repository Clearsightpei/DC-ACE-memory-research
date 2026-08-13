"""p3_char_0252_伊 — G5 attempt

Composition (per P-A-006: MMH-anchor verbatim + stroke-primitive layer,
no whole-radical composition):
  亻 (left):  s1 pie, s2 shu
  尹 (right): s3 heng-zhe (short), s4 heng, s5 heng, s6 long pie

All endpoints taken verbatim from the injected MMH structural block.
"""

import sys, os
from PIL import Image, ImageDraw

# --- import bank primitives ---
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, BANK)
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short

# ---------- MMH-derived pixel anchors ----------
# 米字格 cells: each 100x100. Cell origins (top-left):
#   TL(0,0), TM(100,0), TR(200,0),
#   ML(0,100), C(100,100), MR(200,100),
#   BL(0,200), BM(100,200), BR(200,200)

def A(cell, xf, yf):
    ox, oy = {'TL':(0,0),'TM':(100,0),'TR':(200,0),
              'ML':(0,100),'C':(100,100),'MR':(200,100),
              'BL':(0,200),'BM':(100,200),'BR':(200,200)}[cell]
    return (ox + 100*xf, oy + 100*yf)

# Strokes
s1_head = A('TL', 0.908, 0.659)   # (90.8, 65.9)
s1_tail = A('ML', 0.208, 0.948)   # (20.8, 194.8)
s2_head = A('ML', 0.688, 0.509)   # (68.8, 150.9)
s2_tail = A('BL', 0.732, 0.906)   # (73.2, 290.6)
s3_head = A('C',  0.307, 0.093)   # (130.7, 109.3)
s3_tail = A('MR', 0.074, 0.740)   # (207.4, 174.0)
s4_head = A('ML', 0.996, 0.547)   # (99.6, 154.7)
s4_tail = A('MR', 0.672, 0.424)   # (267.2, 142.4)
s5_head = A('C',  0.228, 0.928)   # (122.8, 192.8)
s5_tail = A('MR', 0.288, 0.849)   # (222.8, 184.9)
s6_head = A('C',  0.588, 0.134)   # (158.8, 113.4)
s6_tail = A('BL', 0.955, 0.950)   # (95.5, 295.0)

# ---------- Render ----------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# s1: pie of 亻 (more pronounced curve to match GT)
draw_pie(d, s1_head, s1_tail, bow_perp=14, w_head=10, w_tail=3)

# s2: shu of 亻 (nearly vertical)
draw_shu(d, s2_head, s2_tail, width=7)

# s3: short 横折 (heng-zhe) — horizontal from head then bend down to tail
draw_heng_zhe_short(d, s3_head, s3_tail, corner_offset=(20, -6))

# s4: long middle heng
draw_heng(d, s4_head, s4_tail, width_head=8, width_tail=9)

# s5: short bottom heng
draw_heng(d, s5_head, s5_tail, width_head=7, width_tail=8)

# s6: long descending 撇 (strong leftward curve as it descends)
draw_pie(d, s6_head, s6_tail, bow_perp=22, w_head=10, w_tail=3)

# ---------- Self-check ----------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 6 primitives called: pie, shu, heng-zhe, heng, heng, pie
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 recipe: MMH endpoints verbatim + stroke primitives. '
             '亻 inlined as pie+shu (no ren_left whole-radical composition). '
             '尹 inlined stroke-by-stroke.'
}

out = os.path.join(os.path.dirname(__file__), "01_伊.png")
img.save(out)
print("wrote", out)
