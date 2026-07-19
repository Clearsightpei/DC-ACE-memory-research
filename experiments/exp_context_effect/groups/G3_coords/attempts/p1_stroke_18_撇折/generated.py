"""p1_stroke_18_撇折 — pie-then-turn-right stroke (撇折).

Description: 撇然后转向右横 — a leftward-downward pie, then turns and
goes right as a horizontal (横).

Coordinate format (G3): origin at canvas center (150,150), math coords
(y grows UP). Rendered with PIL for pixel-perfect 300x300 output.

Stroke design:
  - 撇 segment: diagonal from upper-right down-left to a low point.
      start = (+40, +80),  end = (-40, -50)
  - 折/横 segment: from the pie's terminus, turns right and runs
    horizontally to the right side.
      start = (-40, -50),  end = (+60, -50)
Ink weight: ~10 px. Corners rounded via endpoint ellipses.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
CX, CY = W // 2, H // 2

# Convert math coords (origin center, y-up) to PIL pixel coords.
def m2p(x, y):
    return (CX + x, CY - y)

def draw_piezhe(draw, ox=0, oy=0, scale=1.0, ink=10):
    # pie: diagonal down-left
    p_top    = (ox +  40 * scale, oy +  80 * scale)
    p_bot    = (ox + -40 * scale, oy + -50 * scale)
    # heng: horizontal right, starting from pie's terminus
    h_left   = (ox + -40 * scale, oy + -50 * scale)
    h_right  = (ox +  60 * scale, oy + -50 * scale)

    w = max(1, int(ink * scale))

    # draw pie (diagonal)
    draw.line([m2p(*p_top), m2p(*p_bot)], fill="black", width=w)
    # draw heng (horizontal)
    draw.line([m2p(*h_left), m2p(*h_right)], fill="black", width=w)

    # round endpoints + the corner
    r = w // 2
    for pt in (p_top, p_bot, h_left, h_right):
        px, py = m2p(*pt)
        draw.ellipse([px - r, py - r, px + r, py + r], fill="black")

def main():
    img = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(img)
    draw_piezhe(draw, ox=0, oy=0, scale=1.0, ink=10)
    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p1_stroke_18_撇折/01_撇折.png"
    img.save(out)
    print(f"wrote {out}")

if __name__ == "__main__":
    main()
