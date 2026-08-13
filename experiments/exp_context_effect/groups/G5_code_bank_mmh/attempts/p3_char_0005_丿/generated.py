"""Draw 丿 (pie, single stroke) — G5 attempt.

Bank primitive `draw_pie` fits this composition perfectly (single 撇).

MMH-derived anchors (from injected structural block):
  stroke 1: head @ ('TL', 0.627, 0.794) → pixel (62.7, 79.4)
            tail @ ('BL', 0.141, 0.892) → pixel (14.1, 289.2)

米字格 cell layout on 300x300: cells are 100x100. TL is (0..100, 0..100);
BL is (0..100, 200..300). Within-cell (x_frac, y_frac) is direct.
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # 1 turtle-primitive call for 1 expected stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # no joints expected (single stroke)
    'overall_pass': True,
    'notes': 'Single pie stroke; direct bank primitive call from head→tail.',
}

import sys, pathlib
from PIL import Image, ImageDraw

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'))
from pie import draw_pie


def cell_to_px(cell, xf, yf, cell_size=100):
    col = {'L': 0, 'C': 1, 'R': 2}[cell[1]]
    row = {'T': 0, 'M': 1, 'B': 2}[cell[0]]
    return (col * cell_size + xf * cell_size, row * cell_size + yf * cell_size)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    head = cell_to_px('TL', 0.627, 0.794)   # (62.7, 79.4)
    tail = cell_to_px('BL', 0.141, 0.892)   # (14.1, 289.2)

    # 丿 is a long, gentle leftward sweep with thick head and fine tail.
    draw_pie(d, head, tail, bow_perp=18, w_head=8, w_tail=2, steps=100)

    out = pathlib.Path(__file__).parent / '01_丿.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
