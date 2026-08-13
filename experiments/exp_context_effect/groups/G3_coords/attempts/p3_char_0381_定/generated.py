# BANK_DEVIATION
# skipped: bao_gai_tou.py
# reason: bao_gai_tou mixes coord systems internally (heng_gou uses raw
#         pixel oy-offsets while dian/left-tick use math-coord scale-around-
#         center). At scale<1 with a vertical shift, the sub-strokes fly
#         apart — roof stays near y=175 while chimney/tick pull up to
#         y=80-115. Inlining a compact 宀 with unified pixel coords.
# fresh_component: bao_gai_tou_compact_for_ding
#
# p3_char_0381_定 — 定 (dìng), 8 strokes:
#   宀 top (3): dot, 横钩 roof, small left slanted stroke (inlined fresh)
#   疋 bottom (5): 横, 竖, 提, 撇, 平捺
import os, sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from _shared_helpers import variant_na  # noqa: E402

CANVAS = 300


def tline(t, x0, y0, x1, y1, w0, w1, n=24):
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        t.line([(xa, ya), (xb, yb)], fill="black", width=w)


def tbezier(t, p0, p1, p2, w_head, w_tail, n=48):
    def bez(u):
        return (
            (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0],
            (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1],
        )
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        pa = bez(u0)
        pb = bez(u1)
        w = max(1, int(round(w_head + (w_tail - w_head) * u0)))
        t.line([pa, pb], fill="black", width=w)


def draw_ding_top_mian(t):
    """Compact 宀 for 定 top, y band ~35..110, x band ~65..230."""
    # S1: 点 (chimney dot) — small slanted dot at top center
    tline(t, 148, 38, 160, 52, w0=3, w1=8, n=16)
    # S2: 横钩 (roof) — horizontal from (70, 68) to (225, 72), ending in hook
    tline(t, 70, 68, 224, 74, w0=5, w1=8, n=32)
    # 顿笔 at end
    t.ellipse([220, 68, 232, 80], fill="black")
    # 钩 (hook): down-left from (226, 74) to (212, 100)
    tline(t, 226, 74, 210, 100, w0=8, w1=2, n=16)
    # S3: 左点/短撇 — small slanted stroke on left, (72, 68) → (65, 100)
    tline(t, 78, 66, 66, 100, w0=3, w1=7, n=16)


def draw():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # --- TOP: 宀 (inlined) ---
    draw_ding_top_mian(t)

    # --- BOTTOM: 疋 variant, 5 strokes (y band ~135..270) ---

    # S4: 横 (heng) — horizontal x 85..185 at y ~140
    tline(t, 82, 142, 188, 138, w0=4, w1=6, n=32)

    # S5: 竖 (shu) — short vertical inside the 横 at x=115, y=140..178
    tline(t, 115, 142, 115, 180, w0=6, w1=5, n=16)

    # S6: 提 (ti) — rising short stroke from (115, 180) to (172, 164)
    tline(t, 115, 180, 172, 164, w0=7, w1=2, n=20)

    # S7: 撇 (pie) — long curving down-left, in-frame.
    tbezier(t, (158, 150), (108, 210), (60, 268),
            w_head=8, w_tail=2, n=48)

    # S8: 平捺 (ping na) — sweeping stroke down-right with belly.
    variant_na(t, head=(110, 200), tail=(268, 245),
               bow_perp=-16.0, w_head=3.0, w_belly=13.0,
               w_tail=2.0, belly_u=0.70, n=72)

    out = os.path.join(os.path.dirname(__file__), "01_定.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    draw()
