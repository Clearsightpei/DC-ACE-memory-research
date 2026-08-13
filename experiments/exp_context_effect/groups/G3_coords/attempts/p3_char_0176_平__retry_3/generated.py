# TRAJECTORY DIFF (retry_3 of p3_char_0176_平)
#
# GT structure (from reading gt/phase3/平.png):
#   Stroke 1: short 横 at top, y~70, x~95..200
#   Stroke 2: LEFT dot 丶  — slanting ↙ (head near top-center, tail bottom-LEFT)
#   Stroke 3: RIGHT dot 丶 — slanting ↘ (head near top-center, tail bottom-RIGHT)
#     -> together 丷 pair DIVERGES downward (∧ shape / peak at top, feet apart)
#   Stroke 4: long 一 crossbar, y~155, wide (~x=40..275)
#   Stroke 5: 竖 descending from crossbar (y~158) to near bottom (y~285),
#             at horizontal center
#
# FAILED trajectory:
# - main FAIL: rendered top as roof (upside-down tent), no top 横, 丷 style off
# - retry_1 FAIL: had top 横 + small ∧ 丷 but 丷 too small/faint, proportions off
# - retry_2 FAIL: **critical bug — dots inverted**. retry_2 has LEFT dot
#   moving ↘ (115,105)->(135,138) and RIGHT dot moving ↙ (195,105)->(175,138).
#   That makes the pair CONVERGE at bottom (∨) — mirror of the true 丷 which
#   DIVERGES downward (∧). Panel would read as "downward V" not "upward peak".
#
# FIX plan for retry_3:
#   1) Restore top short 横 (kept from retry_2 — this WAS structurally correct)
#   2) FLIP the 丷 dots: LEFT goes ↙ (head upper-mid, tail lower-left);
#      RIGHT goes ↘ (head upper-mid, tail lower-right). Bottoms flare OUT.
#   3) Make dots more prominent (taper heavier at tail, longer travel)
#   4) Keep the long crossbar and descending 竖 as in retry_2 (those were OK)
#
# RETRY MEMORY CHECKLIST (v7 required for retries)
# Q1 (errata): errata.md p3_char_0176_平 says "小 mirror-slanted dots ABOVE the
#   top heng, not long descending slashes; use small w_tail". The rerun addition
#   flagged "reconstruction still didn't cleanly render 丷". My diagnosis is
#   more specific: the 丷 direction was inverted in retry_2. Fix = flip direction.
# Q2 (form_catalog): 丷 mirror-dot pair (兰, 半, 平). Widths thin per P12 (MMH GT).
# Q3 (helpers): mirror_dian_pair *would* apply but B5 lesson: helpers didn't
#   rescue this family; I hand-render inline with correct direction this time.
#   No helper conflict — I'm rejecting because direct control lets me verify
#   the ↙/↘ direction visually before saving.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def tapered(p0, p1, w0, w1, steps=48):
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

# 1) Short top 横 (short horizontal cap, y~72, spanning ~x=100..200)
tapered((100, 74), (200, 70), 4, 5)

# 2) LEFT 点 of 丷 — DIVERGES downward-LEFT.
#    Head at upper-mid-right (near x=142), tail at lower-LEFT (x~118).
#    This is the fix vs retry_2 which had it going the other way.
tapered((142, 92), (118, 132), 3, 8)

# 3) RIGHT 点 of 丷 — DIVERGES downward-RIGHT.
#    Head at upper-mid-left (near x=158), tail at lower-RIGHT (x~182).
tapered((158, 92), (182, 132), 3, 8)

# 4) Long 横 crossbar (wide, mid-canvas y~158)
tapered((42, 160), (272, 156), 5, 7)

# 5) 竖 descending from crossbar down to near bottom (center x)
tapered((156, 158), (154, 286), 7, 5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0176_平__retry_3/01_平.png")
print("wrote 01_平.png")
