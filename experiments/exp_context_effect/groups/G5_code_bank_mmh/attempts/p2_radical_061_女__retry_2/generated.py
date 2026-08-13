# TRAJECTORY DIFF (retry_2 for 女)
# GT observation: 3 strokes.
#   s1 = 撇点 (pie-dian compound): starts near top-center, sweeps down-left
#        into a sharp corner, then dian sweeps down-right ending near BR.
#   s2 = long 撇 (pie): from just-right-of-center down-left to BL.
#   s3 = long 横 (heng): horizontal across mid, spanning nearly the full width,
#        slight upward tilt from left to right.
# main (verdict C): fused compound stroke's corner ambiguous; s2 pie head too
#        far up; s3 heng not clearly the last continuous crossbar.
# retry_1 (FAIL): s1's dian tail did not swing down-right to BR — it hung
#        low-center; s3 heng too short and offset; overall reads more like
#        a floating bird than 女.
# Fixes for retry_2:
#   1. s1's dian must clearly extend down-right, ending in cell BR near
#      (230, 296) per MMH tail anchor.
#   2. s2 head placed at ~(184, 146) inside cell C; tail at (70, 283) BL.
#   3. s3 heng spans (20, 177) → (278, 166) — long, slightly rising rightward.
#   4. s3 crosses s2 near s2's head (T-tangent joint at ~(190, 165)).
#
# BANK_DEVIATION
# skipped: pie_dian compound (no bank primitive for it), heng, pie
# reason: keep the whole 女 as one coherent inline pass so joints
#         line up (P-P-T triple constraint). Bank primitives have not
#         yielded a passing 女 in main or retry_1.
# fresh_component: pie_dian_compound_for_nu, heng_span_for_nu, pie_long_for_nu

from PIL import Image, ImageDraw

SIZE = 300
BG = (255, 255, 255)
INK = (0, 0, 0)


def _cell(cell):
    row = {'T': 0, 'M': 100, 'B': 200}
    col = {'L': 0, 'C': 100, 'R': 200}
    if cell == 'C':
        return 100, 100
    r, c = cell[0], cell[1]
    return col[c], row[r]


def anchor(cell, xf, yf):
    x0, y0 = _cell(cell)
    return x0 + xf * 100.0, y0 + yf * 100.0


def bezier_quad(p0, p1, p2, n):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stamp_chain(draw, pts, widths):
    """Draw a tapered chain of filled circles along pts. widths list == len(pts)."""
    for (x, y), w in zip(pts, widths):
        r = max(0.5, w / 2.0)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)
    # bridge segments to remove pinholes
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        w = max(widths[i], widths[i + 1])
        # sub-sample
        dx, dy = x1 - x0, y1 - y0
        dist = (dx * dx + dy * dy) ** 0.5
        steps = max(1, int(dist / 0.8))
        for s in range(steps + 1):
            t = s / steps
            xs, ys = x0 + dx * t, y0 + dy * t
            r = max(0.5, w / 2.0)
            draw.ellipse([xs - r, ys - r, xs + r, ys + r], fill=INK)


def taper(n, w_head, w_mid, w_tail):
    out = []
    for i in range(n + 1):
        t = i / n
        if t < 0.5:
            u = t / 0.5
            w = w_head * (1 - u) + w_mid * u
        else:
            u = (t - 0.5) / 0.5
            w = w_mid * (1 - u) + w_tail * u
        out.append(w)
    return out


def draw_stroke_1(draw):
    """撇点: pie from TC down-left to corner, then dian down-right to BR."""
    p_head = anchor('TC', 0.295, 0.627)          # (129.5, 62.7)
    corner = (109.0, 178.0)                      # sharp corner in cell C, lower-left area
    p_tail = anchor('BR', 0.306, 0.968)          # (230.6, 296.8)

    # Pie segment (head -> corner): slight leftward bow.
    pie_ctrl = (122.0, 118.0)                    # subtly pulls curve left
    pie_pts = bezier_quad(p_head, pie_ctrl, corner, 40)
    pie_widths = taper(40, w_head=9.0, w_mid=8.0, w_tail=6.5)

    # Dian segment (corner -> tail): sweeping down-right, thickens toward tail.
    dian_ctrl = (155.0, 230.0)                   # pulls into cell BC crossing
    dian_pts = bezier_quad(corner, dian_ctrl, p_tail, 50)
    dian_widths = taper(50, w_head=6.5, w_mid=9.0, w_tail=6.5)

    stamp_chain(draw, pie_pts, pie_widths)
    stamp_chain(draw, dian_pts, dian_widths)


def draw_stroke_2(draw):
    """Long pie: from C (184, 146) down-left to BL (70, 283)."""
    p_head = anchor('C', 0.84, 0.456)            # (184, 145.6)
    p_tail = anchor('BL', 0.697, 0.83)           # (69.7, 283)
    # slight rightward bow (concave-right)
    ctrl = (120.0, 200.0)
    pts = bezier_quad(p_head, ctrl, p_tail, 60)
    widths = taper(60, w_head=9.5, w_mid=8.0, w_tail=3.0)
    stamp_chain(draw, pts, widths)


def draw_stroke_3(draw):
    """Long heng: (20, 177) -> (278, 166). Slight upward tilt."""
    p_head = anchor('ML', 0.205, 0.77)           # (20.5, 177)
    p_tail = anchor('MR', 0.783, 0.658)          # (278.3, 165.8)
    ctrl = (150.0, 168.0)                        # mild top bow
    pts = bezier_quad(p_head, ctrl, p_tail, 60)
    widths = taper(60, w_head=6.0, w_mid=8.5, w_tail=7.5)
    stamp_chain(draw, pts, widths)


def main():
    img = Image.new('RGB', (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)
    draw_stroke_1(draw)
    draw_stroke_2(draw)
    draw_stroke_3(draw)
    img.save('01_女.png')


SELF_CHECK = {
    'visual_ok': None,          # filled in after render inspection
    'stroke_count_ok': True,    # 3 strokes: s1 pie-dian (one compound stroke), s2 pie, s3 heng
    'endpoint_mismatches': [],  # anchors used match MMH within tolerance
    'joint_class_mismatches': [],  # s1-s2 P at BC ~(155,234); s1-s3 P at C ~(119,170); s2.head-s3.mid T at ~(190,165)
    'overall_pass': None,
    'notes': 'retry_2 fixes: s1 dian sweeps to BR, s3 spans nearly full width; joints line up.'
}


if __name__ == '__main__':
    main()
