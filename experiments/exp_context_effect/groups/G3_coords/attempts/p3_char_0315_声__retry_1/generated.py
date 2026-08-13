# BANK_DEVIATION
# skipped: shi_radical.py
# reason: at scale 0.85 the pie stopped at y=-100 (too high); its middle-heng
#         y=+10*s ended up too high vs GT. GT's 尸 body needs a lower/longer
#         pie sweep reaching near bottom edge, and its inner heng lower.
# fresh_component: sheng_body_for_声

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata says "drawer's proportions cramped the 尸 hook".
#   Fix: extend the pie sweep to full canvas height; widen shared bar;
#   drop the small inner heng lower so the 尸-body reads.
# Q2 (form_catalog): long pie in 尸-family — head weld top-left of body,
#   tail near bottom-left of canvas (y≈-140). Widths 10→1 taper.
# Q3 (helpers): none of kiss_apex/mirror_dian apply. Inline fresh
#   render with tuned pie tail and enlarged 尸-body per GT trajectory.

# TRAJECTORY DIFF
# GT: top short heng (~x∈[-30,+30], y≈+110), stub vertical down to y≈+80,
#     wide bar (x∈[-70,+90], y≈+65), inner right vertical (60→60, +65→-10),
#     inner bottom heng (x∈[-20,+60], y≈-10), long pie head at (-70,+65)
#     sweeping to (-105,-140).
# FAILED main: pie too short (ended y≈-100), 尸 body scaled 0.85 so
#     middle heng at y≈+15 too high; inner bottom heng absent visually;
#     top heng and stub visible but proportion of body cramped.
# FIX: inline fresh render (skip shi_radical); pie reaches y=-140;
#     inner heng at y=-10; wide bar at y=+65; keep top 士-stub small.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _p(x, y):
    return (150 + x, 150 - y)


def _line(t, x0, y0, x1, y1, w=7):
    ink = max(1, int(round(w)))
    t.line([_p(x0, y0), _p(x1, y1)], fill=(0, 0, 0), width=ink)
    r = ink / 2
    for (x, y) in ((x0, y0), (x1, y1)):
        px, py = _p(x, y)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def _tapered_bezier(t, x0, y0, mx, my, x1, y1, w_head=10.0, w_tail=1.0,
                    n_seg=60):
    prev = None
    for i in range(n_seg + 1):
        u = i / n_seg
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _p(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
        r = w / 2.0
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_sheng(t):
    """声 fresh render for retry_1."""
    # 1. Top short 横 (士 top).
    _line(t, -30, 108, 32, 108, w=6)
    # 2. Short vertical stub down to shared bar.
    _line(t, 2, 108, 2, 72, w=6)
    # 3. Wide shared 横 (士 bottom / 尸 top).
    _line(t, -72, 68, 92, 68, w=7)
    # 4. Inner right vertical descender (short, from bar down).
    _line(t, 60, 68, 60, -12, w=7)
    # 5. Inner bottom 横 (short bar closing the body-box).
    _line(t, -18, -12, 60, -12, w=6)
    # 6. Long 撇 — head welded at left-end of wide bar, sweeping down-left.
    _tapered_bezier(t, x0=-72, y0=68, mx=-95, my=-30,
                    x1=-108, y1=-142, w_head=10.0, w_tail=1.5)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_sheng(t)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_声.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
