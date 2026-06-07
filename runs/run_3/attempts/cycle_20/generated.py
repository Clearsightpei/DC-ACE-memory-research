import io, os, turtle
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


# ─── Width profiles ─────────────────────────────────────────────
def w_heng(s):
    # 横: heavy ends, peak 16, middle ~10
    if s < 0.15:
        return 16 - (16 - 12) * (s / 0.15)
    if s > 0.85:
        return 12 + (16 - 12) * ((s - 0.85) / 0.15)
    return 10 + 2 * (1 - abs(s - 0.5) * 2)


def w_shu(s):
    # 竖: heavy ends, peak 16, middle ~10
    if s < 0.15:
        return 16 - (16 - 12) * (s / 0.15)
    if s > 0.85:
        return 12 + (16 - 12) * ((s - 0.85) / 0.15)
    return 10 + 2 * (1 - abs(s - 0.5) * 2)


def w_pie(s):
    # 撇: heavy head, taper to tip. Peak 17 at head.
    if s < 0.05:
        return 17
    if s > 0.95:
        return 3
    return 17 - (17 - 11) * (s - 0.05) / 0.9 + (11 - 6) * (s - 0.05) / 0.9 * (s if s > 0.7 else 0)


def w_pie_simple(s):
    # cleaner taper for 撇
    if s < 0.1:
        return 17
    if s > 0.92:
        return max(3, 17 - (17 - 3) * ((s - 0.1) / 0.85))
    # shaft middle ~11
    return max(11, 17 - (17 - 11) * (s - 0.1) / 0.6)


def w_pie_dominant(s):
    # 万 dominant 撇 with peak 19
    if s < 0.08:
        return 19
    if s > 0.95:
        return 3
    return max(12, 19 - (19 - 12) * (s - 0.08) / 0.85)


def w_na(s):
    # 捺: heavy tail, peak 18 at tail; fine head ~4
    if s < 0.05:
        return 4
    if s > 0.95:
        return 18
    return max(10, 4 + (18 - 4) * s)


def w_ti(s):
    # 提: heavy base (start), taper to tip. Peak 14.
    if s < 0.1:
        return 14
    if s > 0.92:
        return 3
    return max(9, 14 - (14 - 9) * (s - 0.1) / 0.7)


def w_dian(s):
    # 点 teardrop: heavy belly, taper to tail. Peak 14.
    if s < 0.4:
        return max(10, 14 - (14 - 10) * s / 0.4)
    return max(3, 14 - (14 - 3) * (s - 0.4) / 0.6)


def w_gou_shu(s):
    # 竖 part of 竖钩 — keep heavy throughout
    if s < 0.1:
        return 16
    if s > 0.9:
        return 14
    return 12


def w_hook(s):
    # short hook arm — moderate width
    if s < 0.2:
        return 13
    return max(5, 13 - (13 - 5) * (s - 0.2) / 0.8)


def w_wan_gou(s):
    # 竖弯钩 shaft heavy throughout, peak ~15
    if s < 0.1:
        return 15
    if s > 0.9:
        return 11
    return 12


# ─── Stroke helpers ─────────────────────────────────────────────
def stroke_heng(t, x0, y0, x1, y1, samples=140):
    # 横 with subtle arch
    midx = (x0 + x1) / 2
    midy = (y0 + y1) / 2
    brushed_bezier(t, (x0, y0), (x0 + (x1 - x0) * 0.3, midy + 4),
                   (x0 + (x1 - x0) * 0.7, midy + 4), (x1, y1), w_heng, samples=samples)


def stroke_shu(t, x0, y0, x1, y1, samples=140):
    brushed_bezier(t, (x0, y0), (x0, y0 + (y1 - y0) * 0.3),
                   (x1, y0 + (y1 - y0) * 0.7), (x1, y1), w_shu, samples=samples)


def stroke_pie(t, x0, y0, x1, y1, profile=w_pie_simple, samples=160):
    # 撇 curving down-left from head (x0,y0) to tail (x1,y1)
    cx1 = x0 + (x1 - x0) * 0.3
    cy1 = y0 + (y1 - y0) * 0.5
    cx2 = x0 + (x1 - x0) * 0.6
    cy2 = y0 + (y1 - y0) * 0.85
    brushed_bezier(t, (x0, y0), (cx1, cy1), (cx2, cy2), (x1, y1), profile, samples=samples)


def stroke_na(t, x0, y0, x1, y1, samples=160):
    cx1 = x0 + (x1 - x0) * 0.4
    cy1 = y0 + (y1 - y0) * 0.55
    cx2 = x0 + (x1 - x0) * 0.7
    cy2 = y0 + (y1 - y0) * 0.85
    brushed_bezier(t, (x0, y0), (cx1, cy1), (cx2, cy2), (x1, y1), w_na, samples=samples)


def stroke_dian(t, x_belly, y_belly, x_tail, y_tail, samples=80):
    brushed_bezier(t, (x_belly, y_belly),
                   (x_belly + (x_tail - x_belly) * 0.3, y_belly + (y_tail - y_belly) * 0.2),
                   (x_belly + (x_tail - x_belly) * 0.7, y_belly + (y_tail - y_belly) * 0.7),
                   (x_tail, y_tail), w_dian, samples=samples)


# ─── Setup screen ───────────────────────────────────────────────
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.tracer(0, 0)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)


# ── Task 01 | 也 | yě
reset_turtle(t)

# 横折钩 (top-left): heng then drop, with small hook left
# heng: y=+100 spanning x=-100 to +80
stroke_heng(t, -100, 100, 80, 100, samples=140)
# fold drop: shu from (+80, +100) to (+80, +30)
stroke_shu(t, 80, 100, 80, 30, samples=80)
# small hook tip at end of fold (leftward)
brushed_bezier(t, (80, 30), (78, 22), (70, 18), (55, 20), w_hook, samples=40)

# SHU inside: vertical at x=-30 from y=+50 down to y=-50
stroke_shu(t, -30, 50, -30, -50, samples=100)

# 竖弯钩: BIG sweep from (+30, +100) → (+30, -130) → right to (+180, -130) → up-hook (+180, -70)
# vertical part
stroke_shu(t, 30, 100, 30, -130, samples=130)
# curve: from (30, -130) sweeping right with bezier to (180, -130)
brushed_bezier(t, (30, -130), (30, -150), (100, -150), (180, -130), w_wan_gou, samples=100)
# up-hook to (180, -70)
brushed_bezier(t, (180, -130), (185, -110), (185, -90), (180, -70), w_hook, samples=60)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_也.png"))


# ── Task 02 | 巴 | bā
reset_turtle(t)

# Single rectangle on top (no middle divider)
# top heng: y=+200, x=-100 to +100
stroke_heng(t, -100, 200, 100, 200, samples=120)
# left shu: x=-100, y=+200 to 0
stroke_shu(t, -100, 200, -100, 0, samples=120)
# right shu: x=+100, y=+200 to 0
stroke_shu(t, 100, 200, 100, 0, samples=120)
# bottom heng (frame bottom): y=0, x=-100 to +100
stroke_heng(t, -100, 0, 100, 0, samples=120)

# Optional middle small heng inside frame (vertical mouth split) - actually for 巴
# 巴 has a middle horizontal inside upper frame in canonical form. But brief says NO middle divider.
# Follow brief: no middle divider.

# 竖弯钩 below:
# vertical drop from (-100, 0) to (-100, -200)
stroke_shu(t, -100, 0, -100, -200, samples=130)
# curve right from (-100, -200) to (+200, -200)
brushed_bezier(t, (-100, -200), (-50, -220), (100, -220), (200, -200), w_wan_gou, samples=120)
# up-hook to (+200, -150)
brushed_bezier(t, (200, -200), (208, -180), (208, -165), (200, -150), w_hook, samples=60)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_巴.png"))


# ── Task 03 | 寸 | cùn
reset_turtle(t)

# heng: y=+80, x=-150 to +150
stroke_heng(t, -150, 80, 150, 80, samples=140)

# 竖钩: vertical at x=0, y=+150 down to y=-180, then leftward hook
stroke_shu(t, 0, 150, 0, -180, samples=140)
# hook arm leftward 80+ px
brushed_bezier(t, (0, -180), (-15, -175), (-50, -170), (-90, -160), w_hook, samples=70)

# 点 in LOWER-RIGHT: belly (+60, -50), tail (+95, -90), tilted ~30°
stroke_dian(t, 60, -50, 95, -90, samples=70)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_寸.png"))


# ── Task 04 | 万 | wàn
reset_turtle(t)

# heng at y=+100, x=-180 to +180
stroke_heng(t, -180, 100, 180, 100, samples=140)

# 横折弯钩: starts at top of heng-right, drops, then curves
# Top of fold: x=+130, y=+180 → down to x=+130, y=+50 → curve right-down → bottom-right
# Actually 万 has 横 then 横折弯钩.
# heng-fold: small heng top from x=-50 y=+180 to x=+130 y=+180?
# Standard 万 form: top is 一, then 丆 shape with 撇 going left and 横折弯钩 going right
# Let me draw: 横折弯钩 starting from (+130, +180): heng-fold shape
# heng top part of fold: from (+10, +180) to (+130, +180)
stroke_heng(t, 10, 180, 130, 180, samples=80)
# vertical drop of fold: x=+130, y=+180 to y=-50
stroke_shu(t, 130, 180, 130, -50, samples=120)
# curve down-right then hook
brushed_bezier(t, (130, -50), (135, -100), (160, -130), (190, -130), w_wan_gou, samples=80)
# up-hook: (+190, -130) curving up-left to (+170, -90)
brushed_bezier(t, (190, -130), (195, -115), (188, -100), (170, -90), w_hook, samples=50)

# 撇 DOMINANT: head HIGH at (+50, +220), tail at (-220, -150)
stroke_pie(t, 50, 220, -220, -150, profile=w_pie_dominant, samples=180)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_万.png"))


# ── Task 05 | 几 | jǐ
reset_turtle(t)

# 撇 on left: from top (-60, +150) sweeping down-left to (-140, -120)
stroke_pie(t, -60, 150, -140, -120, profile=w_pie_simple, samples=160)

# 横折弯钩 on right:
# top heng at y=+150 from x=-60 to x=+130
stroke_heng(t, -60, 150, 130, 150, samples=100)
# vertical drop right side: x=+130, y=+150 to y=-100 (SHORT drop)
stroke_shu(t, 130, 150, 130, -100, samples=110)
# curve 弯 right to x=+170
brushed_bezier(t, (130, -100), (135, -130), (155, -140), (170, -120), w_wan_gou, samples=70)
# MODERATE up-hook: 40 px arm pointing up
brushed_bezier(t, (170, -120), (172, -105), (168, -90), (160, -80), w_hook, samples=50)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_几.png"))


# ── Task 06 | 公 | gōng
reset_turtle(t)

# 八 on top: left 撇 + right 点/捺
# left 撇: head at (-10, +150), tail at (-150, +30)
stroke_pie(t, -10, 150, -150, 30, profile=w_pie_simple, samples=140)
# right 捺/点: head at (+10, +150), tail at (+150, +30) — short na/dian shape
stroke_na(t, 10, 150, 150, 30, samples=140)

# 厶 below with closure:
# 横撇 portion: heng from (-80, -50) to (+40, -50)
stroke_heng(t, -80, -50, 40, -50, samples=90)
# 折-撇 from (+40, -50) down-left to (-30, -140)
stroke_pie(t, 40, -50, -30, -140, profile=w_pie_simple, samples=120)
# closing 点 — small dian connecting back near the 撇 tail toward right side
# put a 点 from belly near (-15, -130) to tail (+30, -100) — closes the triangle
stroke_dian(t, -15, -125, 35, -95, samples=70)

screen.update()
save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_公.png"))


# done — do not call screen.bye() or turtle.done()
