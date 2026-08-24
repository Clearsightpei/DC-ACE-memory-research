# p3_char_0139_礻 (shi, "spirit/altar", 4 strokes) — character version.
# Char↔radical cross-transfer: the Phase-2 radical 礻 PASSed at position 148
# as shi_ceremony_pang.py. Since the Phase-3 char is the same glyph, use
# an IDENTITY alias per memory_index.md read-order step 3 (Phase-3 char
# whose Phase-2 radical exists in bank → try IDENTITY alias first).

import os
import sys

from PIL import Image, ImageDraw

_BANK = os.path.join(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G3_coords/success_bank/code"
)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shi_ceremony_pang import draw_shi_ceremony_pang  # noqa: E402

CANVAS = 300
OUT = ("<REPO_ROOT>/"
       "experiments/exp_context_effect/groups/G3_coords/"
       "attempts/p3_char_0139_礻/01_礻.png")


def draw():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    # IDENTITY alias: same offsets and scale as the mastered radical.
    draw_shi_ceremony_pang(t, ox=0.0, oy=0.0, scale=1.0)
    img.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    draw()
