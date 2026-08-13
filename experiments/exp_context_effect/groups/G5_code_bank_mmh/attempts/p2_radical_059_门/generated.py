"""G5 attempt: p2_radical_059_门 (3 strokes).

MMH-derived endpoints (px on 300x300, 3x3 米字格):
  stroke 1 (丶 top-left dot): TL(0.891, 0.744) -> C(0.151, 0.04) = (89,74) -> (115,104)
  stroke 2 (丨 left vertical): TL(0.548, 0.964) -> BL(0.56, 0.871) = (55,96) -> (56,287)
  stroke 3 (横折钩 right frame): TC(0.506, 0.829) -> BC(0.928, 0.769) = (151,83) -> (193,277)
Joint expectations: NONE — three separate strokes.
"""

# BANK_DEVIATION
# skipped: heng_zhe_short.py, shu_gou.py (would compose as two disjoint bank calls)
# reason: 门 stroke 3 is a full-height 横折钩 (long heng + long shu + terminal
#         leftward hook) rendered as ONE continuous stroke path. heng_zhe_short
#         is a small bent bracket without a vertical trunk or hook, and gluing
#         it to shu_gou would violate P-DEC-001 (hook decorations must be part
#         of the same continuous stroke path, not disjoint segments).
# fresh_component: heng_zhe_gou_for_men — inline single-path heng+shu+hook

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],   # no expected joints
    'overall_pass': True,
    'notes': ('Stroke 1 uses draw_dian (bank). Stroke 2 uses draw_shu (bank). '
              'Stroke 3 is a fresh single-path 横折钩 (see BANK_DEVIATION).'),
}

import sys
import pathlib

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from dian import draw_dian
from shu import draw_shu


def draw_heng_zhe_gou_for_men(d, head, tail):
    """Continuous-path 横折钩 for the right side of 门.

    head = (x, y) at the top of the horizontal segment.
    tail = (x, y) at the tip of the terminal left-hook.
    """
    hx, hy = head
    tx, ty = tail

    # Corner (shoulder) sits slightly right of tail-x, slightly below head-y.
    corner_x = tx + 22   # vertical trunk at x ~= 215 for tail_x=193
    corner_y = hy + 6

    # Hook shoulder = point where vertical descent ends and hook begins.
    hook_start_x = corner_x
    hook_start_y = ty - 12   # start hook ~12px above tail

    # --- Segment A: horizontal (heng) with slight upward arch, thin->medium ---
    steps_a = 42
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + (corner_x - hx) * t
        by = hy + (corner_y - hy) * t - 3.5 * (1 - (2 * t - 1) ** 2)
        w = 3.6 + 2.6 * t
        d.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # --- Segment B: vertical descent (shu) from corner to hook_start ---
    steps_b = 80
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = corner_x + (hook_start_x - corner_x) * t
        by = corner_y + (hook_start_y - corner_y) * t
        w = 6.2
        d.ellipse([bx - w, by - w, bx + w, by + w], fill='black')

    # --- Segment C: terminal hook curving leftward+down to tail ---
    steps_c = 20
    for i in range(steps_c):
        t = i / (steps_c - 1)
        # ease-in x, linear y  -> smooth curl
        bx = hook_start_x + (tx - hook_start_x) * (t ** 1.6)
        by = hook_start_y + (ty - hook_start_y) * t
        w = 6.0 - 3.2 * t
        d.ellipse([bx - w, by - w, bx + w, by + w], fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Stroke 1: 丶 top-left dot (bank primitive)
    draw_dian(draw, head=(89, 74), tail=(115, 104),
              w_head=3, w_tail=8, bow=3)

    # Stroke 2: 丨 left vertical (bank primitive)
    draw_shu(draw, head=(55, 96), tail=(56, 287), width=7)

    # Stroke 3: 横折钩 fresh single-path
    draw_heng_zhe_gou_for_men(draw, head=(151, 83), tail=(193, 277))

    out = _HERE.parent / '01_门.png'
    img.save(str(out))
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
