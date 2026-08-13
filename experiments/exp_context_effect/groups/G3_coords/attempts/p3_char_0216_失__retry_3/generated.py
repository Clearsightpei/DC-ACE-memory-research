"""
p3_char_0216_失 retry_3 — G3

TRAJECTORY DIFF (from inspecting all 3 prior PNGs vs GT):

- main FAIL: rendered as 天/矢-like — top area collapsed to a tiny
  hooked mark, missing distinct short heng; whole X sits too low.
- retry_1 FAIL: same class — top mark is a scribble; top heng not
  distinct from the second heng; big X apex reads as one blob on
  middle heng but the top structure never resolves.
- retry_2 FAIL: closer, but the top pie+heng cluster is TOO SMALL
  and cramped — reads as a tiny "+" rather than a clearly separated
  short 丿 crossing a short 一. Also the long pie's head starts too
  close to the middle heng, so the upper half of the character has
  no vertical height between the two hengs and the pie head.

Fixes this attempt:
  (1) Enlarge the top pie: extend it higher (y~55) and longer, so
      it is unambiguously a 丿 shape not a tick.
  (2) Enlarge the top heng: y~100..102, width from x=105 to x=200,
      clearly SHORTER than middle heng but visibly a full heng.
  (3) Push middle heng lower (y~158) and slightly wider (x=50..250)
      so the vertical gap between top-heng and middle-heng is bigger.
  (4) Long 丿: start ABOVE middle heng near (170, 118) — real
      vertical run before it pierces middle heng at ~ (150, 158),
      then sweeps to (55, 278).
  (5) Long 乀: from apex on middle heng at (150, 158) to (255, 272)
      with a gentle downward belly.
  (6) Thin MMH weights (~3.5px) throughout.

# RETRY MEMORY CHECKLIST
# Q1 (errata): errata says "apex on middle heng" (same as 矢).
#   Done — pie/na apex sits at (150, 158) on the middle heng.
# Q2 (form_catalog): X-crossing family (大 template). Reuse continuous-
#   pie-through-heng + separate na-from-crossing recipe.
# Q3 (helpers): kiss_apex REJECTED (contradicts GT — 大 graduation
#   lesson). Hand-render tapered bezier strokes.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def tapered_polyline(points, w_head=4.0, w_tail=3.0):
    if len(points) < 2:
        return
    seg_len = []
    total = 0.0
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        d = math.hypot(dx, dy)
        seg_len.append(d)
        total += d
    covered = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        L = seg_len[i]
        if L <= 0:
            continue
        steps = max(2, int(L * 2))
        for s in range(steps + 1):
            u_local = s / steps
            u_global = (covered + u_local * L) / max(1e-6, total)
            w = w_head * (1 - u_global) + w_tail * u_global
            x = x0 + (x1 - x0) * u_local
            y = y0 + (y1 - y0) * u_local
            _stamp(x, y, w / 2)
        covered += L


def cubic_pts(p0, p1, p2, p3, steps=80):
    out = []
    for i in range(steps + 1):
        u = i / steps
        x = ((1 - u) ** 3 * p0[0] + 3 * (1 - u) ** 2 * u * p1[0]
             + 3 * (1 - u) * u ** 2 * p2[0] + u ** 3 * p3[0])
        y = ((1 - u) ** 3 * p0[1] + 3 * (1 - u) ** 2 * u * p1[1]
             + 3 * (1 - u) * u ** 2 * p2[1] + u ** 3 * p3[1])
        out.append((x, y))
    return out


def draw_shi(dr):
    """失 — 5 strokes: 丿 短 + 一 短 + 一 长 + 丿 长 + 乀."""

    # --- Stroke 1: short top 丿 (piercing above/through top heng) ---
    # Long enough to read as pie: from ~(172, 55) sweeping down-left
    # to ~(133, 118), passing through top-heng y-band.
    s1 = cubic_pts((172, 55), (162, 78), (147, 100), (133, 118), steps=60)
    tapered_polyline(s1, w_head=3.6, w_tail=2.4)

    # --- Stroke 2: short TOP heng (sits under the top of pie) ---
    top_heng = [(105, 103), (150, 102), (200, 100)]
    tapered_polyline(top_heng, w_head=3.0, w_tail=3.8)

    # --- Stroke 3: long MIDDLE heng ---
    mid_heng = [(50, 162), (150, 158), (250, 152)]
    tapered_polyline(mid_heng, w_head=3.4, w_tail=4.2)

    # Crossing pixel on the middle heng (apex of the big X)
    apex = (150, 158)

    # --- Stroke 4: long 丿 (from above middle heng, through apex,
    # sweeping to lower-left) ---
    # Upper part: from (168, 122) to apex, mostly vertical descent
    up = cubic_pts((168, 122), (162, 138), (155, 150), apex, steps=40)
    tapered_polyline(up, w_head=3.2, w_tail=4.2)
    # Lower part: from apex sweeping curved out to lower-left
    down = cubic_pts(apex, (128, 195), (90, 240), (52, 278), steps=90)
    tapered_polyline(down, w_head=4.2, w_tail=2.0)

    # --- Stroke 5: long 乀 from apex sweeping down-right with belly ---
    na = cubic_pts(apex, (185, 200), (225, 245), (258, 272), steps=90)
    tapered_polyline(na, w_head=3.2, w_tail=5.2)


draw_shi(draw)

out_path = ("/Users/peilinwu/Documents/AI memory research/"
            "experiments/exp_context_effect/groups/G3_coords/"
            "attempts/p3_char_0216_失__retry_3/01_失.png")
img.save(out_path)
print(f"wrote {out_path}")
