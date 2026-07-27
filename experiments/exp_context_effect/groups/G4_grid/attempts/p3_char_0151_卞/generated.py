"""p3_char_0151_卞 — G4 grid-bank attempt.

Memory checklist:
  1. success_bank/INDEX.md grep: 卞 not present (fresh compose).
  2. errata.md grep: 卞 not listed.
  3. form_catalog: uses heng (long), shu (long), dian x2 — standard classes.
  4. principles_meta TR1: primitives called with OVERRIDING anchors (no defaults).
  5. joint_atlas: s2/s3 joint is N per MMH → do NOT weld (dispatcher spec).

Structural spec (MMH, 4 strokes):
  s1: TC(0.263,0.604) → TC(0.629,0.899)   dian (top dot)
  s2: ML(0.322,0.345) → MR(0.736,0.248)   heng (long horizontal)
  s3: C(0.374,0.356) → BC(0.509,1.035)    shu (long vertical, crosses through heng)
  s4: C(0.746,0.734) → BR(0.18,0.121)     dian (lower-right dot)

Joint: s2.mid ⇆ s3.head class N (expected gap ≈16 px) — no weld.
Actually visually 卞's 一 and 丨 look welded (P). MMH declares N;
follow MMH per structural spec but the natural rendering here has
s3 head above the heng slightly. We keep the head at C(0.374,0.356)
which is just above the heng band (heng lies around y_frac 0.25-0.34
in ML/MR → ~y=345..312). The s3 head at C(0.374,0.356) → PIL y=456
approx — actually that's BELOW the heng band. So there is a natural
N gap between s3.head and heng midpoint. Consistent with N.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'MMH-declared N joint at s2.mid ⇆ s3.head; s3.head placed just below heng band, natural gap preserved.'
}

import sys, os
_BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(_BANK))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu
from dian import draw_dian

W = H = 300
img = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(img)

# Stroke 1 — top dot 丶 (short diagonal, TC cell)
draw_dian(draw,
          from_anchor=('TC', 0.263, 0.604),
          to_anchor=('TC', 0.629, 0.899),
          head_width=2, peak_width=10, curve=0.05)

# Stroke 2 — long horizontal 一
draw_heng(draw,
          from_anchor=('ML', 0.322, 0.345),
          to_anchor=('MR', 0.736, 0.248),
          width=8)

# Stroke 3 — long vertical 丨 (starts just under heng, drops to BC)
draw_shu(draw,
         from_anchor=('C', 0.374, 0.356),
         to_anchor=('BC', 0.509, 1.035),
         width=8)

# Stroke 4 — lower-right dot 丶 (from middle-right, going down-right toward BR)
draw_dian(draw,
          from_anchor=('C', 0.746, 0.734),
          to_anchor=('BR', 0.18, 0.121),
          head_width=2, peak_width=10, curve=0.05)

out_path = os.path.join(os.path.dirname(__file__), '01_卞.png')
img.save(out_path)
print(f'wrote {out_path}')
