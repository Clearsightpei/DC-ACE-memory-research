"""p2_radical_011_匕 (bǐ) — retry_4 RERUN under v9 prompt fix. G3 coord-bank render.

# VISUAL DIFF (mandatory step 0 — from reading prior_PNG and GT_PNG)
# Prior attempt: groups/G3_coords/attempts/p2_radical_011_匕__retry_4/01_匕.png
# GT:           gt/phase2/匕.png
#
# Gap 1 — 撇 DISCONNECTED from the body:
#   In prior PNG the 撇 (short "/" diagonal) floats far to the LEFT of the
#   竖弯钩 body, with a visible white gap of ~25 px between them. In GT the
#   撇 clearly CROSSES the top-left corner of the 竖弯钩 (near where the
#   top horizontal meets the vertical shaft, around (110, 130)). The two
#   strokes must intersect, not sit apart.
#
# Gap 2 — NO UPWARD HOOK at bottom-right of 竖弯钩:
#   In prior PNG the bottom-right end of the body stops FLAT (a rounded
#   cap that goes nowhere), so the shape reads as a plain "C" or "U". In
#   GT there is an unmistakable vertical hook flick going UP from about
#   (215, 260) to (215, 215) — a ~45 px upward tick. This flick is the
#   钩 in 竖弯钩 and defines the character.
#
# Gap 3 — TOP-RIGHT INTRO of the 竖弯钩 got mangled:
#   Prior PNG stitched the "top intro slant" and the shaft into one
#   confused blob so the shape has no clear top-right horizontal. In GT
#   stroke-2 clearly begins with a short RIGHT-going horizontal segment
#   at the top (from about (135, 130) to (200, 145)) BEFORE curving down
#   into the shaft. That top horizontal is missing/absent in prior.
#
# ---
# # RETRY MEMORY CHECKLIST (mandatory)
# # Q1 (errata): errata Fix-idea for 匕 (B4 table): "terminate pie ON shaft
# #   (compute weld pixel) — pie_point helper". Prior retries had the
# #   pie floating. Fix: make the 撇's lower half CROSS the elbow of
# #   the 竖弯钩 at (~110, 145), so the strokes visibly intersect.
# # Q2 (form_catalog): 撇 in "short-lean 撇 crossing shaft" role (like
# #   the 撇 in 千/子). Thin taper 6→3 px. 竖弯钩 as one continuous stroke
# #   with visible hook flick at the end (form ceiling item — hand-inline).
# # Q3 (helpers): pie_point would compute the weld pixel, but v8 says
# #   trust GT. I'll place the 撇 endpoints so it naturally crosses the
# #   elbow, then draw the 竖弯钩 as one hand-inlined polyline with an
# #   explicit up-going hook segment appended.
#
# GT observation (pixels, 300x300):
#   Stroke 1 (撇): from ~(122, 82) diagonally down-left, curving slightly,
#     through the top-left elbow of stroke-2 at ~(108, 140), continuing
#     to lower-left endpoint ~(80, 195). Thin, tapering.
#   Stroke 2 (竖弯钩), one continuous curve, drawn L-to-R at top then
#     down-then-right-then-up:
#     - Top horizontal: (135, 130) → (200, 145) [drawn right-going, slight
#       droop] — a short "小提"-like entry to the 竖弯钩.
#     - Actually MMH draws it beginning at (200, 145) going LEFT then
#       curving down. Rendering the shape rather than the stroke direction:
#     - Top-right terminus: (200, 145)
#     - Elbow into shaft: (108, 140)
#     - Vertical shaft: descends from (108, 140) down to (108, 258)
#     - Bottom curve: from (108, 258) right along baseline to (215, 262)
#     - HOOK flick UP: from (215, 262) up to (215, 215)  <-- must be visible
"""

from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300
OUT = Path(__file__).parent / "01_匕.png"


def stamped_polyline(d, points, w_head=6, w_tail=6, fill=(0, 0, 0)):
    """Draw a tapered polyline by stamping circles along it (calligraphic feel).

    Width interpolates linearly from w_head at points[0] to w_tail at points[-1].
    Simple, robust, and reads as an ink line at 300x300.
    """
    if len(points) < 2:
        return
    # cumulative arc length for interpolation
    seg_len = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        seg_len.append(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    total = sum(seg_len) or 1.0

    covered = 0.0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        L = seg_len[i]
        # sample densely along this segment
        n = max(2, int(L * 2))
        for k in range(n + 1):
            u_seg = k / n
            x = x1 + (x2 - x1) * u_seg
            y = y1 + (y2 - y1) * u_seg
            u_all = (covered + u_seg * L) / total
            w = w_head + (w_tail - w_head) * u_all
            r = w / 2.0
            d.ellipse([x - r, y - r, x + r, y + r], fill=fill)
        covered += L


def draw_pie(d):
    """Stroke 1: 撇 — short diagonal from top-center down-left, crossing
    through the elbow of stroke-2 at (~108, 140). Thin taper 6->3."""
    pts = [
        (122, 82),
        (117, 100),
        (112, 122),
        (108, 140),   # <-- crossing point with stroke-2 elbow
        (100, 160),
        (90, 180),
        (80, 197),
    ]
    stamped_polyline(d, pts, w_head=6, w_tail=3)


def draw_shu_wan_gou(d):
    """Stroke 2: 竖弯钩 — single continuous stroke:
    top-right terminus → elbow → vertical shaft → bottom curve → hook UP.
    """
    # Top horizontal segment: from top-right terminus back-left to elbow.
    top = [
        (200, 145),
        (180, 142),
        (155, 137),
        (135, 133),
        (120, 134),
        (110, 140),   # elbow — curves down into shaft
    ]
    stamped_polyline(d, top, w_head=6, w_tail=7)

    # Body: vertical shaft descending from elbow to bottom-left corner,
    # then curving right along the baseline. One continuous ink line.
    body = [
        (110, 140),
        (108, 165),
        (107, 195),
        (107, 225),
        (108, 250),
        (115, 262),   # bottom-left corner turn
        (140, 268),
        (170, 270),
        (195, 268),
        (212, 262),
        (218, 253),   # bottom-right corner turn
    ]
    stamped_polyline(d, body, w_head=7, w_tail=8)

    # Hook: explicit upward flick from the bottom-right corner. Must be
    # visible (~45 px vertical) — this is the 钩 that was missing before.
    hook = [
        (218, 253),
        (218, 240),
        (217, 225),
        (216, 215),
    ]
    stamped_polyline(d, hook, w_head=8, w_tail=3)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    # Draw stroke-2 (body) first so stroke-1 (撇) overlaps it at the crossing
    # — matches GT visual layering (撇 on top).
    draw_shu_wan_gou(d)
    draw_pie(d)
    img.save(OUT)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
