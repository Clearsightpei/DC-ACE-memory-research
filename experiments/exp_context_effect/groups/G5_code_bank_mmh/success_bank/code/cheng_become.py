"""Bank primitive: 成 (chéng, "become") — 6 strokes.

Promoted from p3_char_0243_成 R1 (G5 B9 PASS 2026-08-09). VALIDATES
P-A-007: main FAIL had wispy pie + wrong hook direction; R1 tuned
xie_gou (bow=14, hook_up=36, hook_back=8) and inflated s3 into a compact
heng_zhe_gou. Note drawer did NOT call draw_ge_dagger despite queue
suggestion — decided 成 anchors differ from 戈 anchors enough that
individual tuned strokes were the right call.

MEDIUM-REUSE: xie_gou-family template (成/戏/咸/威/戌). Records the
correct xie_gou params for the "long diagonal crossing full canvas"
class of stroke.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from xie_gou import draw_xie_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_cheng_become(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top short heng
    draw_heng(draw, _tx(90.5, 147.4, ox, oy, scale),
              _tx(208.9, 124.8, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2 long pie (heavy left contour)
    draw_pie(draw, _tx(67.7, 142.1, ox, oy, scale),
             _tx(28.4, 291.2, ox, oy, scale),
             bow_perp=22, w_head=12, w_tail=4)
    # s3 inner heng_zhe_gou fragment
    draw_heng_zhe_gou(draw,
                      heng_head=_tx(60.0, 200.0, ox, oy, scale),
                      corner=_tx(90.0, 208.0, ox, oy, scale),
                      gou_tail=_tx(95.8, 252.5, ox, oy, scale),
                      hook_tip=_tx(82.0, 244.0, ox, oy, scale))
    # s4 xie_gou — long diagonal + up hook (A-recipe params)
    draw_xie_gou(draw, head=_tx(132.4, 53.6, ox, oy, scale),
                 tail=_tx(274.8, 248.1, ox, oy, scale),
                 width=8, bow=14, hook_up=36, hook_back=8)
    # s5 inner pie
    draw_pie(draw, _tx(211.5, 164.4, ox, oy, scale),
             _tx(146.2, 272.8, ox, oy, scale),
             bow_perp=12, w_head=9, w_tail=3)
    # s6 upper-right dian
    draw_dian(draw, _tx(191.3, 72.4, ox, oy, scale),
              _tx(223.5, 92.6, ox, oy, scale),
              w_head=2, w_tail=7, bow=3)
