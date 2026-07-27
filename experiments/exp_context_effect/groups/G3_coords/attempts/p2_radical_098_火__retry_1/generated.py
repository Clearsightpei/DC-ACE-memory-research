"""
火 (huǒ) — 4-stroke radical (retry_1)

Retry fix idea (per errata.md): use the fu.py (父) X-crossing template
with shared apex pixel — inline both 撇 and 捺 with matched taper.

Prior attempt failure modes (from vision):
- 捺 belly too heavy; ink dominates and reads as 人 with tiny dots.
- Side dots too small and mislocated.
- 撇 and 捺 don't share a clean apex — they diverge slightly.

Retry plan (based on fu.py PASS + GT proportions):
  1. Left dot (点/丶) — sits mid-left flanking the central shape,
     slanting down-left. Larger and higher than v1.
  2. Right dot (short 撇) — mid-right, slanting down-left (mirror of
     left but same direction: both dots point toward central shaft).
  3. Central 撇 — starts at (150, 65) PIL top-center, sweeps down-
     left to (75, 265). Uses fu.py's _tb pattern (w_head=9 → 1).
  4. 捺 — starts at (150, 65) PIL (SAME apex pixel as 撇), sweeps
     down-right to (235, 265). Uses fu.py na taper (w_head=2, belly
     15 at u=0.7, tail 3). Note: shares apex per errata fix.

Convention: PIL pixel coords (y grows DOWN), 300x300 canvas.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def _tb(x0, y0, x1, y1, ctrl_perp=0.0, ctrl_along=0.0,
        w_head=8, w_tail=1, belly_pos=1.0, w_belly=None, n=60):
    """Tapered bezier (copied verbatim from fu.py pattern).
    Draws a quadratic bezier from (x0,y0) to (x1,y1) with control point
    offset perpendicular/along the chord by ctrl_perp/ctrl_along, and
    linear width taper from w_head to w_tail (with optional belly).
    """
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = max(1e-6, (dx * dx + dy * dy) ** 0.5)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    cx = mx + nx * ctrl_perp + ux * ctrl_along
    cy = my + ny * ctrl_perp + uy * ctrl_along
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * cx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * cy + u ** 2 * y1
        if w_belly is not None and belly_pos < 1.0:
            if u <= belly_pos:
                w = w_head + (w_belly - w_head) * (u / belly_pos)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly_pos) / (1 - belly_pos))
        else:
            w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


# REVISION vs pass 1:
# - Side dots moved lower and made shorter (GT dots are compact and sit
#   at ~mid-height, flanking not overlapping the central shape).
# - 捺 now starts ~1/3 down the 撇 shaft (NOT from the apex) — GT shows
#   the 捺 crossing the 撇 at mid-height, not sharing the apex. This is
#   the key difference between 火 and 父/人.
# - 撇 slightly softer scoop; keep needle tip.

# ---- Stroke 1: left dot (丶) — sits mid-LEFT flanking shape ----
# Compact, slanting down-left. Head upper-right (thin) → tail thick.
_tb(122, 138, 100, 168, ctrl_perp=-2, w_head=3, w_tail=7, n=30)

# ---- Stroke 2: right dot (short 撇) — mid-RIGHT ----
# Slanting down-LEFT. Thick head upper-right → thin tail lower-left.
_tb(210, 135, 178, 172, ctrl_perp=-3, w_head=7, w_tail=2, n=30)

# ---- Stroke 3: central big 撇 — TOP → bottom-LEFT ----
# Head at (150, 60). Uses fu.py taper.
_tb(150, 60, 75, 265, ctrl_perp=-7, w_head=9, w_tail=1, n=70)

# ---- Stroke 4: 捺 — crosses 撇 at ~1/3 down (NOT apex) ----
# Head lower and slightly RIGHT of the 撇 shaft so 捺 originates from
# an intersection near (155, 115) — the classic 火 crossing geometry
# (unlike 父/人 where they meet at apex).
_tb(155, 115, 240, 265, ctrl_perp=9, w_head=2, w_tail=3,
    belly_pos=0.72, w_belly=14, n=70)


out_path = os.path.join(os.path.dirname(__file__), "01_火.png")
img.save(out_path)
print(f"Wrote {out_path}")
