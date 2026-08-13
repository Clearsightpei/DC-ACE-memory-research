# p3_char_0143_勻 — 勻 (yún, "even/uniform"), 4 strokes.
# Composition: 勹 envelope (bao_char from bank) + two internal 横 (short heng).
# Uses draw_bao_char as identity alias for outer wrap; inlines two thin
# horizontals with the same pixel-coord system (canvas 300, math-around-150).
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from bao_char import draw_bao_char  # noqa: E402


def draw_yun(t, ox=0, oy=0, scale=1.0):
    # Envelope (勹) — identity call, sits inside 300x300 nicely
    draw_bao_char(t, ox=ox, oy=oy, scale=scale)

    # Two internal short 横. In bao_char's coord system the shaft goes
    # from ~x=215 at top down to x=195 at hook. The interior opens to
    # the left. Horizontals span roughly x=110..195, thickness ~6px.
    def _hline(x0, x1, y, w=6):
        ax = 150 + ox + (x0 - 150) * scale
        ay = 150 + oy + (y - 150) * scale
        bx = 150 + ox + (x1 - 150) * scale
        by = 150 + oy + (y - 150) * scale
        t.line([(ax, ay), (bx, by)], fill=(0, 0, 0),
               width=max(2, int(round(w * scale))))

    # Upper 横 (around vertical mid of envelope)
    _hline(110, 200, 150, w=5)
    # Lower 横 (below, slightly shorter or same)
    _hline(110, 200, 200, w=5)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_yun(t, ox=0, oy=0, scale=1.0)
    out = os.path.join(_HERE, "01_勻.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
