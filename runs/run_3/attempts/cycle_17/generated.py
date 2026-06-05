"""Cycle 17 — 也, 巴, 寸, 万, 太, 几 (smooth-Bezier brushwork)."""
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
    """Cubic Bezier with per-sample pensize. Continuous fluid line."""
    t.penup()
    t.goto(P0)
    t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0] + \
            3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0]
        y = (1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1] + \
            3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1]
        t.pensize(max(1, w_profile(s)))
        t.goto(x, y)
    t.penup()


# Common width profiles ---------------------------------------------------

def heng_w(s):
    # heavy both ends, slightly heavier mid
    return 7 + 2 * (1 - abs(2 * s - 1))


def shu_w(s):
    # heavy both ends
    return 7 + 2 * (1 - abs(2 * s - 1))


def pie_w(s):
    # heavy start, fine end
    return 9 - 7 * s


def na_w(s):
    # fine start, heavy end (flat kick)
    return 2 + 7 * s


def dian_w(s):
    # heavy belly, fine tail
    return 3 + 6 * (1 - s) * (s * 4) if s < 0.5 else 9 - 8 * s


def hook_w(s):
    # for hook tail-arm: heavy at base, fine at tip
    return 7 - 5 * s


def compound_w_thick(s):
    # generic compound: heavy throughout with a 顿笔 swell at corners
    return 7


# ── Task 01 | 也 | yě ────────────────────────────────────────────────
def draw_也(screen, t):
    reset_turtle(t)
    # Composition: three strokes.
    # Stroke 1: 横折钩 — sits INSIDE the 竖弯钩's arc (upper-left area).
    #   short heng from upper-left going right, then drops as a short shu, tiny hook.
    # Heng top-arm
    brushed_bezier(
        t,
        P0=(-160, 140), P1=(-100, 145), P2=(-40, 145), P3=(20, 140),
        w_profile=lambda s: 6 + 2 * (1 - abs(2 * s - 1)),
        samples=80,
    )
    # Shu drop (right side of the 横折钩)
    brushed_bezier(
        t,
        P0=(20, 140), P1=(22, 80), P2=(22, 20), P3=(18, -30),
        w_profile=lambda s: 7 - 2 * s,
        samples=100,
    )
    # Tiny hook to upper-left
    brushed_bezier(
        t,
        P0=(18, -30), P1=(10, -28), P2=(0, -22), P3=(-12, -10),
        w_profile=lambda s: 5 - 3 * s,
        samples=40,
    )

    # Stroke 2: 竖 — short vertical inside, left side of frame
    brushed_bezier(
        t,
        P0=(-110, 100), P1=(-108, 60), P2=(-106, 20), P3=(-104, -20),
        w_profile=shu_w,
        samples=80,
    )

    # Stroke 3: 竖弯钩 — originates UPPER-MIDDLE, sweeps DOWN, curves RIGHT,
    #   long bottom, hook UP at far right. Wraps around the others.
    # Upper-middle start, long shu down, big sweep right, end hook up.
    # Vertical descending portion
    brushed_bezier(
        t,
        P0=(-30, 170), P1=(-32, 90), P2=(-34, 10), P3=(-30, -90),
        w_profile=lambda s: 8 - 2 * s,
        samples=120,
    )
    # Wan portion: sweep right along bottom
    brushed_bezier(
        t,
        P0=(-30, -90), P1=(20, -150), P2=(120, -170), P3=(210, -150),
        w_profile=lambda s: 7 + 1 * (1 - abs(2 * s - 1)),
        samples=120,
    )
    # Hook up at far right
    brushed_bezier(
        t,
        P0=(210, -150), P1=(220, -120), P2=(225, -90), P3=(225, -50),
        w_profile=lambda s: 7 - 5 * s,
        samples=60,
    )

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_也.png"))


# ── Task 02 | 巴 | bā ────────────────────────────────────────────────
def draw_巴(screen, t):
    reset_turtle(t)
    # 巴: small 日-like frame on TOP, BIG 竖弯钩 below extending the vertical
    # extent roughly 2× downward.
    # Frame is in upper portion (y from +60 to +200).
    # Top heng
    brushed_bezier(
        t,
        P0=(-90, 200), P1=(-30, 205), P2=(30, 205), P3=(90, 200),
        w_profile=heng_w,
        samples=80,
    )
    # Left shu of frame
    brushed_bezier(
        t,
        P0=(-90, 200), P1=(-92, 150), P2=(-94, 100), P3=(-95, 60),
        w_profile=shu_w,
        samples=80,
    )
    # Right shu of frame (top right) — short, leads INTO the 竖弯钩 below
    brushed_bezier(
        t,
        P0=(90, 200), P1=(92, 170), P2=(93, 140), P3=(95, 110),
        w_profile=shu_w,
        samples=60,
    )
    # Middle heng inside frame
    brushed_bezier(
        t,
        P0=(-90, 130), P1=(-30, 132), P2=(30, 132), P3=(90, 130),
        w_profile=heng_w,
        samples=60,
    )
    # Bottom heng closing frame
    brushed_bezier(
        t,
        P0=(-95, 60), P1=(-30, 62), P2=(30, 62), P3=(90, 60),
        w_profile=heng_w,
        samples=80,
    )

    # The BIG 竖弯钩 — starts at top-right (continues the right side),
    # drops DEEP below the frame (to y ≈ -200), wraps right, hooks up.
    # Vertical portion: from top of frame all the way down past frame
    brushed_bezier(
        t,
        P0=(95, 110), P1=(95, 40), P2=(95, -60), P3=(90, -180),
        w_profile=lambda s: 8 - 1.5 * s,
        samples=140,
    )
    # Wan: sweep right along the bottom
    brushed_bezier(
        t,
        P0=(90, -180), P1=(140, -220), P2=(200, -230), P3=(250, -210),
        w_profile=lambda s: 7 + 1 * (1 - abs(2 * s - 1)),
        samples=100,
    )
    # Hook up
    brushed_bezier(
        t,
        P0=(250, -210), P1=(258, -180), P2=(262, -150), P3=(262, -110),
        w_profile=lambda s: 7 - 5 * s,
        samples=60,
    )

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_巴.png"))


# ── Task 03 | 寸 | cùn ────────────────────────────────────────────────
def draw_寸(screen, t):
    reset_turtle(t)
    # 寸: 横 on top, 竖钩 down through middle, 点 in TRADITIONAL spot —
    #   below heng, beside 竖钩 on RIGHT side, mid-height.
    # Heng (long top)
    brushed_bezier(
        t,
        P0=(-220, 120), P1=(-100, 125), P2=(80, 125), P3=(200, 120),
        w_profile=heng_w,
        samples=120,
    )
    # 竖钩 — vertical drop, hook left at bottom
    brushed_bezier(
        t,
        P0=(0, 180), P1=(-2, 90), P2=(-4, 0), P3=(-6, -160),
        w_profile=lambda s: 8 - 2 * s,
        samples=140,
    )
    # Hook left at bottom
    brushed_bezier(
        t,
        P0=(-6, -160), P1=(-30, -150), P2=(-55, -130), P3=(-75, -100),
        w_profile=lambda s: 7 - 5 * s,
        samples=50,
    )
    # 点 — traditional spot: right side, below heng, mid-height
    #   (around x≈80, y≈30, tilted ~45°, teardrop, outer heavy)
    brushed_bezier(
        t,
        P0=(60, 70), P1=(80, 50), P2=(100, 30), P3=(120, 10),
        w_profile=lambda s: 3 + 6 * s,  # heavy at outer (end) tip
        samples=50,
    )

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_寸.png"))


# ── Task 04 | 万 | wàn ────────────────────────────────────────────────
def draw_万(screen, t):
    reset_turtle(t)
    # 万: 一 (top heng), 横折弯钩 (right/bottom compound), 撇 (down-left through).
    # Top heng
    brushed_bezier(
        t,
        P0=(-200, 150), P1=(-80, 155), P2=(80, 155), P3=(200, 150),
        w_profile=heng_w,
        samples=120,
    )
    # 横折弯钩 — ONE continuous brushed path:
    #   short top heng (continuing right) → corner (顿笔) → vertical drop →
    #   bottom curve sweeping RIGHT → small upward 钩.
    # Top mini-heng portion of compound (left of corner)
    brushed_bezier(
        t,
        P0=(-40, 60), P1=(20, 62), P2=(80, 62), P3=(140, 58),
        w_profile=lambda s: 7 + 2 * (1 - abs(2 * s - 1)),
        samples=80,
    )
    # Corner 顿笔 + vertical drop (heavy at top for 顿笔 swell)
    brushed_bezier(
        t,
        P0=(140, 58), P1=(138, -10), P2=(130, -80), P3=(115, -150),
        w_profile=lambda s: 9 - 3 * s,
        samples=120,
    )
    # Bottom curve sweeping RIGHT — pronounced curl
    brushed_bezier(
        t,
        P0=(115, -150), P1=(140, -195), P2=(190, -210), P3=(240, -195),
        w_profile=lambda s: 6 + 2 * (1 - abs(2 * s - 1)),
        samples=100,
    )
    # Small upward 钩 at the end
    brushed_bezier(
        t,
        P0=(240, -195), P1=(248, -170), P2=(252, -145), P3=(252, -115),
        w_profile=lambda s: 7 - 5 * s,
        samples=50,
    )

    # 撇 — long diagonal from upper-middle-left through to lower-left
    brushed_bezier(
        t,
        P0=(-20, 130), P1=(-70, 60), P2=(-130, -30), P3=(-200, -150),
        w_profile=pie_w,
        samples=140,
    )

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_万.png"))


# ── Task 05 | 太 | tài ────────────────────────────────────────────────
def draw_太(screen, t):
    reset_turtle(t)
    # 太 = 大 + 点 (lower-center).
    # heng with slight V-dip in the middle (subtle)
    brushed_bezier(
        t,
        P0=(-220, 130), P1=(-90, 115), P2=(90, 115), P3=(220, 130),
        w_profile=heng_w,
        samples=120,
    )
    # 撇 — head above heng middle-left, sweeps through heng to lower-left
    brushed_bezier(
        t,
        P0=(-20, 220), P1=(-70, 100), P2=(-140, -30), P3=(-220, -180),
        w_profile=pie_w,
        samples=160,
    )
    # 捺 — head above heng middle-right, sweeps through heng to lower-right
    # with FLAT horizontal kick at the end
    brushed_bezier(
        t,
        P0=(20, 220), P1=(70, 100), P2=(140, -30), P3=(220, -150),
        w_profile=lambda s: 2 + 7 * s,
        samples=140,
    )
    # Flat kick continuation (small tail) at end of 捺
    brushed_bezier(
        t,
        P0=(220, -150), P1=(240, -155), P2=(260, -158), P3=(280, -160),
        w_profile=lambda s: 9 - 7 * s,
        samples=40,
    )
    # 点 — small dot below the 撇/捺 crossing (lower-center).
    #   The crossing is around (0, 130). Place 点 in lower-center, well below.
    brushed_bezier(
        t,
        P0=(-30, -40), P1=(-15, -55), P2=(5, -70), P3=(30, -90),
        w_profile=lambda s: 3 + 6 * s,  # heavy outer end
        samples=50,
    )

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_太.png"))


# ── Task 06 | 几 | jǐ ────────────────────────────────────────────────
def draw_几(screen, t):
    reset_turtle(t)
    # 几: 撇 (short, upper-left) + 横折弯钩 (right + bottom).
    # 撇 — head at upper-left, sweeps down-left as gentle curve, short
    brushed_bezier(
        t,
        P0=(-110, 180), P1=(-130, 100), P2=(-155, 0), P3=(-180, -120),
        w_profile=pie_w,
        samples=140,
    )
    # 横折弯钩 — ONE continuous compound:
    #   short top heng → corner (顿笔) → vertical drop →
    #   bottom curve right → small upward 钩.
    # Top heng
    brushed_bezier(
        t,
        P0=(-100, 180), P1=(-30, 185), P2=(50, 185), P3=(130, 180),
        w_profile=lambda s: 7 + 2 * (1 - abs(2 * s - 1)),
        samples=80,
    )
    # Corner + vertical drop (heavy at top for 顿笔)
    brushed_bezier(
        t,
        P0=(130, 180), P1=(128, 90), P2=(120, -10), P3=(105, -130),
        w_profile=lambda s: 9 - 3 * s,
        samples=140,
    )
    # Bottom curve sweeping RIGHT — pronounced
    brushed_bezier(
        t,
        P0=(105, -130), P1=(135, -175), P2=(185, -190), P3=(230, -175),
        w_profile=lambda s: 6 + 2 * (1 - abs(2 * s - 1)),
        samples=100,
    )
    # Small upward 钩
    brushed_bezier(
        t,
        P0=(230, -175), P1=(238, -150), P2=(242, -125), P3=(242, -95),
        w_profile=lambda s: 7 - 5 * s,
        samples=50,
    )

    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_几.png"))


# Main --------------------------------------------------------------------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    draw_也(screen, t)
    draw_巴(screen, t)
    draw_寸(screen, t)
    draw_万(screen, t)
    draw_太(screen, t)
    draw_几(screen, t)


if __name__ == "__main__":
    main()
