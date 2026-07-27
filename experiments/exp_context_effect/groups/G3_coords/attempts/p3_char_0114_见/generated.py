# p3_char_0114_见 — 见 (jian, "see"), 4 strokes.
# Composition: 冂-like top (竖 + 横折 open at bottom) + 儿-like bottom
# (撇 + 竖弯钩) but joined — 儿 strokes start from inside the 冂 opening.
#
# Bank primitives used:
#  - draw_shu           : left 竖 of the 冂 top
#  - draw_heng_zhe      : top + right of the 冂
#  - draw_er_ren        : the 撇 + 竖弯钩 pair (rescaled + shifted so
#                         its two strokes align with 冂's opening)
#
# GT observation: the 冂 top is compact, ~upper-left of canvas.
# The 儿 legs extend down and slightly wider than the box.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu import draw_shu                # noqa: E402
from heng_zhe import draw_heng_zhe      # noqa: E402
from er_ren import draw_er_ren          # noqa: E402


def draw_jian(t, ox=0, oy=0, scale=1.0):
    """见: 冂-top (2 strokes) + 儿-bottom (2 strokes)."""
    # --- Top 冂 (open at bottom) ---
    # Left 竖: from (~-60, +80) down to (~-60, 0). Length ~80 → scale 0.40.
    draw_shu(t, ox=ox + (-60) * scale, oy=oy + 40 * scale, scale=0.40 * scale)
    # 横折: top bar + right vertical.
    # heng_zhe canonical: h_start(-90,60), corner(80,60), v_end(80,-75).
    # At scale 0.70: bar y ≈ +42, bar_x from -63 to +56, v_end y ≈ -52.
    # Shift so bar_start lands near (-60, +80) → ox=+3, oy=+38.
    draw_heng_zhe(t, ox=ox + 3 * scale, oy=oy + 38 * scale, scale=0.70 * scale)

    # --- Bottom 儿 legs ---
    # er_ren canonical: pie head roughly (-65,-22)*s, shu_wan_gou at (22,-15)*s.
    # Want pie head to attach near the left 竖 bottom (~-60, ~0) and
    # shu_wan_gou near the right vertical bottom (~+56, ~-8).
    # Use scale 1.0 and shift origin so pie starts near (-60, 0).
    # pie at (-65, -22) so ox_er=+5 → pie x=-60; oy_er=+22 → pie y=0.
    # shu_wan_gou lands at (22+5, -15+22) = (27, 7) — too high/left.
    # Adjust: use scale 1.15 to widen, and lower the whole group.
    draw_er_ren(t, ox=ox + 6, oy=oy + 5, scale=1.15 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_jian(t)
    out = os.path.join(os.path.dirname(__file__), "01_见.png")
    img.save(out)
    print("wrote", out)
