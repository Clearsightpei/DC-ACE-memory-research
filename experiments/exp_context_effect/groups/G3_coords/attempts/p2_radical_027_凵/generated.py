# p2_radical_027_凵 (kan) — G3 coord attempt.
#
# 凵 is a 2-stroke enclosing radical (open at top).
#   Stroke 1: 竖折 (shu_zhe) — vertical descends from upper-left, turns
#             right at the bottom into a horizontal that spans across.
#   Stroke 2: 竖 (shu) — a short vertical on the right, descending from
#             upper-right down to meet the horizontal's right end.
#
# TR6 explicit transforms (math coords, +y up, canvas center origin):
#   Target silhouette (from GT): U-shape occupying lower-middle canvas.
#   - Left vertical: from (-60, +30) down to (-60, -60), then horizontal
#     to (+60, -60). So bank shu_zhe primitive (v_top y=+90, v_bottom y=-70,
#     h_right x=+70 at scale=1) needs squaring:
#       want v_top math y ≈ +30, v_bottom/h_left math y ≈ -60,
#       h_right math x ≈ +60, h_left/v math x ≈ -60.
#     Standalone shu_zhe: v_top=(-30,+90), v_bottom=(-30,-70),
#       h_right=(+70,-70). Its width span=100px, height span=160px.
#     Target span: width 120px, height 90px — proportions different, so
#     INLINE per TR5 rather than distort scale asymmetrically.
#   - Right vertical: from (+60, +30) down to (+60, -60). This is a short
#     shu; bank shu default length 200 → we want length ~90, i.e.
#     scale ≈ 0.45. That's below TR5's 0.4 threshold-ish, so INLINE too
#     to keep taper honest.
#
# Both strokes inlined for consistent thickness ~10 px.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300
INK = 10


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_kan(t):
    # Stroke 1: 竖折 (shu_zhe) — vertical + right-turn horizontal.
    # Revised: enlarge (span 160w x 130h) and shift down so U sits in
    # the lower half of the canvas, matching GT proportions.
    v_top = (-80, 10)      # upper-left start
    v_bot = (-80, -80)     # corner
    h_left = (-80, -80)    # corner (same as v_bot, weld)
    h_right = (80, -80)    # bottom-right end of the horizontal

    w = INK
    t.line([_to_pixel(*v_top), _to_pixel(*v_bot)],
           fill=(0, 0, 0), width=w)
    t.line([_to_pixel(*h_left), _to_pixel(*h_right)],
           fill=(0, 0, 0), width=w)
    # 顿笔 blobs at corner and endpoints for calligraphic feel (P6).
    r = w // 2
    for pt in (v_top, v_bot, h_right):
        px, py = _to_pixel(*pt)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))

    # Stroke 2: right 竖 — short vertical, top slightly HIGHER than left
    # top (the GT shows the right stroke starting a touch above the left
    # stroke top, both ends near the horizontal).
    s2_top = (80, 15)
    s2_bot = (80, -80)   # meets horizontal right end (weld)
    t.line([_to_pixel(*s2_top), _to_pixel(*s2_bot)],
           fill=(0, 0, 0), width=w)
    for pt in (s2_top, s2_bot):
        px, py = _to_pixel(*pt)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_kan(draw)
    out = __file__.rsplit("/", 1)[0] + "/01_凵.png"
    img.save(out)


if __name__ == "__main__":
    main()
