# yong_char.py — 佣 — promoted from p3_char_0350_佣 (B10 main PASS)
# Curator B10 (2026-07-31, position 500).

# 佣 (yōng) — 亻 (left) + 用 (right). 7 strokes.
# Recipe: compressed ren_pang left (via bank) + adapted yong on right
# (bank yong_use is centered at 150,150 with scale about its center; use
# scale ~0.72 and shift right to fit into ~right 60% of canvas).
#
# Both bank funcs use PIL ImageDraw despite the `t` argname (t.line works).

import os
import sys
from PIL import Image, ImageDraw

_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from yong_use import draw_yong  # noqa: E402


def draw_yong_ren(D, ox=0, oy=0, scale=1.0):
    # 亻 on left — compressed, left-shifted (echo ding_ren recipe but
    # slightly larger so the pie/shu junction reads clearly)
    draw_ren_pang(D, ox=ox + (-65) * scale, oy=oy + 15 * scale,
                  scale=0.78 * scale)

    # 用 on right — bank draw_yong (centered at 150,150), scale down and
    # shift right so it fits into right ~55% of canvas.
    draw_yong(D, ox=ox + 45, oy=oy + 0, scale=0.72 * scale)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_yong_ren(D)
    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0350_佣/01_佣.png"
    img.save(out)
    print("saved", out)
