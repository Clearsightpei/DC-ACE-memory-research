# p3_char_0079_已 — 已 (yǐ, "already"), 3 strokes.
# Structure (from GT inspection):
#   1) 横折 top-right: horizontal from mid-left to right, turn down a short vertical.
#      The horizontal does NOT reach the left edge — leaves a gap on the left
#      (this is what distinguishes 已 from 巳: gap open on left).
#   2) short 横 middle: crosses through, meeting the left edge of the envelope.
#   3) 竖弯钩 envelope: left vertical descending, curving right along the bottom,
#      then a small upward hook.
#
# Uses inlined PIL like jie_radical.py — 已 has a specific composition
# (short 横折 + through-中 + 竖弯钩) that doesn't map to any bank primitive
# cleanly at the required proportions. Drawn fresh from GT observation.

import math
from PIL import Image, ImageDraw

CANVAS = 300
OUT = "01_已.png"


def _p(x, y):
    """Math coords (origin at center, y up) -> pixel coords."""
    return (CANVAS / 2 + x, CANVAS / 2 - y)


def draw_yi3(d, ox=0.0, oy=0.0, scale=1.0):
    """Draw 已.

    Coord layout (math, before ox/oy/scale):
      envelope left-vertical top: (-55, 55)
      envelope corner-bottom-left: (-55, -60)
      envelope curve center: (-15, -60), radius 40
      envelope tail-right end: (-15, -100) then horizontal? No —
       actually 竖弯钩: shaft down, curve right, then horizontal tail.
      Rework: shaft goes from (-55, 55) down to (-55, -60), arc quarter to
       (-15, -100), then tail horizontally to (55, -100), then hook up-left
       to (48, -75).
      Top 横折: h_start (-25, 65) -> h_corner (35, 65) -> v_end (35, 20).
      Middle 横: from (-55, 10) to (35, 10) — connects left env to top's vertical.
    """
    ink = max(1, int(round(9 * scale)))

    # ---- Stroke 3 (drawn first for stacking) — 竖弯钩 envelope ----
    # Shaft
    a = _p(ox + -55 * scale, oy + 55 * scale)
    b = _p(ox + -55 * scale, oy + -60 * scale)
    d.line([a, b], fill=(0, 0, 0), width=ink)

    # Quarter arc from (-55, -60) sweeping to (-15, -100) via center (-15, -60), r=40
    arc_cx = ox + -15 * scale
    arc_cy = oy + -60 * scale
    r = 40 * scale
    n_arc = 16
    prev = None
    for i in range(n_arc + 1):
        u = i / n_arc
        angle = math.pi + u * (math.pi / 2)  # 180° -> 270°
        px = arc_cx + r * math.cos(angle)
        py = arc_cy + r * math.sin(angle)
        curr = _p(px, py)
        if prev is not None:
            d.line([prev, curr], fill=(0, 0, 0), width=ink)
        prev = curr

    # Tail horizontal from (-15, -100) to (55, -100)
    ta = _p(ox + -15 * scale, oy + -100 * scale)
    tb = _p(ox + 55 * scale, oy + -100 * scale)
    d.line([ta, tb], fill=(0, 0, 0), width=ink)

    # Upward hook — tapered up-and-left
    hook_base = (ox + 55 * scale, oy + -100 * scale)
    hook_tip = (ox + 48 * scale, oy + -72 * scale)
    n_seg = 10
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(1, int(round((ink - 2) * (1 - (u0 + u1) / 2) + 2)))
        pa = _p(*p0)
        pb = _p(*p1)
        d.line([pa, pb], fill=(0, 0, 0), width=w)

    # ---- Stroke 1 — 横折 top ----
    # horizontal from (-25, 65) to (35, 65)
    h1 = _p(ox + -25 * scale, oy + 65 * scale)
    h2 = _p(ox + 35 * scale, oy + 65 * scale)
    d.line([h1, h2], fill=(0, 0, 0), width=ink)
    # vertical from (35, 65) down to (35, 20)
    v1 = h2
    v2 = _p(ox + 35 * scale, oy + 20 * scale)
    d.line([v1, v2], fill=(0, 0, 0), width=ink)

    # small corner dot at (35, 65)
    cr = ink // 2
    d.ellipse([h2[0] - cr, h2[1] - cr, h2[0] + cr, h2[1] + cr], fill=(0, 0, 0))

    # ---- Stroke 2 — middle 横 ----
    # from (-55, 10) to (35, 10) — spans left envelope to below top's vertical
    m1 = _p(ox + -55 * scale, oy + 10 * scale)
    m2 = _p(ox + 35 * scale, oy + 10 * scale)
    d.line([m1, m2], fill=(0, 0, 0), width=ink)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_yi3(d, ox=0, oy=-5, scale=1.15)
    img.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
