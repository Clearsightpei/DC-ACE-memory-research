# p2_radical_025_力 — retry_1, inline-fresh recipe (TR8/P11 lesson).
#
# Prior attempt used heng_zhe_gou primitive at scale=0.70. Failures:
#   1. Primitive corner was square/machined — GT shows soft rounded turn.
#   2. Descender ran perfectly VERTICAL — GT shows the descender bows
#      LEFTWARD (concave-right) and terminates in a distinct up-left hook.
#   3. pie primitive used was straight — GT 撇 curves gently.
#   4. 撇 head did not visibly cross through the top-horizontal — sat on it.
#
# Fix (inline everything per TR8 / v7 form_catalog approach):
#   - Stroke 1 (横折钩) as ONE continuous polyline:
#       * top 横: PIL(88,110) → PIL(210,105) — slight lift, w~11.
#       * corner 顿笔 blob at PIL(210,108), r=5.
#       * descender as quadratic bezier from PIL(210,108) through
#         control PIL(178,175) to base PIL(178,235). This bows LEFT
#         (concave-right, matching GT). Width ~10.
#       * hook flick: from base PIL(178,235) up-and-left to PIL(155,215),
#         tapered 10→2. Direction: UP-and-LEFT (per P1 hook rule +
#         GT observation).
#   - Stroke 2 (撇) via variant_pie:
#       * head math (30, +45) → PIL(180, 105) — starts ON/JUST ABOVE
#         the top horizontal near its middle-right (crosses the 横 at
#         ~75% span, matching GT where 撇 emerges from inside horizontal).
#       * tail math (-95, -110) → PIL(55, 260) — sweeps far bottom-left.
#       * bow_perp -8 (curve concave-up-right), w_head 9, w_tail 1.
#       * source: form_catalog "撇 | 大-family crossing arm" row
#         (0,+25)→(-95,-110) — nearly identical geometry to 力's 撇.

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from _shared_helpers import tapered_line, tapered_bezier, variant_pie, to_px  # noqa: E402


def render():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # --- STROKE 1: 横折钩 inlined as continuous polyline ---

    # Revision 1: shrink top 横 (was too wide vs GT ~90px), keep bowed
    # descender + up-left hook, and shorten 撇 tail (GT tail ends around
    # PIL(70, 240), not 55/260). Shift character slightly right so it
    # centers better.

    # 1a. Top 横 (short, slight upward drift left→right).
    # Math coords: (-45, +40) → (+55, +45). Width ~100 px (GT ~95).
    tapered_line(d, (-45, 40), (55, 45), w0=10, w1=11, n=32)

    # 1b. 顿笔 corner blob at right end.
    cx, cy = to_px(55, 45)  # PIL (205, 105)
    r = 5.5
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # 1c. Descender bows LEFT (concave-right per GT).
    # From corner (55, 45) via control (28, -20) to base (30, -75).
    tapered_bezier(d, (55, 45), (28, -20), (30, -75),
                   w_head=10, w_tail=9, n=48)

    # 1d. Hook flick up-and-LEFT from base.
    tapered_line(d, (30, -75), (8, -55), w0=9, w1=2, n=20)

    # --- STROKE 2: 撇 crossing through top horizontal ---
    # Head just above/on the top horizontal near ~70% across.
    # Tail at PIL(65, 245) ~ math (-85, -95).
    variant_pie(d,
                head=(20, 48),        # PIL(170, 102) — on top-horizontal
                tail=(-85, -95),      # PIL(65, 245) — bottom-left
                bow_perp=-7.0,        # concave-up-right, soft bow
                w_head=9.0,
                w_tail=1.0,
                n=54)

    out = Path(__file__).parent / "01_力.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
