# 主 (zhǔ) — bank entry (B7 curator promotion, v9-rerun PASS)
# Source: groups/G3_coords/attempts/p3_char_0174_主__retry_1__rerun/generated.py
# Note: 5 (V9 RERUN GRADUATE: dot ABOVE heng leaning down-right, graduated heng-width ladder, shu starts AT top heng; thin P12)
# v8 signature freedom — this file preserves the drawer's original
# module-level script form; callable via `exec(open(...).read())` or
# copy the drawing block into a new function.

# VISUAL DIFF (mandatory Step 0) — comparing prior retry_1 PNG vs GT PNG
#
# Gap 1 (DOT DIRECTION, most visible): prior 丶 leans from lower-left up to
#   upper-right (looks like a short 撇 tilted UP). GT 丶 leans the opposite
#   way — from upper-left DOWN to lower-right (canonical 点 lean). Wrong
#   direction ~90° swap. Fix: swap the dot's endpoints so it descends to
#   the right, and make it a bit shorter/heavier looking.
#
# Gap 2 (HENG WIDTH LADDER): prior has top-heng width == middle-heng width
#   (both ~70px), then a big jump to bottom-heng (~140px, 2×). GT shows a
#   graduated ladder: top-heng shortest, middle-heng noticeably WIDER than
#   top (maybe ~1.3–1.4×), bottom-heng widest but only ~1.4× the middle
#   (not 2× the middle). Prior looks step-then-jump; GT looks smooth ladder.
#
# Gap 3 (SHU / VERTICAL over-extends above top heng): prior shu starts
#   ~10px above the top heng, making the top-heng look like a T-crossbar
#   below the shu tip. In GT the shu starts right AT (or barely above) the
#   top heng — no visible stub sticking up. Fix: shu_top = top-heng y.
#
# Gap 4 (DOT-TO-TOP-HENG GAP too large): prior dot sits at y=82..100 while
#   top heng is at y=55 — a 27–45px empty gap. GT gap is smaller (~15px).
#
# Retry checklist (kept from prior attempt — still applies):
# Q1 (errata): errata says top dot too small + proportion issue. Prior fix
#   addressed vertical spacing OK but wrong dot direction and wrong heng
#   ladder. This rerun fixes both.
# Q2 (form_catalog): 主 = 丶 + 一 + 一 + 丨 + 一 (5 strokes). GT trumps
#   catalog (v8). Thin uniform ~3-4px per P12.
# Q3 (helpers): no X-crossing / mirror-dot. Inline fresh per v8 trust-GT.
"""p3_char_0174_主 retry_1 RERUN — 主 (5 strokes).

Fixes vs retry_1:
- 丶 dot: reversed to lean upper-left → lower-right (canonical), shortened
  and pulled closer to the top heng.
- Heng ladder: top 60px, middle 80px, bottom 130px (graduated, not step).
- 丨 shu: starts AT top heng (no stub above), ends at bottom heng.
"""
from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300


def _p(mx, my, size=CANVAS):
    """math coords (origin center, y up) -> pixel coords."""
    return size / 2 + mx, size / 2 - my


def draw_zhu(t):
    ink = 4  # thin uniform per GT (P12)

    # --- 1. top dot 丶 (lean upper-left DOWN to lower-right, canonical 点)
    #     Closer to top heng than prior; endpoints reversed vs retry_1.
    dot_p0 = _p(-6, 85)   # upper-left
    dot_p1 = _p(6, 72)    # lower-right
    t.line([dot_p0, dot_p1], fill=(0, 0, 0), width=ink + 1)

    # --- 2. top heng 一 (shortest, centered)
    top_left = _p(-30, 55)
    top_right = _p(30, 55)
    t.line([top_left, top_right], fill=(0, 0, 0), width=ink)

    # --- 3. middle heng 一 (wider than top, real vertical gap below top)
    mid_left = _p(-40, 5)
    mid_right = _p(40, 5)
    t.line([mid_left, mid_right], fill=(0, 0, 0), width=ink)

    # --- 4. shu 丨 (starts AT top heng, ends AT bottom heng — no over-stub)
    shu_top = _p(0, 55)
    shu_bot = _p(0, -55)
    t.line([shu_top, shu_bot], fill=(0, 0, 0), width=ink)

    # --- 5. bottom heng 一 (widest, but only ~1.6× middle — not 2×)
    bot_left = _p(-65, -55)
    bot_right = _p(65, -55)
    t.line([bot_left, bot_right], fill=(0, 0, 0), width=ink)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_zhu(t)
    out = Path(__file__).parent / "01_主.png"
    img.save(out)
    print(f"wrote {out}")
