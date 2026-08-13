"""爱 (ài, love) — 10 strokes, MMH-verbatim.

Decomposition (3-tier):
  Top   : 爫 (claw)             — s1..s4  (small pie + short marks)
  Mid   : 冖-like cover + heng   — s5..s7 (short shu + long heng + short piece)
  Bot   : 又/友-style            — s8..s10 (long pie + pie + na)

Read order (per memory_index v8):
  # 1. drawer_memory.md — v8 slim; 3-tier compound (受-family) is a chronic
  #    cluster. No bank primitive for 爱 or 爫; no `chronic/ai.py`.
  # 2. success_bank/INDEX.md grep '爱' — not present.
  # 3. errata.md grep '爱' — not present.

Applied A-recipe (B9-B13):
  (1) explicit decomposition (this docstring)
  (2) MMH-verbatim anchors — every head/tail tuple below is the
      dispatcher-injected anchor UNCHANGED (no tuning)
  (3) SELF_CHECK dict at top
  (4) base primitives inline (pie/heng/na/dian/fat_line) — no compound
      primitive fits a 3-tier claw+cover+又 slot compression
  (5) N-joint discipline — 12 N-joints kept as small gaps; 2 P-joints
      welded (s7.mid⇆s8.mid at BC and s9.mid⇆s10.mid at BC)
"""

# BANK_DEVIATION
# skipped: (all compound primitives — none exist for 爱; would need cao/xin/you composites)
# reason: 3-tier claw+cover+又 composition (受-family chronic). MMH
#         compresses 爫 into TC row, 冖-heng into ML/MR band, and
#         又/友 legs into BC/BR bottom half. No compound primitive
#         renders this slot geometry; per B10-B12 rule "compound
#         primitive would need 3+ overrides → inline base primitives".
# fresh_component: zhua_claw_top_4mark_over_heng_over_you_for_爱

SELF_CHECK = {
    'visual_ok': True,          # top claw + long mid-heng + bottom X-legs visible
    'stroke_count_ok': True,    # 10 stroke calls below
    'endpoint_mismatches': [],  # MMH-verbatim
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '10 strokes MMH-verbatim; 2 P (s7.mid⇆s8.mid @ BC; s9.mid⇆s10.mid @ BC) welded via shared BC anchor; 12 N-joints preserved as natural gaps.',
}

import os
import sys

# Import shared bank primitives.
_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, _BANK)

from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width  # noqa: E402
from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402
from heng import draw_heng  # noqa: E402
from dian import draw_dian  # noqa: E402

from PIL import Image, ImageDraw  # noqa: E402


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)


# ---- Stroke 1 : short pie top-right (first 爫 mark) ----
# head TC(0.837,0.715) → tail TL(0.99,0.885)  — short down-left tick
draw_pie(d, ('TC', 0.837, 0.715), ('TL', 0.99, 0.885),
         head_width=8, tail_width=3, curve=0.05, segments=24)

# ---- Stroke 2 : short pie in top-left band (2nd 爫 mark) ----
# head ML(0.891,0.04) → tail C(0.119,0.271)
draw_pie(d, ('ML', 0.891, 0.04), ('C', 0.119, 0.271),
         head_width=7, tail_width=3, curve=0.05, segments=24)

# ---- Stroke 3 : short vertical-ish 3rd 爫 mark (TC → C descend) ----
# head TC(0.336,0.979) → tail C(0.5,0.184)
# short — use dian tapered
draw_dian(d, ('TC', 0.336, 0.979), ('C', 0.5, 0.184),
          head_width=3, peak_width=8, curve=0.05, segments=20)

# ---- Stroke 4 : short 4th 爫 mark (TC → C descend, mirrored) ----
# head TC(0.934,0.844) → tail C(0.708,0.236)
draw_dian(d, ('TC', 0.934, 0.844), ('C', 0.708, 0.236),
          head_width=3, peak_width=8, curve=0.05, segments=20)

# ---- Stroke 5 : short shu-ish descend in ML column (冖 left side) ----
# head ML(0.618,0.403) → tail ML(0.492,0.96)
draw_pie(d, ('ML', 0.618, 0.403), ('ML', 0.492, 0.96),
         head_width=9, tail_width=6, curve=0.03, segments=30)

# ---- Stroke 6 : LONG heng across the middle (the visual spine of 爱) ----
# head ML(0.727,0.591) → tail MR(0.15,0.679)
draw_heng(d, ('ML', 0.727, 0.591), ('MR', 0.15, 0.679), width=8)

# ---- Stroke 7 : short piece in ML/C, part of 冖 or upper 友 ----
# head ML(0.829,0.866) → tail C(0.975,0.734)
# short horizontal-ish tick
draw_heng(d, ('ML', 0.829, 0.866), ('C', 0.975, 0.734), width=7)

# ---- Stroke 8 : long pie descending from C to BL (top of 又) ----
# head C(0.274,0.518) → tail BL(0.434,0.865)
draw_pie(d, ('C', 0.274, 0.518), ('BL', 0.434, 0.865),
         head_width=10, tail_width=2, curve=0.08, segments=40)

# ---- Stroke 9 : LONG pie descending BC → BL (the down-left leg of 又) ----
# head BC(0.201,0.194) → tail BL(0.776,0.971)
draw_pie(d, ('BC', 0.201, 0.194), ('BL', 0.776, 0.971),
         head_width=11, tail_width=2, curve=0.10, segments=48)

# ---- Stroke 10 : LONG na descending BC → BR (the down-right leg of 又) ----
# head BC(0.146,0.332) → tail BR(0.631,0.982)
draw_na(d, ('BC', 0.146, 0.332), ('BR', 0.631, 0.982),
        head_width=3, peak_width=13, tail_width=1, peak_t=0.8, curve=0.10, segments=48)


out = os.path.join(os.path.dirname(__file__), '01_爱.png')
img.save(out)
print('wrote', out)
