"""末 (mò) — 5 strokes: long top heng + short middle heng + shu + pie + na.

Tags: tag:character tag:5-strokes tag:turtle-renderer tag:contrasts(本,未,木)
Mastered: run_5 c21 (after c18, c20 carry-overs). visual=0.818, OCR='末' margin=1.00. Panel 3/3 YES.

Defining feature vs 未: top heng LONGER than middle (scale 0.80 vs 0.45 — ~78% wider).
Defining feature vs 木: there IS a top heng above 木's heng.

c20 had top scale 0.62 vs mid 0.45 (only 38% wider — panel called it
indistinguishable from 木). c21 bumped top to 0.80 → unambiguous.

Reuse:
    from mo import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from na   import draw as draw_na


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + -3 * scale, oy=oy + 43  * scale, scale=0.80 * scale)
    draw_shu (t, ox=ox + -2 * scale, oy=oy + -53 * scale, scale=0.90 * scale)
    draw_heng(t, ox=ox + 0  * scale, oy=oy + -30 * scale, scale=0.45 * scale)
    s_pie = 0.40
    draw_pie(t,
        ox=ox + (-8 - 150 * s_pie) * scale,
        oy=oy + (-38 - 200 * s_pie) * scale,
        scale=s_pie * scale)
    s_na = 0.45
    draw_na(t,
        ox=ox + (8 - (-150) * s_na) * scale,
        oy=oy + (-38 - 200 * s_na) * scale,
        scale=s_na * scale)
