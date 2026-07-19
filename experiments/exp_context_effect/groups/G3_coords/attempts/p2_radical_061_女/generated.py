# p2_radical_061_女 (nü) — G3 coord-bank attempt, revision 2.
#
# 女 has 3 strokes (canonical order):
#   1. 撇点 (pie_dian) — starts upper-middle, sweeps down-left, then dot down-right
#   2. 撇 (pie)       — starts upper-right, sweeps long down-left across the body
#   3. 横 (heng)      — horizontal crossbar spanning wide across the middle
#
# Revision-1 diagnosis (from PNG vs GT):
# - The bank `pie` primitive's chord is too steep (110px horiz vs 175px vert):
#   the resulting stroke read as nearly-vertical, not as the wide diagonal
#   sweep 女's second stroke needs. Per TR5, INLINE a shallower 撇 recipe.
# - The bank `pie_dian` output was OK on the pie half but the dot was too
#   small and merged with the pie tail. Nudge dot larger + more separation.
# - The crossbar sat too high (y=155) — GT has it near canvas y=170. Lower.
#
# Layout target (canvas 300x300, +y down):
#   - 撇点 pie: head (170, 60) → curves down-left to turn (120, 155);
#     then dot from (140, 165) swelling to (170, 210).
#   - 撇: head (215, 55), sweeps down-left through (150, 175), tail (55, 260).
#   - 横: y=170, spans x=40..255 (width 215), thickness ~12.

import os

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def draw_nü(t, ox=0, oy=0, scale=1.0):
    """女 radical inlined: 撇点 + long 撇 + 横 crossbar."""

    # --- Stroke 1: 撇点 (pie half + dot half) ---
    # Pie half: quadratic bezier from head (170,60) via (140,120) to turn (120,155).
    pd_head = (170 + ox, 60 + oy)
    pd_ctrl = (140 + ox, 118 + oy)
    pd_end  = (118 + ox, 158 + oy)

    steps = 60
    r_start = 7.5 * scale
    r_end = 1.5 * scale
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * pd_head[0] + 2 * (1 - u) * u * pd_ctrl[0] + u * u * pd_end[0]
        y = (1 - u) ** 2 * pd_head[1] + 2 * (1 - u) * u * pd_ctrl[1] + u * u * pd_end[1]
        r = r_start + (r_end - r_start) * u
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))

    # Dot half: short down-right swell.
    dot_start = (128 + ox, 168 + oy)
    dot_end   = (175 + ox, 215 + oy)
    dot_steps = 30
    r_dstart = 2.5 * scale
    r_dend   = 8.5 * scale
    for i in range(dot_steps + 1):
        u = i / dot_steps
        x = dot_start[0] + (dot_end[0] - dot_start[0]) * u
        y = dot_start[1] + (dot_end[1] - dot_start[1]) * u
        r = r_dstart + (r_dend - r_dstart) * u
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))

    # --- Stroke 2: 撇 — long diagonal sweep, shallower chord than bank pie ---
    # Head thick (215, 55), belly-mid (150, 175), tail thin (55, 260).
    p_head = (215 + ox, 55 + oy)
    p_ctrl = (145 + ox, 170 + oy)   # gentle bow left of chord
    p_tail = (55  + ox, 260 + oy)

    n_seg = 70
    w_head = 9.0 * scale
    w_tail = 1.0
    prev = None
    for i in range(n_seg + 1):
        u = i / n_seg
        x = (1 - u) ** 2 * p_head[0] + 2 * (1 - u) * u * p_ctrl[0] + u * u * p_tail[0]
        y = (1 - u) ** 2 * p_head[1] + 2 * (1 - u) * u * p_ctrl[1] + u * u * p_tail[1]
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (x, y)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))
        prev = (x, y)

    # --- Stroke 3: 横 crossbar, y=170, x from 42 to 258 ---
    h_y = 170 + oy
    h_x0 = 42 + ox
    h_x1 = 258 + ox
    t.line([(h_x0, h_y), (h_x1, h_y)], fill=(0, 0, 0), width=12)


def main():
    out = os.path.join(os.path.dirname(__file__), "01_女.png")
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_nü(t)
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
