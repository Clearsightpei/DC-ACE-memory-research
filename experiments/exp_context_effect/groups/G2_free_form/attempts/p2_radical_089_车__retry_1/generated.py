"""G2 retry #1 for 车 (4-stroke simplified radical).

Prior fail (see errata p2_radical_089_车): rendered as symmetric 王-like
with three uniform horizontals; top piece was a "撇折 bowl" instead of
the canonical top-lid. Curator fix:
  (1) top-lid = short 横 + shoulder + short 竖-drop on the RIGHT
      (forming a ⊤-like top piece, drawn as ONE 横折 stroke);
  (2) middle 横 = medium length;
  (3) bottom 横 = the LONGEST;
  (4) central 竖 through everything (no hook), extends above the top
      and below the bottom (form_catalog "竖 as through-going axis").

Stroke plan (MMH order for 车 simplified is 4 strokes):
  S1 = top 横折  (short 横 rightward + shoulder + short down-drop 竖)
  S2 = 撇  small down-left flick from just under the top-lid, forming
       the small 十/cross feature INSIDE the top-lid (this is the
       distinctive "middle bar with left flick" feature of simplified 车)
  Actually per canonical simplified 车 (4 strokes): 一 (top 横), 乛
  (the small folded bit — top-right corner), then 十 body… but the GT
  shows the classic simplified 车 as:
     stroke 1: top 横 (short)
     stroke 2: 撇折 look-alike / OR the ⊤-corner
     ...
  The errata's authoritative fix says: 4 strokes = (top-lid 横折) +
  (middle 横) + (bottom 横) + (central 竖). We follow that.

PIL brush-dab technique. Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(int(dist * 3), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# S1: top 横折  — the ⊤-lid = short 横 rightward + shoulder + short
#      down-drop 竖 on the right (this is the SIGNATURE top of 车).
#      Drawn as ONE compound stroke: 横 then shoulder-dab then 竖-drop.
# ---------------------------------------------------------------
# 横 portion — short, up-tilted a touch
lid_h_x0, lid_h_y0 = 110, 75
lid_h_x1, lid_h_y1 = 195, 70
line_dabs(lid_h_x0, lid_h_y0, lid_h_x1, lid_h_y1, r_start=6, r_end=6)
dab(lid_h_x0, lid_h_y0, 7)
# shoulder dab at the corner (小顿)
dab(lid_h_x1, lid_h_y1, 8)
# 竖-drop portion — short vertical dropping from the shoulder
lid_v_x0, lid_v_y0 = lid_h_x1, lid_h_y1
lid_v_x1, lid_v_y1 = 190, 115   # small down-drop (~45 px), slight left lean
line_dabs(lid_v_x0, lid_v_y0, lid_v_x1, lid_v_y1, r_start=6, r_end=5)
dab(lid_v_x1, lid_v_y1, 6)

# ---------------------------------------------------------------
# S2: middle 横 — MEDIUM length, sits at about y=140. Slight up-tilt.
# ---------------------------------------------------------------
mid_x0, mid_y0 = 88, 145
mid_x1, mid_y1 = 218, 138
line_dabs(mid_x0, mid_y0, mid_x1, mid_y1, r_start=6, r_end=6)
dab(mid_x0, mid_y0, 7)
dab(mid_x1, mid_y1, 7)

# ---------------------------------------------------------------
# S3: bottom 横 — the LONGEST. Slight up-tilt. Spans wide.
# ---------------------------------------------------------------
bot_x0, bot_y0 = 40, 210
bot_x1, bot_y1 = 265, 200
line_dabs(bot_x0, bot_y0, bot_x1, bot_y1, r_start=7, r_end=7)
dab(bot_x0, bot_y0, 8)
dab(bot_x1, bot_y1, 8)

# ---------------------------------------------------------------
# S4: central 竖 — through-going axis. Extends ABOVE the top-lid's
#      횡 (by ~15 px) and BELOW the bottom 横 (by ~50 px). No hook —
#      this is 车 not 事. form_catalog "竖 as through-going axis".
# ---------------------------------------------------------------
v_x0, v_y0 = 150, 55
v_x1, v_y1 = 150, 265
line_dabs(v_x0, v_y0, v_x1, v_y1, r_start=6, r_end=6)
dab(v_x0, v_y0, 8)   # 顿 dab at top
dab(v_x1, v_y1, 7)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_089_车__retry_1/01_车.png"
img.save(out)
print("wrote", out)
