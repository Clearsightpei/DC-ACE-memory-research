# p3_char_0052_亡 — G3 attempt
# 亡 has 3 strokes: (1) small 点/short-pie at top (upper-right area),
# (2) long 横 across middle,
# (3) 竖折: vertical stroke down from left, turning right along bottom.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402
from shu_zhe import draw_shu_zhe  # noqa: E402


CANVAS_SIZE = 300


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: small dot at top-right area (above heng, right of center).
    # GT shows a small slash going from upper-right down-left toward the heng.
    # Use dian primitive at (ox=+10, oy=+70), scale ~0.55
    draw_dian(draw, ox=10, oy=65, scale=0.55)

    # Stroke 2: long 横 across the middle (slightly above center).
    # From GT the heng spans most of canvas width; scale ~1.15
    draw_heng(draw, ox=0, oy=20, scale=1.15)

    # Stroke 3: 竖折 — vertical descends from left end of heng, then turns right
    # along the bottom. Bank primitive is scale=1.0: vertical from
    # (-30, +90) to (-30, -70), then horizontal to (+70, -70). We place it
    # centered below the heng.
    # We want the vertical top to sit just below-left of the heng start.
    # Heng spans math x=[-115, +115] at oy=20. Vertical top should sit near
    # x=-95, y=15. Bottom near y=-95. Right end near x=+95.
    # Primitive at scale=1.0 goes vertical -30→-30 x, top y=+90, bottom y=-70,
    # right x=+70. Offset: we want top at (-95, +15) => ox = -95-(-30)=-65,
    # oy = 15-90 = -75. Then bottom becomes (-95, -145) too low. Scale down.
    # Try scale 0.9: vertical top (-27,+81), bottom (-27,-63), right (+63,-63)
    # Want top at (-95, +15): ox = -95-(-27)=-68; oy = 15-81=-66.
    # Then bottom: (-95, -129) — still too far. Let me pick top at (-95, +5),
    # bottom at (-95, -85), right at (+95, -85).
    # dx_vertical = 0, need horizontal span = 190 px, vertical span = 90 px.
    # Primitive vertical span = 160, horizontal span = 100 (at scale 1).
    # These proportions don't match — inline it fresh instead.

    # Inline 竖折 to match target proportions.
    ink = 10
    # Vertical: from (x_left, y_top) down to (x_left, y_bot)
    x_left = -95
    y_top = 15    # just below heng
    y_bot = -95   # near bottom of char
    x_right = 95
    # Convert to PIL
    def to_px(mx, my):
        return (CANVAS_SIZE / 2 + mx, CANVAS_SIZE / 2 - my)

    draw.line([to_px(x_left, y_top), to_px(x_left, y_bot)],
              fill=(0, 0, 0), width=ink)
    draw.line([to_px(x_left, y_bot), to_px(x_right, y_bot)],
              fill=(0, 0, 0), width=ink)
    # Corner blob (顿笔) at the turn
    r = ink // 2 + 1
    cx, cy = to_px(x_left, y_bot)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # End caps
    for pt in [(x_left, y_top), (x_right, y_bot)]:
        px, py = to_px(*pt)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_亡.png")
    img.save(out_path)
    print(f"saved {out_path}")


if __name__ == "__main__":
    main()
