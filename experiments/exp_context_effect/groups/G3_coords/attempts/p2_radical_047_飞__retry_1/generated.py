# p2_radical_047_飞 — G3 coord-bank drawer, retry_1
#
# Prior attempt (retry_0) failed: main envelope was too "乙"-like (too
# tightly enclosed), the bottom sweep went too far left and the base
# curved back up in a bowl shape. GT actually shows a more OPEN envelope:
# a long, slightly bowed top-horizontal that turns down at the right and
# sweeps down-and-slightly-left into a curve; the tail terminates with a
# small hook up. The right side is open (not a closed bowl).
#
# Anatomy from GT:
#   Stroke 1 (横斜钩 / 横折弯钩 hybrid): starts thin at (~65, 130), runs
#     right along a nearly-horizontal top (slight downward bow) to
#     (~180, 140), then bends down-left through the interior, sweeps
#     along a broad curve to lower area, ending with tiny upward hook.
#     The GT's envelope opens on the right — after the bottom curve it
#     doesn't return up as a "乙" bowl; it just terminates.
#   Stroke 2 (撇): short interior diagonal from ~(175, 138) down-left to
#     ~(150, 175). This 撇 originates from the fold and heads down-left.
#   Stroke 3 (点): small dot at ~(180, 168), interior-right of the pie.
#
# Fix from retry_0: shorten the main sweep so it doesn't wrap back left;
# make it a single arc ending mid-lower with a small hook; tighten the
# pie; make the dian smaller and place it correctly.

from PIL import Image, ImageDraw
import sys, os

BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)


def stamp(t, x, y, r):
    t.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def draw_tapered_path(t, path, widths, steps=80):
    """Draw a piecewise path with per-vertex width, stamping circles."""
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        for s in range(steps + 1):
            u = s / steps
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            w = w0 + (w1 - w0) * u
            stamp(t, x, y, w / 2.0)


def draw_fei(t):
    # Stroke 1: main 横折弯钩 envelope.
    # Thin start at upper-left, gradual thickening along the horizontal,
    # 顿笔 at the fold (~185, 140), then curve down and slightly left,
    # then arc through the bottom middle, terminating with tiny hook.
    # Does NOT wrap back up (unlike a closed 乙 bowl).
    path1 = [
        (55, 132),   # thin head, top-left
        (95, 128),
        (135, 128),
        (170, 132),
        (185, 140),  # 顿笔 fold corner
        (180, 160),  # start of downward sweep
        (170, 185),
        (155, 210),
        (140, 232),
        (135, 250),  # bottom of arc
        (145, 258),  # tiny hook base
        (158, 250),  # hook tip flicking up-right
    ]
    widths1 = [
        3.0,
        6.5,
        8.5,
        9.5,
        10.0,   # corner blob
        9.0,
        8.5,
        8.0,
        7.5,
        7.0,
        5.5,
        2.0,    # hook tapers to point
    ]
    draw_tapered_path(t, path1, widths1, steps=90)
    # Corner 顿笔 blob at fold
    stamp(t, 185, 140, 5.5)

    # Stroke 2: 撇 — short interior diagonal starting near the fold,
    # heading down-left. In GT it originates just below where the fold
    # is and terminates in the interior mid-lower area.
    path2 = [
        (185, 148),
        (175, 165),
        (162, 182),
        (150, 200),
    ]
    widths2 = [7.0, 5.5, 3.5, 1.5]
    draw_tapered_path(t, path2, widths2, steps=60)
    stamp(t, 185, 148, 3.5)  # head blob

    # Stroke 3: 点 — small tick/dot on the right side, below and slightly
    # right of the pie tail. GT shows a compact dot around (190, 175).
    path3 = [(188, 170), (200, 182)]
    widths3 = [3.5, 6.5]
    draw_tapered_path(t, path3, widths3, steps=40)
    stamp(t, 200, 183, 3.5)  # tail cap


def main():
    W = H = 300
    img = Image.new("RGB", (W, H), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_fei(t)
    out_dir = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_047_飞__retry_1"
    out_path = os.path.join(out_dir, "01_飞.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
