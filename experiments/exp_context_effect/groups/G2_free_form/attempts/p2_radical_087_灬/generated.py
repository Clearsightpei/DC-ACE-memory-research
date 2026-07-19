"""
灬 (fire-dots radical, 4 strokes).

Structure: four small dots in a row across the lower band.
Revised (pass 2): GT shows THIN, wiry, more line-like dots — not fat
teardrops. All four are short 撇-style strokes with different lean
angles:
  - dot 1 (leftmost): 撇-style leaning down-and-LEFT strongly.
  - dot 2: near-vertical 撇, slight LEFT lean, thin.
  - dot 3: near-vertical 撇, slight RIGHT lean, thin.
  - dot 4 (rightmost): 反捺-style leaning down-and-RIGHT.

Renderer: PIL brush-dabs. Canvas 300x300 white, black ink,
y grows DOWN. Reduced max radius from ~8 to ~4 to match GT's slender
wire-like dots.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def bezier_dot(p0, p1, p2, r_start, r_end, steps=240, easing=1.0):
    for i in range(steps + 1):
        t = i / steps
        omt = 1 - t
        x = omt * omt * p0[0] + 2 * omt * t * p1[0] + t * t * p2[0]
        y = omt * omt * p0[1] + 2 * omt * t * p1[1] + t * t * p2[1]
        tt = t ** easing
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# --- Dot 1 (leftmost): short 撇 down-and-left ---
# upper-right start, thicker; lower-left tip, sharp
p0_1 = (95, 175)
p1_1 = (88, 195)
p2_1 = (72, 220)
bezier_dot(p0_1, p1_1, p2_1, r_start=4.5, r_end=1.0, steps=260, easing=1.2)

# --- Dot 2: short thin 撇, slight LEFT lean ---
# start upper-right-ish, tip lower-left
p0_2 = (140, 178)
p1_2 = (134, 195)
p2_2 = (128, 218)
bezier_dot(p0_2, p1_2, p2_2, r_start=4.2, r_end=1.0, steps=260, easing=1.2)

# --- Dot 3: short thin 撇, slight LEFT lean (all middle dots in 灬
# canonically lean slightly LEFT; only the last one leans RIGHT) ---
p0_3 = (183, 178)
p1_3 = (177, 195)
p2_3 = (171, 218)
bezier_dot(p0_3, p1_3, p2_3, r_start=4.2, r_end=1.0, steps=260, easing=1.2)

# --- Dot 4 (rightmost): 反捺-style, upper-left -> lower-right, thin->thick ---
p0_4 = (215, 175)
p1_4 = (225, 195)
p2_4 = (245, 220)
bezier_dot(p0_4, p1_4, p2_4, r_start=1.5, r_end=5.0, steps=260, easing=1.3)


out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_087_灬/01_灬.png"
img.save(out)
print("saved:", out)
