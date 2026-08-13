# bing_ren.py — 仌 (bīng, ancient form of 冰), 4 strokes: two 人 stacked.
# PASSed at p3_char_0115_仌 (B5, pos 265). Uses kiss_apex + variant_pie +
# variant_na from _shared_helpers. Upper 人 smaller, lower 人 larger with
# dominant na.
from _shared_helpers import variant_pie, variant_na, kiss_apex


def _draw_ren(t, apex, pie_tail, na_tail, bow_pie=-6.0, bow_na=+8.0,
              w_head_pie=4.0, w_tail_pie=2.0,
              w_head_na=3.0, w_belly_na=4.5, w_tail_na=2.0):
    pie_h, na_h = kiss_apex(apex, pie_tail, na_tail, u_pie=0.0, bow_pie=bow_pie)
    variant_pie(t, head=pie_h, tail=pie_tail,
                bow_perp=bow_pie, w_head=w_head_pie, w_tail=w_tail_pie)
    variant_na(t, head=na_h, tail=na_tail,
               bow_perp=bow_na, w_head=w_head_na, w_belly=w_belly_na,
               w_tail=w_tail_na, belly_u=0.7)


def draw_bing_ren(t, ox=0, oy=0, scale=1.0):
    """仌 — two stacked asymmetric 人 via kiss_apex."""
    def _sh(x, y):
        return (ox + x * scale, oy + y * scale)

    _draw_ren(t,
              apex=_sh(-10, +95),
              pie_tail=_sh(-58, +18),
              na_tail=_sh(+55, +20),
              bow_pie=-8.0, bow_na=+6.0,
              w_head_pie=4.0, w_tail_pie=2.0,
              w_head_na=3.0, w_belly_na=4.0, w_tail_na=2.0)

    _draw_ren(t,
              apex=_sh(-5, +5),
              pie_tail=_sh(-75, -105),
              na_tail=_sh(+85, -110),
              bow_pie=-10.0, bow_na=+8.0,
              w_head_pie=4.5, w_tail_pie=2.0,
              w_head_na=3.0, w_belly_na=5.0, w_tail_na=2.5)
