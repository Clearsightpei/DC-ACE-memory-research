"""Cycle 98 — 静 (jing), 14 MMH strokes.

Left radical 青 (8 strokes) + right radical 争 (6 strokes) = 14.
Every position is derived from the brief's 米字格 anchors via
anchor_to_xy(...). No magic numbers, no subprocess, no tools/.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: E402
from dian import draw_dian        # noqa: E402
from heng import draw_heng        # noqa: E402
from shu import draw_shu          # noqa: E402
from pie import draw_pie          # noqa: E402


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

    # ── 青 (left radical, strokes 1–8) ──────────────────────────────
    # s1: 点 (top-left dot of 青's 立 top)
    draw_dian(t, ('TL', 0.224, 0.928), ('TC', 0.364, 0.796))
    # s2: 横 (slight slant heng, upper-left of 青 top)
    draw_heng(t, ('ML', 0.252, 0.348), ('C', 0.232, 0.204))
    # s3: 横 (right vertical-ish heng — but brief says heng)
    draw_heng(t, ('TL', 0.696, 0.308), ('ML', 0.756, 0.572))
    # s4: 横 (long horizontal across the upper 青)
    draw_heng(t, ('ML', -0.212, 0.82), ('C', 0.372, 0.592))
    # s5: 竖 (left vertical of 月 box)
    draw_shu(t, ('BL', 0.328, 0.032), ('BL', 0.26, 1.3))
    # s6: 竖 (right vertical of 月 box)
    draw_shu(t, ('BL', 0.516, 0.084), ('BL', 0.652, 1.196))
    # s7: 横 (middle horizontal inside 月)
    draw_heng(t, ('BL', 0.48, 0.492), ('BL', 0.836, 0.412))
    # s8: 横 (bottom horizontal of 月)
    draw_heng(t, ('BL', 0.456, 0.832), ('BL', 0.848, 0.748))

    # ── 争 (right radical, strokes 9–14) ───────────────────────────
    # s9: 撇 (top diagonal of 争)
    draw_pie(t, ('TC', 0.944, 0.364), ('C', 0.468, 0.192))
    # s10: 横 (long heng across upper-right of 争, treated as a long horizontal)
    draw_heng(t, ('TC', 0.844, 0.932), ('MR', 0.008, 0.456))
    # s11: 竖 (short vertical in middle of 争)
    draw_shu(t, ('C', 0.512, 0.576), ('BR', 0.508, 0.164))
    # s12: 横 (long heng — the central horizontal bar of 争)
    draw_heng(t, ('C', 0.34, 1.0), ('MR', 1.28, 0.824))
    # s13: 横 (short horizontal on lower right of 争)
    draw_heng(t, ('BC', 0.5, 0.408), ('BR', 0.744, 0.304))
    # s14: 竖 (the central long vertical/hook of 争)
    draw_shu(t, ('C', 0.864, 0.628), ('BC', 0.468, 1.272))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_静.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
