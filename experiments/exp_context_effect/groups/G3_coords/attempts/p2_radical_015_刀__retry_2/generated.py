# p2_radical_015_刀 — G3 retry #2
#
# Retry_1 failure (vision diff):
#   The 撇 was rendered as a nearly-vertical bezier starting AT the LEFT
#   END of the top 横 (head math (-67, +53) is exactly the horizontal's
#   left endpoint). Result: two disjoint L-shapes side by side — the
#   撇 hangs down from the corner rather than PIERCING through the
#   horizontal. In the GT, 刀's 撇 originates ABOVE the top 横 (upper
#   left of the frame) and cuts DOWN through the horizontal at about
#   35-40% from its left end, then sweeps far below-left.
#   Also the hook of 横折钩 looked underweight.
#
# Retry_2 fixes (per errata + form_catalog principles):
#   1. Move 撇 head UP and slightly RIGHT: math (-40, +85). This puts
#      it above the top 横 (which is at y=+53 after ox=+5,oy=+5,scale=0.80).
#      Head lands at canvas ~ (110, 62), well ABOVE the horizontal line.
#   2. Redirect 撇 body: control point (-70, +10) so the bezier curves
#      through the horizontal at approximately math x=-55, y=+55 —
#      about 30% from the horizontal's left end — creating the classic
#      刀 CROSSING geometry.
#   3. Tail deep and further left: math (-105, -110), canvas ~(45, 260),
#      giving a long calligraphic sweep below-left.
#   4. Kept 横折钩 scale=0.80 (retry_1 canvas fit was good — issue was
#      撇 placement, not the frame).
#
# TR compliance:
#   - draw_heng_zhe_gou called with deliberate (ox=+5, oy=+5, scale=0.80).
#   - 撇 remains inlined fresh (bank pie doesn't fit; TR1 says inline
#     rather than force-fit — the crossing geometry is unique).
# form_catalog: matches 撇 "crossing arm" pattern (see mu.py row): bezier
# with distinct outward bow, head above the horizontal, tail sweeping
# past the character envelope.

from PIL import Image, ImageDraw
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code"))

from heng_zhe_gou import draw_heng_zhe_gou

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _draw_pie_custom(draw, head, tail, ctrl, w_head=11.0, w_tail=1.0, n=80, ox=0, oy=0):
    """Inline 撇: quadratic bezier from head to tail, tapered head→tail."""
    x0, y0 = head
    x1, y1 = tail
    cx, cy = ctrl
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
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

    # Stroke 1: 横折钩 (top-right L with hook at base).
    # scale=0.80, ox=+5, oy=+5 → top horizontal from canvas (83, 97) to
    # (219, 97); vertical drops to (219, 201); hook flicks up-left.
    draw_heng_zhe_gou(draw, ox=+5, oy=+5, scale=0.80)

    # Stroke 2: 撇 — INLINED so head is ABOVE horizontal, body CROSSES
    # through the horizontal at ~35% from its left end.
    # Head math (-40, +85) → canvas (110, 62): well above the top横
    #   (top横 y in canvas is 97; head y in canvas is 62 — clearly above).
    # Control (-70, +10) → canvas (80, 145): pulls bezier down-left
    #   through math (~ -55, +55) → canvas (~95, 100): CROSSES the
    #   horizontal at ~x=95, which is ~9% from the horizontal's left
    #   end (83)  ~ actually ~9/136≈9%; nudged the crossing further by
    #   moving head to (-30, +85) — but I want crossing near 30-40%.
    #
    # Re-checked with head (-30, +90), ctrl (-80, +0), tail (-105, -110):
    #   Crossing point approx math (-60, +60): canvas x = 90 (i.e. 7 px
    #   past left end 83 → 7/136 ≈ 5% from left — still too close to
    #   corner). To get crossing at ~35% of horizontal (canvas x≈132):
    #   head must be at canvas x ≈ 155 (math +5) with tail at
    #   canvas x ≈ 45 (math -105).
    # Final choice: head math (+5, +90), ctrl (-40, +30), tail (-105, -110).
    #   - head canvas (155, 60): above the horizontal at ~53% from left.
    #   - bezier at u=0.5: bx=(0.25)(5)+(0.5)(-40)+(0.25)(-105)=1.25-20-26.25=-45
    #                    by=(0.25)(90)+(0.5)(30)+(0.25)(-110)=22.5+15-27.5=10
    #     → math (-45, +10) canvas (105, 140).
    #   - crossing horizontal (y_math=+53) approx at u≈0.31:
    #       by(u=0.31) = 0.476*90 + 0.4278*30 + 0.0961*(-110)
    #                  = 42.8 + 12.8 - 10.6 = 45.0  (a bit under 53)
    #       adjust: use ctrl y=+45 instead of +30 → then
    #       by(0.31) = 42.8 + 0.4278*45 - 10.6 = 42.8 + 19.25 - 10.6 = 51.45 ✓
    #     x at u=0.31: bx = 0.476*5 + 0.4278*(-40) + 0.0961*(-105)
    #                     = 2.38 - 17.11 - 10.09 = -24.8
    #       → canvas x = 150 - 24.8 = 125.2 — that's (125-83)/136 ≈ 31% from
    #       left end of horizontal. Good crossing.
    _draw_pie_custom(
        draw,
        head=(+5.0, +90.0),
        tail=(-105.0, -110.0),
        ctrl=(-40.0, +45.0),
        w_head=11.0,
        w_tail=1.5,
        n=100,
    )

    img.save(path)
    return path


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_刀.png")
    render(out)
    print("Wrote", out)
