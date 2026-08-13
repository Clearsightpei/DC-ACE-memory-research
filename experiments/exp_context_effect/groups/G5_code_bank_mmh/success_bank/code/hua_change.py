"""Bank primitive: 化 (hua, "change" — 4 strokes: 亻 (pie+shu) + 匕).

Promoted from p3_char_0134_化 (G5 B6 PASS, 2026-08-08). L-R composition
built from two bank radicals: `draw_ren_left` on the left (compressed +
shifted left), `draw_bi` on the right (compressed + shifted right/down).

Reuse targets: 花 (艹+化), 华 (亻+化-derivative), and any L-R char
with 亻+匕 pattern.

Signature: (draw, ox=0, oy=0, scale=1.0).
"""

from PIL import ImageDraw

from ren_left import draw_ren_left
from bi_dagger import draw_bi


def draw_hua(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # 亻 shrunk to 0.75 and shifted left; the primitive already
    # bakes internal geometry, so ox absorbs the composition offset.
    draw_ren_left(draw, ox=ox - 40 * scale, oy=oy + 15 * scale,
                  scale=0.75 * scale)
    # 匕 shrunk to 0.65, shifted right + down
    draw_bi(draw, ox=ox + 100 * scale, oy=oy + 40 * scale,
            scale=0.65 * scale)
