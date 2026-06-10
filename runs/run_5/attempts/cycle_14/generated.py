"""Cycle 14 — 大 / 木 / 不

Drawer fresh-subagent. Reads GT PNGs in ground_truths/cycle_14/,
composes turtle primitives from success_bank, renders 3 PNGs.

Coord convention: tx = px - 400, ty = 300 - py (image 800x600 → turtle (0,0) at image center).
"""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie
from na   import draw as draw_na
from dian import draw as draw_dian


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(90)


# ---------------------------------------------------------------------------
# 大 (dà) — heng on top + 撇/捺 forming X-cross below
#
# GT measurements (image 800x600):
#   heng centerline y_img≈299, x_img∈[251, 524] → tx∈[-149,124], ty≈1
#   apex (top of pie/na) ≈ (370, 182) → turtle (-30, 118)
#   pie tail ≈ (251, 494) → turtle (-149, -194)
#   na kick tip ≈ (581, 478) → turtle (181, -178)
# ---------------------------------------------------------------------------
def draw_da(t):
    # heng: span ~273 px (canonical 400) → scale=0.68. center x=387.5 → tx=-12.
    draw_heng(t, ox=-12, oy=1, scale=0.68)
    # 大 structural read: heng at top, then pie+na cross THROUGH/below heng
    # forming an X whose apex is at or just above the heng. Pie tail aligns
    # roughly with heng's left edge; na kick aligns with heng's right edge.
    # Iter-1 had pie/na too long → looked like "A" with apex floating high
    # above a short heng. Iter-2: shrink so apex sits at heng level, tails
    # extend below heng to match GT vertical reach.
    #
    # Strategy: place apex AT heng (-12, 1) and let pie/na extend downward.
    # GT vertical reach below heng ≈ 494-300 = 194 px → ty_bottom ≈ -194.
    # Canonical pie dy=-380, so to reach -194 from apex at +1, need scale
    # 0.51 (380*0.51 = 194). Same for na.
    s_pie = 0.62
    apex_t = (-12, 35)  # just above heng so the upper sliver crosses heng
    head_c = (150 * s_pie, 200 * s_pie)
    draw_pie(t, ox=apex_t[0]-head_c[0], oy=apex_t[1]-head_c[1], scale=s_pie)
    s_na = 0.62
    head_c_na = (-150 * s_na, 200 * s_na)
    draw_na(t, ox=apex_t[0]-head_c_na[0], oy=apex_t[1]-head_c_na[1], scale=s_na)


# ---------------------------------------------------------------------------
# 木 (mù) — heng + shu through heng midpoint + 撇 from shu midpoint + 点 from shu midpoint
#
# GT measurements:
#   heng centerline y_img≈287, x_img∈[287, 506] → tx∈[-113, 106], ty≈13. center tx=-3.
#   shu: x_img≈398 (tx=-2), y_img∈[176, 522] → ty∈[124, -222]. center ty=-49.
#   pie: from shu near heng (≈398, 287) → tail (248, 461) → turtle ((-2,13)→(-152,-161))
#   dot (短捺-like): from shu near heng (≈398, 287) → (580, 447) → turtle((-2,13)→(180,-147))
# ---------------------------------------------------------------------------
def draw_mu(t):
    # heng: span 219 px → scale=0.55. center tx=-3, ty=13.
    draw_heng(t, ox=-3, oy=13, scale=0.55)
    # shu: span 346 px → scale=0.87 (canonical 400). center tx=-2, ty=-49.
    draw_shu(t, ox=-2, oy=-49, scale=0.87)
    # pie: head at heng/shu intersection (~-2, 13), tail near (-152, -161).
    # GT dx=-150, dy=-174 → roughly equal magnitudes.
    # Canonical dx=-330, dy=-380. Use scale ~0.45.
    s_pie = 0.45
    head_t = (-2, 13)
    head_c = (150 * s_pie, 200 * s_pie)  # (67.5, 90)
    draw_pie(t, ox=head_t[0]-head_c[0], oy=head_t[1]-head_c[1], scale=s_pie)
    # right stroke (短捺/点): from (-2, 13) sweeping to (180, -147).
    # GT dx=182, dy=-160. Use na scaled ~0.45 (short kick-style).
    s_na = 0.45
    head_t_na = (-2, 13)
    head_c_na = (-150 * s_na, 200 * s_na)  # (-67.5, 90)
    draw_na(t, ox=head_t_na[0]-head_c_na[0], oy=head_t_na[1]-head_c_na[1], scale=s_na)


# ---------------------------------------------------------------------------
# 不 (bù) — heng on top + 撇 (from heng's right-middle going down-left)
#         + 竖 (hanging from heng center-right) + 点 (right, at bottom)
#
# GT measurements:
#   heng centerline y_img≈220, x_img∈[270, 551] → tx∈[-130, 151], ty≈80. center tx=10.
#   shu: x_img≈399 (tx=-1), y_img∈[235, 516] → ty∈[65, -216]. center ty=-75.
#   pie: from below heng around (400, 244) → tail (242, 460) → turtle ((0,56)→(-158,-160))
#   dot: comp3 centroid (505, 381) → turtle (105, -81); span y∈[340,430], x∈[449,553]
#         → entry near (455, 345)→turtle(55, -45), tail near (553, 425)→turtle(153,-125)
# ---------------------------------------------------------------------------
def draw_bu(t):
    # heng: span 281 px → scale=0.70. center tx=10, ty=80.
    draw_heng(t, ox=10, oy=80, scale=0.70)
    # 撇: head near (0, 56) (just below heng center), tail near (-158, -160).
    # GT dx=-158, dy=-216. Canonical dx=-330, dy=-380. scale=0.55.
    s_pie = 0.55
    head_t = (0, 56)
    head_c = (150 * s_pie, 200 * s_pie)  # (82.5, 110)
    draw_pie(t, ox=head_t[0]-head_c[0], oy=head_t[1]-head_c[1], scale=s_pie)
    # 竖: from (-1, 65) down to (-1, -216). Length 281. Canonical 400 → scale=0.70.
    # center ty=-75.
    draw_shu(t, ox=-1, oy=-75, scale=0.70)
    # 点 (right dot): in GT 不 the right dot is wide and slanted, going
    # from upper-left (~455, 345) to lower-right (~553, 425) → turtle
    # (55, -45) → (153, -125). That's a long, low diagonal — bigger and
    # lower than canonical dian. Use scale ~2.0 centered at (100, -85).
    draw_dian(t, ox=100, oy=-85, scale=2.0)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.colormode(255)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()

    tasks = [
        ("01_大.png", draw_da),  # 大
        ("02_木.png", draw_mu),  # 木
        ("03_不.png", draw_bu),  # 不
    ]
    for fname, fn in tasks:
        reset(t)
        fn(t)
        screen.update()
        out_path = os.path.join(OUT_DIR, fname)
        save_canvas_to_png(screen, out_path)
        print(f"saved {out_path}")

    screen.bye()


if __name__ == "__main__":
    main()
