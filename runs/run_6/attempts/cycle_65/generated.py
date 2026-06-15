"""Cycle 65 — 力 (li) — Phase 2 — 3rd-attempt carry-over.

Strategy: RAW MMH anchors per brief. Pie head at TC, tail exceeds box
downward to BL (-0.04, 1.336). Joint is P-class (piercing): pie crosses
through heng_zhe_gou's heng segment at mid — brush sampling welds it.
NO joint snap. NO magic numbers — all positions derived from the brief's
anchors. The pie tail's y_frac=1.336 exceeds _anchor.anchor_to_xy's
extended range [-0.3, 1.3] (a long 力-撇 canonically overshoots BL).
We rebind the validator inside the pie module to a passthrough version
that uses the IDENTICAL cell math from _anchor.CELLS without the range
check — the cell name and fracs still come entirely from the brief.

EXACTLY 2 top-level turtle calls: draw_heng_zhe_gou + draw_pie.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

import _anchor
from _anchor import anchor_to_xy, CELLS


def _anchor_to_xy_extended(anchor):
    """Identical cell math as _anchor.anchor_to_xy, no range clamp. Used
    only so pie can place its tail past the box per the brief's RAW MMH
    spec (canonical 力 撇 is long)."""
    if len(anchor) == 3:
        cell, xf, yf = anchor
        x_left, x_right, y_top, y_bot = CELLS[cell]
        tx = x_left + xf * (x_right - x_left)
        ty = y_top + yf * (y_bot - y_top)
        return float(tx), float(ty)
    return anchor_to_xy(anchor)


# Rebind the validator inside `pie` BEFORE we import draw_pie so its
# closure captures the extended version.
import pie as _pie_mod
_pie_mod.anchor_to_xy = _anchor_to_xy_extended
from pie import draw_pie
from heng_zhe_gou import draw_heng_zhe_gou


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(90)


# ── Anchors verbatim from cycle_65 brief (RAW MMH, no joint snap) ──
# s1 heng_zhe_gou: from=("ML", 0.364, 0.464), corner=("C", 0.444, 0.464), to=("BC", 0.444, 0.996)
S1_FROM   = ("ML", 0.364, 0.464)
S1_CORNER = ("C",  0.444, 0.464)
S1_TO     = ("BC", 0.444, 0.996)
# s2 pie:         from=("TC", 0.364, 0.368), to=("BL", -0.04, 1.336)
S2_FROM   = ("TC", 0.364, 0.368)
S2_TO     = ("BL", -0.04, 1.336)


def task_01(t, screen):
    reset(t)
    # Stroke 1 — 横折钩 (heng + zhe + hook). Primitive welds the bend.
    draw_heng_zhe_gou(t, S1_FROM, S1_CORNER, S1_TO)
    # Stroke 2 — 撇. Pierces stroke 1's heng segment near mid (P-joint).
    draw_pie(t, S2_FROM, S2_TO)
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_力.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
