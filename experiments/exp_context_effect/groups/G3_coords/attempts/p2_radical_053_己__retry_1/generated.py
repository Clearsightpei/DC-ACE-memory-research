# p2_radical_053_己 (retry 1) — 己 (jǐ, "self"), 3 strokes.
#
# Prior attempt failure: the top 横折 spanned the whole width and the
# middle 横 was too far left, producing a blocky "巨"/"E" silhouette.
# Fix (from errata + sandbox note): inline fresh, keep the top 横折
# COMPACT (occupies only the upper portion), put the middle 横 short
# so it meets the top-right descender, and let the bottom 竖弯钩
# sweep as a large U with a small terminal hook.
#
# Stroke breakdown (per GT):
#   1) 横折 — top piece: short horizontal, then a modest drop.
#            Its LEFT end is the pivot the 竖弯钩 starts from.
#   2) 横   — short middle horizontal, meeting the descender of stroke 1.
#   3) 竖弯钩 — from the top-left, straight down the left side,
#              sweeping right along the bottom, tiny hook up.
#
# TR6/TR8: inline fresh — no primitive matches this composition
# (short top cap, short middle bar, large sweeping U-bowl).
#
# Coords: math convention, +y up, canvas center = (0,0), size 300.

import math
from PIL import Image, ImageDraw

CANVAS_SIZE = 300
INK = (0, 0, 0)


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _line(t, p0, p1, w):
    a = _to_pixel(*p0)
    b = _to_pixel(*p1)
    t.line([a, b], fill=INK, width=w)


def _blob(t, p, r):
    x, y = _to_pixel(*p)
    t.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def _polyline(t, pts, w):
    for i in range(len(pts) - 1):
        _line(t, pts[i], pts[i + 1], w)


def draw_ji(t):
    ink = 7

    # ---- Stroke 1: 横折 (top cap) ----
    # Wider top horizontal, short descender.
    s1_h_start = (-55, 65)
    s1_corner  = (+45, 62)
    s1_v_end   = (+45, 25)
    _line(t, s1_h_start, s1_corner, ink)
    _line(t, s1_corner,  s1_v_end,  ink)
    _blob(t, s1_corner, ink // 2 + 1)  # 顿笔 at corner

    # ---- Stroke 2: 横 (middle short horizontal) ----
    # Sits at mid-height, meeting s1's descender end.
    s2_h_start = (-45, 20)
    s2_h_end   = (+45, 20)
    _line(t, s2_h_start, s2_h_end, ink)

    # ---- Stroke 3: 竖弯钩 (big U bowl with terminal hook) ----
    # Shaft: welded to stroke-1's left start at (-55, +65),
    # descends slightly left-leaning to (-60, -30).
    shaft_top = (-55, 65)
    shaft_bot = (-60, -30)
    _line(t, shaft_top, shaft_bot, ink)

    # Quarter-arc: sweep from (-60,-30) around to (-10, -75).
    # Center at (-10, -30), radius 50. Angles: 180° -> 270°.
    arc_cx, arc_cy = -10, -30
    r = 50
    n_arc = 28
    prev = None
    for i in range(n_arc + 1):
        u = i / n_arc
        angle = math.pi + u * (math.pi / 2)
        px = arc_cx + r * math.cos(angle)
        py = arc_cy + r * math.sin(angle)
        curr = (px, py)
        if prev is not None:
            _line(t, prev, curr, ink)
        prev = curr

    # Tail: from arc end (-10, -80) rightward and slightly up to (+70, -72).
    tail_start = (-10, -80)
    tail_end   = (+70, -72)
    _line(t, tail_start, tail_end, ink)

    # Small terminal hook: up and slightly left, tapered.
    hook_base = tail_end
    hook_tip  = (+62, -48)
    n_seg = 6
    for i in range(n_seg):
        u0 = i / n_seg
        u1 = (i + 1) / n_seg
        p0 = (hook_base[0] + u0 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u0 * (hook_tip[1] - hook_base[1]))
        p1 = (hook_base[0] + u1 * (hook_tip[0] - hook_base[0]),
              hook_base[1] + u1 * (hook_tip[1] - hook_base[1]))
        w = max(1, int(round((ink - 2) * (1 - (u0 + u1) / 2) + 2)))
        _line(t, p0, p1, w)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ji(t)
    out_path = __file__.rsplit("/", 1)[0] + "/01_己.png"
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
