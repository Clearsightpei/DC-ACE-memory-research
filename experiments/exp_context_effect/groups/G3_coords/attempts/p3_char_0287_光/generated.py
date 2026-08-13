# p3_char_0287_光 — G3 attempt
# 光 = top (⺌: 竖 + 左点 + 右短撇) + 一 (heng) + 儿 (er_ren: 撇 + 竖弯钩).
# 6 strokes. GT shows thin uniform ink (MMH). Per xiong_char lesson + v8
# trust-GT posture: inline PIL thin ink rather than calligraphic bank
# primitives which come out too heavy for the MMH GT.

from PIL import Image, ImageDraw

CANVAS = 300
INK = 5  # thin, MMH-like
CX = CY = CANVAS / 2


def M(x, y):
    """Math coords (center origin, y up) -> pixel coords."""
    return (CX + x, CY - y)


def line(d, p1, p2, w=INK):
    d.line([M(*p1), M(*p2)], fill=(0, 0, 0), width=w)
    for (x, y) in (p1, p2):
        px, py = M(x, y)
        r = w / 2
        d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def poly(d, pts, w=INK):
    px_pts = [M(*p) for p in pts]
    d.line(px_pts, fill=(0, 0, 0), width=w, joint="curve")
    for (x, y) in (pts[0], pts[-1]):
        px, py = M(x, y)
        r = w / 2
        d.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def draw_guang(d):
    # ---- Top ⺌ block (y +115 .. +55) ----
    # Stroke 1: 竖 (short vertical stem, center)
    line(d, (0, 110), (0, 60))
    # Stroke 2: 左点 (dot, upper-left, slanting down-right toward center)
    line(d, (-38, 108), (-20, 70))
    # Stroke 3: 右短撇 (short pie, upper-right, slanting down-left toward center)
    line(d, (38, 108), (20, 70))

    # ---- Stroke 4: 一 heng (long horizontal, slight upward tilt) ----
    line(d, (-105, 35), (105, 42))

    # ---- Stroke 5: 撇 left leg (long pie curving down-left) ----
    poly(d, [(-15, 35), (-30, 0), (-55, -50), (-85, -110), (-100, -130)])

    # ---- Stroke 6: 竖弯钩 right leg (down then curve right + hook up) ----
    poly(d, [
        (25, 35),
        (25, -30),
        (28, -75),
        (45, -110),
        (75, -125),
        (105, -125),
        # small hook tick up
        (105, -105),
    ])


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    draw_guang(d)
    img.save("01_光.png")


if __name__ == "__main__":
    main()
