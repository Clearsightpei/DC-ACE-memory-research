"""冊 (cè) — 'volume/book'.
5 strokes in MMH-ish decomposition:
  1. Left frame: long left vertical curving to 撇 at bottom
  2. Left frame: top horizontal + right vertical (横折) — internal divider
  3. Right frame: top horizontal + right vertical with tiny hook (横折钩)
     (this piece and #2 form the two adjacent 冂 shapes)
  4. Right frame: internal vertical (short bottom stub)
  5. Long crossing horizontal through the middle of both frames
GT reference: gt/phase3/冊.png. Inline PIL — bank has no close alias.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5  # medium-thin stroke

# Character bounding: y ~ 55..255, x ~ 45..260
# Two frames side by side around center vertical x=150
# Left frame: x_left=65..145 (right edge shared with center gap)
# Right frame: x=160..245

# --- Stroke 1: left vertical of LEFT frame (curves left at bottom as 撇) ---
# Straight portion from top to ~y=230, then curves out to bottom-left
d.line([(75, 60), (75, 220)], fill=BLACK, width=LW)
# 撇 curve at bottom
d.line([(75, 220), (72, 240), (60, 258), (45, 270)], fill=BLACK, width=LW, joint="curve")

# --- Stroke 2: top-and-right of LEFT frame (横折) ---
# Top horizontal
d.line([(75, 60), (150, 65)], fill=BLACK, width=LW)
# right vertical of left frame
d.line([(150, 65), (148, 245)], fill=BLACK, width=LW)

# --- Stroke 3: top-and-right of RIGHT frame (横折 with mild hook) ---
d.line([(160, 60), (245, 65)], fill=BLACK, width=LW)
d.line([(245, 65), (240, 250)], fill=BLACK, width=LW)
# little hook at bottom-left of right vertical
d.line([(240, 250), (232, 245)], fill=BLACK, width=LW)

# --- Stroke 4: left vertical of RIGHT frame (shorter — internal-ish) ---
d.line([(160, 60), (162, 245)], fill=BLACK, width=LW)

# --- Stroke 5: long horizontal crossing through both frames ---
# passes below the top horizontals, roughly at y=170
d.line([(45, 172), (260, 165)], fill=BLACK, width=LW+1)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0203_冊/01_冊.png")
print("wrote 01_冊.png")
