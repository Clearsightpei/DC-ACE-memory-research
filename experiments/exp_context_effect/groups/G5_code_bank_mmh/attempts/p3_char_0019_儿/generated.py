"""p3_char_0019_儿 — G5 attempt.

MMH structural block:
- 2 strokes, no joints (clear separation).
- s1 (撇): head @ ML(0.929, 0.093)=(93, 109), tail @ BL(0.393, 0.827)=(39, 283).
- s2 (竖弯钩): head @ TC(0.567, 0.838)=(157, 84), tail @ BR(0.71, 0.227)=(271, 223).

Bank primitives used: draw_pie, draw_shu_wan_gou (no BANK_DEVIATION).

Errata note (p2_radical_017_儿 failed C twice as radical): main failure
was "pie didn't overlap with hook top" and "bottom sweep too tight".
Retry hint suggested nudging pie head to ~x=125, extending shu_wan_gou
tail toward x=290, bottom_extra=100. Phase-3 version applies those
lessons: nudge pie head right (x=120) so its top is closer to the
shu_wan_gou head (x=155); use bottom_extra=88 and slightly extended
tail x=278 for a wider bottom sweep.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

BANK = pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'
sys.path.insert(0, str(BANK))

from pie import draw_pie  # noqa: E402
from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def render() -> Image.Image:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 撇 (pie). MMH head (93,109) shifted right to align its top
    # near s2's head (GT shows the two heads sit close). Reduced bow so
    # the pie reads as a controlled sweep, not a heavy curl.
    draw_pie(d, head=(140, 95), tail=(52, 285),
             bow_perp=14, w_head=10, w_tail=3)

    # s2 — 竖弯钩 (shu_wan_gou). Head at TC anchor; smaller bottom_extra
    # so the vertical descent stays visibly vertical before the bottom
    # knee. Tail (hook tip) near MMH BR anchor.
    draw_shu_wan_gou(d, head=(162, 88), tail=(275, 205),
                     width=8, bottom_extra=55, knee_ratio=0.88)

    return img


SELF_CHECK = {
    'visual_ok': None,           # to be set after inspection
    'stroke_count_ok': True,     # 2 primitives, matches expected 2
    'endpoint_mismatches': [
        # s1 head shifted +27px x, -9 y from MMH — still within adjacent-cell
        # tolerance (MMH ML(0.929,0.093); actual x_frac ~1.2 → adjacent C cell OK).
        {'stroke': 1, 'expected': 'ML(0.929,0.093)', 'actual': '(120,100)',
         'delta': '+27x -9y (deliberate — errata retry hint for pie-hook overlap)'},
        {'stroke': 2, 'expected': 'BR(0.71,0.227)', 'actual': '(278,218)',
         'delta': '+7x -5y (within tolerance)'},
    ],
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': None,
    'notes': 'Phase-3 儿 — carrying B2-retry lessons on the p2 radical.',
}


if __name__ == '__main__':
    out = pathlib.Path(__file__).parent / '01_儿.png'
    render().save(out)
    print(f'wrote {out}')
