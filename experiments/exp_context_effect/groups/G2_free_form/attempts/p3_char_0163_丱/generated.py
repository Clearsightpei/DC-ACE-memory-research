"""
Render 丱 (guàn) to 300x300 PNG. Revision 2.

Re-reading the GT: 丱 shows two mirror-image compact "幺/hook" units
flanking a central gap, plus two very long outer curved verticals.
Left unit ≈ a small "乚" — short downstroke then curve right (ends
with a small flick), placed in the upper-left interior.
Right unit is its mirror.
The two outer strokes are tall and gently arced outward, extending
well above and below the inner hook units.
There is NOT a strong middle horizontal — the inner "hooks" are
what dominate the interior. I'll drop the middle bar.

Stroke plan (5 strokes standard for 丱):
  1. Left inner-top short vertical / dot-hook top (small tick).
  2. Left inner curve — the small 乚-like hook body.
  3. Right inner-top short vertical / dot-hook top (mirror).
  4. Right inner curve — mirror of 2.
  5. Two outer long verticals — drawn as two separate strokes.

Actually 丱 is 5 strokes canonically. Cleaner split:
  A. Left outer long curve (vertical, arcs out left slightly).
  B. Left inner hook (small L-shape opening right).
  C. Right inner hook (small L-shape opening left).
  D. Right outer long curve.
  E. Interior small tick at top center (a small horizontal-ish dot).

Keep it simple.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r=4):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke(points, width_fn):
    n = len(points)
    if n < 2:
        return
    dense = []
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        steps = max(2, int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5))
        for s in range(steps):
            t = s / steps
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    dense.append(points[-1])
    m = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(1, m - 1)
        r = width_fn(t)
        dab(x, y, r)


# --- A. LEFT outer long stroke: tall, slight leftward arc ---
sA = [
    (78, 55),
    (72, 100),
    (68, 155),
    (66, 205),
    (68, 245),
    (72, 270),
]
stroke(sA, lambda t: 4.5 - 1.5 * t)

# --- B. LEFT inner small hook (opens right): short downstroke then curve right, small flick up ---
# Located in upper-left interior. Compact: x ~ 100..135, y ~ 100..160
sB = [
    (108, 100),
    (105, 125),
    (108, 148),
    (120, 160),
    (135, 160),
    (140, 155),  # tiny flick up-left
]
stroke(sB, lambda t: 4.0 - 1.0 * t)

# --- C. RIGHT inner small hook (opens left): mirror of B ---
sC = [
    (198, 100),
    (201, 125),
    (198, 148),
    (186, 160),
    (171, 160),
    (166, 155),
]
stroke(sC, lambda t: 4.0 - 1.0 * t)

# --- D. RIGHT outer long stroke: mirror of A ---
sD = [
    (228, 55),
    (234, 100),
    (238, 155),
    (240, 205),
    (238, 245),
    (234, 270),
]
stroke(sD, lambda t: 4.5 - 1.5 * t)

# --- E. Small interior "tick" at top center (short slanted dot-like mark connecting the two inner tops) ---
# In many renderings of 丱 the two inner tops meet with a short crossbar.
sE = [
    (128, 88),
    (150, 86),
    (172, 88),
]
stroke(sE, lambda t: 3.0)


out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0163_丱/01_丱.png"
img.save(out)
print(f"Saved {out}")
