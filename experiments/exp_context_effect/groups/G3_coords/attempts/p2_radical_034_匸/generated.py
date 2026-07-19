"""p2_radical_034_匸 (xi) — 2 strokes.

Decomposition (from GT + shared radical knowledge):
  Stroke 1: 一 (top horizontal, spanning ~180 px wide, upper portion of canvas).
  Stroke 2: 竖折 (short vertical dropping from top-left down, then horizontal
            running rightward at the bottom — the 𠃊 shape enclosing 匸 below).

匸 differs from 匚 in that the top stroke is a plain 一 (not 一 with a
right-side descender) — the enclosure is only on the left+bottom.

Bank primitives used:
  - draw_heng from heng.py (canonical 200x12 horizontal): scale 0.9 → ~180 px.
    Placed near top (oy = +55 math coords), center-x on canvas (ox=0).
  - draw_shu_zhe from shu_zhe.py: canonical L (vertical 160 px + horizontal 100
    px) has too-short a horizontal for 匸's bottom, so we INLINE the shu_zhe
    recipe here per TR5 — we need the bottom horizontal to span ~180 px to
    match the top 一 above it. Vertical spans from just below the top 一
    (y ≈ +50) down to bottom (y ≈ -80). Horizontal spans from left (x=-90)
    to right (x=+90) at y=-80.

Eyeball sanity (TR7):
  - Top 一: pixels x ∈ [60, 240], y = 95. Length 180 px, thickness 11 px.
  - Vertical of 竖折: from (60, 100) down to (60, 230). Height 130 px.
  - Horizontal of 竖折: from (60, 230) to (240, 230). Width 180 px.
  - Small gap (~5 px) between top 一 and vertical descender is INTENDED —
    it matches the GT's visible break at the top-left junction.
  - All strokes within 300x300 with ~60 px margin at sides.
"""

from PIL import Image, ImageDraw
import os
import sys

# Make G3's success_bank/code importable
ROOT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect"
BANK = os.path.join(ROOT, "groups", "G3_coords", "success_bank", "code")
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from heng import draw_heng  # noqa: E402

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_shu_zhe_inline(t, ox=0.0, oy=0.0, scale=1.0, ink=11,
                        v_height=130, h_width=180, top_y=50):
    """Inlined 竖折 with configurable horizontal length (TR5).

    Vertical goes from (ox, oy+top_y) down v_height px.
    Horizontal goes from (ox, oy+top_y-v_height) rightward h_width px.
    """
    v_top_math = (ox, oy + top_y * scale)
    v_bot_math = (ox, oy + (top_y - v_height) * scale)
    h_left_math = v_bot_math
    h_right_math = (ox + h_width * scale, oy + (top_y - v_height) * scale)

    w = max(1, int(ink * scale))

    a = _to_pixel(*v_top_math)
    b = _to_pixel(*v_bot_math)
    c = _to_pixel(*h_right_math)

    t.line([a, b], fill=(0, 0, 0), width=w)
    t.line([b, c], fill=(0, 0, 0), width=w)
    r = w // 2
    for pt in (a, b, c):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Revision (v2): match GT more closely.
    # - Top 一 is slightly wider than bottom horizontal (GT shows top spans
    #   further left+right than bottom).
    # - Vertical descender starts INSIDE the top-left corner (a few px to
    #   the right of the top 一's left endpoint, and just below its y-level),
    #   matching the small visible break in GT.
    # - Bottom horizontal slightly shorter than top; left endpoint aligned
    #   with vertical descender.

    # Stroke 1: 一 (top horizontal). scale 0.95 -> 190 px wide, at ox=+5,
    # oy=+55 math -> PIL y=95, x∈[60, 250].
    draw_heng(t, ox=5.0, oy=55.0, scale=0.95)

    # Stroke 2: 竖折 inlined. Origin at ox=-80 math (PIL x=70 — 10 px right
    # of the 一's left end at PIL x=60, giving GT's slight inside offset).
    # Vertical top starts at oy=+48 math (PIL y=102 — 7 px below the top 一
    # baseline at y=95, creating the visible break).
    # Bottom horizontal spans 165 px (slightly shorter than top's 190).
    draw_shu_zhe_inline(t, ox=-80.0, oy=0.0, scale=1.0, ink=11,
                        v_height=128, h_width=165, top_y=48)

    out = os.path.join(
        ROOT, "groups", "G3_coords", "attempts", "p2_radical_034_匸",
        "01_匸.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
