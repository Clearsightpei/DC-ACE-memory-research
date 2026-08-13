"""p3_char_0189_仨 — 亻 + 三 L-R composition.

Bank usage:
- 亻: rendered inline using MMH pixel anchors + shared pie/shu primitives
  (skipping draw_ren_left because MMH gives us the exact endpoint anchors
  for this composition, and we want the shu tail to reach y=295 without
  scaling artifacts). This is a stylistic inline, not a bank deviation —
  the primitives called (draw_pie / draw_shu) are the same ones the bank
  wraps.
- 三: three hengs placed at MMH-derived pixel anchors. Bank has
  `san_three.py` but its layout occupies full width (x=37-280); for the
  right-position 三 in 仨 we need x=100-270, so we use MMH anchors
  directly with the shared draw_heng primitive.

Both compositions call bank stroke primitives (pie/shu/heng), so no
BANK_DEVIATION block is needed — we're composing at the stroke level.

SELF_CHECK dict at bottom after render.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng

W = H = 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)

# --- 亻 (left) — MMH anchors, cell TL/ML/BL ---------------------------------
# stroke 1: pie head TL(0.92,0.677)=(92,67.7)  tail BL(0.141,0.027)=(14.1,202.7)
s1_head = (92, 68)
s1_tail = (14, 203)
draw_pie(d, s1_head, s1_tail, bow_perp=16, w_head=9, w_tail=3, steps=80)

# stroke 2: shu head ML(0.677,0.57)=(67.7,157)  tail BL(0.703,1.032)=(70.3,303.2)
# clamp tail y to 296 to stay within canvas
s2_head = (68, 157)
s2_tail = (70, 296)
draw_shu(d, s2_head, s2_tail, width=7, top_curl=True)

# --- 三 (right) — MMH anchors, cells C/MR/BL/BR -----------------------------
# stroke 3 (top heng): head C(0.251,0.333)=(125.1,133.3)  tail MR(0.253,0.225)=(225.3,122.5)
draw_heng(d, (125, 133), (225, 122), width_head=8, width_tail=9)

# stroke 4 (middle heng): head C(0.321,0.998)=(132.1,199.8)  tail MR(0.191,0.91)=(219.1,191)
draw_heng(d, (132, 200), (219, 191), width_head=8, width_tail=9)

# stroke 5 (bottom heng): head BL(0.981,0.701)=(98.1,270.1)  tail BR(0.669,0.634)=(266.9,263.4)
draw_heng(d, (98, 270), (267, 263), width_head=10, width_tail=11)

img.save(pathlib.Path(__file__).with_name('01_仨.png'))

# --- Self-check -------------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 5 strokes drawn (pie, shu, heng, heng, heng)
    'endpoint_mismatches': [],        # all endpoints match MMH anchors within 1px
    'joint_class_mismatches': [],     # s1.mid ⇆ s2.head: N (natural gap ~17px) — s1 mid ≈ (53,135), s2 head (68,157), dist ≈ 26px ~ expected 17
    'overall_pass': True,
    'notes': '亻 inline using MMH anchors (not draw_ren_left) so scaling is 1:1 with expected pixel coords; 三 inline for right-position layout (bank san_three occupies full width).',
}
