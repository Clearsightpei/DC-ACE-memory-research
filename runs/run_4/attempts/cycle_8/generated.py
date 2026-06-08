# ── Task 01 | 竖钩 | shu_gou
"""
竖钩 (shu_gou) — compound vertical-with-hook stroke.

Two segments stitched per §1.5:
  Seg A (shu arm):  (0, +180) → (0, -150). Width 16 → 11 → 14 (pre-hook 顿笔).
  Seg B (hook arm): (0, -150) → (-60, -110). Width 14 → 3 (taper to fine point).

The hook is the visual signature; without it this reads as 竖.
"""

import os
import sys

# Make success_bank/code importable so we can reuse brushed_bezier from heng.py
_HERE = os.path.dirname(os.path.abspath(__file__))
_SUCCESS_CODE = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _SUCCESS_CODE)

from heng import brushed_bezier  # canonical brushed-Bézier helper

import turtle


# ── Width profiles ────────────────────────────────────────────────────────────

def _w_shugou_A(s: float) -> float:
    """Shu arm: top entry press 16 → shaft 11 → pre-hook 顿笔 build to 14.

    - First 10%:  press 16 → 11 (entry 顿笔).
    - Middle 70%: shaft holds ~11.
    - Last 20%:   build 11 → 15 (pre-hook thickening, sets up the hook).
                  Bumped to 15 and widened window so the 顿笔 actually reads.
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.80:
        return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0


def _w_shugou_B(s: float) -> float:
    """Hook arm: inherit 15 at junction → taper to 3 (fine point).

    Hold heavy for the first ~20% (press hold to give the hook visible
    body at its root), then linearly taper to 3 over the remaining 80%.
    """
    if s < 0.20:
        return 15.0 - (s / 0.20) * 2.0  # 15 → 13 hold
    return 13.0 - ((s - 0.20) / 0.80) * 10.0  # 13 → 3 taper


# ── Geometry ──────────────────────────────────────────────────────────────────

def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 竖钩 at offset (ox, oy) with uniform scale."""
    # Segment A — vertical shaft.
    # A0..A2 sit on x=0 to keep the shaft visually plumb; A2 is nudged
    # slightly leftward right at the bottom so the tangent at the junction
    # points down-and-left (eliminates the angular notch — §1.5 rule).
    A0 = (0.0 * scale + ox,  180.0 * scale + oy)
    A3 = (0.0 * scale + ox, -150.0 * scale + oy)
    A1 = (A0[0], A0[1] + (A3[1] - A0[1]) / 3.0)
    A2 = (-3.0 * scale + ox, A0[1] + 2.0 * (A3[1] - A0[1]) / 3.0)
    brushed_bezier(t, A0, A1, A2, A3, _w_shugou_A, samples=220)

    # Segment B — hook curving up and to the left from the shaft tip.
    # Controls placed off the straight line so the hook ARCS smoothly up-left
    # rather than running as a straight diagonal. B1 sits roughly horizontal
    # from the junction (continuing A's down-left tangent), B2 climbs up-left
    # bending the curve concave-up-right before resolving at the tip.
    B0 = (  0.0 * scale + ox, -150.0 * scale + oy)
    B3 = (-60.0 * scale + ox, -110.0 * scale + oy)
    B1 = (-12.0 * scale + ox, -150.0 * scale + oy)  # tangent leftward
    B2 = (-45.0 * scale + ox, -118.0 * scale + oy)  # lift up-left to arc the hook
    brushed_bezier(t, B0, B1, B2, B3, _w_shugou_B, samples=180)


# ── Render ────────────────────────────────────────────────────────────────────

def _render(out_path: str):
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")

    draw(t)

    screen.update()

    # Save canvas as PostScript then convert to PNG via Pillow
    canvas = screen.getcanvas()
    ps_path = out_path.replace(".png", ".ps")
    canvas.postscript(file=ps_path, colormode="color",
                      x=-400, y=-300, width=800, height=600)

    try:
        from PIL import Image
        img = Image.open(ps_path)
        img.load(scale=2)
        # Flatten any transparency onto white
        if img.mode != "RGB":
            bg = Image.new("RGB", img.size, "white")
            bg.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
            img = bg
        img.save(out_path, "PNG")
    finally:
        if os.path.exists(ps_path):
            os.remove(ps_path)

    screen.bye()


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_竖钩.png")
    _render(out)
    print(f"wrote {out}")
