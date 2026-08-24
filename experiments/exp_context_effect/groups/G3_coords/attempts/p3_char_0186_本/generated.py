# p3_char_0186_本 — 本 (běn, root), 5 strokes: 木 + short 横 near base of 竖.
# Revision: shrink mu to fit canvas better; short heng lower on the vertical.

import sys
from PIL import Image, ImageDraw

BANK_CODE = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
sys.path.insert(0, BANK_CODE)

from mu import draw_mu, _inline_heng

OUT_PNG = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0186_本/01_本.png"


def draw_ben(t, ox=0.0, oy=0.0, scale=0.85):
    # Draw 木 scaled to leave room; shift up slightly.
    draw_mu(t, ox=ox, oy=oy + 5, scale=scale)
    # mu's 竖 spans y in [-115..+25]*scale + oy+5. Place short heng at y=-70*scale.
    _inline_heng(t, ox + 0, oy + 5 + (-70) * scale, 20 * scale, thickness=6)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), "white")
    t = ImageDraw.Draw(img)
    draw_ben(t, ox=0, oy=0, scale=0.85)
    img.save(OUT_PNG)
    print("wrote", OUT_PNG)
