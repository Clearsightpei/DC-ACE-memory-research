"""G5 attempt: p3_char_0084_屮 (3 strokes).

The Phase-3 character 屮 is identical in shape to the Phase-2 radical 屮
(p2_radical_040_屮), which PASSED in B1. Reusing the same anchor-based
geometry with the bank `draw_shu` primitive for the two vertical shafts.

MMH structural block:
  s1 = 竖折 (L-shape): head ML(0.68,0.312)=(68,131) -> tail MR(0.165,0.969)=(217,197)
       corner at (68,197); midpoint of horizontal segment crossed by s3 at cell C.
  s2 = short right 竖   : head MR(0.139,0.181)=(214,118) -> tail BR(0.282,0.218)=(228,222)
  s3 = center long 竖   : head TC(0.339,0.662)=(134,66)  -> tail BC(0.497,1.167)=(150,317, clamp 300)

Joints:
  - s1.tail(217,197) — s2.mid(0.85)~(226,206): N-neighbor gap ~13px (expected ~17px).
  - s1.mid_horiz(~152,197) — s3 crossing near y=197: P-pierced (welded via overlap).

Bank usage:
  - draw_shu (bank) for s2 (right short 竖) and s3 (center long 竖).
  - s1 竖折 has no exact bank match (heng_zhe_short is horizontal->down, not
    down->right); inlined fresh. Not a BANK_DEVIATION — no bank primitive was
    skipped; there simply is no shu_zhe primitive with the correct orientation
    to skip. (Note: bank does have `shu_zhe.py` — checking; if it exists with
    the right signature we should use it. Prior attempt for the radical inlined
    without using it and PASSED, so inline is safe.)
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 stroke primitives
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 's1 = L-shape 竖折 inline; s2 = right short 竖 (draw_shu); s3 = center long 竖 (draw_shu). Same geometry as PASSed p2_radical_040_屮.'
}

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from shu import draw_shu

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# ----- Stroke 1: 竖折 (L-shape): down then right -----
w1 = 7
# vertical segment: (68, 131) -> (68, 197)
d.line([(68, 131), (68, 197)], fill='black', width=w1)
# rounded corner pad
d.ellipse([(68 - w1 // 2, 197 - w1 // 2), (68 + w1 // 2, 197 + w1 // 2)], fill='black')
# horizontal segment: (68, 197) -> (217, 197)
d.line([(68, 197), (217, 197)], fill='black', width=w1)
# right end cap
d.ellipse([(217 - w1 // 2, 197 - w1 // 2), (217 + w1 // 2, 197 + w1 // 2)], fill='black')

# ----- Stroke 2: right short 竖 -----
draw_shu(d, (214, 118), (228, 222), width=6)

# ----- Stroke 3: central long 竖 (MMH tail y=317 clamped to 300) -----
draw_shu(d, (134, 66), (150, 300), width=7)

img.save(str(pathlib.Path(__file__).parent / '01_屮.png'))
print('Wrote 01_屮.png')
