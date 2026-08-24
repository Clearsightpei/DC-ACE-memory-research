# p3_char_0147_卅 — sà, "thirty" (4 strokes)
# Composition: three near-vertical strokes crossed by one long horizontal.
# Left stroke curves slightly leftward at the bottom (short 撇 tail),
# middle and right strokes are straight verticals extending below the crossbar.
# Crossbar sits ~40% down from the tops of the verticals.
# Thin uniform ink per MMH GT convention (P12).

from PIL import Image, ImageDraw

CANVAS = 300
OUT = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0147_卅/01_卅.png"


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)
    W = 5  # thin uniform ink to match MMH GT

    # Vertical geometry: tops at y=+70, bottoms at y=-90 (baseline), crossbar at y=+20.
    # Horizontal geometry: crossbar spans x=-95..+95.
    y_top = 70
    y_bot = -90
    y_cross = 20
    x_left_v = -60
    x_mid_v = 0
    x_right_v = 60

    # Stroke 1: left vertical/pie — straight from top down to y_cross, then curves left at bottom.
    # Render as polyline: straight segment then a slight 撇 curve.
    left_top_px = _to_pixel(x_left_v, y_top)
    left_bend_px = _to_pixel(x_left_v, -30)
    left_curve_mid_px = _to_pixel(x_left_v - 8, -60)
    left_bot_px = _to_pixel(x_left_v - 25, y_bot)
    d.line([left_top_px, left_bend_px, left_curve_mid_px, left_bot_px],
           fill=(0, 0, 0), width=W, joint="curve")

    # Stroke 2: middle vertical — straight top to bottom.
    mid_top_px = _to_pixel(x_mid_v, y_top)
    mid_bot_px = _to_pixel(x_mid_v, y_bot)
    d.line([mid_top_px, mid_bot_px], fill=(0, 0, 0), width=W)

    # Stroke 3: right vertical — straight top to bottom.
    right_top_px = _to_pixel(x_right_v, y_top)
    right_bot_px = _to_pixel(x_right_v, y_bot)
    d.line([right_top_px, right_bot_px], fill=(0, 0, 0), width=W)

    # Stroke 4: long horizontal crossbar through the three verticals.
    cross_l_px = _to_pixel(-95, y_cross)
    cross_r_px = _to_pixel(95, y_cross)
    d.line([cross_l_px, cross_r_px], fill=(0, 0, 0), width=W)

    img.save(OUT)


if __name__ == "__main__":
    main()
