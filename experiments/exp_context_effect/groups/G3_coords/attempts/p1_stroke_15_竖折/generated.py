"""p1_stroke_15_竖折 — vertical-then-turn-right stroke.

Coordinate format (G3): origin at canvas center (150,150), math coords
(y grows UP). We render with PIL for pixel-perfect 300x300 output.

Stroke design:
  - 竖 (vertical down): from top-mid area down to a lower point.
    start = (-30, +90), end = (-30, -70)
  - small hooked corner (calligraphic pause) at the turn.
  - 折 (horizontal right): from the corner rightward.
    start = (-30, -70), end = (+70, -70)
Ink weight: ~10 px.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
CX, CY = W // 2, H // 2

# Convert math coords (origin center, y-up) to PIL pixel coords.
def m2p(x, y):
    return (CX + x, CY - y)

def draw_shuzhe(draw, ox=0, oy=0, scale=1.0, ink=10):
    # vertical segment
    v_top    = (ox + -30 * scale, oy +  90 * scale)
    v_bottom = (ox + -30 * scale, oy + -70 * scale)
    # horizontal segment (from the corner going right)
    h_left   = (ox + -30 * scale, oy + -70 * scale)
    h_right  = (ox +  70 * scale, oy + -70 * scale)

    # draw vertical
    draw.line([m2p(*v_top), m2p(*v_bottom)], fill="black",
              width=int(ink * scale))
    # draw horizontal
    draw.line([m2p(*h_left), m2p(*h_right)], fill="black",
              width=int(ink * scale))
    # round the corner + endpoints
    r = int(ink * scale) // 2
    for pt in (v_top, v_bottom, h_left, h_right):
        px, py = m2p(*pt)
        draw.ellipse([px - r, py - r, px + r, py + r], fill="black")

def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_shuzhe(draw, ox=0, oy=0, scale=1.0, ink=10)
    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_15_竖折/01_竖折.png"
    img.save(out)
    print(f"wrote {out}")

if __name__ == "__main__":
    main()
