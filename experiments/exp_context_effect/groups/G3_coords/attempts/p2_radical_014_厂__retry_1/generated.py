# 厂 (chang) — 2-stroke radical, RETRY #1.
#
# Prior attempt failure diagnosis (from sandbox.md):
#   - Heng was too short (scale 0.75, ox=+35) and shifted right.
#   - The inlined "pie" used control point (mx = x0 - 40, my = y0 - 10)
#     which pulled the top of the pie LEFT-then-DOWN, producing an
#     arching hook-like curve rather than a mostly-vertical 丿 descent.
#   - Result read as one continuous swoosh, not 一 + 丿.
#
# Retry fix (sandbox.md idea, coord-form):
#   1. Widen the heng: scale ~0.90, centered near canvas x-center-slight-
#      right, high on canvas. Left end should reach further left so the
#      pie head sits well-left. Standalone heng half-len = 100*0.90 = 90.
#      Placement: ox=+10, oy=+70 → left end at math (-80, +70), right end
#      at math (+100, +70). Spans 60% of canvas width but sits high.
#      Actually, GT shows heng spanning ~two-thirds; let's use scale=0.85
#      with ox=+5, oy=+70 → left end (-80, +70), right end (+90, +70).
#   2. Pie: inline a nearly-vertical descent from the heng's LEFT end
#      down to lower-left, with the control point placed close to the
#      midpoint of the chord (NO leftward pull at head). Only the last
#      ~30% of the curve should scoop leftward.
#      Head at (-80, +65) (just inside/below heng left tip so they weld).
#      Tail at (-105, -105) (lower-left, slight leftward offset).
#      Control point at midpoint of chord + tiny leftward push near tail:
#      chord mid = ((-80-105)/2, (65-105)/2) = (-92.5, -20).
#      Push control mildly leftward: mx = -100, my = -20. This keeps
#      the top nearly vertical and only develops a leftward scoop at
#      the bottom.
#
# TR compliance:
#   - heng call: ox=+5, oy=+70, scale=0.85 (deliberate — widens the top
#     to cover roughly two-thirds of canvas horizontal; TR2 says radical
#     in "top" position uses scale 0.75-0.90).
#   - pie call: NOT using bank pie primitive (per P10 — bank pie too
#     diagonal; the radical form is a soft nearly-vertical scoop).
#     Inlined as `draw_radical_pie` with explicit head/tail endpoints.
#   - Weld check: heng half_len = 100*0.85 = 85; heng's math left end
#     = (+5 - 85, +70) = (-80, +70). Pie head at (-80, +65) — welds
#     within 5 px vertical.

from PIL import Image, ImageDraw
import os, sys

REPO = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect"
sys.path.insert(0, os.path.join(REPO, "groups/G3_coords/success_bank/code"))

from heng import draw_heng

CANVAS = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_radical_pie_vertical(t, x0, y0, x1, y1, ctrl_x, ctrl_y,
                              w_head=11.0, w_tail=2.0, n=90):
    """Inlined 丿 for 厂's radical: nearly-vertical descent with a soft
    scoop only near the tail. Bezier control point provided explicitly
    so the caller places the curl deliberately (per TR7 eyeball sanity).
    Head thick, tail tapering.
    """
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * ctrl_x + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * ctrl_y + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # Stroke 1: heng, wide (0.85 * standalone), placed high, centered
    # slightly right of canvas center so its LEFT end reaches x=-80.
    #   math-coord center = (+5, +70)
    #   math-coord left  end = (-80, +70)  ← pie head welds here
    #   math-coord right end = (+90, +70)
    draw_heng(t, ox=+5, oy=+70, scale=0.85)

    # Stroke 2: inlined 丿 radical — nearly vertical with soft tail scoop.
    #   head at (-80, +65) — 5 px below heng center-line to weld cleanly
    #   tail at (-105, -105) — lower-left
    #   ctrl at (-100, -20) — chord midpoint pushed only slightly left
    #     so the top ~60% is nearly vertical, curl develops at bottom
    draw_radical_pie_vertical(
        t,
        x0=-80, y0=+65,
        x1=-105, y1=-105,
        ctrl_x=-100, ctrl_y=-20,
        w_head=11.0, w_tail=2.0,
    )

    out = os.path.join(
        REPO,
        "groups/G3_coords/attempts/p2_radical_014_厂__retry_1/01_厂.png",
    )
    img.save(out)
    print("saved:", out)


if __name__ == "__main__":
    main()
