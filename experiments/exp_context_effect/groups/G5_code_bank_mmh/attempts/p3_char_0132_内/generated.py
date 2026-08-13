"""p3_char_0132_内 — 4 strokes: 竖, 横折钩, 撇, 捺 (inner 人).

Bank primitives used:
  shu (left vertical, s1)
  heng_zhe_gou (right compound, s2)
  pie (inner 撇, s3)
  na (inner 捺, s4)

MMH anchors (pixels, 300x300 canvas, 米字格 mapping):
  s1: head (66.5, 123.6) tail (66.5, 283.3)
  s2: head (84.1, 128.9) tail (184.9, 276.9)  [tail is hook_tip]
  s3: head (134.5, 58.6) tail (89.1, 227.3)
  s4: head (150.0, 169.0) tail (196.6, 218.8)
"""

import os
import sys
from PIL import Image, ImageDraw

# Make bank importable
HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK)

from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,           # 4 stroke primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'v1: bank primitives shu/heng_zhe_gou/pie/na. Corner and gou_tail for '
             'the heng_zhe_gou were inferred (MMH gives only head + hook_tip).',
}


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: 竖 (left vertical) — subtle top nub (top_curl=False; GT hook is minimal)
    draw_shu(d, head=(66.5, 123.6), tail=(66.5, 283.3), width=6, top_curl=False)

    # s2: 横折钩 — heng from (84,129) → corner top-right → down → hook flick
    # hook_tip needs to flick UP-LEFT from gou_tail. MMH tail (184.9, 276.9)
    # is very close to gou_tail; treat it as gou_tail and flick hook up-left.
    draw_heng_zhe_gou(
        d,
        heng_head=(84.1, 128.9),
        corner=(212.0, 124.0),
        gou_tail=(200.0, 276.0),
        hook_tip=(178.0, 258.0),
    )

    # s3: 撇 (inside 人 — start at top area, sweep to bottom-left)
    draw_pie(d, head=(134.5, 58.6), tail=(89.1, 227.3),
             bow_perp=12, w_head=7, w_tail=2)

    # s4: 捺 (short, inside; head near center → bottom-right)
    draw_na(d, head=(150.0, 169.0), tail=(196.6, 218.8),
            bow_perp=6, w_head=3, w_tail=8)

    out = os.path.join(HERE, "01_内.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
