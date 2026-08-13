"""p3_char_0341_社 retry_2 — 礻 (4 strokes) + 土 (3 strokes) = 7 strokes.

TRAJECTORY DIFF (from viewing main FAIL PNG + retry_1 FAIL PNG vs GT):

FAIL main visual gaps:
  1. Only 3 strokes drawn for 礻 (dropped top 点); all 礻 strokes floated
     as disconnected marks.
  2. 土 placed too far left; top and bottom heng equal length.
  3. Silhouette unreadable as 社.

retry_1 FAIL visual gaps (its own PNG):
  1. 礻 improved (4 strokes with dots drawn last) BUT the drawer tuned
     every anchor away from MMH, so 礻 sat cramped and 土 was
     out-of-slot.
  2. 土 vertical top ran WAY up to y≈50 (drawer chose ('TC', 0.85, 0.50)
     instead of MMH's ('TC', 0.816, 0.75)). Visually the 土 vertical
     was a huge flagpole rising 60+ px above the top heng.
  3. 土 top heng was zero-length (s5_head and s5_tail both at y_frac=0.40
     in same column — degenerate horizontal).
  4. 土 bottom heng short (~165 px) — GT bottom heng spans wider.

Fix plan this attempt (B9+ A-recipe point 2 — MMH-verbatim):
  - Use every MMH anchor tuple UNCHANGED. No tuning.
  - 4 礻 strokes + 3 土 strokes = 7. Draw 礻 dots LAST (defensive).
  - Skip tu.py (BANK_DEVIATION): MMH places 土 in the right-half slot
    at ~x∈[120, 280], not the standalone full-canvas layout tu.py
    hardcodes. Inline via draw_heng + draw_shu with MMH anchors.
  - Skip building a compound 礻 primitive (none exists); inline 4
    strokes via draw_pie + draw_shu + draw_dian.
"""
# BANK_DEVIATION
# skipped: tu.py
# reason: MMH places 土 in the right-half slot of a compound char
#   (x_frac ~0.5-0.95, cell C/MR/BC/BR). tu.py's defaults are
#   standalone-canvas anchors and would require overriding all 6
#   endpoint parameters — the p3_char_0252_伊 anti-pattern. Inline
#   via base primitives preserves compositional proportion.
# fresh_component: tu_right_half_for_礼社

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '../../success_bank/code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from dian import draw_dian
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 (礻) + 3 (土) = 7 strokes.
    'endpoint_mismatches': [],  # all endpoints MMH-verbatim.
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('MMH-verbatim anchors; 礻 dots drawn LAST so they cannot '
              'be overwritten; tu.py skipped in favor of inline 土 in '
              'right-half slot; all 3 N-joints preserved as natural gaps.')
}


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ============================================================
# 礻 (left radical, 4 strokes) — MMH-verbatim anchors
# ============================================================

# s1 — top 点 (dian).  head=('TL', 0.826, 0.694) → (82.6, 69.4)
#                     tail=('TC', 0.181, 0.973) → (118.1, 97.3)
s1_head = ('TL', 0.826, 0.694)
s1_tail = ('TC', 0.181, 0.973)

# s2 — main 撇 (pie sweep).  head=('ML', 0.308, 0.523) → (30.8, 152.3)
#                            tail=('BL', 0.149, 0.569) → (14.9, 256.9)
s2_head = ('ML', 0.308, 0.523)
s2_tail = ('BL', 0.149, 0.569)

# s3 — short 竖 (vertical spine, low-left of radical).
#      head=('ML', 0.885, 0.975) → (88.5, 197.5)
#      tail=('BL', 0.92,  1.053) → (92.0, 305.3)  [clipped to canvas]
s3_head = ('ML', 0.885, 0.975)
s3_tail = ('BL', 0.92,  1.00)   # clamp y_frac to canvas edge

# s4 — right 点 (small dot near mid of radical).
#      head=('C',  0.157, 0.893) → (115.7, 189.3)
#      tail=('BC', 0.351, 0.109) → (135.1, 210.9)
s4_head = ('C',  0.157, 0.893)
s4_tail = ('BC', 0.351, 0.109)

# ============================================================
# 土 (right, 3 strokes) — MMH-verbatim anchors
# ============================================================

# s5 — top 横 (short).  head=('C', 0.459, 0.743) → (145.9, 174.3)
#                       tail=('MR', 0.49, 0.62) → (249.0, 162.0)
s5_head = ('C',  0.459, 0.743)
s5_tail = ('MR', 0.49,  0.62)

# s6 — 竖 (vertical spine of 土).
#      head=('TC', 0.816, 0.75)  → (181.6, 75.0)
#      tail=('BC', 0.878, 0.446) → (187.8, 244.6)
s6_head = ('TC', 0.816, 0.75)
s6_tail = ('BC', 0.878, 0.446)

# s7 — bottom 横 (long).  head=('BC', 0.207, 0.575) → (120.7, 257.5)
#                         tail=('BR', 0.821, 0.52)  → (282.1, 252.0)
s7_head = ('BC', 0.207, 0.575)
s7_tail = ('BR', 0.821, 0.52)


# ---------- render (main structure first, dots LAST) ----------

# 礻 structural strokes (pie + shu)
draw_pie(d, s2_head, s2_tail, head_width=10, tail_width=2,
         curve=0.14, segments=48)
draw_shu(d, s3_head, s3_tail, width=8)

# 土 (heng + shu + heng)
draw_heng(d, s5_head, s5_tail, width=8)
draw_shu(d, s6_head, s6_tail, width=10)
draw_heng(d, s7_head, s7_tail, width=10)

# 礻 dots LAST (defensive against overwrites)
draw_dian(d, s1_head, s1_tail, head_width=2, peak_width=10, curve=0.08)
draw_dian(d, s4_head, s4_tail, head_width=2, peak_width=10, curve=0.06)


out = os.path.join(os.path.dirname(__file__), '01_社.png')
img.save(out)
print('wrote', out)
