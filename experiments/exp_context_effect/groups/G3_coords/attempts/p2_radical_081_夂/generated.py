# p2_radical_081_夂 — 3 strokes (short 撇 top + 横撇 + 捺 crossing).
# G3 coord format. 300x300, math coords (center origin, +y up).
#
# Reading of GT: a short 撇 sits near the upper-center, then below it a 横撇
# (short heng that turns and drops down-left as a long pie) and a 捺 sweeping
# down-right — the pie and na cross near the middle-upper region, forming an
# X-like body similar to 又 but with a small pie added on top.
#
# TR8 inline-fresh check: heng_pie primitive's heng is too long+flat for the
# tight top of 夂, and its pie tail direction is fine but scale would need
# extreme values. Better to inline the strokes as tapered beziers/lines with
# per-stroke endpoints picked from the GT.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_bezier(t, p0, ctrl, p1, w0, w1, n=48):
    """Draw a tapered quadratic-bezier line from p0 to p1 (math coords)."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        px, py = _to_pixel(bx, by)
        w = w0 + (w1 - w0) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _tapered_line(t, p0, p1, w0, w1, n=32):
    """Straight tapered line from p0 to p1 (math coords)."""
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        px, py = _to_pixel(x, y)
        w = w0 + (w1 - w0) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_zhi(t, ox=0.0, oy=0.0, scale=1.0):
    """夂 = short pie top + 横撇 (heng+long pie) + 捺 crossing through pie."""

    # Stroke 1: short 撇 at top. Sits at upper-mid-left of the body. Thick
    # head upper-right, tapers to needle at lower-left. Small — spans ~30 px.
    s1_head = (ox + -8 * scale,  oy + 80 * scale)
    s1_ctrl = (ox + -18 * scale, oy + 65 * scale)
    s1_tail = (ox + -28 * scale, oy + 48 * scale)
    _tapered_bezier(t, s1_head, s1_ctrl, s1_tail, w0=7 * scale, w1=1, n=30)

    # Stroke 2: 横撇 — a short heng at the top of the body, then a hard turn
    # and a long 撇 down-left to the lower-left region.
    # Heng segment: from (-35, +35) to (+35, +40) — slight upward rise.
    heng_start = (ox + -35 * scale, oy + 35 * scale)
    heng_end   = (ox + 35 * scale,  oy + 40 * scale)
    _tapered_line(t, heng_start, heng_end, w0=6 * scale, w1=7 * scale, n=24)

    # 顿笔 blob at the turn
    cx, cy = _to_pixel(ox + 36 * scale, oy + 38 * scale)
    r = max(3, int(6 * scale))
    t.ellipse([cx - r, cy - r, cx + r + 1, cy + r + 1], fill=(0, 0, 0))

    # Pie segment of stroke 2: sweeps from the corner down-left through
    # canvas center to the lower-left tail.
    pie_head = (ox + 36 * scale,  oy + 34 * scale)
    pie_ctrl = (ox + -5 * scale,  oy + -10 * scale)  # bows leftward
    pie_tail = (ox + -75 * scale, oy + -75 * scale)
    _tapered_bezier(t, pie_head, pie_ctrl, pie_tail, w0=9 * scale, w1=1, n=48)

    # Stroke 3: 捺 — starts thin from the upper area (near the pie shaft,
    # somewhat below the heng turn), swells in the belly, tapers to a longer
    # foot at lower-right. Its head crosses the pie roughly at (-5, +25).
    na_head = (ox + -8 * scale,  oy + 25 * scale)
    na_tail = (ox + 95 * scale,  oy + -70 * scale)
    na_ctrl = (
        (na_head[0] + na_tail[0]) / 2.0 + 6 * scale,
        (na_head[1] + na_tail[1]) / 2.0 - 8 * scale,
    )
    # Use existing na width profile: thin -> belly -> tapered foot.
    n_segments = 56
    w_head = max(1, 2.0 * scale)
    w_belly = max(1, 13.0 * scale)
    w_tail = max(1, 2.0 * scale)
    prev = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * na_head[0] + 2 * (1 - u) * u * na_ctrl[0] + u ** 2 * na_tail[0]
        by = (1 - u) ** 2 * na_head[1] + 2 * (1 - u) * u * na_ctrl[1] + u ** 2 * na_tail[1]
        px, py = _to_pixel(bx, by)
        t_belly = 0.7
        if u <= t_belly:
            w = w_head + (w_belly - w_head) * (u / t_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - t_belly) / (1 - t_belly))
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_zhi(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_夂.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
