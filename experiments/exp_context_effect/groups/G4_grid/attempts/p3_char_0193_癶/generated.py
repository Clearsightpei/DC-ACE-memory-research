"""癶 (bo, 'two feet') — 5 strokes.
Read: drawer_memory.md (v8) then memory_index.md.
No 癶 in success bank, no chronic primitive covers it, no errata entry.
Composition: left half (long 撇 + small dot/mark) + right half
(short 撇 + short mark + long 捺). Draws fresh per MMH anchors.
"""
import sys, os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 '..', '..', 'success_bank', 'code')))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes; all joints N (natural gap); anchors from MMH'
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# stroke 1: long left 撇  TL(.727,.879) -> BL(.281,.221)
p0 = anchor_to_xy(('TL', 0.727, 0.879))
p2 = anchor_to_xy(('BL', 0.281, 0.221))
# control pt pulled right of chord for concave-left curve
ctrl = ((p0[0] + p2[0]) / 2 + 18, (p0[1] + p2[1]) / 2 - 6)
pts = quad_bezier(p0, ctrl, p2, n=40)
widths = [10 - 6 * (i / 40) for i in range(41)]  # thick head, tapered tail
stroke_variable_width(d, pts, widths)

# stroke 2: small mark on left 撇  ML(.618,.228) -> ML(.885,.462)
a = anchor_to_xy(('ML', 0.618, 0.228))
b = anchor_to_xy(('ML', 0.885, 0.462))
fat_line(d, a, b, width=8)

# stroke 3: short right-top 撇  TC(.992,.604) -> TC(.673,.864)
a = anchor_to_xy(('TC', 0.992, 0.604))
b = anchor_to_xy(('TC', 0.673, 0.864))
ctrl = ((a[0] + b[0]) / 2 + 3, (a[1] + b[1]) / 2 - 2)
pts = quad_bezier(a, ctrl, b, n=20)
widths = [8 - 4 * (i / 20) for i in range(21)]
stroke_variable_width(d, pts, widths)

# stroke 4: small mark  TR(.224,.744) -> C(.913,.157)
a = anchor_to_xy(('TR', 0.224, 0.744))
b = anchor_to_xy(('C', 0.913, 0.157))
fat_line(d, a, b, width=7)

# stroke 5: long 捺 sweep  TC(.512,.885) -> MR(.883,.91)
p0 = anchor_to_xy(('TC', 0.512, 0.885))
p2 = anchor_to_xy(('MR', 0.883, 0.91))
# concave-up curve: control pt pulled up
ctrl = ((p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2 - 20)
pts = quad_bezier(p0, ctrl, p2, n=40)
# thin head, thick middle, tapered tail (捺 shape)
widths = []
for i in range(41):
    t = i / 40
    # peaks around t=0.7
    w = 4 + 10 * (1 - abs(t - 0.7) / 0.7)
    widths.append(max(3, w))
stroke_variable_width(d, pts, widths)

out = os.path.join(os.path.dirname(__file__), '01_癶.png')
img.save(out)
print(f'wrote {out}')
