# ── Task 01 | 横折钩 | heng_zhe_gou
"""
Cycle 9 drawer — 横折钩 (heng_zhe_gou), L-corner with hook tail.

Three Bézier segments per principle_bank §1.5:
  Seg A (heng arm): (-100,+120) → (+100,+120). Width 16→11→15.
  Seg B (shu arm):  (+100,+120) → (+100,-100). Width 15→11→14.
  Seg C (hook):     (+100,-100) → (+50,-60). Width 14→3. Concave-up-right
                    arc (controls bend it, not a straight diagonal).

Tangency:
  A2 nudged downward toward B's direction (small dy down) so the heng's
    end tangent rolls into the vertical drop without an angular notch.
  B2 nudged leftward toward C's direction (small dx left) so the shu's
    end tangent rolls into the hook.

Uses brushed_bezier from the mastered success_bank/code/heng.py.
"""

import os, sys, turtle

# Resolve success_bank path
_HERE = os.path.dirname(os.path.abspath(__file__))
_RUN_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_BANK_CODE = os.path.join(_RUN_ROOT, "success_bank", "code")
sys.path.insert(0, _BANK_CODE)

from heng import brushed_bezier  # noqa: E402


# ─────────────────────────────────────────────────────────────
# Width profiles
# ─────────────────────────────────────────────────────────────

def _w_A(s: float) -> float:
    """Heng arm. 16 → 11 → 15 (entry dunbi, shaft, corner build)."""
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.80:
        return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0


def _w_B(s: float) -> float:
    """Shu arm. 15 → 11 → 14 (corner inherit, shaft, pre-hook thicken)."""
    if s < 0.15:
        return 15.0 - (s / 0.15) * 4.0
    if s < 0.80:
        return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 3.0


def _w_C(s: float) -> float:
    """Hook. 14 → 3 (taper into the kick tip)."""
    # Hold 14 briefly to read as a continuation of B's pre-hook thicken,
    # then taper smoothly to 3 over the remaining ~80%.
    if s < 0.15:
        return 14.0 - (s / 0.15) * 2.0  # 14 → 12 quick press
    return 12.0 - ((s - 0.15) / 0.85) * 9.0  # 12 → 3 long taper


# ─────────────────────────────────────────────────────────────
# Draw
# ─────────────────────────────────────────────────────────────

def draw_heng_zhe_gou(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    # Seg A: heng arm (-100,+120) → (+100,+120)
    A0 = (-100.0 * scale + ox, 120.0 * scale + oy)
    A3 = (100.0 * scale + ox, 120.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1])
    # A2 nudged a few px DOWN so end-tangent points down toward B
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1] - 3.0 * scale)
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=200)

    # Seg B: shu arm (+100,+120) → (+100,-100)
    B0 = (100.0 * scale + ox, 120.0 * scale + oy)
    B3 = (100.0 * scale + ox, -100.0 * scale + oy)
    B1 = (B0[0], B0[1] + (B3[1] - B0[1]) / 3.0)
    # B2 nudged a few px LEFT so end-tangent points down-and-left into C
    B2 = (B0[0] - 3.0 * scale, B0[1] + 2.0 * (B3[1] - B0[1]) / 3.0)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=200)

    # Seg C: hook (+100,-100) → (+50,-60)
    # Concave-up-right: controls bend the curve so it sweeps left-and-up
    # rather than a straight 45° diagonal. C1 pulls down-and-left (continuing
    # B's tangent), C2 sits above the chord (near target) so the path curls up.
    C0 = (100.0 * scale + ox, -100.0 * scale + oy)
    C3 = (50.0 * scale + ox, -60.0 * scale + oy)
    # C1: just below C0, slightly left — sustains the downward tangent from B
    C1 = (92.0 * scale + ox, -108.0 * scale + oy)
    # C2: above the chord midpoint, pulling the curve into a concave-up arc
    C2 = (60.0 * scale + ox, -78.0 * scale + oy)
    brushed_bezier(t, C0, C1, C2, C3, _w_C, samples=180)


# ─────────────────────────────────────────────────────────────
# Render harness
# ─────────────────────────────────────────────────────────────

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.penup()

    draw_heng_zhe_gou(t)

    screen.update()

    # Save PNG via embedded PostScript → PIL conversion
    out_png = os.path.join(_HERE, "01_横折钩.png")
    ps_path = out_png + ".eps"
    canvas = screen.getcanvas()
    canvas.postscript(file=ps_path, colormode="color")

    try:
        from PIL import Image
        img = Image.open(ps_path)
        img.load(scale=2)  # higher-res rasterize
        img = img.convert("RGB")
        img.save(out_png, "PNG")
    finally:
        if os.path.exists(ps_path):
            os.remove(ps_path)

    screen.bye()


if __name__ == "__main__":
    main()
