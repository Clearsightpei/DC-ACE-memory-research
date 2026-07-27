# p3_char_0160_可 — 可 (kě) — 5 strokes.
# Structure: top 一 (long horizontal spanning most of width),
#            小口 (small mouth) in lower-left,
#            竖钩 (long vertical + left hook) on the right side.
# Bank calls: draw_heng (top), draw_kou (口), draw_shu_gou (right hook).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng import draw_heng            # noqa: E402
from kou import draw_kou              # noqa: E402
from shu_gou import draw_shu_gou      # noqa: E402


CANVAS = 300


def draw_ke(t, ox=0.0, oy=0.0, scale=1.0):
    """可 — composition of top 横, lower-left 口, right 竖钩."""
    # Top 一: long horizontal, sits high on canvas.
    # length ~ 200*0.90 = 180 px; centered slightly left of center.
    draw_heng(t, ox=ox + 0 * scale, oy=oy + 70 * scale, scale=0.90 * scale)

    # 口 in lower-left, tucked just under the 一, slightly bigger so it
    # reads clearly. At scale 0.48 → ~62x48 box. Center near (-30, 15).
    draw_kou(t, ox=ox + (-30) * scale, oy=oy + 15 * scale, scale=0.48 * scale)

    # 竖钩 on the right: long vertical from just under top 一 down toward bottom,
    # with hook at bottom flicking up-left.
    # draw_shu_gou half_len = 90*scale; at scale=0.80 → half_len=72, shaft 144 px.
    # Center vertical at y=-10 so top ≈ +62 (just under 一) and bottom ≈ -82.
    draw_shu_gou(t, ox=ox + 60 * scale, oy=oy + (-10) * scale, scale=0.80 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_ke(t, ox=0, oy=0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_可.png")
    img.save(out_path)
    print(f"Wrote {out_path}")
