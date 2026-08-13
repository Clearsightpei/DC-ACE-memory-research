# p3_char_0273_次 — 次 (cì): L-R char, 冫 (left) + 欠 (right)
# G3 attempt: use draw_bing for 冫 at reduced scale; inline 欠 (4 strokes:
# 撇, 横钩, 撇, 捺) with thin-to-moderate widths matching GT.
#
# GT observation: 冫 sits in left band (small, upper-mid); 欠 fills right
# band. 欠's top 撇 is short slanting down-left; short 横 next to it with
# tiny down-hook; long 撇 sweeps from upper-center down to lower-left;
# 捺 sweeps from mid-upper-center down to lower-right (crossing/kissing
# the long 撇 near its start). Lines are moderately thin (uniform), not
# heavy calligraphic.

import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from bing import draw_bing  # noqa: E402


def _px(cx_ox, cx_oy):
    return 150 + cx_ox, 150 - cx_oy


def _tapered_bezier(t, p0, p1, p2, w_head, w_tail, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w_head * (1 - u) + w_tail * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def _tapered_line(t, p0, p1, w_head, w_tail, n=30):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head * (1 - u) + w_tail * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)


def draw_qian_inline(t, ox=60.0, oy=0.0, scale=1.0):
    """欠 inline: 4 strokes (short 撇, 横钩, long 撇, 捺). Origin (ox,oy)
    is the character-center of 欠; drawn in math-coords then converted."""
    s = scale

    # Stroke 1: short 撇 at top. Head upper-right, sweeps down-left.
    p0 = _px(ox + 5 * s, oy + 90 * s)
    p1 = _px(ox + -10 * s, oy + 75 * s)
    p2 = _px(ox + -25 * s, oy + 55 * s)
    _tapered_bezier(t, p0, p1, p2, w_head=3, w_tail=6, n=30)

    # Stroke 2: 横 with small down-hook (横钩). Right of stroke 1.
    heng_left = _px(ox + -5 * s, oy + 60 * s)
    heng_right = _px(ox + 60 * s, oy + 62 * s)
    _tapered_line(t, heng_left, heng_right, w_head=4, w_tail=5, n=20)
    # small hook down
    hook_end = _px(ox + 55 * s, oy + 45 * s)
    _tapered_line(t, heng_right, hook_end, w_head=6, w_tail=2, n=10)

    # Stroke 3: long 撇, from upper (near heng midpoint) down to lower-left.
    p0 = _px(ox + 25 * s, oy + 55 * s)
    p1 = _px(ox + 0 * s, oy + -20 * s)
    p2 = _px(ox + -55 * s, oy + -95 * s)
    _tapered_bezier(t, p0, p1, p2, w_head=4, w_tail=3, n=50)

    # Stroke 4: 捺, from upper-mid down-right to lower-right.
    # Starts near where the long 撇 begins (kiss around upper area).
    p0 = _px(ox + 15 * s, oy + 30 * s)
    p1 = _px(ox + 30 * s, oy + -20 * s)
    p2 = _px(ox + 65 * s, oy + -90 * s)
    _tapered_bezier(t, p0, p1, p2, w_head=3, w_tail=10, n=50)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Left: 冫 — shift left, small scale
    draw_bing(t, ox=-80.0, oy=-10.0, scale=0.55)

    # Right: 欠 inline
    draw_qian_inline(t, ox=55.0, oy=0.0, scale=1.0)

    out = os.path.join(_HERE, "01_次.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
