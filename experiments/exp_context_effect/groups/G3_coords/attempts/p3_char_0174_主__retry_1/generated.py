# RETRY MEMORY CHECKLIST (B4-B5 v7 evolution)
# Q1 (errata): errata says top dot too small, three hengs too close, bottom heng
#   only slightly wider than middle. Fix: match GT spacing - dot standalone,
#   top heng short, middle heng same width, bottom heng only SLIGHTLY wider,
#   shu passes through all three with proper vertical spacing.
# Q2 (form_catalog): 主 = dot + 3 hengs + piercing shu. Under v8, GT trumps
#   catalog. GT shows thin uniform strokes (~3-4px), moderate spacing between
#   hengs, bottom heng wider but not dramatically so.
# Q3 (helpers): No X-crossing / mirror-dot pair here. Just standard heng+shu
#   composition. No helper needed - inline fresh per v8 trust-GT posture.
#   Under v8's format unlock (errata note position 351-400) proportion/dot
#   placement is exactly the failure category to fix free-form.
"""p3_char_0174_主 retry 1 — 主 (5 strokes).

Rewrite from scratch matching GT spacing:
- 丶 top dot: tilted down-left slash, small, sits well above top heng
- 一 top heng: short, thin
- 一 middle heng: same width as top, real vertical gap below top
- 丨 shu: vertical, pierces through all three hengs
- 一 bottom heng: only slightly wider than the others (NOT dramatically)
Uniform thin ink ~3-4px per GT (P12).
"""
from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300


def _p(mx, my, size=CANVAS):
    """math coords (origin center, y up) -> pixel coords."""
    return size / 2 + mx, size / 2 - my


def draw_zhu(t):
    ink = 4  # thin uniform per GT

    # --- 1. top dot 丶 (tilted down-left short dash, sits well above top heng)
    dot_p0 = _p(6, 100)
    dot_p1 = _p(-6, 82)
    t.line([dot_p0, dot_p1], fill=(0, 0, 0), width=ink)

    # --- 2. top heng 一 (short, centered)
    top_left = _p(-35, 55)
    top_right = _p(35, 55)
    t.line([top_left, top_right], fill=(0, 0, 0), width=ink)

    # --- 3. middle heng 一 (same width as top, gap below top)
    mid_left = _p(-35, 5)
    mid_right = _p(35, 5)
    t.line([mid_left, mid_right], fill=(0, 0, 0), width=ink)

    # --- 4. shu 丨 (vertical, pierces top heng down through bottom heng level)
    shu_top = _p(0, 65)
    shu_bot = _p(0, -55)
    t.line([shu_top, shu_bot], fill=(0, 0, 0), width=ink)

    # --- 5. bottom heng 一 (only slightly wider than the others)
    bot_left = _p(-70, -55)
    bot_right = _p(70, -55)
    t.line([bot_left, bot_right], fill=(0, 0, 0), width=ink)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_zhu(t)
    out = Path(__file__).parent / "01_主.png"
    img.save(out)
    print(f"wrote {out}")
