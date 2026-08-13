# BANK_DEVIATION
# skipped: zi_char.py (used at default oy) — its 子 sits vertically-centered
#   on canvas; 学 needs 子 shoved down into the lower ~55% of canvas so the
#   top ⺍ + 冖 cover fit above it. zi_char's internal helper (draw_liao)
#   mixes pixel-oy and math-oy conventions, so applying a uniform vertical
#   shift breaks the composition. Inlined fresh 子 with hand-placed 横撇 +
#   弯钩 + 横 at the correct lower position.
# reason: bank 子 vertical range clashes with 学's three-tier layout; needs
#   deliberate lower placement.
# fresh_component: zi_variant_lower_for_学
#
# p3_char_0379_学 — 学 (xué, "study"), 8 strokes.
# Composition (top → bottom):
#   1. ⺍ (three small dot/pie strokes at top)      strokes 1–3
#   2. 冖 (cover: dot + heng-hook)                   strokes 4–5
#   3. 子 (child: 横撇 + 弯钩 + 横)                  strokes 6–8
# Bank uses:
#   - draw_mi_radical for 冖 (its default position sits at pixel y~118 —
#     ideal middle-band for 学).
# Fresh inline:
#   - Top ⺍ three strokes above the 冖 bar (bank has no ⺍ primitive).
#   - Bottom 子 pushed down into lower canvas (see BANK_DEVIATION above).
import os
import sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from mi_radical import draw_mi_radical  # noqa: E402

CANVAS = 300


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _tapered_line(draw, p0, p1, w0, w1, steps=20):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)
    r = max(1, w1 / 2)
    draw.ellipse([p1[0] - r, p1[1] - r, p1[0] + r, p1[1] + r], fill="black")


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=40):
    pts = _qbez(p0, p1, p2, steps)
    for i in range(len(pts) - 1):
        u = i / (len(pts) - 1)
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        draw.line([pts[i], pts[i + 1]], fill="black", width=w)
        r = w / 2
        draw.ellipse([pts[i + 1][0] - r, pts[i + 1][1] - r,
                      pts[i + 1][0] + r, pts[i + 1][1] + r], fill="black")


def draw_top_mie(draw):
    """⺍ — three small strokes above the 冖 cover.
    All three fan outward from a central top point (like 小's top pattern).
    """
    # Left short 撇: slants down-left more aggressively.
    _tapered_line(draw, (140, 45), (108, 88), w0=5, w1=2, steps=18)
    # Center short 撇: slight down-left slant.
    _tapered_line(draw, (158, 42), (150, 88), w0=5, w1=2, steps=18)
    # Right short 点/pie: slants down-right (heavy tail characteristic 点).
    _tapered_line(draw, (178, 48), (205, 88), w0=3, w1=7, steps=18)


def draw_zi_lower(draw):
    """子 pushed to lower ~55% of canvas."""
    # Stroke 1: 横撇 — short horizontal then diagonal down-left flick.
    # Horizontal segment top of 子.
    _tapered_line(draw, (85, 158), (215, 160), w0=4, w1=9, steps=24)
    # Diagonal flick down-left from right end.
    _tapered_line(draw, (215, 160), (180, 195), w0=9, w1=2, steps=18)

    # Stroke 2: 弯钩 — long curved descender with leftward hook.
    # Body curves gently: starts just below 横撇 top-right, arcs down/left.
    body = _qbez((198, 165), (215, 220), (170, 268), steps=60)
    for i in range(len(body) - 1):
        u = i / (len(body) - 1)
        if u < 0.55:
            w = 7 + (10 - 7) * (u / 0.55)
        else:
            w = 10 - (10 - 5) * ((u - 0.55) / 0.45)
        w_int = max(3, int(round(w)))
        draw.line([body[i], body[i + 1]], fill="black", width=w_int)
        r = w_int / 2
        draw.ellipse([body[i + 1][0] - r, body[i + 1][1] - r,
                      body[i + 1][0] + r, body[i + 1][1] + r], fill="black")
    # Hook flick up-left from body end.
    p_end = body[-1]
    _tapered_line(draw, p_end, (128, 258), w0=5, w1=2, steps=14)

    # Stroke 3: 横 — horizontal bar crossing the descender near middle.
    _tapered_line(draw, (55, 215), (255, 218), w0=5, w1=8, steps=30)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # Top: ⺍ (three little strokes).
    draw_top_mie(draw)

    # Middle: 冖 via bank primitive (default position puts bar at pixel y~118-122).
    draw_mi_radical(draw, ox=0, oy=0, scale=1.0)

    # Bottom: 子 (fresh inline, lower placement).
    draw_zi_lower(draw)

    out = os.path.join(_HERE, "01_学.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
