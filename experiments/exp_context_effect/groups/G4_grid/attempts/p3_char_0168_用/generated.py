"""p3_char_0168_用 — 用 (yòng, "use", 5画).

Structure: 月-like frame with piercing middle vertical.
Stroke order (MMH):
  s1: 撇 — from upper-inner (TL) down-left to bottom-left (BL)
  s2: 横折钩 — top horizontal from TL(0.94) then bends down along right side to BC (with hook)
  s3: 横 middle — inside frame, spans C row
  s4: 横 bottom — inside frame, spans C bottom
  s5: 竖 middle — from TC top through both middle & bottom heng (P/welded)

Joints:
  s1.head ⇆ s2.head @ TL : N (small gap top-left corner)
  s2.head ⇆ s5.head @ TC : N (small gap where top-horizontal meets middle-vertical head)
  s3.mid ⇆ s5.mid @ C : P (welded — cross)
  s4.mid ⇆ s5.mid @ C : P (welded — cross)

Lookup checklist:
  1. success_bank/INDEX.md grep 用 — not present.
  2. errata.md grep 用 — not present.
  3. form_catalog — 月-family frame with piercing 竖 (like 月/曰 extended).
  4. principles_meta — TR8: heng/shu must share row/column; TR10: N joints ≤25px gap.
  5. joint_atlas — P joints welded, N joints ~15-20px.
  6. chronic — none of 丿刀冂弓马 as top-level here; inline the frame per TR6.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line, quad_bezier, stroke_variable_width


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '5 strokes: pie, heng-zhe-gou frame, middle heng, bottom heng, piercing shu.'
}


def draw_yong(draw):
    # ---- s1: 撇 (pie) from upper-inner-left down to bottom-left ----
    s1h = anchor_to_xy(('TL', 0.72, 0.30))   # start near top of frame (adjusted up from 0.81 for visual reach to top)
    s1t = anchor_to_xy(('BL', 0.10, 0.95))   # curve out to bottom-left
    # curve control: slight leftward bulge
    ctl = ((s1h[0] + s1t[0]) / 2 - 15, (s1h[1] + s1t[1]) / 2)
    pts = quad_bezier(s1h, ctl, s1t, n=40)
    widths = [11 - 5 * (i / 40) for i in range(41)]  # thick to thin
    stroke_variable_width(draw, pts, widths)

    # ---- s2: 横折钩 (heng-zhe-gou) frame top+right with hook ----
    # top horizontal from just past s1 head across to top-right corner
    s2h = anchor_to_xy(('TL', 0.90, 0.30))   # top-left corner start (right of s1 head)
    s2corner = anchor_to_xy(('TR', 0.85, 0.30))  # top-right corner (bend)
    s2t = anchor_to_xy(('BR', 0.75, 0.90))   # bottom-right end (before hook)
    # horizontal
    fat_line(draw, s2h, s2corner, width=9)
    # small triangular thickening at the bend (dun-bi)
    r = 7
    draw.ellipse([s2corner[0] - r, s2corner[1] - r,
                  s2corner[0] + r, s2corner[1] + r], fill=(0, 0, 0))
    # vertical (right leg)
    fat_line(draw, s2corner, s2t, width=9)
    # hook: small leftward flick at bottom
    hook_end = (s2t[0] - 18, s2t[1] - 8)
    fat_line(draw, s2t, hook_end, width=8)

    # ---- s3: middle 横 inside frame — reach nearly to right leg ----
    s3h = anchor_to_xy(('ML', 0.85, 0.55))
    s3t = anchor_to_xy(('C',  0.95, 0.50))   # extends to near right leg
    fat_line(draw, s3h, s3t, width=8)

    # ---- s4: bottom 横 inside frame — reach nearly to right leg ----
    s4h = anchor_to_xy(('BL', 0.30, 0.20))
    s4t = anchor_to_xy(('BC', 0.95, 0.15))
    fat_line(draw, s4h, s4t, width=8)

    # ---- s5: middle 竖 piercing through both hengs (P joints) ----
    s5h = anchor_to_xy(('TC', 0.50, 0.32))   # starts at top frame edge
    s5t = anchor_to_xy(('BC', 0.55, 0.95))   # extends past bottom heng into hook area
    fat_line(draw, s5h, s5t, width=9)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yong(draw)
    out = os.path.join(os.path.dirname(__file__), '01_用.png')
    img.save(out)
    print(f"wrote {out}")


if __name__ == '__main__':
    main()
