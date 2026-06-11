"""未 (wèi) — short top heng + longer middle heng + shu + pie + na.

Tags: tag:character tag:5-strokes tag:turtle-renderer tag:contrasts(末)
Mastered: run_5 c20 (after c18 carry-over). visual=0.828, OCR='未' margin=1.00. Panel 3/3 YES.

Defining feature vs 末: top heng SHORTER than middle heng (scale 0.36 vs 0.60).
Defining feature vs 木: there IS a top heng (above 木's heng).

This is a COMPOSITION character — not built by calling draw_mu()
(that produced the c18 failure because draw_mu's coords kept 木 at its
default position, leaving the top heng to overlap). Built from primitives
with explicit positioning per MMH GT measurement.

Reuse:
    from wei import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from na   import draw as draw_na


def draw(t, ox=0, oy=0, scale=1.0):
    # 1. Top heng (SHORT)
    draw_heng(t, ox=ox + -2 * scale, oy=oy + 47  * scale, scale=0.36 * scale)
    # 2. Shu (full spine)
    draw_shu (t, ox=ox + -3 * scale, oy=oy + -52 * scale, scale=0.90 * scale)
    # 3. Middle heng (LONG — longer than top)
    draw_heng(t, ox=ox + 22 * scale, oy=oy + -30 * scale, scale=0.60 * scale)
    # 4. Pie (from middle-heng crossing)
    s_pie = 0.40
    draw_pie(t,
        ox=ox + (-12 - 150 * s_pie) * scale,
        oy=oy + (-36 - 200 * s_pie) * scale,
        scale=s_pie * scale)
    # 5. Na
    s_na = 0.45
    draw_na(t,
        ox=ox + (4 - (-150) * s_na) * scale,
        oy=oy + (-33 - 200 * s_na) * scale,
        scale=s_na * scale)
