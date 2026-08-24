"""
Render 马 (horse) — 3-stroke simplified form.

Revised (pass 2):
  - Enlarge the upper box, move it toward center.
  - Make the 竖折折钩 stroke: left wall, first fold (middle horizontal),
    then a clearly extended long horizontal ending in a hook flick.
  - Bottom 一 extends left of the character and passes right through.
"""

from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 6

def line(p0, p1, w=W):
    d.line([p0, p1], fill=BLACK, width=w)

# ---- Stroke 1: 横折 (top edge + right wall of upper box) ----
# top edge, slightly rising to the right
line((95, 90), (200, 82))
# right wall descending; note in GT it curves outward slightly, but
# a straight-ish line is fine
line((200, 82), (210, 165))

# ---- Stroke 2: 竖折折钩 ----
# (a) left wall of upper box
line((90, 88), (85, 165))
# (b) middle horizontal — bottom edge of upper box
line((85, 165), (210, 162))
# (c) after the fold at right, stroke turns down slightly then goes
#     right-and-down forming a long sweeping stroke, then hooks
#     upward at the end. In simplified 马 the right side extends
#     down further and terminates with an upward-left hook.
line((210, 162), (235, 235))
# hook flick — sharp up-left at the terminal
line((235, 235), (218, 220))

# ---- Stroke 3: long bottom 一 crossing under ----
line((45, 250), (230, 245))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0085_马/01_马.png")
print("Saved 01_马.png (revised)")
