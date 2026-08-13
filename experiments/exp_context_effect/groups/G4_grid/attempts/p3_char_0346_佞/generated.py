"""p3_char_0346_佞 — G4 attempt.

Decomposition: 佞 = 亻 (left, 2 strokes) + 二 (top-right, 2 strokes) +
女-like (bottom-right, 3 strokes: 捺 + 撇 + 横 per MMH anchors) = 7 strokes.

Memory reads (per memory_index.md v8 slim checklist):
  1. drawer_memory.md — no chronic primitive fires (佞 has no 丿/刀/冂/弓/马
     as a dominant part beyond 亻); high-value shortlist: 亻 (ren_side)
     applies. No chronic import required.
  2. success_bank/INDEX.md — no entry for 佞; components present: ren_side,
     er, nv. Using ren_side directly. NOT calling er/nv wholesale because
     they assume full-canvas anchors; MMH gives us in-position anchors
     for this composition — using per-stroke primitives at MMH anchors
     is a cleaner fit.
  3. errata.md — 佞 not listed.

MMH structural expectation: 7 strokes; MMH decomposes the 女-like right-
bottom as three straight strokes (down-right 捺, down-left 撇, horizontal
横) welded at BC. Trusting MMH anchors verbatim (v9 lesson from 比: MMH
verbatim beats hand-tune for cross-stroke topology).
"""
import os, sys
_BANK = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G4_grid/success_bank/code"
sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw
from _anchor import anchor_to_xy, fat_line
from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from na import draw_na

# --- SELF_CHECK (filled in after render; see notes at bottom) ---
SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '7 strokes: 亻(pie+shu), 二(heng+heng), 女-like(na+pie+heng). '
             'MMH anchors used verbatim. All 3 N joints are natural gaps; '
             '3 P/T joints at s5/s6/s7 crossings emerge from anchor geometry.'
}


def draw_ninh(draw):
    # 亻 (s1: 撇, s2: 竖) — MMH anchors verbatim, T-joint at s2.head touching s1 body
    draw_pie(draw, ('TL', 0.94, 0.703), ('BL', 0.173, 0.042),
             head_width=11, tail_width=1, curve=0.09)
    draw_shu(draw, ('ML', 0.7, 0.567), ('BL', 0.744, 0.953), width=9)

    # 二 (s3: top 横, s4: bottom 横) — near-horizontal, top slightly shorter
    draw_heng(draw, ('C', 0.354, 0.017), ('TR', 0.145, 0.949), width=8)
    draw_heng(draw, ('C', 0.172, 0.453), ('MR', 0.37, 0.365), width=9)

    # 女-like (s5: 捺 down-right, s6: 撇 down-left, s7: 横 across)
    # s5 & s6 cross at BC (P), s5 & s7 cross at BC (P), s6.head touches s7 (T)
    draw_na(draw, ('C', 0.57, 0.652), ('BR', 0.347, 0.988),
            head_width=3, peak_width=11, tail_width=1, peak_t=0.85, curve=0.08)
    draw_pie(draw, ('C', 0.893, 0.846), ('BC', 0.107, 0.93),
             head_width=10, tail_width=1, curve=0.08)
    draw_heng(draw, ('BL', 0.967, 0.048), ('MR', 0.66, 0.963), width=8)


if __name__ == '__main__':
    img = Image.new('RGB', (300, 300), 'white')
    d = ImageDraw.Draw(img)
    draw_ninh(d)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '01_佞.png')
    img.save(out)
    print('wrote', out)
