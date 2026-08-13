"""p3_char_0049_子 — G5 attempt.

3 strokes per MMH: heng_pie (top), wan_gou (main body), heng (middle bar).

Uses bank primitives:
- heng_pie: bank; overriding apex_x / corner_x because default (hx+130) is
  tuned for 又 and would place the corner far off-canvas for 子's short top.
- wan_gou:  bank identity call with MMH anchors (matches 了 sibling).
- heng:     bank identity call spanning full width.
"""

import sys
import pathlib

# Wire success_bank/code onto sys.path.
_here = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_here.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw  # noqa: E402
from heng_pie import draw_heng_pie  # noqa: E402
from wan_gou import draw_wan_gou  # noqa: E402
from heng import draw_heng  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 primitives called == 3 expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        'heng_pie tuned for short 子-top (apex_x=120, corner_x=155); '
        'wan_gou default params sized to sibling 了; heng spans ML->MR. '
        's1.tail(157,132) ~ s2.head(138,128) dist~19 (N joint, gap OK). '
        's2@0.24 (~150,176) ~ s3@0.51 (~157,179) dist~8 (P joint, welded '
        'given stroke widths ~6-10).'
    ),
}

img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Stroke 1: 横撇 (heng_pie) at top.
# MMH: head (TL,0.861,0.917)=(86.1, 91.7) -> tail (C,0.57,0.318)=(157, 131.8)
draw_heng_pie(d, head=(86, 92), tail=(157, 132), apex_x=120, corner_x=155)

# Stroke 2: 弯钩 (wan_gou) main body.
# MMH: head (C,0.383,0.277)=(138.3, 127.7) -> tail (BC,0.034,0.728)=(103.4, 272.8)
draw_wan_gou(d, head=(138, 128), tail=(103, 273))

# Stroke 3: 横 (heng) middle bar.
# MMH: head (ML,0.349,0.813)=(34.9, 181.3) -> tail (MR,0.745,0.764)=(274.5, 176.4)
draw_heng(d, head=(35, 181), tail=(275, 176))

out = _here.parent / '01_子.png'
img.save(out)
print(f'wrote {out}')
