"""Cycle 5 — three 撇+捺 compositions: 八, 人, 入.

Introduces two new atomic primitives: 撇 (pie) and 捺 (na).
Both are written as reusable functions taking explicit head/tail coords
so that each character can position them according to its structural rule:

    八 — heads SEPARATED (visible horizontal gap at top)
    人 — heads SHARE the apex (no gap)
    入 — 捺 dominates (full top-left to bottom-right sweep);
         撇 is a SHORTER secondary stroke whose head sits BELOW the 捺's apex

All width profiles obey §1.0: floor of max(3, w(s)) per sample.
"""

import os
import sys

from PIL import Image, ImageDraw

SB = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "success_bank", "code"
)
sys.path.insert(0, SB)

from heng import brushed_bezier, to_px, bezier_point, CANVAS_W, CANVAS_H  # noqa: E402,F401


# ---------------------------------------------------------------------------
# Primitive: 撇 (pie) — tapered diagonal sweep, upper-right -> lower-left.
# Width profile: heavy entry head (18) -> shaft (14 -> 11 -> 8) -> taper to 3.
# Centerline: cubic Bezier with controls placing the curve slightly ABOVE the
# straight head-to-tail line so it reads as a gentle concave-down arc
# (the body bows up-right, the tail sweeps down-left).
# ---------------------------------------------------------------------------
def _w_profile_pie(s):
    # Heavy press at head (s near 0), tapering progressively to a fine tail.
    if s <= 0.08:
        return 18.0
    elif s <= 0.20:
        t = (s - 0.08) / 0.12
        return 18.0 + (14.0 - 18.0) * t
    elif s <= 0.50:
        t = (s - 0.20) / 0.30
        return 14.0 + (11.0 - 14.0) * t
    elif s <= 0.75:
        t = (s - 0.50) / 0.25
        return 11.0 + (8.0 - 11.0) * t
    else:
        t = (s - 0.75) / 0.25
        return 8.0 + (3.0 - 8.0) * t


def draw_pie(pil_draw, head_x, head_y, tail_x, tail_y, scale=1.0):
    """Draw a 撇 from (head_x, head_y) -> (tail_x, tail_y) in math-coords.

    Controls placed ABOVE the straight chord (i.e. shifted toward +x / -y mix)
    to bow the arc concave-down (the body curves rightward of the chord, so
    the tail kicks out to the lower-left).
    """
    dx = tail_x - head_x
    dy = tail_y - head_y
    # Perpendicular direction (rotate the chord 90deg CCW in math coords):
    # for a head-upper-right -> tail-lower-left chord, +perp points
    # up-and-right, which produces the desired concave-down arc.
    # Bow magnitude scales with chord length.
    chord_len = (dx * dx + dy * dy) ** 0.5
    bow = 0.05 * chord_len  # gentle arc (reduced from 0.10 — was too curly)
    # Perpendicular unit vector (math coords, y-up):
    px_u = -dy / chord_len
    py_u = dx / chord_len
    # For a 撇 head-upper-right -> tail-lower-left: dx<0, dy<0,
    # so perp = (-dy, dx) = (+, -). We want bow UP-RIGHT -> flip sign so
    # the perpendicular points UP-RIGHT (positive x, positive y in math).
    # Test: dx=-100, dy=-100 -> perp = (100, -100). That is DOWN-RIGHT, wrong.
    # Negate so perp = (-100, 100) = UP-LEFT. Hmm, also not what we want.
    # Actually for a concave-DOWN arc on a NW-pointing chord, we want the
    # bow OFFSET toward UP-RIGHT (i.e. above the chord). UP-RIGHT = (+, +).
    # That is perp = (-dy, dx) negated -> (dy, -dx) = (-100, 100). Wrong sign.
    # Try (-dy, dx) directly with dx=-100, dy=-100 -> (100, -100). DOWN-RIGHT.
    # We want UP-RIGHT (+, +), so use (dy, -dx) = (-100, 100). That is UP-LEFT.
    # Neither perpendicular is up-right. The chord goes NW; both perpendiculars
    # are NE and SW. NE perpendicular = (+, +) means perp_x>0 AND perp_y>0.
    # dx=-100, dy=-100. (-dy, dx) = (100, -100) is SE. (dy, -dx) = (-100, 100)
    # is NW. So actually for chord NW, perpendiculars are NE and SW... wait no,
    # rotate (-100,-100) by 90 CCW (math): (x,y)->(-y,x) gives (100,-100) -> SE.
    # Rotate 90 CW: (x,y)->(y,-x) gives (-100,100) -> NW. Hmm.
    # The chord (-100,-100) points SW (y-down in image but math y-up here so
    # NW=upper-left when negative dx & y... actually math y-up: dy<0 means
    # going DOWN. dx<0 means LEFT. So chord points to lower-left (SW). Its
    # perpendiculars are UPPER-LEFT (NW) and LOWER-RIGHT (SE). We want the
    # bow on the UPPER-RIGHT side -- but UPPER-RIGHT isn't perpendicular to
    # a SW chord, it's roughly opposite. Re-read brief: "controls placing
    # the curve *above* the straight head-to-tail line (concave-down arc)".
    # 'Above' the chord (in image sense, smaller image-y == math larger y) =
    # the UPPER side. For a chord going lower-left, the upper side is NE
    # (upper-right of the chord) -- which is perpendicular SE... no.
    # Let me re-derive: chord from (0,0) head to (-100,-100) tail (math coords).
    # 'Above the line' geometrically = points where y - line_y > 0, i.e.
    # points with larger math-y for a given x. The chord at midpoint (-50,-50).
    # A perpendicular bow pushing the midpoint to (-50+a, -50+b). 'Above' means
    # b > 0 (larger math-y). Perpendicular to chord direction (-1,-1)/sqrt2 is
    # either (1,-1)/sqrt2 or (-1,1)/sqrt2. The second one has +y component, so
    # that's the 'above' direction: (-1, 1)/sqrt2. That equals (dy, -dx)/|chord|.
    # So use (dy, -dx).
    px_u = dy / chord_len
    py_u = -dx / chord_len
    # Control points at ~1/3 and 2/3 along the chord, offset by bow:
    P0 = (head_x, head_y)
    P1 = (head_x + dx * 0.33 + px_u * bow, head_y + dy * 0.33 + py_u * bow)
    P2 = (head_x + dx * 0.66 + px_u * bow * 0.7, head_y + dy * 0.66 + py_u * bow * 0.7)
    P3 = (tail_x, tail_y)
    brushed_bezier(pil_draw, P0, P1, P2, P3, _w_profile_pie, samples=260)


# ---------------------------------------------------------------------------
# Primitive: 捺 (na) — right-diagonal sweep with a flat closing kick.
# Segment A: main sweep, thin head (5) growing to heavy tail (18).
# Segment B: flat kick (出锋) — width 18 -> hold 16 (25%) -> release to 3.
# ---------------------------------------------------------------------------
def _w_profile_na_main(s):
    # 5 -> 8 -> 14 -> 18, growing toward the tail.
    if s <= 0.25:
        t = s / 0.25
        return 5.0 + (8.0 - 5.0) * t
    elif s <= 0.70:
        t = (s - 0.25) / 0.45
        return 8.0 + (14.0 - 8.0) * t
    else:
        t = (s - 0.70) / 0.30
        return 14.0 + (18.0 - 14.0) * t


def _w_profile_na_kick(s):
    # 18 (hold to 25%) -> 16 hold to 50% -> release to 3 by end.
    if s <= 0.25:
        return 18.0
    elif s <= 0.50:
        t = (s - 0.25) / 0.25
        return 18.0 + (16.0 - 18.0) * t
    else:
        t = (s - 0.50) / 0.50
        return 16.0 + (3.0 - 16.0) * t


def draw_na(pil_draw, head_x, head_y, tail_x, tail_y, scale=1.0, kick_len_frac=0.22):
    """Draw a 捺 from (head_x, head_y) -> (tail_x, tail_y) in math-coords.

    Main sweep is bowed concave-up (bow toward the upper side of the chord).
    A short flat kick extends from the tail roughly horizontally to the right.
    """
    dx = tail_x - head_x
    dy = tail_y - head_y
    chord_len = (dx * dx + dy * dy) ** 0.5
    # Bow direction: for a chord going lower-right (dx>0, dy<0), the 'below'
    # side of the chord (where image-y is larger / math-y is smaller) gives a
    # gentle belly to the stroke (concave seen from the upper-right). That is
    # perpendicular = (-dy, dx)/|chord| with dx>0, dy<0 -> (+,+). math-y>0 =
    # upper. We actually want the curve to dip slightly BELOW the chord (so
    # the stroke flexes outward to the lower-left), giving the classic 捺
    # 'belly'. perp_below = (dy, -dx)/|chord| = (-,-) -> lower-left side.
    bow = 0.08 * chord_len
    px_u = dy / chord_len  # -ve for normal 捺 chord
    py_u = -dx / chord_len  # -ve for normal 捺 chord
    P0 = (head_x, head_y)
    P1 = (head_x + dx * 0.30 + px_u * bow * 0.5, head_y + dy * 0.30 + py_u * bow * 0.5)
    P2 = (head_x + dx * 0.65 + px_u * bow, head_y + dy * 0.65 + py_u * bow)
    P3 = (tail_x, tail_y)
    brushed_bezier(pil_draw, P0, P1, P2, P3, _w_profile_na_main, samples=260)

    # Kick: short flat segment extending from the tail to the right
    # (slightly downward then leveling off). Roughly horizontal.
    kick_dx = chord_len * kick_len_frac
    kick_dy = -chord_len * 0.02  # very slight downward (math y-down)
    K0 = (tail_x, tail_y)
    K1 = (tail_x + kick_dx * 0.35, tail_y + kick_dy * 0.5)
    K2 = (tail_x + kick_dx * 0.70, tail_y + kick_dy * 0.9)
    K3 = (tail_x + kick_dx, tail_y + kick_dy)
    brushed_bezier(pil_draw, K0, K1, K2, K3, _w_profile_na_kick, samples=140)


# ---------------------------------------------------------------------------
# Canvas helpers
# ---------------------------------------------------------------------------
def new_canvas():
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), "white")
    return img, ImageDraw.Draw(img)


# ---------------------------------------------------------------------------
# Task 1: 八 — SEPARATED heads, gap at top.
# 撇 (left): head around upper-mid, tail at lower-left.
# 捺 (right): head higher up, separate position, tail at lower-right.
# GT shows 撇 noticeably shorter & lower than 捺 — 捺 head is higher.
# ---------------------------------------------------------------------------
def render_ba():
    img, d = new_canvas()
    # math coords, origin = canvas center, y-up.
    # GT: 撇 is shorter & lower-left; 捺 is taller, head clearly higher and
    # to the right with a visible horizontal gap between the two heads.
    # 撇: head at (-30, +50), tail at (-160, -130) — diagonal sweep, body
    # curves so the bow is to the upper-right of the chord.
    draw_pie(d, head_x=-30, head_y=50, tail_x=-160, tail_y=-130)
    # 捺: head at (+60, +130) (HIGHER than 撇 head by ~80px in math y),
    # tail at (+220, -90). Clear ~90px horizontal gap between heads.
    draw_na(d, head_x=60, head_y=130, tail_x=220, tail_y=-90)
    img.save(os.path.join(os.path.dirname(__file__), "01_八.png"))


# ---------------------------------------------------------------------------
# Task 2: 人 — SHARED apex.
# Both strokes start from the SAME point at top.
# 撇 is slightly steeper/longer-down-left; 捺 sweeps further right.
# ---------------------------------------------------------------------------
def render_ren():
    img, d = new_canvas()
    apex_x, apex_y = 0, 130  # shared apex near upper-mid canvas
    # 撇: from apex down to lower-left.
    draw_pie(d, head_x=apex_x, head_y=apex_y, tail_x=-160, tail_y=-150)
    # 捺: from apex down to lower-right (sweeps further right).
    draw_na(d, head_x=apex_x, head_y=apex_y, tail_x=180, tail_y=-130)
    img.save(os.path.join(os.path.dirname(__file__), "02_人.png"))


# ---------------------------------------------------------------------------
# Task 3: 入 — 捺 DOMINATES; 撇 is a shorter secondary stroke.
# 捺 spans from top-left to bottom-right (full stroke).
# 撇 head sits BELOW the 捺's apex, attaching to the upper portion of 捺,
# tail kicks down-left.
# ---------------------------------------------------------------------------
def render_ru():
    img, d = new_canvas()
    # 捺: dominant. Head top-left at (-50, +150), tail lower-right (+200, -120).
    # This stroke is the visual backbone of 入.
    draw_na(d, head_x=-50, head_y=150, tail_x=200, tail_y=-120)
    # 撇: SHORT secondary stroke. The 捺's upper section runs roughly from
    # (-50, +150) to (+30, +80) over its first ~30% — its centerline passes
    # near x≈0 at y≈+110. Plant the 撇 head ON the 捺's upper section near
    # (+10, +100). Tail sweeps down-left a SHORT distance to (-110, -10) so
    # it stays in the upper-LEFT quadrant and reads as a secondary mark
    # (NOT crossing the 捺's body, NOT longer than ~60% of 捺's chord).
    draw_pie(d, head_x=10, head_y=100, tail_x=-110, tail_y=-10)
    img.save(os.path.join(os.path.dirname(__file__), "03_入.png"))


if __name__ == "__main__":
    render_ba()
    render_ren()
    render_ru()
    print("rendered 01_八.png, 02_人.png, 03_入.png")
