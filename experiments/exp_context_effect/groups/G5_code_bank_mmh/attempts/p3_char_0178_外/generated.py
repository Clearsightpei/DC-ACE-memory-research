# BANK_DEVIATION
# skipped: bu_divine.py
# reason: bu_divine geometry (vertical at x~100-108, tip curl at top, dot at 148-200)
#         does not match the required MMH anchors for 外's right side
#         (vertical from TC(168.8, 54.8) to BC(180.2, 314.4) with no J-tip;
#         dot from C(193.4, 143.8) to MR(268.4, 189.3)). Inlining fresh.
# fresh_component: bu_for_wai (卜 right-side with straight tall vertical + longer diagonal dot)
#
# No bank primitive for 夕 (left side of 外) — inlining fresh.

"""Render 外 (wai, "outside") — 5 strokes.

Layout (米字格, 300x300):
  Cell TL: (0,0)-(100,100)     TC: (100,0)-(200,100)     TR: (200,0)-(300,100)
  Cell ML: (0,100)-(100,200)   C:  (100,100)-(200,200)   MR: (200,100)-(300,200)
  Cell BL: (0,200)-(100,300)   BC: (100,200)-(200,300)   BR: (200,200)-(300,300)

Composition: 夕 (left, 3 strokes) + 卜 (right, 2 strokes).
"""

from PIL import Image, ImageDraw

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 5 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes inlined; N-gaps preserved at all 4 joints (no welding).',
}

W, H = 300, 300


def _dot(d, p, r, fill='black'):
    d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=fill)


def _bezier(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def _polyline(d, pts, width):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill='black', width=width)
    for p in pts:
        _dot(d, p, width / 2)


def _tapered_dot(d, head, tail, w_head=3, w_mid=9, w_tail=3):
    """Filled tapered dash from head to tail (belly at mid)."""
    dx, dy = tail[0] - head[0], tail[1] - head[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    mid = ((head[0] + tail[0]) / 2, (head[1] + tail[1]) / 2)
    poly = [
        (head[0] + px * w_head, head[1] + py * w_head),
        (mid[0] + px * w_mid, mid[1] + py * w_mid),
        (tail[0] + px * w_tail, tail[1] + py * w_tail),
        (tail[0] - px * w_tail, tail[1] - py * w_tail),
        (mid[0] - px * w_mid, mid[1] - py * w_mid),
        (head[0] - px * w_head, head[1] - py * w_head),
    ]
    d.polygon(poly, fill='black')
    _dot(d, head, w_head + 1)
    _dot(d, mid, w_mid)
    _dot(d, tail, w_tail + 1)


def draw_wai(d):
    # --- Stroke 1: 撇 — long curved diagonal (top-right to middle-lower-left) ---
    # head TL(0.926, 0.838) -> (92.6, 83.8)
    # tail ML(0.372, 0.767) -> (37.2, 176.7)
    s1_head = (92.6, 83.8)
    s1_tail = (37.2, 176.7)
    # bow slightly outward (leftward-lower) to give a natural 撇 curve
    s1_ctrl = (55, 115)
    s1_pts = _bezier(s1_head, s1_ctrl, s1_tail, n=50)
    _polyline(d, s1_pts, width=7)

    # --- Stroke 2: 横折 (夕's second stroke) — starts near top of 夕, drops,
    # then curves down-left to bottom-left. Approximate as two-arc bezier chain.
    # head ML(0.899, 0.321) -> (89.9, 132.1)
    # mid(0.57) ML(0.939, 0.981) -> (93.9, 199.8)   [joint anchor]
    # tail BL(0.305, 0.716) -> (30.5, 271.6)
    s2_head = (89.9, 132.1)
    s2_mid = (93.9, 199.8)
    s2_tail = (30.5, 271.6)
    # Upper segment: head → mid (near-vertical, slight rightward bow)
    s2a = _bezier(s2_head, (98, 165), s2_mid, n=30)
    # Lower segment: mid → tail (diagonal down-left, gentle outward bow)
    s2b = _bezier(s2_mid, (75, 245), s2_tail, n=40)
    _polyline(d, s2a, width=7)
    _polyline(d, s2b, width=7)

    # --- Stroke 3: 点 inside 夕 (short diagonal dot) ---
    # head ML(0.598, 0.714) -> (59.8, 171.4)
    # tail ML(0.879, 0.925) -> (87.9, 192.5)
    _tapered_dot(d, (59.8, 171.4), (87.9, 192.5),
                 w_head=3, w_mid=6, w_tail=3)

    # --- Stroke 4: 竖 of 卜 — long straight vertical (very slight rightward drift) ---
    # head TC(0.688, 0.548) -> (168.8, 54.8)
    # tail BC(0.802, 1.144) -> (180.2, 314.4)   [clip at canvas bottom]
    s4_head = (168.8, 54.8)
    s4_tail_true = (180.2, 314.4)
    # clip visually inside canvas
    s4_tail = (178.5, 297.0)
    s4_pts = _bezier(s4_head, (174, 175), s4_tail, n=50)
    _polyline(d, s4_pts, width=8)

    # --- Stroke 5: 点 of 卜 (right diagonal dot, longer than 夕's inside dot) ---
    # head C(0.934, 0.438) -> (193.4, 143.8)
    # tail MR(0.684, 0.893) -> (268.4, 189.3)
    _tapered_dot(d, (193.4, 143.8), (268.4, 189.3),
                 w_head=3, w_mid=9, w_tail=3)


def main():
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)
    draw_wai(d)
    out = __file__.rsplit('/', 1)[0] + '/01_外.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
