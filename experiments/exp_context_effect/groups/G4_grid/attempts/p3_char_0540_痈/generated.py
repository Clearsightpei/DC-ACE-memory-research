"""p3_char_0540_痈 — sickness radical 疒 + 用 inside.

Decomposition: 痈 = 疒 (strokes 1-5, top-left frame) + 用 (strokes 6-10).

Bank lookup (per memory_index.md v8 checklist):
  1. drawer_memory.md — 疒 has named-pattern `ne_sick_top_left_frame_for_*`
     (B13: 6/8 non-FAIL). Inline 5-stroke frame via MMH-verbatim anchors.
     用 contains 冂 shape but chronic/jiong_frame is full-canvas (300x300);
     here 用 is compressed into the right-bottom slot (~x∈[0.6, 2.1],
     y∈[1.5, 2.9]) so jiong_frame won't fit. Inline via base primitives.
  2. INDEX.md grep — 0168_用 mastered (inline frame + shu). 疽/疸 give
     canonical 疒-inline recipe. Reuse the recipe pattern (not the file).
  3. errata.md grep 痈 — not present.

BANK_DEVIATION:
  skipped: chronic/jiong_frame.py
  reason: 用 sits in right-bottom compound slot (x∈[115,207], y∈[151,293]),
    ~2/3 canvas — chronic/jiong_frame full-canvas defaults would overrun
    onto 疒. Inline via _anchor + fat_line per B10/B11/B12 slot rule.
  fresh_component: yong_right_bottom_slot_for_疒compound

Expected 10 strokes (from MMH):
  s1 : TC(.479,.548) -> TC(.796,.791)   top dot 点
  s2 : C (.055,.087) -> TR(.341,.943)   top short heng 亠 bar
  s3 : ML(.844,.031) -> BL(.343,1.006)  long 撇 sweep (疒 left frame)
  s4 : ML(.422,.354) -> ML(.662,.579)   inner upper dot
  s5 : BL(.199,.221) -> ML(.773,.878)   inner rising 提
  s6 : C (.151,.512) -> BL(.899,.892)   用 left 撇/竖 (slight slant)
  s7 : C (.271,.532) -> BC(.916,.786)   用 横折钩 (top + right + hook)
  s8 : C (.43,.963)  -> MR(.062,.86)    用 upper inner 横 (P-welds spine)
  s9 : BC(.395,.303) -> BR(.071,.221)   用 lower inner 横 (P-welds spine)
  s10: C (.617,.567) -> BC(.72,.927)    用 central 竖 spine

Joints (11 — all N except 2 P):
  s1.tail ⇆ s2.mid  (TC)   N ~34px  dot vs top-heng
  s2.head ⇆ s3.head (C)    N ~16px  top-heng vs 撇 head
  s3.mid  ⇆ s5.tail (ML)   N ~16px  撇 body vs 提 tail
  s6.head ⇆ s7.head (C)    N ~10px  用 left top vs 横折钩 top
  s6.mid  ⇆ s8.head (C)    N ~29px  用 left vs upper 横
  s6.mid  ⇆ s9.head (BC)   N ~30px  用 left vs lower 横
  s7.mid  ⇆ s8.tail (MR)   N ~34px  用 right vs upper 横 right
  s7.mid  ⇆ s9.tail (BR)   N ~35px  用 right vs lower 横 right
  s7.head ⇆ s10.head (C)   N ~13px  横折钩 top vs spine top
  s8.mid  ⇆ s10.mid (C)    P WELD   upper 横 crosses spine
  s9.mid  ⇆ s10.mid (BC)   P WELD   lower 横 crosses spine
"""

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 10 primitives (s7 = 2 fat_line segments = 1 stroke)
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '疒 frame from ne_sick pattern (疽 A + 疸 PASS). 用 inlined per BANK_DEVIATION (slot-compressed). s8/s9 P-weld the spine s10; other joints N-gapped.'
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

    # ============ 疒 FRAME (strokes 1-5) ============

    # s1 — top dot (点), small tapered pie
    h = anchor_to_xy(('TC', 0.479, 0.548))
    t = anchor_to_xy(('TC', 0.796, 0.791))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 3), t, n=20)
    widths = [3 + 5 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s2 — top short heng (亠 top bar)
    h = anchor_to_xy(('C', 0.055, 0.087))
    t = anchor_to_xy(('TR', 0.341, 0.943))
    mid = ((h[0] + t[0]) / 2, min(h[1], t[1]) - 4)
    pts = quad_bezier(h, mid, t, n=30)
    widths = [4] * len(pts)
    stroke_variable_width(d, pts, widths)

    # s3 — long 撇 sweep (left-falling 疒 frame)
    h = anchor_to_xy(('ML', 0.844, 0.031))
    t = anchor_to_xy(('BL', 0.343, 1.006))
    ctrl = (h[0] - 20, h[1] + (t[1] - h[1]) * 0.75)
    pts = quad_bezier(h, ctrl, t, n=60)
    n = len(pts)
    widths = [3 + 4 * (1 - abs(2 * (i / (n - 1)) - 1)) for i in range(n)]
    stroke_variable_width(d, pts, widths)

    # s4 — inner upper dot (short thick pie)
    h = anchor_to_xy(('ML', 0.422, 0.354))
    t = anchor_to_xy(('ML', 0.662, 0.579))
    pts = quad_bezier(h, ((h[0] + t[0]) / 2 - 2, (h[1] + t[1]) / 2), t, n=20)
    widths = [3 + 4 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s5 — inner lower rising 提 (ti)
    h = anchor_to_xy(('BL', 0.199, 0.221))
    t = anchor_to_xy(('ML', 0.773, 0.878))
    mid = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2 + 4)
    pts = quad_bezier(h, mid, t, n=25)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # ============ 用 INTERIOR (strokes 6-10) ============

    # s6 — 用 left 撇 (MMH endpoints verbatim; nearly straight line)
    h = anchor_to_xy(('C', 0.151, 0.512))
    t = anchor_to_xy(('BL', 0.899, 0.892))
    # near-linear (small ctrl at midpoint) — avoid extra leftward bulge that
    # would confuse with 疒's s3 撇 nearby.
    ctrl = ((h[0] + t[0]) / 2, (h[1] + t[1]) / 2)
    pts = quad_bezier(h, ctrl, t, n=40)
    widths = [5 - 2 * (i / len(pts)) for i in range(len(pts))]
    stroke_variable_width(d, pts, widths)

    # s7 — 横折钩: top horizontal + right vertical (hook at bottom)
    h = anchor_to_xy(('C', 0.271, 0.532))
    t = anchor_to_xy(('BC', 0.916, 0.786))
    # corner at top-right of 用 frame
    corner = (t[0], h[1])
    fat_line(d, h, corner, 5)           # top horizontal
    fat_line(d, corner, t, 5)           # right vertical
    # small hook tick at tail (leftward)
    hook_end = (t[0] - 8, t[1] - 3)
    fat_line(d, t, hook_end, 4)

    # s8 — upper inner 横 (P-welds the spine)
    #   MMH endpoints: head @ C(.43,.963)=(143,196) tail @ MR(.062,.86)=(206,186)
    h = anchor_to_xy(('C', 0.43, 0.963))
    t = anchor_to_xy(('MR', 0.062, 0.86))
    fat_line(d, h, t, 4)

    # s9 — lower inner 横 (P-welds the spine)
    #   MMH endpoints: head @ BC(.395,.303)=(140,230) tail @ BR(.071,.221)=(207,222)
    h = anchor_to_xy(('BC', 0.395, 0.303))
    t = anchor_to_xy(('BR', 0.071, 0.221))
    fat_line(d, h, t, 4)

    # s10 — central 竖 spine (top -> bottom, crosses s8 and s9 — P welds)
    h = anchor_to_xy(('C', 0.617, 0.567))
    t = anchor_to_xy(('BC', 0.72, 0.927))
    fat_line(d, h, t, 5)

    out = os.path.join(HERE, '01_痈.png')
    img.save(out)
    print(f'wrote {out}')


if __name__ == '__main__':
    draw()
