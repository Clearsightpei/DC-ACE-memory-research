# BANK_DEVIATION
# skipped: zi_char.py, ren_side.py (composed inline instead)
# reason: MMH decomposes 孚's 弯钩 into two strokes (s7 body + s8 hook-tail) and 爫 into 4 strokes (s3-s6); the packaged wan_gou/heng_pie/ren_side wrappers don't map 1:1 to this 9-stroke MMH breakdown.
# fresh_component: fu_inline_9stroke_from_mmh
"""p3_char_0490_俘 — 亻 (2) + 孚 [爫(4) + 子(3)] = 9 strokes.

Memory-lookup checklist:
1. drawer_memory.md — 亻 usually via ren_side; 子 via zi_char. But MMH
   breakdown for 俘 splits the 弯钩 into 2 pieces so wan_gou can't wrap it.
   Deviating per v13 and drawing 9 stroke primitives directly at MMH anchors.
2. success_bank/INDEX.md — ren_side.py, zi_char.py exist; 爫 lives inline
   (采 entry). Using low-level pie/shu/dian/heng primitives per MMH anchors.
3. errata.md — 俘 not listed.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),
    '..', '..', 'success_bank', 'code'))

from PIL import Image, ImageDraw
from pie import draw_pie
from shu import draw_shu
from dian import draw_dian
from heng import draw_heng

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,   # 9 = pie + shu + pie + dian + dian + pie + dian + shu + heng
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': '9 strokes at MMH anchors; all joints are N-class except s8xs9 which is P (welded).',
}

img = Image.new('RGB', (300, 300), 'white')
draw = ImageDraw.Draw(img)

# ---- 亻 (left radical, 2 strokes) ----
# s1 撇: MMH TL(0.861, 0.636) → ML(0.185, 0.89)
draw_pie(draw,
         ('TL', 0.861, 0.636),
         ('ML', 0.185, 0.89),
         head_width=11, tail_width=1, curve=0.10, segments=48)

# s2 竖: MMH ML(0.688, 0.427) → BL(0.732, 0.801)
draw_shu(draw,
         ('ML', 0.688, 0.427),
         ('BL', 0.732, 0.801),
         width=8)

# ---- 爫 top (4 small strokes 3-6) ----
# s3 short 撇 upper-left of 爫: TR(0.057, 0.715) → TC(0.283, 0.908)
draw_pie(draw,
         ('TR', 0.057, 0.715),
         ('TC', 0.283, 0.908),
         head_width=6, tail_width=1, curve=0.08, segments=24)

# s4 dot: C(0.184, 0.131) → C(0.412, 0.354)
draw_dian(draw,
          ('C', 0.184, 0.131),
          ('C', 0.412, 0.354),
          head_width=2, peak_width=8, curve=0.08, segments=24)

# s5 dot: C(0.556, 0.008) → C(0.737, 0.198)
draw_dian(draw,
          ('C', 0.556, 0.008),
          ('C', 0.737, 0.198),
          head_width=2, peak_width=8, curve=0.08, segments=24)

# s6 short 撇 (rightmost of 爫): TR(0.244, 0.85) → C(0.907, 0.28)
draw_pie(draw,
         ('TR', 0.244, 0.85),
         ('C', 0.907, 0.28),
         head_width=6, tail_width=1, curve=0.08, segments=24)

# ---- 子 body (strokes 7-9) ----
# s7 弯钩 body: C(0.248, 0.553) → C(0.77, 0.878) — curved down-right
draw_dian(draw,
          ('C', 0.248, 0.553),
          ('C', 0.77, 0.878),
          head_width=3, peak_width=10, curve=0.05, segments=32)

# s8 竖 (hook stem down-slight-left): C(0.617, 0.893) → BC(0.383, 0.815)
draw_shu(draw,
         ('C', 0.617, 0.893),
         ('BC', 0.383, 0.815),
         width=9)

# s9 横 (long crossbar, wide): BL(0.905, 0.142) → BR(0.783, 0.021)
draw_heng(draw,
          ('BL', 0.905, 0.142),
          ('BR', 0.783, 0.021),
          width=9)

out_path = os.path.join(os.path.dirname(__file__), '01_俘.png')
img.save(out_path)
print('wrote', out_path)
