"""p3_char_0198_立 (lì, 'stand') — G5 attempt.

Composition: 5 strokes per MMH.
  s1: top 点 (dian)
  s2: upper 横 (heng, medium length)
  s3: left short dot/pie (short, down-right per MMH)
  s4: right short pie (down-left)
  s5: bottom 横 (long baseline heng)

s4↔s5 joint: N (neighbor, ~20px gap — do NOT weld).

Uses bank: dian.py, heng.py. Two short strokes (s3, s4) inlined as
tapered short lines because they are too short/atypical for dian
signature.
"""

import sys
from pathlib import Path

BANK_DIR = Path(__file__).resolve().parents[3] / "G5_code_bank_mmh" / "success_bank" / "code"
sys.path.insert(0, str(BANK_DIR))

from PIL import Image, ImageDraw

from dian import draw_dian  # noqa: E402
from heng import draw_heng  # noqa: E402


# ---------- MMH-derived pixel anchors (300x300 canvas) ----------
# cell mapping: TC=(100..200, 0..100), ML=(0..100, 100..200),
#               MR=(200..300, 100..200), BL=(0..100, 200..300),
#               BC=(100..200, 200..300), BR=(200..300, 200..300),
#               C =(100..200, 100..200)
S1_HEAD = (124.2, 73.8)    # TC (0.242, 0.738)
S1_TAIL = (165.2, 98.1)    # TC (0.652, 0.981)
S2_HEAD = (80.6, 153.8)    # ML (0.806, 0.538)
S2_TAIL = (220.0, 134.8)   # MR (0.20,  0.348)
S3_HEAD = (93.8, 187.2)    # ML (0.938, 0.872)
S3_TAIL = (118.4, 227.3)   # BC (0.184, 0.273)
S4_HEAD = (176.7, 164.9)   # C  (0.767, 0.649)
S4_TAIL = (156.2, 253.4)   # BC (0.562, 0.534)
S5_HEAD = (33.4, 273.3)    # BL (0.334, 0.733)
S5_TAIL = (271.0, 271.6)   # BR (0.71,  0.716)


def _draw_short_tapered(draw, head, tail, w_head, w_tail, steps=40):
    """Inline: short tapered stroke (used for the two body dots which
    are longer than a proper dian but shorter than a full pie)."""
    (x0, y0), (x1, y1) = head, tail
    for i in range(steps):
        t = i / (steps - 1)
        w = w_head + (w_tail - w_head) * t
        cx = x0 + (x1 - x0) * t
        cy = y0 + (y1 - y0) * t
        r = max(1.0, w / 2)
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=0)


def render(path: str):
    img = Image.new("L", (300, 300), 255)
    d = ImageDraw.Draw(img)

    # s1: top dian (small dot)
    draw_dian(d, S1_HEAD, S1_TAIL, w_head=3, w_tail=9, bow=4, steps=48)

    # s2: upper heng (medium length ~140px)
    draw_heng(d, S2_HEAD, S2_TAIL, width_head=8, width_tail=9)

    # s3: left body dot (short, ~47px, tapered head->tail thickening)
    _draw_short_tapered(d, S3_HEAD, S3_TAIL, w_head=4, w_tail=10, steps=44)

    # s4: right body pie/dot (short, ~90px, tapered)
    _draw_short_tapered(d, S4_HEAD, S4_TAIL, w_head=4, w_tail=9, steps=60)

    # s5: bottom heng (long baseline, ~238px)
    draw_heng(d, S5_HEAD, S5_TAIL, width_head=10, width_tail=11)

    img.save(path)


SELF_CHECK = {
    "visual_ok": True,
    "stroke_count_ok": True,        # 5 stroke primitives called (dian, heng, tapered, tapered, heng)
    "endpoint_mismatches": [],       # all endpoints placed exactly at MMH anchors
    "joint_class_mismatches": [],    # s4.tail y=253 vs s5.mid y≈272 → ~19px vertical gap = N (matches spec)
    "overall_pass": True,
    "notes": "s4 ends at (156, 253); s5 baseline y≈272. Vertical gap ~19px matches expected N gap (20.1px).",
}


if __name__ == "__main__":
    render(str(Path(__file__).parent / "01_立.png"))
