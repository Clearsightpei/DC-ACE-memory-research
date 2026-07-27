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

## Batch B1 (Phase-2 radicals 019–068; 35 pass + 15 fail + 4 retry-pass + 2 retry-fail)

Human PASS on 35/50 main items and 4/6 retries (乚 厂 刂 儿). The 2
retry-fail items (丿 刀) stay in `errata.md` with updated diagnoses.

### Main-batch promotions (35 files)

| pos | item_id | Radical | File | Composition | Joints |
|-----|---------|---------|------|-------------|--------|
| 51 | p2_radical_019_匚 | 匚 (fāng, 2画) | `fang.py` | 横 + 竖折 | N at TL top-left |
| 52 | p2_radical_020_阝 | 阝-right (fù, 2画) | `fu_right.py` | 横撇弯钩 + 竖 | T/S near ear base |
| 53 | p2_radical_021_丷 | 丷 (2画) | `pian.py` | 点 + 撇 (fanning out) | none (S) |
| 54 | p2_radical_022_几 | 几 (jī, 2画) | `ji.py` | 撇 + 横折弯钩 (inlined) | N at top |
| 58 | p2_radical_026_冖 | 冖 (mì, 2画) | `mi_cover.py` | 短撇 + 横钩 | N at TL corner |
| 59 | p2_radical_027_凵 | 凵 (qiǎn, 2画) | `qian_kan.py` | 竖折 + 竖 | N at BR corner |
| 60 | p2_radical_028_人 | 人 (rén, 2画) | `ren.py` | 撇 + 捺 | T at apex |
| 61 | p2_radical_029_亻 | 亻 (rén-side, 2画) | `ren_side.py` | 撇 + 竖 | T (竖 head on 撇 body) |
| 62 | p2_radical_030_入 | 入 (rù, 2画) | `ru.py` | 撇 + 捺 | N at apex (~12 px) |
| 63 | p2_radical_031_十 | 十 (shí, 2画) | `shi_ten.py` | 横 + 竖 through C | P at C (welded) |
| 64 | p2_radical_032_厶 | 厶 (sī, 2画) | `si_private.py` | 撇折 + 点 | N on right side |
| 65 | p2_radical_033_亠 | 亠 (tóu, 2画) | `tou.py` | 点 + 横 | none (S) |
| 66 | p2_radical_034_匸 | 匸 (xì, 2画) | `xi_box.py` | 横 + 竖折 (left-opening) | N at TR corner |
| 67 | p2_radical_035_讠 | 讠 (yán, 2画) | `yan_speech.py` | 点 + 横折提 | none (S) |
| 68 | p2_radical_036_廴 | 廴 (yǐn, 2画) | `yin_stride.py` | 横折折撇 + 平捺 (both inlined) | P near BL |
| 69 | p2_radical_037_又 | 又 (yòu, 2画) | `you_again.py` | 横撇 + 捺 | P (crossing) |
| 70 | p2_radical_040_屮 | 屮 (chè, 3画) | `chuo.py` | 竖折 + 短竖 + 竖 | P at C, N at right |
| 71 | p2_radical_041_彳 | 彳 (chì, 3画) | `chi_step.py` | 撇 + 撇 + 竖 | 2 × N |
| 72 | p2_radical_042_巛 | 巛 (chuān, 3画) | `chuan_river.py` | 3 × 弯 (inlined helper) | none (S) |
| 73 | p2_radical_043_川 | 川 (chuān, 3画) | `chuan.py` | 撇 + 竖 + 竖 | none (S) |
| 74 | p2_radical_044_辶 | 辶 (chuò, 3画) | `chuo_walk.py` | 点 + 横折折撇 + 平捺 (all inlined) | N at s2-s3 |
| 75 | p2_radical_046_大 | 大 (dà, 3画) | `da.py` | 横 + 撇 + 捺 | P + 2×N |
| 76 | p2_radical_048_干 | 干 (gān, 3画) | `gan.py` | 短横 + 长横 + 竖 | N + P |
| 77 | p2_radical_049_工 | 工 (gōng, 3画) | `gong.py` | 横 + 竖 + 横 | 2 × P |
| 78 | p2_radical_051_廾 | 廾 (gǒng, 3画) | `gong_join.py` | 横 + 撇 + 竖 crossing | 2 × P |
| 79 | p2_radical_052_广 | 广 (guǎng, 3画) | `guang.py` | 点 + 横 + 撇 | N at head-corner |
| 80 | p2_radical_056_巾 | 巾 (jīn, 3画) | `jin.py` | 竖 + 横折 + 竖 (center pierces) | N + P |
| 81 | p2_radical_057_口 | 口 (kǒu, 3画) | `kou.py` | 竖 + 横折 + 横 (all N corners) | 3 × N |
| 82 | p2_radical_060_宀 | 宀 (mián, 3画) | `mian.py` | 点 + 点 + 横钩 | N at top |
| 83 | p2_radical_063_山 | 山 (shān, 3画) | `shan.py` | 竖 + 竖折 + 竖 | 2 × N |
| 84 | p2_radical_064_彡 | 彡 (shān, 3画) | `shan_hair.py` | 3 × 撇 stacked | none (S) |
| 85 | p2_radical_065_尸 | 尸 (shī, 3画) | `shi_corpse.py` | 横折 + 横 + 撇 | 3 × N |
| 86 | p2_radical_066_饣 | 饣 (shí, 3画) | `shi_food.py` | 撇 + 横钩 + 竖提 | 2 × N |
| 87 | p2_radical_067_士 | 士 (shì, 3画) | `shi_scholar.py` | 长横 + 竖 + 短横 (top-longer) | P + N |
| 88 | p2_radical_068_扌 | 扌 (shǒu-side, 3画) | `shou_side.py` | 横 + 竖钩 (inlined) + 提 | 2 × P |

### Retry promotions (4 files, from bootstrap-batch failures)

| item_id | Radical | File | Fix vs bootstrap | Joints |
|---------|---------|------|------------------|--------|
| p2_radical_007_乚 | 乚 (yǐ-hook, 1画) | `yi_hook.py` | swapped `draw_shu_wan` → `draw_shu_wan_gou` for up-tick | none |
| p2_radical_014_厂 | 厂 (chǎng, 2画) | `chang.py` | welded 撇-head to 横-head (T-class shared anchor) | T (weld override; MMH nominal N) |
| p2_radical_016_刂 | 刂 (dāo-side, 2画) | `dao_side.py` | overrode hook_pt.x = head.x to keep shu_gou body vertical | none |
| p2_radical_017_儿 | 儿 (ér, 2画) | `er_legs.py` | canonical 竖弯钩 recipe: bend at bottom, tip up-flick | none |

### B1 fails NOT in bank (17 items = 15 main + 2 retry)

15 main: p2_radical_023_卩, 024_冂, 025_力, 038_㔾, 039_艹, 045_寸, 047_飞,
050_弓, 053_己, 054_彐, 055_彑, 058_马, 059_门, 061_女, 062_犭.
2 retry: p2_radical_003_丿 (retry_1), p2_radical_015_刀 (retry_1).
See `errata.md`.

## Batch B2 (Phase-2 radicals 069–118; 20 main pass + 2 retry pass)

Human PASS on 20/50 main items and 2/9 retries (彐 门). Score
collapsed to 40% main + 22% retry vs B1's 70% + 67%. Diagnosis: many
FAILs are MMH-verbatim renders that ignored TR9 (under-span) or drew
strokes with tilted rows (TR8 rule 5/6 violation). Memory
self-evolution activated in response — principle_bank split into
three files; new `form_catalog.md` created.

### Main-batch promotions (20 files)

| pos | item_id | Radical | File | Composition | Joints |
|-----|---------|---------|------|-------------|--------|
| 101 | p2_radical_069_氵 | 氵 (shuǐ, 3画) | `shui.py` | 点 + 点 + 提 (inlined ti helper) | S (all separate) |
| 103 | p2_radical_071_巳 | 巳 (sì, 3画) | `si.py` | 横折 + 横 + 竖弯钩 | 3 × N |
| 104 | p2_radical_072_土 | 土 (tǔ, 3画) | `tu.py` | 短横 + 竖 + 长横 (bottom-longer) | P + N |
| 105 | p2_radical_073_囗 | 囗 (wéi, 3画) | `wei_enclose.py` | shu + heng_zhe + heng (enclosing) | 3 × N |
| 106 | p2_radical_074_兀 | 兀 (wù, 3画) | `wu_lame.py` | 横 + 撇 + 竖弯 | 2 × N |
| 108 | p2_radical_076_小 | 小 (xiǎo, 3画) | `xiao.py` | 竖钩 + 撇 + 点 | none (S) |
| 109 | p2_radical_077_忄 | 忄 (shù xīn, 3画) | `xin_side.py` | dot(left, inline) + dot(right) + 竖(inline curl-press) | N |
| 110 | p2_radical_078_幺 | 幺 (yāo, 3画) | `yao_small.py` | 撇折 + 撇折 (stacked) + 点 | 2 × N |
| 111 | p2_radical_079_弋 | 弋 (yì, 3画) | `yi_arrow.py` | 短横 + 斜钩 + 点 | P at C (welded) |
| 112 | p2_radical_080_尢 | 尢 (yóu, 3画) | `you.py` | 横 + 撇 + 竖弯钩 | P + N |
| 115 | p2_radical_083_丬 | 丬 (pán, 3画) | `pan.py` | 撇 + 提 + 竖 | N |
| 119 | p2_radical_087_灬 | 灬 (huǒ, 4画) | `huo_four.py` | 4 × 点 (narrow, mirror-outer pair) | none (S) |
| 121 | p2_radical_089_车 | 车 (chē, 4画) | `che.py` | 横 + 撇折(inlined) + 横 + 竖 | 3 × P |
| 127 | p2_radical_095_父 | 父 (fù, 4画) | `fu.py` | 撇 + 点 + 撇 + 捺 (X-cross) | P at BC |
| 135 | p2_radical_103_毛 | 毛 (máo, 4画) | `mao.py` | 撇 + 横 + 横 + 竖弯钩 | N + T + P |
| 136 | p2_radical_104_木 | 木 (mù, 4画) | `mu.py` | 横 + 竖 + 撇 + 捺 | P + N connections |
| 138 | p2_radical_106_牛 | 牛 (niú, 4画) | `niu.py` | 撇 + 短横 + 长横 + 竖 | N + 2 × P |
| 140 | p2_radical_108_片 | 片 (piàn, 4画) | `pian_slice.py` | inline curved pie + shu + heng + heng_zhe | 3 × N |
| 142 | p2_radical_110_攵 | 攵 (pū, 4画) | `pu.py` | 撇 + 横 + 撇 + 捺 (BC-override X-weld) | 3 × N + P at BC |
| 145 | p2_radical_113_犬 | 犬 (quǎn, 4画) | `quan.py` | 大 (heng+pie+na) + upper-right dot | P + 2 × N |

Note: `pian_slice.py` chosen to avoid collision with `pian.py` (丷).
Namespace collision was also latent between `si.py` (巳) and the
existing `si_private.py` (厶) — used a different pinyin gloss.

### Retry promotions (2 files, from B1 failures)

| item_id | Radical | File | Fix vs B1 | Joints |
|---------|---------|------|-----------|--------|
| p2_radical_054_彐 | 彐 (jì, 3画) | `xue_broom.py` | every 横's endpoints in same cell row (TR8 rule 5) — no 100 px diagonal tilt | 2 × N |
| p2_radical_059_门 | 门 (mén, 3画) | `men.py` | enclosing-radical TR2/TR9 layout enforced; 3 strokes coherent as one enclosure | none |

### B2 fails NOT in bank (37 items = 30 main + 7 retry)

30 main: p2_radical_070_纟, 075_夕, 081_夂, 082_子, 084_夊, 085_贝,
086_比, 088_长, 090_歹, 091_斗, 092_厄, 093_方, 094_风, 096_戈,
097_户, 098_火, 099_旡, 100_见, 101_斤, 102_耂, 105_肀, 107_爿,
109_攴, 111_气, 112_欠, 114_日, 115_氏, 116_礻, 117_手, 118_殳.

7 retry (retry_n=1, cool-down 50 items): p2_radical_024_冂, 038_㔾,
047_飞, 050_弓, 053_己, 058_马, 062_犭.

See `errata.md` for per-item diagnoses.

## Bank size (post-B2)

**99 primitives** (77 through B1 + 20 B2 main + 2 B2 retry) +
`_anchor.py` helper = **100 files** in `code/`.
