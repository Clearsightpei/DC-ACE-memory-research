# BANK_DEVIATION
# skipped: zhu_master.py (canvas-centered, no ox/oy — cannot slot into right half)
# reason: 主 needs to sit on the right ~2/3 of the canvas as 往's right component; the frozen bank entry has hardcoded canvas-center positions with no offset support, so a local re-inline is cleaner than exec-and-translate.
# fresh_component: zhu_shifted_right (same graduated heng ladder + reversed dot from zhu_master, translated +55mx and scaled 0.85 for L-R composition)
"""p3_char_0399_往 — 往 (8 strokes).

Structure: 彳 (double-person radical, 3 strokes) on left + 主 (5 strokes) on right.

彳 (left third): two pies stacked (top shorter) + long shu descending from
    the second pie's inner shaft.
主 (right two-thirds): dot leaning UL→LR + graduated heng ladder
    (top narrow, middle wider, bottom widest) with a shu piercing from
    top-heng down to bottom-heng. Recipe carried from zhu_master.py
    (B7 v9 graduate) but shifted right by +55mx, scaled 0.85.

Thin uniform ~4px ink per P12 (MMH GT convention).
"""
from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300


def _p(mx, my, size=CANVAS):
    """math coords (origin center, y up) -> pixel coords."""
    return size / 2 + mx, size / 2 - my


def draw_wang(t):
    ink = 4  # thin uniform per P12

    # ================= 彳 (left, 3 strokes) =================
    # Revision v2: connect pie₁'s tail into pie₂'s upper shaft (were floating
    # apart before); shorten shu to match 主's baseline (was overshooting by
    # ~40px vs bottom heng at y=-47).
    # --- 1. top short 撇 (pie₁): sweeps from upper-right down-left, short.
    t.line([_p(-70, 85), _p(-100, 45)], fill=(0, 0, 0), width=ink)

    # --- 2. main 撇 (pie₂): longer, steeper; head sits near pie₁'s tail so
    #        the two pies read as a stacked pair.
    t.line([_p(-50, 45), _p(-120, -35)], fill=(0, 0, 0), width=ink + 1)

    # --- 3. shu 丨: descends from mid pie₂ shaft down to ~主's baseline.
    t.line([_p(-75, -10), _p(-75, -100)], fill=(0, 0, 0), width=ink)

    # ================= 主 (right, 5 strokes; translated +55mx, scaled 0.85) ==
    # --- 4. top dot 丶 (canonical lean: upper-left DOWN to lower-right)
    dot_p0 = _p(-6 * 0.85 + 55, 85 * 0.85)   # upper-left
    dot_p1 = _p(6 * 0.85 + 55, 72 * 0.85)    # lower-right
    t.line([dot_p0, dot_p1], fill=(0, 0, 0), width=ink + 1)

    # --- 5. top heng (shortest of ladder)
    t.line([_p(-30 * 0.85 + 55, 55 * 0.85),
            _p(30 * 0.85 + 55, 55 * 0.85)], fill=(0, 0, 0), width=ink)

    # --- 6. middle heng (wider than top)
    t.line([_p(-40 * 0.85 + 55, 5 * 0.85),
            _p(40 * 0.85 + 55, 5 * 0.85)], fill=(0, 0, 0), width=ink)

    # --- 7. shu 丨 (starts AT top heng, ends AT bottom heng — no over-stub)
    t.line([_p(0 * 0.85 + 55, 55 * 0.85),
            _p(0 * 0.85 + 55, -55 * 0.85)], fill=(0, 0, 0), width=ink)

    # --- 8. bottom heng (widest)
    t.line([_p(-65 * 0.85 + 55, -55 * 0.85),
            _p(65 * 0.85 + 55, -55 * 0.85)], fill=(0, 0, 0), width=ink)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)
    draw_wang(t)
    out = Path(__file__).parent / "01_往.png"
    img.save(out)
    print(f"wrote {out}")
