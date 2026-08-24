"""
p3_char_0101_亓 — G2 attempt.

亓 (qí) — 4 strokes:
  1. 一 (short top horizontal) — centered near top
  2. 一 (long horizontal) — below the first, forms the roof
  3. 丿 (left leg) — descends from the underside of the long 一, curves left
  4. 丨 (right vertical) — descends straight down from right portion of long 一

Silhouette: top-heavy roof with two legs splayed under it (like 元 minus
the top). Aspect ~1:1 within an inner square. Legs are shorter than the
horizontal is wide.

Not on sibling_signature_checklist.md.
Free-form G2 draw: derive directly from GT.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)


def brush_line(draw, pts, width=10):
    """Draw a polyline with rounded caps by dabbing circles + drawing lines."""
    if len(pts) < 2:
        return
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        draw.line([(x1, y1), (x2, y2)], fill=INK, width=width)
    r = width // 2
    for x, y in pts:
        draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


# --- Stroke 1: short top 一 (dot-like short horizontal) ---
# Centered horizontally, near top. Slight upward tilt to the right.
brush_line(d, [(115, 80), (175, 74)], width=9)

# --- Stroke 2: long 一 (main roof) ---
# Wide, slight upward tilt.
brush_line(d, [(55, 130), (250, 122)], width=11)

# --- Stroke 3: 丿 left leg ---
# Starts just under the long 一 on the left side, sweeps down and left, ending near bottom.
# A gentle curve — use several points for a smooth 撇.
left_leg = [
    (95, 138),
    (90, 165),
    (82, 200),
    (72, 235),
    (60, 265),
]
brush_line(d, left_leg, width=10)

# --- Stroke 4: 丨 right vertical ---
# Straight down from the right portion of the long 一.
brush_line(d, [(195, 138), (195, 265)], width=10)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0101_亓/01_亓.png"
)
print("wrote 01_亓.png")
