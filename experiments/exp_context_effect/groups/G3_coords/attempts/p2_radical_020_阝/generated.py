"""p2_radical_020_阝 — G3 coord-bank drawer attempt.

阝 (fu/yi) — 2画部首:
  Stroke 1: 横撇弯钩 (heng pie wan gou) — the "ear" curl. A rounded
            hook-shape that reads like a small '3' or reversed-B loop
            in the upper portion of the canvas.
  Stroke 2: 竖 (shu) — long vertical descender from below the loop
            reaching to the bottom of the canvas.

GT observations (from gt/phase2/阝.png):
- Loop occupies upper ~55% of canvas, roughly x ∈ [80, 180], y ∈ [40, 175].
- Loop reads as one continuous rounded stroke: start upper-left,
  swoop up-right, arc down through a middle waist, arc down-right
  again, then hook back left. Two smooth bumps like a wobbly '3'.
- Long vertical descender starts near loop's lower-left waist
  (~ x=90, y=170) and drops nearly to bottom (~y=280). Long, straight.
- Ink is medium-thin, uniform-ish.

Bank/primitive choices per TR1-TR7:
- shu primitive for the descender (TR2 not applicable — this is
  standalone-like descender, not a scale-shrunken component):
  shu default: half_len=100, thickness 12. We want ~110 px length
  (from y=170 to y=280 in PIL = math -20 to math -130). That's
  half-len 55, so scale ~0.55, centered at math (x=-60, y=-75).
  Actually shu is length 2*half_len*scale — with scale 0.55 → 110 px.
  Center in math coords: x=-60 (i.e. PIL x=90), y=-75 (i.e. PIL y=225).
  So ox=-60, oy=-75, scale=0.55.
- Ear loop: INLINED as a single Bezier-like stroke, because no bank
  primitive captures the double-bump '3' shape at scale that matches
  (heng_zhe_zhe_pie is closest in topology but wrong terminal — it
  has a 撇 sweep, not a 钩 back-curl). Per TR5: inline when no
  primitive fits.

Sanity check (TR7):
- Loop: math x∈[-70,+30], y∈[+30,+110]. In PIL: x∈[80,180], y∈[40,120]. OK.
- Shu head (top) in PIL: (150 + -60, 150 - (-75 + 55)) = (90, 170). OK — lands
  right below the loop's lower-left waist.
- Shu tail (bottom) in PIL: (90, 280). ~20 px margin from bottom edge. OK.
"""

from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _tapered_line(draw, p0, p1, w0, w1, steps=80):
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _bezier_taper(draw, p0, p1, ctrl, w0, w1, steps=100):
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def _cubic_taper(draw, p0, p1, c1, c2, w0, w1, steps=140):
    for i in range(steps + 1):
        u = i / steps
        omu = 1 - u
        bx = (omu ** 3 * p0[0] + 3 * omu ** 2 * u * c1[0]
              + 3 * omu * u ** 2 * c2[0] + u ** 3 * p1[0])
        by = (omu ** 3 * p0[1] + 3 * omu ** 2 * u * c1[1]
              + 3 * omu * u ** 2 * c2[1] + u ** 3 * p1[1])
        r = (w0 + (w1 - w0) * u) / 2.0
        draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))


def draw_ear_loop(draw):
    """横撇弯钩 — the ear-curl of 阝, inlined.

    Topology: from upper-left start, arc right+up (small first hump),
    curve back down through mid waist, arc right+down (second hump),
    then hook back left-down toward the waist.

    Rendered as TWO Bezier segments joined at the middle waist, which
    is also where the descender's head will land.
    """
    # Segment A: top hump — from upper-left start, sweep right and down
    # to the middle waist.
    #   start (math): (-70, +105) — upper-left of loop
    #   end   (math): (-40, +65)  — middle waist (a bit left-of-center)
    #   ctrl 1     : (+10, +130) — pulls up-right, forms the top hump
    #   ctrl 2     : (+30, +75)  — pulls right of waist so the hump bulges right
    p0 = _to_pixel(-70, 105)
    p1 = _to_pixel(-40, 65)
    c1 = _to_pixel(10, 130)
    c2 = _to_pixel(30, 80)
    _cubic_taper(draw, p0, p1, c1, c2, 7.0, 8.0, steps=120)

    # Segment B: bottom hump + hook — from middle waist, sweep right+down
    # for the lower bulge, then hook back toward waist / descender head.
    #   start (math): (-40, +65)  — waist (weld to seg A)
    #   end   (math): (-55, +25)  — hook tip, ends just above/left of shu head
    #   ctrl 1     : (+25, +40)   — pulls right for the lower bulge
    #   ctrl 2     : (+15, +10)   — pulls hook back down-left
    p0 = _to_pixel(-40, 65)
    p1 = _to_pixel(-55, 25)
    c1 = _to_pixel(25, 40)
    c2 = _to_pixel(15, 10)
    _cubic_taper(draw, p0, p1, c1, c2, 8.0, 4.0, steps=120)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # Stroke 1: ear-curl loop (inlined 横撇弯钩).
    draw_ear_loop(draw)

    # Stroke 2: 竖 (shu) — long vertical descender.
    # Inline the shu recipe (TR6: recording transform explicitly).
    # We want top at math (-60, +25) which is PIL (90, 125) — inside/at
    # bottom of loop waist, and bottom at math (-60, -125) which is PIL
    # (90, 275). Length 150 px, thickness ~10 px.
    top = _to_pixel(-60, 25)
    bot = _to_pixel(-60, -125)
    _tapered_line(draw, top, bot, 10.0, 10.0, steps=100)

    out_path = ("<REPO_ROOT>/experiments/"
                "exp_context_effect/groups/G3_coords/attempts/"
                "p2_radical_020_阝/01_阝.png")
    img.save(out_path)
    print(f"saved {out_path}")


if __name__ == "__main__":
    main()
