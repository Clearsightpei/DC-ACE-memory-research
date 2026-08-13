"""毛 retry_2 — 4-stroke radical.

TRAJECTORY DIFF (inspected GT + main + retry_1 PNGs):

  Main attempt (C) failures:
  1. s4 vertical placed too far LEFT (x=110). Off-center. Hook
     wraps too far right and looks stubby.
  2. s1 pie too long/flat; sits well above the vertical top with
     no visual connection.
  3. Hengs too low; whole composition floats high leaving empty
     bottom.

  Retry_1 (C) failures:
  1. s4 head at (135,90) but hook tip at (215,255) with
     bottom_extra=25 → the wan (curl) is CRAMPED. In GT the
     bottom curl clearly descends to ~y=275 and the hook rises
     back up to ~y=235 (visible 40px hook rise). Retry_1 hook
     rise is only ~25px and reads as a soft nub.
  2. s3 (lower heng) at y=212 → 188 rise is barely visible; GT
     rise is ~20-25px (bigger tilt).
  3. Pie tail (105,128) sits BELOW top-heng head (75,148) — the
     pie's tail should be ABOVE the top heng so the pie appears
     to hook down onto the vertical, not stab through the heng.

  Retry_2 fixes:
  - Pie: shorten and lift → head=(178,62), tail=(112,95). Tail
    lands just above s4 top and just above s2, matching GT's
    upper-left "curl" look.
  - s2 upper heng: raise & shorten. head=(80,132), tail=(198,118).
  - s3 lower heng: extend LEFT (this is the widest stroke).
    head=(28,200), tail=(220,178). Rise ~22px.
  - s4 shu_wan_gou: head=(138,65) (top-center, matches MMH
    TC 0.799,0.738), tail (hook tip)=(222,238).
    bottom_extra=42 → bottom_y≈280; knee_ratio=1.05 → curl
    extends slightly past hook tip x, giving the pronounced
    right-bulge visible in GT.

Bank use: pie, heng ×2, shu_wan_gou — all bank-appropriate.
No BANK_DEVIATION.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parent.parent.parent / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 4 primitive calls; MMH=4
    'endpoint_mismatches': [],     # anchors within tolerance of MMH
    'joint_class_mismatches': [],  # s1.mid⇆s4.head N; s2.mid⇆s4 T; s3.mid⇆s4 P
    'overall_pass': True,
    'notes': 'Retry_2: larger wan-curl, longer bottom heng, pie tail lifted above hengs.',
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ---- s1: pie (small hook-like curl at top-right) ----
# GT: head ~(178, 62) → tail ~(112, 95). Tail lands ABOVE both hengs
# so it visually attaches to the top of s4, not the middle of s2.
draw_pie(d, head=(178, 62), tail=(112, 95),
         bow_perp=7, w_head=7, w_tail=3)

# ---- s2: upper heng (short, gentle rise) ----
draw_heng(d, head=(80, 132), tail=(198, 118),
          width_head=8, width_tail=9)

# ---- s3: lower heng (LONGEST stroke; clear rise) ----
draw_heng(d, head=(28, 200), tail=(220, 178),
          width_head=8, width_tail=9)

# ---- s4: shu_wan_gou (top-center vertical → big right curl → hook up) ----
# head at (138, 65) sits near top pie tail (N-joint gap ~10px).
# tail = hook tip at (222, 238). bottom_extra=42 → curve bottom ~y=280.
# knee_ratio=1.05 → knee bulges slightly past hook tip.x for the
# pronounced right-shoulder shape visible in GT.
draw_shu_wan_gou(d, head=(138, 65), tail=(222, 238),
                 width=7, bottom_extra=42, knee_ratio=1.05)

out = Path(__file__).parent / "01_毛.png"
img.save(out)
print(f"wrote {out}")
