"""p3_char_0128_太 — 太 = 大 + 丶 (dot below the crotch).

Composition: reuse bank primitive `draw_da` (3 strokes: heng+pie+na)
for the base 大, then add a tapered `draw_dian` at the MMH-specified
BC-cell location for the 4th stroke.
"""
import sys
from pathlib import Path

BANK = Path("<REPO_ROOT>/experiments/exp_context_effect/groups/G5_code_bank_mmh/success_bank/code")
sys.path.insert(0, str(BANK))

from PIL import Image, ImageDraw

from da_big import draw_da
from dian import draw_dian


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,      # 3 (from draw_da: heng+pie+na) + 1 dian = 4
    'endpoint_mismatches': [],
    'joint_class_mismatches': [], # P at s1-s2 mid via draw_da; N gaps preserved by using bank geometry + separate dian
    'overall_pass': True,
    'notes': '大 base reused from bank; s4 dian placed per MMH BC-cell anchors.',
}


def render(path: str):
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # Strokes 1-3: reuse bank 大 primitive as-is (identity transform).
    draw_da(draw, ox=0, oy=0, scale=1.0)

    # Stroke 4: dian below the crotch.
    # MMH anchors: head BC(0.166, 0.525) -> (116.6, 252.5)
    #              tail BC(0.462, 0.786) -> (146.2, 278.6)
    # The dot arcs down-and-right, thin head -> thicker tail.
    s4_head = (116.6, 252.5)
    s4_tail = (146.2, 278.6)
    draw_dian(draw, s4_head, s4_tail,
              w_head=2.5, w_tail=5.5, bow=3, steps=60)

    img.save(path)


if __name__ == "__main__":
    out = Path(__file__).parent / "01_太.png"
    render(str(out))
    print("wrote", out)
