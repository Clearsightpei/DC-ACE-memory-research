"""Cycle 18 — carry-overs-only batch: 也, 巴, 寸, 万, 太, 几.

CRITICAL: brushwork width-floor repair after c17 regression.
Per-stroke peaks (from drawer_memory.md):
  横     peak 16, shaft 10, taper ends 6
  竖     peak 16, shaft 10, taper ends 6
  撇     peak 17 head, shaft 11, tail 2 only at last 5%
  捺     peak 18 tail, shaft 10, head 4
  提     peak 14 base, shaft 9, tip 2 only at last 5%
  点     peak 14 belly, tail 2

Renderer: smooth cubic Bézier with per-sample pensize,
`t.pensize(max(3, w_profile(s)))` — NEVER below 3 outside true tip.
"""
import io
import os
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ───────── infrastructure ─────────

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
    """Smooth cubic Bézier; per-sample pensize with hard floor 3."""
    t.penup()
    t.goto(P0)
    t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0] \
            + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0]
        y = (1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1] \
            + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1]
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


# ───────── width profiles (each stroke type) ─────────

def w_heng(s):
    """横: heavy both ends, peak 16, shaft mid 10, taper to 6."""
    # bell with thick shoulders
    if s < 0.08:
        return 16 - (s / 0.08) * 6   # 16 -> 10
    if s > 0.92:
        return 10 + ((s - 0.92) / 0.08) * 6  # 10 -> 16
    # shaft 10 with slight dip at center to 9
    mid = 0.5
    return 10 - abs(s - mid) * 2  # 10 at ends of shaft, 9 at middle


def w_shu(s):
    """竖: heavy both ends, peak 16, shaft 10."""
    if s < 0.08:
        return 16 - (s / 0.08) * 6
    if s > 0.92:
        return 10 + ((s - 0.92) / 0.08) * 6
    return 10 - abs(s - 0.5) * 2


def w_pie(s):
    """撇: head heavy (peak 17), shaft 11, tapers to 2 only at last 5%."""
    if s < 0.10:
        return 17 - (s / 0.10) * 6   # 17 -> 11
    if s < 0.95:
        return 11 - ((s - 0.10) / 0.85) * 2  # 11 -> 9 smooth shaft
    # last 5%: hard taper 9 -> 2
    return 9 - ((s - 0.95) / 0.05) * 7


def w_na(s):
    """捺: tail heavy (peak 18), shaft 10, head 4."""
    if s < 0.10:
        return 4 + (s / 0.10) * 6   # 4 -> 10
    if s < 0.85:
        return 10 + ((s - 0.10) / 0.75) * 2  # 10 -> 12 swelling toward tail
    return 12 + ((s - 0.85) / 0.15) * 6  # 12 -> 18 at tail


def w_ti(s):
    """提: base heavy (peak 14), shaft 9, tip 2 only at last 5%."""
    if s < 0.10:
        return 14 - (s / 0.10) * 5  # 14 -> 9
    if s < 0.95:
        return 9 - ((s - 0.10) / 0.85) * 1  # 9 -> 8
    return 8 - ((s - 0.95) / 0.05) * 6  # 8 -> 2


def w_dian(s):
    """点: belly heavy (peak 14), tail 2."""
    if s < 0.30:
        return 6 + (s / 0.30) * 8  # 6 -> 14
    if s < 0.70:
        return 14 - ((s - 0.30) / 0.40) * 2  # 14 -> 12
    return 12 - ((s - 0.70) / 0.30) * 10  # 12 -> 2


def w_pie_hook(s):
    """竖钩 type: shaft like 竖, tapers to point at hook tip."""
    if s < 0.08:
        return 16 - (s / 0.08) * 5  # 16 -> 11
    if s < 0.85:
        return 11 - ((s - 0.08) / 0.77) * 1  # 11 -> 10
    return 10 - ((s - 0.85) / 0.15) * 4  # 10 -> 6


def w_shuwangou(s):
    """竖弯钩: starts shu-thick, curves through bottom, ends with hook.
    Use shaft 11 with hook tip taper."""
    if s < 0.10:
        return 16 - (s / 0.10) * 5  # 16 -> 11
    if s < 0.88:
        return 11
    return 11 - ((s - 0.88) / 0.12) * 5  # 11 -> 6 at hook tip


def w_hengzhegou(s):
    """横折钩: continuous shaft 11–13, both ends 6 (hook tip)."""
    if s < 0.07:
        return 14 - (s / 0.07) * 3   # 14 -> 11
    if s < 0.90:
        return 11
    return 11 - ((s - 0.90) / 0.10) * 5  # 11 -> 6


def w_hengzhewangou(s):
    """横折弯钩 (几's right side): heavy 横 head, shaft 11, hook tip 6."""
    if s < 0.08:
        return 16 - (s / 0.08) * 5  # 16 -> 11
    if s < 0.92:
        return 11
    return 11 - ((s - 0.92) / 0.08) * 5  # 11 -> 6


# ───────── helpers: simple strokes built from one Bézier ─────────

def stroke_heng(t, x1, y1, x2, y2, w=w_heng):
    """horizontal stroke."""
    dx = x2 - x1
    P0 = (x1, y1)
    P1 = (x1 + dx * 0.33, y1 + 2)
    P2 = (x1 + dx * 0.67, y2 + 2)
    P3 = (x2, y2)
    brushed_bezier(t, P0, P1, P2, P3, w)


def stroke_shu(t, x1, y1, x2, y2, w=w_shu):
    """vertical stroke."""
    dy = y2 - y1
    P0 = (x1, y1)
    P1 = (x1 + 2, y1 + dy * 0.33)
    P2 = (x2 - 2, y1 + dy * 0.67)
    P3 = (x2, y2)
    brushed_bezier(t, P0, P1, P2, P3, w)


def stroke_pie(t, x1, y1, x2, y2, w=w_pie):
    """diagonal 撇: from upper-right to lower-left with curve."""
    dx = x2 - x1
    dy = y2 - y1
    P0 = (x1, y1)
    # curve bulging to outer side
    P1 = (x1 + dx * 0.2, y1 + dy * 0.45)
    P2 = (x1 + dx * 0.55, y1 + dy * 0.8)
    P3 = (x2, y2)
    brushed_bezier(t, P0, P1, P2, P3, w)


def stroke_na(t, x1, y1, x2, y2, w=w_na):
    """diagonal 捺: from upper-left to lower-right, sweeping."""
    dx = x2 - x1
    dy = y2 - y1
    P0 = (x1, y1)
    P1 = (x1 + dx * 0.3, y1 + dy * 0.4)
    P2 = (x1 + dx * 0.7, y1 + dy * 0.85)
    P3 = (x2, y2)
    brushed_bezier(t, P0, P1, P2, P3, w)


def stroke_dian(t, cx, cy, angle_deg=45, length=22, w=w_dian):
    """小点 stroke, tilted at angle_deg from horizontal (right-down)."""
    import math
    rad = math.radians(angle_deg)
    x1 = cx - length * 0.3 * math.cos(rad)
    y1 = cy + length * 0.3 * math.sin(rad)
    x2 = cx + length * 0.7 * math.cos(rad)
    y2 = cy - length * 0.7 * math.sin(rad)
    P0 = (x1, y1)
    P1 = (x1 + (x2 - x1) * 0.3, y1 + (y2 - y1) * 0.3 - 4)
    P2 = (x1 + (x2 - x1) * 0.7, y1 + (y2 - y1) * 0.7 - 2)
    P3 = (x2, y2)
    brushed_bezier(t, P0, P1, P2, P3, w)


# ───────── Task 01 | 也 | yě ─────────

def draw_ye(t, screen):
    """也 = 横折钩 (top frame opening down) + 竖弯钩 + 竖.
    Layout (c17 worked for OCR — keep): upper-middle 竖弯钩 plus inset 横折钩.
    Apply width floors per cheat sheet."""
    reset_turtle(t)

    # Stroke 1: 横折钩 — top horizontal, turn down, hook left at bottom-right
    # Top heng from (-130, 120) to (130, 120)
    stroke_heng(t, -130, 120, 130, 120, w=w_hengzhegou)
    # Turn down: 竖 portion from (130, 120) down to (130, -100), with hook
    # Use a single shu-like curve ending with hook to the left
    P0 = (130, 120)
    P1 = (135, 60)
    P2 = (135, -60)
    P3 = (115, -110)   # hook curls inward-left
    brushed_bezier(t, P0, P1, P2, P3, w_hengzhegou)
    # Small hook tail going up-left
    P0 = (115, -110)
    P1 = (100, -105)
    P2 = (85, -100)
    P3 = (70, -90)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: max(3, 7 - s * 4))

    # Stroke 2: 竖 — internal vertical bar (left-of-center)
    stroke_shu(t, -50, 120, -50, -40, w=w_shu)

    # Stroke 3: 竖弯钩 — middle vertical, curves right at bottom, hook up
    # Start: (40, 60), go down, curve right, hook up
    P0 = (40, 60)
    P1 = (40, -20)
    P2 = (50, -90)
    P3 = (95, -110)    # bottom of curve
    brushed_bezier(t, P0, P1, P2, P3, w_shuwangou)
    # Final hook upward
    P0 = (95, -110)
    P1 = (98, -100)
    P2 = (100, -85)
    P3 = (98, -70)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: max(3, 8 - s * 5))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_也.png"))


# ───────── Task 02 | 巴 | bā ─────────

def draw_ba(t, screen):
    """巴 = 横 + 竖 (left) + 横折 (closing top right) + 竖弯钩 (bottom right curl).
    Frame must be WIDER than tall."""
    reset_turtle(t)

    # Use a wider-than-tall upper frame.
    # Top frame: width ~340, height ~200
    LEFT, RIGHT = -170, 170
    TOP, MID = 150, -50
    BOTTOM = -150

    # Stroke 1: 竖 — left vertical (full height)
    stroke_shu(t, LEFT, TOP, LEFT, BOTTOM + 20, w=w_shu)

    # Stroke 2: 横折 — top heng + right shu (top of frame)
    stroke_heng(t, LEFT, TOP, RIGHT, TOP, w=w_heng)
    stroke_shu(t, RIGHT, TOP, RIGHT, MID, w=w_shu)

    # Stroke 3: middle 横 — divides the upper compartment
    stroke_heng(t, LEFT, MID, RIGHT, MID, w=w_heng)

    # Stroke 4: 竖弯钩 — from middle-right, sweep down and right, then hook up
    P0 = (RIGHT, MID)
    P1 = (RIGHT, MID - 60)
    P2 = (RIGHT - 30, BOTTOM)
    P3 = (RIGHT + 60, BOTTOM)   # sweep right
    brushed_bezier(t, P0, P1, P2, P3, w_shuwangou)
    # hook upward
    P0 = (RIGHT + 60, BOTTOM)
    P1 = (RIGHT + 65, BOTTOM + 15)
    P2 = (RIGHT + 60, BOTTOM + 30)
    P3 = (RIGHT + 50, BOTTOM + 45)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: max(3, 9 - s * 6))

    # Stroke 5: bottom 横 — close bottom of left compartment
    stroke_heng(t, LEFT, BOTTOM, RIGHT - 20, BOTTOM, w=w_heng)

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_巴.png"))


# ───────── Task 03 | 寸 | cùn ─────────

def draw_cun(t, screen):
    """寸 = 横 + 竖钩 + 点 (traditional spot lower-right)."""
    reset_turtle(t)

    # Stroke 1: 横 — wide top
    stroke_heng(t, -160, 80, 160, 80, w=w_heng)

    # Stroke 2: 竖钩 — central vertical with leftward hook at bottom
    # Main shu
    P0 = (10, 110)
    P1 = (10, 30)
    P2 = (8, -60)
    P3 = (5, -130)
    brushed_bezier(t, P0, P1, P2, P3, w_pie_hook)
    # hook left
    P0 = (5, -130)
    P1 = (-10, -125)
    P2 = (-25, -115)
    P3 = (-40, -100)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: max(3, 9 - s * 6))

    # Stroke 3: 点 — traditional spot, lower-right of center
    stroke_dian(t, 70, 10, angle_deg=55, length=36, w=w_dian)

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_寸.png"))


# ───────── Task 04 | 万 | wàn ─────────

def draw_wan(t, screen):
    """万 = 横 + 撇 + 横折弯钩.
    FIX: 撇 head MUST start ABOVE the heng (head y > heng_y + 30);
    sweeps THROUGH the heng to lower-left."""
    reset_turtle(t)

    HENG_Y = 100

    # Stroke 1: 横 — top horizontal
    stroke_heng(t, -180, HENG_Y, 160, HENG_Y, w=w_heng)

    # Stroke 2: 撇 — head ABOVE the heng (y = 150), sweeps through heng down to lower-left
    # head x slightly left of center, tail far lower-left
    P0 = (-30, 160)            # head ABOVE heng_y + 30 = 130
    P1 = (-50, 80)              # passes through heng on the way down
    P2 = (-110, -40)
    P3 = (-180, -150)           # lower-left
    brushed_bezier(t, P0, P1, P2, P3, w_pie)

    # Stroke 3: 横折弯钩 — start near right of heng (intersection),
    # go down, curve at bottom, hook up.
    # Start: (75, HENG_Y) — descender from heng
    # Down to (75, -100), then curve right & up to hook.
    P0 = (75, HENG_Y - 5)
    P1 = (78, 30)
    P2 = (75, -60)
    P3 = (85, -130)
    brushed_bezier(t, P0, P1, P2, P3, w_hengzhewangou)
    # Curve right-up
    P0 = (85, -130)
    P1 = (115, -135)
    P2 = (145, -110)
    P3 = (160, -70)
    brushed_bezier(t, P0, P1, P2, P3, w_hengzhewangou)
    # Hook small tail upward-left
    P0 = (160, -70)
    P1 = (155, -55)
    P2 = (148, -40)
    P3 = (135, -30)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: max(3, 8 - s * 5))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_万.png"))


# ───────── Task 05 | 太 | tài ─────────

def draw_tai(t, screen):
    """太 = 大-shape (横 + 撇 + 捺) + 点 below center.
    大 was MASTERED at 10/10 in c12 — restore proper widths."""
    reset_turtle(t)

    # Stroke 1: 横 — top horizontal
    stroke_heng(t, -160, 100, 160, 100, w=w_heng)

    # Stroke 2: 撇 — head upper-right area (above heng intersection),
    # sweeps down-left through to lower-left
    P0 = (20, 130)              # head above heng
    P1 = (-20, 60)
    P2 = (-90, -50)
    P3 = (-170, -150)
    brushed_bezier(t, P0, P1, P2, P3, w_pie)

    # Stroke 3: 捺 — head upper-left (near 撇 head), sweeps down-right
    P0 = (20, 130)              # head shared zone with pie
    P1 = (50, 50)
    P2 = (100, -40)
    P3 = (170, -120)
    brushed_bezier(t, P0, P1, P2, P3, w_na)

    # Stroke 4: 点 — below center, traditional dot
    stroke_dian(t, -10, -40, angle_deg=55, length=30, w=w_dian)

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_太.png"))


# ───────── Task 06 | 几 | jǐ ─────────

def draw_ji(t, screen):
    """几 = 撇 (left) + 横折弯钩 (right).
    Structure was correct in c17 — just fix widths."""
    reset_turtle(t)

    # Stroke 1: 撇 — starts upper-left top area, sweeps down-left
    # Top is a small cap; the 撇 head sits at the top-left corner.
    P0 = (-110, 140)            # head
    P1 = (-130, 60)
    P2 = (-150, -30)
    P3 = (-170, -130)           # tail lower-left
    brushed_bezier(t, P0, P1, P2, P3, w_pie)

    # Stroke 2: 横折弯钩 — top heng from pie-head over to upper-right,
    # turn down, curve at bottom, hook up.
    # Top portion: small heng from (-110, 140) to (130, 140)
    stroke_heng(t, -100, 140, 130, 140, w=w_heng)
    # Right shu portion descending and curving at the bottom
    P0 = (130, 140)
    P1 = (135, 60)
    P2 = (130, -50)
    P3 = (140, -130)
    brushed_bezier(t, P0, P1, P2, P3, w_hengzhewangou)
    # Hook up-left
    P0 = (140, -130)
    P1 = (138, -110)
    P2 = (135, -90)
    P3 = (125, -75)
    brushed_bezier(t, P0, P1, P2, P3, lambda s: max(3, 9 - s * 6))

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_几.png"))


# ───────── main ─────────

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()

    # ── Task 01 | 也 | yě
    draw_ye(t, screen)

    # ── Task 02 | 巴 | bā
    draw_ba(t, screen)

    # ── Task 03 | 寸 | cùn
    draw_cun(t, screen)

    # ── Task 04 | 万 | wàn
    draw_wan(t, screen)

    # ── Task 05 | 太 | tài
    draw_tai(t, screen)

    # ── Task 06 | 几 | jǐ
    draw_ji(t, screen)


if __name__ == "__main__":
    main()
