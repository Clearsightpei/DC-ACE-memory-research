"""
內 (nèi) — 4 strokes, character p3_char_0121_內.

Structure per form_catalog.md:
  - 冂 bracket: 3-sided ENCLOSE, open bottom, shared corners.
    Two strokes: 竖 (left wall) + 横折钩 (top + right wall + hook).
  - Inside: 人-like body (撇 + 捺), forming the 入-style with 捺
    overhanging (looking at GT, 捺 dips lower than the 撇 base).

Signature bits (from GT inspection):
  - Top-lid extends beyond right wall on top-right corner slightly.
  - Inside 人 is centered horizontally and sits in the lower half
    of the box (~y from 130 to 220).
  - Right-wall bottom has a small hook flick.

Canvas 300x300, PIL, black ink on white.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"


def stroke(points, width=6):
    """Draw a polyline with round joints."""
    d.line(points, fill=INK, width=width, joint="curve")
    # Cap the ends round
    for (x, y) in (points[0], points[-1]):
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# Layout (revised): larger box filling most of the canvas, top lid
# overhanging both walls (calligraphic 冂), inner 人 centered.
#
# Box: left wall x≈75, right wall x≈225, top y≈60, bottom y≈275.
# Top lid overhangs: extends from x≈55 to x≈245 (past both walls).

# --- Stroke 1: 竖 (left wall of 冂)  -----------------------------------
stroke([(75, 65), (72, 275)], width=6)

# --- Stroke 2: 横折钩 (top lid + right wall + small hook) --------------
# Lid overhangs both sides; drops down as right wall; ends with a
# small up-left hook flick at the bottom.
top_left = (55, 68)
top_right = (245, 72)
bot_right = (225, 275)
hook_tip = (210, 262)
stroke([top_left, top_right, bot_right, hook_tip], width=6)

# --- Stroke 3: 撇 (inside, upper-left of inner 人) ---------------------
# Starts near upper-middle of interior, throws down-left toward bottom.
stroke([(150, 130), (105, 245)], width=6)

# --- Stroke 4: 捺 (inside, right leg — 入-style overhanging) ----------
# Starts slightly ABOVE and to the left of the 撇 origin (入 style),
# sweeps down-right past the 撇's baseline. Broad terminal foot.
stroke([(145, 118), (205, 250)], width=6)
# Broad foot at the end of the 捺
d.ellipse((199, 244, 213, 258), fill=INK)

out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0121_內/01_內.png"
)
img.save(out_path)
print(f"Wrote {out_path}")
