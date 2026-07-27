# p3_char_0047_也 (yě) — 3 strokes: 横折钩 (left) + 竖 (middle) + 竖弯钩 (right envelope).
# Draw fresh with PIL. Uses bank primitive shu_wan_gou as the enveloping right stroke;
# inlines the left 横折钩 and middle 竖 with concrete coords to fit 也's proportions.

import os
import sys
from PIL import Image, ImageDraw

# Make the shared success_bank/code importable to reuse shu_wan_gou primitive.
_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu_wan_gou import draw_shu_wan_gou  # noqa: E402

CANVAS = 300


def _px(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered(t, p0, p1, w0, w1, steps=24):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        t.line([_px(xa, ya), _px(xb, yb)], fill=(0, 0, 0), width=w)


def draw_ye(t, ox=0, oy=0, scale=1.0):
    # 也 layout (300x300 canvas, math-coords centred):
    #   - Middle 竖 is the TOP-most element (peeks up highest).
    #   - Left 横折钩 has a slightly-slanted top-heng going up-right, corners at
    #     mid-upper, then long down, with a small up-left hook near bottom.
    #   - Right 竖弯钩 envelops: its shaft descends from mid-upper-right through
    #     the character, curves LEFT-ward under the base, and its horizontal tail
    #     sweeps back to the right edge with an upward hook.
    # Actually the correct 竖弯钩 shape: shaft goes DOWN, curves RIGHT, tail
    # extends rightward, hooks UP. But in 也 the "envelope" effect is because
    # the bottom-tail extends LEFT (across the whole char base) — this is 竖弯
    # with the tail direction driven by needing to close under 横折钩. The
    # standard form is still "shaft-down, curve-right-at-base, hook-up-right".

    # Stroke 1: 横折钩 — top-left. Short heng heading up-right (rising to corner),
    # then vertical down about 100 px, tiny hook up-left at the base.
    p_h_start = (ox + -105 * scale, oy + 55 * scale)   # left tip (lower)
    p_corner  = (ox + -50 * scale,  oy + 72 * scale)   # top-right of L (higher)
    p_v_end   = (ox + -50 * scale,  oy + -35 * scale)  # bottom of vertical

    _tapered(t, p_h_start, p_corner, 9 * scale, 12 * scale, steps=20)
    cx, cy = _px(*p_corner)
    r = int(7 * scale)
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    _tapered(t, p_corner, p_v_end, 12 * scale, 11 * scale, steps=24)
    # small up-left hook at base of the L
    h_base = p_v_end
    h_tip  = (p_v_end[0] - 16 * scale, p_v_end[1] + 16 * scale)
    _tapered(t, h_base, h_tip, 11 * scale, 2 * scale, steps=14)

    # Stroke 2: 竖 — the middle vertical. Peeks up the highest (top ~ oy+95),
    # descends to about the middle-lower zone (oy=-10). Sits above the envelope.
    v_top = (ox + 0 * scale,  oy + 95 * scale)
    v_bot = (ox + 0 * scale,  oy + -10 * scale)
    _tapered(t, v_top, v_bot, 11 * scale, 12 * scale, steps=22)

    # Stroke 3: 竖弯钩 — the enveloping right stroke.
    # Bank canonical: shaft (ox, oy+70) -> (ox, oy-30), arc r=40 to
    # (ox+40, oy-70), tail (ox+40..+80, oy-70), hook up to (+75, -48).
    # For 也 we want:
    #   shaft top around ( +45, +75 )  and descending long
    #   arc bottom around ( +45..+85, -70 ), tail extending to about +125
    # So we scale up modestly (scale ~ 1.15) and offset the anchor so the
    # shaft-x lands near +45 (i.e. ox_arg = +45 in the primitive's frame,
    # which means we pass ox = ox + 45, oy = oy + 5).
    draw_shu_wan_gou(t, ox=ox + 45 * scale, oy=oy + 5 * scale, scale=1.15 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_ye(d)
    out = os.path.join(os.path.dirname(__file__), "01_也.png")
    img.save(out)
    print(f"wrote {out}")
