# Success Bank — INDEX (G4 grid-bank, Phase-1-only reset)

## Reset context

This index was rebuilt after a wholesale-deletion mishap during a
Phase-2 restart pruning pass. The parser that was supposed to trim the
bank down to Phase-1 stroke primitives mis-handled G4's INDEX table
format and wiped every stroke `.py` file (leaving only `_anchor.py`).
This is a clean **Phase-1-only** rebuild — no Phase-2 radicals — from
the 26 passing Phase-1 stroke attempts (batch 1: 19 items, batch 2's
Phase-1 slice: 7 items).

Primitives were reconstructed from the .pyc metadata (signatures +
docstrings survived in `__pycache__`), the batch attempt files, and
G4's shared conventions. Every primitive was smoke-tested by importing
+ rendering with sample anchors.

## Convention (unchanged)

Anchors use the 米字格 convention (see `code/_anchor.py`):
`(cell, x_frac, y_frac)` where cell ∈
`{TL, TC, TR, ML, C, MR, BL, BC, BR}`. `x_frac` from cell LEFT edge,
`y_frac` from cell TOP edge (**PIL-native: y grows DOWN**). Canvas is
300×300; each cell is 100×100.

Helper: `_anchor.py` — provides `anchor_to_xy`, `quad_bezier`,
`stroke_variable_width`, `fat_line`, `sample_line`.

## Batch 1 (Phase-1 strokes 01–20; 19 passes)

| # | Item | File | Signature | Joints |
|---|------|------|-----------|--------|
| 01 | 横 (héng) | `heng.py` | `draw_heng(draw, from_anchor, to_anchor, width=10)` | none |
| 02 | 竖 (shù) | `shu.py` | `draw_shu(draw, from_anchor, to_anchor, width=10)` | none |
| 03 | 撇 (piě) | `pie.py` | `draw_pie(draw, from_anchor, to_anchor, head_width=12, tail_width=1, curve=0.10, segments=48)` | none |
| 04 | 捺 (nà) | `na.py` | `draw_na(draw, from_anchor, to_anchor, head_width=3, peak_width=14, tail_width=1, peak_t=0.8, curve=0.10, segments=48)` | none |
| 05 | 点 (diǎn) | `dian.py` | `draw_dian(draw, from_anchor, to_anchor, head_width=2, peak_width=11, curve=0.08, segments=24)` | none |
| 06 | 提 (tí) | `ti.py` | `draw_ti(draw, from_anchor, to_anchor, head_width=13, tail_width=1, curve=0.09, segments=48)` | none |
| 07 | 弯钩 (wān gōu) | `wan_gou.py` | `draw_wan_gou(draw, head, belly, hook_pt, tip, head_w=8, belly_w=12, hook_start_w=10, tip_w=2)` | internal hook (up-left) |
| 08 | 卧钩 (wò gōu) | `wo_gou.py` | `draw_wo_gou(draw, start, belly, exit, tip, head_w=3, belly_w=10, exit_w=10, tip_w=1)` | internal hook (up-left) |
| 09 | 横撇 (héng piě) | `heng_pie.py` | `draw_heng_pie(draw, head, corner, tip, head_w=7, corner_w=11, tip_w=2)` | P (welded) at corner |
| 10 | 横钩 (héng gōu) | `heng_gou.py` | `draw_heng_gou(draw, head, shoulder, tip, head_w=8, mid_w=6, shoulder_w=11, tip_w=2)` | internal hook (down-left) |
| 11 | 横折 (héng zhé) | `heng_zhe.py` | `draw_heng_zhe(draw, head, corner, tail, h_width=10, v_width=10, shoulder=13)` | P at corner |
| 12 | 竖提 (shù tí) | `shu_ti.py` | `draw_shu_ti(draw, shu_head, shu_tail, ti_tail, shu_head_w=13, shu_tail_w=11, ti_head_w=13, ti_tail_w=1)` | P at shu_tail = ti_head |
| 13 | 竖弯 (shù wān) | `shu_wan.py` | `draw_shu_wan(draw, head, belly, corner, tail, head_w=8, belly_w=12, corner_w=11, tail_w=9)` | welded round bend at corner |
| 14 | 竖钩 (shù gōu) | `shu_gou.py` | `draw_shu_gou(draw, head, belly, hook_pt, tip, head_w=13, belly_w=11, hook_start_w=10, tip_w=2)` | internal hook (up-left); body must stay STRAIGHT (belly is width-knot, not curve control) |
| 15 | 竖折 (shù zhé) | `shu_zhe.py` | `draw_shu_zhe(draw, head, corner, tail, v_width=10, h_width=10, shoulder=13)` | P at corner |
| 16 | 斜钩 (xié gōu) | `xie_gou.py` | `draw_xie_gou(draw, head, belly, hook_pt, tip, head_w=8, belly_w=15, hook_start_w=13, tip_w=2)` | internal hook (points UP, not up-left) |
| 17 | 撇点 (piě diǎn) | `pie_dian.py` | `draw_pie_dian(draw, head, pivot, tail, pie_head_w=13, pie_tip_w=4, dian_head_w=4, dian_tail_w=11)` | P at pivot |
| 18 | 撇折 (piě zhé) | `pie_zhe.py` | `draw_pie_zhe(draw, head, pivot, tail, pie_head_w=13, pie_tip_w=5, heng_w=7, shoulder=4)` | P at pivot |
| 20 | 橫折提 (héng zhé tí) | `heng_zhe_ti.py` | `draw_heng_zhe_ti(draw, head_h, corner, knee, tail, h_width=10, v_head_w=10, v_knee_w=12, shoulder=13, knee_shoulder=14, ti_head_w=13, ti_tail_w=1, ti_curve=0.06)` | P at corner, P at knee |

FAIL in batch 1: 19 横斜钩 (not in this bank; see `errata.md` if it
still exists in the source-of-truth memory, else re-derive from
scratch).

## Batch 2 (Phase-1 stroke portion, strokes 21–32; 7 passes)

| # | Item | File | Signature | Joints |
|---|------|------|-----------|--------|
| 22 | 横折钩 (héng zhé gōu) | `heng_zhe_gou.py` | `draw_heng_zhe_gou(draw, head, corner, tail, tip, h_width=10, v_width=10, shoulder=13, tip_w=2)` | P at corner, internal hook (up-left) |
| 23 | 竖弯钩 (shù wān gōu) | `shu_wan_gou.py` | `draw_shu_wan_gou(draw, head, belly, corner, hook_pt, tip, head_w=8, belly_w=12, corner_w=11, hook_start_w=10, tip_w=2)` | welded round bend at corner, internal UP hook |
| 24 | 横撇弯钩 (héng piě wān gōu) | `heng_pie_wan_gou.py` | `draw_heng_pie_wan_gou(draw, head_h, corner, knee, belly, hook_pt, tip, h_width=8, corner_shoulder=12, pie_head_w=11, pie_knee_w=8, knee_shoulder=11, wan_head_w=8, wan_belly_w=12, hook_start_w=10, tip_w=2)` | P at corner, P at knee, internal hook |
| 28 | 竖折折 (shù zhé zhé) | `shu_zhe_zhe.py` | `draw_shu_zhe_zhe(draw, head, corner1, corner2, tail, v_width=10, h_width=10, shoulder=13)` | P × 2 (corner1, corner2) |
| 30 | 横折折折 (héng zhé zhé zhé) | `heng_zhe_zhe_zhe.py` | `draw_heng_zhe_zhe_zhe(draw, head, corner1, corner2, corner3, tail, h_width=10, v_width=10, shoulder=13)` | P × 3 (corner1..3) |
| 31 | 竖折折钩 (shù zhé zhé gōu) | `shu_zhe_zhe_gou.py` | `draw_shu_zhe_zhe_gou(draw, head, corner1, corner2, hook_pt, tip, v_width=10, h_width=10, shoulder=13, hook_start_w=10, tip_w=1)` | P × 2, internal hook (up-left) |
| 32 | 横折折折钩 (héng zhé zhé zhé gōu) | `heng_zhe_zhe_zhe_gou.py` | `draw_heng_zhe_zhe_zhe_gou(draw, head, corner1, corner2, corner3, tail, tip, h_width=10, v_width=10, shoulder=13, tip_w=2)` | P × 3, internal hook (up-left) |

Batch 2's Phase-1 failures (21 横折弯, 25 横折弯钩, 26 横折折, 27 竖折撇,
29 横折折撇) and all Phase-2 radicals are NOT in this bank — the reset
is Phase-1-only. Any Phase-2 work restarts from an empty Phase-2 slate.

## Bootstrap batch (Phase-2 radicals, positions 33–50; 12 passes)

12 Phase-2 radicals promoted from the bootstrap batch (2026-07-17).
All are 1画 or 2画 radicals; the 1画 wrappers alias existing Phase-1
stroke primitives with MMH-derived standalone anchors.

| pos | item_id | Radical | File | Signature | Joints |
|-----|---------|---------|------|-----------|--------|
| 33 | p2_radical_001_丨 | 丨 (gǔn, 1画) | `gun.py` | `draw_gun(draw, head=('TC',0.301,0.665), tail=('BC',0.412,1.0), width=10)` — wrapper for `draw_shu` | none |
| 34 | p2_radical_002_亅 | 亅 (jué, 1画) | `jue.py` | `draw_jue(draw, head=('TC',0.283,0.674), belly=('C',0.283,0.35), hook_pt=('BC',0.283,0.85), tip=('BL',0.973,0.722))` — wrapper for `draw_shu_gou` | internal hook |
| 36 | p2_radical_004_乛 | 乛 (1画) | `heng_gou_cover.py` | `draw_heng_gou_cover(...)` — wrapper for `draw_heng_gou`, head ML(0.782,0.342), shoulder MR(0.40,0.25), tip C(0.89,0.623) | internal hook |
| 37 | p2_radical_005_一 | 一 (yī, 1画) | `yi_one.py` | `draw_yi_one(draw, head=('ML',0.354,0.849), tail=('MR',0.695,0.825), width=10)` — wrapper for `draw_heng` | none |
| 38 | p2_radical_006_乙 | 乙 (yǐ, 1画) | `yi_second.py` | `draw_yi_second(draw, head, corner, bottom, hook_s, tail)` — inlined 4-segment variable-width path (no bank primitive fits) | none (single continuous stroke) |
| 40 | p2_radical_008_丶 | 丶 (zhǔ, 1画) | `zhu.py` | `draw_zhu(draw, head=('TC',0.146,0.946), tail=('C',0.717,0.652), peak_width=7, ...)` — wrapper for `draw_dian` (thinner peak_width than default) | none |
| 41 | p2_radical_009_八 | 八 (bā, 2画) | `ba.py` | `draw_ba(draw, s1_head=('ML',0.97,0.623), s1_tail=('BL',0.261,0.64), s2_head=('TC',0.324,0.964), s2_tail=('BR',0.865,0.569))` — 撇 + 捺 | none (S) |
| 42 | p2_radical_010_勹 | 勹 (bāo, 2画) | `bao.py` | `draw_bao(draw, s1_head, s1_tail, s2_head, s2_corner, s2_tail, s2_tip)` — 撇 + 横折钩 | N at ML (small gap ~15-20 px) |
| 43 | p2_radical_011_匕 | 匕 (bǐ, 2画) | `bi.py` | `draw_bi(draw, s1_head, s1_tail, s2_head, s2_belly, s2_corner, s2_hook_pt, s2_tip)` — 撇 + 竖弯钩 | N crossing at s2 body midpoint |
| 44 | p2_radical_012_冫 | 冫 (bīng, 2画) | `bing.py` | `draw_bing(draw, s1_head=('TC',0.245,0.976), s1_tail=('C',0.638,0.395), s2_head=('BC',0.315,0.780), s2_tail=('C',0.734,0.781))` — 点 + 提 | none (S) |
| 45 | p2_radical_013_卜 | 卜 (bǔ, 2画) | `bu.py` | `draw_bu(draw, s1_head=('TC',0.213,0.642), s1_tail=('BC',0.342,1.0), s2_head=('C',0.62,0.477), s2_tail=('MR',0.396,0.91))` — 竖 + 点 | N at s1.mid ⇆ s2.head (gap ~35 px) |
| 50 | p2_radical_018_二 | 二 (èr, 2画) | `er.py` | `draw_er(draw, s1_head=('ML',0.858,0.28), s1_tail=('MR',0.147,0.157), s2_head=('BL',0.369,0.358), s2_tail=('BR',0.684,0.326))` — 横 + 横; top shorter than bottom | none (S) |

FAIL (human) in bootstrap batch (6 items, positions 35/39/46/47/48/49):
p2_radical_003_丿, 007_乚, 014_厂, 015_刀, 016_刂, 017_儿 — see `errata.md`.

## Bank size

**38 primitives** (26 Phase-1 + 12 Phase-2 bootstrap radicals) +
`_anchor.py` helper = **39 files** in `code/`.
