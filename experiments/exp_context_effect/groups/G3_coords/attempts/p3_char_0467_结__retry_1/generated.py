# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Errata says "same 纟 fix as 给 + bank shi_male + bank kou for 吉".
#   Main attempt did that but with size=18/22 hooks -> scribbled. Fix: use
#   size=15/18 hooks like 给 recipe (cleaner). Also nudge 提 slightly lower
#   so it separates from the middle hook.
# Q2 (form_catalog): Silk radical in LR-left slot: hooks compact (size ~15-18),
#   ink ~5-6; short 提 confined to left half so it does not cross into 吉.
# Q3 (helpers): None match — 纟 has no X-crossing/mirror-dot; per-stroke inline
#   is required because bank si_zi_pang has hand-baked pixel coords that
#   ignore ox/oy/scale for its 提 (would sweep across right column).
#
# BANK_DEVIATION
# skipped: si_zi_pang.py
# reason: bank 纟 uses baked-in pixel coords; its 提 sweeps -65..+60 native
#         and would run under 吉 on the right of 结.
# fresh_component: si_zi_pang_LR_left_v2 (smaller/cleaner hooks than main
#         attempt; short 提 confined to left column)
#
# TRAJECTORY DIFF
# Main attempt (verdict C):
#   - 纟 hooks size=18/22, ink=6/7 -> visually noisy/scribbled ("blob-like"
#     rather than two clean 撇折 loops). GT shows two distinct, small,
#     angular hooks stacked cleanly.
#   - Middle 提 endpoint x=-25 -> feels short-cropped; could extend slightly
#     to x=-15 for more balance while still staying left of 吉 column.
#   - Right side 吉 (shi_male + kou) matched the PASSing 佶 recipe -> keep.
# Fixes this attempt:
#   1. Shrink hooks to size=15/18, ink=5/6 (matches PASSing 纟-radical style).
#   2. Lower middle hook cy from +15 to +5 for tighter stacking.
#   3. 提 stretched to end x=-15 (still safely left of 吉 which starts near x=+15).
#   4. Right side (士+口) unchanged from PASSing 佶 recipe.

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi_male import draw_shi_male      # noqa: E402
from kou import draw_kou                # noqa: E402


CANVAS = 300


def _to_px(x, y):
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def _tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=40, head_ramp=0.1):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_px(bx, by)
        if u < head_ramp:
            w = w_head
        else:
            w = w_head + (w_tail - w_head) * ((u - head_ramp) / (1 - head_ramp))
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                         fill=(0, 0, 0))
        prev = pt


def _draw_pie_zhe_hook(draw, cx, cy, size, ink=5):
    # First stroke: short 撇 down-and-in to the apex (cx, cy)
    p0 = (cx + size * 0.55, cy + size * 1.15)
    p2 = (cx, cy)
    p1 = ((p0[0] + p2[0]) / 2 + size * 0.1,
          (p0[1] + p2[1]) / 2 - size * 0.1)
    _tapered_bezier(draw, p0, p1, p2,
                    w_head=ink, w_tail=max(2, ink - 2), n=30)
    # Second stroke: 折 out from apex to lower-right
    h0 = (cx, cy)
    h2 = (cx + size * 1.5, cy + size * 0.45)
    h1 = (h0[0] + size * 0.35, h0[1] + size * 0.10)
    _tapered_bezier(draw, h0, h1, h2,
                    w_head=ink + 1, w_tail=1.5, n=40, head_ramp=0.05)


def draw_si_zi_pang_LR_left_v2(draw):
    """Compact 纟 confined to left column (smaller hooks, short 提)."""
    # Upper hook — small, high
    _draw_pie_zhe_hook(draw, cx=-95, cy=+55, size=15, ink=5)
    # Middle hook — slightly larger, tighter stack
    _draw_pie_zhe_hook(draw, cx=-100, cy=+5, size=18, ink=6)
    # Bottom 提 — head at lower-left, tail rising to just past mid-left
    p0 = (-118, -55)
    p2 = (-15, -35)
    p1 = ((p0[0] + p2[0]) / 2 - 3, (p0[1] + p2[1]) / 2 - 5)
    _tapered_bezier(draw, p0, p1, p2,
                    w_head=12, w_tail=1.5, n=50, head_ramp=0.08)


def draw_jie_char(t, ox=0.0, oy=0.0, scale=1.0):
    """结 — fresh compact 纟 (left) + 吉 stacked (士 top + 口 bottom, right).

    Right-column recipe mirrors PASSed 佶 (ji_lucky).
    """
    draw_si_zi_pang_LR_left_v2(t)
    # Right 吉: 士 upper half, 口 lower half of right column.
    draw_shi_male(t, ox=ox + 45 * scale, oy=oy + 55 * scale,
                  scale=0.55 * scale)
    draw_kou(t, ox=ox + 45 * scale, oy=oy + (-55) * scale,
             scale=0.55 * scale)


def _render(out_png):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_jie_char(d, ox=0.0, oy=0.0, scale=1.0)
    img.save(out_png, "PNG")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_结.png")
    _render(out)
    print("Wrote", out)
