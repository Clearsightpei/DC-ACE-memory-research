# p3_char_0062_卄 — 卄 (nian)
#
# Structurally similar to 廾 but with a more symmetric appearance:
# both vertical strokes are essentially 竖 (with only slight lean),
# not a strong 撇-vs-竖 pair. GT shows two mostly-vertical strokes
# crossed by one horizontal near the middle.
#
# So we do NOT reuse gong_radical directly (its 撇 is too curved for 卄).
# Instead we inline three near-vertical + one horizontal line, matching
# the GT silhouette.

import os
from PIL import Image, ImageDraw

_CANVAS = 300


def _to_px(bx, by, ox=0.0, oy=0.0, scale=1.0):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def draw_nian(draw, ox=0.0, oy=0.0, scale=1.0):
    """卄: two near-vertical strokes + one horizontal crossbar."""
    thickness = max(1, int(round(9 * scale)))

    # Stroke 1: left vertical (slight lean, top slightly right of bottom).
    p_top_l = _to_px(-38, +70, ox, oy, scale)
    p_bot_l = _to_px(-50, -85, ox, oy, scale)
    draw.line([p_top_l, p_bot_l], fill=(0, 0, 0), width=thickness)

    # Stroke 2: horizontal crossbar (spans wider than the two verticals).
    p_left = _to_px(-80, +5, ox, oy, scale)
    p_right = _to_px(+72, +5, ox, oy, scale)
    draw.line([p_left, p_right], fill=(0, 0, 0), width=thickness)

    # Stroke 3: right vertical (slight lean, top slightly left of bottom).
    p_top_r = _to_px(+42, +70, ox, oy, scale)
    p_bot_r = _to_px(+52, -85, ox, oy, scale)
    draw.line([p_top_r, p_bot_r], fill=(0, 0, 0), width=thickness)


def render():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_nian(draw, ox=0.0, oy=0.0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_卄.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    render()
