"""cycle 16 — 人 / 大 / 不

Renderer: turtle + postscript, NO subprocess.

Measurements from GT (px → turtle: tx=px-400, ty=300-py).

人 GT (2 connected components — 撇+joint, 捺):
  comp1 (撇 + 捺 head joint): bbox=(224,212)-(404,472)
    apex (top right of comp1) ≈ (385,212) → turtle (-15,88)
    tail (lower-left)         ≈ (224,472) → turtle (-176,-172)
  comp2 (捺 sweep):           bbox=(385,316)-(594,474)
    head (where it joins pie)  ≈ (385,316) → turtle (-15,-16)
    tail (lower-right)         ≈ (594,474) → turtle (194,-174)
  Picked: pie scale=0.55 ox=-100 oy=-25  (head≈(-17.5,85) tail≈(-199,-124))
          na  scale=0.50 ox=60  oy=-115  (head≈(-15,-15) tail≈(180,-201))
  Structural note: na head sits BELOW pie apex — they meet on pie mid-shaft,
  not at apex.

大 GT (heng + pie merged comp1, na comp2):
  heng band: center y≈305, x range 283-524 → turtle center (4,-5), w≈241
  pie:  head ~(385,182) → (-15,118),  tail ~(251,494) → (-149,-194)
  na:   head ~(390,334) → (-10,-34),  tail ~(581,494) → (181,-194)
  Picked: heng scale=0.60 ox=4   oy=-5
          pie  scale=0.55 ox=-95 oy=-2  (head≈(-12.5,108) tail≈(-194,-101))
          na   scale=0.45 ox=60  oy=-115 (head≈(-7.5,-25) tail≈(168,-192))
  Structural note: pie/na apexes coincide at upper area, pie extends above
  heng (canonical 大).

不 GT (heng comp1, pie+shu merged comp2, dian comp3):
  heng:  bbox=(270,214)-(551,250), center (410,232) → turtle (10,68), w≈281
  shu:   hangs from heng middle ~(400,250) to (400,516) → turtle (0,50) to (0,-216)
  pie:   from below heng right-of-center ~(390,270) → (-10,30)
         to lower-left tail ~(242,516) → (-158,-216)
  dian:  bbox=(449,340)-(553,430) → turtle center (101,-85), span ~104x90
  Picked: heng scale=0.70 ox=10  oy=68
          shu  scale=0.66 ox=0   oy=-83
          pie  scale=0.55 ox=-90 oy=-80  (head≈(-7.5,30) tail≈(-189,-179))
          dian scale=1.5  ox=98  oy=-83
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

from heng import draw as draw_heng
from shu import draw as draw_shu
from pie import draw as draw_pie
from na import draw as draw_na
from dian import draw as draw_dian


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


def draw_ren(t):
    """人 — pie (dominant) + na (attached to pie mid-shaft, below apex).

    GT measured: pie apex (-2,60), tail (-157,-160).
                 na head (-12,-20), tail (120,-160).
    Picked: pie scale=0.55 ox=-84 oy=-50 → apex (-1.5,60), tail (-183,-149)
            na scale=0.40 ox=-30 oy=-100 → head (-90,-20), tail (66,-169)
            (na head attaches to pie body at y≈-20 where body x≈-90)
    """
    draw_pie(t, ox=-50, oy=-30, scale=0.55)
    draw_na(t, ox=25, oy=-110, scale=0.50)


def draw_da(t):
    """大 — heng on top + pie & na crossing through (apex at heng level)."""
    # draw pie & na first, heng on top to cleanly cross
    draw_pie(t, ox=-95, oy=-2, scale=0.55)
    draw_na(t, ox=60, oy=-115, scale=0.45)
    draw_heng(t, ox=4, oy=-5, scale=0.60)


def draw_bu(t):
    """不 — heng on top + pie (below heng, down-left) + shu (hanging from heng mid) + dian (lower-right)."""
    draw_heng(t, ox=10, oy=68, scale=0.70)
    draw_shu(t, ox=0, oy=-83, scale=0.66)
    draw_pie(t, ox=-90, oy=-80, scale=0.55)
    draw_dian(t, ox=98, oy=-83, scale=1.5)


def render_one(screen, t, draw_fn, filename):
    reset(t)
    draw_fn(t)
    screen.update()
    out_path = os.path.join(OUT_DIR, filename)
    save_canvas_to_png(screen, out_path)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0, 0)
    t = turtle.Turtle()
    render_one(screen, t, draw_ren, "01_人.png")
    render_one(screen, t, draw_da, "02_大.png")
    render_one(screen, t, draw_bu, "03_不.png")
    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
