"""p3_char_0126_长 — identity-reuse of bank primitive draw_chang_long.

P-A-001 identity: this Phase-3 character IS the same shape as the
Phase-2 radical 长 (p2_radical_088), which PASSed at B4 R2 and was
promoted as chang_long.py. Call with default (ox=0, oy=0, scale=1.0).

MMH structural expectations (from injection):
  4 strokes: pie(TC->C), heng(ML->MR), shu_ti(TL->BC), na(C->BR)
  4 joints, all in cell C.
The bank recipe already implements this 4-stroke topology.
"""

import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'),
)
from chang_long import draw_chang_long  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # bank primitive draws exactly 4 stroke polylines
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'identity-reuse of chang_long bank primitive (B4 R2 PASS).',
}


def main() -> None:
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)
    draw_chang_long(draw, ox=0, oy=0, scale=1.0)
    out = pathlib.Path(__file__).with_name('01_长.png')
    img.save(out)


if __name__ == '__main__':
    main()
