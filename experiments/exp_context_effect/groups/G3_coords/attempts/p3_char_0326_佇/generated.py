# p3_char_0326_佇 — 佇 (zhù), 7 strokes.
# Decomposition: 亻 (left) + 宁 (right).
#   宁 = 宀 (roof: dot + short-slant + heng-gou) + 丁 (heng + shu-gou).
#
# Revision vs pass 1:
#   Pass 1 used bank ren_pang + bao_gai_tou + ding_char but the roof
#   primitive's raw-PIL scaling produced a runaway heng-gou descender
#   that read as an extra stroke. Under v8 trust-GT posture, inline
#   with thin uniform ink per P12.

from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300


def _p(mx, my, size=CANVAS):
    """math coords (origin center, y up) -> pixel coords."""
    return size / 2 + mx, size / 2 - my


def draw_zhu_stand(t):
    ink = 5  # thin uniform per P12

    # ============================================================
    # LEFT: 亻 (2 strokes) — taking the left ~35% of the canvas.
    # ============================================================
    # S1: 撇 sweeping down-left from upper-right of the radical zone.
    pie_head = _p(-70, 90)
    pie_tail = _p(-100, -50)
    t.line([pie_head, pie_tail], fill=(0, 0, 0), width=ink)

    # S2: 竖 dropping from the pie's mid-shaft, straight down.
    shu_top = _p(-80, 40)
    shu_bot = _p(-80, -100)
    t.line([shu_top, shu_bot], fill=(0, 0, 0), width=ink)

    # ============================================================
    # RIGHT: 宁 (5 strokes) — occupying the right ~55% of the canvas.
    # ============================================================
    # --- 宀 roof block ---
    # S3: top dot 丶 (canonical lean upper-left down to lower-right)
    dot_p0 = _p(20, 115)
    dot_p1 = _p(30, 100)
    t.line([dot_p0, dot_p1], fill=(0, 0, 0), width=ink + 1)

    # S4: short left slanted stroke 丶 (left side of the roof shoulder)
    lslant_p0 = _p(-15, 85)
    lslant_p1 = _p(-25, 60)
    t.line([lslant_p0, lslant_p1], fill=(0, 0, 0), width=ink)

    # S5: 横钩 roof — long heng across the top, small hook drop on right.
    heng_l = _p(-25, 65)
    heng_r = _p(85, 65)
    t.line([heng_l, heng_r], fill=(0, 0, 0), width=ink)
    hook_top = _p(85, 65)
    hook_bot = _p(78, 45)
    t.line([hook_top, hook_bot], fill=(0, 0, 0), width=ink)

    # --- 丁 nail under the roof ---
    # S6: interior heng, spans most of the roof width, sits below roof.
    ding_heng_l = _p(-15, 15)
    ding_heng_r = _p(70, 15)
    t.line([ding_heng_l, ding_heng_r], fill=(0, 0, 0), width=ink)

    # S7: central 竖钩 descending from beneath heng center, small hook left.
    ding_shu_top = _p(30, 15)
    ding_shu_bot = _p(30, -95)
    t.line([ding_shu_top, ding_shu_bot], fill=(0, 0, 0), width=ink)
    hook2_top = _p(30, -95)
    hook2_end = _p(18, -85)
    t.line([hook2_top, hook2_end], fill=(0, 0, 0), width=ink)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_zhu_stand(t)
    out = Path(__file__).parent / "01_佇.png"
    img.save(out)
    print(f"wrote {out}")
