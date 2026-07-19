"""巾 (jin, 3画 radical) — G3 coord-format render.

Structure per GT:
  1) Short top 竖 (small vertical head) at top-center-left of the enclosure.
  2) 横折钩 — the top horizontal bar joins into a right vertical shaft ending
     in a small up-and-left hook. Forms the top+right of the box.
  3) A long central 竖 that starts near the top-left corner of the enclosure
     and descends WELL BELOW the enclosure (this is the distinguishing
     tail of 巾 vs 冂).

Bank primitives used (all with deliberate ox/oy/scale per TR1/TR6):
  - draw_shu for the short head vertical (very short, tiny scale)
  - draw_heng_zhe_gou for the right-and-top envelope
  - inline the long central 竖 (bank shu is uniform 12px 200 long — we need
    a taller line here that extends past the enclosure, so we inline it
    per TR5 rather than force-stretching).

Math coords (center origin, +y up). Canvas 300x300.
"""

import sys, os
_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from shu import draw_shu
from heng_zhe_gou import draw_heng_zhe_gou

CANVAS = 300
IMG = Image.new("RGB", (CANVAS, CANVAS), "white")
DRAW = ImageDraw.Draw(IMG)


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


# ---------------------------------------------------------------------------
# 1) Top short 竖 (small head) — the little vertical nub above the enclosure
#    top-left corner.
#    Design: length ~30px, thickness 8px.
#    Position (math coords): center around (-38, +80), so it extends from
#      y=+95 (top) down to y=+65 (meeting the horizontal of heng_zhe_gou).
#    Using bank shu (canonical 200 long): scale = 30/200 = 0.15 -- but that
#    would make thickness = 12*0.15 ~ 2px (too thin).
#    Per TR5, small scale breaks brushwork proportions. INLINE instead.

def draw_top_nub():
    # Inline short vertical stroke — length ~28 px, thickness 8 px.
    # Sits above the top-left corner of the enclosure.
    x_top, y_top = _to_pixel(-70, 90)
    x_bot, y_bot = _to_pixel(-70, 62)
    DRAW.line([(x_top, y_top), (x_bot, y_bot)], fill=(0, 0, 0), width=8)


# ---------------------------------------------------------------------------
# 2) 横折钩 — top horizontal spans the enclosure top; folds down into a
#    right vertical shaft that hooks left at the bottom.
#    Canonical heng_zhe_gou (scale=1):
#      p_h_start (-90, +60), p_corner (+80, +60), p_v_end (+80, -70).
#      Width h ~180 px, height ~130 px.
#    For 巾: we want top ~ y=+60, right ~ x=+55, corner should sit near
#    (+55, +60), horizontal starts around x=-40 (matching top nub column).
#    So we want a smaller heng_zhe_gou centered so that:
#      h_start_x ≈ -40, corner_x ≈ +55, corner_y ≈ +60, v_end_y ≈ -50.
#    Try scale = 0.55:
#      h_start = (-49.5, +33), corner = (+44, +33), v_end = (+44, -38.5).
#    Then ox=+8, oy=+27 shifts:
#      h_start -> (-41.5, +60), corner -> (+52, +60), v_end -> (+52, -12).
#    v_end y=-12 is too high; hook would be inside enclosure. Try scale=0.65,
#    ox=+2, oy=+22:
#      canonical h_start = (-58.5, +39), corner = (+52, +39), v_end = (+52, -45.5).
#      shifted: h_start = (-56.5, +61), corner = (+54, +61), v_end = (+54, -23.5).
#    Better; the right-shaft length in canonical is 130*0.65 = 84.5 px.
#    Enclosure height should be ~85 px — matches GT reasonably.

def draw_envelope():
    draw_heng_zhe_gou(DRAW, ox=+2, oy=+22, scale=0.65)


# ---------------------------------------------------------------------------
# 3) Long central 竖 — starts at the top-left corner of the enclosure and
#    descends all the way to near the bottom of the canvas.
#    Top point should be near (-56.5, +61) (where the h_start lives, so it
#    joins the horizontal on the left).
#    Actually 巾's central shaft descends from a bit RIGHT of the left corner
#    — inspecting GT: the long tail is roughly under the middle/right of
#    the top horizontal. Let's put it at x ≈ -40 to align with the top nub
#    (creating a visual continuity: top nub → gap → long shaft).
#    Length: from y=+62 (touching horizontal from below) down to y=-115
#    (well below the enclosure floor at y=-23).
#    Inline (per TR5): thickness ~11 px, straight vertical.

def draw_long_shaft():
    # Central 竖 of 巾: starts at MIDDLE of the top horizontal, descends
    # WELL BELOW the enclosure. Slightly left-of-center per GT.
    # Envelope horizontal spans roughly x=-56 .. x=+54, midpoint ≈ -1.
    # GT places the tail slightly left of center; use x = -2.
    x_top, y_top = _to_pixel(-2, 62)
    x_bot, y_bot = _to_pixel(-2, -120)
    DRAW.line([(x_top, y_top), (x_bot, y_bot)], fill=(0, 0, 0), width=11)


# ---- Render order: envelope first, then top nub, then long shaft on top
draw_envelope()
draw_top_nub()
draw_long_shaft()

out_path = os.path.join(_HERE, "01_巾.png")
IMG.save(out_path)
print(f"wrote {out_path}")
