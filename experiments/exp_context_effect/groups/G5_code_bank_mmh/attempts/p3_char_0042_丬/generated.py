"""p3_char_0042_丬 — G5 attempt (bank-composed).

Uses stroke bank primitives: pie (short dian-like), ti, shu.
Anchors taken directly from MMH-derived structural block.

SELF_CHECK block at bottom.
"""

import sys
import pathlib
from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'success_bank' / 'code'))

from pie import draw_pie
from ti import draw_ti
from shu import draw_shu


def cell_to_px(cell, xf, yf):
    """9-cell 米字格 to pixel. Canvas 300x300, 3x3 grid, each cell 100x100."""
    col_map = {'L': 0, 'C': 100, 'R': 200}
    row_map = {'T': 0, 'C': 100, 'B': 200}
    if cell == 'C':
        col, row = 'C', 'C'
    elif len(cell) == 2:
        row, col = cell[0], cell[1]
    else:
        raise ValueError(cell)
    return (col_map[col] + xf * 100, row_map[row] + yf * 100)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # stroke 1 — short pie in upper part of center cell
    # head @ ('C', 0.046, 0.081) tail @ ('C', 0.342, 0.424)
    # GT shows a thin diagonal, not a heavy dian-blob — narrow widths.
    s1_head = cell_to_px('C', 0.046, 0.081)
    s1_tail = cell_to_px('C', 0.342, 0.424)
    draw_pie(draw, s1_head, s1_tail, bow_perp=3, w_head=5, w_tail=2)

    # stroke 2 — ti rising from BL up to C. Pull tail back along the ti
    # direction so the joint vs s3 shu is class-N (visible gap ~28 px),
    # not welded.
    # head @ ('BL', 0.87, 0.306) tail @ ('C', 0.576, 0.749)
    s2_head = cell_to_px('BL', 0.87, 0.306)
    s2_tail_full = cell_to_px('C', 0.576, 0.749)
    dx = s2_tail_full[0] - s2_head[0]
    dy = s2_tail_full[1] - s2_head[1]
    L = (dx * dx + dy * dy) ** 0.5
    pullback = 26.0
    s2_tail = (s2_tail_full[0] - dx / L * pullback,
               s2_tail_full[1] - dy / L * pullback)
    draw_ti(draw, s2_head, s2_tail, w_head=9, w_tail=2)

    # stroke 3 — long shu from TC down to BC (slight rightward drift)
    # head @ ('TC', 0.538, 0.7) tail @ ('BC', 0.638, 1.026)
    s3_head = cell_to_px('TC', 0.538, 0.7)
    s3_tail = cell_to_px('BC', 0.638, 1.026)
    draw_shu(draw, s3_head, s3_tail, width=7)

    out = HERE / '01_丬.png'
    img.save(out)
    print(f"wrote {out}")


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,   # 3 primitives called == 3 expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': (
        's1 pie C→C, s2 ti BL→C, s3 shu TC→BC. '
        'Joint s2.tail↔s3.mid(0.39): both near (158,175) vs (158,161) — '
        'natural N gap held by stroke widths (no explicit weld).'
    ),
}


if __name__ == '__main__':
    main()
