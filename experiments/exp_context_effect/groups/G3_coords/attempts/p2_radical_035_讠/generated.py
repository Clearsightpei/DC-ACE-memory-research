# p2_radical_035_讠 — 讠 (yán radical, 2 strokes).
#
# Structure (from GT viewing):
#   Stroke 1: 点 — small diagonal dot at top-center, slightly left.
#   Stroke 2: 横折提 — compact form: short flat 横 top-left, dropping 折
#             mostly vertical, ending in a rising 提 tick to the right.
#
# TR1/TR6: every primitive call is a deliberate placement.
# TR2: this is a standalone radical (no full character host), so we
#      center it in the canvas, at scale ~0.85 for radical form.
# TR3: math-coord center is (150,150) in PIL. +y = up.
# TR4: joints — the 点 is disconnected from the body (visible gap in GT).
#      The heng_zhe_ti's internal joints are baked into the primitive.
# TR5: for the 点, standalone dian primitive is a bit heavy for a radical
#      dot at top of 讠. Use dian_radical (already bank-tuned for radical
#      form: slimmer, PASSed at position 40 as 丶).
#
# Placement plan (math coords, +y up):
#   点 (dian_radical): target center ≈ (-40, +60) — upper-left of canvas.
#     ox = -40, oy = +60, scale ~ 0.55 (small dot).
#   横折提 (heng_zhe_ti): compact, centered below the dot.
#     Standalone primitive spans roughly x [-90..+108], y [-18..+58].
#     For 讠 radical we want a smaller, more upright form:
#       - horizontal top short (~60 px wide)
#       - vertical drop long (~90 px)
#       - tick moderate
#     scale = 0.60 will shrink the whole compound.
#     ox = -30, oy = -20 places it below and slightly left of dot.

import sys, os
from PIL import Image, ImageDraw

# Bank primitives — add path
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from dian_radical import draw_dian_radical  # noqa: E402


def _to_pixel(ox, oy):
    """Math coord (center origin, +y up) → PIL pixel."""
    return 150 + ox, 150 - oy


def _stroke_line(t, p0, p1, w0, w1, steps=60):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_heng_zhe_ti_compact(t, ox=0, oy=0):
    """讠's body: compact 横折提 (per TR5 inline; standalone primitive
    was too wide-and-shallow for the radical form)."""
    # Endpoints in math coords (+y up), relative to (ox, oy):
    #   heng:    A=(-30, +45) → B=(+30, +50)   — short, slight upward tilt
    #   corner blob at B
    #   zhe:     C=(+30, +50) → D=(+22, -45)   — long vertical, slight in-lean
    #   ti:      D=(+22, -45) → E=(+55, -25)   — rising tick to right
    heng_a = _to_pixel(ox - 30, oy + 45)
    heng_b = _to_pixel(ox + 30, oy + 50)
    _stroke_line(t, heng_a, heng_b, 8, 10, steps=60)

    # 顿笔 corner blob
    dun = _to_pixel(ox + 30, oy + 50)
    r = 7
    t.ellipse([dun[0] - r, dun[1] - r, dun[0] + r, dun[1] + r], fill=(0, 0, 0))

    # 折 vertical drop
    zhe_a = _to_pixel(ox + 32, oy + 52)
    zhe_b = _to_pixel(ox + 20, oy - 45)
    _stroke_line(t, zhe_a, zhe_b, 11, 8, steps=80)

    # 提 rising tick
    ti_a = _to_pixel(ox + 20, oy - 45)
    ti_b = _to_pixel(ox + 55, oy - 25)
    _stroke_line(t, ti_a, ti_b, 10, 2, steps=60)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # --- Stroke 1: 点 (top dot) ---
    # Target center pixel ≈ (110, 88) → math (-40, +62).
    draw_dian_radical(t, ox=-40, oy=+62, scale=0.55)

    # --- Stroke 2: 横折提 (compact body, inlined per TR5) ---
    # Body center chosen at math (-5, -5) so heng sits around y=100..105
    # PIL and the tail lands near y=200 PIL — matches GT proportions.
    draw_heng_zhe_ti_compact(t, ox=-5, oy=-5)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_讠.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
