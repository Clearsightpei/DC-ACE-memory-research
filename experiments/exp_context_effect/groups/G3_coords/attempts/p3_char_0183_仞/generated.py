# p3_char_0183_仞 — 亻 (left) + 刃 (right).
# 刃 = 横折钩 + 撇 + 点 (dot inside the enclosure).
# Revision 2: shrink 亻, enlarge 刃, reposition strokes so the pie
# passes THROUGH the heng_zhe_gou (刀 shape) and the dot sits inside.
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402
from pie import draw_pie  # noqa: E402
from dian import draw_dian  # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # LEFT: 亻 modest, upper-left quadrant.
    draw_ren_pang(draw, ox=-60, oy=-5, scale=0.70)

    # RIGHT: 刃 — larger, right half.
    # 横折钩 (刀's outline) — scale 0.70, centered around x~+30.
    # Pre-scale span x=[-90,+80], y=[+60,-70]; after 0.70: x=[-63,+56], y=[+42,-49].
    # Shift ox=+35: span becomes x=[-28,+91], y=[+42,-49]. Good.
    draw_heng_zhe_gou(draw, ox=35, oy=0, scale=0.70)

    # 撇 (left-falling stroke of 刀) — from top-left area of heng_zhe_gou
    # sweeping down-left, crossing the top-horizontal region.
    # pie canonical head (+65,+90) tail (-45,-85). Scale 0.60.
    # Place so head sits around top-middle of the 刀 and tail exits below-left.
    draw_pie(draw, ox=15, oy=-25, scale=0.65)

    # 点 (short dot inside the 刀 enclosure — the mark that makes 刃).
    # Place around (x=+40, y=+10), small.
    draw_dian(draw, ox=50, oy=5, scale=0.40)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_仞.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
