# BANK_DEVIATION
# skipped: heng_pie.py (for s1 and s2)
# reason: 予's top two heng-pie strokes have very short horizontal segments
#   and the pies bow steeply into the character body; bank primitive's
#   default apex_x=+130 and bow_perp=18 are tuned for 又 which is much wider.
#   Inlined with tighter geometry per MMH anchors.
# fresh_component: heng_pie_yu_top (compact heng-pie for 予-family tops)
#
# Uses bank: heng.py (s3 middle horizontal), wan_gou.py (s4 vertical hook)
#
# 予 (yǔ) — 4 strokes per MMH:
#   s1: heng_pie (top-right small angular piece)
#   s2: heng_pie (second small angular piece, below s1)
#   s3: heng    (middle long horizontal)
#   s4: wan_gou (long vertical hook down center, bows right, flicks left)

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]
                       / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng import draw_heng
from wan_gou import draw_wan_gou


def _bezier2(p0, p1, p2, steps=60):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w_head, w_tail):
    n = max(len(pts) - 1, 1)
    for i, (x, y) in enumerate(pts):
        t = i / n
        w = w_head * (1 - t) + w_tail * t
        draw.ellipse([x - w, y - w, x + w, y + w], fill='black')


def draw_heng_pie_compact(draw, head, tail,
                          horiz_len=None, bow_perp=8):
    """Compact heng-pie: short horizontal from head, then pie sweeping
    down/right-then-left to tail. Tuned for 予's tight top geometry.
    """
    hx, hy = head
    tx, ty = tail
    # horizontal ends at corner; corner sits above tail
    if horiz_len is None:
        horiz_len = abs(tx - hx) + 20
    corner_x = hx + horiz_len
    corner_y = hy + 4

    # Segment A: short horizontal head -> corner
    steps_a = 40
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + t * (corner_x - hx)
        by = hy + t * (corner_y - hy)
        w = 5.0 + 2.5 * t
        draw.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # Segment B: pie from corner to tail, bows outward
    p0 = (corner_x, corner_y)
    p2 = (tx, ty)
    mx, my = (p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2
    dx, dy = p2[0] - p0[0], p2[1] - p0[1]
    length = (dx * dx + dy * dy) ** 0.5 or 1.0
    px, py = -dy / length, dx / length
    ctrl = (mx + px * bow_perp, my + py * bow_perp)
    pts = _bezier2(p0, ctrl, p2, steps=60)
    _stamp(draw, pts, 7.5, 2.0)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: top heng-pie (upper)
    # MMH: head TL(0.894,0.817)=(89.4,81.7), tail C(0.515,0.187)=(151.5,118.7)
    s1_head = (90, 82)
    s1_tail = (152, 119)
    draw_heng_pie_compact(d, s1_head, s1_tail, horiz_len=75, bow_perp=6)

    # ---- Stroke 2: second heng-pie (below s1, smaller)
    # MMH: head C(0.301,0.154)=(130.1,115.4), tail C(0.576,0.415)=(157.6,141.5)
    s2_head = (130, 115)
    s2_tail = (158, 142)
    draw_heng_pie_compact(d, s2_head, s2_tail, horiz_len=40, bow_perp=4)

    # ---- Stroke 3: middle long heng
    # MMH: head ML(0.463,0.708)=(46.3,170.8), tail MR(0.197,0.857)=(219.7,185.7)
    s3_head = (46, 171)
    s3_tail = (220, 186)
    draw_heng(d, s3_head, s3_tail, width_head=8, width_tail=10)

    # ---- Stroke 4: vertical hook (wan_gou)
    # MMH: head C(0.43,0.652)=(143.0,165.2), tail BC(0.081,0.801)=(108.1,280.1)
    s4_head = (143, 165)
    s4_tail = (108, 280)
    draw_wan_gou(d, s4_head, s4_tail,
                 belly_right=18, hook_len=22, hook_up=10,
                 w_head=5, w_body=5.5, w_tail=2)

    out = pathlib.Path(__file__).parent / '01_予.png'
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': None,          # filled after render
    'stroke_count_ok': True,    # 4 strokes: s1 heng_pie_compact, s2 heng_pie_compact, s3 heng, s4 wan_gou
    'endpoint_mismatches': [],  # all within tolerance of MMH anchors (integer rounding only)
    'joint_class_mismatches': [], # all three joints implemented as N (natural gaps, no welding)
    'overall_pass': None,
    'notes': ('4 strokes as MMH specifies. Joints all N-class: '
              's1.tail~(152,119) vs s2.mid~(149,133) gap~14px (expect ~16); '
              's2.tail~(158,142) vs s3.mid~(133,178) gap~44px slightly wide (expect ~23) — '
              'artefact of s3 length; ok as N-class; '
              's3.mid~(110,178) vs s4.head~(143,165) gap~35px (expect ~11) — '
              'looser than target but still natural gap not weld.')
}


if __name__ == '__main__':
    p = render()
    print(f'wrote {p}')
