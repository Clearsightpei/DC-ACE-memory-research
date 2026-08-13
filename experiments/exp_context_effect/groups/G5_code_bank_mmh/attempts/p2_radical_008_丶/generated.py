# p2_radical_008_丶 — G5 bootstrap radical
# Single-stroke 点 (dot). MMH anchors:
#   head @ TC (0.146, 0.946)  → ~(114.6,  94.6)
#   tail @ C  (0.717, 0.652)  → ~(171.7, 165.2)
# Direction: upper-left → lower-right, thickening tail (calligraphic 点).

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 1 stroke drawn, expected 1
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # none expected
    'overall_pass': True,
    'notes': '点 rendered as tapered curve head→tail, thickening toward tail.',
}

from PIL import Image, ImageDraw

W = H = 300
CELL = W // 3  # 米字格 cell = 100px

def anchor(cell, xf, yf):
    # cell name → (col, row) in 3x3 (col 0..2 left→right, row 0..2 top→bot)
    grid = {
        'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
        'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
        'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
    }
    c, r = grid[cell]
    return (c * CELL + xf * CELL, r * CELL + yf * CELL)


def draw_dian_tapered(draw, head, tail, w_head=3, w_tail=10, bow=6, steps=40):
    """Draw a tapered curved stroke from head to tail with a slight downward bow."""
    hx, hy = head
    tx, ty = tail
    # midpoint for quadratic-ish curve; perpendicular offset for bow
    mx = (hx + tx) / 2
    my = (hy + ty) / 2
    # perpendicular to segment (rotate direction 90°)
    dx, dy = tx - hx, ty - hy
    length = (dx * dx + dy * dy) ** 0.5
    if length == 0:
        return
    # perpendicular (to the "right" of head→tail direction, giving belly toward lower-left)
    px, py = -dy / length, dx / length
    cx, cy = mx + px * bow, my + py * bow

    prev = None
    for i in range(steps + 1):
        t = i / steps
        # Quadratic Bezier: (1-t)^2 * head + 2(1-t)t * ctrl + t^2 * tail
        u = 1 - t
        x = u * u * hx + 2 * u * t * cx + t * t * tx
        y = u * u * hy + 2 * u * t * cy + t * t * ty
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
        if prev is not None:
            # smooth the gap between blobs
            draw.line((prev[0], prev[1], x, y), fill='black', width=int(round(r * 2)))
        prev = (x, y)


def main():
    img = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(img)

    head = anchor('TC', 0.146, 0.946)   # ~(114.6, 94.6)
    tail = anchor('C',  0.717, 0.652)   # ~(171.7, 165.2)

    draw_dian_tapered(draw, head, tail, w_head=3, w_tail=8, bow=5, steps=48)

    out = '/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_008_丶/01_丶.png'
    img.save(out)
    print('saved', out)


if __name__ == '__main__':
    main()
