# p3_char_0401_取 — 取 (qǔ, "take"), L-R compose: 耳 (left, 6 strokes) + 又 (right, 2 strokes).
# 耳 is not in the bank — inlined fresh with thin uniform strokes to match MMH GT style.
# 又 uses the bank draw_you at scale 0.70, placed right.
#
# BANK_DEVIATION
# skipped: none for 又 (using bank); 耳 has no bank entry, inlined fresh
# reason: 耳 radical unavailable in success_bank; inlined 6-stroke box structure
# fresh_component: er_ear_radical_inline (6 strokes: top heng, L shu, 2 interior heng, R shu extending down, bottom heng)

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from you import draw_you  # noqa: E402

CANVAS = 300


def _px(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def _line(t, p0, p1, width=5):
    t.line([_px(*p0), _px(*p1)], fill=(0, 0, 0), width=width)


def draw_er_ear(t):
    """Inline 耳 radical (ear), 6 strokes, thin uniform lines to match MMH GT."""
    W = 5
    # 1. Top short heng — slight rise
    _line(t, (-115, 60), (-30, 65), width=W)
    # 2. Left shu (vertical) — from top-left corner down
    _line(t, (-105, 55), (-105, -75), width=W)
    # 3. Upper interior heng
    _line(t, (-100, 20), (-40, 20), width=W)
    # 4. Lower interior heng
    _line(t, (-100, -18), (-40, -18), width=W)
    # 5. Right shu — extends below the box baseline (characteristic of 耳)
    _line(t, (-35, 60), (-35, -95), width=W)
    # 6. Bottom heng/提 — extends left past the left shu, slight downward tilt
    _line(t, (-125, -80), (-32, -83), width=W)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # 耳 on the LEFT
    draw_er_ear(t)

    # 又 on the RIGHT — bank primitive, scale 0.70, placed right
    # heng_pie unit at scale 0.70 spans ~-56..+45; ox=+55 → spans -1..+100
    draw_you(t, ox=+55, oy=-15, scale=0.70)

    return img


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_取.png")
    render().save(out)
    print(f"wrote {out}")
