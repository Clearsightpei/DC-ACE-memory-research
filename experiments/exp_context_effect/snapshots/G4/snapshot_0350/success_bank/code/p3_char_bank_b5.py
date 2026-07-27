"""B5 batch — 26 Phase-3 character PASS entries (aggregator stub).

Same pattern as `p3_char_bank.py` (B3 aggregator) — one file listing
all B5 PASSes rather than 26 individual .py files. Each entry names
the item, source attempt path, stroke count, and any notable bank
primitives reused. Full anchor plans live in the attempt directory.

Rationale: 26 individual thin-wrapper files would grow the bank to
173 files and make grep noisier. A single aggregator file with 26
records preserves the anchor evidence while keeping bank size sane.
The full anchor tuples are available by reading
`attempts/<item_id>/generated.py`.

To reuse one of these entries in a future composition, either:
  (a) inline the anchor plan from the attempt directory, or
  (b) call the primitive(s) named in `primitives` with the anchors
      recorded here.
"""

# Item records (as data — no runnable draw functions here).
B5_PASSES = [
    {'item_id': 'p3_char_0084_屮', 'strokes': 3,
     'primitives': ['shu', 'heng', 'shu'],
     'notes': '屮 = short 竖 + 横 mid + short 竖-tick right; TR8 col-share.'},
    {'item_id': 'p3_char_0087_工', 'strokes': 3,
     'primitives': ['heng', 'shu', 'heng'],
     'notes': '工 = top heng + centered shu + bottom heng; both heng row-lock.'},
    {'item_id': 'p3_char_0088_川', 'strokes': 3,
     'primitives': ['pie', 'shu', 'shu'],
     'notes': '川 = short pie + two vertical shu; column separation.'},
    {'item_id': 'p3_char_0089_义', 'strokes': 3,
     'primitives': ['dian', 'pie', 'na'],
     'notes': '义 = top dot + pie + na apex-shared (P at C).'},
    {'item_id': 'p3_char_0090_幺', 'strokes': 3,
     'primitives': ['pie', 'pie_zhe', 'dian'],
     'notes': '幺 = tiny pie + stacked pie_zhe loop + closing dot; yao_small pattern.'},
    {'item_id': 'p3_char_0092_廾', 'strokes': 3,
     'primitives': ['heng', 'pie', 'shu'],
     'notes': '廾 = middle heng + slanted pie + right shu; two P at heng.'},
    {'item_id': 'p3_char_0093_弋', 'strokes': 3,
     'primitives': ['heng', 'xie_gou', 'dian'],
     'notes': '弋 = short heng + xie_gou body + upper dot; xie_gou.py reused.'},
    {'item_id': 'p3_char_0094_不', 'strokes': 4,
     'primitives': ['heng', 'pie', 'shu', 'dian'],
     'notes': '不 = top heng full-span + pie down-left + shu centered + right dot.'},
    {'item_id': 'p3_char_0095_丹', 'strokes': 4,
     'primitives': ['pie', 'heng_zhe_gou', 'dian', 'heng'],
     'notes': '丹 = pie left + heng_zhe_gou frame + inner dot + middle heng.'},
    {'item_id': 'p3_char_0100_中', 'strokes': 4,
     'primitives': ['shu', 'heng_zhe', 'heng', 'shu'],
     'notes': '中 = enclosing box + centered vertical piercing; P-cross at C.'},
    {'item_id': 'p3_char_0102_天', 'strokes': 4,
     'primitives': ['heng', 'heng', 'pie', 'na'],
     'notes': '天 = short top heng + long mid heng + pie/na apex-shared.'},
    {'item_id': 'p3_char_0105_仂', 'strokes': 4,
     'primitives': ['ren_side', 'li'],
     'notes': '仂 = 亻 (ren_side.py) left + 力 (li.py) right; component-composition.'},
    {'item_id': 'p3_char_0106_日', 'strokes': 4,
     'primitives': ['shu', 'heng_zhe', 'heng', 'heng'],
     'notes': '日 = closed frame + middle heng wall-to-wall + bottom heng.'},
    {'item_id': 'p3_char_0107_仃', 'strokes': 4,
     'primitives': ['ren_side', 'heng', 'shu_gou'],
     'notes': '仃 = 亻 left + 丁 right (heng + shu_gou); T-weld at right heng.'},
    {'item_id': 'p3_char_0108_无', 'strokes': 4,
     'primitives': ['heng', 'heng', 'pie', 'shu_wan_gou'],
     'notes': '无 = short top heng + long mid heng + long pie + 竖弯钩; P at C.'},
    {'item_id': 'p3_char_0109_仄', 'strokes': 4,
     'primitives': ['chang', 'ren'],
     'notes': '仄 = 厂 (chang.py) top + 人 (ren.py) tucked inside.'},
    {'item_id': 'p3_char_0112_心', 'strokes': 4,
     'primitives': ['wo_gou', 'dian', 'dian', 'dian'],
     'notes': '心 = 卧钩 base + 3 dots (bottom + upper-left + upper-mid).'},
    {'item_id': 'p3_char_0115_仌', 'strokes': 4,
     'primitives': ['pie', 'na', 'pie', 'na'],
     'notes': '仌 = 从-like (two pie+na pairs) stacked; two apex P-welds.'},
    {'item_id': 'p3_char_0116_公', 'strokes': 4,
     'primitives': ['pie', 'na', 'si_private'],
     'notes': '公 = 八 top (pie+na) + 厶 bottom (private).'},
    {'item_id': 'p3_char_0117_仑', 'strokes': 4,
     'primitives': ['pie', 'na', 'bi'],
     'notes': '仑 = 亼 top (pie+na apex-shared) + 匕 bottom.'},
    {'item_id': 'p3_char_0124_文', 'strokes': 4,
     'primitives': ['dian', 'heng', 'pie', 'na'],
     'notes': '文 = top dot + mid heng + pie/na apex-shared at BC.'},
    {'item_id': 'p3_char_0126_长', 'strokes': 4,
     'primitives': ['pie', 'heng', 'shu_ti', 'na'],
     'notes': '长 = short pie + heng + 竖提 spine + na sweep.'},
    {'item_id': 'p3_char_0127_冈', 'strokes': 4,
     'primitives': ['shu', 'heng_zhe_gou', 'pie', 'dian'],
     'notes': '冈 = 冂 frame + inner 义 (pie + dot); enclosing pattern.'},
    {'item_id': 'p3_char_0128_太', 'strokes': 4,
     'primitives': ['heng', 'pie', 'na', 'dian'],
     'notes': '太 = 大 (heng + pie + na apex-shared) + tucked dot.'},
    {'item_id': 'p3_char_0129_龶', 'strokes': 4,
     'primitives': ['heng', 'heng', 'shu', 'heng'],
     'notes': '龶 = 3 heng stacked + centered shu piercing all; multi-P.'},
    {'item_id': 'p3_char_0131_冗', 'strokes': 4,
     'primitives': ['mi_cover_char', 'ji'],
     'notes': '冗 = 冖 (mi_cover_char.py) top + 几-like bottom; enclosing + legs.'},
]
