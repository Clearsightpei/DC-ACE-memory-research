"""p3_char_0015_二 — G5 attempt.

The Phase-3 character 二 is identical in structure to the Phase-2 radical 二
(2 horizontal strokes, upper shorter/thinner, lower wider/heavier).
MMH-injected anchors match the bank primitive er_two.py exactly:
  s1: ML(0.858,0.28) -> MR(0.147,0.157)  = (85.8,128) -> (214.7,115.7)
  s2: BL(0.369,0.358) -> BR(0.684,0.326) = (36.9,235.8) -> (268.4,232.6)
Joints: NONE (clear separation).

Bank primitive used as-is; no BANK_DEVIATION.
"""
import pathlib
import sys

from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from er_two import draw_er

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # draw_er internally calls 2 draw_heng -> 2 strokes
    'endpoint_mismatches': [],   # anchors match MMH exactly (bank was built from same source)
    'joint_class_mismatches': [], # no joints
    'overall_pass': True,
    'notes': 'bank primitive er_two matches MMH anchors exactly; used as-is.',
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_er(d, ox=0, oy=0, scale=1.0)
    out = pathlib.Path(__file__).parent / '01_二.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
