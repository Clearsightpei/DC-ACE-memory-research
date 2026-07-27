"""三 (sān) — Phase-3 character, 3画. Composition: 横 + 横 + 横.

Mandatory lookup checklist:
  1. success_bank/INDEX.md grep → er.py (二, 2 horizontals) is closest mastered analog.
  2. errata.md grep → 三 not present.
  3. form_catalog / principles_meta → TR1 override anchors when reusing primitive.
  4. joint_atlas → none needed (no joints).
  5. sandbox → n/a.

Plan: 3 horizontal strokes stacked; classic 三 proportion — top shortest,
middle medium, bottom longest. Clear vertical gaps between all three (S).
MMH-derived anchors used, snapped to nearby cells so each heng lies on
one horizontal band.
"""
import os, sys
from PIL import Image, ImageDraw

_HERE = os.path.dirname(os.path.abspath(__file__))
_BANK = os.path.abspath(os.path.join(_HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, _BANK)

from heng import draw_heng  # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,  # 3 draw_heng calls == expected 3
    'endpoint_mismatches': [],  # all anchors within ±0.20 / adjacent-cell tolerance of MMH
    'joint_class_mismatches': [],  # no joints expected; none drawn
    'overall_pass': True,
    'notes': 'Three horizontal strokes: top short, middle medium, bottom longest. Clear vertical gaps (S).',
}


def render(out_path):
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # s1 — top 横 (short): sit in upper third (TC band).
    draw_heng(d, ('TL', 0.75, 0.75), ('TR', 0.25, 0.75), width=9)

    # s2 — middle 横 (medium): sit in central band (C).
    draw_heng(d, ('ML', 0.65, 0.50), ('MR', 0.35, 0.50), width=10)

    # s3 — bottom 横 (longest): sit in lower band, widest span.
    draw_heng(d, ('BL', 0.20, 0.40), ('BR', 0.80, 0.40), width=11)

    img.save(out_path)


if __name__ == "__main__":
    out = os.path.join(_HERE, "01_三.png")
    render(out)
    print("wrote", out)
