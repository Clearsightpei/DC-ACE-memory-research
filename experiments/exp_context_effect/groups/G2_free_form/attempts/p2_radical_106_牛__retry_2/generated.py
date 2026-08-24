"""
p2_radical_106_牛 retry_2

Errata fix (B3 note):
  Prior fails: top 横 and bottom 横 too similar in length -> reads as 午 or ambiguous.
  APPLY "move the knob further" rule:
    top 横 ~65 px (~40% of bottom); bottom 横 ~165 px.
  Sibling risk: 午 (has short 撇 lid + short 横 + long 横 + 竖).
  Distinguishing 牛 from 午: 牛 stroke 1 = short 撇 attached tightly to left of upper 横;
  the two 横 are stacked with UPPER very short and LOWER very long.
  Plus 竖 extends BELOW the bottom 横 with meaningful length.

Layout (300x300 canvas, math-image coords y grows DOWN):
  Stroke 1 (撇):  short down-left flick, top around (135, 60) -> (100, 100)
  Stroke 2 (横):  short top 横 at y=105, from x=100 to x=175  (length ~75 px, sits ABOVE middle)
  Stroke 3 (横):  long bottom 横 at y=175, from x=55 to x=245 (length ~190 px)
  Stroke 4 (竖):  long central 竖 x=150, from y=80 down to y=270 (crosses both 横s, extends below)

Cross-refs:
  form_catalog "竖 as through-going axis"
  form_catalog "横 as top-vs-bottom length-differentiator"
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def taper_line(p0, p1, r0, r1, steps=80):
    """Draw a stroke by dabbing circles of interpolated radius along the segment."""
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# --- Stroke 1: 撇 (short flick, upper-right -> lower-left) ---
# Small lid on the upper-left of the top 横.
taper_line((140, 62), (100, 108), r0=4.5, r1=1.5, steps=60)

# --- Stroke 2: top 横 (SHORT) ---
# From just right of the 撇's tip, extending rightward.
# length ~75 px (upper 横 much shorter than lower).
taper_line((100, 108), (178, 100), r0=3.0, r1=3.5, steps=60)
# small terminal press
draw.ellipse((175, 96, 183, 104), fill="black")

# --- Stroke 3: bottom 横 (LONG) ---
# The dominant horizontal. length ~190 px (65 vs 190 ~= 34%).
taper_line((52, 178), (248, 172), r0=3.0, r1=3.8, steps=100)
# terminal presses at both ends
draw.ellipse((48, 174, 58, 184), fill="black")
draw.ellipse((243, 168, 253, 178), fill="black")

# --- Stroke 4: 竖 (through-going axis) ---
# Vertical passes through both 横s and extends well below.
taper_line((150, 82), (150, 272), r0=3.5, r1=3.0, steps=120)
# small terminal press top
draw.ellipse((147, 79, 153, 85), fill="black")

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_106_牛__retry_2/01_牛.png"
)
print("wrote 01_牛.png")
