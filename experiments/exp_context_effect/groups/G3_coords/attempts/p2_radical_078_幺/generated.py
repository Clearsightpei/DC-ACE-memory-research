# 幺 (yāo) — 3-stroke radical: 撇折 + 撇折 + 点.
#
# Structure per GT (visually inspected):
#   Stroke 1 (top small): 撇折 — small pie starting upper-right, going
#                         down-left, then a short curved segment turning
#                         back rightward-up (forms tiny "レ"-like loop
#                         at top).
#   Stroke 2 (middle large): 撇折 — larger pie starting upper-right,
#                            going down-left with strong curve, then a
#                            longer bent segment scooping right-and-down,
#                            forming the body of the character.
#   Stroke 3 (bottom): 点 — small dot at bottom-right closing the char.
#
# TR8 (INLINE-FRESH): pie_zhe primitive has sharp corners and a
# straight horizontal. 幺's turns are ROUNDED. Inline fresh.
# Revision 1 changes vs pass-1:
#   - Enlarge overall glyph (fill more of the canvas).
#   - Make the two 撇折 shapes more distinct and calligraphic (each
#     is a pie-diagonal then a bend, not a snake).
#   - Fix stroke 2 tail: should scoop rightward-downward toward the
#     bottom-right, not descend far to bottom-left.

from PIL import Image, ImageDraw
import math

CANVAS = 300
CX, CY = CANVAS // 2, CANVAS // 2


def _to_pixel(mx, my):
    return CX + mx, CY - my


def tapered_bezier(draw, p0, p1, p2, w_start, w_end, steps=50):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pt = _to_pixel(x, y)
        w = max(1, int(round(w_start + (w_end - w_start) * u)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w)
        r = w // 2
        draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                     fill=(0, 0, 0))
        prev = pt


def draw_pie_zhe_inline(draw, head, corner, end,
                        w_head_pie, w_corner, w_end,
                        pie_ctrl=None, zhe_ctrl=None):
    """A 撇折 as two tapered beziers sharing the corner pixel.
    head -> corner: pie (diagonal down-left), curved.
    corner -> end: zhe (bent segment scooping rightward), curved.
    ctrl points optional; default midpoint chord."""
    if pie_ctrl is None:
        pie_ctrl = ((head[0] + corner[0]) / 2, (head[1] + corner[1]) / 2)
    if zhe_ctrl is None:
        zhe_ctrl = ((corner[0] + end[0]) / 2, (corner[1] + end[1]) / 2)
    # pie segment (tapered from head thick-ish to corner)
    tapered_bezier(draw, head, pie_ctrl, corner,
                   w_start=w_head_pie, w_end=w_corner, steps=40)
    # small ellipse at corner (顿笔 per P6)
    cx, cy = _to_pixel(*corner)
    r = w_corner // 2 + 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # zhe segment (tapered from corner to end)
    tapered_bezier(draw, corner, zhe_ctrl, end,
                   w_start=w_corner, w_end=w_end, steps=40)


def draw_dian(draw, cx, cy, length=20, angle_deg=30,
              w_head=3, w_tail=13):
    a = math.radians(angle_deg)
    p_head = (cx - length / 2 * math.cos(a), cy + length / 2 * math.sin(a))
    p_tail = (cx + length / 2 * math.cos(a), cy - length / 2 * math.sin(a))
    steps = 24
    prev = None
    for i in range(steps + 1):
        u = i / steps
        x = p_head[0] + (p_tail[0] - p_head[0]) * u
        y = p_head[1] + (p_tail[1] - p_head[1]) * u
        pt = _to_pixel(x, y)
        w = max(1, int(round(w_head + (w_tail - w_head) * u)))
        if prev is not None:
            draw.line([prev, pt], fill=(0, 0, 0), width=w)
        r = w // 2
        draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                     fill=(0, 0, 0))
        prev = pt


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # === Stroke 1 — top small 撇折 ===
    # Small: head high-right, corner mid-left, end curling upper-right-ish
    # Math coords, +y up. Canvas useful range ~ [-120, 120].
    draw_pie_zhe_inline(
        draw,
        head=(+20, +85),        # upper-right
        corner=(-15, +50),      # down-left (pie end)
        end=(+15, +55),         # scoops back up-right (small loop)
        w_head_pie=5, w_corner=8, w_end=4,
        pie_ctrl=(+8, +65),     # gentle curve
        zhe_ctrl=(-2, +42),     # loop under
    )

    # === Stroke 2 — larger middle 撇折 forming body ===
    # Head starts around (+20, +25), sweeps down-left, corner around
    # (-40, -20), then scoops right-and-down ending around (+30, -50).
    draw_pie_zhe_inline(
        draw,
        head=(+25, +25),        # starts below stroke-1 corner
        corner=(-45, -25),      # pie tail lower-left (main diagonal)
        end=(+30, -50),         # zhe scoops right-down, ends near dian
        w_head_pie=6, w_corner=10, w_end=5,
        pie_ctrl=(-15, +5),     # belly bulges leftward
        zhe_ctrl=(-15, -55),    # zhe dips downward before rising right
    )

    # === Stroke 3 — bottom dian ===
    # Small dot at bottom-right, closing the composition.
    draw_dian(draw, cx=+45, cy=-70, length=22, angle_deg=30,
              w_head=3, w_tail=13)

    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_078_幺/01_幺.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
