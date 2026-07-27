"""p2_radical_127_牙 — 4-stroke radical.

Revision 1: adjustments after v1 self-check
  - moved top 横 up and right, made it shorter
  - lengthened middle heng and made shoulder more prominent
  - moved 撇 head up so its origin is near the top-right corner
  - kept 竖钩 spanning full height with terminal upward-left flick

Strokes (per typical MMH order):
  1. 横 (short top horizontal) — upper middle-right
  2. 竖折 (down-left slant then middle heng right) — the shoulder
  3. 竖钩 (long vertical hook on right) — from top-right down w/ hook
  4. 撇 (long sweeping stroke crossing from upper right to lower left)
"""

import sys, os
from PIL import Image, ImageDraw

BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))
from _shared_helpers import (
    to_px, tapered_line, tapered_bezier, variant_pie,
)


def draw_ya(draw, ox=0, oy=0, scale=1.0):
    # ---- Stroke 1: short 横 at upper mid — a short bar
    h1_head = (ox + -10 * scale, oy + 72 * scale)
    h1_tail = (ox + 50 * scale, oy + 76 * scale)
    tapered_line(draw, h1_head, h1_tail, 8, 11)
    # tiny 顿笔 at right end
    rx, ry = to_px(*h1_tail)
    draw.ellipse([rx - 5, ry - 5, rx + 5, ry + 5], fill=(0, 0, 0))

    # ---- Stroke 2: 竖折 — starts left of stroke1 as a short 撇/竖 that
    # descends to the shoulder, then folds RIGHT along the middle.
    # sub-A: down-left slant
    zh_p0 = (ox + -10 * scale, oy + 72 * scale)     # meets top heng start
    zh_p1 = (ox + -55 * scale, oy + 20 * scale)     # shoulder corner
    tapered_line(draw, zh_p0, zh_p1, 11, 11)
    # sub-B: middle heng from shoulder rightward to right shaft
    zh_p2 = (ox + -55 * scale, oy + 18 * scale)
    zh_p3 = (ox + 55 * scale, oy + 22 * scale)
    tapered_line(draw, zh_p2, zh_p3, 11, 11)
    # 顿笔 blob at fold
    cx, cy = to_px(*zh_p1)
    draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(0, 0, 0))

    # ---- Stroke 3: 竖钩 — long vertical shaft down the right side
    sg_top = (ox + 55 * scale, oy + 75 * scale)
    sg_bot = (ox + 58 * scale, oy + -100 * scale)
    tapered_line(draw, sg_top, sg_bot, 10, 9)
    # hook: flick up-left from base
    hook_base = (ox + 58 * scale, oy + -97 * scale)
    hook_tip  = (ox + 28 * scale, oy + -70 * scale)
    tapered_line(draw, hook_base, hook_tip, 10, 2)

    # ---- Stroke 4: long 撇 sweeping upper-right → lower-left
    pie_head = (ox + 55 * scale, oy + 55 * scale)
    pie_tail = (ox + -95 * scale, oy + -115 * scale)
    variant_pie(draw, pie_head, pie_tail,
                bow_perp=-16, w_head=10, w_tail=1.5)


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_ya(draw, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_牙.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
