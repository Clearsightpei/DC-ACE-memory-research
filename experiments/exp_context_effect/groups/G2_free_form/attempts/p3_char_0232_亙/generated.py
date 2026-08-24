"""
亙 (gèn) — 6 strokes: top 横, then a 日/亘-like middle shape (竖折/竖 + 横 + 横折),
bottom 横 (longest, slight upward tilt at ends per GT).

Structure per GT:
  - stroke 1: top 横, moderate length, slight upward tilt on right
  - middle 亘-like body: a squarish enclosure with two internal horizontals
      * left 竖 down
      * top 横 across
      * right side: 横折 (down)
      * one internal 横
  - bottom 横: longest, spans full width, slight downward bow

Simplification: render top 横, middle 日-like box with one internal 横,
bottom 横. All in slight brushy PIL lines.
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(pts, width=7):
    """Draw a polyline stroke with rounded joints."""
    d.line(pts, fill=BLACK, width=width, joint="curve")
    r = width // 2
    for (x, y) in pts:
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# --- Top 横 (stroke 1) ---
stroke([(60, 55), (150, 52), (240, 58)], width=6)

# --- Middle 亘-like box body ---
# Left 竖 (down the left side)
stroke([(95, 95), (93, 210)], width=6)

# Top 横 of box
stroke([(95, 95), (210, 95)], width=6)

# Right 横折 (goes down)
stroke([(210, 95), (212, 210)], width=6)

# Internal 横 (middle of box)
stroke([(105, 155), (200, 152)], width=5)

# Small diagonal stroke inside (per GT lower area)
stroke([(115, 165), (170, 205)], width=5)

# Bottom of the box closes it
stroke([(95, 210), (212, 210)], width=5)

# --- Bottom 横 (final stroke, longest, slight bow) ---
stroke([(45, 258), (100, 250), (200, 250), (255, 260)], width=7)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0232_亙/01_亙.png"
)
