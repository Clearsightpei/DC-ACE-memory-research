# p2_radical_015_刀 — G3 retry #3
#
# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   errata p2_radical_015_刀 retry_2 fix: "Draw the whole 刀 as ONE continuous
#   polyline: wide 横 head -> 折 corner -> 竖 -> 钩 up-left, with a separate 撇
#   crossing at the horizontal's ~60% mark. Verify hook shares last 5px of
#   shaft (P9)." B3 retry log confirms retry_1/2 both failed with same mode
#   ("heng_zhe_gou + pie disconnection"). retry_2 also failed: pie was too
#   long/steep, head placed near the RIGHT-of-center of the horizontal
#   instead of on the LEFT (~15-30%), and its tail overshot the frame.
#   B4 cross-transfer table does NOT list 刀 (no PASSing char version).
#
# Q2 (form_catalog): Search form_catalog.md for rows matching the stroke(s)
#   that caused the fail.
#   - 横折钩 is the same primitive used in 力/刀/勺 family. Bank primitive
#     `heng_zhe_gou` is trusted (has PASSed as stroke). Keep it at scale=0.80
#     as before -- the frame was fine in retry_2.
#   - 撇 "crossing arm" pattern -- form_catalog rows for 大-family and 木-family
#     say: head slightly ABOVE the crossbar, crossing at ~25-35% from the
#     crossbar's left end, tail sweeping past character envelope. For 刀
#     specifically the pie is shorter and starts NEAR THE LEFT of the top
#     heng (not the right half).
#
# Q3 (helpers): Does the fail category match any of these helpers?
#   - X-crossing / apex-kiss / cross-shaft weld -> YES. `pie_point` helps
#     compute the exact pixel where the pie should cross the horizontal.
#     I'll use it to place the pie so it welds cleanly to the horizontal.
#   The other helpers (mirror_dian_pair, variant_dian) don't apply.
#   Choice: use `pie_point` to derive the weld pixel, then draw the pie
#   as a tapered bezier that passes THROUGH that pixel.
#
# Design (retry_3, addressing retry_2 diagnosis):
#   Retry_2 problems visible in 01_刀.png:
#     (a) 撇 head sat at CANVAS x=155 (math +5) which is ~53% from left of
#         the horizontal -- too far right. Reads like the pie originates
#         from the middle-top, not the left-top corner region of 刀.
#     (b) 撇 tail extended to canvas y=260 (math -110) -- overshoots the
#         hook base at canvas y=201 by ~60px, giving a huge overshooting
#         diagonal that dominates the frame.
#     (c) Result: the pie and the frame read as two disjoint shapes.
#   Fix: move pie head LEFT (~20% from left of horizontal), shorten the
#     tail so it lands near the hook base's y (or slightly below), and
#     ensure the pie visually crosses the horizontal.
#
#   Frame primitive: draw_heng_zhe_gou(ox=+5, oy=+5, scale=0.80)
#     Horizontal spans math (-67, +53) to (+69, +53); canvas (83, 97) to
#     (219, 97). Vertical drops to math (+69, -51); canvas (219, 201).
#     Hook base near canvas (219, 201), hook tip up-left.
#
#   Pie design:
#     head math (-45, +75)  -> canvas (105, 65)   -- ABOVE the horizontal,
#         ~16% from horizontal's left end (canvas 83). Head is above and
#         slightly right of the frame's top-left corner.
#     weld target: cross horizontal at math (-40, +53) -> canvas (110, 97),
#         ~20% from left of horizontal.
#     tail math (-95, -55)  -> canvas (55, 205)  -- ends near the vertical
#         extent of the hook base (canvas y=201), sweeping out to the left
#         edge of the frame (canvas x=55). Length is proportional -- no
#         overshoot.
#     Use variant_pie from _shared_helpers, or an inline tapered bezier
#         through the weld pixel. I'll go inline for explicit control
#         (variant_pie is a symmetric perpendicular bow which won't hit
#         the exact weld pixel).
#     Control point derived so the bezier passes near the weld:
#         B(u) = (1-u)^2 * H + 2(1-u)u * C + u^2 * T
#         At u=0.4, want B ~ (-40, +53).
#         head=(-45,+75), tail=(-95,-55). Solve for C:
#         (1-0.4)^2 = 0.36; 2*0.6*0.4 = 0.48; 0.4^2 = 0.16
#         Bx: 0.36*(-45) + 0.48*Cx + 0.16*(-95) = -40
#             -> -16.2 + 0.48*Cx - 15.2 = -40 -> 0.48*Cx = -8.6 -> Cx = -17.9
#         By: 0.36*(75) + 0.48*Cy + 0.16*(-55) = +53
#             -> 27 + 0.48*Cy - 8.8 = 53 -> 0.48*Cy = 34.8 -> Cy = 72.5
#         So ctrl = (-18, +72). That means the bezier curves outward-right
#         at its top and then sweeps left as it descends. Good -- matches
#         the classic 撇 curl.
#   Widths: w_head=9 (medium, matching frame's ~10px), w_tail=1.5.
#
# TR compliance: heng_zhe_gou called with deliberate (ox=+5, oy=+5,
#   scale=0.80). Pie is inline (bank pie doesn't fit the crossing geometry).

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from heng_zhe_gou import draw_heng_zhe_gou

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _draw_pie_bezier(draw, head, tail, ctrl, w_head=9.0, w_tail=1.5, n=100):
    """Inline 撇: quadratic bezier from head to tail, tapered head->tail."""
    x0, y0 = head
    x1, y1 = tail
    cx, cy = ctrl
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def render(path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Stroke 1: 横折钩 frame -- top 横, right-angle corner, vertical shaft,
    # up-left hook at base. Same scale/offset as retry_2 (frame was fine).
    draw_heng_zhe_gou(draw, ox=+5, oy=+5, scale=0.80)

    # Stroke 2: 撇 crossing at ~25% from left of top horizontal, sweeping
    # down-left to the frame's bottom-left region (no overshoot).
    # Revision: lowered head y so head sits JUST above horizontal (no bulb
    # protrusion). Head math (-38, +62) -> canvas (112, 78); crosses horizontal
    # at math (-32, +53) -> canvas (118, 97) ~26% from left of horizontal.
    _draw_pie_bezier(
        draw,
        head=(-38.0, +62.0),   # canvas (112, 78)  just ABOVE horizontal
        tail=(-95.0, -55.0),   # canvas (55, 205)  near hook-base y
        ctrl=(-25.0, +58.0),   # curve outward-right at top then sweep down-left
        w_head=7.0,
        w_tail=1.5,
        n=120,
    )

    img.save(path)
    return path


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_刀.png")
    render(out)
    print("Wrote", out)
