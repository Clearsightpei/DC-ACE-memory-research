"""响 (xiǎng) — 9 strokes.

Decomposition: 响 = 口 (left) + 向 (right).
  口 (left):  s1 竖, s2 横折, s3 横 — 3 strokes, all N corners.
  向 (right): s4 撇, s5 竖 (冂 left), s6 横折钩 (冂 top+right+hook),
             s7 竖 (inner 口 left), s8 横折 (inner 口 top+right), s9 横 (inner 口 bottom).

Slot layout (per MMH anchors):
  Left 口 occupies ML+BL cells (x≈0.09-0.32, y≈0.47-0.72 canvas).
  向 fills right two-thirds: 撇 apex TC, 冂 frame spans C→BR, inner 口 sits inside 冂.

MMH-verbatim anchors used throughout (per A-recipe points 2 + 4:
inline base primitives, trust MMH). All joints N-class — leave the
natural gap.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code'))
from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes MMH-verbatim; 口 left + 向 right; all N-joints preserved as ~3px shortening.',
}


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_response(draw):
    W = 9  # stroke thickness

    # === Left 口 (strokes 1-3) ===
    s1h = anchor_to_xy(('ML', 0.264, 0.421))
    s1t = anchor_to_xy(('BL', 0.48, 0.159))
    s2h = anchor_to_xy(('ML', 0.413, 0.418))
    s2t = anchor_to_xy(('ML', 0.768, 0.813))
    s2c = (s2t[0], s2h[1])  # top-right corner of left 口
    s3h = anchor_to_xy(('BL', 0.536, 0.01))
    s3t = anchor_to_xy(('ML', 0.961, 0.89))

    fat_line(draw, _shorten(s1h, s1t, 3), _shorten(s1t, s1h, 3), width=W)
    fat_line(draw, _shorten(s2h, s2c, 3), s2c, width=W)
    fat_line(draw, s2c, _shorten(s2t, s2c, 2), width=W)
    fat_line(draw, _shorten(s3h, s3t, 3), _shorten(s3t, s3h, 2), width=W)

    # === Right 向 (strokes 4-9) ===
    # s4: 撇 head TC(0.632,0.718) → tail C(0.418,0.5), curved (pie)
    s4h = anchor_to_xy(('TC', 0.632, 0.718))
    s4t = anchor_to_xy(('C', 0.418, 0.5))
    ctrl = ((s4h[0] + s4t[0]) / 2 + 6, (s4h[1] + s4t[1]) / 2 - 2)
    pts = quad_bezier(s4h, ctrl, s4t, n=32)
    widths = [max(2, int(round(W * (1 - 0.55 * (i / (len(pts) - 1)))))) for i in range(len(pts))]
    stroke_variable_width(draw, pts, widths)

    # s5: 冂 left 竖 head C(0.14,0.506) → tail BC(0.204,0.848)
    s5h = anchor_to_xy(('C', 0.14, 0.506))
    s5t = anchor_to_xy(('BC', 0.204, 0.848))
    fat_line(draw, _shorten(s5h, s5t, 3), s5t, width=W)

    # s6: 横折钩 head C(0.298,0.547) → tail BR(0.068,0.73)
    s6h = anchor_to_xy(('C', 0.298, 0.547))
    s6t = anchor_to_xy(('BR', 0.068, 0.73))
    s6c = (s6t[0], s6h[1])  # top-right corner
    fat_line(draw, _shorten(s6h, s6c, 3), s6c, width=W)
    hook_start = _shorten(s6t, s6c, 10)
    fat_line(draw, s6c, hook_start, width=W)
    # small leftward hook flick
    hook_end = (s6t[0] - 14, s6t[1] - 5)
    fat_line(draw, hook_start, hook_end, width=W)

    # === Inner 口 (strokes 7-9) inside 冂 ===
    s7h = anchor_to_xy(('C', 0.494, 0.872))
    s7t = anchor_to_xy(('BC', 0.632, 0.399))
    s8h = anchor_to_xy(('C', 0.635, 0.884))
    s8t = anchor_to_xy(('BC', 0.948, 0.183))
    s8c = (s8t[0], s8h[1])
    s9h = anchor_to_xy(('BC', 0.685, 0.329))
    s9t = anchor_to_xy(('BR', 0.092, 0.271))

    W_INNER = 7
    fat_line(draw, _shorten(s7h, s7t, 2), _shorten(s7t, s7h, 2), width=W_INNER)
    fat_line(draw, _shorten(s8h, s8c, 2), s8c, width=W_INNER)
    fat_line(draw, s8c, _shorten(s8t, s8c, 2), width=W_INNER)
    fat_line(draw, _shorten(s9h, s9t, 2), _shorten(s9t, s9h, 2), width=W_INNER)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_response(d)
    out = os.path.join(os.path.dirname(__file__), '01_响.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
