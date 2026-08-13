# ding_ren.py — 仃 (dīng), 5 strokes: 亻 (left) + 丁 (right).
# PASSed at p3_char_0107_仃 (B5, pos 262). ren_pang compressed left +
# inline heng + shu_gou for right 丁.
from ren_pang import draw_ren_pang
from heng import draw_heng
from shu_gou import draw_shu_gou


def draw_ding_ren(t, ox=0, oy=0, scale=1.0):
    """仃 — 亻 (compressed, left-shifted) + 丁 (heng + shu_gou)."""
    draw_ren_pang(t, ox=ox + (-55) * scale, oy=oy + 10 * scale,
                  scale=0.70 * scale)

    right_ox = ox + 35 * scale
    right_oy = oy + 0 * scale
    right_scale = 0.75 * scale
    draw_heng(t, ox=right_ox + 0 * right_scale,
              oy=right_oy + 55 * right_scale, scale=0.75 * right_scale)
    draw_shu_gou(t, ox=right_ox + 5 * right_scale,
                 oy=right_oy - 10 * right_scale, scale=0.75 * right_scale)
