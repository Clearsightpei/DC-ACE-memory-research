# p2_radical_053_己 — 己 (ji, "self"), 3 strokes.
#
# Stroke breakdown per GT:
#   1) 横折 — short horizontal at the top-left, turning down at right end.
#   2) 横   — short horizontal in the middle, starting at the left edge,
#             ending short of the descender (this gap distinguishes 己 from 已).
#   3) 竖弯钩 — starts at top-left (welded to stroke-1 start), descends,
#              curves right along the bottom, ending in a small hook up.
#
# Layout (math coords, +y up, center=0):
#   Stroke 1 (横折): from (-45, +55) to (+45, +55) then down to (+45, +18)
#   Stroke 2 (横):   from (-45, +18) to (+18, +18)   -- ends WELL before right side
#   Stroke 3 (竖弯钩): shaft from (-45, +55) down to (-45, -55), quarter-arc
#                       right, tail y=-70 to (+55, -70), tiny hook up-left to (+48, -55).
#
# TR6: bank primitives are NOT invoked; the composition needs precise
# shared start-points and specific segment lengths that don't match any
# standalone primitive's (ox, oy, scale) recipe (e.g. stroke-3's shaft is
# taller than shu_wan_gou's canonical 100 px, and stroke-1 needs a short
# 90-px horizontal head not the 200-px heng primitive). Per TR5 the
# safest path is to inline the recipe.

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


def draw_ji(t):
    ink = 10

    # ---- Stroke 1: 横折 (top-right corner) ----
    # Wider, shorter drop — matches GT's compact top-right shoulder.
    s1_h_start = (-55, 60)
    s1_corner  = (+55, 60)
    s1_v_end   = (+55, 30)
    _line(t, s1_h_start, s1_corner, ink)
    _line(t, s1_corner,  s1_v_end,  ink)
    _blob(t, s1_corner, ink // 2 + 1)   # 顿笔 at corner (P6)

    # ---- Stroke 2: 横 (middle short horizontal) ----
    # Starts a bit right of stroke-3's shaft-top area, ends short of
    # the right descender's projection (this gap = 己 not 已).
    s2_h_start = (-55, 5)
    s2_h_end   = (+20, 5)
    _line(t, s2_h_start, s2_h_end, ink)

    # ---- Stroke 3: 竖弯钩 (bottom, opens right) ----
    # Shaft: welded to stroke-1's left start, descends left side.
    shaft_top = (-55, 60)
    shaft_bot = (-55, -35)
    _line(t, shaft_top, shaft_bot, ink)

    # Quarter-arc: rounded bottom-left corner. Radius bigger for a
    # softer, more calligraphic curl (GT's bottom is a smooth sweep).
    import math
    arc_cx, arc_cy = -20, -35
    r = 35
    n_arc = 20
    prev = None
    for i in range(n_arc + 1):
        u = i / n_arc
        angle = math.pi + u * (math.pi / 2)  # 180° -> 270°
        px = arc_cx + r * math.cos(angle)
        py = arc_cy + r * math.sin(angle)
        curr = (px, py)
        if prev is not None:
            _line(t, prev, curr, ink)
        prev = curr

    # Tail: horizontal from arc end (-20,-70) rightward to +65
    tail_start = (-20, -70)
    tail_end   = (+65, -70)
    _line(t, tail_start, tail_end, ink)

    # Small hook: up-and-left, tapered per P1.
    hook_base = tail_end
    hook_tip  = (+58, -52)
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
