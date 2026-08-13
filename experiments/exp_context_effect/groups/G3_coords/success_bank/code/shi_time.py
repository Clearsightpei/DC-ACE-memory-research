# shi_time.py — 时 — promoted from p3_char_0295_时__retry_1 (B10 retry PASS)
# Curator B10 (2026-07-31, position 500).

# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): errata for p3_char_0295_时 says "drawer inlined 寸 without hook;
#   fresh 寸 rendered without hook. Bank-composition-retrieval failure."
#   Fix idea: actually call bank primitives OR carefully inline with hook.
# Q2 (form_catalog): 日 as left radical (tall, ~1:2 aspect); 寸 as right
#   component (heng + shu_gou + dian, thin uniform widths for MMH GT).
# Q3 (helpers): No X-crossing / mirror-pair / apex-kiss needed. This is a
#   straight L-R composition (like 对/付). Widths thin ~5px per P12
#   (MMH GT convention).
#
# TRAJECTORY DIFF
# Prior main FAIL: (a) 日 rendered as thick rectangle w/ correct shape but
#   too small and shifted; (b) 寸 was inline but MISSING the hook — the
#   vertical stroke had no leftward flick at bottom; (c) horizontal top
#   heng of 寸 was ABSENT — only a lonely dian curve and a vertical remained.
# Fixes this attempt:
#   1. Inline both components with thin uniform ~5px lines (MMH-style GT).
#   2. 日 as tall rectangle x=[40,110], y=[55,240], middle bar y=147.
#   3. 寸: heng at y=110 spanning x=[135,265]; shu_gou vertical at x=200
#      from y=85 to y=225 with a leftward hook flick to (~185, 213);
#      dian dot in lower-left pocket around (170, 155).

from PIL import Image, ImageDraw
import os

CANVAS = 300
W = 5  # thin uniform width matching MMH GT


def draw_ri_left(t):
    """Inline 日 on the left — tall rectangle with a middle bar."""
    x_l, x_r = 40, 110
    y_t, y_b = 55, 240
    y_m = 147
    # Stroke 1: left 竖
    t.line([(x_l, y_t), (x_l, y_b)], fill="black", width=W)
    # Stroke 2: 横折 (top + right)
    t.line([(x_l, y_t), (x_r, y_t)], fill="black", width=W)
    t.line([(x_r, y_t), (x_r, y_b)], fill="black", width=W)
    # Stroke 3: middle 横 (slight right gap)
    t.line([(x_l + 2, y_m), (x_r - 4, y_m)], fill="black", width=W)
    # Stroke 4: bottom 横
    t.line([(x_l, y_b), (x_r, y_b)], fill="black", width=W)


def draw_cun_right(t):
    """Inline 寸 on the right — heng + shu_gou + dian."""
    # Stroke 1: 横 (heng) — top horizontal, slight right rise
    heng_left = (135, 118)
    heng_right = (270, 108)
    t.line([heng_left, heng_right], fill="black", width=W)

    # Stroke 2: 竖钩 (shu_gou) — vertical crossing the heng, hook at bottom
    shu_top = (205, 88)
    shu_bot = (205, 235)
    t.line([shu_top, shu_bot], fill="black", width=W)
    # Hook: leftward flick from bottom, curling up-and-left
    hook_tip = (182, 218)
    # Approximate a small curve with two segments
    hook_mid = (198, 232)
    t.line([shu_bot, hook_mid], fill="black", width=W)
    t.line([hook_mid, hook_tip], fill="black", width=W)

    # Stroke 3: 丶 dian — small slanting dot in lower-left of vertical
    dian_start = (170, 148)
    dian_end = (192, 168)
    t.line([dian_start, dian_end], fill="black", width=W + 1)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_ri_left(t)
    draw_cun_right(t)
    return img


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "01_时.png")
    render().save(out)
    print(f"wrote {out}")
