"""五 (wǔ) — top heng + left shu + middle heng + heng_zhe + bottom heng.

Tags: tag:character tag:5-strokes tag:turtle-renderer tag:uses-heng_zhe
Mastered: run_5 c20 (after c19 carry-over). visual=0.862, OCR='五' margin=0.99. Panel 3/3 YES.

c19's failure: over-complex 5-call decomposition that OCR'd as 左. c20 fix:
clean 5-stroke MMH order with heng_zhe as the right-side closure.

Reuse:
    from wu import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from heng_zhe import draw as draw_hz


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + 9   * scale, oy=oy + 75   * scale, scale=0.46 * scale)
    draw_shu (t, ox=ox + -34 * scale, oy=oy + -40  * scale, scale=0.50 * scale)
    draw_heng(t, ox=ox + -17 * scale, oy=oy + -36  * scale, scale=0.39 * scale)
    draw_hz  (t, ox=ox + 15  * scale, oy=oy + -80  * scale, scale=0.50 * scale)
    draw_heng(t, ox=ox + 3   * scale, oy=oy + -153 * scale, scale=0.91 * scale)
