"""Retry #1 for p3_char_0011_人.

Errata diagnosis for retry_0 (from errata.md):
  Drawer cited form_catalog + sibling-pair table but then OVER-REASONED
  to a "small apex gap" reading from the GT and broke the shared-apex
  signature. Result read as 入 (捺 overhanging) or ambiguous.

Fix (HARD RULE from memory_index.md v7.1 pos 213):
  "Signatures in form_catalog.md's sibling-pair table are IDENTITY BITS."
  For 人 vs 入, the sibling-pair table says:
    人: apex at same y (shared apex)
    入: 捺 starts HIGHER, overhangs 撇
  DO NOT let a perceived GT nuance ("small gap") override the bit.
  Render 人 with BOTH strokes originating at the same apex y.

Approach: copy the successful p2_radical_028_人__retry_1 layout —
shared APEX = (150, 60), 撇 to lower-left, 捺 to lower-right with
thin→thick taper and broad flat foot. For the character (Phase 3)
scale, splay the legs wider so the character fills the 300x300 canvas.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_pt(p0, p1, p2, t):
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    return x, y


# ---- SHARED APEX — the signature bit for 人 ----
APEX = (150, 60)

# ---- Stroke 1: 撇 (left leg) — thick→thin, gentle rightward bow ----
p0 = APEX
p2 = (45, 265)         # wider splay for Phase-3 character scale
ctrl = (130, 175)      # pulled right of chord midpoint → belly bows right
r_start = 9.0
r_end = 1.2

# 顿笔 press at apex
dab(p0[0], p0[1], r_start)

steps = 400
for i in range(steps + 1):
    t = i / steps
    x, y = bezier_pt(p0, ctrl, p2, t)
    r = r_start + (r_end - r_start) * t
    dab(x, y, r)

# ---- Stroke 2: 捺 (right leg) — thin→THICK with broad flat foot ----
# Starts at SAME apex (shared) — the HARD-RULE bit.
q0 = APEX
q2 = (260, 260)        # wide splay to lower-right
qctrl = (195, 180)     # slight downward bow
r0 = 1.8               # thin start at apex
r2 = 10.5              # thick before terminal foot

steps = 400
for i in range(steps + 1):
    t = i / steps
    x, y = bezier_pt(q0, qctrl, q2, t)
    tt = t ** 1.3     # swell more near the end (捺 signature)
    r = r0 + (r2 - r0) * tt
    dab(x, y, r)


def bez_deriv(p0, p1, p2, t):
    return (2 * (1 - t) * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0]),
            2 * (1 - t) * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1]))


# Broad flat terminal foot along tangent direction
dx, dy = bez_deriv(q0, qctrl, q2, 1.0)
mag = math.hypot(dx, dy)
ux, uy = dx / mag, dy / mag

foot_len = 20
foot_steps = 60
r_foot_start = 11.0
r_foot_end = 3.0
for i in range(foot_steps + 1):
    t = i / foot_steps
    x = q2[0] + ux * foot_len * t
    y = q2[1] + uy * foot_len * t
    r = r_foot_start + (r_foot_end - r_foot_start) * t
    dab(x, y, r)


out_path = ("<REPO_ROOT>/experiments/"
            "exp_context_effect/groups/G2_free_form/attempts/"
            "p3_char_0011_人__retry_1/01_人.png")
img.save(out_path)
print("saved", out_path)
