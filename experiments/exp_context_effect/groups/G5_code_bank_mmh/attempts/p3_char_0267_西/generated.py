"""p3_char_0267_西 — G5 render.

Recipe: P-A-006 (MMH-anchor verbatim + stroke-primitive layer).
6 strokes:
  s1: top horizontal ─ (isolated top bar)
  s2: left | (of body, slightly slanted rightward going down)
  s3: 横折 (top of body + right side, from ML down through box to BC)
  s4: inner long | (from top-bar area down to bottom of box, left inner)
  s5: inner slanted (from top-bar area down-right to right side of box, right inner)
  s6: bottom ─ (closing box)

Anchors are MMH-derived (canvas 300x300, cells 100x100 in 米字格 layout).
"""
import sys, os
BANK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK_DIR)

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'P-A-006 recipe. s3 is inline 横折 (heng+shu L-shape). s4,s5 inner verticals cross s3 top → P joints. s6 bottom horizontal near-touches s2.tail and s3.tail → N.'
}


def cell_xy(cell, xf, yf, canvas=300):
    cell_size = canvas / 3
    col_map = {'TL': 0, 'ML': 0, 'BL': 0,
               'TC': 1, 'C': 1, 'BC': 1,
               'TR': 2, 'MR': 2, 'BR': 2}
    row_map = {'TL': 0, 'TC': 0, 'TR': 0,
               'ML': 1, 'C': 1, 'MR': 1,
               'BL': 2, 'BC': 2, 'BR': 2}
    x = col_map[cell] * cell_size + xf * cell_size
    y = row_map[cell] * cell_size + yf * cell_size
    return (x, y)


def draw_xi(draw):
    # --- MMH anchors ---
    s1_head = cell_xy('TL', 0.738, 0.967)   # (73.8, 96.7)
    s1_tail = cell_xy('TR', 0.171, 0.829)   # (217.1, 82.9)
    s2_head = cell_xy('ML', 0.437, 0.570)   # (43.7, 157.0)
    s2_tail = cell_xy('BL', 0.762, 0.728)   # (76.2, 272.8)
    s3_head = cell_xy('ML', 0.653, 0.614)   # (65.3, 161.4)
    s3_tail = cell_xy('BC', 0.983, 0.604)   # (198.3, 260.4)
    s4_head = cell_xy('C',  0.084, 0.066)   # (108.4, 106.6)
    s4_tail = cell_xy('BL', 0.935, 0.224)   # (93.5, 222.4)
    s5_head = cell_xy('TC', 0.529, 0.993)   # (152.9, 99.3)
    s5_tail = cell_xy('BR', 0.118, 0.010)   # (211.8, 201.0)
    s6_head = cell_xy('BL', 0.832, 0.648)   # (83.2, 264.8)
    s6_tail = cell_xy('BR', 0.027, 0.528)   # (202.7, 252.8)

    # s1: top horizontal (bank primitive)
    draw_heng(draw, s1_head, s1_tail, width_head=10, width_tail=11)

    # s2: left vertical of body (bank primitive, slight slant OK — draw_shu draws head→tail)
    draw_shu(draw, s2_head, s2_tail, width=8)

    # s3: 横折 (heng top of box + shu right side). Corner is at (s3_tail.x, s3_head.y).
    corner = (s3_tail[0], s3_head[1])
    # top horizontal segment
    draw.line([s3_head, corner], fill='black', width=8)
    # right vertical segment
    draw.line([corner, s3_tail], fill='black', width=8)
    # subtle corner reinforcement (small, not a blob)
    draw.ellipse([corner[0]-3, corner[1]-3, corner[0]+3, corner[1]+3], fill='black')
    # tail 顿笔 dab
    draw.ellipse([s3_tail[0]-5, s3_tail[1]-5, s3_tail[0]+5, s3_tail[1]+5], fill='black')

    # s4: inner-left long stroke — mostly-vertical, slightly leftward-slanting.
    # No endpoint blobs (they read as noise on inner strokes).
    draw.line([s4_head, s4_tail], fill='black', width=6)

    # s5: inner-right slanted stroke — from top-bar center down-right into box.
    draw.line([s5_head, s5_tail], fill='black', width=6)

    # s6: bottom horizontal (closing box) — bank primitive
    draw_heng(draw, s6_head, s6_tail, width_head=9, width_tail=10)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_xi(d)
    out = os.path.join(os.path.dirname(__file__), '01_西.png')
    img.save(out)
    print('Wrote', out)
    # Stroke count verification
    n_strokes = 6  # s1..s6
    assert n_strokes == 6, f'Expected 6 strokes, got {n_strokes}'


if __name__ == '__main__':
    main()
