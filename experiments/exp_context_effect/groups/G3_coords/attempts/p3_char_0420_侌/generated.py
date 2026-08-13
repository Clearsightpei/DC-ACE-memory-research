# BANK_DEVIATION
# skipped: (no 今 or 云 primitive in bank; hui_char is 囗+口 unrelated)
# reason: 侌 = 今 (top) + 云 (bottom) stacked; neither component exists as a
#         reusable bank primitive and the top-bottom stack proportion needs
#         fresh derivation from GT rather than warping unrelated primitives.
# fresh_component: jin_top_for_stack, yun_bottom_for_stack
#
# GT observation (侌):
#   Top half (~y 30–150) = 今: 人 cover (撇 + 捺) forming a broad tent
#     over a small ㇇/ㄱ (横折) piece.
#   Bottom half (~y 150–275) = 云: two 横 (short top, longer bottom)
#     + a small ㄥ (撇折 + 点) curl underneath the lower 横.
#   Ink is thin/uniform MMH-style (~3–4 px).

from PIL import Image, ImageDraw

W, H = 300, 300
INK = (0, 0, 0)
LW = 4  # calligraphy-like but uniform


def _line(t, p0, p1, w=LW):
    t.line([p0, p1], fill=INK, width=w)


def _polyline(t, pts, w=LW):
    for a, b in zip(pts, pts[1:]):
        t.line([a, b], fill=INK, width=w)


def draw_jin_top(t, cx=150, top_y=30, bottom_y=140):
    """今 sitting in the top half of the canvas."""
    # 人-cover: 撇 (from apex down-left) + 捺 (from apex down-right)
    apex = (cx, top_y)
    left_end = (cx - 78, bottom_y - 8)
    right_end = (cx + 82, bottom_y - 6)
    # 撇: slight curve outward (bow left)
    mid_pie = ((apex[0] + left_end[0]) / 2 - 10, (apex[1] + left_end[1]) / 2 + 6)
    _polyline(t, [apex, mid_pie, left_end], w=LW)
    # 捺: gentle curve, thicker feel toward tail
    mid_na = ((apex[0] + right_end[0]) / 2 + 8, (apex[1] + right_end[1]) / 2 + 4)
    _polyline(t, [apex, mid_na, right_end], w=LW)

    # Inner 横折 (a small ㇇): short horizontal starting under-left of apex,
    # then hooking down-right briefly. Sits inside the tent.
    hz_y = top_y + 60
    hz_x0 = cx - 30
    hz_x1 = cx + 34
    _line(t, (hz_x0, hz_y), (hz_x1, hz_y), w=LW)
    # small down-turn (折)
    _line(t, (hz_x1, hz_y), (hz_x1 - 6, hz_y + 22), w=LW)


def draw_yun_bottom(t, cx=150, top_y=185, bottom_y=280):
    """云 sitting in the bottom half: 二 + ㄥ."""
    # Upper 横 (short)
    _line(t, (cx - 30, top_y), (cx + 32, top_y), w=LW)
    # Lower 横 (longer, wider than upper)
    lh_y = top_y + 22
    _line(t, (cx - 66, lh_y), (cx + 72, lh_y), w=LW)
    # ㄥ (撇折 + 点) hanging under lower 横, roughly centered
    # 撇折: down-left slope, then horizontal-right along bottom
    p_start = (cx + 6, lh_y + 4)
    p_mid = (cx - 22, lh_y + 32)
    p_bot_left = (cx - 26, lh_y + 48)
    _polyline(t, [p_start, p_mid, p_bot_left], w=LW)
    # bottom horizontal sweep
    p_bot_right = (cx + 34, lh_y + 52)
    _polyline(t, [p_bot_left, (cx, lh_y + 54), p_bot_right], w=LW)
    # 点 (small dot) tucked at upper-right of the curl
    d0 = (cx + 18, lh_y + 14)
    d1 = (cx + 30, lh_y + 26)
    _line(t, d0, d1, w=LW + 1)


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_jin_top(t)
    draw_yun_bottom(t)
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_侌.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
