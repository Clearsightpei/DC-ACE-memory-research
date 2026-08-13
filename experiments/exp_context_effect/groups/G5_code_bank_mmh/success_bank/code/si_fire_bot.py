"""Bank primitive: 灬 (four-dots-water / fire-bottom — 4 dots at bottom).

Promoted from p2_radical_087_灬 (G5 B2 PASS 2026-08-08). HIGH-REUSE
bottom-radical: appears in 点/热/然/黑/煮/照/熊/无... Leftmost is a
leftward pie; middle two are short down-right dians; rightmost is a
long rightward dian. No joints — natural gaps between all four.
"""

from PIL import ImageDraw

from pie import draw_pie
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_si_fire_bot(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 — leftmost pie (down-left, slight rightward bow)
    draw_pie(draw, head=_tx(67.7, 170.8, ox, oy, scale),
             tail=_tx(50.4, 220.6, ox, oy, scale),
             bow_perp=max(2, int(4 * scale)),
             w_head=max(2, int(7 * scale)),
             w_tail=max(1, int(3 * scale)))
    # s2 — short dian leaning right
    draw_dian(draw, head=_tx(106.9, 172.0, ox, oy, scale),
              tail=_tx(122.5, 203.3, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(7 * scale)),
              bow=max(1, int(2 * scale)))
    # s3 — short dian leaning right
    draw_dian(draw, head=_tx(154.4, 170.8, ox, oy, scale),
              tail=_tx(172.9, 198.9, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(7 * scale)),
              bow=max(1, int(2 * scale)))
    # s4 — long rightward dian (na-like)
    draw_dian(draw, head=_tx(209.2, 169.0, ox, oy, scale),
              tail=_tx(252.0, 219.4, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(9 * scale)),
              bow=max(2, int(3 * scale)))
