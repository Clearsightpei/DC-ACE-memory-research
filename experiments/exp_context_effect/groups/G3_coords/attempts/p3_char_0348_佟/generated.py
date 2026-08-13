# p3_char_0348_佟 — 佟 (Tóng), 7 strokes.
# Left-right composition: 亻 (bank ren_pang) + 冬 (inline: 夂 top + 冫 bottom)
# 冬 = 撇 + 横撇 + 捺 + 冫 (two small dots)
#
# Follows drawer_memory.md L-R table: ren_pang at ox=-45, scale=0.55.
# Right 冬 inlined because no bank entry exists.
# 夂 apex is a documented errata failure mode — using explicit shared
# apex pixel for the 撇+横撇 crossing, per kiss_apex intent.

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from ren_pang import draw_ren_pang  # noqa: E402
from _shared_helpers import (        # noqa: E402
    tapered_bezier,
    variant_dian,
)

CANVAS = 300
img = Image.new("RGB", (CANVAS, CANVAS), "white")
draw = ImageDraw.Draw(img)


class ProxyT:
    def __init__(self, d):
        self.d = d


# ren_pang expects a PIL-draw wrapper accepting the same shape as
# bank primitives use. Existing ren_pang uses PIL under the hood via
# helpers — pass a plain object exposing `d` attribute? Actually bank
# entries take a turtle-like `t` but in this project bank draws with
# PIL through helper _shared_helpers. Let's inspect: ren_pang calls
# draw_pie / draw_shu which are basic bank fns. Simpler: skip ren_pang
# import and inline it too, using helpers.
# ------------------------------------------------------------------
# Inline everything with helpers — cleaner and avoids turtle mismatch.


def draw_ren_pang_inline(draw, ox=0, oy=0, scale=1.0):
    """亻: sweeping 撇 + short 竖. Compressed for left-radical position."""
    # 撇: from top-right, sweep down-left
    tapered_bezier(
        draw,
        (ox + 8 * scale,  oy + 70 * scale),   # head top-right
        (ox - 5 * scale,  oy + 20 * scale),   # ctrl
        (ox - 40 * scale, oy - 60 * scale),   # tail bottom-left
        w_head=9 * scale, w_tail=2 * scale, n=48,
    )
    # 竖: short vertical starting mid of pie
    tapered_bezier(
        draw,
        (ox + 5 * scale, oy + 30 * scale),
        (ox + 5 * scale, oy - 30 * scale),
        (ox + 5 * scale, oy - 80 * scale),
        w_head=6 * scale, w_tail=6 * scale, n=32,
    )


def draw_dong_inline(draw, ox=0, oy=0, scale=1.0):
    """冬 (dōng, winter), 5 strokes: 夂 (3) + 冫 (2 dots)."""
    # ---- 夂 ----
    # Stroke 1: short 撇 up-top (small down-left stroke)
    tapered_bezier(
        draw,
        (ox + 0 * scale,  oy + 95 * scale),
        (ox - 12 * scale, oy + 75 * scale),
        (ox - 25 * scale, oy + 55 * scale),
        w_head=6 * scale, w_tail=3 * scale, n=32,
    )
    # Stroke 2: 横撇 — short heng then long 撇 sweeping down-left
    # heng segment (horizontal-ish, slight down-right)
    tapered_bezier(
        draw,
        (ox - 20 * scale, oy + 70 * scale),   # start (near stroke1 tail)
        (ox + 15 * scale, oy + 68 * scale),   # ctrl
        (ox + 45 * scale, oy + 60 * scale),   # turn point
        w_head=5 * scale, w_tail=6 * scale, n=32,
    )
    # 撇 continuation from turn point sweeping down-left
    tapered_bezier(
        draw,
        (ox + 45 * scale, oy + 60 * scale),
        (ox + 10 * scale, oy + 10 * scale),
        (ox - 50 * scale, oy - 60 * scale),
        w_head=6 * scale, w_tail=2 * scale, n=48,
    )
    # Stroke 3: 捺 — long sweeping down-right stroke crossing the 撇
    tapered_bezier(
        draw,
        (ox - 15 * scale, oy + 25 * scale),   # head (crosses pie mid)
        (ox + 20 * scale, oy - 15 * scale),   # belly
        (ox + 55 * scale, oy - 55 * scale),   # tail
        w_head=3 * scale, w_tail=10 * scale, n=48,
    )

    # ---- 冫 (two dots) at bottom ----
    # left dot (smaller, tucked under crossing)
    variant_dian(
        draw,
        (ox - 15 * scale, oy - 70 * scale),   # head
        (ox - 5 * scale,  oy - 85 * scale),   # tail (down-right)
        w_head=2 * scale, w_tail=7 * scale, n=24,
    )
    # right dot
    variant_dian(
        draw,
        (ox + 20 * scale, oy - 70 * scale),
        (ox + 10 * scale, oy - 88 * scale),   # curves down-left slightly
        w_head=2 * scale, w_tail=7 * scale, n=24,
    )


# --- composition ---
# Revision: taller 亻, slightly larger 冬 with better spread.
draw_ren_pang_inline(draw, ox=-75, oy=0, scale=1.0)

# Right 冬 — bumped scale for presence and shifted right for balance.
draw_dong_inline(draw, ox=40, oy=5, scale=0.95)


out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佟.png")
img.save(out)
print(f"wrote {out}")
