"""cycle_93 — 想 (xiang), 13 MMH strokes.

All anchors come from task_briefs/cycle_93_dataset.json. Each MMH
stroke is exactly one draw_<primitive>() call. No magic numbers.
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (used implicitly by primitives)
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na
from heng_zhe import draw_heng_zhe
from dian import draw_dian


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

    # ── Top-left radical 木-like base (strokes 1–4) ─────────────────
    # s1  heng : ML(0.08, 0.172) → TC(0.344, 0.992)
    draw_heng(t, ('ML', 0.08, 0.172), ('TC', 0.344, 0.992))
    # s2  shu  : TL(0.748, 0.196) → BL(0.82, 0.46)
    draw_shu(t, ('TL', 0.748, 0.196), ('BL', 0.82, 0.46))
    # s3  pie  : ML(0.784, 0.212) → BL(-0.032, 0.296)
    draw_pie(t, ('ML', 0.784, 0.212), ('BL', -0.032, 0.296))
    # s4  na   : ML(0.964, 0.428) → C(0.264, 0.728)
    draw_na(t, ('ML', 0.964, 0.428), ('C', 0.264, 0.728))

    # ── Right-top 目 box (strokes 5–9) ───────────────────────────────
    # s5  shu       : TC(0.512, 0.684) → BC(0.632, 0.296)
    draw_shu(t, ('TC', 0.512, 0.684), ('BC', 0.632, 0.296))
    # s6  heng_zhe  : TC(0.74, 0.752) → TR(0.472, 0.752) → BR(0.472, 0.28)
    draw_heng_zhe(t, ('TC', 0.74, 0.752), ('TR', 0.472, 0.752), ('BR', 0.472, 0.28))
    # s7  heng      : C(0.756, 0.276) → MR(0.236, 0.172)
    draw_heng(t, ('C', 0.756, 0.276), ('MR', 0.236, 0.172))
    # s8  heng      : C(0.732, 0.712) → MR(0.248, 0.632)
    draw_heng(t, ('C', 0.732, 0.712), ('MR', 0.248, 0.632))
    # s9  heng      : BC(0.736, 0.192) → BR(0.336, 0.04)
    draw_heng(t, ('BC', 0.736, 0.192), ('BR', 0.336, 0.04))

    # ── Bottom 心 component (strokes 10–13) ─────────────────────────
    # s10 shu  : BL(0.42, 0.64) → BL(0.16, 1.3)   (y_clamp extends past row)
    draw_shu(t, ('BL', 0.42, 0.64), ('BL', 0.16, 1.3))
    # s11 heng : BL(0.784, 0.74) → BR(0.236, 0.856)
    draw_heng(t, ('BL', 0.784, 0.74), ('BR', 0.236, 0.856))
    # s12 dian : BC(0.356, 0.532) → BC(0.712, 0.864)
    draw_dian(t, ('BC', 0.356, 0.532), ('BC', 0.712, 0.864))
    # s13 dian : BR(0.452, 0.5)  → BR(0.976, 0.928)
    draw_dian(t, ('BR', 0.452, 0.5), ('BR', 0.976, 0.928))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_想.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
