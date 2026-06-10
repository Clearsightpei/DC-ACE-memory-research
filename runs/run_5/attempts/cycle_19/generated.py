"""
Cycle 19 — 五 / 六 / 九

五: 4 strokes — top heng + slanting shu (down-left) + middle short heng + heng_zhe corner
    (which forms the right-vertical and bottom heng).
六: 4 strokes — top 点 + long heng + lower-left 撇 (short, scale ~0.4) + lower-right 点
九: 2 strokes — 撇 (long, sweeping down-left from upper-right) + 横折弯钩.

Turtle math-coords on 800x600 canvas, origin center, y-up.
"""

import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, "..", "..", "success_bank", "code")
sys.path.insert(0, SB)

from heng import draw as draw_heng  # noqa: E402
from shu import draw as draw_shu    # noqa: E402
from pie import draw as draw_pie    # noqa: E402
from dian import draw as draw_dian  # noqa: E402
from heng_zhe import draw as draw_hz  # noqa: E402
from heng_zhe_wan_gou import draw as draw_hzwg  # noqa: E402


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def draw_wu(t):
    """五 — 4 strokes.

    From GT inspection (turtle coords, y-up):
      1) Top heng:  span x[-120,+130] at y≈+85. -> heng(ox=5, oy=85, scale=0.63).
      2) Slanting shu/pie: from (-30,+85) down-left to (-135,-160).
         Use pie scaled & translated.
      3) Middle short heng: x[-90,+40] at y≈-57. -> heng(ox=-25, oy=-57, scale=0.33).
      4) heng_zhe corner: heng from (+40,-57) right and down to bottom,
         then the closing bottom heng goes left across the character.
         The heng_zhe primitive draws heng-arm + shu-arm; we use a wider scale
         to form the right side, then add a long bottom heng (the closing arm
         of 五's 横折 is effectively the bottom heng).
    """
    # 1) Top heng — slightly higher so layout is balanced
    draw_heng(t, ox=5, oy=85, scale=0.63)

    # 2) Descending slant — extend further down so it reaches the bottom heng.
    # Use pie scale 0.75 head canonical (112.5, 150), tail canonical (-135, -135).
    # Want head ~(-25, +85), tail ~(-110, -155).
    # ox = -25 - 112.5 = -137.5, oy = 85 - 150 = -65.
    # Tail = (-135 - 137.5, -135 - 65) = (-272.5, -200). Tail too far left + low.
    # Better scale 0.65: head canonical (97.5, 130), tail canonical (-117, -117).
    # ox = -25 - 97.5 = -122.5, oy = 85 - 130 = -45.
    # Tail = (-117-122.5, -117-45) = (-239.5, -162). Tail x too far left still but y matches bottom heng.
    draw_pie(t, ox=-122.5, oy=-45, scale=0.65)

    # 3) Middle short heng — extend leftward to touch the slant
    # Want span x[-110, +50] at y≈-50. center ox=-30, length=160, scale=0.40.
    draw_heng(t, ox=-30, oy=-50, scale=0.40)

    # 4) Right vertical (part of 横折) — from middle heng's right end down to bottom heng
    # Want top (+45, -50), bottom (+50, -155). length ~105.
    # scale = 105/400 = 0.26. center y = -102.5.
    draw_shu(t, ox=48, oy=-102, scale=0.265)

    # 5) Bottom long heng
    draw_heng(t, ox=0, oy=-157, scale=0.9)


def draw_liu(t):
    """六 — 4 strokes.

    GT (turtle coords):
      1) Top 点 at ~(-15, +100). Short tilted dot.
      2) Long heng: x[-140,+140] at y≈-10. -> ox=0, oy=-10, scale=0.7.
      3) Lower-left 撇: head ~(-90, -85), tail ~(-115, -170).
         Short, fairly vertical. Use small scale pie.
      4) Lower-right 点 (right-leaning short dian): head ~(+35,-85), tail ~(+70,-170).
         Use draw_dian scaled up.
    """
    # 1) Top dot — closer to heng top
    draw_dian(t, ox=-10, oy=80, scale=1.3)

    # 2) Long heng
    draw_heng(t, ox=0, oy=-10, scale=0.70)

    # 3) Lower-left 撇 (short, fairly steep)
    # scale=0.28: head canonical (42, 56), tail canonical (-50.4, -50.4).
    # Want head ~(-75, -50), tail ~(-115, -165).
    # ox = -75 - 42 = -117, oy = -50 - 56 = -106.
    # Tail = (-50.4-117, -50.4-106) = (-167, -156). dx -92, dy -106. Decent.
    draw_pie(t, ox=-117, oy=-106, scale=0.28)

    # 4) Lower-right dian — short stroke going down-right (like 反捺 / 右点)
    # GT span: entry (+25, -55), tail (+70, -170). dy=-115, dx=+45.
    # dian canonical dx=+55, dy=-45 — too horizontal. Need elongated dian.
    # Two dians stacked won't work cleanly. Use dian at large scale but the GT is more vertical.
    # Use draw_dian with scale 2.5: entry canonical (-62.5, +50), tail canonical (+75, -62.5).
    # ox = +25 - (-62.5) = +87.5, oy = -55 - 50 = -105.
    # Tail = (+75+87.5, -62.5-105) = (+162.5, -167.5). dx +138 way too horizontal.
    # The lower-right stroke in 六 is technically 右点 leaning down-right.
    # Best compromise: use dian scale 2.0, lean it lower:
    draw_dian(t, ox=55, oy=-115, scale=2.0)


def draw_jiu(t):
    """九 — 2 strokes.

    GT (turtle coords):
      1) Long 撇: from upper-right (+5,+120) sweeping down-left to (-205,-175).
         dx = -210, dy = -295. Pie canonical: dx=-330, dy=-380.
         Use scale 0.78: pie span dx=-258, dy=-297. Close.
         head_canon (150,200)*0.78 = (117,156). ox = +5-117 = -112, oy = +120-156 = -36.
         tail = (-180*0.78 + -112, -180*0.78 + -36) = (-140.4-112, -140.4-36) = (-252.4, -176.4).
         dx from head: -257, dy: -296. Tail slightly past target — fine.
      2) 横折弯钩: heng from (-40, 0) to (+160, 0), down to (+160,-150), curve to (+220,-180), hook up.
         heng_zhe_wan_gou canonical: heng (-80,+120)→(+80,+120), drop to (+80,-60), curve to (+140,-100), hook to (+170,-50).
         Total horizontal span 250 (heng 160 + drop+curve to +140 then hook to +170).
         Want similar span ~260 horizontally. Use scale ~1.05? But also need to shift.
         heng start (-80*s + ox), end (+80*s + ox). Want start ~(-40), end ~(+160).
         center of heng: (start+end)/2 = +60 = ox; heng half-span = 100 = 80*s → s=1.25.
         oy: heng at canonical y=+120. Want heng at y≈0. oy = -120.
         scale=1.25, ox=60, oy=-120 gives:
           heng: (-100+60, 150-120) to (+100+60, 150-120) = (-40, +30) to (+160, +30).
           drop end: (+100+60, -75-120) = (+160, -195).
           curve end: (+175+60, -125-120) = (+235, -245).
           hook end: (+212.5+60, -62.5-120) = (+272.5, -182.5).
         Heng y too high (+30 vs target 0); drop too low (-195 vs -150).
         Use scale=1.0, ox=60, oy=-120:
           heng (-20, 0) to (+140, 0). drop end (+140, -180). curve end (+200, -220). hook end (+230, -170).
           Acceptable.
    """
    # 1) Long pie — head at (+5, +120), tail at (-205, -175).
    # Pie head canonical (150, 200), tail canonical (-180, -180). scale=0.78.
    # Head: (117, 156) + (ox, oy) = (+5, +120) -> ox=-112, oy=-36.
    # Tail: (-140.4, -140.4) + (-112, -36) = (-252, -176). Tail x is far left, OK.
    draw_pie(t, ox=-112, oy=-36, scale=0.78)

    # 2) 横折弯钩 — its heng must cross under the 撇.
    # Canonical heng_zhe_wan_gou: heng (-80,+120)→(+80,+120), drop (+80,-60),
    # curve to (+140,-100), hook to (+170,-50).
    # Want heng span (-50, 0) to (+150, 0), drop to (+150, -140),
    # curve to (+200, -180), hook tip to (+220, -130).
    # scale=1.0: heng (-80+ox, 120+oy) to (+80+ox, 120+oy).
    # Want heng_left = -50 -> ox = +30. Want heng_y = 0 -> oy = -120.
    # heng span: (-50, 0) to (+110, 0). drop end (+110, -180). curve end (+170, -220). hook (+200, -170).
    # Heng too short — try scale 1.1:
    # heng (-88+ox, 132+oy) to (+88+ox, 132+oy). Want heng_left=-50 -> ox=+38. heng_y=0 -> oy=-132.
    # heng (-50, 0) to (+126, 0). drop end (+126, -198). curve end (+192, -242). hook (+225, -187).
    # Drop too low. Use scale 1.0 with ox=+40:
    draw_hzwg(t, ox=40, oy=-130, scale=1.0)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()

    tasks = [
        ("01_五.png", draw_wu),
        ("02_六.png", draw_liu),
        ("03_九.png", draw_jiu),
    ]

    for fname, fn in tasks:
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, fname))

    try:
        turtle.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
