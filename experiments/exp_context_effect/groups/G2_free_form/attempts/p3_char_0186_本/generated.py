"""
本 (běn) — 木 + short horizontal mark near bottom of the vertical.

# SIGNATURE CHECK (from sibling_signature_checklist.md, 木 family):
#   木 base = 一 (top 横) + 竖 + 人-body (撇+捺)
#   本 adds a SHORT lower 横, positioned NEAR THE BOTTOM of the 竖
#     (marks the "root" — 本义: tree root).
#   Distinguisher vs 木: presence of the small lower 横.
#   Distinguisher vs 未/末: 未/末 have TWO full-width 横 above the
#     branching; 本 has ONE full 横 up top + one SHORT stub below.
#   Distinguisher vs 术: 术 has a 点 upper-right; 本 does not.

Stroke order (MMH-standard):
  1. Top 横 (long)
  2. 竖 (vertical through center)
  3. 撇 (left-down diagonal from near top of vertical, below 横)
  4. 捺 (right-down diagonal from near top of vertical, below 横)
  5. Short 横 near the bottom of the 竖 (the root mark)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 9  # brush width

# --- Layout (米字格 eyeball) ---
# Top 横: y ~ 95, x from ~40 to ~260  (long, spans most of width)
# Vertical: x = 150, y from ~70 (slight cap above 横) to ~275
# Branching point (撇/捺 origin): near where 竖 meets 横, y ~ 100–105
# 撇: from (150, 105) sweeping down-left to (~50, 260)
# 捺: from (150, 105) sweeping down-right to (~250, 260)
# Short root 横: y ~ 245, x from ~115 to ~185 (short stub, centered)

# 1) Top 横 — long, slight rightward-upward tilt then settle
d.line([(40, 100), (260, 92)], fill=BLACK, width=INK)

# 2) 竖 — full-length vertical, small cap poking above 横
d.line([(150, 72), (150, 278)], fill=BLACK, width=INK)

# 3) 撇 — from below the 横 crossing, sweeping down-left
# Bezier-ish: sample via short segments
pie_pts = [
    (150, 108),
    (128, 140),
    (108, 175),
    (88, 210),
    (65, 250),
    (45, 275),
]
for i in range(len(pie_pts) - 1):
    d.line([pie_pts[i], pie_pts[i + 1]], fill=BLACK, width=INK)

# 4) 捺 — from below the 横 crossing, sweeping down-right (thicker foot)
na_pts = [
    (150, 108),
    (172, 140),
    (195, 175),
    (218, 210),
    (245, 250),
    (268, 268),
]
for i in range(len(na_pts) - 1):
    # emulate thickening toward the foot
    w = INK + (i // 2)
    d.line([na_pts[i], na_pts[i + 1]], fill=BLACK, width=w)

# 5) Short root 横 — near bottom of 竖 (the distinguishing mark)
d.line([(115, 248), (185, 248)], fill=BLACK, width=INK)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0186_本/01_本.png"
)
print("wrote 01_本.png")
