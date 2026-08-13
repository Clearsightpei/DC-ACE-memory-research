# quan_tian_for_LR_left.py — promoted from p3_char_0434_畎 (B12 main A verdict)
# Curator B12 (2026-08-04, position 601).
#
# Compressed 田 for the LEFT slot of L-R compositions. Rendered inline in
# PIL pixel coords (NOT turtle math-coords) so the box slots cleanly into
# ~40% left column without colliding with the right sibling.
#
# Motivating context: 畎 (田 + 犬). Reuse targets: 略 (田+各), 畔 (田+半),
# 畝 (田+亩-abbrev), 畦 (田+圭), 畯 (田+夋), 畹 (田+宛), 畈 (田+反), 畋
# (田+攵) — any L-R compound with 田 on the left.
#
# Why fresh (v13 BANK_DEVIATION rationale): `bi_field_over_ji.py` bakes a
# full-canvas 田 with a 丌 base underneath — that primitive is
# canvas-centered and cannot compress into a left ~40% band without heavy
# transform, and its baked base spills into the right-side slot.
#
# Signature: (d, x_left=30, x_right=125, y_top=100, y_bot=220, w=5)
# All coords are absolute PIL px on a 300x300 canvas. Caller controls the
# box extent by passing x_left/x_right/y_top/y_bot. Line width w=5 matches
# MMH thin-ink GT.
#
# The recipe: 5-stroke 田 = left 竖 + 横折 (top+right) + middle 竖 (thinner) +
# middle 横 (thinner) + bottom 横. The 2px overshoots at heng ends are the
# calligraphic corner-lift that B10's `bai_char_compressed_for_LR` also uses.

from PIL import Image, ImageDraw


def draw_quan_tian_for_LR_left(d, x_left=30, x_right=125,
                                y_top=100, y_bot=220,
                                w=5, wm=4, black=(0, 0, 0)):
    """Compressed 田 for LR-left slot. d = PIL ImageDraw."""
    x_mid = (x_left + x_right) // 2
    y_mid = (y_top + y_bot) // 2

    # S1: left 竖
    d.line([(x_left, y_top), (x_left, y_bot)], fill=black, width=w)
    # S2: 横折 (top heng + right shu). Small overshoots at ends.
    d.line([(x_left - 2, y_top), (x_right + 2, y_top)], fill=black, width=w)
    d.line([(x_right, y_top), (x_right, y_bot)], fill=black, width=w)
    # S3: middle 竖 (thinner)
    d.line([(x_mid, y_top + 3), (x_mid, y_bot - 2)], fill=black, width=wm)
    # S4: middle 横 (thinner)
    d.line([(x_left + 2, y_mid), (x_right - 2, y_mid)], fill=black, width=wm)
    # S5: bottom 横
    d.line([(x_left - 2, y_bot), (x_right + 2, y_bot)], fill=black, width=w)


def main():
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_quan_tian_for_LR_left(d)
    import os
    out = os.path.join(os.path.dirname(__file__), "01_quan_tian_for_LR_left.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
