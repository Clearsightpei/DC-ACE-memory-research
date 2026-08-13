# 采 (cǎi) = 爫 (top claw) + 木 (tree base).
# Bank primitives zhao_top + mu, composed vertically; scale-up on 爫
# so it visually balances the 木; 木 heng sits just below the claw baseline.
import os
import sys
from PIL import Image, ImageDraw

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..",
                                     "success_bank", "code"))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from zhao_top import draw_zhao_top  # noqa: E402
from mu import draw_mu  # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)
    # Top claw radical 爫 — enlarged so its width matches the 木 spread.
    draw_zhao_top(d, ox=0, oy=52, scale=1.25)
    # Base 木 — heng near center; shu extends up into the 爫 area.
    draw_mu(d, ox=0, oy=5, scale=0.85)
    return img


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_采.png")
    render().save(out)
    print("wrote", out)
