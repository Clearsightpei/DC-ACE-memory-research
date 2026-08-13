# p3_char_0318_伽 — 7 strokes: 亻 (2) + 力 (2) + 口 (3)
# L-M-R composition. Following G3 v8 posture: inline PIL, trust GT.
# Reference recipe: ban_char.py (力) for tapered lines + men_plural
# L-R pattern. Revised pass 2: make 力 pie clearly visible / crossing,
# tighten 亻 vertical extent, align three columns at similar y-band.

from PIL import Image, ImageDraw
import os

CANVAS = 300


def _tapered_line(D, p0, p1, w0, w1, steps=28):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def _tapered_bezier(D, p0, p1, p2, w0, w1, steps=48):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = max(1, int(round(w0 + (w1 - w0) * u)))
        if prev is not None:
            D.line([prev, (bx, by)], fill=(0, 0, 0), width=w)
            r = w / 2.0
            D.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def draw_jia(D):
    W = 4  # thin ink per P12

    # ---- 亻 (left column, x ~ 30..80) ----
    # Stroke 1: 撇 — short sweep from top-right down-left
    _tapered_bezier(D, (70, 85), (55, 145), (35, 195), W + 2, 1, steps=45)
    # Stroke 2: 竖 — longer vertical shaft touching pie's mid, descends deep
    _tapered_line(D, (75, 135), (75, 275), W, W, steps=34)

    # ---- 力 (middle column, x ~ 100..190) ----
    # Stroke 3: 横折钩 — 横 across top → 折 down → small 钩 up-left
    hzg_top_l = (110, 110)
    hzg_corner = (185, 105)
    hzg_bot = (183, 230)
    _tapered_line(D, hzg_top_l, hzg_corner, W, W + 1, 24)
    _tapered_line(D, hzg_corner, hzg_bot, W + 1, W, 32)
    hook_end = (163, 218)
    _tapered_line(D, hzg_bot, hook_end, W, max(1, W - 1), 12)

    # Stroke 4: 撇 — from above 横 (LEFT third) crossing it, sweeping
    # down-LEFT with clear leftward bow. Must be visibly distinct from
    # 亻's shu (different x range).
    _tapered_bezier(D, (128, 88), (105, 175), (90, 260),
                    W + 2, 1, steps=60)

    # ---- 口 (right column, x ~ 205..265) ----
    box_l, box_r = 208, 265
    box_t, box_b = 155, 230
    # Stroke 5: 竖 (left vertical)
    _tapered_line(D, (box_l, box_t + 3), (box_l, box_b), W, W, 20)
    # Stroke 6: 横折 — top heng into right shu
    _tapered_line(D, (box_l - 2, box_t), (box_r, box_t), W, W + 1, 22)
    _tapered_line(D, (box_r, box_t), (box_r, box_b), W + 1, W, 22)
    # Stroke 7: 横 (bottom heng)
    _tapered_line(D, (box_l - 2, box_b), (box_r + 2, box_b), W, W, 22)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    D = ImageDraw.Draw(img)
    draw_jia(D)
    out_path = os.path.join(os.path.dirname(__file__), "01_伽.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
