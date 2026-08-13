"""p3_char_0207_册 — G5 attempt.

册 (ce, "book"): 5-stroke character. Two mirrored frames joined by a
long horizontal that pierces both left and right frames.

MMH-injected structural expectations:
  s1: TL(.706,.899) -> BL(.407,.909)  = left long 撇 (top-right of TL,
      descending to bottom-left of BL)
  s2: TL(.917,.987) -> BL(.905,.569)  = left vertical (right edge of
      left frame, top to mid)
  s3: TC(.585,.847) -> BC(.318,.947)  = middle 撇 (descending)
  s4: TC(.764,.861) -> BC(.846,.684)  = right vertical (slight drift)
  s5: ML(.281,.770) -> MR(.792,.731)  = long horizontal pierces both
      frames (P joints with s1, s2, s3, s4)

Anchor→pixel conversion (image-down, 300x300, 3x3 米字格 cells 100px):
  cell origins: TL(0,0) TC(100,0) TR(200,0)
                ML(0,100) C(100,100) MR(200,100)
                BL(0,200) BC(100,200) BR(200,200)
  s1 head=(70.6, 89.9)   tail=(40.7, 290.9)
  s2 head=(91.7, 98.7)   tail=(90.5, 256.9)
  s3 head=(158.5, 84.7)  tail=(131.8, 294.7)
  s4 head=(176.4, 86.1)  tail=(184.6, 268.4)
  s5 head=(28.1, 177.0)  tail=(279.2, 173.1)

Joints (from MMH block):
  s1-s2 N (top-left gap ~14px)  — heads separate, don't weld
  s3-s4 N (top-mid gap ~15px)   — heads separate, don't weld
  s2-s3 tail N (~30px gap)      — the middle interior area
  s1-s5 P, s2-s5 P, s3-s5 P, s4-s5 P — the horizontal welds all 4 verticals

Bank uses: pie, shu, heng — all fit cleanly, no deviation needed.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Two mirror frames + long horizontal. All joints natural given straight-line strokes crossing the horizontal.',
}

import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng

img = Image.new('L', (300, 300), 255)
d = ImageDraw.Draw(img)

# --- stroke 1: left 撇 (nearly vertical body, soft leftward tail — 竖撇) ---
# Use a small bow so it reads as an upright frame edge with a gentle sweep.
draw_pie(d, head=(75, 90), tail=(38, 288),
         bow_perp=5, w_head=6, w_tail=3, steps=90)

# --- stroke 2: left vertical (right edge of left frame) ---
draw_shu(d, head=(92, 99), tail=(90, 257), width=7)

# --- stroke 3: middle 撇 (right frame's left descending stroke) ---
draw_pie(d, head=(160, 85), tail=(130, 292),
         bow_perp=5, w_head=6, w_tail=3, steps=90)

# --- stroke 4: right vertical (right frame's right edge, slight rightward drift) ---
draw_shu(d, head=(176, 86), tail=(185, 268), width=7)

# --- stroke 5: long horizontal piercing both frames ---
draw_heng(d, head=(28, 176), tail=(278, 174),
          width_head=6, width_tail=7)

out_path = os.path.join(os.path.dirname(__file__), '01_册.png')
img.save(out_path)
print(f'wrote {out_path}')
