"""夕 (xī) — 3-stroke radical. G3 coord format.

Composition:
  Stroke 1: 撇 (short) — starts upper-middle, sweeps down-left to left-of-center.
  Stroke 2: 横折撇 — starts near stroke 1's head, short 横 to the right,
            turns/hooks downward, then long sweeping 撇 all the way to bottom-left.
  Stroke 3: 点 — small dot inside the pocket, on stroke 1's tail area.

TR8 note: 夕 has a distinctive continuous curve on the outer sweep (stroke 2)
that primitive `heng_pie` at compressed scale would flatten and lose the belly.
So stroke 2 is INLINED FRESH as one continuous bezier polyline.
Stroke 1 is a short inlined pie (primitive is too long/diagonal for this compact
top-left slash — inline-fresh per TR8).
Stroke 3 uses `dian` primitive with deliberate placement (TR1).
"""

from PIL import Image, ImageDraw

CANVAS = 300
CX, CY = CANVAS / 2, CANVAS / 2


def _to_pixel(ox, oy):
    return CX + ox, CY - oy


def _tapered_bezier(draw, p_start, p_ctrl, p_end, w_head, w_tail, n=48):
    """Draw a quadratic-bezier tapered stroke via stamped-circle sequence."""
    x0, y0 = p_start
    x1, y1 = p_ctrl
    x2, y2 = p_end
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_xi(draw):
    """Render 夕 into an ImageDraw."""

    # -----------------------------------------------------------
    # Stroke 1: short 撇 — head near upper-left of the 夕 body, tail lower-left.
    # Inline-fresh (TR8): compact slash from about (-15, +70) sweeping down
    # to (-60, +10). Slightly right of the outer sweep's starting corner.
    _tapered_bezier(
        draw,
        p_start=(-10, 75),    # thick head, upper
        p_ctrl=(-35, 40),     # leftward bow
        p_end=(-65, 5),       # thin tail, mid-left
        w_head=9, w_tail=2, n=40,
    )

    # -----------------------------------------------------------
    # Stroke 2: 横折撇 — the outer sweep, drawn as ONE continuous curved path.
    # Rounded top-right corner (no sharp elbow), then long sweeping 撇 to
    # the bottom-left. Using a single cubic-like path via two bezier arcs.
    #
    # Arc A: rounded top — from (-10, +80) curving through top and turning
    # down at the right, ending at (+40, +55). This makes the 横 portion
    # look continuous with the descending curve (no boxy corner).
    _tapered_bezier(
        draw,
        p_start=(-10, 80),
        p_ctrl=(30, 90),      # bows up over the top-right shoulder
        p_end=(45, 55),       # descending onto the right shoulder
        w_head=7, w_tail=8, n=30,
    )

    # Arc B: the long descending 撇 from the right shoulder (+45, +55)
    # curving down with a belly bowing outward-right, ending far bottom-left.
    _tapered_bezier(
        draw,
        p_start=(45, 55),
        p_ctrl=(30, -35),     # belly bows out to the right and down
        p_end=(-60, -115),    # thin tail at bottom-left
        w_head=8, w_tail=2, n=60,
    )

    # -----------------------------------------------------------
    # Stroke 3: 点 — small dot inside the pocket.
    # Placed just below stroke 1's tail, inside the enclosed area.
    from dian import draw_dian
    # scale 0.45 keeps the dot small; center around (-15, -20).
    draw_dian(draw, ox=-15, oy=-20, scale=0.45)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_xi(draw)
    out_path = __file__.rsplit("/", 1)[0] + "/01_夕.png"
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    import sys
    import os
    # Make the bank importable so `from dian import draw_dian` works.
    bank = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..", "success_bank", "code",
    )
    sys.path.insert(0, os.path.abspath(bank))
    main()
