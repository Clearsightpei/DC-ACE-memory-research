"""
p2_radical_042_巛 — retry_2 (revised)

Consulted memory:
- memory_index.md: no direct entry for 巛 in HOT LOOKUP or sibling table.
  Not in sibling_signature_checklist.md.
- errata.md entry for 042_巛: each stroke = short top piece + curving
  body swinging down. GT is three ㄑ-shapes with a two-segment kink.
- retry_1 rendered as three parallel plain curves (no kink) — FAIL.
- First pass of this retry_2 had the knee bulging RIGHT — wrong side.
  GT has each stroke shaped like a mirrored "<" (i.e. ")") — top
  drifts down-LEFT, bends at knee, bottom continues down with slight
  leftward drift. Fixed below.

Approach: three near-identical strokes, evenly spaced.
Each = two connected segments with knee on the LEFT (opens left):
  P0 (top, mildly right) → P1 (knee, further left, ~1/3 down) →
  P2 (bottom, slightly right of knee — so the lower segment drops
  mostly vertical with a mild rightward or straight drift).
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
STROKE_W = 6


def stroke(cx):
    """One ")"-shape centered horizontally around cx.

    GT shape per stroke:
      - short top segment slanting down-and-LEFT
      - bend at knee (knee is the LEFTMOST point of the stroke)
      - long bottom segment descending mostly-vertical with slight
        leftward drift (ending slightly left of knee's x, or ~=)
    """
    y_top = 90
    y_knee = 140
    y_bot = 240

    p0 = (cx + 8, y_top)      # top tip, right
    p1 = (cx - 6, y_knee)     # knee, leftmost — opens to LEFT
    p2 = (cx - 4, y_bot)      # bottom, near-knee-x or slightly right

    d.line([p0, p1], fill=INK, width=STROKE_W)
    d.line([p1, p2], fill=INK, width=STROKE_W)
    # Round caps at endpoints and knee
    for (x, y) in (p0, p1, p2):
        r = STROKE_W // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# Three strokes, evenly spaced ~55 px apart, centered on canvas
stroke(105)
stroke(160)
stroke(215)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_042_巛__retry_2/01_巛.png"
)
print("wrote 01_巛.png")
