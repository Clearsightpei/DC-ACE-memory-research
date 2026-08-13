# chuan_char.py — 串 — promoted from p3_char_0296_串__retry_1 (B10 retry PASS)
# Curator B10 (2026-07-31, position 500).

# p3_char_0296_串__retry_1 — 串 (chuan, "string/skewer"), 2 stacked 口
# pierced by a single central 竖.
#
# TRAJECTORY DIFF (from inspecting GT + main FAIL PNG)
# FAILED main attempt gaps:
#   1. Both 口 boxes rendered too SMALL (kou_scale=0.45 → ~58w x 45h).
#      In GT the boxes are substantial, filling most of the left-right
#      band. Fix: bump kou_scale to ~0.62 → ~80w x 60h.
#   2. Vertical shu protrusion above the top box was too short — in GT
#      the shu clearly sticks up above the top box (~30-40 units) and
#      well below the bottom box (~50+ units). Fix: extend top to +125,
#      bottom to -135.
#   3. Top and bottom boxes sat too close to center — leaving little
#      room for shu head/tail. Fix: push oy to +55 / -55 so gap opens.
#
# RETRY MEMORY CHECKLIST (v7 evolution)
# Q1 (errata): errata says boxes too small at 0.42 scale; shu doesn't
#   protrude visibly. Fix idea: bigger boxes + longer protrusion.
# Q2 (form_catalog): kou primitive at scale 0.6-0.65 renders full-size;
#   for 串's stacked pair, scale ~0.6 fits vertically in canvas.
# Q3 (helpers): No X-crossing / apex-kiss here — piercing shu is at
#   x=0 in the interior of each box, doesn't touch box strokes. No
#   mirror-dot pair. Bank kou + inline shu is the right recipe.
import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from kou import draw_kou  # noqa: E402


CANVAS = 300


def _to_pixel(mx, my):
    return CANVAS / 2 + mx, CANVAS / 2 - my


def draw_chuan(d, ox=0.0, oy=0.0, scale=1.0):
    """串: two stacked kou boxes pierced by a central vertical shu."""
    kou_scale = 0.62 * scale
    # Top 口 — sits high; center around y=+55.
    draw_kou(d, ox=ox + 0, oy=oy + 55 * scale, scale=kou_scale)
    # Bottom 口 — sits low; center around y=-55.
    draw_kou(d, ox=ox + 0, oy=oy + (-55) * scale, scale=kou_scale)
    # Central piercing 竖 — through x=0, protrudes above top box and
    # tail extends well below bottom box.
    top_y = 125 * scale + oy
    bot_y = -135 * scale + oy
    x_top, y_top = _to_pixel(ox + 0, top_y)
    x_bot, y_bot = _to_pixel(ox + 0, bot_y)
    d.line([(x_top, y_top), (x_bot, y_bot)], fill=(0, 0, 0), width=8)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_chuan(d, ox=0.0, oy=0.0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_串.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
