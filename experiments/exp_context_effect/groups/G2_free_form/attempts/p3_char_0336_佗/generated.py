"""
佗 (p3_char_0336_佗) — 5-stroke character = 亻 (left) + 它 (right).

SIGNATURE CHECK (from sibling_signature_checklist.md — 匕 appears as
component of 它-bottom): 匕 top stroke is a 撇 (upper-right→lower-left);
terminal hook flicks UP-and-LEFT. But 它's bottom is actually 匕-like
but is 竖弯钩 (vertical→horizontal→up-left hook). TIER-0 hook table:
竖弯钩 flick UP-and-LEFT (~-105° to -115°).

Composition:
- 亻 on the left (compressed): 撇 + 竖. Roughly x=55..115, y=55..255.
- 它 on the right: 宀 roof (top 点 + left tick + 横钩) + body
  (撇 + 竖弯钩). Roughly x=120..260, y=50..255.

Strokes of 它 (per MMH order):
  1. 点 on top of 宀 (small dot at top-center of 宀)
  2. 左点/竖点 — left-side tick of 宀
  3. 横钩 — long horizontal + right-terminal hook flicking DOWN-LEFT
     (this is the roof; hook flick is short down-inward — 横钩 pattern)
  4. 撇 — short slanting stroke inside, starting under-left of roof
  5. 竖弯钩 — starts as 竖 dropping down, curves rightward at bottom,
     terminal hook flicks UP-and-LEFT (per TIER-0)
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def line_stroke(p0, p1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ============ LEFT: 亻 (compressed for compound) ============
# Compressed vs standalone: slightly narrower, curved 撇 still prominent.
# 撇 (throw): upper-right → lower-left
pie_p0 = (110, 65)
pie_ctrl = (105, 130)
pie_p2 = (55, 235)
dab(pie_p0[0], pie_p0[1], 7)
bezier_stroke(pie_p0, pie_ctrl, pie_p2, r_start=7.5, r_end=1.5,
              steps=500, ease=1.3)

# 竖: starts near midpoint of 撇, drops straight down
shu_top = (95, 130)
shu_bot = (95, 260)
dab(shu_top[0], shu_top[1], 6)
line_stroke(shu_top, shu_bot, r_start=5.5, r_end=6.0, steps=250)
dab(shu_bot[0], shu_bot[1], 6.5)


# ============ RIGHT: 它 (宀 top + body) ============

# ---- Stroke 1: 点 on top of 宀 ----
# small tick, slanting down-right, at top-center of 宀
d1_p0 = (190, 55)
d1_p1 = (196, 62)
d1_p2 = (200, 75)
bezier_stroke(d1_p0, d1_p1, d1_p2, r_start=2.5, r_end=5.5,
              steps=150, ease=0.9)
dab(d1_p2[0], d1_p2[1], 5.5)

# ---- Stroke 2: 左点 (left tick of 宀) ----
# short tick coming down-left near left side of roof
d2_p0 = (145, 82)
d2_p1 = (140, 92)
d2_p2 = (135, 108)
bezier_stroke(d2_p0, d2_p1, d2_p2, r_start=3.0, r_end=5.5,
              steps=150, ease=0.9)
dab(d2_p2[0], d2_p2[1], 5.5)

# ---- Stroke 3: 横钩 (roof top with right-terminal hook) ----
# Long horizontal + short down-left hook at right end.
heng_p0 = (140, 100)
heng_p1 = (250, 100)
# 顿 at start
dab(heng_p0[0], heng_p0[1], 6)
line_stroke(heng_p0, heng_p1, r_start=5.5, r_end=6.5, steps=280)
# small 顿 press
dab(heng_p1[0], heng_p1[1], 7)
# hook flick DOWN-and-LEFT (横钩 pattern: shoulder → down-left tick)
hook_p0 = (250, 100)
hook_p1 = (247, 108)
hook_p2 = (235, 125)
bezier_stroke(hook_p0, hook_p1, hook_p2, r_start=6.5, r_end=1.5,
              steps=180, ease=1.2)

# ---- Stroke 4: 撇 (short inner throw) ----
# starts under-left inside the roof, sweeps down-left short
pie2_p0 = (185, 135)
pie2_ctrl = (175, 165)
pie2_p2 = (150, 215)
dab(pie2_p0[0], pie2_p0[1], 5.5)
bezier_stroke(pie2_p0, pie2_ctrl, pie2_p2, r_start=5.5, r_end=1.5,
              steps=350, ease=1.3)

# ---- Stroke 5: 竖弯钩 (vertical → horizontal-right → hook up-left) ----
# Starts high, drops as 竖, curves rightward along the base, then
# a small hook flicks UP-and-LEFT (TIER-0 rule).
# vertical part
sv_top = (220, 135)
sv_bend_start = (220, 215)
line_stroke(sv_top, sv_bend_start, r_start=5.5, r_end=6.0, steps=220)
# rounded bend: bezier arc from bend_start, through (230, 240),
# to horizontal end (265, 240)
arc_p0 = (220, 215)
arc_p1 = (223, 245)
arc_p2 = (265, 245)
bezier_stroke(arc_p0, arc_p1, arc_p2, r_start=6.0, r_end=6.5,
              steps=260, ease=1.0)
# hook flick UP-and-LEFT from (265, 245) — short, angled ~ -110°
hk_p0 = (265, 245)
hk_p1 = (263, 238)
hk_p2 = (255, 225)
bezier_stroke(hk_p0, hk_p1, hk_p2, r_start=6.5, r_end=1.5,
              steps=180, ease=1.2)


# ---------------- Save ----------------
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0336_佗/01_佗.png"
img.save(out)
print(f"Saved {out}")
