"""
p2_radical_028_人 — retry_5 RERUN under v9 prompt fix.

============================================================================
VISUAL DIFF (mandatory Step 0)
============================================================================
Compared prior retry_5 PNG vs GT PNG side by side. Concrete gaps:

1. APEX GAP. Prior attempt has a visible ~10 px WHITE GAP between the top
   of the 撇 (left) and the top of the 捺 (right) — the two strokes do
   not meet. GT: the two strokes share the apex pixel and flow into each
   other; the top reads as a single joined point, not two separate line
   tops.

2. UNIFORM STICK-LIKE WEIGHT vs CALLIGRAPHIC TAPER. Prior strokes are
   thin, uniform, straight-ish black lines end to end. GT strokes have
   clear calligraphic ink modulation:
     - 撇 is thick near the apex (~10 px) and tapers to a fine point at
       its lower-left tail.
     - 捺 starts thin near the apex, thickens as it descends, and
       terminates in a distinctly HEAVIER FLAT FOOT (typical 捺 tail /
       近似 燕尾) at the lower-right.

3. STROKE SHAPE. Prior 撇 is essentially a straight diagonal. GT 撇 bows
   OUTWARD (belly leans to the left of the chord) — a clear curve, not
   a stick. Prior 捺 is also straight; GT 捺 is a subtly right-leaning
   curve that flares at the bottom.

4. PROPORTION. Prior renders both legs at nearly identical length and
   both descend to about the same y. In GT, the 撇 tail sweeps lower
   and further LEFT; the 捺 tail is a bit HIGHER but reaches further
   RIGHT, giving the character a slightly wider stance at bottom than
   at top, with an asymmetric footprint.

Fix plan: draw both strokes as tapered polylines (stamped variable-radius
circles along a bezier), share an exact APEX pixel between them, bow the
撇 leftward, keep the 捺 mostly-straight with a heavier flat tail.

============================================================================
RETRY MEMORY CHECKLIST (per memory_index.md)
============================================================================
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   errata says X-crossing family + terminal-freeze-lifted under v8. The
#   proposed lever historically was kiss_apex(u_pie=0.0) so two strokes
#   share their heads at a common apex. B5 diagnosis: kiss_apex made the
#   strokes touch but the result didn't read as a proper calligraphic 人.
#   The B5 lesson (丷 graduation) is: trust the GT over the helper
#   abstraction. So: implement apex-sharing DIRECTLY (compute one pixel,
#   both strokes start from it) rather than call the helper, and pay
#   equal attention to the calligraphic TAPER + CURVE the helper doesn't
#   express.
# Q2 (form_catalog): 撇 in X-crossing / apex-kiss context needs bow to
#   the left of chord and taper 10→2. 捺 in apex-kiss context needs
#   flat-foot terminus (thicken toward end). Use these numbers.
# Q3 (helpers): Fail category is apex-kiss + calligraphic taper. The
#   available helpers (kiss_apex, variant_pie, variant_na) target only
#   the geometry of the apex-touch, not the ink modulation the GT
#   actually shows. Under v8 signature freedom, I inline the whole
#   character with an explicit apex pixel + explicit taper width
#   profile per stroke. This is exactly what B5's 丷 did to graduate.

============================================================================
Function signature freedom (v8): (t, ox, oy, scale) unused — this
character is atomic enough to draw with a single specialized inline
function using PIL directly.
"""

from PIL import Image, ImageDraw

W, H = 300, 300


def _stamp_taper(draw, pts, w_head, w_tail):
    """Stamp filled circles along a polyline path with linearly-varying
    radius. pts is a list of (x, y) in pixel coords."""
    if len(pts) < 2:
        return
    # cumulative length so width varies with arc-length
    seglens = []
    total = 0.0
    for i in range(len(pts) - 1):
        dx = pts[i + 1][0] - pts[i][0]
        dy = pts[i + 1][1] - pts[i][1]
        d = (dx * dx + dy * dy) ** 0.5
        seglens.append(d)
        total += d
    if total <= 0:
        return
    cum = 0.0
    step = 0.6  # sub-pixel oversample
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        d = seglens[i]
        if d <= 0:
            continue
        n = max(int(d / step), 1)
        for k in range(n + 1):
            t = k / n
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            u = (cum + d * t) / total
            w = w_head * (1 - u) + w_tail * u
            r = max(w / 2.0, 0.5)
            draw.ellipse((x - r, y - r, x + r, y + r), fill=0)
        cum += d


def _bezier(p0, p1, p2, n=60):
    """Sample a quadratic bezier."""
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


def draw_ren(img):
    """Draw the radical 人 in the 300x300 canvas.

    Explicit apex pixel shared by both strokes. Pixel coords (y grows DOWN,
    PIL convention).
    """
    draw = ImageDraw.Draw(img)

    # Shared apex — near top-center, slightly above vertical middle.
    APEX = (150, 78)

    # ---- 撇 (left stroke) ----
    # Starts thick at apex, curves OUTWARD (belly to the left of chord),
    # tapers to a fine point at lower-left. Longer / lower than the 捺.
    pie_start = APEX
    pie_end = (58, 248)          # far bottom-left, low
    # control point pulled to the left of chord to create the outward bow
    chord_mid = ((pie_start[0] + pie_end[0]) / 2,
                 (pie_start[1] + pie_end[1]) / 2)
    pie_ctrl = (chord_mid[0] - 26, chord_mid[1] - 4)
    pie_path = _bezier(pie_start, pie_ctrl, pie_end, n=90)
    _stamp_taper(draw, pie_path, w_head=11, w_tail=2)

    # ---- 捺 (right stroke) ----
    # Starts THIN at apex (below/adjacent to 撇 top so they share ink),
    # thickens as it descends, ends at a HEAVIER FLAT FOOT at lower-right.
    # Slightly SHORTER (higher y) than 撇 tail, further to the right.
    na_start = APEX
    na_body_end = (232, 236)     # heavy body end
    # subtle inward-then-outward curve — control point slightly right of
    # chord for a gentle rightward bow.
    chord_mid2 = ((na_start[0] + na_body_end[0]) / 2,
                  (na_start[1] + na_body_end[1]) / 2)
    na_ctrl = (chord_mid2[0] + 6, chord_mid2[1] + 10)
    na_body = _bezier(na_start, na_ctrl, na_body_end, n=90)
    # thin at head → thick at foot base
    _stamp_taper(draw, na_body, w_head=3, w_tail=13)

    # ---- 捺 flat foot / 燕尾 ----
    # Short heavy nearly-horizontal segment continuing out from the body
    # end, tapering to a chisel tip.
    foot_start = na_body_end
    foot_end = (262, 232)
    foot_path = [foot_start, foot_end]
    _stamp_taper(draw, foot_path, w_head=13, w_tail=3)

    # ---- Reinforce the apex kiss ----
    # A small dark cap right at APEX so the two stroke starts read as
    # one shared ink point rather than two adjacent line tops.
    ax, ay = APEX
    draw.ellipse((ax - 5.5, ay - 5.5, ax + 5.5, ay + 5.5), fill=0)


def main():
    img = Image.new("L", (W, H), color=255)
    draw_ren(img)
    out = (
        "<REPO_ROOT>/experiments/"
        "exp_context_effect/groups/G3_coords/attempts/"
        "p2_radical_028_人__retry_5__rerun/01_人.png"
    )
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
