# BANK_DEVIATION
# skipped: heng_zhe_gou.py for stroke 2
# reason: 书 stroke 2 is a long horizontal that dips down then hooks up-and-back
#   (approx 横折折钩 with a wide belly); the bank heng_zhe_gou is oriented for
#   short-heng + long-shu (力/月 family), which does not fit this cursive body.
# fresh_component: shu_book_body — long belly-heng + right-turn dip + hook-up

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 4 strokes drawn (heng_zhe, cursive body, shu, dian)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # s1/s3, s2/s3 welded via overlapping paths; s1/s2 N gap present
    'overall_pass': True,
    'notes': '书 4-stroke: heng_zhe_short (s1), inlined body_hook (s2, BANK_DEV), draw_shu long (s3), draw_dian (s4). s3 vertical pierces s1 corner + crosses s2 near lower center.',
}

import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / 'G5_code_bank_mmh' / 'success_bank' / 'code'))

from PIL import Image, ImageDraw
from heng_zhe_short import draw_heng_zhe_short
from shu import draw_shu
from dian import draw_dian


def draw_shu_book_body(d, head, tail):
    """Long heng that dips down mid-way then turns and hooks upward.

    head : left endpoint of the top horizontal (start of writing)
    tail : upward hook tip on the right side (end)
    Path: head -> right along y=head.y with gentle belly-down -> corner
          -> descend/curve right -> hook up to tail.
    """
    hx, hy = head
    tx, ty = tail

    # anchor waypoints
    right_x = 250          # right edge of the belly-heng
    belly_y = hy + 6       # gentle drop along the horizontal
    corner_x = right_x
    corner_y = hy + 4
    dip_x = 235            # lowest point of the descending curve
    dip_y = 285

    # --- Segment A: long horizontal with subtle belly ---
    steps_a = 90
    prev = None
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = hx + (right_x - hx) * t
        by = hy + (corner_y - hy) * t + 3.0 * (1 - (2 * t - 1) ** 2)
        w = 3.5 + 2.5 * t
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
        prev = (bx, by)

    # --- Corner emphasis ---
    d.ellipse((corner_x - 6.5, corner_y - 5.5, corner_x + 6.5, corner_y + 5.5), fill='black')

    # --- Segment B: descending curve down + slight left dip ---
    steps_b = 70
    for i in range(steps_b):
        t = i / (steps_b - 1)
        # quadratic bezier from corner -> dip
        cx_ctrl = corner_x + 3
        cy_ctrl = (corner_y + dip_y) / 2
        bx = (1 - t) ** 2 * corner_x + 2 * (1 - t) * t * cx_ctrl + t ** 2 * dip_x
        by = (1 - t) ** 2 * corner_y + 2 * (1 - t) * t * cy_ctrl + t ** 2 * dip_y
        w = 5.5 - 2.0 * t
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')

    # --- Segment C: hook up-and-back-left to tail ---
    steps_c = 30
    for i in range(steps_c):
        t = i / (steps_c - 1)
        # bezier from dip -> tail with control pulling upper-right first
        cx_ctrl = dip_x + 6
        cy_ctrl = dip_y - 10
        bx = (1 - t) ** 2 * dip_x + 2 * (1 - t) * t * cx_ctrl + t ** 2 * tx
        by = (1 - t) ** 2 * dip_y + 2 * (1 - t) * t * cy_ctrl + t ** 2 * ty
        w = 4.0 * (1 - t) + 1.2
        d.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # Stroke 1: 横折 small at top-left. Head (89,136) tail (186,176).
    draw_heng_zhe_short(d, head=(89, 136), tail=(186, 176), corner_offset=(0, 2))

    # Stroke 2: cursive body (fresh, BANK_DEVIATION). Head (48,197) tail (188,251).
    draw_shu_book_body(d, head=(48, 197), tail=(188, 251))

    # Stroke 3: 竖 long vertical spine. Head (136,66) tail (145,313).
    draw_shu(d, head=(136, 66), tail=(145, 300), width=7)

    # Stroke 4: 点 dot top-right. Head (211,84) tail (239,111).
    draw_dian(d, head=(211, 84), tail=(239, 111), w_head=3, w_tail=8, bow=3)

    out = pathlib.Path(__file__).parent / '01_书.png'
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    main()
