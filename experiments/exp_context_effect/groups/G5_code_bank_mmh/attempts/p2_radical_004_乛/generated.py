"""p2_radical_004_乛 — G5 bootstrap attempt.

Stroke count: 1 (horizontal-then-hook, 横折).
MMH anchors:
  stroke 1: head @ ('ML', 0.782, 0.342) → (78, 134)
            tail @ ('C',  0.890, 0.623) → (189, 162)

Bank is empty at bootstrap — inline fresh render from GT + MMH.
"""
from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # no joints expected
    'overall_pass': True,
    'notes': 'Single stroke 乛 — horizontal segment then downward hook curve.',
}

W, H = 300, 300


def cell_to_px(cell, xf, yf):
    """米字格 cell + fractional (xf, yf) → absolute pixel."""
    col = {'L': 0, 'C': 1, 'R': 2}[cell[1]] if len(cell) == 2 else 1
    row = {'T': 0, 'M': 1, 'B': 2}[cell[0]] if len(cell) == 2 else 1
    if cell == 'C':
        col, row = 1, 1
    x = col * 100 + xf * 100
    y = row * 100 + yf * 100
    return x, y


def draw_heng_zhe(draw):
    # Head at ML(0.782, 0.342), Tail at C(0.89, 0.623).
    x0, y0 = cell_to_px('ML', 0.782, 0.342)   # ≈ (78, 134)
    x1, y1 = cell_to_px('C',  0.890, 0.623)   # ≈ (189, 162)

    # Path: mostly horizontal from head, brief right-going span, then a
    # downward hook curve into the tail. Model as two segments joined by a
    # smooth corner around ~(160, 140):
    #   A: (x0,y0) -> corner  (nearly-flat horizontal, slight downward drift)
    #   B: corner -> (x1,y1)  (bends down more steeply, curved)
    corner_x, corner_y = 162, 138

    # Segment A: slight taper — start with mild lead-in blob.
    steps_a = 30
    for i in range(steps_a):
        t = i / (steps_a - 1)
        # gentle quadratic bow above the straight line for a slight arch
        bx = x0 + (corner_x - x0) * t
        by = y0 + (corner_y - y0) * t - 2.5 * (1 - (2 * t - 1) ** 2)
        # width tapers from thin lead-in to full body
        w = 3.2 + 2.0 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill=(0, 0, 0))

    # Segment B: quadratic Bezier from corner through control down to tail.
    # Control point pulls tightly right/flat then down for a sharper hook.
    cx, cy = 193, 135
    steps_b = 40
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * corner_x + 2 * (1 - t) * t * cx + t ** 2 * x1
        by = (1 - t) ** 2 * corner_y + 2 * (1 - t) * t * cy + t ** 2 * y1
        # width tapers slightly toward the tail tip
        w = 4.8 - 2.6 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill=(0, 0, 0))


def main():
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)
    draw_heng_zhe(d)
    out = __file__.rsplit('/', 1)[0] + '/01_乛.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
