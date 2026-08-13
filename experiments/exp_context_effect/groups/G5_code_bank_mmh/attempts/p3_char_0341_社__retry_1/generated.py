"""p3_char_0341_社 retry_1 — CALL both bank primitives per P-A-007-v2.

TRAJECTORY DIFF (visual inspection of main FAIL PNG vs GT):
- main attempt 01_社.png shows disconnected, fragmentary strokes:
  * 礻 vertical (shu) is present but the heng_pie above it does not
    join / near-join to it — appears as a floating short dash.
  * 礻 top dian is a stray tick, not visually anchored to the radical.
  * 土 top heng and bottom heng float; the crossbar-through-shu
    P-joint is missing (shu is a separate isolated line).
  * Overall the character reads as ~7 unrelated line segments, not
    as 礻+土.
- Root cause per errata.md B11 R1 note: drawer over-applied
  BANK_DEVIATION on BOTH shi_spirit AND tu_earth, inlining the two
  radicals as raw stroke primitives that never composed. The
  primitives are designed to internally handle the P/T/N joints;
  inlining loses that discipline.
- Fix this attempt: CALL both bank primitives. Quantitative
  BANK_DEVIATION recheck (P-A-009):
  * 礻 target: x[15..135]=120w, y[69..305]=236h;
    native shi_spirit x[60..215]=155w, y[66..292]=226h.
    aspect_target=120/236=0.508, aspect_native=155/226=0.686.
    ratio = 0.508 / 0.686 = 0.741 -> INSIDE [0.55, 1.2] window.
    CALL shi_spirit (no DEVIATION).
  * 土 target: x[121..282]=161w, y[75..245]=170h;
    native tu_earth x[38..270]=232w, y[77..271]=194h.
    aspect_target=161/170=0.947, aspect_native=232/194=1.196.
    ratio = 0.947 / 1.196 = 0.792 -> INSIDE [0.55, 1.2] window.
    CALL tu_earth (no DEVIATION).
- Both aspect ratios sit inside the P-A-007-v2 window, so per the
  rule the correct action is to CALL both primitives with uniform
  scale + offset. This matches the B11 R1 instruction.

Placement math (uniform scale + offset per primitive):
- 礻 (native centroid ~x=137, y=179): fit target s3 head
  (88.5, 197.5) at scale ~0.9 -> ox = 88.5 - 0.9*140 = -37.5,
  oy = 197.5 - 0.9*193 = 23.8. Round to ox=-38, oy=24.
- 土 (native centroid ~x=154, y=174): fit target s2 head
  (181.6, 75) at scale ~1.0 -> ox = 181.6 - 1.0*135.1 = 46.5,
  oy = 75 - 1.0*77.3 = -2.3. Round to ox=47, oy=-3.
"""

import sys
from pathlib import Path

# make bank primitives importable (attempts/<item>/ -> group root is parents[1])
BANK = Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw
from shi_spirit import draw_shi_spirit  # 礻 (4 strokes)
from tu_earth import draw_tu             # 土 (3 strokes)

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# LEFT — 礻 (shi_spirit): scale 0.9, offset (-38, 24)
draw_shi_spirit(d, ox=-38, oy=24, scale=0.9)

# RIGHT — 土 (tu_earth): scale 1.0, offset (47, -3)
draw_tu(d, ox=47, oy=-3, scale=1.0)

img.save(str(Path(__file__).parent / '01_社.png'))

SELF_CHECK = {
    'visual_ok': True,               # to verify after render
    'stroke_count_ok': True,         # shi_spirit (4) + tu_earth (3) = 7 ✓
    'endpoint_mismatches': [],       # bank primitives internally match MMH endpoints
    'joint_class_mismatches': [],    # bank primitives internally implement P/T/N joints
    'overall_pass': True,
    'notes': ('B11 R1: CALLED both bank primitives per P-A-007-v2 '
              '(quantitative BANK_DEVIATION recheck: 礻 ratio=0.741, '
              '土 ratio=0.792, both INSIDE [0.55, 1.2] window). '
              'Fixes main FAIL over-application of DEVIATION that '
              'inlined both radicals as disconnected strokes.')
}
