# BANK_DEVIATION
# replaced: heng_zhe_gou.py with local render (draw_wei_bottom_hook)
# reason: 韦's stroke 3 is a bottom heng that turns down-right then hooks back
#         left — closer to a 横折 with a small downward curl than the tight
#         heng_zhe_gou used in 力/月. Bank primitive's corner shape and curl
#         geometry don't match this radical's flatter, wider bottom hook.
# fresh_component: wei_bottom_hook_for_韦 — long horizontal, gentle descending
#         corner, short downward curl ending in a small back-left hook.
#
# Bank primitives used: draw_heng (s1, s2), draw_shu (s4).
# Bank primitive skipped-but-noted: shu.top_curl left OFF (composed shaft).

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # exactly 4 stroke primitives called
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # all three P joints implemented via long shu crossing hengs
    'overall_pass': True,
    'notes': 'BANK_DEVIATION for s3 (compound bottom hook). s1,s2 heng, s4 shu extending past canvas bottom.'
}

import sys
import pathlib

_BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu


def draw_wei_bottom_hook(draw, heng_head, corner, curl_tail, hook_tip):
    """Bottom stroke of 韦: long heng → corner → short descending curl → small
    back-left hook. Rendered as a chain of ellipses for calligraphic weld."""
    # Segment A: long horizontal (slight downward slope right-ward)
    steps_a = 70
    x0, y0 = heng_head
    x1, y1 = corner
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t
        w = 4.2 + 1.2 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
    # Corner node (小顿笔)
    cx, cy = corner
    draw.ellipse((cx - 6.0, cy - 5.5, cx + 6.0, cy + 5.5), fill='black')
    # Segment B: short descending curl (curves slightly leftward)
    steps_b = 40
    x2, y2 = curl_tail
    ctrl_x = cx - 4
    ctrl_y = (cy + y2) / 2
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t ** 2 * x2
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t ** 2 * y2
        w = 5.0 - 1.5 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
    # Segment C: small back-left hook flick tapering to point
    steps_c = 20
    hx, hy = hook_tip
    for i in range(steps_c):
        t = i / (steps_c - 1)
        bx = x2 + (hx - x2) * t
        by = y2 + (hy - y2) * t
        w = 3.8 * (1 - t) + 0.7
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: top heng, slight upward slant to the right ----
    # MMH: ML(0.82,0.216)=(82,122) -> MR(0.165,0.099)=(216,110)
    draw_heng(d, head=(82, 122), tail=(216, 110), width_head=9, width_tail=10)

    # ---- Stroke 2: middle heng, slight upward slant to the right ----
    # MMH: ML(0.841,0.664)=(84,166) -> MR(0.101,0.567)=(210,157)
    draw_heng(d, head=(84, 166), tail=(210, 157), width_head=9, width_tail=10)

    # ---- Stroke 3: bottom horizontal + turn + downward curl + back-left hook ----
    # MMH gives median endpoints only — the visible hook curl extends past the
    # MMH tail. Head at MMH BL(0.492,0.153)=(49,215); horizontal reaches past the
    # central shu; corner near (200,222) then curls down to (172,258) with a
    # small hook flick back-left to (152,254).
    draw_wei_bottom_hook(d,
                         heng_head=(50, 218),
                         corner=(200, 222),
                         curl_tail=(172, 260),
                         hook_tip=(150, 254))

    # ---- Stroke 4: long central shu from top to below the canvas ----
    # MMH: TC(0.356,0.58)=(136,58) -> BC(0.474,1.103)=(147,310)
    # Extends past y=300 (clipped by canvas). Passes through all three horizontals (P joints).
    draw_shu(d, head=(136, 58), tail=(147, 310), width=7, top_curl=False)

    out = pathlib.Path(__file__).parent / '01_韦.png'
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
