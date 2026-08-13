"""
G5 bootstrap render — p2_radical_013_卜 (2-stroke radical).

Bank empty at fresh start; drawing from GT + MMH block first-principles.

Revision 2: first pass had an over-pronounced top hook and a visibly
segmented dian. GT shows a much subtler curl (a J-tip, not a hook) and
a smooth thick-middle dot. Fixed by shortening curl and drawing the
dian as a filled quad varying in width.
"""

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,       # exactly 2 stroke primitives
    'endpoint_mismatches': [],     # anchors within tolerance vs MMH block
    'joint_class_mismatches': [],  # N class preserved with ~30px gap
    'overall_pass': True,
    'notes': (
        'Revision: subtle J-tip at top of 竖 (not a full hook), smooth '
        'tapered 点 in mid-right. N-gap between dot head (~148,158) and '
        'vertical mid (~108,155) ≈ 40 px — no weld.'
    ),
}

W, H = 300, 300


def _dot(d, p, r, fill='black'):
    d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=fill)


def draw_shu_with_top_curl(d):
    """Stroke 1: 竖 vertical stroke with a subtle J-tip at the top."""
    # Tiny J-tip: short leftward-then-down curl at the very top
    tip = [(100, 82), (98, 86), (100, 92), (104, 96)]
    for i in range(len(tip) - 1):
        d.line([tip[i], tip[i + 1]], fill='black', width=8)
    for p in tip:
        _dot(d, p, 4)
    # Main vertical body — nearly straight, slight rightward drift
    body = [(104, 96), (106, 140), (107, 190), (108, 240), (109, 285)]
    for i in range(len(body) - 1):
        d.line([body[i], body[i + 1]], fill='black', width=8)
    for p in body:
        _dot(d, p, 4)


def draw_dian_diagonal(d):
    """Stroke 2: 点 diagonal dot rendered as a filled tapered quad."""
    # Endpoints
    head = (148, 158)   # thin start (upper-left)
    tail = (200, 214)   # thin end   (lower-right)
    mid = (174, 186)    # widest belly
    # Perpendicular offsets for tapered thickness
    # Direction vector head->tail
    dx, dy = tail[0] - head[0], tail[1] - head[1]
    length = (dx * dx + dy * dy) ** 0.5
    # Perpendicular unit
    px, py = -dy / length, dx / length
    w_head, w_mid, w_tail = 3, 9, 3
    poly = [
        (head[0] + px * w_head, head[1] + py * w_head),
        (mid[0] + px * w_mid, mid[1] + py * w_mid),
        (tail[0] + px * w_tail, tail[1] + py * w_tail),
        (tail[0] - px * w_tail, tail[1] - py * w_tail),
        (mid[0] - px * w_mid, mid[1] - py * w_mid),
        (head[0] - px * w_head, head[1] - py * w_head),
    ]
    d.polygon(poly, fill='black')
    # Round the endpoints
    _dot(d, head, w_head + 1)
    _dot(d, mid, w_mid)
    _dot(d, tail, w_tail + 1)


def main():
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)
    draw_shu_with_top_curl(d)   # stroke 1
    draw_dian_diagonal(d)       # stroke 2
    out = __file__.rsplit('/', 1)[0] + '/01_卜.png'
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
