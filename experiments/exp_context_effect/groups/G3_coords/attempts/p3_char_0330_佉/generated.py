# p3_char_0330_佉 — 佉 (qū), 8 strokes.
# Decomposition: 亻 (left) + 去 (right); 去 = 土 (top) + 厶 (bottom).
# Layout: 亻 tall on left (~35% width); 去 fills right, stacked top+bottom.
# Trust-GT posture (v8): thin uniform lines to match MMH aesthetic.

import os
import sys
from PIL import Image, ImageDraw

BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from ren_pang import draw_ren_pang  # noqa: E402


def draw_tu_small(d, cx, cy, w=90, h=60):
    """Inline 土: heng (top, SHORT), shu (mid), heng (bottom, WIDE)."""
    # top heng — clearly shorter than bottom (土 distinguishes from 士)
    top_y = cy - h / 2
    d.line([(cx - w * 0.24, top_y), (cx + w * 0.24, top_y)],
           fill=(0, 0, 0), width=4)
    # shu — vertical from top-heng to bottom-heng
    d.line([(cx, top_y - 2), (cx, cy + h / 2)],
           fill=(0, 0, 0), width=4)
    # bottom heng — wider (extends fully across w)
    d.line([(cx - w / 2, cy + h / 2), (cx + w / 2, cy + h / 2)],
           fill=(0, 0, 0), width=4)


def draw_si_small(d, cx, cy, w=80, h=60):
    """Inline 厶 (2 strokes): (1) 撇折 — pie down-left then horizontal fold
    right; (2) small 点/收笔 at upper-right closing the shape."""
    # 撇折 stroke — pie sweep down-left, then hard turn to horizontal right
    x_top = cx + w * 0.10
    y_top = cy - h * 0.35
    x_bend = cx - w * 0.35
    y_bend = cy + h * 0.30
    x_fold_end = cx + w * 0.30
    y_fold_end = cy + h * 0.35
    # sub-segment a: pie down-left
    d.line([(x_top, y_top), (x_bend, y_bend)],
           fill=(0, 0, 0), width=4)
    # sub-segment b: horizontal fold rightward (slightly rising)
    d.line([(x_bend, y_bend), (x_fold_end, y_fold_end)],
           fill=(0, 0, 0), width=4)
    # closing 点 — SHORT diagonal from upper-right area meeting fold end
    x_dot_a = cx + w * 0.05
    y_dot_a = cy - h * 0.05
    x_dot_b = cx + w * 0.28
    y_dot_b = cy + h * 0.30
    d.line([(x_dot_a, y_dot_a), (x_dot_b, y_dot_b)],
           fill=(0, 0, 0), width=4)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # 亻 on left — tall, slim, positioned ox=-70
    draw_ren_pang(d, ox=-70.0, oy=0.0, scale=0.95)

    # 去 on right — split into 土 (top) + 厶 (bottom)
    # right column center x ~ 200 (i.e. ox=+50 relative to canvas center)
    right_cx = 200
    # 土 top-right, upper band
    draw_tu_small(d, cx=right_cx, cy=100, w=80, h=60)
    # 厶 bottom-right, lower band
    draw_si_small(d, cx=right_cx, cy=210, w=90, h=70)

    out = os.path.join(os.path.dirname(__file__), "01_佉.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
