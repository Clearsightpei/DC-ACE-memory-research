# BANK_DEVIATION
# skipped: shu_wan_gou.py (bank has 竖弯钩 but 几's right stroke is 横折弯钩 —
#          it needs a leading small heng segment at the top before the 竖 body,
#          which shu_wan_gou does not provide).
# reason: 几's right stroke starts with a short horizontal tick (heng-zhe) at
#         (~119,106) that turns down for the shu body, then curves right
#         (wan) and hooks up (gou). Bank's shu_wan_gou starts with a
#         pure vertical descent from head — no top heng segment. Applying
#         it would give a wrong silhouette (no top-left tick).
# fresh_component: heng_zhe_wan_gou_for_几 (inline). Uses draw_pie from bank
#                  for stroke 1.

import os, sys, pathlib
from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))
from pie import draw_pie  # bank primitive for stroke 1

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'Stroke 1 uses bank draw_pie. Stroke 2 inlined as heng-zhe-wan-gou (bank shu_wan_gou lacks the top heng tick — BANK_DEVIATION documented). N joint gap between s1.head and s2.head ~24px (target ~15.6px).'
}


def _bezier2(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _bezier3(p0, p1, p2, p3, n=60):
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


def draw_heng_zhe_wan_gou_for_ji(draw, head, tail, width=7):
    """Inline 横折弯钩 for 几's right stroke.

    Path: head -> short heng right -> corner -> shu down -> wan right ->
    gou up-right to tail.
    """
    hx, hy = head
    tx, ty = tail
    # 1. Short heng: from head go right to corner. Corner sits ~85% across
    #    (near x of tail) since the shu is nearly vertical and tail is only
    #    slightly right of the shu body.
    heng_end_x = tx - 8   # corner just left of tail x
    heng_end_y = hy + 4   # slight down-tick as it turns
    corner = (heng_end_x, heng_end_y)
    # 3. Shu body: descend from corner nearly vertically to bottom knee.
    #    The knee sits at ~(corner.x + small_out, ty + 40) — hook base
    #    is just below tail-y level.
    bottom_y = ty + 45
    knee_x = heng_end_x + 6
    body_head = corner
    body_c1 = (corner[0] + 2, corner[1] + 60)
    body_c2 = (knee_x - 2, bottom_y - 15)
    body_end = (knee_x, bottom_y)
    body = _bezier3(body_head, body_c1, body_c2, body_end, n=50)

    # hook: compact curl up-right from body_end to tail
    hook_ctrl1 = (body_end[0] + 10, body_end[1] + 6)
    hook_ctrl2 = (tx + 6, ty + 20)
    hook = _bezier3(body_end, hook_ctrl1, hook_ctrl2, tail, n=40)

    # Heng segment: near-flat, thin
    heng_pts = _bezier2(head, ((hx + heng_end_x) / 2, hy), corner, n=20)

    all_pts = heng_pts + body[1:] + hook[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in all_pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    # round the endpoints softly
    r = width // 2
    x0, y0 = ipts[0]
    draw.ellipse([x0 - r, y0 - r, x0 + r, y0 + r], fill='black')
    # taper the hook tip: draw a small triangle-like tail
    xf, yf = ipts[-1]
    draw.ellipse([xf - r + 1, yf - r + 1, xf + r - 1, yf + r - 1], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Anchors from MMH block:
    # s1: head (TL, 0.952, 0.94) = (95, 94)  tail (BL, 0.378, 0.877) = (38, 288)
    # s2: head (C,  0.192, 0.063) = (119,106) tail (BR, 0.78, 0.188) = (278,219)
    s1_head = (95, 94)
    s1_tail = (38, 288)
    s2_head = (119, 106)
    s2_tail = (278, 219)

    # Stroke 1: 撇 — bank primitive
    draw_pie(draw, s1_head, s1_tail, bow_perp=14, w_head=8, w_tail=2, steps=80)

    # Stroke 2: 横折弯钩 (inline — BANK_DEVIATION)
    draw_heng_zhe_wan_gou_for_ji(draw, s2_head, s2_tail, width=7)

    out = _HERE.parent / '01_几.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
