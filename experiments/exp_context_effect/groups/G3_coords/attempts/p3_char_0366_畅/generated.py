# p3_char_0366_畅 (chàng) — G3 attempt
# Structure: 申 (left) + 昜 (right, simplified form).
#   Right side (昜): small stacked horizontals on top (曰 abbreviated)
#   + 一 divider + 勿-like envelope with two inner 撇 at the bottom.
#
# Compose fresh: shen_extend.py's coords are hard-wired to the center
# of a 300x300 canvas (no true rescale knob), so a scaled left-half 申
# is inlined here rather than transformed through the bank primitive.
# The right side (昜) has no direct bank entry; the 勿-lower is
# structurally identical to wu_neg.py so its recipe (envelope + 2
# variant_pie inner strokes) is applied inline at the right-lower
# region.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from _shared_helpers import variant_pie  # noqa: E402


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _cbez(p0, p1, p2, p3, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        b0 = (1 - u) ** 3
        b1 = 3 * (1 - u) ** 2 * u
        b2 = 3 * (1 - u) * u * u
        b3 = u ** 3
        x = b0 * p0[0] + b1 * p1[0] + b2 * p2[0] + b3 * p3[0]
        y = b0 * p0[1] + b1 * p1[1] + b2 * p2[1] + b3 * p3[1]
        pts.append((x, y))
    return pts


def _draw_pts(d, pts, widths):
    for i in range(len(pts) - 1):
        w = max(2, int(round(widths[i])))
        d.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=w)
        r = w / 2.0
        bx, by = pts[i + 1]
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_shen_left(d):
    """Compact 申 in left half. Box + middle heng + central protruding shu."""
    x_left = 40
    x_right = 130
    y_top = 100
    y_bot = 205
    y_mid = 152
    w = 6
    w_mid = 5
    w_shu = 7

    # Stroke 1: left 竖 of box
    d.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 2: 横折 (top + right side)
    d.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 3: middle 横
    d.line([(x_left + 2, y_mid), (x_right - 2, y_mid)],
           fill=(0, 0, 0), width=w_mid)
    # Stroke 4: bottom 横
    d.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)
    # Stroke 5: central 竖 (protrudes above/below)
    x_c = (x_left + x_right) // 2
    d.line([(x_c, 55), (x_c, 265)], fill=(0, 0, 0), width=w_shu)


def draw_yang_right(d):
    """Right side (simplified 昜): small 曰 stack on top merged into
    a 勿-like envelope + two inner 撇 below. No wide middle 一 —
    the 曰-lower-bar doubles as the divider."""
    # --- Top 曰: compact box, ~x=175..240, y=70..135, middle bar ~y=105 ---
    x_l, x_r = 178, 238
    y_t, y_m, y_b = 72, 105, 135
    d.line([(x_l, y_t), (x_r, y_t)], fill=(0, 0, 0), width=6)   # top heng
    d.line([(x_l, y_t), (x_l, y_b)], fill=(0, 0, 0), width=6)   # left shu
    d.line([(x_r, y_t), (x_r, y_b)], fill=(0, 0, 0), width=6)   # right shu
    d.line([(x_l + 2, y_m), (x_r - 2, y_m)],
           fill=(0, 0, 0), width=5)                              # middle bar
    d.line([(x_l, y_b), (x_r, y_b)], fill=(0, 0, 0), width=6)   # bottom heng

    # --- Bottom 勿-like: envelope + two inner 撇 (starts just below 曰) ---
    # Top short pie of the envelope (tiny top-left tick pointing down-left)
    pie_top = _qbez((180, 148), (172, 162), (168, 175), 20)
    _draw_pts(d, pie_top, [4 - 1.5 * (i / (len(pie_top) - 1))
                           for i in range(len(pie_top))])

    # Envelope: horizontal top → shoulder → shaft → hook
    env_top = _qbez((168, 162), (215, 160), (258, 158), 24)
    _draw_pts(d, env_top, [6] * len(env_top))
    shoulder = _cbez((258, 158), (270, 160), (272, 172), (270, 185), 18)
    _draw_pts(d, shoulder, [6] * len(shoulder))
    shaft = _cbez((270, 185), (263, 215), (250, 245), (230, 268), 40)
    _draw_pts(d, shaft, [6 - 1.5 * (i / (len(shaft) - 1))
                         for i in range(len(shaft))])
    hook = _qbez((230, 268), (218, 266), (207, 253), 15)
    _draw_pts(d, hook, [4 - 2 * (i / (len(hook) - 1))
                        for i in range(len(hook))])

    # Two inner long 撇 — MUCH bolder so they read.
    # variant_pie uses math coords (+y up, origin (150,150)).
    # Inner-left: PIL (190, 175) -> math (40, -25); PIL (170, 260) -> math (20, -110)
    variant_pie(d, head=(40, -25), tail=(20, -110),
                bow_perp=10.0, w_head=8.0, w_tail=3.0, n=48)
    # Inner-right: PIL (225, 175) -> math (75, -25); PIL (200, 260) -> math (50, -110)
    variant_pie(d, head=(75, -25), tail=(50, -110),
                bow_perp=10.0, w_head=8.0, w_tail=3.0, n=48)


def render(out_path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_shen_left(d)
    draw_yang_right(d)
    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_畅.png")
    render(out)
    print("wrote", out)
