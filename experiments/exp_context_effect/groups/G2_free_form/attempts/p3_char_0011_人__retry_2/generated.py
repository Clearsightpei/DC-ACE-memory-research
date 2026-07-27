"""Render 人 (person) — two-stroke apex character. Retry #2.

# SIGNATURE CHECK (verbatim from sibling_signature_checklist.md):
# 人 | apex SHARED at same y; both strokes throw outward; 捺 has thick foot | 入 (捺 overhangs)

Prior failures:
- retry_1: apex was too pointy/geometric (curator-blind called it correct but
  human FAILed). Fix: softer meeting point (small joining dab), slight
  rightward bow on 撇.
- retry_0 (original): drawer over-reasoned "small gap" between strokes based
  on handwritten GT — broke apex-shared signature. Fix: SIGNATURE OVERRIDE —
  apex-shared is 人's identity, don't veer to per-GT gap.

This retry: apex SHARED at (150, 88). Small joining dab softens the meeting.
撇 curves leftward with slight rightward bow at top. 捺 sweeps to
bottom-right with taper thin→thick and a broad flat foot.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def sample_bezier(p0, p1, p2, n=200):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        pts.append((x, y))
    return pts


def stroke_taper(pts, w_start, w_end):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / (n - 1) if n > 1 else 0
        r = w_start * (1 - t) + w_end * t
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


# Shared apex — both strokes meet here (SIGNATURE bit).
APEX = (145, 90)

# ---- Stroke 1: 撇 (apex → bottom-left, curves organically) ----
# Small 顿笔 tick at start (upper-right nub before the sweep).
draw.ellipse([APEX[0] - 3, APEX[1] - 6, APEX[0] + 6, APEX[1] + 3], fill="black")

p0 = APEX
p2 = (50, 275)
# Curve bows RIGHTWARD in the upper half then swings left (classic 撇).
p1 = (135, 200)
pie_pts = sample_bezier(p0, p1, p2, n=280)
# 撇 tapers thick-to-thin.
stroke_taper(pie_pts, w_start=4.5, w_end=1.2)

# ---- Stroke 2: 捺 (starts AT apex, sweeps to bottom-right, thin→thick) ----
q0 = APEX
q2 = (270, 258)
# Bow slightly downward (natural sagging 捺 arc).
q1 = (218, 210)
na_pts = sample_bezier(q0, q1, q2, n=280)
# 捺 tapers thin-to-thick.
stroke_taper(na_pts, w_start=1.6, w_end=7.5)

# Soft joining dab at apex to unify the meeting (per retry_1 diagnosis).
ax, ay = APEX
draw.ellipse([ax - 4, ay - 3, ax + 4, ay + 4], fill="black")

# Broad flat terminal foot on 捺 — horizontally elongated dab.
foot_x, foot_y = na_pts[-1]
for k in range(0, 14):
    r = 7.8 - k * 0.35
    if r <= 1:
        break
    draw.ellipse(
        [foot_x + k * 1.2 - r, foot_y - r * 0.5,
         foot_x + k * 1.2 + r, foot_y + r * 0.5],
        fill="black",
    )

out = ("/Users/peilinwu/Documents/AI memory research/experiments/"
       "exp_context_effect/groups/G2_free_form/attempts/"
       "p3_char_0011_人__retry_2/01_人.png")
img.save(out)
print(f"wrote {out}")
