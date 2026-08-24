"""Render 刀 (dāo, knife) — Phase 3, item p3_char_0033_刀, retry #1.

Prior attempt (retry_0) FAILED — reads as 力 / too-boxy. Diagnosis:
- The 撇 crossed the 横 at x≈135 (middle of 横), producing a small
  enclosed "box" in top-right — this is 力/几 topology.
- 横折钩 shu segment was overly vertical/plump, producing 力-style density.

刀 vs 力 signature: In 刀 the 撇 crosses the 横 near the RIGHT end
(close to the shoulder), so no box forms in the upper right — the
top-right region has 撇+shoulder converging near one point.

Fix (retry_1):
- 撇 crosses 横 near x≈165 (much closer to the shoulder at x≈180).
- 撇 top pokes above 横 by ~25 px at x≈170 (top-right).
- 撇 sweeps down-left more prominently.
- 横折钩 body curves as a graceful, slimmer arc; hook flicks up-left.
- Overall: airier, less 力-like density.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_stroke(pts, r_start, r_end):
    dense = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        seg_len = math.hypot(x1 - x0, y1 - y0)
        n = max(2, int(seg_len))
        for k in range(n):
            t = k / n
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(pts[-1])
    N = len(dense) - 1
    for i, (x, y) in enumerate(dense):
        t = i / N if N > 0 else 0
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------- Stroke 1: 横折钩 ----------
# Segment A: top 横 — slight up-tilt. Shorter than 力's 横 to leave
# air, softer entry.
heng_pts = [(65, 90), (75, 84), (130, 80), (180, 78)]
taper_stroke(heng_pts, r_start=4.2, r_end=4.8)

# Shoulder (turn)
shoulder = (186, 82)
dab(shoulder[0], shoulder[1], 5.0)

# Segment B: gracefully swooping descending curve — leans right at
# top then curves back leftward toward the bottom (concave-left,
# swan-neck shape typical of 刀).
shu_pts = [
    (186, 82),
    (192, 120),
    (192, 160),
    (180, 205),
    (162, 245),  # hook base — more leftward than before
]
taper_stroke(shu_pts, r_start=4.8, r_end=3.8)

# Segment C: hook flick — small, up-left
hook_base = (162, 245)
hook_len = 22
hook_dx = -hook_len * math.cos(math.radians(35))
hook_dy = -hook_len * math.sin(math.radians(35))
hook_end = (hook_base[0] + hook_dx, hook_base[1] + hook_dy)
dab(hook_base[0], hook_base[1], 3.8)
taper_stroke([hook_base, hook_end], r_start=3.8, r_end=1.2)

# ---------- Stroke 2: 撇 (body-crossing diagonal) ----------
# Starts clearly ABOVE 横 near top (x≈165, y≈50), crosses 横 near
# right end at x≈158, sweeps down-left to lower-left (x≈45, y≈275).
# Top nub pokes ABOVE the 横 line by ~30 px — critical for 刀 identity.
pie_start = (165, 50)
pie_cross = (158, 80)   # crosses 横 close to shoulder
pie_mid = (105, 170)
pie_end = (45, 275)
taper_stroke(
    [pie_start, pie_cross, pie_mid, pie_end],
    r_start=5.5,
    r_end=1.0,
)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0033_刀__retry_1/01_刀.png"
img.save(out)
print(f"Saved {out}")
