# zou_zhi_thin_pil_envelope.py — promoted from p3_char_0493_适 (B13 main PASS)
# Curator B13 (2026-08-05, position ~651).
#
# 辶 envelope (top-left dot + horizontal-fold-fold-pie zigzag + long 平捺
# base) in PIL pixel coords with MMH-thin ink. Companion to the frozen
# `zou_zhi.py` (turtle-based, calligraphic weight). This variant covers
# the thin-uniform-line render that keeps re-appearing in 辶-envelope
# PASSes across B7-B13 (过, 这, 进, 甸-inline, 适).
#
# Motivating context: 适 (辶+舌) B13 PASS. Reuse targets: 逃, 通, 追,
# 迄, 迅, 逢, 逛, 逝, 递, 造, 遇, 遂, 遍, 遥, 遣, 遭, 邂, 邈, 邃 — the
# 辶 radical is one of the largest LR-envelope families in Chinese
# script. Prior PASSes (过=0203, 这=0291, 进=0303, 甸=0290 (辶-cousin))
# each re-inlined this same envelope shape; this canonicalizes it.
#
# Why fresh (v13 BANK_DEVIATION rationale): frozen `zou_zhi.py` is
# turtle math-coord and tuned for calligraphic wider strokes; MMH GT for
# most 辶 chars is uniform thin ~4-5px, and the drawer wants an interior
# radical (吉, 舌, 甬, 前, 甫) that sits in the upper-right chamber and
# hangs above the 平捺. Mixing turtle + PIL for envelope+interior is
# fragile. This variant is the PIL-native canonical.
#
# Signature: (d, w=4, x_dot=70, x_zig_L=45, x_zig_R=95,
#             y_dot_top=75, y_zig_top=140, y_zig_bot=215,
#             na_left=35, na_right=290, na_belly_y=278, na_belly_w=10)
# Defaults render on a 300x300 canvas with the interior chamber at
# roughly x ∈ [110, 285], y ∈ [55, 235]. Adjust by moving x_zig_L/R
# for narrower/wider envelope; adjust na_belly_w for the 捺 flare.
#
# The recipe: 3-stroke 辶 envelope = 点 (top-left dot, tapered thin→thick)
# + 横折折撇 (small zigzag on the left side of the interior chamber) +
# 平捺 (long flat sweep across the bottom with a belly-bulge before the
# right-tail thin flare).

from PIL import Image, ImageDraw


def _tapered_line(d, p0, p1, w_head, w_tail, n=30, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (x, y)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def _tapered_bezier(d, p0, p1, p2, w_head, w_tail, n=48,
                     belly=None, w_belly=None, black=(0, 0, 0)):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if belly is not None and w_belly is not None:
            if u <= belly:
                w = w_head + (w_belly - w_head) * (u / belly)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly) / (1 - belly))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        cur = (bx, by)
        if prev is not None:
            d.line([prev, cur], fill=black, width=wi)
            r = w / 2.0
            d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=black)
        prev = cur


def draw_zou_zhi_thin_pil_envelope(d, w=4,
                                    x_dot=70, y_dot_top=75,
                                    x_zig_L=45, x_zig_R=95,
                                    y_zig_top=140, y_zig_bot=215,
                                    na_left=35, na_right=290,
                                    na_belly_y=278, na_belly_w=10,
                                    black=(0, 0, 0)):
    """辶 envelope in PIL pixel coords, MMH thin ink.

    Renders 3 strokes: top-left dot, left-side zigzag, long bottom 平捺.
    Interior radical is placed by caller in the upper-right chamber
    (roughly x ∈ [110, na_right-15], y ∈ [55, y_zig_bot+15]).
    """
    # S1: 点 (top-left small dot, thin→thicker)
    _tapered_bezier(d,
                    (x_dot, y_dot_top),
                    (x_dot + 9, y_dot_top + 13),
                    (x_dot + 18, y_dot_top + 27),
                    w_head=2, w_tail=w + 2, n=18, black=black)

    # S2: 横折折撇 — small zigzag on the left of the interior chamber.
    A = (x_zig_L, y_zig_top)
    B = (x_zig_R, y_zig_top - 5)
    C = (x_zig_L + 10, y_zig_top + 40)
    D_pt = (x_zig_R - 5, y_zig_bot)
    _tapered_line(d, A, B, w, w + 1, n=18, black=black)
    _tapered_bezier(d,
                    B,
                    (B[0] + 4, (B[1] + C[1]) / 2 + 2),
                    C,
                    w_head=w + 1, w_tail=w + 1, n=26, black=black)
    _tapered_bezier(d,
                    C,
                    ((C[0] + D_pt[0]) / 2 - 4, (C[1] + D_pt[1]) / 2 - 3),
                    D_pt,
                    w_head=w + 1, w_tail=2, n=26, black=black)

    # S3: 平捺 — long flat sweep with belly-bulge before thin right flare.
    _tapered_bezier(d,
                    (na_left, y_zig_bot + 30),
                    ((na_left + na_right) / 2, na_belly_y),
                    (na_right, y_zig_bot + 25),
                    w_head=3, w_tail=2, n=80,
                    belly=0.6, w_belly=na_belly_w, black=black)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zou_zhi_thin_pil_envelope(d)
    import os
    out = os.path.join(os.path.dirname(__file__),
                       "01_zou_zhi_thin_pil_envelope.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
