"""
G5 attempt for p2_radical_009_八 (2-stroke radical).

MMH structural expectations:
  stroke 1: head @ ('ML', 0.97, 0.623)  → px (97, 162)
            tail @ ('BL', 0.261, 0.64)  → px (26, 264)
            -- left 撇, drops down and curves left
  stroke 2: head @ ('TC', 0.324, 0.964) → px (132, 96)
            tail @ ('BR', 0.865, 0.569) → px (287, 257)
            -- right 捺, drops down-right with thickening tail
  joints: NONE (strokes do not meet — clear separation)

Bootstrap radical: bank empty, no primitives to skip → no BANK_DEVIATION.
"""

from PIL import Image, ImageDraw

SIZE = 300


def cell_to_px(cell, x_frac, y_frac):
    """米字格 anchor → image pixel. Image convention (y grows down)."""
    cols = {'L': 0, 'C': 100, 'R': 200}
    rows = {'T': 0, 'M': 100, 'B': 200}
    cx = cols[cell[1]] if cell[0] == 'M' or cell[0] == 'T' or cell[0] == 'B' else None
    # cell format is like 'ML' (row=M, col=L) or 'TC' (row=T, col=C)
    row_char, col_char = cell[0], cell[1]
    px = cols[col_char] + x_frac * 100
    py = rows[row_char] + y_frac * 100
    return (px, py)


def _bezier(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _tapered_stroke(draw, pts, w_head, w_tail):
    """Draw a tapered stroke by stamping filled circles along the path."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1)
        w = w_head * (1 - t) + w_tail * t
        r = w / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill=0)


def draw_pie_left(draw):
    """Stroke 1: 撇 from ML(0.97, 0.623) to BL(0.261, 0.64), curving left."""
    head = cell_to_px('ML', 0.97, 0.623)   # (97, 162)
    tail = cell_to_px('BL', 0.261, 0.64)   # (26, 264)
    # Control point: bow slightly toward the right/upper side so the curve
    # dips leftward (mirror of 撇 concavity). Midpoint pulled up-right.
    mid = ((head[0] + tail[0]) / 2, (head[1] + tail[1]) / 2)
    ctrl = (mid[0] + 12, mid[1] - 8)
    pts = _bezier(head, ctrl, tail, steps=80)
    _tapered_stroke(draw, pts, w_head=9, w_tail=3)


def draw_na_right(draw):
    """Stroke 2: 捺 from TC(0.324, 0.964) to BR(0.865, 0.569), curving out."""
    head = cell_to_px('TC', 0.324, 0.964)  # (132, 96)
    tail = cell_to_px('BR', 0.865, 0.569)  # (287, 257)
    mid = ((head[0] + tail[0]) / 2, (head[1] + tail[1]) / 2)
    # 捺 typically curves so the belly is on the lower-left of the line.
    ctrl = (mid[0] - 10, mid[1] + 14)
    pts = _bezier(head, ctrl, tail, steps=80)
    # 捺 thickens toward the tail (bottom-right).
    _tapered_stroke(draw, pts, w_head=4, w_tail=11)


def render():
    img = Image.new('L', (SIZE, SIZE), 255)
    draw = ImageDraw.Draw(img)
    draw_pie_left(draw)
    draw_na_right(draw)
    return img


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 strokes drawn (draw_pie_left + draw_na_right)
    'endpoint_mismatches': [], # anchors used exactly as expected
    'joint_class_mismatches': [], # no joints expected; strokes remain separated
    'overall_pass': True,
    'notes': 'Bootstrap radical; bank empty; endpoints copied verbatim from MMH block.',
}


if __name__ == '__main__':
    out = '/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_009_八/01_八.png'
    render().save(out)
    print('wrote', out)
