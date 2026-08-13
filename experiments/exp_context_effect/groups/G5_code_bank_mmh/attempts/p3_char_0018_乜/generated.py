"""p3_char_0018_乜 — G5 attempt.

乜 = 2 strokes:
  1) heng across left-center (MMH: ML(0.275,0.913) → C(0.67,0.98))
  2) 竖弯钩-like wrap (MMH: ML(0.981,0.046) → BR(0.563,0.039))

Both strokes are covered by existing bank primitives:
  - draw_heng for stroke 1
  - draw_shu_wan_gou for stroke 2 (start at top, descend, curve right,
    hook up into upper-right tail). Bare shu_wan_gou shape matches the
    大弯 sweep of 乜's second stroke well.
No BANK_DEVIATION.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'heng + shu_wan_gou; MMH anchors used as-is; joint P at C emerges from stroke1 crossing stroke2 body.',
}

import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


CELL = 100  # 米字格 cell size (300/3)


def anchor(cell, xf, yf):
    """Convert (cell_name, x_frac, y_frac) to pixel (x, y)."""
    row_map = {'T': 0, 'M': 1, 'B': 2, 'C': 1}
    col_map = {'L': 0, 'M': 1, 'R': 2, 'C': 1}
    if cell == 'C':
        r, c = 1, 1
    else:
        r = row_map[cell[0]]
        c = col_map[cell[1]]
    return (c * CELL + xf * CELL, r * CELL + yf * CELL)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: heng, ML(0.275,0.913) → C(0.67,0.98)
    s1_head = anchor('ML', 0.275, 0.913)
    s1_tail = anchor('C', 0.67, 0.98)
    draw_heng(d, s1_head, s1_tail, width_head=10, width_tail=11)

    # Stroke 2: shu_wan_gou-like wrap. GT sweep is large — the bottom
    # dips well below tail.y (~y=270) before hooking up-right into tail.
    # bumped bottom_extra=80, knee_ratio=0.80, width=9.
    s2_head = anchor('ML', 0.981, 0.046)
    s2_tail = anchor('BR', 0.563, 0.039)
    draw_shu_wan_gou(d, s2_head, s2_tail,
                     width=9, bottom_extra=80, knee_ratio=0.80)

    out = pathlib.Path(__file__).parent / '01_乜.png'
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
