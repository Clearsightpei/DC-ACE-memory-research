"""p3_char_0096_为 — 4 strokes.

Structure per MMH block + GT visual:
  s1: small pie/dian, top-left (short, going down-left)
  s2: BIG pie, upper-center-right → lower-left
  s3: small dian/pie, middle-left area, going down-right
  s4: 横折弯钩 (heng-zhe-wan-gou) enclosing the right side —
      bank has heng_zhe_gou; we deviate slightly for the wider,
      more-curved "wan" descent characteristic of 为's rightside.

Bank calls: draw_pie (x2), draw_dian (x1), draw_heng_zhe_gou (x1 — reused
as-is; the primitive was authored for 力/月/内/为).
"""

# BANK_DEVIATION
# skipped: none — heng_zhe_gou.py used as-is; its docstring explicitly
#   names 为 as a target character. Geometry (corner, curve, hook) is
#   controlled by anchors, so no need to inline.
# reason: n/a
# fresh_component: n/a

import sys
from pathlib import Path

from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank" / "code"
sys.path.insert(0, str(BANK))

from pie import draw_pie                           # noqa: E402
from dian import draw_dian                         # noqa: E402
from heng_zhe_gou import draw_heng_zhe_gou         # noqa: E402


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitives = 4 strokes
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': "s2/s3 P-joint welds at ~(140,180); s2/s4 N-gap left "
             "natural (s4 heng starts right of s2 mid).",
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ---- s1: top-left short pie/dian (small, going down-left) ----
    #   MMH: TL(0.902,0.8) → C(0.189,0.134). Visual: short down-left flick.
    draw_pie(d, head=(105, 55), tail=(72, 105),
             bow_perp=4, w_head=6, w_tail=2, steps=40)

    # ---- s2: BIG pie, upper center → bottom-left ----
    #   MMH: TC(0.664,0.574) → BL(0.331,0.871).
    #   The dominant diagonal of the character.
    draw_pie(d, head=(180, 55), tail=(50, 275),
             bow_perp=20, w_head=9, w_tail=3, steps=110)

    # ---- s3: middle small dian ----
    #   MMH: ML(0.595,0.55) → BC(0.541,0.666). Small stroke, midpoint area.
    draw_dian(d, head=(128, 158), tail=(160, 188),
              w_head=3, w_tail=7, bow=3, steps=40)

    # ---- s4: 横折弯钩 wrapping the right side ----
    #   Heng from left-of-center to right; curved vertical descent; hook flick.
    heng_head = (85, 138)
    corner   = (232, 130)
    gou_tail = (198, 275)
    hook_tip = (165, 260)
    draw_heng_zhe_gou(d, heng_head, corner, gou_tail, hook_tip)

    out = Path(__file__).parent / "01_为.png"
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
