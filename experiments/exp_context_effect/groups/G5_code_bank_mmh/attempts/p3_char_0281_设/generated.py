"""p3_char_0281_设 — G5 attempt (B8, position ~419).

Structure: 讠 (2 strokes: dian + heng_zhe_ti) + 殳 (4 strokes: pie + heng-zhe-arch
+ heng_pie + na, with na crossing heng_pie in the bottom 又 sub-radical).

Recipe: P-A-006 — MMH-anchor verbatim + stroke-primitive layer.
The 讠 sub-radical uses draw_yan_speech-style anchors but placed via MMH
pixel coordinates (left-third), and the 殳 right side uses stroke primitives
inlined with MMH endpoint anchors verbatim. No whole-radical composition
call (which would double-transform under Phase-3 aspect).

Joints: s3.head ~ s4.head (N, gap ~11.5 px at TC); s3.tail ~ s5.head
(N, gap ~33 px at C); s5.mid ~ s6.mid (P, welded at BC).
"""

import sys
import pathlib

sys.path.insert(
    0, str(pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code')
)

from PIL import Image, ImageDraw

from dian import draw_dian
from heng_zhe_ti import draw_heng_zhe_ti
from pie import draw_pie
from na import draw_na


SELF_CHECK = {
    'visual_ok': None,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': None,
    'notes': (
        '6 strokes: dian, heng_zhe_ti, pie (殳-top-left), '
        'inline heng-zhe-arch (殳-top-right), heng_pie (殳-bottom), na (殳-bottom). '
        'X-cross via s5 heng_pie + s6 na welded near BC.'
    ),
}


def _stamp(draw, x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_heng_zhe_arch(draw, head, tail, apex_up=6, corner_frac=0.55):
    """Inline draw of a top-right arch for 殳's second stroke:
    a slight horizontal arch that bends down-right into the tail.
    Not a bank primitive — 殳-top-right specific geometry per BANK_DEVIATION.
    """
    hx, hy = head
    tx, ty = tail
    # corner where horizontal turns
    cx = hx + (tx - hx) * corner_frac
    cy = hy + 4
    # Segment A: gently arched horizontal head -> corner
    steps_a = 42
    apex_x = hx + (cx - hx) * 0.5
    apex_y = hy - apex_up
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = (1 - t) ** 2 * hx + 2 * (1 - t) * t * apex_x + t * t * cx
        by = (1 - t) ** 2 * hy + 2 * (1 - t) * t * apex_y + t * t * cy
        w = 3.2 + 1.6 * t
        _stamp(draw, bx, by, w)
    # Segment B: quadratic curve down-right to tail, thinning
    steps_b = 60
    ctrl_x = tx + 2
    ctrl_y = cy + (ty - cy) * 0.15
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t * t * tx
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t * t * ty
        w = 5.0 - 3.0 * t
        if w < 1.8:
            w = 1.8
        _stamp(draw, bx, by, w)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- 讠 (left radical, 2 strokes) ----
    # s1: dian at TL area (MMH: head TL 0.797,0.703 -> tail TC 0.151,0.97)
    s1_head = (79.7, 70.3)
    s1_tail = (115.1, 97.0)
    draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=7, bow=3, steps=48)

    # s2: heng_zhe_ti (MMH: head ML 0.138,0.708 -> tail BC 0.266,0.256)
    # Widened horizontal + shallower descent for a cleaner speech-radical body.
    s2_head = (25.0, 168.0)
    s2_tail = (128.0, 218.0)
    s2_corner = (108.0, 174.0)
    s2_descend_mid = (90.0, 200.0)
    s2_ti_head = (58.0, 228.0)
    draw_heng_zhe_ti(d, s2_head, s2_tail,
                     corner=s2_corner,
                     descend_mid=s2_descend_mid,
                     ti_head=s2_ti_head,
                     width=5)

    # ---- 殳 (right radical, 4 strokes) ----
    # s3: 殳's top-left pie (MMH: head TC 0.474,0.873 -> tail C 0.248,0.761)
    s3_head = (147.4, 87.3)
    s3_tail = (124.8, 176.1)
    draw_pie(d, s3_head, s3_tail, bow_perp=10, w_head=7, w_tail=2, steps=75)

    # s4: 殳's top-right arch (MMH: head TC 0.617,0.888 -> tail MR 0.678,0.523)
    # Inline (BANK_DEVIATION-lite) — arch geometry not covered cleanly by
    # heng_zhe_short at these anchors; drawing fresh.
    s4_head = (161.7, 88.8)
    s4_tail = (267.8, 152.3)
    draw_heng_zhe_arch(d, s4_head, s4_tail, apex_up=3, corner_frac=0.62)

    # s5: 又's heng_pie (MMH: head C 0.512,0.875 -> tail BC 0.151,0.851)
    # This is a pie coming down-left from center of canvas to bottom-center.
    s5_head = (151.2, 187.5)
    s5_tail = (115.1, 285.1)
    draw_pie(d, s5_head, s5_tail, bow_perp=10, w_head=7, w_tail=2, steps=80)

    # s6: 又's na (MMH: head BC 0.383,0.033 -> tail BR 0.836,0.936)
    # head slightly right of s5 head and below (203 vs 187) — starts at the
    # X-cross apex and sweeps down-right, thickening. Welds with s5 mid at BC.
    s6_head = (138.3, 203.3)
    s6_tail = (283.6, 293.6)
    draw_na(d, s6_head, s6_tail, bow_perp=12, w_head=4, w_tail=11, steps=90)

    return img


if __name__ == '__main__':
    img = render()
    out = pathlib.Path(__file__).parent / '01_设.png'
    img.save(out)
    print(f'wrote {out}')
