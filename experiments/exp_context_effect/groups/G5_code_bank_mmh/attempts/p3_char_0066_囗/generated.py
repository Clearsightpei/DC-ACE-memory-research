"""p3_char_0066_囗 (wei, enclosure) — bank identity reuse.

The character 囗 is the same 3-stroke enclosure radical already promoted
as `wei_enclose.py` (from p2_radical_073_囗, G5 B2 PASS). Direct
identity-reuse (P-A-001 route): call `draw_wei(draw)` with default
(ox=0, oy=0, scale=1.0) — the bank primitive is already sized for the
full 300×300 canvas.

Stroke count: 3 (matches MMH expectation).
Anchors: same skeleton the bank primitive was PASSed on; MMH endpoint
anchors for this dispatch are geometrically identical to those of the
Phase-2 radical (both are just 囗 rendered at canvas scale).
Joints: all three joints are class N (natural calligraphic gap), which
is exactly what `draw_wei` produces (shu / heng_zhe_box / heng do not
weld — the endpoints are offset by MMH's original 3–7 px gaps × the
bank's coordinate spacing, giving ~14–24 px gaps on the 300 canvas).
"""

import os
import sys

from PIL import Image, ImageDraw

# Add the bank directory to sys.path so we can import the primitive.
_BANK = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "success_bank", "code",
)
sys.path.insert(0, os.path.abspath(_BANK))

from wei_enclose import draw_wei  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,           # verified after first render vs GT
    'stroke_count_ok': True,     # 3 primitive calls inside draw_wei (shu, heng_zhe_box, heng)
    'endpoint_mismatches': [],   # bank primitive was PASSed on identical MMH anchors
    'joint_class_mismatches': [],# all 3 joints are N — bank produces natural gaps, not welds
    'overall_pass': True,
    'notes': 'Identity-reuse of wei_enclose.py (P-A-001). Same character, same skeleton.',
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_wei(draw)  # default ox=0, oy=0, scale=1.0 — fills canvas
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_囗.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
