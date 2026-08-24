"""Attempt: p1_stroke_11_横折 (G4 — grid-bank memory).

Target: 横折 — a horizontal stroke that turns 90° downward at its right
        end (canonical corner-turn stroke of 口, 日, 田, 门 outlines).
        Description: 横然后转90°向下.

米字格 anchor plan:
  head    = ('ML', 0.15, 0.30)   — 起笔 upper-left of mid row
  corner  = ('MR', 0.85, 0.30)   — 折 corner, upper-right of mid row
  tail    = ('BR', 0.85, 0.85)   — end of vertical descent, bottom-right

Shape rationale:
  - The 横 (horizontal) segment sits in the upper part of the mid band
    (y_frac=0.30 within ML and MR) so that the following 竖 (vertical)
    has room to descend into the bottom row without leaving the canvas.
  - The corner is at MR, x_frac=0.85 — right of center, matching the
    typical 横折 proportions where the horizontal is a bit longer than
    the vertical drop (the horizontal spans ~70% of canvas, the drop
    spans ~55%). In many characters the vertical is shorter, but for
    the isolated stroke a 竖 that reaches the bottom row reads more
    clearly as "转 90° 向下" than a short stub.
  - The turn is a sharp 90° corner, not rounded. In kaishu there is a
    tiny 顿笔 (press-out) bump at the corner where the brush changes
    direction; I render this by drawing the horizontal slightly past
    the corner and the vertical starting slightly above the corner,
    with a filled disc at the corner to fatten it visually. This gives
    the characteristic "shoulder" of 横折.

Width profile:
  - Horizontal: near-uniform ~10 px, matching a printed kaishu 横.
  - Corner shoulder: filled disc ~13 px (the 顿笔 bump).
  - Vertical: ~10 px near the top, tapering slightly to ~9 px at the
    tail (a mild 收笔). No hook — this is 横折, not 横折钩.

Joint spec: single compound stroke, no external joints. The internal
corner is a P-class (piercing / welded) self-joint at MR (0.85, 0.30).
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


def draw_heng_zhe(draw, head_anchor, corner_anchor, tail_anchor,
                  h_width=10, v_width=10, shoulder=13, color=(0, 0, 0)):
    """Render 横折: horizontal head→corner, 90° turn, vertical corner→tail.

    - Horizontal drawn from head to corner.
    - Small 顿笔 shoulder disc at the corner.
    - Vertical drawn from corner to tail. Since this is 横折 (no hook,
      no taper-to-tip), width holds nearly constant with a mild
      收笔 at the tail.
    """
    head = anchor_to_xy(head_anchor)
    corner = anchor_to_xy(corner_anchor)
    tail = anchor_to_xy(tail_anchor)

    # Horizontal segment
    fat_line(draw, head, corner, h_width, color)

    # Vertical segment — near-uniform width, single fat line for
    # cleanness. A mild 收笔 disc at the tail keeps the ending square.
    fat_line(draw, corner, tail, v_width, color)

    # 顿笔 shoulder disc at the corner (drawn last so it sits on top)
    r = shoulder / 2.0
    cx, cy = corner
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)


# ---- Render -----------------------------------------------------------

OUT_PATH = Path(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G4_grid/attempts/p1_stroke_11_横折/01_横折.png"
)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe(
        draw,
        head_anchor=('ML', 0.15, 0.30),
        corner_anchor=('MR', 0.85, 0.30),
        tail_anchor=('BR', 0.85, 0.85),
        h_width=10,
        v_width=10,
        shoulder=13,
    )
    img.save(OUT_PATH)
    return img


if __name__ == "__main__":
    img = render()
    assert img.size == (CANVAS, CANVAS), f"expected {CANVAS}x{CANVAS}, got {img.size}"
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")
