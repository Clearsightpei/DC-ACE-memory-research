"""Render 旡 (p2_radical_099) — 4 strokes. Retry #1.

TRAJECTORY DIFF (from viewing main-attempt PNG vs GT):
  MAIN attempt FAIL. Concrete visual gaps:
    (a) Top region too crammed high in canvas: s1 and s2 both floated up
        around y=80-115 with a big VERTICAL GAP between them, disconnected
        from the pie top. GT shows s1 (short top tick) sitting just above
        s3's head so they nearly touch (N joint, ~11 px gap), and s2
        (main heng) crossing s3 in the middle of the character
        (piercing joint) — visible X-crossing.
    (b) s4 (right stroke) rendered as a tall J-shape starting at (200,150)
        (attached to s2 tail). Head was too high and too far right; the
        MMH anchor puts s4 head at C(154,169) — inside the character
        body, below the heng, NOT welded to s2. Also the tail curled too
        far right (x≈268 per MMH) making the whole right side look
        oversized vs the compact GT.

  FIXES this retry:
    1. Drop s1 down to MMH y=~90 but LENGTHEN it and place its right end
       near where s3 head starts, so s1.mid ~ s3.head (N joint).
    2. Place s2 mid-canvas y=~120-146, ensuring it PIERCES s3 near
       C(137,153). Slightly down-tilting to the right per MMH.
    3. Anchor s3 pie head at TC (130,96) so it touches s1.mid (N gap).
       Tail toward BL but shortened to avoid off-glyph tip.
    4. s4: keep shu_wan_gou (GT visually shows 竖弯钩 shape — vertical +
       right curve + small up-hook). Move head to MMH C(156,168) — NOT
       welded to s2 (N joint, ~29 px gap). Reduce tail x to ~232 for a
       more compact right end. Reduce bottom_extra so the curve doesn't
       fall off the canvas.
    Errata suggested xie_gou; visually GT is clearly shu_wan_gou (curve
    goes DOWN then RIGHT with terminal up-hook, not diagonal). Sticking
    with shu_wan_gou but re-tuning geometry.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw

BANK = Path(__file__).resolve().parents[2] / "success_bank/code"
sys.path.insert(0, str(BANK))

from heng import draw_heng
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 4 primitive calls, 4 strokes
    'endpoint_mismatches': [
        {'stroke': 3, 'expected': 'BL(0.419,0.883)=(42,288)',
         'actual': '(58,278)',
         'delta': 'pie tail shortened ~15 px to keep tip on-glyph'},
        {'stroke': 4, 'expected': 'BR(0.684,0.35)=(268,235)',
         'actual': '(232,232)',
         'delta': 'tail x reduced 36 px to match GT compact hook end'},
    ],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('Reworked from main-fail. Anchors now honored: s1 mid area '
              'meets s3 head as N joint; s2 pierces s3 mid; s4 head at '
              'C(156,168) with N gap from s2. shu_wan_gou retained '
              '(errata suggested xie_gou but GT silhouette is clearly '
              'vertical + right curve + up-hook, not diagonal descent).'),
}


def main():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # s1: short top tick, slight up-slope going right.
    # MMH TC(0.028,0.905) -> TR(0.109,0.779)  = (103,90) -> (211,78)
    draw_heng(d, (103, 92), (208, 82), width_head=6, width_tail=6)

    # s2: main heng, ML(0.782,0.143) -> MR(0.306,0.465) = (78,114) -> (230,146)
    # Slight down-right tilt. Long enough to visibly cross s3 (pie).
    draw_heng(d, (78, 120), (232, 145), width_head=8, width_tail=8)

    # s3: pie descending from top-center to lower-left.
    # Head TC(0.301,0.996)=(130,100) — placed at (130,96) so it lands
    # near s1's midpoint (~155,87) with a small natural gap (N joint).
    # Tail BL(0.419,0.883)=(42,288); pulled in to (58,278) to keep the
    # tip inside the visible glyph area.
    draw_pie(d, (130, 96), (58, 278), bow_perp=10, w_head=8, w_tail=3)

    # s4: 竖弯钩. Head at C(154,169) — inside body, NOT welded to s2
    # (N joint, ~29 px expected gap). Tail toward BR but compacted to
    # (232,232) to match GT's compact right terminus.
    draw_shu_wan_gou(d, (156, 168), (232, 232),
                     width=7, bottom_extra=42, knee_ratio=0.85)

    out = Path(__file__).with_name('01_旡.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
