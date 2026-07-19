# p2_radical_108_片 — G3 attempt
# 片 (piàn), 4 strokes. Structure:
#   S1: left 竖撇 — nearly vertical from top-center, curves down-left at bottom
#   S2: short 横 — top bar starting at S1's top going right
#   S3: 竖 — right vertical, from top of right side descending, hooks slightly left at bottom
#         (per GT this is a 竖 with small tick; treat as tapered 竖 turning left tail)
#   S4: 横折 — middle horizontal bar starting from S1, turning down to meet S3's tail
#         forming a small closed pocket on the right.
#
# INLINE-FRESH per TR8: 片's strokes don't cleanly match any bank primitive at
# scale=1.0 — the 竖撇 is longer/more vertical than pie primitive; the box bars
# need specific endpoint welding. So we inline tapered-line recipes here.
#
# Coord convention (P5): center origin, +y up. _to_pixel converts to PIL.

from PIL import Image, ImageDraw
import os

CANVAS_SIZE = 300
CX = CANVAS_SIZE / 2
CY = CANVAS_SIZE / 2


def _to_pixel(ox, oy):
    return (CX + ox, CY - oy)


def tapered_line(draw, p0, p1, w0, w1, n=40):
    """Straight tapered stroke from math-coord p0 to p1, width w0->w1."""
    (x0, y0), (x1, y1) = p0, p1
    prev = None
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        px, py = _to_pixel(x, y)
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def tapered_bezier(draw, p0, p_ctrl, p1, w0, w1, n=60):
    """Quadratic bezier tapered stroke."""
    (x0, y0) = p0
    (mx, my) = p_ctrl
    (x1, y1) = p1
    prev = None
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        px, py = _to_pixel(x, y)
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_pian(draw):
    # Revision: taller/thinner character, S1 tail sweeps further down-left below the box,
    # S1 head higher, S2 top bar starts right at S1 head. Box shifted slightly right.

    # --- S1: 竖撇 (nearly vertical, then hooks down-left near bottom) ---
    # Head at (-25, +100) — high upper-left.
    # Nearly straight vertical mid-portion; curves left near tail.
    # Tail at (-75, -110) — well below box baseline.
    s1_head = (-25, 100)
    s1_ctrl = (-28, -30)   # keeps upper 2/3 near vertical
    s1_tail = (-75, -110)
    tapered_bezier(draw, s1_head, s1_ctrl, s1_tail, w0=11, w1=2, n=80)

    # --- S2: top 横 (short horizontal) starting at S1 head going right ---
    s2_left = (-24, 100)
    s2_right = (48, 95)
    tapered_line(draw, s2_left, s2_right, w0=9, w1=11, n=40)

    # --- S3: 竖 on right — from S2 right end descending to bottom-right corner ---
    s3_head = (48, 93)
    s3_tail = (46, -55)
    tapered_line(draw, s3_head, s3_tail, w0=10, w1=9, n=50)

    # --- S4: 横折 forming middle pocket bar + closing right wall + bottom seal ---
    # In 片 the "口" pocket is closed on the right side.
    # Middle horizontal from S1 shaft (x=-28, y=+20) to (+48, +20)
    s4a_left = (-28, 20)
    s4a_right = (48, 20)
    tapered_line(draw, s4a_left, s4a_right, w0=9, w1=10, n=40)
    # Corner 顿笔 blob
    px, py = _to_pixel(48, 20)
    r = 5
    draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
    # Bottom closing horizontal from S1 shaft (x=-38, y=-55) to (+46, -55)
    s4c_left = (-38, -55)
    s4c_right = (48, -55)
    tapered_line(draw, s4c_left, s4c_right, w0=9, w1=10, n=40)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_pian(draw)
    out_path = os.path.join(os.path.dirname(__file__), "01_片.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
