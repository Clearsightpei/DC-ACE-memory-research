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
    """Cubic Bézier rendered with per-sample pensize (no dot stamps)."""
    t.penup(); t.goto(P0); t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0] + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0]
        y = (1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1] + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1]
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


# ---------- Width profiles (mandatory floors) -----------------------------
# Peak: 横 16, 竖 16, 撇 17, 捺 18, 提 14, 点 14. Shaft middle >= 10 (>=7 for tapered).

def w_heng(s):
    # Heavy at both ends, middle still >= 10
    # peak 16 at tips, dip to 10 in middle
    return 16 - 6 * (1 - (2 * s - 1) ** 2)


def w_shu(s):
    # Heavy at both ends, middle >= 10
    return 16 - 6 * (1 - (2 * s - 1) ** 2)


def w_pie(s):
    # 撇: heavy head, tapers to fine tail
    # s=0: 17, s=1: 3 (only very tip thin)
    if s < 0.05:
        return 17
    if s > 0.95:
        return 3
    # shaft middle ~ 11
    return 17 - 11 * ((s - 0.05) / 0.9) ** 1.1


def w_na(s):
    # 捺: starts thin at head, swells to peak near 0.85, then flat-kick (still heavy)
    if s < 0.05:
        return 5
    if s < 0.75:
        return 5 + 13 * ((s - 0.05) / 0.7)  # ramp 5 -> 18
    # tail: stays heavy for flat kick
    return 18 - 4 * ((s - 0.75) / 0.25)  # 18 -> 14 at very tip


def w_dian(s):
    # 点: heavy at belly (start side), thin tail
    if s < 0.6:
        return 14 - 4 * (s / 0.6)  # 14 -> 10
    return 10 - 7 * ((s - 0.6) / 0.4)  # 10 -> 3


def w_ti(s):
    # 提: heavy at base (start), thin tail
    if s < 0.6:
        return 14 - 4 * (s / 0.6)
    return 10 - 7 * ((s - 0.6) / 0.4)


def w_shu_gou(s):
    # 竖钩: heavy mostly, hook tapers
    if s < 0.85:
        # shu portion
        return 16 - 4 * (1 - (2 * (s / 0.85) - 1) ** 2)
    # hook tapers but stays >= 6
    return 14 - 6 * ((s - 0.85) / 0.15)


def w_heng_zhe(s):
    # uniform-ish heng-zhe: 14 throughout, slight taper at very tip
    if s > 0.95:
        return 6
    return 14


def w_shu_wan_gou(s):
    # 竖弯钩: heavy throughout, hook end tapers a bit
    if s > 0.9:
        return 14 - 6 * ((s - 0.9) / 0.1)
    return 16 - 4 * (1 - (2 * s - 1) ** 2)


# ---------- Helpers: straight & polyline brushed strokes ------------------

def brushed_line(t, A, B, w_profile, samples=120):
    """Straight line as a degenerate Bézier."""
    P1 = (A[0] + (B[0] - A[0]) / 3.0, A[1] + (B[1] - A[1]) / 3.0)
    P2 = (A[0] + 2 * (B[0] - A[0]) / 3.0, A[1] + 2 * (B[1] - A[1]) / 3.0)
    brushed_bezier(t, A, P1, P2, B, w_profile, samples=samples)


def brushed_polyline(t, pts, w_profile, samples_each=80):
    """Brushed sequence of straight segments with shared width profile across whole path."""
    # compute cumulative lengths for parameterization
    import math
    seg_lens = []
    for i in range(len(pts) - 1):
        a = pts[i]; b = pts[i + 1]
        seg_lens.append(math.hypot(b[0] - a[0], b[1] - a[1]))
    total = sum(seg_lens) or 1.0
    cum = [0.0]
    for L in seg_lens:
        cum.append(cum[-1] + L)
    t.penup(); t.goto(pts[0]); t.pendown()
    for i in range(len(pts) - 1):
        a = pts[i]; b = pts[i + 1]
        for k in range(samples_each + 1):
            u = k / samples_each
            x = a[0] + (b[0] - a[0]) * u
            y = a[1] + (b[1] - a[1]) * u
            s = (cum[i] + seg_lens[i] * u) / total
            t.pensize(max(3, w_profile(s)))
            t.goto(x, y)
    t.penup()


# =================================================================
# Task drawers
# =================================================================

def draw_ye(t):
    # ── Task 01 | 也 | yě
    # OPEN 横折钩 (no closing left bar). Layout: small upper heng-zhe (OPEN), then
    # a DOMINANT 竖弯钩 sweeping bottom half. Small 竖 at center upper.
    # 1) small 横 across upper (the top bar of 也)
    brushed_line(t, (-150, 160), (140, 160), w_heng, samples=140)

    # 2) short 竖 dropping from center-upper (no left rectangle!)
    brushed_line(t, (-40, 160), (-40, 20), w_shu, samples=100)

    # 3) OPEN 横折钩 fragment: small heng at upper right + 折 down + tiny hook
    # heng across (-20,+90) -> (+170,+90), then drop to (+170,-20), tiny hook left
    brushed_polyline(t, [(-20, 90), (170, 90), (170, -10), (130, 0)], w_heng_zhe, samples_each=90)

    # 4) DOMINANT 竖弯钩: starts upper-left, sweeps down then right, hook up at end
    # vertical portion from (-180,+120) down to (-180,-160), then arc right to (+180,-160), hook up to (+180,-110)
    brushed_polyline(
        t,
        [(-180, 120), (-180, -140), (-150, -180), (100, -180), (170, -150), (170, -100)],
        w_shu_wan_gou,
        samples_each=80,
    )


def draw_ba(t):
    # ── Task 02 | 巴 | bā
    # Upper rectangle SHORTER (y +180 to +20), width 100±, fully closed.
    # 竖弯钩 dominates lower 2/3 (frame bottom at -180+).
    # Upper rectangle: 4 closed sides
    # top heng (-50,+180)->(+50,+180)
    brushed_line(t, (-50, 180), (50, 180), w_heng, samples=100)
    # right shu (+50,+180)->(+50,+20)
    brushed_line(t, (50, 180), (50, 20), w_shu, samples=100)
    # bottom heng (-50,+20)->(+50,+20)
    brushed_line(t, (-50, 20), (50, 20), w_heng, samples=100)
    # left shu (-50,+180)->(-50,+20)
    brushed_line(t, (-50, 180), (-50, 20), w_shu, samples=100)
    # internal horizontal divider inside the box for 巴 (middle bar)
    brushed_line(t, (-50, 100), (50, 100), w_heng, samples=100)

    # 竖弯钩: starts at frame's bottom-left (-50,+20), sweeps down well below frame, then right, hook up
    brushed_polyline(
        t,
        [(-50, 20), (-50, -180), (-10, -240), (140, -240), (200, -210), (200, -150)],
        w_shu_wan_gou,
        samples_each=80,
    )


def draw_cun(t):
    # ── Task 03 | 寸 | cùn
    # heng wider (-220 to +220), 竖钩 thicker with hook arm 70 px,
    # 点 at bottom-right of heng: belly (+150,+50) tail (+200,+10).
    # 1) long heng
    brushed_line(t, (-220, 80), (220, 80), w_heng, samples=160)
    # 2) 竖钩: vertical from (0,+200) down to (0,-200), hook left to (-70,-180)
    brushed_polyline(
        t,
        [(0, 200), (0, -200), (-20, -210), (-70, -180)],
        w_shu_gou,
        samples_each=100,
    )
    # 3) 点 at bottom-right of heng (just below heng, well right of 竖钩)
    brushed_bezier(
        t,
        (130, 60),       # P0 (belly start, upper-left of dot)
        (160, 50),       # P1
        (190, 30),       # P2
        (210, 0),        # P3 (tail, lower-right)
        w_dian,
        samples=80,
    )


def draw_wan(t):
    # ── Task 04 | 万 | wàn
    # top heng VERY LONG (-220 to +220).
    # 撇 head (+30,+180) tail (-180,-150).
    # 横折钩 starts (+150,+100), corner (+150,+20), hook left to (+90,+30).
    # 1) long top heng
    brushed_line(t, (-220, 200), (220, 200), w_heng, samples=160)

    # 2) 撇 from above-right of heng sweeping down-left across whole frame
    brushed_bezier(
        t,
        (30, 280),         # head HIGH above heng
        (-20, 180),
        (-100, 0),
        (-200, -180),      # tail lower-left
        w_pie,
        samples=160,
    )

    # 3) 横折钩: short heng at (+0,+100) -> (+150,+100), corner drop to (+150,+20), hook left to (+90,+30)
    brushed_polyline(
        t,
        [(-20, 110), (150, 110), (150, 20), (90, 35)],
        w_heng_zhe,
        samples_each=90,
    )


def draw_gong(t):
    # ── Task 05 | 公 | gōng
    # 八 ends at y=+30. 厶 starts at y=-20 (50 px gap).
    # 厶: small 撇 (-40,-30)->(-100,-130) + 点 (+40,-30)->(+90,-110). NO connecting heng.
    # 1) 八 left stroke (撇): head (-10,+180), tail (-150,+30)
    brushed_bezier(
        t,
        (-10, 200),
        (-40, 160),
        (-100, 80),
        (-150, 30),
        w_pie,
        samples=140,
    )
    # 2) 八 right stroke (捺): head (+10,+180), tail (+150,+30) with flat kick
    brushed_bezier(
        t,
        (10, 200),
        (40, 160),
        (100, 80),
        (160, 30),
        w_na,
        samples=140,
    )
    # 3) 厶 - 撇 portion: (-40,-30) -> (-100,-130)
    brushed_bezier(
        t,
        (-40, -30),
        (-60, -60),
        (-80, -90),
        (-100, -130),
        w_pie,
        samples=100,
    )
    # 4) 厶 - 点 portion: (+40,-30) -> (+90,-110)
    brushed_bezier(
        t,
        (40, -30),
        (55, -50),
        (75, -80),
        (90, -110),
        w_dian,
        samples=100,
    )


def draw_fu(t):
    # ── Task 06 | 夫 | fū
    # top heng short (-100,+200)->(+100,+200)
    # lower heng long (-180,+80)->(+180,+80) with V-dip middle
    # 撇 head (-20,+220) tail (-200,-160)
    # 捺 head (+20,+220) tail (+200,-140) flat kick
    # 1) top short heng
    brushed_line(t, (-100, 200), (100, 200), w_heng, samples=120)
    # 2) lower long heng with V-dip via Bézier control pulling middle down
    brushed_bezier(
        t,
        (-180, 80),
        (-60, 60),
        (60, 60),
        (180, 80),
        w_heng,
        samples=160,
    )
    # 3) 撇 sweeping from above lower heng down to lower-left
    brushed_bezier(
        t,
        (-20, 220),
        (-60, 140),
        (-130, 0),
        (-200, -160),
        w_pie,
        samples=160,
    )
    # 4) 捺 sweeping from above lower heng down to lower-right with flat kick
    brushed_bezier(
        t,
        (20, 220),
        (60, 140),
        (130, 0),
        (200, -140),
        w_na,
        samples=160,
    )


# =================================================================
# Main
# =================================================================

TASKS = [
    ("01_也.png", "也", "yě", draw_ye),
    ("02_巴.png", "巴", "bā", draw_ba),
    ("03_寸.png", "寸", "cùn", draw_cun),
    ("04_万.png", "万", "wàn", draw_wan),
    ("05_公.png", "公", "gōng", draw_gong),
    ("06_夫.png", "夫", "fū", draw_fu),
]


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (fname, ch, pinyin, fn) in enumerate(TASKS, start=1):
        # ── Task NN | <char> | <pinyin>
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, fname))


if __name__ == "__main__":
    main()
