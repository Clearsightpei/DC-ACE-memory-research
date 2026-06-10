"""木 (mù) — heng + shu (through heng midpoint) + 撇 + 短捺.

Tags: tag:character tag:4-strokes tag:heng+shu+pie+na tag:turtle-renderer
Mastered: run_5 c14. visual=0.853, OCR='木' margin=1.00. Panel 3/3 YES.

The first run_5 character with mid-sized 撇 AND 捺 to clear visual > 0.8.
Key: pie scale 0.45 and na scale 0.45 keep the brushwork pixel surplus
small enough relative to the central heng+shu mass that visual stays
above the gate. Larger diagonals (scale 0.55+) fail visual (see 大/不 c14).

Reuse:
    from mu import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from na   import draw as draw_na

_S_PIE = 0.45
_S_NA  = 0.45
_HEAD_C_PIE = (150 * _S_PIE, 200 * _S_PIE)
_HEAD_C_NA  = (-150 * _S_NA, 200 * _S_NA)


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + -3 * scale, oy=oy + 13  * scale, scale=0.55 * scale)
    draw_shu (t, ox=ox + -2 * scale, oy=oy + -49 * scale, scale=0.87 * scale)
    head_t = (-2, 13)
    draw_pie(t,
        ox=ox + (head_t[0] - _HEAD_C_PIE[0]) * scale,
        oy=oy + (head_t[1] - _HEAD_C_PIE[1]) * scale,
        scale=_S_PIE * scale)
    draw_na(t,
        ox=ox + (head_t[0] - _HEAD_C_NA[0]) * scale,
        oy=oy + (head_t[1] - _HEAD_C_NA[1]) * scale,
        scale=_S_NA * scale)
