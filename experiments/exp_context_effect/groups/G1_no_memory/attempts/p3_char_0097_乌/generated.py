"""Render 乌 (wū) to 01_乌.png at 300x300.

Structure of 乌 (4 strokes) — matching GT layout:
  1. 撇 — short tick above/left of head
  2. 横折 — top horizontal + right-vertical of the small squarish head
  3. 竖折折钩 — from left of head: down, across middle, down along right,
                 then long hook curving to lower right
  4. 横 — long bottom horizontal

GT observations:
 - Head is small squarish shape upper-center (~x 100-190, y 55-135).
 - Body descends and hooks far to lower right, ending near (245, 240).
 - Long bottom horizontal spans ~x 55..250 at y ~250, slightly below hook.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# --- Stroke 1: 撇 (short tick at top-left of head) ---
line([(110, 45), (100, 62)])

# --- Stroke 2: 横折 — top and right side of the head box ---
line([(112, 48), (190, 55), (192, 130)])

# --- Stroke 3: 竖折折钩 — inner left vert, middle horiz, then long hook ---
# left vertical of head
line([(112, 65), (115, 135)])
# middle horizontal (closes bottom of head)
line([(115, 135), (192, 138)])
# long descending curve/hook down and out to lower right
line([(192, 138), (200, 200), (215, 235), (245, 240), (255, 225)])

# --- Stroke 4: long bottom 横 ---
line([(50, 258), (250, 260)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0097_乌/01_乌.png")
print("wrote 01_乌.png")
