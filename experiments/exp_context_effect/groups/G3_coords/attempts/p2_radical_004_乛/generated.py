"""p2_radical_004_乛 (heng gou radical) — G3 attempt, REVISED.

Per P7: 乛 ↔ heng_gou. First render used draw_henggou primitive with
default (0,0,1.0) but result was too heavy and horizontal too wide
vs GT — GT is a thinner, shorter calligraphic curve occupying the
middle horizontal band.

Per TR5: when primitive extent doesn't match, INLINE. Below I inline
the heng_gou recipe with adjusted numeric endpoints (shorter horizontal
~90..205, thinner widths ~5→8, smaller hook).

TR7 sanity check (before render):
- horizontal: (90, 128) → (205, 138) — spans ~115 px, mid-canvas
- 顿笔 blob r=5 at (205,138)
- hook: from (207,140) down-left to (190,168) — short, ~30 px
- All within 300×300 with ~90 px margins each side. OK.
"""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).parent / "01_乛.png"

img = Image.new("RGB", (300, 300), "white")
draw = ImageDraw.Draw(img)

# --- Inlined heng_gou recipe, tuned for the 乛 radical proportions --- #
scale = 1.0
x0, y0 = 90, 128
x1, y1 = 205, 138

# Horizontal 横 — tapered from thin start to thicker end (顿笔)
line_w_start = int(4 * scale)
line_w_end = int(7 * scale)
steps = 20
for i in range(steps):
    t0 = i / steps
    t1 = (i + 1) / steps
    xa = x0 + (x1 - x0) * t0
    ya = y0 + (y1 - y0) * t0
    xb = x0 + (x1 - x0) * t1
    yb = y0 + (y1 - y0) * t1
    w = int(line_w_start + (line_w_end - line_w_start) * t0)
    draw.line([(xa, ya), (xb, yb)], fill="black", width=w)

# 顿笔 blob at horizontal's right end (smaller than primitive default)
r = int(5 * scale)
draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill="black")

# 钩 hook — down-and-to-the-left from 顿笔, short and tapered
hx0 = x1 + 1
hy0 = y1 + 1
hx1 = x1 - int(15 * scale)
hy1 = y1 + int(30 * scale)
hsteps = 12
for i in range(hsteps):
    t0 = i / hsteps
    t1 = (i + 1) / hsteps
    xa = hx0 + (hx1 - hx0) * t0
    ya = hy0 + (hy1 - hy0) * t0
    xb = hx0 + (hx1 - hx0) * t1
    yb = hy0 + (hy1 - hy0) * t1
    w = max(1, int((8 - 7 * t0) * scale))
    draw.line([(xa, ya), (xb, yb)], fill="black", width=w)

img.save(OUT)
print(f"Saved: {OUT}")
