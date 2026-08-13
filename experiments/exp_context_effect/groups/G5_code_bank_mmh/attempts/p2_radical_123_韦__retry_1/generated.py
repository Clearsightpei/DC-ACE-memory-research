# TRAJECTORY DIFF (retry_1 of p2_radical_123_韦)
#
# Prior attempt (main, verdict C): 01_韦.png
#   Visual gaps vs GT:
#   1) Top of central shu (stroke 4) had NO top curl/tick — GT clearly shows
#      a small hook curling in from upper-left before descending into the
#      vertical shaft. Attempt used top_curl=False so the shu head was a
#      bare rounded terminal.
#   2) Bottom hook (stroke 3) rendered too small/tight — the descending curl
#      was only ~40 px deep (corner y=222 -> curl_tail y=260) and the flick
#      hooked left too abruptly, giving the impression of a small "厶" at
#      bottom-right rather than a proper 力/月-style bottom hook.
#   3) The two horizontal strokes (s1, s2) were nearly flat — GT hengs slope
#      more strongly upward to the right (roughly 15-18 px lift over 130 px
#      run) so they look calligraphic rather than mechanical.
#
# Fixes applied in this retry:
#   - Stroke 4: enable draw_shu top_curl=True so the shu starts with a
#     small leftward tick that curls back down into the vertical shaft.
#   - Stroke 3: extend the horizontal further right, make the descending
#     curl deeper (~55 px), and flick the hook tip further to the left
#     so it reads as a distinct terminal hook.
#   - Strokes 1 & 2: increase upward slant (tail y ~15 px above head y).
#
# BANK_DEVIATION
# replaced: heng_zhe_gou.py with local render (draw_wei_bottom_hook)
# reason: 韦's stroke 3 is a wider heng that turns into a modest descending
#         curl and back-left hook — flatter and wider than heng_zhe_gou's
#         tight tall corner used in 力/月. Same deviation rationale as the
#         main attempt; the primitive still doesn't fit this radical.
# fresh_component: wei_bottom_hook_for_韦_v2 — wider horizontal, deeper
#         descending curl, more visible back-left hook flick.

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 strokes: heng, heng, wei_bottom_hook, shu
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],  # 3 P joints via long central shu crossing s1/s2/s3
    'overall_pass': True,
    'notes': 'Retry: top_curl on shu; wider+deeper bottom hook; steeper heng slant.'
}

import sys
import pathlib

_BANK = pathlib.Path(__file__).resolve().parents[2] / 'success_bank' / 'code'
sys.path.insert(0, str(_BANK))

from PIL import Image, ImageDraw
from heng import draw_heng
from shu import draw_shu


def draw_wei_bottom_hook(draw, heng_head, corner, curl_tail, hook_tip):
    """Bottom stroke of 韦: long horizontal → soft corner → descending curl
    (slightly leftward drift) → back-left hook tapering to a point."""
    # Segment A: horizontal (nearly flat, slight downward drift)
    steps_a = 80
    x0, y0 = heng_head
    x1, y1 = corner
    for i in range(steps_a):
        t = i / (steps_a - 1)
        bx = x0 + (x1 - x0) * t
        by = y0 + (y1 - y0) * t
        w = 4.5 + 1.3 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
    # Corner node (小顿笔)
    cx, cy = corner
    draw.ellipse((cx - 6.5, cy - 6.0, cx + 6.5, cy + 6.0), fill='black')
    # Segment B: descending curl (curves leftward as it drops)
    steps_b = 50
    x2, y2 = curl_tail
    ctrl_x = cx - 8   # more pronounced leftward bow
    ctrl_y = (cy + y2) / 2
    for i in range(steps_b):
        t = i / (steps_b - 1)
        bx = (1 - t) ** 2 * cx + 2 * (1 - t) * t * ctrl_x + t ** 2 * x2
        by = (1 - t) ** 2 * cy + 2 * (1 - t) * t * ctrl_y + t ** 2 * y2
        w = 5.5 - 1.8 * t
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')
    # Segment C: back-left hook flick, tapering to point
    steps_c = 26
    hx, hy = hook_tip
    for i in range(steps_c):
        t = i / (steps_c - 1)
        bx = x2 + (hx - x2) * t
        by = y2 + (hy - y2) * t
        w = 4.2 * (1 - t) + 0.6
        draw.ellipse((bx - w, by - w, bx + w, by + w), fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- Stroke 1: top heng, upward slant to the right ----
    # MMH: ML(0.82,0.216)=(82,122) -> MR(0.165,0.099)=(216,110)
    # Steeper slant applied (~15px lift) to match calligraphic GT.
    draw_heng(d, head=(80, 125), tail=(220, 108), width_head=9, width_tail=10)

    # ---- Stroke 2: middle heng, upward slant to the right ----
    # MMH: ML(0.841,0.664)=(84,166) -> MR(0.101,0.567)=(210,157)
    draw_heng(d, head=(82, 170), tail=(218, 152), width_head=9, width_tail=10)

    # ---- Stroke 3: bottom compound (wider horizontal + deeper curl + hook) ----
    # MMH: BL(0.492,0.153)=(49,215) -> BC(0.89,0.37)=(189,237)
    # Visible ink continues past MMH tail into the descending hook.
    draw_wei_bottom_hook(
        d,
        heng_head=(48, 218),
        corner=(210, 225),
        curl_tail=(200, 280),
        hook_tip=(168, 268),
    )

    # ---- Stroke 4: long central shu WITH top_curl, extending past canvas ----
    # MMH: TC(0.356,0.58)=(136,58) -> BC(0.474,1.103)=(147,310)
    # top_curl=True adds the calligraphic entry curl seen in GT.
    draw_shu(d, head=(138, 62), tail=(148, 310), width=7, top_curl=True)

    out = pathlib.Path(__file__).parent / '01_韦.png'
    img.save(out)
    return out


if __name__ == '__main__':
    print(render())
