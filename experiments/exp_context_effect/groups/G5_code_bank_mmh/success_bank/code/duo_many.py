"""Bank primitive: 多 (duō, 'many' — 6 strokes = 2 stacked 夕).

Promoted from p3_char_0245_多 (G5 B8 PASS via BANK_DEVIATION on heng_pie).

Each 夕 = pie + heng_pie_slim + dian. Top 夕 sits in TC/ML region; bottom
夕 sits in C/BL. All 7 joints are N-class (natural gap); do NOT weld.

Reuse targets: 多 (identity), 名 (sibling top 夕), 岁, 够, 夜.
"""

from pie import draw_pie
from dian import draw_dian
from heng_pie_slim import draw_heng_pie_slim


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_duo_many(draw, ox=0, oy=0, scale=1.0):
    def T(x, y):
        return _tx(x, y, ox, oy, scale)

    def w(v):
        return max(2, int(v * scale))

    # --- TOP 夕 ---
    # s1: pie TC -> ML
    draw_pie(draw, T(139.5, 54.5), T(76.8, 124.5),
             bow_perp=8, w_head=w(6), w_tail=w(3))
    # s2: heng_pie_slim ML -> BL
    draw_heng_pie_slim(draw, T(107.7, 87.4), T(63.3, 154.7),
                       horiz_len=int(20 * scale),
                       bow_perp=6, w_head=w(5), w_corner=w(4), w_tail=w(2))
    # s3: dian C -> C
    draw_dian(draw, T(115.0, 106.0), T(148.0, 128.0),
              w_head=w(2), w_tail=w(6), bow=w(2), steps=40)

    # --- BOTTOM 夕 ---
    # s4: pie C -> BL
    draw_pie(draw, T(178.5, 141.5), T(55.3, 259.3),
             bow_perp=13, w_head=w(9), w_tail=w(3))
    # s5: heng_pie_slim in BC area
    draw_heng_pie_slim(draw, T(145.0, 175.0), T(103.0, 245.0),
                       horiz_len=int(22 * scale),
                       bow_perp=6, w_head=w(5), w_corner=w(4), w_tail=w(2))
    # s6: dian BC -> BC (bottom right dot)
    draw_dian(draw, T(146.0, 195.0), T(184.0, 220.0),
              w_head=w(2), w_tail=w(7), bow=w(2), steps=40)
