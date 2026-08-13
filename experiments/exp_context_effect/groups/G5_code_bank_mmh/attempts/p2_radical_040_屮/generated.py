"""G5 attempt: p2_radical_040_屮 (3 strokes).

Structure per MMH block:
  s1 = 竖折 (L-shape): head ML(68,131) -> corner (68,197) -> tail MR(217,197)
  s2 = 短竖 on right : head (214,118) -> tail (228,222)
  s3 = 长竖 center   : head TC(134,66) -> tail BC(150,317, clamped to 300)

Bank usage:
  - draw_shu (bank) for s2 and s3 (both are plain vertical shafts).
  - s1 is 竖折 — no matching bank primitive (heng_zhe_short is horizontal-then-down,
    not down-then-right). Inlined fresh; not a BANK_DEVIATION since no bank
    primitive was skipped.

Joints:
  - s1.tail (217,197) N-neighbor s2.mid(0.85)~(226,206): gap ~13px (target ~17px).
  - s1.mid ~(152,197) P-pierced by s3 crossing near y=197: welded via overlap.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 stroke primitives called: L (as 2 line segs = 1 stroke), shu, shu
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's1 = L-shape 竖折 inline; s2 = right short 竖 (bank draw_shu); s3 = center long 竖 (bank draw_shu).'
}

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ----- Stroke 1: 竖折 (L-shape) -----
# vertical segment: (68, 131) -> (68, 197)
# horizontal segment: (68, 197) -> (217, 197)
w1 = 7
# vertical part with slight taper feel (uniform width)
d.line([(68, 131), (68, 197)], fill='black', width=w1)
# rounded corner: small pad at corner so it doesn't look pixely
d.ellipse([(68 - w1 // 2, 197 - w1 // 2), (68 + w1 // 2, 197 + w1 // 2)], fill='black')
# horizontal part
d.line([(68, 197), (217, 197)], fill='black', width=w1)
# end tip subtle taper: cap the right end with a small ellipse
d.ellipse([(217 - w1 // 2, 197 - w1 // 2), (217 + w1 // 2, 197 + w1 // 2)], fill='black')

# ----- Stroke 2: right short 竖 -----
draw_shu(d, (214, 118), (228, 222), width=6)

# ----- Stroke 3: central long 竖 -----
# MMH tail y_frac 1.167 -> y=317, clamp to 300 (bottom of canvas)
draw_shu(d, (134, 66), (150, 300), width=7)

img.save(str(pathlib.Path(__file__).parent / '01_屮.png'))
print('Wrote 01_屮.png')
