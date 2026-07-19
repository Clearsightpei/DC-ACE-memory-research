"""p2_radical_114_日 — G3 coord-format render.

日 (rì) — 4 strokes: 竖 (left) + 横折 (top+right) + 横 (middle) + 横 (bottom).

Structural analysis of GT (viewed 300x300):
  - Tall narrow rectangle ~110px wide, ~210px tall, roughly canvas-
    centered but slightly left-of-center.
  - Middle 横 spans the interior (does NOT touch the right wall on
    every hand — GT shows a small gap on right, but for radical
    identity we let it span the interior).
  - Bottom 横 spans full width, welding to left 竖 and right descent.

TR-compliance / INLINE-FRESH TEST:
  - kou.py primitive in bank is for the WIDER 口 (aspect ~1:1). 日 is
    aspect ~1:2 (much taller than wide). Force-fitting kou would
    require scale_y ≠ scale_x, which the primitive can't do. Per TR5
    / TR8, inline fresh.
  - Draw as 4 straight tapered lines. Coord format: numeric offsets
    on 300x300 canvas, math-coord convention where used.

Origin: canvas center (150, 150) in PIL px.
Box dimensions:
  x_left  =  90 px, x_right = 205 px  → width 115
  y_top   =  50 px, y_bot   = 250 px  → height 200
  y_mid   = 155 px  (slightly below geometric center — GT shows middle
                     bar sits just below true center, more visual balance)
"""

from PIL import Image, ImageDraw

CANVAS = 300


def draw_ri(t, ox=0, oy=0, scale=1.0):
    """Draw 日 with numeric coord offsets (all in PIL px, top-left origin)."""
    # Box corners (before offset/scale).
    x_left = 90 + ox
    x_right = 205 + ox
    y_top = 50 + oy
    y_bot = 250 + oy
    y_mid = 155 + oy

    # Stroke thickness (matches heng/shu bank default: 12 px at scale=1.0).
    w = max(1, int(round(11 * scale)))
    w_mid = max(1, int(round(9 * scale)))  # middle 横 slightly thinner (GT)

    # Stroke 1: left 竖 — TL (x_left, y_top) → BL (x_left, y_bot).
    #   Top-left tap slightly hooked in on GT; we draw straight line.
    t.line([(x_left, y_top), (x_left, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 2: 横折 — top 横 from TL to TR, then 竖 down TR to BR.
    #   Drawn as two segments meeting at (x_right, y_top).
    #   The 横 slightly overshoots left edge on GT — start weld at x_left.
    t.line([(x_left, y_top), (x_right, y_top)], fill=(0, 0, 0), width=w)
    t.line([(x_right, y_top), (x_right, y_bot)], fill=(0, 0, 0), width=w)

    # Stroke 3: middle 横 — spans interior. GT has small gap right of ~5 px.
    #   We draw with a 4-px right-gap to mimic the "not welded" look of GT.
    t.line([(x_left + 2, y_mid), (x_right - 5, y_mid)],
           fill=(0, 0, 0), width=w_mid)

    # Stroke 4: bottom 横 — full width, welds both walls.
    t.line([(x_left, y_bot), (x_right, y_bot)], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_ri(t)
    out_path = __file__.rsplit("/", 1)[0] + "/01_日.png"
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
