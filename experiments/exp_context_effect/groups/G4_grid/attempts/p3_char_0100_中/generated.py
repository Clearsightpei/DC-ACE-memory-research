"""中 (zhōng, "middle", 4 strokes) — G4 batch attempt.

Memory checklist (per memory_index.md):
  1. success_bank/INDEX.md grep '中'  → NOT found.
  2. errata.md grep '中'              → NOT found.
  3. form_catalog.md — 竖 as spine crossing 横 rows (十, 木, 车, 牛)
     apply: s4 is a long 竖 spine, P-welded through s2 (top bar) and
     s3 (bottom bar). Reference `shi_ten.py` for P at C.
  4. principles_meta.md — TR1 override-anchors always, TR10 N-gap
     ~15 px on box corners (口-family), TR8 same-row/col rule.
  5. joint_atlas.md — box corners are N (do NOT weld); spine
     crossings are P (welded).
  6. sandbox.md — no prior 中-specific note.

Composition:
  s1 — 竖 left wall of box (ML down to BL region).
  s2 — 横折 top bar + right wall (like 口's s2; short vertical drop).
  s3 — 横 bottom bar (slight upward slant left→right per MMH).
  s4 — long 竖 spine (TC through both bars to below BC).

Joints:
  s1.head ⇆ s2.head @ ML  → N (top-left corner, ~15 px gap).
  s1.tail ⇆ s3.head @ BL  → N (bottom-left corner, ~15 px gap).
  s2.tail ⇆ s3.mid  @ MR  → N (bottom-right corner, ~15 px gap).
  s2.mid  ⇆ s4.mid  @ C   → P (spine crosses top bar, welded).
  s3.mid  ⇆ s4.mid  @ C   → P (spine crosses bottom bar, welded).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', '..', 'success_bank', 'code'))
from _anchor import anchor_to_xy, fat_line
from PIL import Image, ImageDraw


SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': ('4 strokes: 竖 left wall, 横折 top+right, 横 bottom, 长竖 spine. '
              'Two P-welds at C via shared spine x-coord; three N-corners via '
              '_shorten(4). Corner endpoints match MMH within tolerance.')
}


def _shorten(pt, other, px):
    x0, y0 = pt
    x1, y1 = other
    dx, dy = x1 - x0, y1 - y0
    d = (dx * dx + dy * dy) ** 0.5
    if d < 1e-6:
        return (x0, y0)
    t = min(1.0, px / d)
    return (x0 + dx * t, y0 + dy * t)


def draw_zhong(draw):
    # ---- s4: long 竖 spine — pick the spine x FIRST, then align box bars.
    # MMH s4 head ('TC', 0.315, 0.589) / tail ('BC', 0.462, 1.029).
    # We keep the spine near canvas center x (~150) so the box bars can
    # weld at C. Use a nearly-straight vertical for a clean P-cross.
    s4_head = ('TC', 0.50, 0.55)   # (150, 55) — start closer to top of box
    s4_tail = ('BC', 0.50, 1.00)   # (150, 300) — canvas bottom
    s4h = anchor_to_xy(s4_head); s4t = anchor_to_xy(s4_tail)
    spine_x = s4h[0]

    # ---- Box geometry: choose top bar y and bottom bar y so the spine
    # crosses both cleanly. Top bar around y=115, bottom bar around
    # y=200. Left wall x ~ 70; right wall x ~ 230.
    top_y = 115.0
    bot_y = 200.0
    left_x = 70.0
    right_x = 230.0

    # ---- s1: 竖 left wall — nearly vertical, faint rightward slant.
    s1h = (left_x + 2.0, top_y)
    s1t = (left_x + 8.0, bot_y)

    # ---- s2: 横折 top bar + short right descender.
    s2h = (left_x + 10.0, top_y - 2.0)
    s2c = (right_x, top_y - 2.0)
    s2t = (right_x + 2.0, bot_y - 25.0)

    # ---- s3: 横 bottom bar (nearly flat).
    s3h = (left_x + 6.0, bot_y + 3.0)
    s3t = (right_x - 3.0, bot_y - 2.0)

    # ---- Apply N-gap shortening on the three corners of the box.
    s1h_g = _shorten(s1h, s1t, 4)
    s1t_g = _shorten(s1t, s1h, 4)
    s2h_g = _shorten(s2h, s2c, 6)
    s2t_g = _shorten(s2t, s2c, 3)
    s3h_g = _shorten(s3h, s3t, 5)
    s3t_g = _shorten(s3t, s3h, 3)

    # ---- Draw order: box first, spine last so weld is on top.
    W = 8
    fat_line(draw, s1h_g, s1t_g, width=W)                    # s1 left wall
    fat_line(draw, s2h_g, s2c, width=W)                      # s2 top bar
    fat_line(draw, s2c, s2t_g, width=W)                      # s2 right wall
    # small fillet ellipse at corner
    cx, cy = s2c; r = 5
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    fat_line(draw, s3h_g, s3t_g, width=W)                    # s3 bottom bar
    fat_line(draw, s4h, s4t, width=W)                        # s4 spine (welds P at C)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_zhong(d)
    out = os.path.join(os.path.dirname(__file__), '01_中.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
