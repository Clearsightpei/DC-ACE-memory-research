"""p3_char_0542_痉 — 疒 (sickness top-left frame) + 圣 (interior: 又 top + 土 bottom).

Reading log (memory_index.md v8 checklist):
  1. drawer_memory.md — named pattern `ne_sick_top_left_frame_for_*` (B13 codified).
     5-stroke frame inlined via base primitives + MMH-verbatim endpoints (no chronic).
     Interior 圣 = 又 (s6+s7 pie+na) + 土 (s8+s9+s10 heng+shu+heng).
     Follow A-recipe: explicit decomposition, MMH-verbatim, SELF_CHECK, base primitives,
     N-joint gaps preserved (all 8 joints are N per brief).
  2. INDEX/success_bank grep 痉 — not present. Grep 圣 — not present. Grep 又/土 —
     you_again.py and tu.py exist but full-canvas default; interior 圣 is compressed
     into bottom-right slot (roughly x∈[0.20, 0.95], y∈[0.35, 1.00]). BANK_DEVIATION.
  3. errata.md grep 痉 — not present.

Expected 10 strokes (from MMH-injected block):
  s1 : TC(.468,.548) -> TC(.811,.776)   top dot of 疒 (点)
  s2 : C (.096,.063) -> TR(.306,.955)   top short heng (亠 top piece)
  s3 : ML(.873,.005) -> BL(.240,.962)   long 撇 sweep (left frame)
  s4 : ML(.434,.310) -> ML(.665,.562)   inner upper dot (点)
  s5 : BL(.188,.206) -> ML(.858,.904)   inner lower rising 提 (ti)
  s6 : C (.230,.403) -> BC(.154,.112)   又's pie (short, nearly vertical)
  s7 : C (.793,.761) -> BR(.338,.077)   又's na (right-falling)
  s8 : BC(.216,.218) -> BR(.130,.147)   土's top 横 (heng)
  s9 : BC(.605,.285) -> BC(.600,.748)   土's central 竖 (shu)
  s10: BL(.861,.880) -> BR(.587,.854)   土's bottom 横 (wide)

Joints (all 8 declared N-class → preserve small natural gaps, DO NOT weld):
  s2.head ⇆ s3.head @ C          ~17 px (top-heng meets 撇 head)
  s3.mid  ⇆ s5.tail @ ML         ~9  px (撇 body vs inner-ti tail)
  s3.mid  ⇆ s6.head @ C          ~34 px (撇 body vs interior 又 start)
  s6.mid  ⇆ s7.head @ C          ~16 px (又 pie mid vs na head)
  s6.tail ⇆ s8.head @ BC         ~17 px (pie tail vs 土 top-heng head)
  s7.mid  ⇆ s8.tail @ BR         ~30 px (na body vs top-heng tail)
  s8.mid  ⇆ s9.head @ BC         ~12 px (top-heng mid vs 竖 head)
  s9.tail ⇆ s10.mid @ BC         ~17 px (竖 tail vs bottom-heng mid)
"""

# BANK_DEVIATION
# skipped: you_again.py, tu.py
# reason: interior 圣 is compressed into 疒's bottom-right slot (x~[.20,.95] y~[.35,1.0]);
#         you_again / tu bake full-canvas defaults and would overrun the frame.
# fresh_component: sheng_interior_for_ne_sick (又 top + 土 bottom compressed under 疒)

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 primitives, one per MMH stroke
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 5-stroke frame (named pattern) + 圣 = 又+土 inline. All 8 joints N-class (small gaps, no welds).',
}

from PIL import Image, ImageDraw
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.abspath(os.path.join(HERE, '..', '..', 'success_bank', 'code'))
sys.path.insert(0, BANK)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402


def draw():
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)

    # ============ 疒 FRAME (strokes 1-5) — draw s1 (top dot) LAST defensively ============

    # s2 — top short heng (亠 top bar; slight rise / arc)
    h = anchor_to_xy(('C', 0.096, 0.063))
    t = anchor_to_xy(('TR', 0.306, 0.955))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 3)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [4] * len(pts)
    stroke_variable_width(d, pts, widths)

    # s3 — long 撇 sweep (left frame of 疒), tapered
    h = anchor_to_xy(('ML', 0.873, 0.005))
    t = anchor_to_xy(('BL', 0.240, 0.962))
    ctrl = (h[0] - 18, h[1] + (t[1] - h[1]) * 0.72)
    pts = quad_bezier(h, ctrl, t, n=60)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        widths.append(3 + 4 * (1 - abs(2 * u - 1)))  # bulge in middle
    stroke_variable_width(d, pts, widths)

    # s4 — inner upper dot (short thick pie)
    h = anchor_to_xy(('ML', 0.434, 0.310))
    t = anchor_to_xy(('ML', 0.665, 0.562))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2 - 2, (h[1] + t[1]) / 2), t, n=20)
    widths = [3 + 4 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s5 — inner rising 提 (ti)
    h = anchor_to_xy(('BL', 0.188, 0.206))
    t = anchor_to_xy(('ML', 0.858, 0.904))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 4)
    pts = quad_bezier(h, mid, t, n=25)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ============ 圣 INTERIOR — 又 (s6+s7) + 土 (s8+s9+s10) ============

    # s6 — 又's pie: short, nearly vertical, slight left-lean
    h = anchor_to_xy(('C', 0.230, 0.403))
    t = anchor_to_xy(('BC', 0.154, 0.112))
    ctrl = ((h[0] + t[0]) / 2 - 4, (h[1] + t[1]) / 2)
    pts = quad_bezier(h, ctrl, t, n=25)
    widths = [5 - 3 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s7 — 又's na (right-falling, bulge)
    h = anchor_to_xy(('C', 0.793, 0.761))
    t = anchor_to_xy(('BR', 0.338, 0.077))
    ctrl = ((h[0] + t[0]) / 2 + 4, (h[1] + t[1]) / 2 + 6)
    pts = quad_bezier(h, ctrl, t, n=30)
    widths = []
    n = len(pts)
    for i in range(n):
        u = i / (n - 1)
        # thin head, bulge near 0.75, taper to thin tail
        widths.append(3 + 8 * (u ** 1.5) * (1 - u * 0.4))
    stroke_variable_width(d, pts, widths)

    # s8 — 土's top 横 (short, nearly flat, tiny upward)
    h = anchor_to_xy(('BC', 0.216, 0.218))
    t = anchor_to_xy(('BR', 0.130, 0.147))
    fat_line(d, h, t, 5)

    # s9 — 土's central 竖 (vertical)
    h = anchor_to_xy(('BC', 0.605, 0.285))
    t = anchor_to_xy(('BC', 0.600, 0.748))
    fat_line(d, h, t, 5)

    # s10 — 土's bottom 横 (wide, spans across bottom)
    h = anchor_to_xy(('BL', 0.861, 0.880))
    t = anchor_to_xy(('BR', 0.587, 0.854))
    fat_line(d, h, t, 6)

    # s1 — 疒 top dot LAST (defensive per B6 rule for top-dot items)
    h = anchor_to_xy(('TC', 0.468, 0.548))
    t = anchor_to_xy(('TC', 0.811, 0.776))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 3), t, n=20)
    widths = [3 + 5 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    out = os.path.join(HERE, '01_痉.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
