# VISUAL DIFF (retry_2 of p3_char_0176_平)
#
# Prior attempt (retry_1) vs GT:
# 1. Prior TOP renders as a small triangle/tent with two dashes -- a
#    "hut" shape. GT has a short 横 across the top plus a mirror-slanted
#    丷 pair (small dian left + small pie right) sitting just below the
#    top heng. No triangle.
# 2. Prior VERTICAL (shu) descends from top all the way through both
#    horizontals to bottom -- it passes THROUGH the top area. GT shu
#    only descends FROM the main (long) middle heng downward -- the
#    top of the character is 丷 + short heng, then the shu starts at
#    the crossing with the long heng.
# 3. Prior long heng too short, doesn't span like GT's wide crossbar.
#
# Fix plan (per errata + visual diff):
#   1) short top 横  (narrow, y near top)
#   2) left 点  (small ↘ slant, sitting on/above short heng, mirror of #3)
#   3) right 撇 (small ↙ slant, mirror of #2)  --> together = 丷
#   4) long 横  (wide crossbar mid-canvas)
#   5) 竖 descending only from crossbar down to near bottom
#
# RETRY MEMORY CHECKLIST (v7 required for retries)
# Q1 (errata): The fix idea from errata.md says: 丷-style dots should be
#   small mirror-slanted dots ABOVE the top heng, not long descending
#   slashes. Use small w_tail. Prior rerun still failed to cleanly
#   render 丷 + short heng + main heng + shu-descending-only-below-main.
# Q2 (form_catalog): Relevant rows: 丷 mirror-dot pair (like in 兰, 半);
#   long 横 as main crossbar; 竖 partial descend (below crossbar only).
# Q3 (helpers): Mirror-dot pair applies -- 丷 above the short heng.
#   But per B5 lesson: "if helper conflicts with GT, prefer GT". I
#   render inline with PIL for full control of tapered strokes rather
#   than importing helpers (past retries failed even with helpers).

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def tapered(p0, p1, w0, w1, steps=40):
    """Tapered line from p0->p1 with widths w0->w1 (linear)."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = w0 + (w1 - w0) * ((t0 + t1) / 2)
        d.line([(xa, ya), (xb, yb)], fill="black", width=max(1, int(round(w))))

# 1) Short top 横 (short horizontal at top)
tapered((105, 88), (205, 82), 4, 5)

# 2) Left 点 (small dot, slanted ↘, sitting BELOW short heng, well left of center)
#    Keep bottom clearly left of center so 丷 does NOT converge to a point.
tapered((115, 105), (135, 138), 3, 6)

# 3) Right 撇 (small pie, slanted ↙, sitting BELOW short heng, well right of center)
tapered((195, 105), (175, 138), 3, 6)

# 4) Long 横 (main crossbar across full width, mid-canvas)
tapered((45, 168), (270, 165), 5, 6)

# 5) 竖 (vertical) descending from the crossbar down to near bottom, roughly at char center
tapered((158, 168), (156, 285), 6, 5)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0176_平__retry_2/01_平.png")
print("wrote 01_平.png")
