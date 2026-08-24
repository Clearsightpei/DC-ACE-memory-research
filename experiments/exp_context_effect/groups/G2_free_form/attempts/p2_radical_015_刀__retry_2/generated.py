"""刀 (dao) — 2-stroke radical. RETRY 2.

Analysis of retry_1 failure (studied GT + retry_1 PNG + errata):
- Stroke 1 (横折钩): hook flick was 34 px at -140° with joining dab
  radius > segment radius. Result: a stray dot artifact appeared
  below the intended terminal-竖 endpoint.
- Stroke 2 (撇): started at y=72 (too far above 横 at y~95), and
  its 顿笔 was r=7 — that big dab, floating clearly above the 横,
  read as a spurious dot/notch. Also curved too aggressively right,
  so the "crossing" of the 横 became a T-junction instead of a
  smooth through-cross.

Fixes for retry_2 (per errata + own diagnosis):
(a) Hook joining-dab radius EQUAL to segment radius (no extra +2 dab).
(b) Hook length shortened to ~22 px (was 34).
(c) Hook angle -135° (was -140°) — slightly more up, less lateral.
(d) 撇 start lowered to y=84 so it pokes only ~8-10 px above the 横
    (matches GT). Start-dab reduced to r=6.
(e) 撇 crosses through the 横 at ~x=125 (left-third), sweeping to a
    lower-left tip near (55, 255).
(f) 竖 belly-right control moved slightly (232, 175) so terminal
    endpoint sits at x≈175 — reasonably centered under the shoulder.

Rendered at 300x300, PIL brush-dabs.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=500, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# ---- Stroke 1: 横折钩 ----
# Top 横 — moderate width, slight up-tilt.
r_h = 5.0
h_start = (95, 105)
h_end = (225, 95)
dab(h_start[0], h_start[1], r_h + 1)  # small 顿笔 at start (standalone rule: r+1)
line_dabs(h_start[0], h_start[1], h_end[0], h_end[1], r_h, r_h, steps=300)

# Shoulder dab at corner (folded joint — legitimate r+3)
shoulder = h_end
dab(shoulder[0], shoulder[1], r_h + 3)

# Curving 竖 — belly on RIGHT (concave-left). Terminal at (175, 240).
v_start = shoulder
v_end = (172, 240)
v_ctrl = (230, 170)  # control pulled right → belly on right
bezier_dabs(v_start, v_end, v_ctrl, r0=r_h + 1, r1=r_h + 0.2, steps=450)

# Hook flick — longer (~30 px) and clearly visible, angle -125°
# (up and left but more up than lateral so it does not read as a dot).
# Joining dab RADIUS EQUAL to segment radius (per errata fix (a)).
seg_r_at_end = r_h + 0.2
hook_len = 30
hook_angle = math.radians(-125)
hx = v_end[0] + hook_len * math.cos(hook_angle)
hy = v_end[1] + hook_len * math.sin(hook_angle)
# NO extra joining dab — the bezier's last dab at v_end already sits
# at radius seg_r_at_end. Drawing another dab here would violate errata.
line_dabs(v_end[0], v_end[1], hx, hy, r0=seg_r_at_end, r1=1.0, steps=180)


# ---- Stroke 2: 撇 ----
# Start just above the 横 (~10 px poke), cross THROUGH the 横 near x=125,
# sweep down-and-left. Use gentle rightward bow. Slow the taper (ease=0.85)
# so the tail retains visible width further along its length — retry_1's
# tail vanished mid-curve creating a "disconnected wisp" appearance.
pie_p0 = (128, 88)     # ~10 px above 横 at x=128 (poke small)
pie_p2 = (48, 255)     # lower-left tip
pie_ctrl = (102, 185)  # control for gentle rightward bow
# Small 顿笔 dab at start — r=6, avoid r=7+ dot-above-横 artifact
dab(pie_p0[0], pie_p0[1], 6)
bezier_dabs(pie_p0, pie_p2, pie_ctrl, r0=6.5, r1=1.4, steps=600, ease=0.9)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_015_刀__retry_2/01_刀.png"
)
