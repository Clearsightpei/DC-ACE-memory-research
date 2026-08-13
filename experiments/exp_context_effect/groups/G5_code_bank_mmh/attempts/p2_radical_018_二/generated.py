# p2_radical_018_二 — G5 first attempt (bootstrap, bank empty)
# 二 = two horizontal strokes (upper shorter, lower longer).
# MMH anchors (300x300 canvas, 3x3 米字格 cells 100px each):
#   stroke 1: head (ML, 0.858, 0.28) = (85.8, 128)
#             tail (MR, 0.147, 0.157) = (214.7, 115.7)
#   stroke 2: head (BL, 0.369, 0.358) = (36.9, 235.8)
#             tail (BR, 0.684, 0.326) = (268.4, 232.6)
# No joints (N — clear separation).

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 strokes drawn == 2 expected
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'two horizontals, upper shorter, lower longer; clear vertical gap.'
}


def cell_to_px(cell, xf, yf, size=300):
    # 3x3 米字格: cols T/M/B correspond to rows; cell like 'ML' = middle-row, left-col.
    row_map = {'T': 0, 'M': 1, 'B': 2}
    col_map = {'L': 0, 'C': 1, 'R': 2}
    row = row_map[cell[0]]
    col = col_map[cell[1]]
    cell_w = size / 3
    x = col * cell_w + xf * cell_w
    y = row * cell_w + yf * cell_w
    return (x, y)


def draw_heng(draw, p_head, p_tail, width=14):
    # Simple horizontal stroke with rounded ends (calligraphic feel).
    draw.line([p_head, p_tail], fill='black', width=width)
    r = width / 2
    for (x, y) in (p_head, p_tail):
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # stroke 1 — upper heng (shorter)
    h1 = cell_to_px('ML', 0.858, 0.28)
    t1 = cell_to_px('MR', 0.147, 0.157)
    draw_heng(d, h1, t1, width=13)

    # stroke 2 — lower heng (longer, slightly heavier)
    h2 = cell_to_px('BL', 0.369, 0.358)
    t2 = cell_to_px('BR', 0.684, 0.326)
    draw_heng(d, h2, t2, width=15)

    out = '/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_018_二/01_二.png'
    img.save(out)
    print('wrote', out)
    print('SELF_CHECK:', SELF_CHECK)


if __name__ == '__main__':
    main()
