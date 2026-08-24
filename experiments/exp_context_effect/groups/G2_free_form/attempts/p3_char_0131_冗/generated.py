"""
冗 (rong) — 4 strokes: 点 + 横钩 (冖 lid) + 撇 + 横折弯钩 (几 body).

memory pointers used:
- form_catalog "冖 | TOP | wide-flat lid, NO top dot" — lid must not
  have a 亠-style top dot; the leftmost mark is a small 点 sitting AT
  the left end of the lid, not floating above it.
- form_catalog "横 as top-lid" (~140–160 px wide, y ≈ 70–90, small
  顿 dabs).
- Bracket-family / legs-splay: 几-body has a 撇 on the left and a
  横折弯钩 on the right; the two legs splay so bottom is wider than
  top. No hook up-and-left (unlike 儿's 竖弯钩) — 几's right leg
  ends with a rightward curve and a small up-hook.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=BLACK, width=width)
    for p in pts:
        d.ellipse([p[0] - width // 2, p[1] - width // 2,
                   p[0] + width // 2, p[1] + width // 2], fill=BLACK)


# ---------- 冖 lid ----------
# Stroke 1: 点 at the left end of the lid (short down-left flick,
# sits AT the lid, not floating above like 亠). Slightly thicker
# and clearly separated from the lid horizontal so it reads as a
# distinct 冖-signature dot.
stroke([(68, 72), (60, 100)], width=9)

# Stroke 2: 横钩 — long 横 across the top, terminal shoulder-hook
# tucking down-left on the right.
lid_pts = [
    (72, 85),        # start (right of the 点)
    (230, 82),       # 横 across
    (238, 105),      # shoulder down (small hook)
    (228, 118),      # hook tip
]
stroke(lid_pts, width=8)

# ---------- 几 body ----------
# Stroke 3: 撇 — from just under the lid on the left, sweeps down and
# curves out-left. Starts around (85, 118) → (55, 260).
pie_pts = [
    (88, 118),
    (82, 165),
    (72, 210),
    (55, 258),
]
stroke(pie_pts, width=8)

# Stroke 4: 横折弯钩 — starts at right under lid, drops as 竖, curves
# right at baseline, then a small up-hook.
zheh_pts = [
    (215, 118),
    (215, 175),
    (218, 225),
    (225, 258),
    (245, 265),      # curve out to bottom-right
    (250, 258),      # small up-hook at end
    (247, 248),
]
stroke(zheh_pts, width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0131_冗/01_冗.png")
