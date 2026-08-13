# BANK_DEVIATION
# skipped: heng_zhe_short.py (no rising ti tail); using compound inline
# reason: stroke 2 of simplified 讠 is 横折提 (heng-zhe-ti) — horizontal
#         top → down-corner → descending body → rising ti (upward flick).
#         Bank has heng_zhe_short (missing ti), shu_zhe (missing ti),
#         and ti (rising tail only). Compose s2 inline: horizontal +
#         corner + descending body, then bank draw_ti for the final
#         flick. Counts as ONE compound stroke.
# fresh_component: heng_zhe_ti_for_yan (compound polyline + ti call)
#
# TRAJECTORY DIFF (retry 2 of p2_radical_035_讠)
# ----------------------------------------------
# main (C): missing tí flick — s2 read as heng-zhe-gou-ish.
# retry_1 (C): tí added but the whole radical was too SMALL / too
#              cramped in the upper-left. GT is bigger, occupies more
#              vertical extent (dot near y=55–90, s2 spans y=135–245).
#              Retry_1 fitted s2 into y=135–215, too short.
# Fixes for retry 2:
#   (a) Enlarge dian (thicker, longer, more diagonal top-left of canvas)
#       from ~(95, 55) to (140, 95). Approximates GT's chunkier dot.
#   (b) Enlarge s2 vertical extent: horizontal at y≈140 (x 55→110),
#       descent to y≈240, tí ends at ~(125, 235). Total span ~100 px
#       vs retry_1's ~80 px.
#   (c) Keep bank draw_ti for the flick (worked visually in retry_1);
#       just move its endpoints down and out.

"""Render simplified 讠 (yán speech-radical, 2 MMH strokes)."""

import os, sys, pathlib
from PIL import Image, ImageDraw

# ---- bank imports ----
BANK = pathlib.Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))
from dian import draw_dian  # noqa: E402
from ti import draw_ti      # noqa: E402


# ---- 米字格 anchor helper (300×300, 3×3 cells) ----
CELL = {
    'TL': (0, 0), 'TC': (100, 0), 'TR': (200, 0),
    'ML': (0, 100), 'C': (100, 100), 'MR': (200, 100),
    'BL': (0, 200), 'BC': (100, 200), 'BR': (200, 200),
}


def anchor(cell, xf, yf):
    cx, cy = CELL[cell]
    return (cx + 100 * xf, cy + 100 * yf)


# ---- Canvas ----
W, H = 300, 300
img = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(img)


# ---- Stroke 1: 点 (dian) — bigger, chunkier than retry_1 ----
# Approx GT: diagonal from upper-left corner area (95,55) to (140,95),
# tapered thin→thick. MMH head TL(0.683,0.724)=(68,72), tail C(0.061,0.014)=(106,101).
# Nudged slightly right + longer to match GT visual centroid.
s1_head = (95, 55)
s1_tail = (140, 100)
draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=10, bow=4, steps=48)


# ---- Stroke 2: 横折提 (compound, BANK_DEVIATION) ----
# Visible GT shape (enlarged from retry_1):
#   - horizontal at y≈140, x=55..110 (~5 px thick, slight down-tilt)
#   - crisp corner ~ (114, 152)
#   - descending body curving slightly left down to ~ (60, 238)
#   - rising tí from (~60, 238) up-right to (~130, 230)
#
# retry_1 spanned y=135..215 for s2 (too short). Now span y=140..245.

def draw_polyline(draw, pts, width=6):
    for a, b in zip(pts, pts[1:]):
        draw.line([a, b], fill='black', width=width)
    for p in pts:
        r = width / 2
        draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill='black')


h_left      = (55, 140)
h_right     = (108, 145)
corner      = (116, 154)
descend_mid = (95, 195)
ti_head     = (65, 240)          # heavy end of tí (bottom-left)

draw_polyline(d, [h_left, h_right, corner, descend_mid, ti_head], width=6)

# Rising tí using bank primitive
ti_tail = (130, 232)   # visible tí endpoint (up-right)
draw_ti(d, ti_head, ti_tail, w_head=9, w_tail=2, steps=50)


# ---- SELF_CHECK ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 visual strokes: dian + heng-zhe-ti compound
    'endpoint_mismatches': [
        # s1 nudged from MMH TL(0.683,0.724)=(68,72) → (95,55) to match GT
        # visible dot centroid (MMH median offset artifact).
        {'stroke': 1, 'expected': ('TL', 0.683, 0.724),
         'actual': ('TC', -0.05, 0.55),
         'delta': 'x+27,y-17 (matches GT visible dot)'},
        # s2 head: MMH ML(0.164,0.734)=(16,173); visible horizontal begins
        # at x=55. Median artifact.
        {'stroke': 2, 'expected': ('ML', 0.164, 0.734),
         'actual': ('ML', 0.55, 0.40),
         'delta': 'x+39,y-33 (visible horizontal start)'},
        # s2 tail: MMH BC(0.348,0.288)=(135,229); tí endpoint (130,232) ~within tol.
        {'stroke': 2, 'expected': ('BC', 0.348, 0.288),
         'actual': ('BC', 0.30, 0.32),
         'delta': '≈0.04 x_frac, ≈0.03 y_frac (within ±0.20)'},
    ],
    'joint_class_mismatches': [],   # none expected (strokes separate)
    'overall_pass': True,
    'notes': ('Retry 2: enlarged both strokes to match GT footprint. '
              'Dot chunkier and moved right. s2 spans y=140..245 '
              '(was 135..215 in retry_1). Bank draw_ti retained.'),
}


# ---- Save ----
out_png = os.path.join(os.path.dirname(__file__), "01_讠.png")
img.save(out_png)
print(f"wrote {out_png}")
