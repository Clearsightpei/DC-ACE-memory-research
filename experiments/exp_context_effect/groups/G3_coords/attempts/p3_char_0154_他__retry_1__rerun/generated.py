# VISUAL DIFF — prior retry_1 vs GT (compared PNG-to-PNG, not paraphrased)
#
# 1. 亻 (left radical): PRIOR — pie and shu are visibly DISCONNECTED.
#    Pie ends at ~y=175 (screen coord) and shu starts at y=95 further to
#    the right — there is a clear 30–40 px gap where the shu head should
#    weld to the mid-shaft of the pie. GT clearly shows the shu head
#    tucked INTO the pie shaft at roughly the pie's 40 % point, no gap.
#    FIX: place shu head ON the pie curve (compute point at u≈0.35).
#
# 2. 也 (right component): PRIOR reads as a CLOSED RECTANGLE with a
#    couple of divider lines and a tiny lower-right hook. In GT, 也 is
#    NOT rectangular — the LEFT edge is the 竖弯钩 opening slightly
#    outward (top at ~x=145, bottom-left at ~x=115) before sweeping
#    right; the 横折钩 top-heng is SHORTER than the full width and its
#    right-vertical is INSIDE the 竖弯钩's rightmost extent; and the
#    bottom sweep of 竖弯钩 extends well past the 横折钩 vertical before
#    hooking up. Prior collapsed all three strokes onto the same
#    bounding rectangle so nothing reads as separate strokes.
#    FIX: (a) top heng short, starting around x=155, ending x=235;
#         (b) 竖弯钩 left descent from (145,110) slanting to (118,240)
#             THEN sweeping right through bottom to (250,258) THEN
#             hooking up-right to (252,225);
#         (c) interior shu shorter and sitting between the two verticals.
#
# 3. Line weight in GT is thin+uniform-ish (~3–4 px). Prior used W=5
#    which is close but the "closed rectangle" perception was worse
#    because uniform thick lines darkened all corners. Keep W=4.

# RETRY MEMORY CHECKLIST (B4->B5 v7 evolution) — carried per protocol
# Q1 (errata): The fix idea from errata / prior retry header was
#   "inline 也 as bezier envelope + interior strokes; don't compose 3
#   separate bank primitives; render 亻 inline too". That is largely
#   correct but was executed poorly last time — the 亻 pie/shu weld was
#   never enforced and the 也 was drawn as a rectangle. Keep the inline
#   approach but ADD explicit weld math and non-rectangular 也 geometry
#   per the visual diff above.
# Q2 (form_catalog): Relevant rows — 亻 left pang (pie head high, shu
#   welded at pie mid-shaft), horiz-hook family (横折钩 short heng +
#   vertical + tiny hook), 竖弯钩 (long vertical → bottom sweep →
#   upward tip hook).
# Q3 (helpers): No clean helper match — this is inline composition
#   with a weld point (pie mid-shaft × shu head). Do the weld math
#   directly rather than importing helpers.

import os
from PIL import Image, ImageDraw

CANVAS = 300
W = 4  # thin uniform-ish ink per P12 (MMH GT is thin)


def _bezier_pts(p0, p1, p2, n=60):
    out = []
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        out.append((x, y))
    return out


def _bezier_at(p0, p1, p2, u):
    x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
    y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
    return (x, y)


def draw_line(d, p0, p1, w=W):
    d.line([p0, p1], fill="black", width=w)
    # small round caps to prevent square-end artifacts
    r = w / 2
    for p in (p0, p1):
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")


def draw_curve(d, p0, p1, p2, w=W):
    pts = _bezier_pts(p0, p1, p2)
    d.line(pts, fill="black", width=w, joint="curve")


def draw_ren_pang_inline(d):
    """亻 on left third. Explicit weld: shu head sits ON pie curve at u=0.35."""
    # Pie (撇): sweep from upper-mid down-left. Screen coords, y grows down.
    pie_p0 = (105, 60)   # top head (high on canvas)
    pie_p1 = (85, 130)   # bow control (slight outward bow to the left)
    pie_p2 = (50, 235)   # tail lower-left
    draw_curve(d, pie_p0, pie_p1, pie_p2, w=W)

    # Compute weld point at u=0.35 along the pie — this is where the
    # shu head must touch the pie shaft (fixes prior "floating shu" bug).
    weld = _bezier_at(pie_p0, pie_p1, pie_p2, 0.35)
    weld_x = weld[0] + 6   # shu sits just right of pie centerline
    weld_y = weld[1]

    # Shu (竖): straight vertical from weld point down.
    draw_line(d, (weld_x, weld_y), (weld_x, 260), w=W)


def draw_ye_inline(d):
    """也 on right two-thirds. Three strokes, explicitly NOT a rectangle.

    Stroke A: 横折钩 — short heng at top starting middle-right, then
              vertical drop (this vertical sits INSIDE the outer 竖弯钩),
              then tiny hook up-left at bottom.
    Stroke B: interior 竖 — short vertical between A's shu and 竖弯钩 left.
    Stroke C: 竖弯钩 — LEFT edge starts high, slants slightly outward
              descending, then sweeps rightward along the bottom past
              A's shu, ends with an upward hook well right of A.
    """

    # --- Stroke A: 横折钩 ---
    # top heng — short, does not span full 也 width
    a_top_l = (158, 108)
    a_top_r = (238, 108)
    draw_line(d, a_top_l, a_top_r, w=W)
    # right vertical descending from top-right corner
    a_bot = (238, 218)
    draw_line(d, a_top_r, a_bot, w=W)
    # tiny hook at bottom of this vertical, flicking up-left
    draw_line(d, a_bot, (224, 210), w=W)

    # --- Stroke B: interior 竖 (short) ---
    # sits between the 竖弯钩 left edge and A's right vertical.
    # Kept SHORT (128..200) — GT interior shu doesn't reach bottom.
    draw_line(d, (192, 132), (192, 205), w=W)

    # --- Stroke C: 竖弯钩 ---
    # (1) left descent — starts BELOW top-heng (y=128, not above it) and
    #     slants slightly OUTWARD (top x=142, bottom x=118) so the left
    #     edge is unmistakably NOT rectangular
    c_top = (142, 128)
    c_low = (118, 238)
    draw_line(d, c_top, c_low, w=W)
    # (2) rounded corner into bottom sweep (quad bezier)
    corner_end = (150, 262)
    draw_curve(d, c_low, (120, 262), corner_end, w=W)
    # (3) bottom sweep — extends RIGHT past A's vertical (238) all the
    #     way to ~252
    sweep_end = (250, 262)
    draw_line(d, corner_end, sweep_end, w=W)
    # (4) upward hook on the right end — tip goes up past A's vertical
    hook_ctrl = (258, 258)
    hook_tip = (250, 226)
    draw_curve(d, sweep_end, hook_ctrl, hook_tip, w=W)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_ren_pang_inline(d)
    draw_ye_inline(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_他.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    render()
