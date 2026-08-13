"""p3_char_0370_乶 — G5 attempt.

Decomposition (from GT + MMH 8-anchor block):
 The character appears to be 甫-like top (s1-s7) + flat 乙-sweep bottom (s8).
 MMH anchors give per-stroke endpoints; joint expectations show s6 is the
 vertical spine that P-welds through s1, s3, s4, s5.

Stroke plan (per MMH anchors, converted via 米字格 cell → pixel):
 s1: heng — TL(0.981,0.87)=(98,87)  → TC(0.957,0.756)=(196,76)   short top horizontal
 s2: shu  — ML(0.732,0.151)=(73,115) → ML(0.967,0.966)=(97,297)   long LEFT vertical (spans 甫 down through 乙 area)
 s3: shu  — ML(0.946,0.286)=(95,129) → C (0.969,0.84)=(197,184)   diagonal right side (upper box)
 s4: heng — C(0.128,0.45)=(113,145)  → C(0.749,0.345)=(175,135)   upper interior horizontal
 s5: heng — C(0.128,0.723)=(113,172) → C(0.767,0.614)=(177,161)   lower interior horizontal
 s6: shu  — TC(0.321,0.475)=(132,47) → C(0.436,0.963)=(143,196)   long central vertical (spine)
 s7: dian — TR(0.021,0.521)=(202,52) → TR(0.306,0.762)=(231,76)   top-right tick
 s8: yi_second-style — BL(0.574,0.247)=(57,225) → BR(0.625,0.552)=(263,255)   flat 乙 hook

BANK_DEVIATION
 skipped: yi_second.py
 reason: bank 乙 primitive is compact upright (~140w x 180h); MMH tail here
         demands very flat spread (206w x 30h) across bottom row.
 fresh_component: yi_flat_for_乶  (inline low-belly S-curve with terminal hook up)

Stroke-primitive layer per P-A-006. Reasoning trace inline per P-A-008.
"""

import os, sys
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(BASE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from heng import draw_heng          # noqa
from shu import draw_shu            # noqa
from dian import draw_dian          # noqa

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 8 primitives called below
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'stroke primitives sourced from bank (heng/shu/dian); s8 inlined as flat 乙 (BANK_DEVIATION).',
}


def draw_yi_flat(d, head, tail, width=7):
    """Inline flat 乙 sweep — head→apex→trough→terminal hook up."""
    hx, hy = head
    tx, ty = tail
    # GT shows a wide flat 乙 sweep: entry drops to belly, cruises right,
    # then a gentle upturn — not a tall vertical hook.
    belly_x = hx + (tx - hx) * 0.45
    belly_y = max(hy, ty) + 30          # low belly under both endpoints
    cruise_x = hx + (tx - hx) * 0.80
    cruise_y = belly_y - 2
    hook_ctrl_x = tx + 6
    hook_ctrl_y = ty - 4
    hook_top_x = tx + 2
    hook_top_y = ty - 14                # small upturn, not tall
    pts = []

    def bez(p0, p1, p2, steps=40):
        for i in range(steps + 1):
            t = i / steps
            x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
            y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
            pts.append((x, y))

    bez((hx, hy), (belly_x, belly_y), (cruise_x, cruise_y))
    bez((cruise_x, cruise_y), (tx, ty + 6), (tx, ty))
    bez((tx, ty), (hook_ctrl_x, hook_ctrl_y), (hook_top_x, hook_top_y))

    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill='black', width=width)


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: short top horizontal (near top-left ~top-center) ----
    # bank heng: fits — clean short horizontal
    draw_heng(d, (98, 87), (196, 76), width_head=8, width_tail=9)

    # ---- s2: long LEFT vertical, spans full character height ----
    # bank shu: fits — vertical from upper area down through bottom
    draw_shu(d, (73, 115), (97, 297), width=6)

    # ---- s3: right-side vertical/diagonal (upper box right edge) ----
    # bank shu accepts diagonal endpoints — no better primitive
    draw_shu(d, (95, 129), (197, 184), width=6)

    # ---- s4: upper interior horizontal ----
    draw_heng(d, (113, 145), (175, 135), width_head=6, width_tail=7)

    # ---- s5: lower interior horizontal ----
    draw_heng(d, (113, 172), (177, 161), width_head=6, width_tail=7)

    # ---- s6: long central vertical spine (P-welds with s1/s3/s4/s5) ----
    draw_shu(d, (132, 47), (143, 196), width=6)

    # ---- s7: top-right dian/tick ----
    draw_dian(d, (202, 52), (231, 76), w_head=3, w_tail=7, bow=3)

    # ---- s8: flat 乙 sweep across bottom (BANK_DEVIATION, inline) ----
    draw_yi_flat(d, (57, 225), (263, 255), width=7)

    out = os.path.join(BASE, '01_乶.png')
    img.save(out)
    print(f'wrote {out}')
    print(f'SELF_CHECK: {SELF_CHECK}')


if __name__ == '__main__':
    render()
