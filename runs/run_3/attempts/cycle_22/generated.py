"""Cycle 22 drawer — 6 chars: 也, 寸, 万, 公, 夫, 车.

Brush rules (from drawer_memory.md):
- Per-sample pensize (NEVER dot stamps); never below 3.
- Width floors: heng/shu peak 16 middle 10; 撇 peak 17 shaft 11;
  捺 peak 18 shaft 10; 提 peak 14 shaft 9; 点 peak 14.
- Smooth Bézier centerlines, samples=160.

c21 lessons baked into brief:
- 也: closed 横折钩 top (no left 竖), 竖弯钩 sweeps bottom half.
- 寸: pronounced 竖钩 hook (100px arm). 点 to upper-right.
- 万: 撇 head ABOVE heng; tail extends past heng's left edge.
- 公: close gap — 厶 overlaps bottom of 八.
- 夫: top heng longer, two hengs closer together (gap 120).
- 车 (new): heng-top, 撇, 竖, heng-bottom — stylized Z.
"""

import io
import os
import turtle

from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ──────────────────────────────────────────────────────────────────
# Canvas helpers
# ──────────────────────────────────────────────────────────────────
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


# ──────────────────────────────────────────────────────────────────
# Width profiles (per drawer_memory.md floors)
# ──────────────────────────────────────────────────────────────────
def w_heng(s):
    # peak 16 at both ends-of-taper, middle 10
    if s < 0.10:
        return 6 + (16 - 6) * (s / 0.10)
    if s > 0.90:
        return 6 + (16 - 6) * ((1 - s) / 0.10)
    if s < 0.25:
        return 16 - (16 - 10) * ((s - 0.10) / 0.15)
    if s > 0.75:
        return 16 - (16 - 10) * ((0.90 - s) / 0.15)
    return 10


def w_shu(s):
    # 竖: peak 16 ends, middle 10
    if s < 0.10:
        return 6 + (16 - 6) * (s / 0.10)
    if s > 0.90:
        return 6 + (16 - 6) * ((1 - s) / 0.10)
    if s < 0.25:
        return 16 - (16 - 10) * ((s - 0.10) / 0.15)
    if s > 0.75:
        return 16 - (16 - 10) * ((0.90 - s) / 0.15)
    return 10


def w_pie(s):
    # 撇: peak 17 at head, shaft 11, hairline only last 5%
    if s < 0.10:
        return 17
    if s < 0.50:
        return 17 - (17 - 11) * ((s - 0.10) / 0.40)
    if s < 0.95:
        return 11 - (11 - 5) * ((s - 0.50) / 0.45)
    return 5 - (5 - 2) * ((s - 0.95) / 0.05)


def w_na(s):
    # 捺: peak 18 at tail (flat horizontal kick), shaft 10, head 4
    if s < 0.10:
        return 4 + (10 - 4) * (s / 0.10)
    if s < 0.70:
        return 10
    if s < 0.90:
        return 10 + (18 - 10) * ((s - 0.70) / 0.20)
    return 18 - (18 - 12) * ((s - 0.90) / 0.10)


def w_dian(s):
    # 点: peak 14 at belly (~s=0.30), tail 2
    if s < 0.30:
        return 6 + (14 - 6) * (s / 0.30)
    return 14 - (14 - 3) * ((s - 0.30) / 0.70)


def w_ti(s):
    # 提: peak 14 at base (start), shaft 9, hairline very end
    if s < 0.10:
        return 14
    if s < 0.50:
        return 14 - (14 - 9) * ((s - 0.10) / 0.40)
    if s < 0.95:
        return 9 - (9 - 4) * ((s - 0.50) / 0.45)
    return 4 - (4 - 2) * ((s - 0.95) / 0.05)


# Compound-stroke width profile: width tracks the *thicker* atomic
# component throughout — never lets the joint thin out.
def w_compound(s):
    # generic peak 16, middle 11 — no zone < 8
    if s < 0.08:
        return 7 + (16 - 7) * (s / 0.08)
    if s > 0.92:
        return 7 + (16 - 7) * ((1 - s) / 0.08)
    return 11 + 4 * (1 - abs(s - 0.5) * 2) * 0.5  # gentle belly 11→13


# ──────────────────────────────────────────────────────────────────
# Atomic-stroke renderers (straight strokes as 4-point Bézier with
# controls colinear → straight, but per-sample width).
# ──────────────────────────────────────────────────────────────────
def stroke_line(t, P0, P3, w_profile, samples=160):
    # 1/3 and 2/3 controls along the line → straight centerline
    P1 = (P0[0] + (P3[0] - P0[0]) / 3, P0[1] + (P3[1] - P0[1]) / 3)
    P2 = (P0[0] + 2 * (P3[0] - P0[0]) / 3, P0[1] + 2 * (P3[1] - P0[1]) / 3)
    brushed_bezier(t, P0, P1, P2, P3, w_profile, samples)


def draw_heng(t, x0, x1, y):
    stroke_line(t, (x0, y), (x1, y), w_heng)


def draw_shu(t, x, y0, y1):
    stroke_line(t, (x, y0), (x, y1), w_shu)


def draw_pie(t, P0, P3):
    # Curved 撇: control points pull leftward in the middle for arc
    dx = P3[0] - P0[0]
    dy = P3[1] - P0[1]
    P1 = (P0[0] + dx * 0.35, P0[1] + dy * 0.20)
    P2 = (P0[0] + dx * 0.65 - 30, P0[1] + dy * 0.65)
    brushed_bezier(t, P0, P1, P2, P3, w_pie)


def draw_na(t, P0, P3):
    # 捺: arcs down-right with flat horizontal tail kick
    dx = P3[0] - P0[0]
    dy = P3[1] - P0[1]
    P1 = (P0[0] + dx * 0.30, P0[1] + dy * 0.55)
    P2 = (P0[0] + dx * 0.70, P0[1] + dy * 0.95)
    brushed_bezier(t, P0, P1, P2, P3, w_na)


def draw_dian(t, P0, P3):
    # Short 点 with belly bulge
    mx = (P0[0] + P3[0]) / 2
    my = (P0[1] + P3[1]) / 2
    P1 = (mx - 3, my + 3)
    P2 = (mx + 3, my - 3)
    brushed_bezier(t, P0, P1, P2, P3, w_dian, samples=80)


def draw_ti(t, P0, P3):
    stroke_line(t, P0, P3, w_ti)


# ──────────────────────────────────────────────────────────────────
# Compound strokes
# ──────────────────────────────────────────────────────────────────
def draw_heng_zhe_gou_closed(t, x_left, x_right, y_top, y_bot, hook_arm=40):
    """横折钩 with closed top (no left 竖). Used in 也.
    Top heng goes left→right at y_top; turns down at x_right→y_bot;
    ends with up-left hook.
    """
    # Top heng
    draw_heng(t, x_left, x_right, y_top)
    # 竖 going down at x_right
    draw_shu(t, x_right, y_top, y_bot)
    # 钩: short up-and-left tick
    P0 = (x_right, y_bot)
    P3 = (x_right - hook_arm, y_bot + hook_arm * 0.7)
    P1 = (x_right - hook_arm * 0.3, y_bot - 5)
    P2 = (x_right - hook_arm * 0.8, y_bot + hook_arm * 0.3)
    brushed_bezier(t, P0, P1, P2, P3, w_compound, samples=80)


def draw_shu_wan_gou(t, x_top, y_top, x_bot_turn, y_bot, x_end, hook_up=50):
    """竖弯钩: down from (x_top,y_top), curves right at y_bot,
    extends to x_end, then up-hook of hook_up px.
    """
    # 竖 part (curving)
    P0 = (x_top, y_top)
    P1 = (x_top, y_top - (y_top - y_bot) * 0.5)
    P2 = (x_top + (x_bot_turn - x_top) * 0.4, y_bot + 20)
    P3 = (x_bot_turn, y_bot)
    brushed_bezier(t, P0, P1, P2, P3, w_compound, samples=120)
    # 弯 horizontal part
    P0 = (x_bot_turn, y_bot)
    P1 = (x_bot_turn + (x_end - x_bot_turn) * 0.4, y_bot - 5)
    P2 = (x_bot_turn + (x_end - x_bot_turn) * 0.7, y_bot)
    P3 = (x_end, y_bot)
    brushed_bezier(t, P0, P1, P2, P3, w_compound, samples=100)
    # 钩 up
    P0 = (x_end, y_bot)
    P3 = (x_end - 10, y_bot + hook_up)
    P1 = (x_end + 5, y_bot + hook_up * 0.3)
    P2 = (x_end - 5, y_bot + hook_up * 0.7)
    brushed_bezier(t, P0, P1, P2, P3, w_compound, samples=60)


def draw_shu_gou(t, x, y_top, y_bot, hook_arm=100):
    """竖钩: straight 竖 then leftward hook at the bottom."""
    draw_shu(t, x, y_top, y_bot)
    # Hook
    P0 = (x, y_bot)
    P3 = (x - hook_arm, y_bot + hook_arm * 0.3)
    P1 = (x - hook_arm * 0.3, y_bot - 10)
    P2 = (x - hook_arm * 0.7, y_bot + hook_arm * 0.1)
    brushed_bezier(t, P0, P1, P2, P3, w_compound, samples=80)


# ──────────────────────────────────────────────────────────────────
# Character drawers
# ──────────────────────────────────────────────────────────────────
def draw_ye(t):
    # ── Task 01 | 也 | yě
    # Closed 横折钩 on top: top closes RIGHT (no left 竖).
    # 竖弯钩 sweeps the bottom half — dominant feature.
    # Plus a single middle vertical to suggest the central element.

    # Top: closed 横折钩 — horizontal top + right-side down + hook
    # Top heng narrower, sitting at y=+120
    draw_heng_zhe_gou_closed(
        t,
        x_left=-130, x_right=130,
        y_top=120, y_bot=20,
        hook_arm=45,
    )

    # Central short 竖 inside the top (suggests the middle stem)
    draw_shu(t, 0, 90, -10)

    # Dominant 竖弯钩: starts upper-left (y≈+100), down to y≈-130,
    # then right to x≈+200, hook up.
    draw_shu_wan_gou(
        t,
        x_top=-180, y_top=110,
        x_bot_turn=-150, y_bot=-130,
        x_end=200,
        hook_up=55,
    )


def draw_cun(t):
    # ── Task 02 | 寸 | cùn
    # heng x=±200 y=80; 竖钩 (0,+170)→(0,-160) hook arm 100;
    # 点 belly (+130,+30) tail (+170,-10).
    draw_heng(t, -200, 200, 80)
    draw_shu_gou(t, 0, 170, -160, hook_arm=100)
    draw_dian(t, (130, 30), (170, -10))


def draw_wan(t):
    # ── Task 03 | 万 | wàn
    # heng (-200,+100)→(+200,+100).
    # 竖 short (just enough to start the 横折弯钩 idea) — using a
    # short 竖 from (-100,+100) down to (-100,+40).
    # 撇 head (+30,+200) tail (-260,-160) — past heng's left edge.
    draw_heng(t, -200, 200, 100)
    # short 竖 (left tick under heng) — left arm of the 横折弯钩
    draw_shu(t, -100, 100, -40)
    # short heng-折 connecting to the right — for the box-ish bottom
    # actually 万 has a 横折弯钩 — drawing the right arm + hook:
    P0 = (200, 100)
    P1 = (200, 50)
    P2 = (180, -20)
    P3 = (-20, -60)
    brushed_bezier(t, P0, P1, P2, P3, w_compound, samples=120)
    # small hook up
    P0 = (-20, -60)
    P3 = (-50, -20)
    P1 = (-20, -50)
    P2 = (-40, -30)
    brushed_bezier(t, P0, P1, P2, P3, w_compound, samples=60)
    # The dominant 撇 — head ABOVE heng, tail past heng's left edge
    draw_pie(t, (30, 200), (-260, -160))


def draw_gong(t):
    # ── Task 04 | 公 | gōng
    # 八 on top, 厶 on bottom with slight overlap.
    # 八: left 撇 from top center down-left, right 点/捺 from top center down-right
    # 八 ends y=0.
    draw_pie(t, (-30, 180), (-130, 0))
    draw_na(t, (30, 180), (140, 0))
    # 厶 starts y=+10 (slight overlap with 八)
    draw_pie(t, (-30, 10), (-110, -150))
    draw_dian(t, (40, 10), (100, -130))


def draw_fu(t):
    # ── Task 05 | 夫 | fū
    # Top heng longer (-150,+170)→(+150,+170);
    # Lower heng (-180,+50)→(+180,+50).
    # 撇 head (-20,+200) tail (-200,-160);
    # 捺 head (+20,+200) tail (+200,-140).
    draw_heng(t, -150, 150, 170)
    draw_heng(t, -180, 180, 50)
    draw_pie(t, (-20, 200), (-200, -160))
    draw_na(t, (20, 200), (200, -140))


def draw_che(t):
    # ── Task 06 | 车 | chē
    # heng top (-200,+170)→(+200,+170);
    # 撇 head (+30,+200) tail (-150,+40);
    # 竖 (0,+90)→(0,-180);
    # heng bottom (-180,-80)→(+180,-80).
    draw_heng(t, -200, 200, 170)
    draw_pie(t, (30, 200), (-150, 40))
    # Middle horizontal (日-like middle band of 车) — small heng at y=+40
    draw_heng(t, -130, 130, 40)
    # Bottom heng
    draw_heng(t, -180, 180, -80)
    # Long central 竖 through the whole stack
    draw_shu(t, 0, 90, -180)


# ──────────────────────────────────────────────────────────────────
# Orchestrator
# ──────────────────────────────────────────────────────────────────
TASKS = [
    ("01_也.png", "也", "yě", draw_ye),
    ("02_寸.png", "寸", "cùn", draw_cun),
    ("03_万.png", "万", "wàn", draw_wan),
    ("04_公.png", "公", "gōng", draw_gong),
    ("05_夫.png", "夫", "fū", draw_fu),
    ("06_车.png", "车", "chē", draw_che),
]


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()

    for filename, char, pinyin, draw_fn in TASKS:
        # ── Task 0X | <char> | <pinyin>
        reset_turtle(t)
        draw_fn(t)
        screen.update()
        out_path = os.path.join(OUT_DIR, filename)
        save_canvas_to_png(screen, out_path)


if __name__ == "__main__":
    main()
