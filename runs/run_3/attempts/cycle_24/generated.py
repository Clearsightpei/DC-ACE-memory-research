"""Cycle 24 — Drawer (run_3).

5 carry-overs (也, 寸, 万, 公, 为) + 1 new (女).
Width floors enforced: peaks 14–18, middles ≥7, tips ≥3 except very-end taper.
Smooth Bézier centerline with per-sample pensize (NOT dot stamps).
"""

import io
import os
import turtle

from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


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
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=160):
    t.penup()
    t.goto(P0)
    t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0] + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0]
        y = (1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1] + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1]
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


# ---------- width profiles ----------

def w_heng(s):
    # heng: heavy both ends, middle slightly lighter; peak 16, middle 10
    # Use a U-shape: w = 10 + 6*(1 - 4*s*(1-s))
    return 10 + 6 * (1 - 4 * s * (1 - s))


def w_shu(s):
    # 竖: heavy both ends, middle 10, peak 16
    return 10 + 6 * (1 - 4 * s * (1 - s))


def w_pie(s):
    # 撇: heavy head (peak 17), shaft 11, taper to ~3 at very end
    if s < 0.85:
        # linear from 17 down to 11 over 0..0.85
        return 17 - (17 - 11) * (s / 0.85)
    # final 15%: taper from 11 down to 3
    u = (s - 0.85) / 0.15
    return 11 - (11 - 3) * u


def w_na(s):
    # 捺: heavy tail (peak 18), head 4, shaft 10
    if s < 0.85:
        return 4 + (10 - 4) * (s / 0.85)
    u = (s - 0.85) / 0.15
    return 10 + (18 - 10) * u


def w_dian(s):
    # 点: belly heavy (peak 14), tail tapers to ~3
    # belly ~ s=0.3
    if s < 0.3:
        return 6 + (14 - 6) * (s / 0.3)
    u = (s - 0.3) / 0.7
    return 14 - (14 - 3) * u


def w_ti(s):
    # 提: heavy base (peak 14), taper to ~3 at tip
    if s < 0.85:
        return 14 - (14 - 9) * (s / 0.85)
    u = (s - 0.85) / 0.15
    return 9 - (9 - 3) * u


def w_uniform(peak=14):
    return lambda s: peak


# ---------- canvas setup ----------

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.tracer(0, 0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)


# ─────────────────────────────────────────────────────────
# ── Task 01 | 也 | yě
# ─────────────────────────────────────────────────────────
reset_turtle(t)

# LARGER 横折钩 (covers most of upper area)
# heng segment: (-150,+150)→(+100,+150)
brushed_bezier(t,
               (-150, 150), (-50, 152), (40, 152), (100, 150),
               w_heng)
# 折 down: (+100,+150)→(+100,-50)
brushed_bezier(t,
               (100, 150), (102, 100), (102, 30), (100, -50),
               w_shu)
# small hook at bottom of 折: (+100,-50)→(+50,-30)  (up-left hook)
brushed_bezier(t,
               (100, -50), (85, -45), (65, -38), (50, -30),
               lambda s: 11 - 6 * s if s < 0.85 else max(3, 11 - 6 * 0.85 - 5 * (s - 0.85) / 0.15))

# Middle 竖: (0,+100)→(0,-100)
brushed_bezier(t,
               (0, 100), (0, 50), (0, -20), (0, -100),
               w_shu)

# 竖弯钩: (-100,0)→(-100,-180)→(+170,-180)→(+170,-130)
# Render as two Bézier arcs joining smoothly.
# Arc 1: vertical drop with bottom curve
brushed_bezier(t,
               (-100, 0), (-100, -90), (-95, -170), (-60, -180),
               w_shu)
# Arc 2: bottom horizontal sweep to right with up-hook
brushed_bezier(t,
               (-60, -180), (40, -184), (130, -184), (170, -180),
               w_heng)
# Hook tip up: (+170,-180)→(+170,-130)
brushed_bezier(t,
               (170, -180), (172, -170), (172, -150), (170, -130),
               lambda s: 11 - 7 * s if s < 0.85 else max(3, 11 - 7 * 0.85 - 4 * (s - 0.85) / 0.15))

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_也.png"))


# ─────────────────────────────────────────────────────────
# ── Task 02 | 寸 | cùn
# ─────────────────────────────────────────────────────────
reset_turtle(t)

# Long heng: (-220,+100)→(+220,+100)
brushed_bezier(t,
               (-220, 100), (-80, 103), (80, 103), (220, 100),
               w_heng)

# 竖钩: (0,+200)→(0,-180) with LARGE hook arm (-90,-150)
# vertical
brushed_bezier(t,
               (0, 200), (0, 100), (0, -40), (0, -180),
               w_shu)
# large hook arm to upper-left: (0,-180)→(-90,-150)
brushed_bezier(t,
               (0, -180), (-30, -180), (-65, -170), (-90, -150),
               lambda s: 12 - 7 * s if s < 0.85 else max(3, 12 - 7 * 0.85 - 5 * (s - 0.85) / 0.15))

# 点: belly (+140,+45), tail (+200,0). Tilted ~45°.
brushed_bezier(t,
               (140, 45), (160, 30), (180, 15), (200, 0),
               w_dian)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_寸.png"))


# ─────────────────────────────────────────────────────────
# ── Task 03 | 万 | wàn
# ─────────────────────────────────────────────────────────
reset_turtle(t)

# heng at (-180,+80)→(+180,+80)
brushed_bezier(t,
               (-180, 80), (-60, 83), (60, 83), (180, 80),
               w_heng)

# 横折钩: (+130,+80)→(+130,-50)→(+80,-30)
# vertical drop
brushed_bezier(t,
               (130, 80), (132, 40), (132, -20), (130, -50),
               w_shu)
# hook up-left
brushed_bezier(t,
               (130, -50), (115, -45), (95, -38), (80, -30),
               lambda s: 11 - 6 * s if s < 0.85 else max(3, 11 - 6 * 0.85 - 5 * (s - 0.85) / 0.15))

# DOMINANT 撇: head at (+60,+260) — very high above heng — down to tail (-220,-180)
brushed_bezier(t,
               (60, 260), (20, 150), (-100, 20), (-220, -180),
               w_pie)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_万.png"))


# ─────────────────────────────────────────────────────────
# ── Task 04 | 公 | gōng
# ─────────────────────────────────────────────────────────
reset_turtle(t)

# 八 撇: (-15,+150)→(-130,+10)
brushed_bezier(t,
               (-15, 150), (-50, 110), (-90, 60), (-130, 10),
               w_pie)
# 八 捺: (+15,+150)→(+140,+10)
brushed_bezier(t,
               (15, 150), (55, 110), (100, 60), (140, 10),
               w_na)

# 厶 撇: (-40,-10)→(-110,-130)
brushed_bezier(t,
               (-40, -10), (-60, -45), (-85, -85), (-110, -130),
               w_pie)
# 厶 closing stroke (横折-like dot/curve): (+50,-10)→(+105,-110)
# Render as a curved stroke that goes down then closes leftward at tip — keep tail heavy like 点.
brushed_bezier(t,
               (50, -10), (75, -40), (95, -75), (105, -110),
               w_dian)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_公.png"))


# ─────────────────────────────────────────────────────────
# ── Task 05 | 为 | wèi
# ─────────────────────────────────────────────────────────
reset_turtle(t)

# Top 点: (+30,+200)→(+85,+155)
brushed_bezier(t,
               (30, 200), (45, 188), (65, 172), (85, 155),
               w_dian)

# 横折钩: (-90,+105) → corner (+95,+105) → drops to (+95,-30) → hook (+45,-15)
# horizontal segment
brushed_bezier(t,
               (-90, 105), (-30, 108), (40, 108), (95, 105),
               w_heng)
# vertical drop
brushed_bezier(t,
               (95, 105), (97, 60), (97, 10), (95, -30),
               w_shu)
# hook up-left
brushed_bezier(t,
               (95, -30), (80, -25), (60, -20), (45, -15),
               lambda s: 11 - 6 * s if s < 0.85 else max(3, 11 - 6 * 0.85 - 5 * (s - 0.85) / 0.15))

# DOMINANT 撇 (full width): (-30,+85)→(-260,-180)
brushed_bezier(t,
               (-30, 85), (-90, 30), (-180, -70), (-260, -180),
               w_pie)

# Lower-right 点: (+85,-90)→(+150,-150)
brushed_bezier(t,
               (85, -90), (105, -105), (128, -128), (150, -150),
               w_dian)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_为.png"))


# ─────────────────────────────────────────────────────────
# ── Task 06 | 女 | nǚ
# ─────────────────────────────────────────────────────────
reset_turtle(t)

# stroke 1 (撇点): start (-30,+200), curve down-left to (-180,0), then 点 to (-100,-160)
# 撇 portion (heavy head → tapered curve into joint)
brushed_bezier(t,
               (-30, 200), (-70, 150), (-130, 75), (-180, 0),
               w_pie)
# 点 portion of the compound: heavy belly near (-180,0), taper down-right to (-100,-160)
brushed_bezier(t,
               (-180, 0), (-160, -40), (-130, -100), (-100, -160),
               w_dian)

# stroke 2 (撇): head (+90,+200), tail (-210,-180), big sweep through center
brushed_bezier(t,
               (90, 200), (30, 110), (-90, -30), (-210, -180),
               w_pie)

# stroke 3 (heng): (-180,-30) to (+180,-30), slight V-dip in the middle
brushed_bezier(t,
               (-180, -30), (-60, -36), (60, -36), (180, -30),
               w_heng)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_女.png"))
