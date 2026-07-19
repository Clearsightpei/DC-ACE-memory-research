"""饣 (shi, food radical) — 3 strokes.

Decomposition (looking at GT):
  1. 撇 (pie): a diagonal head-stroke starting upper-right, sweeping down-left.
     Occupies upper-left third; head near (160, 60) descending to about (95, 145)
     in PIL top-left px. (Math coords: ox top-right head ~ +10, +90 down to
     roughly -55, +5.)
  2. 横钩 (heng_gou): a short compact horizontal with a hook, starting from
     where the pie tail meets (upper-mid area), running rightward, then
     terminating in a downward-left hook. This forms the belly-top of 饣.
  3. 竖提 (shu_ti): a shorter vertical descending from the hook's bottom
     area, then a flick up-right at the base.

Transformation notes (TR6):
  - pie: standalone bank pie runs (+65,+90) -> (-45,-85). For 饣, we want a
    smaller, upper-left-shifted 撇. Scale ≈ 0.55, offset ox=-25, oy=+30.
    Head ends up around canvas math (+11, +80) i.e. PIL (161, 70); tail
    around math (-50, -17) i.e. PIL (100, 167).
  - heng_gou (raw PIL coord primitive): standalone spans x∈[55,245], y≈125.
    For 饣 we want a small horizontal starting where pie's tail lands,
    at PIL (~100, 150) and ending short at PIL (~180, 160), with the hook
    dropping down-left to PIL (~160, 195). Standalone anchor is (55,120)
    head and (245,130) hook base; we want (100,150) head and (180,160) hook
    base. That is not a simple linear scale — INLINE (per TR5).
  - shu_ti (math-coord primitive): standalone shu_top=(0,+95), shu_bot=
    (0,-85), ti_end=(+95,-25). Standalone occupies a tall vertical. For 饣,
    we need the shu_ti short and offset right + down: scale 0.45, ox=+7,
    oy=-35. That places shu top around math (+7, +8) → PIL (157, 142) and
    shu_bot around math (+7, -73) → PIL (157, 223), ti_end around math
    (+50, -46) → PIL (200, 196). This ties into the horizontal-hook end
    reasonably.
"""

from PIL import Image, ImageDraw
import sys, os

# Ensure bank primitives importable
BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(BANK))

from pie import draw_pie
from shu_ti import draw_shu_ti


CANVAS = 300


def draw_shi_radical(draw):
    # ---------- Stroke 1: 撇 (pie) ----------
    # Use bank primitive. Scale 0.55, ox=-22, oy=+22 (math coords).
    # We want pie tail to land near the heng_gou head at PIL (~105, 150).
    # Standalone tail math (-45,-85); after transform with scale 0.55:
    # (-45*0.55-22, -85*0.55+22) = (-46.75, -24.75) → PIL (103.25, 174.75).
    # Head math (+65,+90); after transform: (+65*0.55-22, +90*0.55+22)
    # = (+13.75, +71.5) → PIL (163.75, 78.5). Good: descending upper-right
    # to lower-left, tail below-left of the heng start (weld-ish).
    draw_pie(draw, ox=-22, oy=+22, scale=0.55)

    # ---------- Stroke 2: 横钩 (heng_gou) — INLINED per TR5 ----------
    # Standalone anchor doesn't linearly scale to what we need. Inline the
    # recipe: a short tapered horizontal with an ending 顿笔 blob and a
    # tapered hook flicking down-left.
    #
    # Head at PIL (~105, 150); end at PIL (~180, 158); hook tip at PIL
    # (~163, 195). All raw PIL coords (top-left origin).
    x0, y0 = 108, 158
    x1, y1 = 178, 165
    w_start = 5
    w_end = 8
    steps = 20
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = int(w_start + (w_end - w_start) * t0)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)
    # 顿笔 blob at horizontal end
    r = 5
    draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill="black")
    # Hook: tapered flick down-left from the blob
    hx0, hy0 = x1 + 1, y1 + 1
    hx1, hy1 = x1 - 14, y1 + 25
    hsteps = 12
    for i in range(hsteps):
        t0 = i / hsteps
        t1 = (i + 1) / hsteps
        xa = hx0 + (hx1 - hx0) * t0
        ya = hy0 + (hy1 - hy0) * t0
        xb = hx0 + (hx1 - hx0) * t1
        yb = hy0 + (hy1 - hy0) * t1
        w = max(1, int(9 - 8 * t0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)

    # ---------- Stroke 3: 竖提 (shu_ti) ----------
    # Standalone shu_top math (0,+95), shu_bot (0,-85), ti_end (+95,-25).
    # We want shu_top at PIL (~140, 180) i.e. math (-10, -30), so it
    # starts below the hook base and to the left, descending vertically
    # to PIL (~140, 235) and then flicking up-right to PIL (~200, 210).
    # Scale 0.35, ox=-10, oy=-63:
    #   shu_top (0*0.35-10, +95*0.35-63) = (-10, -29.75) → PIL (140, 179.75)
    #   shu_bot (0*0.35-10, -85*0.35-63) = (-10, -92.75) → PIL (140, 242.75)
    #   ti_end (+95*0.35-10, -25*0.35-63) = (+23.25, -71.75) → PIL (173.25, 221.75)
    # ti_end is a bit short; bump scale to 0.40:
    #   shu_top (-10, -25) → PIL (140, 175)
    #   shu_bot (-10, -97) → PIL (140, 247)  — too low, canvas margin issue.
    # Compromise: scale 0.38, ox=-8, oy=-58.
    #   shu_top (-8, -21.9) → PIL (142, 171.9)
    #   shu_bot (-8, -90.3) → PIL (142, 240.3)
    #   ti_end (+28.1, -67.5) → PIL (178.1, 217.5)
    draw_shu_ti(draw, ox=-8, oy=-58, scale=0.38)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_shi_radical(draw)
    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_饣.png"
    )
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
