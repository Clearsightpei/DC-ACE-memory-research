# p2_radical_074_兀 — 3 strokes: 横 (top) + 撇 (left leg) + 竖弯钩 (right leg).
#
# TR8 (INLINE-FRESH TEST) applied:
#   - 横 (top): standalone shape matches the target exactly (uniform ~12px
#     bar spanning most of the width). USE bank primitive draw_heng with a
#     deliberate placement (top of canvas, ~65% width).
#   - 撇 (left leg): the target leg is NEARLY VERTICAL with only a mild
#     left-lean at the tail — the standalone pie primitive is a WIDE
#     diagonal sweep (P10, TR8 example for 彳). INLINE FRESH as a tapered
#     bezier with a mostly-vertical spine.
#   - 竖弯钩 / 竖弯 (right leg): descends vertically then curves right at
#     the bottom. No bank primitive matches this shu-then-curve shape at
#     radical scale without heavy distortion. INLINE FRESH as one
#     tapered-line polyline (vertical segment + quarter-circle-ish curve).
#
# Composition targets (300x300 canvas, PIL pixel coords):
#   heng: from (~90, 90) to (~215, 90), thickness 12 -> uses draw_heng
#         center at math (ox=+2, oy=+60), scale=0.62.
#         Verify: half_len = 100*0.62 = 62; center px = (150+2, 150-60) = (152, 90).
#         Endpoints: (152-62, 90)=(90,90); (152+62, 90)=(214,90). MATCHES GT.
#   left pie leg: starts at (100, 95) — welds under heng near its left end
#         (weld tolerance ~5px). Descends to (75, 225). Slight leftward
#         belly. Tapered from ~10px head to ~3px tail.
#   right shu-wan leg: starts at (205, 95) — welds under heng near right
#         end. Descends vertically to (207, 205), then curves right to
#         (230, 220). Uniform ~11px thickness (P4: shu uniform ~12).
#
# TR7 sanity check:
#   - Weld gaps: left leg head (100,95) is 5px below heng right endpoint
#     (90,90) — visually welds. Right leg head (205,95) is 9px inward
#     from heng right end (214,90) — visually welds (heng end is thick).
#   - All strokes within 300x300 with >=10px margin (min x=75, max x=230,
#     min y=90, max y=225). OK.

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

from heng import draw_heng  # noqa: E402


CANVAS = 300


def _tapered_line(draw, p0, p1, w0, w1, steps=48):
    """Draw a tapered straight line from p0 to p1 with width w0 -> w1."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = w0 + (w1 - w0) * ((u0 + u1) / 2)
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0),
                  width=max(1, int(round(w))))


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=64):
    """Quadratic bezier with linear-in-u width taper."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2

    def pt(u):
        um = 1.0 - u
        x = um * um * x0 + 2 * um * u * x1 + u * u * x2
        y = um * um * y0 + 2 * um * u * y1 + u * u * y2
        return x, y

    prev = pt(0.0)
    for i in range(1, steps + 1):
        u = i / steps
        cur = pt(u)
        w = w0 + (w1 - w0) * u
        draw.line([prev, cur], fill=(0, 0, 0),
                  width=max(1, int(round(w))))
        prev = cur


def draw_wu(draw):
    # Stroke 1: 横 (top horizontal). Bank primitive with deliberate placement.
    # TR6 comment: heng default center (150,150) -> target center (152, 90).
    # ox = +2 (math), oy = +60 (math, since +y up), scale = 0.62.
    draw_heng(draw, ox=+2, oy=+60, scale=0.62)

    # Stroke 2: 撇 (left leg). REV1: GT shows a mostly-straight leg with
    # only a mild left-curl at bottom third. Reduce belly, thicker at tail
    # (radical-撇 vs stroke-撇: keeps more ink to the tip, per P10).
    # Head at (100, 95); tail at (72, 232). Slight left-belly bezier.
    _tapered_bezier(
        draw,
        p0=(100, 95),
        p1=(92, 170),   # subtle left bias for gentle leftward curl
        p2=(72, 232),
        w0=9, w1=5,
    )

    # Stroke 3: 竖弯 (right leg, no visible hook per GT). REV1: extend the
    # curve so it sweeps more smoothly, ending flatter (not down-diving).
    _tapered_line(
        draw,
        p0=(205, 95),
        p1=(208, 210),
        w0=10, w1=10,
    )
    # Curve segment: rounded elbow, ending horizontal at ~y=222.
    _tapered_bezier(
        draw,
        p0=(208, 210),
        p1=(210, 224),   # elbow control
        p2=(232, 224),
        w0=10, w1=7,
    )


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wu(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_兀.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
