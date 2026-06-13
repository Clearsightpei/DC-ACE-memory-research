"""Cycle 1 — 一 (heng atomic stroke).

Single brushed-Bezier 横 with 楷书 dunbi entry and a heavier closing
press at the right end. All endpoint positions come from
`anchor_to_xy(...)`; no magic numbers in `task_01()`.
"""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy   # only file in success_bank/code so far


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(90)


# ── INLINE primitive (to be promoted to success_bank/code/heng.py on success) ──
def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220):
    """Stamp a cubic Bezier from P0..P3 with per-sample pensize w_profile(s)."""
    t.penup(); t.goto(P0); t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = ((1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0]
             + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0])
        y = ((1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1]
             + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1])
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


def w_heng(s):
    """Width along arc-length s ∈ [0, 1].

    - [0.00, 0.10] entry dunbi:    16 → 11
    - [0.10, 0.85] shaft:          ~11
    - [0.85, 1.00] closing press:  11 → 19  (heaviest, the diagnostic
                                              feature of a 楷书 横)
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.85:
        return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 8.0


def draw_heng(t, from_anchor, to_anchor):
    """Draw a 横 from from_anchor to to_anchor.

    Canonical endpoints: P0 = anchor_to_xy(from_anchor),
                         P3 = anchor_to_xy(to_anchor).
    Control points sit at the 1/3 and 2/3 marks with a small upward
    bow (+4 in y) for the 楷书 arc.
    """
    p0 = anchor_to_xy(from_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.33,
          p0[1] + (p3[1] - p0[1]) * 0.33 + 4)
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.67,
          p0[1] + (p3[1] - p0[1]) * 0.67 + 4)
    brushed_bezier(t, p0, p1, p2, p3, w_heng, samples=220)


def task_01(t, screen):
    reset(t)
    # Exactly ONE top-level draw_heng call for the 1-stroke 一.
    draw_heng(t, ("V_left", "H_mid"), ("V_right", "H_mid"))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    screen.update()


if __name__ == "__main__":
    main()
