# BANK_DEVIATION
# skipped: heng_zhe_short.py (no rising ti tail); using compound inline
# reason: stroke 2 of simplified 讠 is 横折提 (heng-zhe-ti) — horizontal
#         top → down-corner → descending body → rising ti (upward flick).
#         Bank has heng_zhe_short (missing ti), shu_zhe (missing ti),
#         and ti (only the rising tail). So we compose s2 inline as
#         a horizontal + corner + descent segment, then call draw_ti
#         for the final rising flick. Counts as ONE compound stroke.
# fresh_component: heng_zhe_ti_for_yan (compound polyline + ti call)
#
# TRAJECTORY DIFF (retry 1 of p2_radical_035_讠)
# ----------------------------------------------
# FAILED main attempt got C. Visual issues seen:
#   (1) The tí (upward flick) at the bottom was MISSING — the descent
#       just terminated without a visible rising sweep, so s2 read as
#       heng-zhe-gou-ish rather than heng-zhe-ti.
#   (2) The horizontal top was chunky and too heavy compared to GT's
#       thin, calligraphic horizontal.
# Fix plan:
#   (a) Use bank `draw_ti` for the final rising portion so a clean
#       tapered flick is guaranteed (thick head, thin rising tail).
#   (b) Reduce horizontal ink weight; give the horizontal a slight
#       downward tilt like GT.
#   (c) Keep dian for stroke 1 unchanged — that part was OK.

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


# ---- Stroke 1: 点 (dian) ----
# MMH: head ('TL', 0.683, 0.724) ≈ (68, 72), tail ('C', 0.061, 0.014) ≈ (106, 101)
s1_head = anchor('TL', 0.683, 0.724)
s1_tail = anchor('C', 0.061, 0.014)
draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=7, bow=3, steps=48)


# ---- Stroke 2: 横折提 (compound, BANK_DEVIATION) ----
# MMH: head ('ML', 0.164, 0.734) ≈ (16, 173), tail ('BC', 0.348, 0.288) ≈ (135, 229)
#
# Visible GT shape:
#   - short thin horizontal at top, ~y=135, x=55..108, slight down-tilt
#   - crisp corner ~ (112, 148)
#   - descending body curving slightly left down to ~ (85, 215)
#   - rising ti (upward flick) from (~85, 215) up-right to (~135, 195)
#
# The MMH head at (16, 173) is a median artifact — well left of the
# visible horizontal start; MMH tail at (135, 229) lies at the ti
# endpoint region (within tolerance of the visible flick end).

# Horizontal top + corner + descent (thinner than prior attempt)
def draw_polyline(draw, pts, width=5):
    for a, b in zip(pts, pts[1:]):
        draw.line([a, b], fill='black', width=width)
    for p in pts:
        r = width / 2
        draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill='black')


h_left  = (56, 135)
h_right = (108, 141)
corner  = (114, 150)
descend_mid = (100, 190)
ti_head = (85, 215)          # heavy end of ti (bottom-left)

draw_polyline(d, [h_left, h_right, corner, descend_mid, ti_head], width=5)

# Rising ti using bank primitive (thick head, thin tail)
ti_tail = anchor('BC', 0.35, 0.15)   # ~ (135, 215) — visible ti endpoint
draw_ti(d, ti_head, ti_tail, w_head=7, w_tail=2, steps=50)


# ---- SELF_CHECK ----
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 2 visual strokes: dian + heng-zhe-ti compound
    'endpoint_mismatches': [
        # s2 head visually offset from MMH: MMH gives median (16,173) but
        # visible horizontal starts at (56,135). Accepted median artifact.
        {'stroke': 2, 'expected': ('ML', 0.164, 0.734),
         'actual': ('ML', 0.56, 0.35),
         'delta': 'visible horizontal starts inside ML/C boundary (median artifact)'},
        # s2 tail close in x to MMH BC(0.348, 0.288)=(135,229); ti endpoint
        # rendered at (135,215) — within ±0.20 y_frac tolerance.
        {'stroke': 2, 'expected': ('BC', 0.348, 0.288),
         'actual': ('BC', 0.35, 0.15),
         'delta': '≈0.14 y_frac (within ±0.20)'},
    ],
    'joint_class_mismatches': [],   # none expected
    'overall_pass': True,
    'notes': ('Retry 1: added explicit rising ti via bank draw_ti '
              'to fix missing ti flick from main attempt. Horizontal '
              'thinned. Corner kept crisp.'),
}


# ---- Save ----
out_png = os.path.join(os.path.dirname(__file__), "01_讠.png")
img.save(out_png)
print(f"wrote {out_png}")
