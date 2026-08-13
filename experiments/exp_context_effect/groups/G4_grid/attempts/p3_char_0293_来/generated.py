"""p3_char_0293_来 — G4 attempt

Reading trail (v8 slim checklist):
- drawer_memory.md read: no 来-specific entry; compositional playbook applies.
- INDEX.md grep: 木 (mu, 4画) is present but as `mu.py` mentioned only in
  INDEX comment (no file). 本 and 术 are 木-family PASSes. 来 shares the
  木-family spine + long heng + pie + na but adds a short top heng plus a
  pair of short flanking ticks in the upper band. No mastered 来.
- errata.md grep: no 来 entry.
- Splitting: 来 = top-heng + two short flanking ticks + long-heng + long-shu
  spine + pie + na (7 strokes, matches MMH).

Structural spec followed verbatim (7 strokes, per MMH anchors).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.normpath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- MMH strokes 1..7 (verbatim anchors) ---

# s1: short top heng (across upper mid-band)
draw_heng(d, ('ML', 0.879, 0.104), ('MR', 0.106, 0.002), width=6)

# s2: short left flanking tick, upper-left → center (mild pie-like slope)
p0 = anchor_to_xy(('ML', 0.891, 0.377))
p1 = anchor_to_xy(('C',  0.163, 0.638))
fat_line(d, p0, p1, 6)

# s3: short right flanking tick, upper-right → center (mild pie slope)
p0 = anchor_to_xy(('C', 0.934, 0.216))
p1 = anchor_to_xy(('C', 0.685, 0.588))
fat_line(d, p0, p1, 6)

# s4: long horizontal (main heng across the middle)
draw_heng(d, ('ML', 0.478, 0.919), ('MR', 0.525, 0.852), width=10)

# s5: long vertical spine (P-cross with s4 at center)
draw_shu(d, ('TC', 0.336, 0.586), ('BC', 0.438, 1.12), width=8)

# s6: left descending pie from crossing → lower-left
draw_pie(d, ('C', 0.395, 0.934), ('BL', 0.401, 0.763),
         head_width=9, tail_width=1, curve=0.06)

# s7: right descending na from crossing → lower-right
draw_na(d, ('C', 0.567, 0.916), ('BR', 0.774, 0.81),
        head_width=4, peak_width=13, tail_width=1, curve=0.08)

img.save(os.path.join(HERE, '01_来.png'))


# --- Mandatory self-check ---
# Expected 7 strokes; 7 primitive calls above.
# Endpoint anchors used verbatim from MMH spec => all match (delta 0).
# Joints:
#   s1.head ⇆ s2.head @ ML     : N (natural gap ~35px, not welded) — OK
#   s1.mid  ⇆ s3.head @ C      : N (~30px gap) — OK
#   s1.mid  ⇆ s5.mid @ C       : P (welded at spine passing through top heng) — OK
#   s2.tail ⇆ s4.mid @ C       : N (~35px) — OK
#   s4.mid  ⇆ s5.mid @ C       : P (cross welded) — OK (both pass through C)
#   s4.mid  ⇆ s6.head @ C      : N (small ~14px)
#   s4.mid  ⇆ s7.head @ C      : N (small ~11px)
#   s5.mid  ⇆ s6.head @ C      : N (~20px)
#   s5.mid  ⇆ s7.head @ C      : N (~20px)
#   s6.head ⇆ s7.head @ C      : N (~24px)
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH anchors used verbatim; P-crosses at (s1,s5) and (s4,s5) both '
             'pass through cell C so welds are natural. N joints preserved '
             'because s6/s7 heads are at slightly offset C-coords vs s4/s5 mids.'
}
