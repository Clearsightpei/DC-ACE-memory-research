"""G1 render of 子 (radical, 3 strokes).

Strokes (MMH standard order for 子):
  1) 横撇弯钩 — horizontal at top that turns down-left, then a curve
     down and hook right (the entire "hat + belly" of 子).
  2) 竖钩 — actually 子 has only 2 strokes for the top+body glyph? No,
     子 has 3 strokes: (1) 横撇 hat, (2) 弯钩 curved-down with hook,
     (3) 横 the middle horizontal.
     But standard MMH decomposition: stroke1 = 横撇弯钩 (single stroke,
     combines the top and the belly-hook), stroke2 = 横.
     However 子 is listed as 3-stroke in the brief.
     Fine — most Xinhua sources: 1 横撇, 2 弯钩, 3 横 = 3 strokes.

Approach: render with PIL, 300x300, black ink, white bg.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
T = 6  # ink thickness


def line(a, b, w=T):
    d.line([a, b], fill=INK, width=w)


def polyline(pts, w=T):
    d.line(pts, fill=INK, width=w, joint="curve")


# --- Stroke 1: 横撇 (top hat) ---------------------------------------
# A short horizontal that then turns sharply down-left.
# Top-of-glyph region. Looking at GT the top piece sits roughly y=60..95,
# x=95..190; horizontal goes left->right then hooks down-left.
s1 = [
    (90, 78),    # start left
    (195, 72),   # horizontal to the right, subtle arc
    (175, 110),  # sharp turn down-left (the 撇 tail)
]
polyline(s1, w=T)

# --- Stroke 2: 弯钩 (curved hook, the belly of 子) -------------------
# Mostly vertical stem with a slight leftward lean, ending in a
# small hook that curls back up-left at the bottom.
s2 = [
    (178, 95),
    (170, 130),
    (160, 165),
    (150, 200),
    (140, 235),
    (135, 250),  # bottom of stem
    (120, 248),  # hook curling left-up
    (115, 240),
]
polyline(s2, w=T)

# --- Stroke 3: 横 (the middle horizontal crossbar) -------------------
# Long horizontal crossing the vertical near mid-height.
s3 = [(50, 172), (250, 162)]
polyline(list(s3), w=T)

# Save
out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_082_子/01_子.png"
img.save(out)
print("wrote", out)
