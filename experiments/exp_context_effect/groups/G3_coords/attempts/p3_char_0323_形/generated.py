# 形 (xing) — p3_char_0323
# Composition: 开 (left, 4 strokes) + 彡 (right, 3 pie strokes).
# 彡 uses bank primitive `shan_radical` (identity of a mastered radical).
# 开 rendered inline with PIL (no direct bank match for 开).
# Canvas 300x300, math-coord helpers (+y up, origin center=(150,150)).

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

from shan_radical import draw_shan_radical  # noqa: E402

CANVAS = 300


def _px(mx, my):
    """math coord (center origin, +y up) -> pixel."""
    return CANVAS / 2 + mx, CANVAS / 2 - my


def stroke(draw, pts, width=6):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=width)
        r = width / 2
        for p in (pts[i], pts[i + 1]):
            draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=(0, 0, 0))


def draw_kai_left(d):
    """开 on the left half. Uses pixel coords tuned to GT."""
    # 1. top short heng: mostly-flat, slight rise on right.
    stroke(d, [(45, 105), (90, 100), (130, 105)], width=5)

    # 3. long horizontal crossing both uprights
    stroke(d, [(20, 160), (95, 156), (165, 160)], width=5)

    # 2. left pie/vertical: starts near top-inner, sweeps down-left.
    pts = []
    for i in range(21):
        u = i / 20
        x = 78 + (35 - 78) * u
        y = 110 + (235 - 110) * u
        # slight bow: pulled left in middle
        x += -6 * (1 - u) * u * 4
        pts.append((x, y))
    for i in range(len(pts) - 1):
        w = int(round(6 - 3 * (i / max(1, len(pts) - 1))))
        d.line([pts[i], pts[i + 1]], fill=(0, 0, 0), width=max(2, w))

    # 4. right vertical, small left-hook at bottom
    stroke(d, [(128, 105), (128, 230)], width=6)
    stroke(d, [(128, 230), (118, 240)], width=4)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # left component 开
    draw_kai_left(d)

    # right component 彡 via bank primitive.
    # Bank pies at scale 0.32/0.38/0.48 are small; bump outer scale to
    # 1.55 for a full-height 彡 that matches GT.
    # Center around pixel (230, 155) -> math (80, -5).
    draw_shan_radical(d, ox=80.0, oy=-5.0, scale=1.55)

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_形.png"
    )
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
