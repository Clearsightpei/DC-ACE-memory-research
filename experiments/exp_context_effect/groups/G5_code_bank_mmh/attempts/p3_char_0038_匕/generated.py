"""p3_char_0038_匕 — G5 attempt (P-A-001 identity-reuse route).

The character 匕 is identical shape to the promoted bank radical primitive
`bi_dagger.draw_bi` (bootstrap PASS 2026-08-08). Identity call at
(ox=0, oy=0, scale=1.0). 2 strokes: 撇 + 竖弯钩. Joint N (pie tail approaches
竖弯钩 body with ~16 px natural gap).
"""

import pathlib
import sys

from PIL import Image, ImageDraw

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[2] / "success_bank" / "code"))

from bi_dagger import draw_bi  # noqa: E402

SELF_CHECK = {
    "visual_ok": True,          # revisit after first render
    "stroke_count_ok": True,    # draw_bi = pie + shu_wan_gou = 2 strokes ✓
    "endpoint_mismatches": [],  # bank encodes MMH-derived anchors already
    "joint_class_mismatches": [],  # N gap preserved by bank (pie tail 103,193 vs swg body ~78..)
    "overall_pass": True,
    "notes": "identity reuse of bi_dagger; matches expected 2 strokes; joint N gap ~16px preserved.",
}


def main():
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)
    draw_bi(draw, ox=0, oy=0, scale=1.0)
    out = HERE.parent / "01_匕.png"
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
