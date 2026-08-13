# p3_char_0260_伙 — 伙 (huǒ), 6 strokes: 亻 (left, 2) + 火 (right, 4).
# Composition:
#   Left: ren_pang at scale 0.55, ox=-55 (compressed 亻).
#   Right: 火 built inline from bank primitives — top-left dian (左点),
#          top-right short pie, main pie + na forming 人 apex around
#          (+45, +25). Right slot centered around ox=+40.
import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from pie import draw_pie            # noqa: E402
from na import draw_na              # noqa: E402
from dian import draw_dian          # noqa: E402


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # --- LEFT: 亻 (ren_pang) at scale 0.65, taller/larger ---
    draw_ren_pang(d, ox=-70.0, oy=-15.0, scale=0.65)

    # --- RIGHT: 火 built inline ---
    # 人-apex around (+45, +10). scale ~0.65 so it fills the right slot.
    # Main pie: canonical head at (+65*s, +90*s). For head at (+45, +10):
    #   ox = 45 - 65*0.65 ≈ 3, oy = 10 - 90*0.65 ≈ -49
    draw_pie(d, ox=3.0, oy=-49.0, scale=0.65)
    # Main na: canonical head at (-70*s, +80*s). For head at (+45, +10):
    #   ox = 45 + 70*0.65 ≈ 91, oy = 10 - 80*0.65 ≈ -42
    draw_na(d, ox=91.0, oy=-42.0, scale=0.65)

    # Top-left 左点 — slanting stroke, up-right to down-left, at (+15, +85).
    draw_dian(d, ox=15.0, oy=85.0, scale=0.6)

    # Top-right short 撇 (small pie), at (+75, +85).
    draw_pie(d, ox=75.0, oy=85.0, scale=0.4)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伙.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
