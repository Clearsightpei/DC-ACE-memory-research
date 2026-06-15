"""Cycle 99 — 影 (ying), 15 MMH strokes.

Left component (景, strokes 1-10): top 日 box, sun atop the 京 below.
Right component (彡, strokes 11-15): three 撇 sweeps + auxiliary marks.

Brief override: y_clamp — some y_fracs reach 1.228..1.3, within _anchor's
extended [-0.3, 1.3] range. No magic numbers — all positions come from
anchor_to_xy via the brief.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy        # noqa: E402
from shu import draw_shu                # noqa: E402
from heng_zhe import draw_heng_zhe      # noqa: E402
from heng import draw_heng              # noqa: E402
from pie import draw_pie                # noqa: E402
from dian import draw_dian              # noqa: E402
from na import draw_na                  # noqa: E402


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(90)


def task_01(t, screen):
    reset(t)

    # ── 景 (left of 影, strokes 1-10) ────────────────────────────────
    # s1: 竖 — left vertical of the top 日 box.
    draw_shu(t, ('TL', 0.376, 0.464), ('ML', 0.652, 0.284))
    # s2: 横折 — top + right vertical of the top 日 box.
    draw_heng_zhe(t,
                  ('TL', 0.552, 0.464),
                  ('TC', 0.384, 0.464),
                  ('C',  0.384, 0.216))
    # s3: 横 — middle bar of top 日 box.
    draw_heng(t, ('TL', 0.684, 0.880), ('TC', 0.212, 0.796))
    # s4: 竖 — bottom edge / closer of top 日 box (slanted).
    draw_shu(t, ('ML', 0.728, 0.228), ('C', 0.232, 0.096))
    # s5: 横 — first horizontal of the 京 mid section.
    draw_heng(t, ('ML', 0.808, 0.296), ('C', 0.104, 0.460))
    # s6: 横 — second horizontal of the 京 mid section (longer, lower).
    draw_heng(t, ('ML', -0.072, 0.716), ('C', 0.752, 0.512))
    # s7: 撇 — left descending sweep below the mid bar.
    draw_pie(t, ('ML', 0.396, 0.936), ('BL', 0.668, 0.580))
    # s8: 竖 — long center vertical of 京 (extends below cell).
    draw_shu(t, ('ML', 0.460, 0.920), ('BC', 0.328, 0.236))
    # s9: 横 — short horizontal piece (口 detail in 京).
    draw_heng(t, ('BL', 0.728, 0.472), ('BC', 0.544, 0.364))
    # s10: 竖 — right vertical leg of 京 (extends below cell, y_clamp 1.228).
    draw_shu(t, ('BL', 0.944, 0.484), ('BL', 0.584, 1.228))

    # ── 彡 (right of 影, strokes 11-15: 3 sweeps + 2 marks) ──────────
    # s11: 点 — small dot/dot-like mark left of 彡 (y_clamp 1.3).
    draw_dian(t, ('BL', 0.456, 0.712), ('BL', 0.240, 1.300))
    # s12: 捺 — right-down sweep (y_clamp 1.0).
    draw_na(t, ('BC', 0.372, 0.676), ('BC', 0.732, 1.000))
    # s13: 撇 — first 彡 sweep, upper.
    draw_pie(t, ('TR', 0.596, 0.372), ('C', 0.980, 0.432))
    # s14: 撇 — second 彡 sweep, middle.
    draw_pie(t, ('MR', 0.684, 0.208), ('BC', 0.936, 0.316))
    # s15: 撇 — third 彡 sweep, long bottom (y_clamp 1.3).
    draw_pie(t, ('BR', 0.764, 0.052), ('BC', 0.484, 1.300))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_影.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
