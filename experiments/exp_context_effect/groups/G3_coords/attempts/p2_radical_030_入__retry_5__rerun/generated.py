# VISUAL DIFF (Step 0 — mandatory before code)
# Prior failed attempt:  attempts/p2_radical_030_入__retry_5/01_入.png
# GT:                    gt/phase2/入.png
#
# Gap 1 — TOPOLOGY (biggest, this is the whole reason 入 keeps failing as 人):
#   Prior renders as two symmetric slanting lines meeting AT a top apex
#   (classic 人 shape). GT's 入 is different: the 捺 does NOT emerge from
#   the very top of the 撇. In GT the 撇's head sits at roughly (150, 85)
#   and its top has a small "hood" curling left; the 捺 emerges from the
#   SIDE of the 撇 at roughly (148, 118) — about 30 px below the pie top.
#   So the 撇's top nub visibly pokes above where the 捺 begins.
#
# Gap 2 — STROKE LENGTH ASYMMETRY:
#   Prior: 撇 and 捺 are roughly equal length, symmetric.
#   GT:    the 捺 clearly extends further right AND lower than the 撇
#          extends left. 捺 dominates. Ratio roughly 撇:捺 ≈ 0.8:1.0.
#   In prior my pie tail was at ~(75, 245) and na tail at ~(220, 245);
#   distance from apex ~120 px each. In GT the pie tail is around
#   (95, 235) (~150 px from head) and na tail (232, 240) (~160 px), with
#   pie head much higher than na head — so pie is longer along its own
#   axis but the na visually sweeps further to the right side of frame.
#
# Gap 3 — LINE WEIGHT / TAPER:
#   Prior: fairly uniform ~6-7 px lines throughout.
#   GT:    calligraphic. Pie has a small thicker head + hood then tapers
#          to a thin tail. Na starts thin at the junction, thickens
#          through the middle, then tapers to a fine tail at the tip.
#          Overall ink weight ~5-8 px (MMH thin per P12, but with taper).
#
# Fix plan:
#   - Render 撇 as a tapered polyline with a small hood at the top (a
#     tiny left-curling head above y=95), then a smooth bezier down to
#     (90, 240). Width 8 -> 3.
#   - Render 捺 as a tapered polyline STARTING at ~(148, 118) — ON the
#     shaft of the 撇, ~30 px below the pie's top — and sweeping down to
#     (232, 240). Slight downward bow. Width 4 -> 9 -> 3 (mid-swell).
#   - Do NOT make the two strokes kiss at an apex. They must not share
#     a top point; the pie's head must sit ABOVE the na's head.

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def _stamp(xy, r):
    x, y = xy
    d.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0))


def bezier_pt(p0, p1, p2, p3, t):
    x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
    y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
    return (x, y)


def tapered_bezier(p0, p1, p2, p3, w_head, w_tail, steps=140, swell=None):
    """Stamp-along-bezier with tapered width. If swell=(t0, w_mid), width
    peaks at t=t0 (mid-stroke) then tapers to w_tail. Used for 捺."""
    for i in range(steps + 1):
        t = i / steps
        pt = bezier_pt(p0, p1, p2, p3, t)
        if swell is None:
            w = w_head + (w_tail - w_head) * t
        else:
            t0, w_mid = swell
            if t <= t0:
                w = w_head + (w_mid - w_head) * (t / t0)
            else:
                w = w_mid + (w_tail - w_mid) * ((t - t0) / (1 - t0))
        _stamp(pt, w / 2.0)


def draw_ru(canvas_draw):
    # === 撇 (pie) — the LEFT stroke, drawn first, with a small hood at top ===
    # Head sits at (150, 85). Hood: tiny curl going slightly left from
    # (155, 88) to (145, 92). Then main body: bezier down to (90, 240).
    #
    # We approximate the hood by starting the bezier a few pixels
    # up-right of the visible head and giving it strong initial leftward
    # curvature so the top nub reads as a "起笔" head.
    p0 = (156, 82)     # tiny hood start (slightly right and above)
    p1 = (146, 100)    # hood pulls left-down
    p2 = (120, 170)    # body bends down-left
    p3 = (90, 240)     # pie tail bottom-left
    tapered_bezier(p0, p1, p2, p3, w_head=8.5, w_tail=2.5, steps=160)

    # === 捺 (na) — the RIGHT stroke ===
    # KEY: head is NOT at the top of pie. It attaches ~30px BELOW pie top,
    # on the pie's shaft. Pie at t=0 is (156, 82), at t≈0.20 the bezier
    # passes near (145, 118). We set na head to (148, 118) so it visibly
    # sprouts from the side of pie, leaving pie's hood above uncovered.
    n0 = (148, 118)
    n1 = (175, 160)   # gentle initial slope
    n2 = (205, 205)   # curves into the swell
    n3 = (232, 240)   # na tail bottom-right (further right than pie tail)
    # Swell mid-stroke so na reads as calligraphic dominant stroke.
    tapered_bezier(n0, n1, n2, n3, w_head=3.5, w_tail=3.0,
                   steps=160, swell=(0.55, 9.0))


draw_ru(d)

out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_030_入__retry_5__rerun/01_入.png"
img.save(out_path)
print(f"wrote {out_path}")
