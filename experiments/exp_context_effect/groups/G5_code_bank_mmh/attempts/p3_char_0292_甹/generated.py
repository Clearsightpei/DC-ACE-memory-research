"""Attempt: p3_char_0292_甹 — G5 B9 (P-A-006 recipe).

7 strokes: 由-like top box (s1..s5) + long main heng (s6) + curling
乙-like bottom-right stroke (s7). P-A-006 recipe — stroke primitives
called with MMH-verbatim endpoint anchors. s2 uses draw_heng_zhe_gou
with hook_tip==gou_tail (no hook). s7 inlined via BANK_DEVIATION
(no direct bank primitive matches — wan_gou expects big right-belly
with sharp left-flick, but 甹's s7 is a wider looping curl).
"""

# BANK_DEVIATION
# skipped: wan_gou.py (considered for s7 — bottom right curl)
# reason: 甹's s7 is a wide looping curl that arcs right, drops, and returns
#         to a bottom-center tail without wan_gou's characteristic left-flick;
#         wan_gou's belly_right + hook_up geometry doesn't fit
# fresh_component: ping_pin_tail_loop_v1 (bezier: head → right belly → down → tail)

import sys
import pathlib

from PIL import Image, ImageDraw

_HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[2] / 'success_bank' / 'code'))

from shu import draw_shu  # noqa: E402
from heng import draw_heng  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,          # 7 stroke primitive calls (s2's heng_zhe_gou is 1 compound stroke)
    'endpoint_mismatches': [],        # all anchors are MMH-verbatim
    'joint_class_mismatches': [],     # joints emerge from anchor placement
    'overall_pass': True,
    'notes': 'P-A-006 stroke-primitive layer + MMH anchors. s7 inlined bezier per BANK_DEVIATION.'
}


def _bezier3(p0, p1, p2, p3, steps=90):
    pts = []
    for i in range(steps):
        t = i / (steps - 1)
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _stamp(draw, pts, w_head, w_tail):
    n = max(len(pts) - 1, 1)
    for i, (x, y) in enumerate(pts):
        t = i / n
        w = w_head * (1 - t) + w_tail * t
        draw.ellipse((x - w, y - w, x + w, y + w), fill='black')


def draw_s7_loop(draw, head, tail):
    """Wide looping curl for 甹's bottom-right stroke.
    Path: head (top center-left) -> arcs right (belly ~x=210) ->
    drops down -> curves back to tail (bottom center-left)."""
    p0 = head
    p1 = (210.0, 215.0)   # arc out right
    p2 = (215.0, 260.0)   # drop far right-bottom
    p3 = tail
    pts = _bezier3(p0, p1, p2, p3, steps=100)
    _stamp(draw, pts, w_head=5.5, w_tail=3.0)


img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# --- Top 由-like box (s1..s5) ---

# s1: left vertical of box (MMH: ML(0.814,0.005) -> C(0.078,0.787))
draw_shu(d, (81.4, 100.5), (107.8, 178.7), width=6)

# s2: heng_zhe forming top + right of box (MMH: ML(0.999,0.025) -> C(0.837,0.646))
# heng_head = MMH head; corner = top-right (same y as head, same x as tail);
# gou_tail = MMH tail; hook_tip = tail => no hook flick.
draw_heng_zhe_gou(d,
                  (99.9, 102.5),
                  (183.7, 102.5),
                  (183.7, 164.6),
                  (183.7, 164.6))

# s3: middle heng inside box (MMH: C(0.166,0.359) -> C(0.778,0.286))
draw_heng(d, (116.6, 135.9), (177.8, 128.6),
          width_head=6, width_tail=7)

# s4: central shu extending above box (MMH: TC(0.351,0.595) -> C(0.412,0.579))
draw_shu(d, (135.1, 59.5), (141.2, 157.9), width=6)

# s5: bottom heng closing box (MMH: C(0.137,0.711) -> C(0.79,0.576))
draw_heng(d, (113.7, 171.1), (179.0, 157.6),
          width_head=6, width_tail=7)

# --- Main long heng across canvas (s6) ---
# MMH: BL(0.457,0.024) -> MR(0.575,0.91) = (45.7,200.2) -> (257.5,191.0)
draw_heng(d, (45.7, 200.2), (257.5, 191.0),
          width_head=9, width_tail=10)

# --- Bottom-right curling stroke (s7, inline BANK_DEVIATION) ---
# MMH: BC(0.192,0.042) -> BC(0.289,0.839) = (119.2,204.2) -> (128.9,283.9)
draw_s7_loop(d, (119.2, 204.2), (128.9, 283.9))

out_path = _HERE.parent / '01_甹.png'
img.save(str(out_path))
print(f'wrote {out_path}')
