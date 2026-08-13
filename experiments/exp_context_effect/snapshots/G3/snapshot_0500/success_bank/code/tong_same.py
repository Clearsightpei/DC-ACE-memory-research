# generated.py — 仝 (tong / same-as 同), 5 strokes.
# Composition: 人 (top, pie + na meeting at apex) + 工 (bottom, gong radical).
# Bank primitives used:
#   pie, na (for 人 apex) — offset so heads meet at apex ~(0, +75)
#   gong (for 工 bottom) — shifted down into lower half
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

from pie import draw_pie  # noqa: E402
from na import draw_na    # noqa: E402
from gong import draw_gong  # noqa: E402


def draw_tong(t, ox=0.0, oy=0.0, scale=1.0):
    """仝: 人 (apex ~top-center) sitting on 工 (bottom half).

    人 apex sits high; the two legs splay outward covering the top half.
    工 is compact and centered in the bottom third.
    """
    # 人 — apex near (0, +95), legs splaying out to roughly (-70, -5)
    # (pie tail) and (+70, -5) (na tail). Larger scale so 人 covers the
    # top ~55% of canvas.
    #
    # pie canonical head at (+65*scale, +90*scale), tail at (-45, -85).
    # Choose scale 0.75. Place head near (0, +95):
    #   ox_pie = 0 - 65*0.75 ≈ -49
    #   oy_pie = 95 - 90*0.75 ≈ 27
    draw_pie(t, ox=ox + (-49) * scale, oy=oy + 27 * scale, scale=0.75 * scale)
    # na canonical head at (-70*scale, +80*scale), tail at (+80, -90).
    # scale 0.75. Place head near (0, +95):
    #   ox_na = 0 - (-70)*0.75 ≈ +52
    #   oy_na = 95 - 80*0.75 ≈ 35
    draw_na(t, ox=ox + 52 * scale, oy=oy + 35 * scale, scale=0.75 * scale)

    # 工 in the bottom third — shift gong down so its top-heng sits
    # near y = -20 (under the 人 legs), bottom-heng near y = -110.
    #   gong canonical: top-heng at oy=+45, bottom-heng at oy=-80.
    #   choose gong_scale=0.80. Place top-heng at ~-25:
    #     oy_gong = -25 - 45*0.80 = -61
    draw_gong(t, ox=ox, oy=oy + (-65) * scale, scale=0.85 * scale)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_tong(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_仝.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
