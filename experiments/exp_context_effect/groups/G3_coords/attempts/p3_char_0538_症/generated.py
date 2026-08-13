# p3_char_0538_症 (zhèng) — 疒 envelope + 正 (upright) interior.
#
# GT decomposition (from gt/phase3/症.png):
#   1. 疒: top-right small dot, thin heng roof, long left-descending 撇,
#      two 冫 marks (upper 点 + lower 提) in upper-left belly.
#   2. 正: 5 strokes — top heng, left shu, middle short heng,
#      right short shu, base heng. Sits in the belly (right of pie
#      shaft, below the top heng).
#
# Bank reuse:
#   - Envelope: reuse draw_ne_chuang from ne_sick.py (v9 rerun graduate,
#     the canonical 疒 envelope; used cleanly by shan_hernia and others).
#   - Interior 正: inline PIL fresh render (no bank 正 primitive exists
#     that fits this scale/position; keep same PIL coord system as envelope).
#
# No BANK_DEVIATION — envelope is used as-is; interior 正 is a fresh
# inline render (no bank 正 exists).

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from ne_sick import draw_ne_chuang  # noqa: E402

_CANVAS = 300


def draw_zheng_interior(draw, top_y=155, base_y=258, left_x=145,
                        right_x=255, w=6):
    """正 (5 strokes) rendered inline in the belly of 疒.

    top_y  = y of top heng
    base_y = y of base heng
    left_x, right_x = extents of top & base heng
    """
    mid_y = (top_y + base_y) // 2 + 8  # middle heng slightly below center
    # Left vertical sits inset from the top-heng's left end.
    left_v_x = left_x + 8
    # Middle heng is shorter, centered.
    mid_hleft = left_v_x
    mid_hright = left_x + int((right_x - left_x) * 0.62)
    # Right short vertical sits between middle heng right and base.
    right_v_x = mid_hright

    # Stroke 1: top heng.
    draw.line([(left_x, top_y), (right_x, top_y)],
              fill=(0, 0, 0), width=w)
    # Stroke 2: left 竖 (down from just inside top heng's left end to base).
    draw.line([(left_v_x, top_y), (left_v_x, base_y)],
              fill=(0, 0, 0), width=w)
    # Stroke 3: middle short heng.
    draw.line([(mid_hleft, mid_y), (mid_hright, mid_y)],
              fill=(0, 0, 0), width=w)
    # Stroke 4: right short 竖 (from middle heng down to base).
    draw.line([(right_v_x, mid_y), (right_v_x, base_y)],
              fill=(0, 0, 0), width=w)
    # Stroke 5: base heng — the widest, spans the belly base.
    draw.line([(left_x - 5, base_y), (right_x + 5, base_y)],
              fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    # Envelope 疒 from bank.
    draw_ne_chuang(draw)
    # Interior 正 in the belly (right of pie shaft, below heng roof).
    draw_zheng_interior(draw, top_y=160, base_y=258,
                        left_x=150, right_x=258, w=6)
    out = os.path.join(_HERE, "01_症.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
