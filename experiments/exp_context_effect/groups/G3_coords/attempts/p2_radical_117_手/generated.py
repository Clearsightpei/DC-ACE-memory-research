# p2_radical_117_手 (shǒu, "hand") — 4 strokes.
# GT shows:
#   1. 撇 — short slanting curve at top, going from upper-right down-left
#          (fairly short compared to a full-scale pie).
#   2. 短横 — short horizontal near top, crossing/touching the 撇 tail.
#   3. 长横 — longer horizontal in the middle.
#   4. 竖钩 — vertical shaft down the centre, hook flicks up-left.
#
# Bank use decisions (TR1, TR8 inline-fresh test):
# - heng primitive: matches both hengs well after uniform scaling.
#   Use bank at scale ~0.35 (short heng) and ~0.55 (long heng).
# - shu_gou primitive: matches the central vertical + hook well.
#   Use bank at scale ~0.85.
# - pie primitive: TOO diagonal for 手's short top 撇 (per P10).
#   The 撇 here is short and mostly angled ~60° from horizontal,
#   only ~50-60 px long. Bank's pie head sits at (+65,+90) → too far
#   right/high for our target. INLINE FRESH as one tapered bezier.
#
# Math coords: origin at (150,150), +y up.
# Chosen anchors on the 300x300 canvas (math coords):
#   短横: center ≈ (+5,  +50), length ~90 px, so scale 0.45.
#   长横: center ≈ (-5,  +5),  length ~150 px, so scale 0.75.
#   竖钩: shaft from y≈+45 down to y≈-70, hook flicks left at bottom.
#         Bank shu_gou half_len = 90*scale. To span y∈[-70,+45] (115 px)
#         set scale ≈ 0.64, centered at (ox=+5, oy≈-13).
#   撇 (inlined): head at (+30, +85), tail at (-20, +45), curved slightly.

import os
import sys

from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK_CODE = os.path.abspath(
    os.path.join(_HERE, "..", "..", "success_bank", "code")
)
if _BANK_CODE not in sys.path:
    sys.path.insert(0, _BANK_CODE)

from heng import draw_heng          # noqa: E402
from shu_gou import draw_shu_gou    # noqa: E402


CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def draw_pie_short(t, head_math, tail_math, bow=-8.0, w_head=8.0, w_tail=1.0,
                   n_segments=48):
    """Inline-fresh 撇: tapered bezier from head (thick) to tail (thin).
    head_math, tail_math: (x, y) in math coords.
    bow: perpendicular offset for control point (negative = curve left).
    """
    x0, y0 = head_math
    x1, y1 = tail_math
    # Control point: midpoint of chord, pushed perpendicular by `bow`.
    mx = (x0 + x1) / 2.0 + bow
    my = (y0 + y1) / 2.0 - 3.0  # tiny downward push for the 撇 belly
    prev_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_shou(t, ox=0.0, oy=0.0, scale=1.0):
    """手 = 撇 (inlined) + 短横 (bank) + 长横 (bank) + 竖钩 (bank)."""

    # Stroke 1: 撇 (short, top). Inline-fresh per TR8 (P10: bank pie too
    # diagonal & too long for this short top 撇). Head upper-right, tail
    # curves down and to the LEFT, tail lands near left end of 短横
    # (which is centered at (+5, +50), extending x∈[-40,+50]).
    # Head math (+35, +95), tail math (-30, +45). Strong left-bowing curl.
    draw_pie_short(
        t,
        head_math=(ox + 35.0 * scale, oy + 95.0 * scale),
        tail_math=(ox - 30.0 * scale, oy + 45.0 * scale),
        bow=-14.0 * scale,
        w_head=7.0 * scale,
        w_tail=1.0,
    )

    # Stroke 2: 短横 (top, short) — center approx (+5, +50).
    # Uses bank heng: canonical length 200, so scale 0.45 → ~90 px.
    draw_heng(t, ox=ox + 5.0 * scale, oy=oy + 50.0 * scale, scale=0.45 * scale)

    # Stroke 3: 长横 (middle, longer) — center approx (-5, +5).
    # Bank heng scale 0.75 → ~150 px.
    draw_heng(t, ox=ox - 5.0 * scale, oy=oy + 5.0 * scale, scale=0.75 * scale)

    # Stroke 4: 竖钩 (center vertical + hook). Shaft spans y≈+45 down to y≈-70.
    # Bank shu_gou half_len=90*scale → scale 0.64 gives ~115 px shaft.
    # Center of shaft is y = ((+45)+(-70))/2 = -12.5. So oy≈-13.
    # Slight rightward offset ox=+5 to center relative to long heng.
    draw_shu_gou(t, ox=ox + 5.0 * scale, oy=oy - 13.0 * scale, scale=0.64 * scale)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_shou(t)
    out = os.path.join(_HERE, "01_手.png")
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
