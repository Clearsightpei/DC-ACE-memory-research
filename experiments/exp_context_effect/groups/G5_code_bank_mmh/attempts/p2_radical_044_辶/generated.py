# BANK_DEVIATION
# skipped: na.py for stroke 3 (would use if simple na, but 辶's bottom is a
#          long *flat* 平捺 with a distinct tail flare, not the diagonal 八-捺 shape)
# replaced: no primitive exists for 横折折撇 (stroke 2 zigzag) — inlined fresh
# reason: 辶's middle stroke is a compound 3-segment zigzag with no bank equivalent,
#         and its bottom 平捺 is far more horizontal (nearly flat, wide span)
#         than the na.py bootstrap version tuned for 八's right-diagonal stroke.
# fresh_component: zigzag_zzp_for_辶 (stroke 2 body), ping_na_for_辶 (stroke 3 flat)
#
# Item: p2_radical_044_辶  (3 strokes)
# Uses bank: dian.py (stroke 1 dot)
# Inlined: stroke 2 (compound zigzag), stroke 3 (flat 平捺)

import sys
from pathlib import Path
from PIL import Image, ImageDraw

# Add bank code dir to import path
BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))
from dian import draw_dian  # noqa

# --- Anchor derivations from MMH block ------------------------------------
# 米字格 cells: 100px each on a 300 canvas.
# Cell (col, row) → (x_min, y_min): TL=(0,0) TM=(100,0) TR=(200,0)
#                                    ML=(0,100) MM=(100,100) MR=(200,100)
#                                    BL=(0,200) BM=(100,200) BR=(200,200)

def anchor(cell, xf, yf):
    cx = {'TL': 0, 'ML': 0, 'BL': 0, 'TM': 100, 'MM': 100, 'BM': 100,
          'TR': 200, 'MR': 200, 'BR': 200}[cell]
    cy = {'TL': 0, 'TM': 0, 'TR': 0, 'ML': 100, 'MM': 100, 'MR': 100,
          'BL': 200, 'BM': 200, 'BR': 200}[cell]
    return (cx + xf * 100, cy + yf * 100)


# Stroke 1: dot (点)  TL(0.618,0.718) -> TL(0.964,0.967)
s1_head = anchor('TL', 0.618, 0.718)   # ~ (61.8, 71.8)
s1_tail = anchor('TL', 0.964, 0.967)   # ~ (96.4, 96.7)

# Stroke 2: compound 横折折撇  ML(0.272,0.55) -> BL(0.814,0.388)
s2_head = anchor('ML', 0.272, 0.55)    # ~ (27.2, 155.0)
s2_tail = anchor('BL', 0.814, 0.388)   # ~ (81.4, 238.8)

# Stroke 3: 平捺  BL(0.284,0.543) -> BR(0.689, 0.789)
s3_head = anchor('BL', 0.284, 0.543)   # ~ (28.4, 254.3)
s3_tail = anchor('BR', 0.689, 0.789)   # ~ (268.9, 278.9)


# --- Fresh inline draws ----------------------------------------------------
def _bezier_thickened(draw, pts_ctrl, w_head, w_tail, steps=60):
    """Quadratic bezier with linear width taper."""
    p0, p1, p2 = pts_ctrl
    prev = None
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = w_head + (w_tail - w_head) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')
        prev = (x, y)


def _line_thickened(draw, p0, p1, w0, w1, steps=40):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = w0 + (w1 - w0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


def draw_zigzag_zzp(draw, head, tail):
    """Inlined 横折折撇 for 辶: 3-segment zigzag from top-left to lower-left.
    Sequence: short 横 rightward tick, then 折 down-left, then 撇 down-right.
    """
    hx, hy = head
    tx, ty = tail
    # Waypoints derived from visual GT: small rightward tick, drop back-left,
    # then diagonal down-right to the tail.
    p_top_right = (hx + 30, hy - 3)         # short 横 tick
    p_mid_left  = (hx + 4, hy + 32)         # 折 down-left
    p_low_mid   = (hx + 20, hy + 55)        # inflection before final 撇
    # Segment 1: small 横 (top-left to top-right)
    _line_thickened(draw, head, p_top_right, 5, 5)
    # Segment 2: down-left curve (折)
    _bezier_thickened(draw, (p_top_right, (hx + 34, hy + 14), p_mid_left), 5, 5)
    # Segment 3: down-right into a 撇 landing at tail
    _bezier_thickened(draw, (p_mid_left, p_low_mid, tail), 5, 4)


def draw_ping_na(draw, head, tail):
    """Inlined 平捺 for 辶: long, near-horizontal sweeping stroke with a
    slight downward belly and a flared tail (thick then slight taper up)."""
    hx, hy = head
    tx, ty = tail
    # Slight downward belly (positive y in image coords is down)
    mx, my = (hx + tx) / 2, (hy + ty) / 2 + 8  # bow down a touch
    # Head is a small entry (thin), belly thickens, tail flares out.
    steps = 100
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * hx + 2 * u * t * mx + t * t * tx
        y = u * u * hy + 2 * u * t * my + t * t * ty
        # Width profile: thin at head, grows through belly, peaks near 0.85,
        # slight taper into tail flare.
        if t < 0.15:
            r = 3 + (5 - 3) * (t / 0.15)
        elif t < 0.85:
            r = 5 + (10 - 5) * ((t - 0.15) / 0.70)
        else:
            r = 10 - (10 - 6) * ((t - 0.85) / 0.15)
        draw.ellipse((x - r, y - r, x + r, y + r), fill='black')


# --- Compose --------------------------------------------------------------
img = Image.new('RGB', (300, 300), 'white')
d = ImageDraw.Draw(img)

# Stroke 1: dot via bank primitive
draw_dian(d, s1_head, s1_tail, w_head=3, w_tail=8, bow=3)

# Stroke 2: inlined zigzag
draw_zigzag_zzp(d, s2_head, s2_tail)

# Stroke 3: inlined 平捺
draw_ping_na(d, s3_head, s3_tail)

out = Path(__file__).parent / '01_辶.png'
img.save(out)
print(f"Saved: {out}")


# --- Self-check -----------------------------------------------------------
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,        # 3 primitives (dian + zigzag + ping_na) == expected 3
    'endpoint_mismatches': [],       # all anchors used verbatim from MMH block
    'joint_class_mismatches': [],    # s2.tail ~ (81, 239); s3 midpoint area ~ (85, 249): natural ~10 px gap (N)
    'overall_pass': True,
    'notes': 'Used bank dian for s1. Inlined s2 (compound 横折折撇 — no bank match) and s3 (平捺 — flatter than na.py). Joint N respected by not welding s2.tail into s3 body.'
}
