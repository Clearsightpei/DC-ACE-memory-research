"""Render 丱 (guàn) at 300x300 using PIL — revision 1.

Re-read of GT (2nd pass):
- The character has essentially two symmetric halves like mirrored "y"/"h" shapes.
- Left half: a long descending 撇 stroke (curves left, top-right to bottom-left)
  PLUS a small hook shape at mid-height (looks like a tiny "L" opening right).
- Right half: mirror — long descending stroke (curves right) plus a small hook
  at mid-height opening left.
- Between them at the top there's a small vertical/dot? Actually looking again
  the GT's shapes at mid-height look like two small hook-shapes that come UP
  from mid-height and curl. They're not tiny — they extend up and curl at top.

Best decomposition matching GT visually:
- LEFT long stroke: 竖-like, starts near top-center-left, curves left+down,
  ending near bottom-center-left.
- RIGHT long stroke: mirror of left.
- LEFT inner: a small curve like ⌐ mirrored — vertical up then hook right,
  positioned in middle-left interior.
- RIGHT inner: mirror.
- (No center top stroke — I mis-saw before.)

Thin uniform width per P12 for MMH GT match.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 4


def stroke(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")


# --- Left long stroke: starts high near center-left, slants down-and-left,
# then curls slightly back inward at the bottom (like a 撇 with a soft tail).
left_long = [
    (135, 40), (120, 80), (100, 130), (80, 180), (70, 225), (75, 260)
]
stroke(left_long)

# --- Right long stroke: mirror
right_long = [
    (165, 40), (180, 80), (200, 130), (220, 180), (230, 225), (225, 260)
]
stroke(right_long)

# --- Left inner hook: small shape like a tiny 竖 with hook at bottom-right
# Positioned in the middle interior, opening rightward
# It's short vertical then hooks right at bottom
left_inner = [
    (110, 130), (108, 165), (108, 195), (115, 200), (130, 195)
]
stroke(left_inner)

# --- Right inner hook: mirror
right_inner = [
    (190, 130), (192, 165), (192, 195), (185, 200), (170, 195)
]
stroke(right_inner)

# --- Central small stroke (looking at GT there's a tiny vertical or dot at top-center)
# Very small — like a 丶 or short 竖
center = [(150, 55), (150, 85)]
stroke(center)


out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0163_丱/01_丱.png"
img.save(out)
print(f"saved {out}")
