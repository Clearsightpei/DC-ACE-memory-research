"""里 (lǐ) — 8 strokes (decomposed): 日 box (4) + 土 (3) + bottom heng.

Tags: tag:character tag:8-strokes tag:turtle-renderer tag:composes(日,土)
Mastered: run_5 c25 (after c24 carry-over). visual=0.863, OCR='里' margin=1.00. Panel 3/3 YES.

The c24 attempt had the 土 portion missing its middle heng (panel 1/3 NO).
c25 fix: explicit middle heng of 土 at scale 0.22, offset slightly left of
shu center (ox=-35, oy=-100) to match GT.

Note: 8 strokes drawn because 横折 is split into top heng + right shu
(simpler positioning per GT measurement).

Reuse:
    from li import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_shu (t, ox=ox + -78 * scale, oy=oy + 17   * scale, scale=0.30 * scale)
    draw_heng(t, ox=ox + -2  * scale, oy=oy + 78   * scale, scale=0.52 * scale)
    draw_shu (t, ox=ox + 90  * scale, oy=oy + 17   * scale, scale=0.30 * scale)
    draw_heng(t, ox=ox + 5   * scale, oy=oy + 22   * scale, scale=0.43 * scale)
    draw_heng(t, ox=ox + 1   * scale, oy=oy + -32  * scale, scale=0.35 * scale)
    draw_shu (t, ox=ox + -2  * scale, oy=oy + -44  * scale, scale=0.64 * scale)
    draw_heng(t, ox=ox + -35 * scale, oy=oy + -100 * scale, scale=0.22 * scale)
    draw_heng(t, ox=ox + 10  * scale, oy=oy + -172 * scale, scale=0.84 * scale)
