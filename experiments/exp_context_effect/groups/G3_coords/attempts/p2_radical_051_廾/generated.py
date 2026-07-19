# p2_radical_051_廾 (gong) — 3-stroke radical.
# Composition (from GT):
#   Stroke 1: 撇 (pie) — left arm, starts upper-mid, sweeps down-left.
#             Head around (-30, +50), tail around (-75, -75) in math coords.
#   Stroke 2: 横 (heng) — horizontal spanning both arms at mid height.
#             Roughly y = +5 in math coords, x from -85 to +75 (length ~160).
#   Stroke 3: 竖 (shu) — right arm, nearly vertical, from ~(+50, +55)
#             down to ~(+50, -80). Slightly right of center.
# Draw order (canonical): pie (left), heng (crossbar), shu (right).
#
# TR1/TR6 transform notes (every bank call is deliberate):
#   draw_pie: scale=0.85 shrinks canonical pie (65,90)->(-45,-85)
#             ox=-15 shifts head left of center; oy=-3 shifts slightly down.
#             Result head ~( -15+55, -3+77 )=(+40, +74) — a bit high; adjust:
#             we want head near (-30,+50). pie head = ox + 65*scale =
#             ox + 55.25. So ox = -30 - 55.25 = -85.25 → head lands wrong.
#             Instead: use scale=0.7. head-offset = 65*0.7=+45.5,
#             tail-offset = -45*0.7=-31.5. If ox=-40, oy=+5, head =
#             (-40+45.5, +5+63)=(+5.5, +68) — still too far right/high.
#             Simpler: INLINE the pie for exact endpoint control (per TR5).
#   draw_heng: canonical length 200*scale. Target length ~160 → scale=0.80.
#              ox=-5, oy=+5 → spans x in [-105,+95], y=+5. Close to target.
#   draw_shu: canonical length 200*scale. Target length ~135 → scale=0.68.
#             half_len=68. Center around (+50, -12) so top ~ (+50,+56),
#             bot ~ (+50, -80). ox=+50, oy=-12.
#
# The pie needs to sit lower-left with head above the heng, tail well
# below. To match GT's steep pie exactly, inline a tapered bezier
# (per TR5 — the canonical pie is tuned as standalone).

from PIL import Image, ImageDraw

CANVAS = 300
CX = CANVAS / 2
CY = CANVAS / 2


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return (CX + ox, CY - oy)


def draw_inlined_pie(draw, head, tail, ctrl_offset=(-8, +5),
                     w_head=9, w_tail=1, n_seg=60):
    """Tapered quadratic-bezier pie from head (thick) to tail (fine).

    head, tail in math coords. ctrl_offset shifts midpoint to bow the curve
    left-ish (down-left sweep character of 撇).
    """
    x0, y0 = head
    x1, y1 = tail
    mx = (x0 + x1) / 2.0 + ctrl_offset[0]
    my = (y0 + y1) / 2.0 + ctrl_offset[1]

    prev = None
    for i in range(n_seg + 1):
        u = i / n_seg
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_inlined_heng(draw, left_x, right_x, y, thickness=10):
    """Simple horizontal tapered line (uniform width per P4)."""
    p_left = _to_pixel(left_x, y)
    p_right = _to_pixel(right_x, y)
    draw.line([p_left, p_right], fill=(0, 0, 0), width=thickness)


def draw_inlined_shu(draw, x, top_y, bot_y, thickness=10):
    """Vertical uniform-thickness shu."""
    p_top = _to_pixel(x, top_y)
    p_bot = _to_pixel(x, bot_y)
    draw.line([p_top, p_bot], fill=(0, 0, 0), width=thickness)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: 撇 (left arm). Head well above heng, tail below-left.
    # Revised: head raised to +75 (higher above crossbar), tail lengthened.
    draw_inlined_pie(
        draw,
        head=(-25, 75),
        tail=(-82, -90),
        ctrl_offset=(-8, 0),
        w_head=10,
        w_tail=1,
        n_seg=60,
    )

    # Stroke 2: 横 (horizontal crossbar). Length ~165, at y=+5.
    # Spans from x=-90 to x=+75.
    draw_inlined_heng(draw, left_x=-90, right_x=+75, y=+5, thickness=10)

    # Stroke 3: 竖 (right vertical). Revised: top raised to +70, slight
    # leftward lean at the top (typical calligraphic 廾 right arm).
    # From (+55, +70) to (+48, -85) — 3px lean toward center.
    p_top = _to_pixel(+55, +70)
    p_bot = _to_pixel(+48, -85)
    draw.line([p_top, p_bot], fill=(0, 0, 0), width=10)

    out_path = __file__.rsplit("/", 1)[0] + "/01_廾.png"
    img.save(out_path, "PNG")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
