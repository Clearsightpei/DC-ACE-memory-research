"""p3_char_0138_水 (shui) — 4 strokes.

MMH-injected structural expectations (300x300, cells 100x100):
  s1 head TC(0.386, 0.615)=(138.6, 61.5)  tail BC(0.049, 0.713)=(104.9, 271.3)  — central 竖钩
  s2 head ML(0.431, 0.562)=(43.1, 156.2)  tail BL(0.331, 0.678)=(33.1, 267.8)   — left downward pie
  s3 head MR(0.159, 0.002)=(215.9, 100.2) tail C (0.729, 0.676)=(172.9, 167.6)  — upper-right→center pie
  s4 head C (0.579, 0.535)=(157.9, 153.5) tail BR(0.9,   0.458)=(290.0, 245.8)  — 捺

Joints (all N — natural gap, do NOT weld):
  s1.mid(0.40) ⇆ s3.tail @ C  (~33 px gap)
  s1.mid(0.40) ⇆ s4.head @ C  (~17 px gap)
  s3.tail     ⇆ s4.head @ C  (~11 px gap)

Bank usage:
  s1: draw_shu_gou (central hook — matches shape well)
  s2: draw_pie (left downward pie; near-vertical, small bow)
  s3: draw_pie (short upper-right → center pie)
  s4: draw_na  (rightward na)
"""

import sys
import pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from shu_gou import draw_shu_gou
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': '4 strokes; using bank primitives shu_gou + pie + pie + na. '
             'All joints are class N (natural gap) — strokes drawn to '
             'MMH endpoints without welding.'
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: central 竖钩 — TC(138.6, 61.5) -> BC(104.9, 271.3)
    # bigger hook_start_offset makes the hook more visible / calligraphic
    draw_shu_gou(d, head=(138.6, 61.5), tail=(104.9, 271.3),
                 width=7, hook_start_offset=70)

    # s2: left downward pie — ML(43.1, 156.2) -> BL(33.1, 267.8)
    # increase bow for a proper leftward pie curve
    draw_pie(d, head=(43.1, 156.2), tail=(33.1, 267.8),
             bow_perp=10, w_head=8, w_tail=3, steps=60)

    # s3: upper-right → center pie — MR(215.9, 100.2) -> C(172.9, 167.6)
    draw_pie(d, head=(215.9, 100.2), tail=(172.9, 167.6),
             bow_perp=8, w_head=7, w_tail=3, steps=60)

    # s4: 捺 — C(157.9, 153.5) -> BR(290.0, 245.8)
    draw_na(d, head=(157.9, 153.5), tail=(290.0, 245.8),
            bow_perp=12, w_head=4, w_tail=11, steps=80)

    out = pathlib.Path(__file__).parent / '01_水.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    render()
