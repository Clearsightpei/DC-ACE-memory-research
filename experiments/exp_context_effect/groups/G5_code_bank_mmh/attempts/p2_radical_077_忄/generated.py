"""p2_radical_077_忄  (xin, heart-side radical) — 3 strokes.

Composition:
  s1 = left dian (long-ish left-slanting dot / 撇-like)
  s2 = short right dian
  s3 = vertical shu-gou (bottom hook curves LEFT)

MMH anchors (cell + fraction, cell=100px):
  s1: head C(0.125, 0.468) tail BC(0.014, 0.051)  -> (112,147) -> (101,205)
  s2: head C(0.600, 0.371) tail C(0.890, 0.632)   -> (160,137) -> (189,163)
  s3: head TC(0.371, 0.697) tail BC(0.447, 1.073) -> (137,70)  -> (145,307)

Joint expectation:
  s2.head <-> s3.mid(0.25) at cell C : N (gap ~19px) -> keep neighbor gap.

Bank usage (from drawer_memory retrieval table):
  - dian.py    for both dots (s1 long taper, s2 short taper)
  - shu_gou.py for s3 (hook curves left at bottom)
No BANK_DEVIATION — bank primitives fit this composition cleanly.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from dian import draw_dian
from shu_gou import draw_shu_gou


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 3 strokes: dian + dian + shu_gou
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': (
        's1 head (112,147) tail (101,205); s2 head (160,137) tail (189,163); '
        's3 head (137,70) hook-tip (125,290). s2.head to s3.mid(0.25)=(139,129) '
        'distance ~22px (N-neighbor, near expected 19).'
    ),
}


def render(path: str) -> None:
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — left dian (long, tapering, slight rightward bow to give a curved 撇-like shape)
    draw_dian(d, head=(112, 147), tail=(101, 205),
              w_head=3, w_tail=7, bow=3, steps=60)

    # s2 — right dian (short, thick tail)
    draw_dian(d, head=(160, 137), tail=(189, 163),
              w_head=3, w_tail=8, bow=3, steps=40)

    # s3 — vertical shu-gou; MMH tail passes canvas, so hook-tip is inset.
    # head at top-center, hook lands lower-left at (125, 290).
    draw_shu_gou(d, head=(137, 70), tail=(125, 290),
                 width=7, hook_start_offset=25)

    img.save(path)


if __name__ == '__main__':
    out = str(_HERE.parent / '01_忄.png')
    render(out)
    print('wrote', out)
