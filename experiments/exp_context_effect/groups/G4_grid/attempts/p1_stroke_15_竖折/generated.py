"""Attempt: p1_stroke_15_竖折 (G4 — grid-bank memory).

Target: 竖折 — a vertical stroke that turns 90° to the right at its
        bottom end. Description: 竖然后转向右.
        This is the mirror-partner of 横折 (which goes horizontal→
        90°→down). 竖折 goes vertical→90°→right. Canonical use: 山,
        丩, and as the outer corner of 凵, 匚 (rotated).

米字格 anchor plan:
  head    = ('TL', 0.30, 0.15)   — 起笔 upper-left of top row
  corner  = ('BL', 0.30, 0.85)   — 折 corner, bottom-left of bottom row
  tail    = ('BR', 0.85, 0.85)   — end of horizontal, bottom-right

Shape rationale:
  - The 竖 (vertical) segment sits in the left part of the canvas
    (x_frac=0.30 within TL and BL) so that the following 横
    (horizontal) segment has room to travel rightward across the
    bottom band without leaving the canvas.
  - The corner is at BL, y_frac=0.85 — near the bottom of the canvas.
    The vertical spans ~70% of canvas height; the horizontal spans
    ~55% of canvas width. This matches the typical isolated 竖折
    proportion (vertical dominant, horizontal moderate) and mirrors
    how 横折 (my p1_stroke_11 attempt) had horizontal dominant with a
    shorter drop.
  - The turn is a sharp 90° corner, not rounded. In kaishu there is a
    tiny 顿笔 (press-out) bump at the corner where the brush changes
    direction — a small "shoulder" pointing down-right. I render this
    with a filled disc at the corner, drawn on top of both segments.

Width profile:
  - Vertical: near-uniform ~10 px, matching a printed kaishu 竖 with
    no taper (this is 竖折, not 竖折钩 or a tapered 竖).
  - Corner shoulder: filled disc ~13 px (the 顿笔 bump at the elbow).
  - Horizontal: ~10 px throughout, with a mild 收笔 (square ending)
    at the tail. No hook, no rightward taper-to-tip.

Joint spec: single compound stroke, no external joints. The internal
corner is a P-class (piercing / welded) self-joint at BL (0.30, 0.85).
"""

from pathlib import Path
from PIL import Image, ImageDraw


# ---- 米字格 helpers ----------------------------------------------------

CANVAS = 300  # px. PIL pixel coords: (0,0) top-left.
_CELL = CANVAS / 3.0

_CELL_ORIGIN = {
    'TL': (0, 0), 'TC': (1, 0), 'TR': (2, 0),
    'ML': (0, 1), 'C':  (1, 1), 'MR': (2, 1),
    'BL': (0, 2), 'BC': (1, 2), 'BR': (2, 2),
}


def anchor_to_xy(anchor):
    """(cell, x_frac, y_frac) → PIL pixel coords.
    x_frac / y_frac are 0..1 within cell, (0,0) at cell top-left.
    """
    cell, xf, yf = anchor
    col, row = _CELL_ORIGIN[cell]
    return ((col + xf) * _CELL, (row + yf) * _CELL)


# ---- Stroke primitives ------------------------------------------------

def fat_line(draw, p0, p1, width, color=(0, 0, 0)):
    """Line with rounded caps (filled discs at both ends)."""
    draw.line([p0, p1], fill=color, width=width)
    r = width / 2.0
    for (x, y) in (p0, p1):
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)


def draw_shu_zhe(draw, head_anchor, corner_anchor, tail_anchor,
                 v_width=10, h_width=10, shoulder=13, color=(0, 0, 0)):
    """Render 竖折: vertical head→corner, 90° turn, horizontal corner→tail.

    - Vertical drawn from head to corner (top→bottom).
    - Small 顿笔 shoulder disc at the corner (the elbow of the turn).
    - Horizontal drawn from corner to tail (left→right).
    - No hook, no taper-to-tip — 竖折 ends with a square 收笔.
    """
    head = anchor_to_xy(head_anchor)
    corner = anchor_to_xy(corner_anchor)
    tail = anchor_to_xy(tail_anchor)

    # Vertical segment (the 竖)
    fat_line(draw, head, corner, v_width, color)

    # Horizontal segment (the 折 rightward travel)
    fat_line(draw, corner, tail, h_width, color)

    # 顿笔 shoulder disc at the corner (drawn last so it sits on top)
    r = shoulder / 2.0
    cx, cy = corner
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)


# ---- Render -----------------------------------------------------------

OUT_PATH = Path(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G4_grid/attempts/p1_stroke_15_竖折/01_竖折.png"
)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_shu_zhe(
        draw,
        head_anchor=('TL', 0.30, 0.15),
        corner_anchor=('BL', 0.30, 0.85),
        tail_anchor=('BR', 0.85, 0.85),
        v_width=10,
        h_width=10,
        shoulder=13,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (CANVAS, CANVAS), f"expected {CANVAS}x{CANVAS}, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
