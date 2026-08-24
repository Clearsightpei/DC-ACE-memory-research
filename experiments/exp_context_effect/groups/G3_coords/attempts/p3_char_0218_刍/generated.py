"""
刍 (chu) — 5 strokes.
Structure (from GT):
  1. 撇 (short pie, upper-center)
  2. 横折 (top curved stroke: heng then down-right pie/curve to form top hook)
  3. 短横 (short horizontal in middle)
  4. 横折 (bottom horizontal-fold, forming right side of enclosure with slight hook)
  5. 长横 (long bottom horizontal extending right)

G3: inline PIL rendering. Simple thin lines matching GT's thin uniform stroke widths.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 4  # thin uniform width matching GT

def line(a, b, w=LW):
    d.line([a, b], fill=INK, width=w)

def polyline(pts, w=LW):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w=w)

# --- Stroke 1: short 撇 at upper-center, going down-left ---
polyline([(160, 55), (140, 90)])

# --- Stroke 2: top 横折 / curve — starts upper-left, goes right and down,
#     then curves down-right forming the top "arc" of the character.
#     In GT it looks like a broad 撇 that curves right at the end.
polyline([(95, 80), (130, 105), (170, 130), (190, 155)])

# --- Stroke 3: short 横 inside (middle horizontal) ---
line((110, 165), (185, 165))

# --- Stroke 4: 横折 forming bottom-right hook of the enclosure ---
#     Horizontal top then a short down segment (right wall of box)
polyline([(105, 200), (215, 200), (220, 235)])

# --- Stroke 5: long bottom 横 extending across ---
line((70, 250), (245, 248))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p3_char_0218_刍/01_刍.png")
print("wrote 01_刍.png")
