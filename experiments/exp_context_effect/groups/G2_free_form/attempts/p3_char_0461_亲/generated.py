"""
Render 亲 (qin1) at 300x300, black ink on white.

亲 = 立 (top) + 木 (bottom).  9 strokes.

Structure from GT:
  1. 点  — short slant at top-center (top-left→bottom-right)
  2. 横  — short horizontal directly below the 点
  3. 点  — small left-leaning dot (like left half of 丷)
  4. 撇  — small right-leaning dot / mini-撇 (right half of 丷)
  5. 横  — LONG horizontal, the widest stroke of the character
  6. 横  — medium horizontal (top of 木)
  7. 竖  — vertical drop through 木 center
  8. 撇  — down-left sweep from center of 木
  9. 捺  — down-right S-curve from center of 木

Calligraphic-4 recipe applied:
  - variable-width tapers on every 点/撇/捺
  - bez() curves on 撇 and 捺
  - shoulder dab at 横+竖 crossover of 木
  - no hooks in 亲 (no 钩 stroke)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- 立 top ---

# 1. Top 点 — short slant, thin→thick going down-right
p1 = bez((148, 32), (152, 38), (156, 46), (160, 54), n=30)
stroke(p1, (3, 8))

# 2. Short 横 under the top dot
h_top = bez((105, 72), (140, 70), (180, 70), (215, 74), n=40)
stroke(h_top, (5, 6))

# 3. Left small 点 (leans down-left) — closer to center under top 横
lp = bez((130, 92), (126, 100), (121, 110), (114, 122), n=30)
stroke(lp, (3, 8))

# 4. Right small 撇/点 (leans down-right, mirror)
rp = bez((190, 92), (194, 100), (199, 110), (206, 122), n=30)
stroke(rp, (3, 8))

# 5. Long 横 — widest stroke of the character (base of 立)
h_long = bez((45, 148), (110, 145), (200, 145), (260, 150), n=80)
stroke(h_long, (7, 7))
# thin lead-in and thick end (calligraphic横)
dab(45, 148, 4)
dab(260, 150, 6)

# --- 木 bottom ---

# 6. 横 of 木 — medium horizontal, below the long 横
h_mu = bez((70, 190), (130, 187), (200, 187), (235, 192), n=60)
stroke(h_mu, (6, 6))

# 7. 竖 of 木 — vertical through center
sh = bez((152, 175), (152, 210), (152, 245), (152, 280), n=60)
stroke(sh, (7, 7))

# Shoulder dab at the 横+竖 crossing
dab(152, 189, 5)

# 8. 撇 of 木 — sweeping down-left curve from center of horizontal
pie = bez((150, 200), (135, 225), (115, 250), (85, 280), n=70)
stroke(pie, (8, 3))

# 9. 捺 of 木 — S-curve sweeping down-right with foot flare
na = bez((155, 202), (175, 225), (200, 250), (225, 275), n=70)
stroke(na, (4, 11))
# foot flare
foot = bez((225, 275), (232, 277), (238, 279), (243, 280), n=15)
stroke(foot, (11, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0461_亲/01_亲.png")
