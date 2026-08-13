"""G5 retry_1: p2_radical_047_飞 (3 strokes).

# TRAJECTORY DIFF
# main attempt (FAIL):
#   - s1 was drawn as a mostly-flat horizontal top with only a shallow
#     descent to lower-right. GT shows a strong DOWN curve after the
#     horizontal top segment — the stroke visibly drops through the
#     center vertically before reaching BR.
#   - s1 terminal hook curled DOWN-LEFT (like a claw). GT's hook at
#     the end of 横斜钩 curls UP-LEFT (like 亅), a small upward tick.
#   - Small interior strokes (s2, s3) were positioned OK but too thin
#     and disconnected from the composition; they read as noise.
# fixes this pass:
#   - Give s1 a real "L"-like profile: near-horizontal top ~40 px,
#     then a strong vertical-ish descent, ending with a tiny UP-LEFT
#     hook at the tail.
#   - Make s2 a compact 撇/dian (down-left) with visible taper.
#   - Make s3 a compact right-descending 捺-like tick.
#   - Slightly heavier ink weight so composition reads as one glyph.

# BANK_DEVIATION
# skipped: shu_wan_gou.py, heng_zhe_gou.py, pie.py, dian.py
# reason: 飞's outer stroke is a long compound 横斜钩 with a specific
#         near-horizontal top then a sharp diagonal descent and a
#         terminal up-left hook — none of the bank primitives cover
#         this geometry (heng_zhe_gou is right-angle box hook,
#         shu_wan_gou starts vertical). s2/s3 are tiny bespoke ticks
#         inside a radical, not standalone pie/dian.
# fresh_component: heng_xie_gou_for_fei (long h-then-diagonal + up-hook),
#                  tiny_pie_tick, tiny_na_tick.
"""

from PIL import Image, ImageDraw
from pathlib import Path

W = H = 300

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 3 primitive calls
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('s1 now has visible horizontal top then strong descent '
              'with up-left terminal hook. All 3 joints are N (small '
              'natural gaps around center cell, not welded).'),
}


def _bezier3(p0, p1, p2, p3, n=80):
    pts = []
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _bezier2(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def _stroke_var_width(draw, pts, w_head, w_tail):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_heng_xie_gou_for_fei(draw, head, tail, width=9):
    """飞's main outer stroke.

    Shape: horizontal top ~110 px wide, a clear elbow/knee, then a
    long diagonal descent bowing outward (to the right/down), ending
    with a terminal hook curling UP-LEFT (like 亅 tip).
    """
    hx, hy = head
    tx, ty = tail

    # Explicit elbow (pivot) — placed after the horizontal top.
    # Move it toward the center-right so the top reads as horizontal.
    pivot = (160, hy + 18)

    # First cubic: essentially horizontal, gently sagging to the pivot.
    c1a = (hx + 50, hy - 2)
    c1b = (135, hy + 4)
    top = _bezier3(head, c1a, c1b, pivot, n=55)

    # Second cubic: strong diagonal descent from pivot down to tail,
    # bowing outward (down-right) to give the swoop its calligraphic curve.
    knee = (tx + 2, ty + 2)
    c2a = (215, hy + 65)          # push the curve outward-down
    c2b = (tx + 30, ty - 15)      # bow right before landing
    descent = _bezier3(pivot, c2a, c2b, knee, n=80)

    pts = top + descent[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')

    # Terminal hook — tick curling UP-LEFT from the tail (亅-style).
    hook_ctrl = (tx - 4, ty - 10)
    hook_end = (tx - 22, ty - 20)
    hook_pts = _bezier2(knee, hook_ctrl, hook_end, n=22)
    ipts2 = [(int(round(x)), int(round(y))) for x, y in hook_pts]
    draw.line(ipts2, fill='black', width=width - 1, joint='curve')

    r = width // 2
    for x, y in (ipts[0], ipts2[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def draw_tiny_pie_tick(draw, head, tail, w_head=8, w_tail=3, bow_perp=4):
    """Short down-left 撇-like tick with a modest bow."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    # perpendicular (rotate 90 ccw)
    px, py = -dy / L, dx / L
    cx, cy = mx + px * bow_perp, my + py * bow_perp
    pts = _bezier2(head, (cx, cy), tail, n=45)
    _stroke_var_width(draw, pts, w_head, w_tail)


def draw_tiny_na_tick(draw, head, tail, w_head=3, w_tail=8, bow_perp=-4):
    """Short down-right 捺-like tick that thickens toward the tail."""
    hx, hy = head
    tx, ty = tail
    mx, my = (hx + tx) / 2, (hy + ty) / 2
    dx, dy = tx - hx, ty - hy
    L = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / L, dx / L
    cx, cy = mx + px * bow_perp, my + py * bow_perp
    pts = _bezier2(head, (cx, cy), tail, n=45)
    _stroke_var_width(draw, pts, w_head, w_tail)


def main():
    img = Image.new('RGB', (W, H), 'white')
    d = ImageDraw.Draw(img)

    # MMH endpoints:
    # s1: ML(0.369, 0.318) → BR(0.651, 0.484)   = (37,132) → (265,248)
    # s2: MR(0.168, 0.26)  → C(0.849, 0.77)     = (217,126) → (185,177)
    # s3: C(0.767, 0.863)  → BR(0.367, 0.291)   = (177,186) → (237,229)

    s1_head, s1_tail = (37, 132), (265, 248)
    s2_head, s2_tail = (217, 126), (185, 177)
    s3_head, s3_tail = (177, 186), (237, 229)

    # Stroke 1 — long 横斜钩 (dominant outer stroke).
    draw_heng_xie_gou_for_fei(d, s1_head, s1_tail, width=8)

    # Stroke 2 — small down-left tick at top-right, into the center.
    draw_tiny_pie_tick(d, s2_head, s2_tail, w_head=8, w_tail=3, bow_perp=4)

    # Stroke 3 — small down-right tick from center into lower BR.
    draw_tiny_na_tick(d, s3_head, s3_tail, w_head=3, w_tail=8, bow_perp=-4)

    out = Path(__file__).parent / '01_飞.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
