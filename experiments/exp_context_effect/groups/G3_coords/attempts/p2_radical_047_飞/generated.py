# p2_radical_047_飞 — G3 coord-bank drawer
#
# 飞 (fēi) — 3 strokes (radical form):
#   1) 横折弯钩 (heng-zhe-wan-gou): long horizontal top, sharp turn down,
#      then swept curve down-and-right forming a rounded envelope, ending
#      in a small hook up.
#   2) 撇 (pie): short diagonal in the middle interior.
#   3) 点 (dian): a dot below/right of the pie, inside the envelope.
#
# Bank-fit analysis (TR1-TR7):
#   - Stroke 1 has no matching primitive: yi_radical.py (乙) is the
#     closest analog (a continuous 横折弯钩 sweep), but 飞's shape is
#     distinctly different — the horizontal is longer at top, the
#     descending curve is more of a leftward-sweeping bow, and the
#     hook is at the bottom RIGHT (not top-right like 乙). Per TR5,
#     stretching yi_radical with extreme (ox, oy, scale) would ruin
#     its proportions. INLINE stroke 1 as a piecewise path with
#     tapered widths (analogous to yi_radical's storage form).
#   - Stroke 2 (撇): could reuse draw_pie but 飞's interior pie is
#     short and steep — inline a small tapered segment instead
#     (scale < 0.4 rule per TR5).
#   - Stroke 3 (点): reuse draw_dian with small scale placed at
#     interior-lower position.
#
# Canvas: 300x300, PIL, math-coord for stroke 3 only (via dian primitive);
# strokes 1 & 2 in raw PIL pixels for direct GT alignment.

from PIL import Image, ImageDraw
import sys, os

# Add bank code path so we can import draw_dian
BANK = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/success_bank/code"
if BANK not in sys.path:
    sys.path.insert(0, BANK)

from dian import draw_dian


def stamp(t, x, y, r):
    t.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def draw_tapered_path(t, path, widths, steps=60):
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
    # Stroke 1: 横折弯钩 — continuous sweep.
    # Anatomy in PIL pixels (y grows down):
    #   Head: ~ (60, 118) — thin start on the left of the horizontal top.
    #   Horizontal segment rightward to ~ (168, 118).
    #   Sharp fold (顿笔) turning down and slightly right: (172, 128).
    #   Then swept curve descending down-left then curving right along
    #   the bottom of the envelope: through (155, 165), (135, 200),
    #   (125, 230), (135, 252), (160, 260), (190, 258).
    #   Small hook flick up-left at the tail: (198, 245).
    # Path descends down-LEFT from the fold (bowl-shaped envelope),
    # rounds along the bottom, and terminates at the bottom-right with
    # a tiny upward hook flick.
    path1 = [
        (55, 128),   # thin head at top-left of horizontal
        (95, 122),
        (135, 120),
        (162, 122),  # end of horizontal
        (168, 132),  # 顿笔 fold corner (short downward tick)
        (160, 152),  # start of downward-left sweep
        (140, 180),
        (120, 215),
        (110, 240),
        (115, 258),
        (140, 268),
        (175, 265),
        (198, 258),  # bottom-right of envelope
        (205, 248),  # hook tip (small up-left flick)
    ]
    widths1 = [
        3.0,
        7.0,
        9.5,
        10.5,
        11.0,   # corner blob (顿笔)
        9.5,
        8.5,
        8.0,
        8.0,
        8.5,
        9.0,
        8.5,
        6.5,
        2.0,    # hook tapers to point
    ]
    draw_tapered_path(t, path1, widths1, steps=80)
    # Corner 顿笔 blob at the fold
    stamp(t, 168, 130, 6.5)
    # Head cap
    stamp(t, 55, 128, 2.0)

    # Stroke 2: 撇 (short interior pie).
    # Located high-inside the envelope, roughly under the top horizontal's
    # right portion, sweeping down-left. In GT it starts around (160, 155)
    # and tails to about (135, 195).
    path2 = [(162, 148), (152, 168), (142, 188), (132, 205)]
    widths2 = [8.0, 6.0, 3.5, 1.5]
    draw_tapered_path(t, path2, widths2, steps=50)
    stamp(t, 162, 148, 4.0)  # head blob

    # Stroke 3: 点 (dot) — small, placed just right of the pie tail,
    # inside the envelope. Target center PIL ~(175, 195).
    # Math coords: ox_math = 175 - 150 = +25, oy_math = 150 - 195 = -45.
    draw_dian(t, ox=25, oy=-45, scale=0.5)


def main():
    W = H = 300
    img = Image.new("RGB", (W, H), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_fei(t)
    out_dir = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_047_飞"
    out_path = os.path.join(out_dir, "01_飞.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
