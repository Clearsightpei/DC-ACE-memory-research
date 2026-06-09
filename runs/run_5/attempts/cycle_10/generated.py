"""Cycle 10 — 八 / 人 / 入 (CARRY-OVER from c9).

Fixes vs c9:
- c9 had visual_scores 0.37–0.46 for 八/人 (position/scale didn't match GT) and a
  structural error on 入 (撇 was placed above 捺's head; in 入 the 捺 apex must be
  the topmost point and the 撇 attaches BELOW it).
- This attempt measures the actual MMH GT stroke heads/tails via connected-component
  pixel analysis (see drawer summary), then solves for (ox, oy, scale) that map the
  canonical pie/na endpoints to those measured pixel positions.

Targets (math-coords, derived from CC pixel analysis of GTs):

  八 (gap; 捺 starts higher and slightly right of 撇):
    捺 head=(-22,+72)  kick≈(+191,-148)   → na  scale=0.57, ox=+63.5, oy=-42
    撇 head=(-71,-18)  tail =(-168,-161)  → pie scale=0.34, ox=-122,  oy=-86

  人 (撇 dominant, 捺 attaches to 撇's shaft below apex):
    撇 head=(-11,+88)  tail =(-175,-172)  → pie scale=0.60, ox=-101, oy=-32
    捺 head=(-14,-16)  kick =(+194,-171)  → na  scale=0.45, ox=+53.5, oy=-106

  入 (捺 dominant and TOPMOST; 撇 short, head BELOW the 捺 apex):
    捺 head=(-67,+67)  kick =(+188,-171)  → na  scale=0.65, ox=+30.5, oy=-63
    撇 head=(-4,-2)    tail =(-158,-172)  → pie scale=0.46, ox=-73,   oy=-94

Same turtle + postscript pattern as c6/c8. NO subprocess. `t.reset()` between tasks.
"""
import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from pie import draw as draw_pie
from na import draw as draw_na


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def task_01(t, screen):
    """八 — 撇 + 捺 with visible gap. 捺 is the taller/topmost stroke (per MMH GT)."""
    reset(t)
    # 捺 (right, taller, head higher) — scale 0.57, head at (-22,+72)
    draw_na(t, ox=63.5, oy=-42, scale=0.57)
    # 撇 (left, shorter, head LOWER than 捺's head) — scale 0.34, head at (-71,-18)
    draw_pie(t, ox=-122, oy=-86, scale=0.34)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_八.png"))


def task_02(t, screen):
    """人 — 撇 dominant; 捺 attaches to 撇's shaft below the apex (not a shared apex)."""
    reset(t)
    # 撇 (long, apex at (-11,+82); iter-2 tweak: oy nudged down 6 to land apex at +82 vs +88
    # — iter-1 apex was at pixel y=206 vs GT 212; this brings it down ~6 px)
    draw_pie(t, ox=-101, oy=-38, scale=0.60)
    # 捺 (head at (-14,-16) — about 100 px below the 撇 apex, attaching to shaft)
    draw_na(t, ox=53.5, oy=-106, scale=0.45)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_人.png"))


def task_03(t, screen):
    """入 — 捺 is the dominant/topmost stroke; 撇 is short with head BELOW 捺's apex.

    KEY STRUCTURAL FIX: the 捺's head (-67,+67) must be the topmost point.
    The 撇's head (-4,-2) sits ~70 px below and to the right, attaching to the
    upper-middle section of the 捺's body.
    """
    reset(t)
    # 捺 first (it's the dominant stroke; head is the apex of the whole character)
    draw_na(t, ox=30.5, oy=-63, scale=0.65)
    # 撇 — head BELOW the 捺's head. iter-2: shift the 撇 head slightly down-left
    # (-15 in x, -10 in y vs measured GT) so the thick dunbi blob doesn't visually
    # merge with the 捺 body. New head ≈ (-19, -12), tail ≈ (-173, -182).
    draw_pie(t, ox=-88, oy=-104, scale=0.46)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_入.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen)
    task_02(t, screen)
    task_03(t, screen)


if __name__ == "__main__":
    main()
