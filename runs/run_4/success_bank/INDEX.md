# Success Bank — Index

Curator-owned. **Only mastered code lives here.** Entries are added
when the Curator decides a Drawer output crossed the mastery gate
(`is_correct AND ocr_confidence ≥ 0.4 AND rubric ≥ 7 no 0`, after
both skeleton and brushwork phases passed).

## How to use this bank (for the Drawer)

Two queries:

1. **By character**: looking up a whole character that's been
   mastered — copy the code from `code/<char>.py` verbatim,
   including all parameters.
2. **By component tag**: looking up a 部首 or 笔画 组合 — grep this
   INDEX for the tag (e.g. `tag:撇捺-symmetric`) and pull the cited
   entries.

**Never modify a Success Bank file by guessing.** If parameters need
adjustment for a new context (translate, scale), follow the rules in
`principle_bank.md` — but the *primitives themselves* are immutable
"hardware tools".

## Visual index

`visual/visual_index.png` — assembled grid of past wins, regenerated
by the Curator when a new entry is added. The Drawer sees this card
during render time. **This is the Drawer's only legal source of
visual reference** (it shows the Drawer's own past outputs, not GT).

## Entries

| char | file | rubric | component tags | added in cycle |
|------|------|--------|----------------|----------------|
| 横    | [code/heng.py](code/heng.py) | 10/10 | tag:atomic-stroke tag:heng | c1 |
| 竖    | [code/shu.py](code/shu.py)   | 10/10 | tag:atomic-stroke tag:shu tag:垂露竖 | c2 |
| 撇    | [code/pie.py](code/pie.py)   | 10/10 | tag:atomic-stroke tag:撇 tag:斜撇 tag:tapered-tip | c3 |
| 捺    | [code/na.py](code/na.py)     | 10/10 | tag:atomic-stroke tag:捺 tag:斜捺 tag:flat-kick-tail tag:multi-segment | c4 |
| 提    | [code/ti.py](code/ti.py)     | 10/10 | tag:atomic-stroke tag:提 tag:tapered-tip | c5 |
| 点    | [code/dian.py](code/dian.py) | 10/10 | tag:atomic-stroke tag:点 tag:右点 | c6 |
| 横折  | [code/heng_zhe.py](code/heng_zhe.py) | 10/10 | tag:compound-stroke tag:横折 tag:multi-segment tag:corner-顿笔 | c7 |
| 竖钩  | [code/shu_gou.py](code/shu_gou.py) | 10/10 | tag:compound-stroke tag:竖钩 tag:hook tag:multi-segment | c8 |
| 横折钩 | [code/heng_zhe_gou.py](code/heng_zhe_gou.py) | 10/10 | tag:compound-stroke tag:横折钩 tag:hook tag:multi-segment tag:corner-顿笔 | c9 |
| 竖弯钩 | [code/shu_wan_gou.py](code/shu_wan_gou.py) | 10/10 | tag:compound-stroke tag:竖弯钩 tag:hook tag:multi-segment tag:curved-middle | c10 |
| 横撇  | [code/heng_pie.py](code/heng_pie.py) | 10/10 | tag:compound-stroke tag:横撇 tag:tapered-tip tag:multi-segment tag:corner-顿笔 | c11 |
| 竖折  | [code/shu_zhe.py](code/shu_zhe.py) | 10/10 | tag:compound-stroke tag:竖折 tag:multi-segment tag:corner-顿笔 | c12 |
| 横折弯钩 | [code/heng_zhe_wan_gou.py](code/heng_zhe_wan_gou.py) | 10/10 | tag:compound-stroke tag:横折弯钩 tag:hook tag:multi-segment tag:corner-顿笔 tag:curved-middle | c13 |
| 一    | [code/yi.py](code/yi.py) | 10/10 (OCR 一 conf 0.77, visual 0.85) | tag:character tag:1-stroke tag:heng tag:component-of(三,二,王,工,干,上,下) | c14 |
