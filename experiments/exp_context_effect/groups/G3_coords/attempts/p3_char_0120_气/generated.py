# p3_char_0120_气 (qì, "air/gas") — 4 strokes:
#   1) 撇 (short pie, top-left)
#   2) 横 (top short heng)
#   3) 横 (middle longer heng)
#   4) 横折弯钩 (envelope hook: heng-turn-curve-hook, from top-right sweeping
#      down-left then back to lower-right with an upward flick hook)
#
# GT shows thin, uniform-width MMH strokes. Draw with PIL primitives.

from PIL import Image, ImageDraw

CANVAS = 300
WIDTH_MAIN = 6       # thin, MMH-style
WIDTH_HOOK = 6


def _mx(ox):
    return CANVAS / 2 + ox


def _my(oy):
    return CANVAS / 2 - oy


def draw_qi_gas(t, ox=0, oy=0, scale=1.0):
    def M(x, y):
        return (_mx(ox + x * scale), _my(oy + y * scale))

    # 1) 撇 — short pie top-left, from upper area sloping down-left.
    #    starts near (- 20, +60), ends near (- 78, +20)
    p1_a = M(-25, 70)
    p1_b = M(-80, 25)
    t.line([p1_a, p1_b], fill=(0, 0, 0), width=WIDTH_MAIN)

    # 2) 横 — top short heng, from about (-30, +55) to (+55, +45)
    p2_a = M(-30, 55)
    p2_b = M(60, 42)
    t.line([p2_a, p2_b], fill=(0, 0, 0), width=WIDTH_MAIN)

    # 3) 横 — middle heng, longer, from (-75, +8) to (+65, -2)
    p3_a = M(-78, 8)
    p3_b = M(68, -4)
    t.line([p3_a, p3_b], fill=(0, 0, 0), width=WIDTH_MAIN)

    # 4) 横折弯钩 — starts at right end of middle heng, small heng continues,
    #    turns down, sweeps left and down along the bottom envelope,
    #    ends with a small upward hook flick.
    # Path polyline sampled from GT (looking at bottom envelope curve):
    path = [
        (55, -4),     # continues from middle-heng right end (very small heng)
        (72, -8),
        (75, -35),    # turn corner, go down
        (68, -70),    # begin curving
        (48, -100),   # sweep down-left
        (10, -118),   # bottom
        (-25, -115),  # bottom-left
        (-20, -95),   # hook flick upward
    ]
    pts = [M(x, y) for (x, y) in path]
    t.line(pts, fill=(0, 0, 0), width=WIDTH_HOOK, joint="curve")


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_qi_gas(draw, ox=0, oy=0, scale=1.0)
    out = __file__.rsplit("/", 1)[0] + "/01_气.png"
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
