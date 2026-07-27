# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   errata says "Box + bottom curl; no matching curl primitive. Inline curl."
#   The bank has no shu_zhe_zhe_gou. Inline all three strokes. Prior main
#   attempt (retry_0) used calligraphic ~10px widths + blobs which made the
#   shape look distorted/thick vs MMH thin GT. Fix: thin uniform lines per
#   P12 (~4px) and tighter box proportions matching the GT.
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   P12 rule: MMH GTs use w_head~4 / w_tail~2 uniform; do NOT use
#   calligraphic 10-14 widths. This is directly applicable to 马
#   (all three strokes should be thin uniform ~3-4 px). No specific
#   row for 竖折折钩 in the catalog — inline fresh with thin widths.
# Q3 (helpers): Does the fail category match any of these helpers?
#   - X-crossing / apex-kiss: NO (all joints are right-angle folds, not kisses)
#   - Mirror-dot pair: NO
#   - Per-stroke form variants: partially — could use variant_pie/na for the
#     final hook, but 竖折折钩's hook is a short flick, simplest to inline
#     as a tapered polyline segment.
#   - Uniform thin lines (P12): YES — apply thin ~4 px uniform widths.
#   Plan: NO helper import needed for retry_2; use thin uniform PIL lines
#   with a small hook flick at the end of stroke 2, matching the GT's
#   thin MMH style.

# p2_radical_058_马 retry_2 — G3 coord-form, thin MMH-style.
# 3 strokes:
#   1. 横折 — small top box: short horizontal then drop to form top-right of box
#   2. 竖折折钩 — left vertical of box, then across (middle), then long down,
#      then hook up-left (flick)
#   3. 横 — long bottom horizontal crossing under the shaft
#
# Coords: math convention, origin at canvas center (150,150), +y up.

from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def line(draw, p1, p2, w=4):
    draw.line([_to_pixel(*p1), _to_pixel(*p2)], fill=(0, 0, 0), width=w)


def tapered(draw, p1, p2, w0, w1, steps=14):
    x0, y0 = p1
    x1, y1 = p2
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        draw.line([_to_pixel(xa, ya), _to_pixel(xb, yb)], fill=(0, 0, 0), width=w)


def draw_ma(draw):
    W = 4  # thin uniform per P12

    # Revision: bigger top box (wider), slight rightward drift on descender,
    # softer subtler hook that flicks up-left from a slightly-lower position.

    # Stroke 1: 横折 — top of the box.
    # Horizontal top slightly rising to the right, then drops to form right
    # side of the top box.
    s1_a = (-55, 78)
    s1_b = (35, 82)
    s1_c = (38, 22)
    line(draw, s1_a, s1_b, W)
    line(draw, s1_b, s1_c, W)

    # Stroke 2: 竖折折钩 — the main body.
    #   left vertical from top-left of box down to mid-height
    #   across right (middle horizontal, close to but not exactly matching s1_c)
    #   long descender with slight rightward curve
    #   short hook up-left
    s2_a = (-55, 78)
    s2_b = (-55, 22)
    s2_c = (48, 22)          # middle horizontal extends past s1_c
    # Descender: use a slight curve by drawing two segments (mild rightward
    # bow at top, then near-vertical). Simulate curve with intermediate point.
    s2_d_mid = (55, -20)
    s2_d = (52, -78)
    s2_hook_tip = (10, -60)

    line(draw, s2_a, s2_b, W)
    line(draw, s2_b, s2_c, W)
    line(draw, s2_c, s2_d_mid, W)
    line(draw, s2_d_mid, s2_d, W)
    # hook: taper from body width to a point (up and to the left)
    tapered(draw, s2_d, s2_hook_tip, W, 1, steps=14)

    # Stroke 3: 横 — long horizontal near the bottom.
    # Slightly below the descender's endpoint; extends past both sides.
    s3_a = (-95, -85)
    s3_b = (90, -85)
    line(draw, s3_a, s3_b, W)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ma(d)
    out_path = __file__.rsplit("/", 1)[0] + "/01_马.png"
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
