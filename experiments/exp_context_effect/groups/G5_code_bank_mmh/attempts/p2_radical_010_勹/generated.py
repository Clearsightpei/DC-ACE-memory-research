"""
勹 (bao) — 2-stroke radical.
Bank is empty (fresh G5 start). Drawing from GT + MMH-derived anchors.

米字格 layout on 300x300: 3x3 cells of 100px each.
Cell (col, row) -> origin (col*100, row*100), local frac maps within it.

MMH anchors:
  s1 head @ TC(0.116, 0.645) -> (111.6, 64.5)     — top-center short 撇
  s1 tail @ ML(0.56,  0.682) -> (56.0, 168.2)
  s2 head @ ML(0.987, 0.336) -> (98.7, 133.6)     — start of 橫折鉤
  s2 tail @ BC(0.453, 0.742) -> (145.3, 274.2)
Joint: s1.mid(0.65) ⇆ s2.head is class N (~17px gap — do NOT weld).
"""

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,     # 2 strokes drawn
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': 'Fresh start — no bank. Stroke 2 is a curved 橫折鉤 through the top-right, arcing down and inward to the bottom-center.',
}

CELLS = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}

def anchor(cell, xf, yf):
    ox, oy = CELLS[cell]
    return (ox + xf * 100, oy + yf * 100)


def draw_pie_short(draw, p_head, p_tail, width=6):
    """Short 撇 — slight leftward bow."""
    hx, hy = p_head
    tx, ty = p_tail
    # midpoint pulled slightly left/down to give the 撇 curve
    mx = (hx + tx) / 2 - 4
    my = (hy + ty) / 2 + 2
    # sample a quadratic bezier
    pts = []
    N = 40
    for i in range(N + 1):
        t = i / N
        x = (1 - t) ** 2 * hx + 2 * (1 - t) * t * mx + t ** 2 * tx
        y = (1 - t) ** 2 * hy + 2 * (1 - t) * t * my + t ** 2 * ty
        pts.append((x, y))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill='black', width=width)


def draw_heng_zhe_gou_bao(draw, p_head, p_tail, width=6):
    """
    橫折鉤 for 勹: from left-middle area, go up-right across the top,
    turn down along the right, curve back to bottom-center with a small hook.
    p_head at ~(99,134), p_tail at ~(145,274).
    """
    hx, hy = p_head
    tx, ty = p_tail

    # Path control points (hand-designed to trace 勹's wrapper):
    #  - horizontal top: from head, arc up-right to a top-right shoulder
    top_shoulder = (215, 108)     # upper-right corner region
    #  - right side descending: bow slightly outward (right)
    right_bulge = (230, 200)
    #  - approach to tail via bottom curve
    bottom_curve = (200, 258)

    ctrl = [p_head, (150, 118), top_shoulder, (232, 150), right_bulge, bottom_curve, p_tail]

    # Sample a smooth polyline through control points using Catmull-Rom-ish
    def catmull(p0, p1, p2, p3, N=25):
        pts = []
        for i in range(N):
            t = i / N
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) +
                       (-p0[0] + p2[0]) * t +
                       (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 +
                       (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) +
                       (-p0[1] + p2[1]) * t +
                       (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 +
                       (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            pts.append((x, y))
        return pts

    padded = [ctrl[0]] + ctrl + [ctrl[-1]]
    all_pts = []
    for i in range(len(padded) - 3):
        all_pts.extend(catmull(padded[i], padded[i + 1], padded[i + 2], padded[i + 3]))
    all_pts.append(p_tail)

    for i in range(len(all_pts) - 1):
        draw.line([all_pts[i], all_pts[i + 1]], fill='black', width=width)

    # small hook at tail — a short flick up-left
    hook_end = (tx - 10, ty - 14)
    draw.line([p_tail, hook_end], fill='black', width=width)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    s1_head = anchor('TC', 0.116, 0.645)   # (111.6, 64.5)
    s1_tail = anchor('ML', 0.56,  0.682)   # (56.0, 168.2)

    s2_head = anchor('ML', 0.987, 0.336)   # (98.7, 133.6)
    s2_tail = anchor('BC', 0.453, 0.742)   # (145.3, 274.2)

    # Stroke 1
    draw_pie_short(draw, s1_head, s1_tail, width=6)
    # Stroke 2 (starts with N-gap from s1's midpoint region)
    draw_heng_zhe_gou_bao(draw, s2_head, s2_tail, width=6)

    out = '<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/attempts/p2_radical_010_勹/01_勹.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
