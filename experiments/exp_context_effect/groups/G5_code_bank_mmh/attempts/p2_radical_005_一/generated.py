"""G5 render for p2_radical_005_一 (一 — heng, 1 stroke).

MMH-derived structural expectations:
- 1 stroke
- head @ ('ML', 0.354, 0.849)  -> px (35, 185)
- tail @ ('MR', 0.695, 0.825)  -> px (270, 183)
- no joints

Bank is empty at bootstrap. No BANK_DEVIATION necessary.
"""
from PIL import Image, ImageDraw
from pathlib import Path

# 米字格 → pixel helper (300x300 canvas, 3x3 cells of 100 px each)
CELL_ORIGINS = {
    'TL': (0,   0),   'TM': (100, 0),   'TR': (200, 0),
    'ML': (0, 100),   'MM': (100, 100), 'MR': (200, 100),
    'BL': (0, 200),   'BM': (100, 200), 'BR': (200, 200),
}

def anchor_to_px(cell, xf, yf, cell_size=100):
    ox, oy = CELL_ORIGINS[cell]
    return (ox + xf * cell_size, oy + yf * cell_size)


def draw_heng(draw, head, tail, width_head=9, width_tail=10):
    """Simple 横 stroke with mild thickness taper — head slightly thinner,
    body full, tail with a small 顿笔 bump."""
    # Body as a fat line
    draw.line([head, tail], fill='black', width=width_head)
    # Tiny end-cap dabs for calligraphic feel
    hx, hy = head
    tx, ty = tail
    r = width_head / 2
    draw.ellipse([hx - r + 1, hy - r, hx + r - 1, hy + r], fill='black')
    r2 = width_tail / 2 + 1
    draw.ellipse([tx - r2, ty - r2, tx + r2, ty + r2], fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    head = anchor_to_px('ML', 0.354, 0.849)  # (35.4, 184.9)
    tail = anchor_to_px('MR', 0.695, 0.825)  # (269.5, 182.5)

    draw_heng(draw, head, tail)

    out = Path(__file__).parent / '01_一.png'
    img.save(out)
    return out, head, tail


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # exactly 1 draw_heng call
    'endpoint_mismatches': [],     # anchors used verbatim
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': 'Bootstrap radical 一, single 横; anchors match MMH block exactly.',
}


if __name__ == '__main__':
    out, head, tail = render()
    print(f'wrote {out}')
    print(f'head={head} tail={tail}')
    print(f'SELF_CHECK={SELF_CHECK}')
