"""Cycle 78 — 美 (mei). 9 strokes: 羊 top (6) + 大 bottom (3).

Stroke list (anchors verbatim from task_briefs/cycle_78.md):
  s1: pie  TL(0.864, 0.392) -> TC(0.224, 0.696)   top-left dot/pie
  s2: pie  TC(0.868, 0.196) -> TC(0.568, 0.808)   top-right dot/pie
  s3: heng ML(0.580, 0.132) -> TR(0.304, 0.924)   top heng of 羊
  s4: heng ML(0.848, 0.600) -> MR(0.052, 0.464)   middle heng
  s5: shu  C(0.324, 0.172)  -> C(0.372, 0.924)    central shu of 羊
  s6: heng BL(0.284, 0.092) -> MR(0.616, 0.920)   third heng (羊's bottom)
  s7: heng BL(0.496, 0.632) -> BR(0.468, 0.536)   long heng (top of 大)
  s8: pie  BC(0.196, 0.136) -> BL(0.256, 1.300)   left sweep of 大
  s9: na   BC(0.472, 0.660) -> BR(1.116, 1.300)   right sweep of 大
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy  # noqa: F401  (imported for invariant per skill)
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


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
    # s1 — top-left pie
    draw_pie(t, ("TL", 0.864, 0.392), ("TC", 0.224, 0.696))
    # s2 — top-right pie
    draw_pie(t, ("TC", 0.868, 0.196), ("TC", 0.568, 0.808))
    # s3 — top heng of 羊
    draw_heng(t, ("ML", 0.580, 0.132), ("TR", 0.304, 0.924))
    # s4 — middle heng
    draw_heng(t, ("ML", 0.848, 0.600), ("MR", 0.052, 0.464))
    # s5 — central shu
    draw_shu(t, ("C", 0.324, 0.172), ("C", 0.372, 0.924))
    # s6 — third heng (羊's bottom)
    draw_heng(t, ("BL", 0.284, 0.092), ("MR", 0.616, 0.920))
    # s7 — long heng (top of 大)
    draw_heng(t, ("BL", 0.496, 0.632), ("BR", 0.468, 0.536))
    # s8 — left pie sweep of 大
    draw_pie(t, ("BC", 0.196, 0.136), ("BL", 0.256, 1.300))
    # s9 — right na sweep of 大
    draw_na(t, ("BC", 0.472, 0.660), ("BR", 1.116, 1.300))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_美.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
