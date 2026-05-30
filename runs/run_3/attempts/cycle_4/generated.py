import io, os, math, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ──────────────────────────────────────────────────────────────────────
# Canvas helpers
# ──────────────────────────────────────────────────────────────────────

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


# ──────────────────────────────────────────────────────────────────────
# Brushed stroke primitives
# ──────────────────────────────────────────────────────────────────────
#
# Width profile is keyed by stroke IDENTITY (the `kind` argument), not
# by chord direction. This is the key fix for 捺 (heavy lower-right
# tail must be at END regardless of how start/end are passed).
#
# 顿笔 cap softening: peak <= ~2x middle, middle floor ~30% of peak.
# We pick peak=1.0 and middle=0.55 (ratio ~1.8, middle = 55% of peak)
# so end caps thicken smoothly rather than reading as separate discs.


def _cubic_bezier(p0, p1, p2, p3, n=160):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1.0 - t
        x = (u * u * u * p0[0]
             + 3 * u * u * t * p1[0]
             + 3 * u * t * t * p2[0]
             + t * t * t * p3[0])
        y = (u * u * u * p0[1]
             + 3 * u * u * t * p1[1]
             + 3 * u * t * t * p2[1]
             + t * t * t * p3[1])
        pts.append((t, x, y))
    return pts


def _width_heng(t, peak):
    """横: weighted entry + thinner middle + weighted end-press.
       Soft caps: peak ~= 1.0, middle floor ~= 0.55*peak.
       No hairline middle, no dumbbell."""
    middle = 0.55 * peak
    # Entry shoulder: t in [0, 0.18] ramps peak -> middle smoothly
    # Body: t in [0.18, 0.78] stays near middle (gentle dip then rise)
    # End press: t in [0.78, 1.0] ramps middle -> peak
    if t <= 0.18:
        # cosine ease from peak to middle
        a = t / 0.18
        return peak - (peak - middle) * (0.5 - 0.5 * math.cos(math.pi * a))
    elif t >= 0.82:
        a = (t - 0.82) / 0.18
        return middle + (peak - middle) * (0.5 - 0.5 * math.cos(math.pi * a))
    else:
        # mild dip in body so it still reads brushed; floor at middle
        a = (t - 0.18) / 0.64
        # symmetric dip ~5% below middle at mid-stroke
        dip = 0.05 * middle * math.sin(math.pi * a)
        return middle - dip


def _width_shu(t, peak):
    """竖: weighted bulb top + thin middle (floored) + weighted foot.
       Same soft-cap profile as heng."""
    return _width_heng(t, peak)


def _width_pie(t, peak):
    """撇: heavy head at START → smooth taper to FINE POINT at END."""
    # peak at t=0, slim taper toward end; near-zero (but not zero) at t=1
    middle = 0.55 * peak
    if t <= 0.15:
        # tiny rounded press at the head
        a = t / 0.15
        return peak - (peak - middle) * (0.5 - 0.5 * math.cos(math.pi * a))
    else:
        # taper from middle down to ~10% of peak (fine but visible)
        a = (t - 0.15) / 0.85
        # ease-out cubic toward fine tail
        end_w = 0.10 * peak
        return middle - (middle - end_w) * (a ** 1.4)


def _width_na(t, peak):
    """捺: THIN entry → broadening body → HEAVY FLAT pressed tail at END.

    This is the cycle-3 failure mode being fixed. The tail (t→1) is the
    heaviest part with a brief flat press, then a short kick.
    Heavy end is ALWAYS at t=1 (the lower-right tail in our chord setup).
    """
    entry = 0.18 * peak       # thin entry
    body_peak_t = 0.92        # peak press near end
    if t <= 0.55:
        # thin entry growing toward body
        a = t / 0.55
        # ease-in: stays thin then accelerates
        return entry + (0.55 * peak - entry) * (a ** 1.3)
    elif t <= body_peak_t:
        # broaden into heavy pressed tail
        a = (t - 0.55) / (body_peak_t - 0.55)
        return 0.55 * peak + (peak - 0.55 * peak) * (0.5 - 0.5 * math.cos(math.pi * a))
    else:
        # short flat press + kick: stay near peak then drop slightly
        a = (t - body_peak_t) / (1.0 - body_peak_t)
        # hold at peak for first half of tail, drop ~25% at the very tip
        return peak * (1.0 - 0.25 * (a ** 2))


WIDTH_FNS = {
    "heng": _width_heng,
    "shu":  _width_shu,
    "pie":  _width_pie,
    "na":   _width_na,
}


def draw_brushed(t, kind, p0, p3, peak=14, arc=0.0, samples=160):
    """Draw a brushed stroke from p0 to p3 using a cubic Bézier
    centerline and per-sample pensize keyed off `kind`.

    `arc` controls perpendicular bow of the curve in pixels (small for
    heng/shu; meaningful for pie/na). Sign convention: positive arc
    bows to the left of the chord direction.
    """
    dx = p3[0] - p0[0]
    dy = p3[1] - p0[1]
    L = math.hypot(dx, dy) or 1.0
    # perpendicular unit vector (left of chord)
    nx, ny = -dy / L, dx / L

    # Bezier control points: distribute along chord with perpendicular
    # offsets to give a smooth bow.
    c1 = (p0[0] + dx * 0.33 + nx * arc * 0.6,
          p0[1] + dy * 0.33 + ny * arc * 0.6)
    c2 = (p0[0] + dx * 0.66 + nx * arc * 1.0,
          p0[1] + dy * 0.66 + ny * arc * 1.0)

    width_fn = WIDTH_FNS[kind]
    pts = _cubic_bezier(p0, c1, c2, p3, n=samples)

    # Move to start with pen up
    t.penup()
    t.goto(p0[0], p0[1])
    t.pendown()

    for (tt, x, y) in pts:
        w = max(1, width_fn(tt, peak))
        t.pensize(w)
        t.goto(x, y)

    t.penup()


# ──────────────────────────────────────────────────────────────────────
# Screen setup
# ──────────────────────────────────────────────────────────────────────

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.tracer(0, 0)
T = turtle.Turtle()


# ──────────────────────────────────────────────────────────────────────
# Tasks
# ──────────────────────────────────────────────────────────────────────

# ── Task 01 | 一 | yi
def task_01():
    reset_turtle(T)
    # Single 横 centered around (0, 0); soft end-caps, slight upward tilt.
    # Length ~360 px so it fills the canvas well.
    p0 = (-180, -8)
    p3 = ( 180,  8)   # faint upward tilt
    draw_brushed(T, "heng", p0, p3, peak=16, arc=2.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_一.png"))


# ── Task 02 | 二 | er
def task_02():
    reset_turtle(T)
    # Top heng (shorter) above center, bottom heng (longer) below.
    # Soft end-discs on both.
    top_y, bot_y = 70, -70
    top_half, bot_half = 110, 170   # bottom longer
    draw_brushed(T, "heng", (-top_half, top_y - 3), (top_half, top_y + 3),
                 peak=14, arc=1.8)
    draw_brushed(T, "heng", (-bot_half, bot_y - 4), (bot_half, bot_y + 4),
                 peak=16, arc=2.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_二.png"))


# ── Task 03 | 三 | san
def task_03():
    reset_turtle(T)
    # Top medium, middle shortest, bottom longest.
    top_y, mid_y, bot_y = 110, 0, -110
    top_half, mid_half, bot_half = 120, 95, 175
    draw_brushed(T, "heng", (-top_half, top_y - 3), (top_half, top_y + 3),
                 peak=14, arc=1.8)
    draw_brushed(T, "heng", (-mid_half, mid_y - 2), (mid_half, mid_y + 2),
                 peak=13, arc=1.5)
    draw_brushed(T, "heng", (-bot_half, bot_y - 4), (bot_half, bot_y + 4),
                 peak=16, arc=2.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_三.png"))


# ── Task 04 | 十 | shi
def task_04():
    reset_turtle(T)
    # 横 then 竖, crossing at center. 竖 extends slightly more below
    # than above.
    # Heng
    draw_brushed(T, "heng", (-170, -5), (170, 5), peak=16, arc=2.0)
    # Shu: top to bottom; from +130 to -180 (slightly more below center)
    draw_brushed(T, "shu", (0, 150), (0, -200), peak=16, arc=0.0)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_十.png"))


# ── Task 05 | 人 | ren
def task_05():
    reset_turtle(T)
    # 撇 starts upper-center and goes lower-LEFT; longer, starts higher.
    # 捺 starts from the apex area and goes lower-RIGHT; heavy tail at
    # lower-right end.  撇 has its head (heavy) at the START.
    apex = (0, 170)

    # 撇: from apex DOWN-LEFT to a lower-left tail. Heavy at start.
    pie_end = (-160, -180)
    draw_brushed(T, "pie", apex, pie_end, peak=18, arc=-22)
    # arc negative = bow to the right of chord (typical 撇 curl)

    # 捺: starts a touch below the apex (so 撇 visually dominates the
    # apex), goes DOWN-RIGHT. Heavy pressed tail at END (lower-right).
    na_start = (10, 110)
    na_end   = (170, -170)
    draw_brushed(T, "na", na_start, na_end, peak=18, arc=14)
    # arc positive = bow to the left of chord → gentle convex outward

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_人.png"))


# ── Task 06 | 八 | ba
def task_06():
    reset_turtle(T)
    # Two diverging strokes with a GAP at the top — no shared apex.
    # Left = 撇 (heavy start upper, fine tail lower-left).
    # Right = 捺 (thin start upper, heavy pressed tail lower-right).

    # 撇 (left)
    pie_start = (-40, 150)
    pie_end   = (-180, -170)
    draw_brushed(T, "pie", pie_start, pie_end, peak=17, arc=-20)

    # 捺 (right)
    na_start = (40, 150)
    na_end   = (180, -170)
    draw_brushed(T, "na", na_start, na_end, peak=18, arc=14)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_八.png"))


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

def main():
    task_01()
    task_02()
    task_03()
    task_04()
    task_05()
    task_06()


if __name__ == "__main__":
    main()
