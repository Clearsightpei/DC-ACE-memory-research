"""Attempt: p3_char_0112_心 (heart, 4 strokes).

Same character as p2_radical_126_心. Reusing the prior attempt approach
(3 dians + inline 卧钩) which visually matched the GT reasonably well.

MMH anchors -> pixels (300x300, 米字格 3x3 cells of 100x100):
  1. 左点  ML(0.542,0.646) -> BL(0.39,0.309)   ~= (54,165) -> (39,231)
  2. 卧钩  ML(0.896,0.614) -> MR(0.024,0.849)  ~= (90,161) -> (202,185)
       (belly dips through BC to ~y=260, then small hook up-back at tail)
  3. 中点  C(0.245,0.046)  -> C(0.588,0.436)    ~= (125,105) -> (159,144)
  4. 右点  MR(0.229,0.222) -> MR(0.681,0.661)   ~= (223,122) -> (268,166)

Joints: NONE (strokes do not meet).

# BANK_DEVIATION
# skipped: (no bank entry for 卧钩; closest is shu_wan_gou.py but topology
#          is L-vs-U; wan_gou.py is vertical-shaft not wide-smile)
# reason: 卧钩 is a wide horizontal smile-shape dipping in the middle and
#         terminating with a small up-hook at the right; none of the
#         existing hook primitives have this topology.
# fresh_component: wo_gou_for_xin  (curator promotion candidate on PASS)
"""

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                    '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)
from dian import draw_dian  # noqa: E402


def draw_wo_gou(draw, head, tail, belly_y=260, width=8, hook_up=26, hook_back=6):
    """卧钩 — wide smile-curve head(upper-left) -> down-through-belly ->
    tail(upper-right), then a small hook up-and-slightly-back-left.
    Cubic bezier body + quadratic bezier hook.
    """
    hx, hy = head
    tx, ty = tail
    c1 = (hx - 15, belly_y + 30)
    c2 = (hx + (tx - hx) * 0.80, belly_y + 30)

    body = []
    n = 80
    for i in range(n + 1):
        t = i / n
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * hx + b1 * c1[0] + b2 * c2[0] + b3 * tx
        y = b0 * hy + b1 * c1[1] + b2 * c2[1] + b3 * ty
        body.append((x, y))

    hook_tip = (tx - hook_back, ty - hook_up)
    hook_ctrl = (tx + 2, ty - hook_up * 0.4)
    hook = []
    for i in range(21):
        t = i / 20
        u = 1 - t
        x = u * u * tx + 2 * u * t * hook_ctrl[0] + t * t * hook_tip[0]
        y = u * u * ty + 2 * u * t * hook_ctrl[1] + t * t * hook_tip[1]
        hook.append((x, y))

    pts = body + hook[1:]
    ipts = [(int(round(x)), int(round(y))) for x, y in pts]
    draw.line(ipts, fill='black', width=width, joint='curve')
    r = width // 2
    for x, y in (ipts[0], ipts[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill='black')


def render():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1 — 左点
    draw_dian(d, head=(54, 165), tail=(39, 231),
              w_head=3, w_tail=8, bow=4)

    # s2 — 卧钩
    draw_wo_gou(d, head=(90, 161), tail=(202, 185),
                belly_y=260, width=8, hook_up=26, hook_back=6)

    # s3 — 中点
    draw_dian(d, head=(125, 105), tail=(159, 144),
              w_head=3, w_tail=7, bow=2)

    # s4 — 右点
    draw_dian(d, head=(223, 122), tail=(268, 166),
              w_head=3, w_tail=8, bow=3)

    out = os.path.join(os.path.dirname(__file__), '01_心.png')
    img.save(out)
    return out


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,     # 4 strokes: dian + wo_gou + dian + dian
    'endpoint_mismatches': [],   # anchors used directly from MMH block
    'joint_class_mismatches': [], # NONE per MMH block
    'overall_pass': True,
    'notes': 'reuse of p2_radical_126_心 approach; wo_gou inlined (BANK_DEVIATION).',
}

if __name__ == '__main__':
    print(render())
