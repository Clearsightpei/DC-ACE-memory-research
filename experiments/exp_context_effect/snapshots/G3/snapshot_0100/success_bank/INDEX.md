# Success Bank — INDEX (G3 coord-bank)

**Phase-1-only reconstruction.** This bank was reset after a Phase-2
restart mishap in which a pruning-parser bug misinterpreted radical
aliasing rows (丨/一/丶/乛 reusing shu/heng/dian/heng_gou) as
authorising deletion of the referenced primitive files themselves.
Four primitives (`heng.py`, `shu.py`, `dian.py`, `heng_gou.py`) were
lost and have been re-extracted from their passing Phase-1 attempts;
`heng.py` was reconstructed against its passing-attempt docstring
(200x12 px horizontal, canvas-centered) since the attempt only
imported the primitive without inlining logic.

The bank now contains **only Phase-1 stroke primitives** that
correspond to passing `p1_stroke_*` attempts. No Phase-2 radicals are
included. Format for every entry:
`def draw_<name>(t, ox=0, oy=0, scale=1.0)` where `t` is a PIL
`ImageDraw` and `(ox, oy, scale)` are numeric offsets on a 300x300
canvas — no 米字格 anchors, no cell references, no joint specs. Pure
coord format.

| # | name | file | strokes | mastered at |
|---|------|------|---------|-------------|
| 1 | 横 (heng) | heng.py | 1 | p1_stroke_01_横 |
| 2 | 竖 (shu) | shu.py | 1 | p1_stroke_02_竖 |
| 3 | 撇 (pie) | pie.py | 1 | p1_stroke_03_撇 |
| 4 | 捺 (na) | na.py | 1 | p1_stroke_04_捺 |
| 5 | 点 (dian) | dian.py | 1 | p1_stroke_05_点 |
| 6 | 提 (ti) | ti.py | 1 | p1_stroke_06_提 |
| 7 | 弯钩 (wan gou) | wan_gou.py | 1 (compound) | p1_stroke_07_弯钩 |
| 8 | 卧钩 (wo gou) | wo_gou.py | 1 (compound) | p1_stroke_08_卧钩 |
| 9 | 横撇 (heng pie) | heng_pie.py | 1 (compound) | p1_stroke_09_横撇 |
| 10 | 横钩 (heng gou) | heng_gou.py | 1 (compound) | p1_stroke_10_横钩 |
| 11 | 横折 (heng zhe) | heng_zhe.py | 1 (compound) | p1_stroke_11_横折 |
| 12 | 竖提 (shu ti) | shu_ti.py | 1 (compound) | p1_stroke_12_竖提 |
| 13 | 竖弯 (shu wan) | shu_wan.py | 1 (compound) | p1_stroke_13_竖弯 |
| 14 | 竖折 (shu zhe) | shu_zhe.py | 1 (compound) | p1_stroke_15_竖折 |
| 15 | 撇点 (pie dian) | pie_dian.py | 1 (compound) | p1_stroke_17_撇点 |
| 16 | 撇折 (pie zhe) | pie_zhe.py | 1 (compound) | p1_stroke_18_撇折 |
| 17 | 橫折提 (heng zhe ti) | heng_zhe_ti.py | 1 (compound) | p1_stroke_20_橫折提 |
| 18 | 横折钩 (heng zhe gou) | heng_zhe_gou.py | 1 (compound) | p1_stroke_22_横折钩 |
| 19 | 横撇弯钩 (heng pie wan gou) | heng_pie_wan_gou.py | 1 (compound) | p1_stroke_24_横撇弯钩 |
| 20 | 竖折撇 (shu zhe pie) | shu_zhe_pie.py | 1 (compound) | p1_stroke_27_竖折撇 |
| 21 | 竖折折 (shu zhe zhe) | shu_zhe_zhe.py | 1 (compound) | p1_stroke_28_竖折折 |
| 22 | 横折折撇 (heng zhe zhe pie) | heng_zhe_zhe_pie.py | 1 (compound) | p1_stroke_29_横折折撇 |
| 23 | 横折折折 (heng zhe zhe zhe) | heng_zhe_zhe_zhe.py | 1 (compound) | p1_stroke_30_横折折折 |
| 24 | 竖钩 (shu gou) | shu_gou.py | 1 (compound) | p1_stroke_14_竖钩 (batch-3 retry PASS) |
| 25 | 竖弯钩 (shu wan gou) | shu_wan_gou.py | 1 (compound) | p1_stroke_23_竖弯钩 (batch-3 retry PASS) |
| 26 | 丨 radical (gun_radical) | gun_radical.py | 1 (variant of shu — scooping head) | p2_radical_001_丨 (bootstrap) |
| 27 | 亅 radical (jue_radical) | jue_radical.py | 1 (alias — wraps shu_gou at +22,-5,0.85) | p2_radical_002_亅 (bootstrap) |
| 28 | 丿 radical (pie_radical) | pie_radical.py | 1 (variant of pie — softer scoop; P10) | p2_radical_003_丿 (bootstrap) |
| 29 | 乛 radical (heng_gou_radical) | heng_gou_radical.py | 1 (variant of heng_gou — thinner, shorter) | p2_radical_004_乛 (bootstrap) |
| 30 | 一 (yi) | yi.py | 1 (inlined 横 with soft-taper width profile) | p2_radical_005_一 (bootstrap) |
| 31 | 乙 radical (yi_radical) | yi_radical.py | 1 (continuous 横折弯钩-form sweep) | p2_radical_006_乙 (bootstrap) |
| 32 | 乚 radical (ya_radical) | ya_radical.py | 1 (alias — wraps shu_wan_gou at -45,-12,1.2) | p2_radical_007_乚 (bootstrap) |
| 33 | 丶 radical (dian_radical) | dian_radical.py | 1 (variant of dian — longer, slimmer) | p2_radical_008_丶 (bootstrap) |
| 34 | 八 (ba) | ba.py | 2 (pie + na, V-notch top) | p2_radical_009_八 (bootstrap) |
| 35 | 冫 (bing) | bing.py | 2 (dian + inlined down-left slash w/ up-right hook) | p2_radical_012_冫 (bootstrap) |
| 36 | 卜 (bu) | bu.py | 2 (shu + dian) | p2_radical_013_卜 (bootstrap) |
| 37 | 刂 (dao_pang) | dao_pang.py | 2 (short shu + shu_gou) | p2_radical_016_刂 (bootstrap) |
| 38 | 儿 (er_ren) | er_ren.py | 2 (pie + shu_wan_gou) | p2_radical_017_儿 (bootstrap) |
| 39 | 二 (er) | er.py | 2 (two heng — upper short, lower long) | p2_radical_018_二 (bootstrap) |
| 40 | 匚 (fang) | fang.py | 2 (heng + inlined 竖折) | p2_radical_019_匚 (B1, pos 51) |
| 41 | 几 (ji) | ji.py | 2 (inlined 撇 + inlined 横折弯钩 bezier) | p2_radical_022_几 (B1, pos 54) |
| 42 | 卩 (jie_radical) | jie_radical.py | 2 (fully inlined 横折钩 + 竖) | p2_radical_023_卩 (B1, pos 55) |
| 43 | 冖 (mi_radical) | mi_radical.py | 1 (inlined 横钩 tuned wider) | p2_radical_026_冖 (B1, pos 58) |
| 44 | 凵 (qu_radical) | qu_radical.py | 1 (inlined U-shape: shu + heng + shu) | p2_radical_027_凵 (B1, pos 59) |
| 45 | 亻 (ren_pang) | ren_pang.py | 2 (pie + shu, left-radical scale) | p2_radical_029_亻 (B1, pos 61) |
| 46 | 十 (shi) | shi.py | 2 (heng crossing shu at center — TR4 exemplar) | p2_radical_031_十 (B1, pos 63) |
| 47 | 亠 (tou_radical) | tou_radical.py | 2 (dian + heng) | p2_radical_033_亠 (B1, pos 65) |
| 48 | 匸 (xi_radical) | xi_radical.py | 2 (heng + inlined 竖折, similar to 匚) | p2_radical_034_匸 (B1, pos 66) |
| 49 | 又 (you) | you.py | 2 (pie + heng_pie / na-like) | p2_radical_037_又 (B1, pos 69) |
| 50 | 艹 (cao_zi_tou) | cao_zi_tou.py | 3 (fully inlined: heng + two 竖 tails) | p2_radical_039_艹 (B1, pos 71) |
| 51 | 川 (chuan) | chuan.py | 3 (inlined 撇 + 2 shu, spaced verticals) | p2_radical_043_川 (B1, pos 75) |
| 52 | 辶 (zou_zhi) | zou_zhi.py | 3 (dian + inlined 横折折撇 + inlined 平捺) | p2_radical_044_辶 (B1, pos 76) |
| 53 | 寸 (cun) | cun.py | 3 (heng + shu_gou + dian) | p2_radical_045_寸 (B1, pos 77) |
| 54 | 干 (gan) | gan.py | 3 (two heng + shu) | p2_radical_048_干 (B1, pos 80) |
| 55 | 工 (gong) | gong.py | 3 (heng + shu + heng) | p2_radical_049_工 (B1, pos 81) |
| 56 | 廾 (gong_radical) | gong_radical.py | 4 (inlined) | p2_radical_051_廾 (B1, pos 83) |
| 57 | 广 (guang) | guang.py | 3 (dian + inlined heng + inlined 撇) | p2_radical_052_广 (B1, pos 84) |
| 58 | 彐 (ji_radical) | ji_radical.py | 3 (fully inlined: 3 tapered segments) | p2_radical_054_彐 (B1, pos 86) |
| 59 | 口 (kou) | kou.py | 3 (shu + heng_zhe + heng — box) | p2_radical_057_口 (B1, pos 89) |
| 60 | 宀 (bao_gai_tou) | bao_gai_tou.py | 3 (dian + heng_gou + inlined short shu) | p2_radical_060_宀 (B1, pos 92) |
| 61 | 山 (shan) | shan.py | 3 (shu + inlined 竖折 + shu) | p2_radical_063_山 (B1, pos 95) |
| 62 | 彡 (shan_radical) | shan_radical.py | 3 (three pie at descending scale) | p2_radical_064_彡 (B1, pos 96) |
| 63 | 尸 (shi_radical) | shi_radical.py | 3 (fully inlined: heng_zhe_gou + heng + pie) | p2_radical_065_尸 (B1, pos 97) |
| 64 | 饣 (shi_pang) | shi_pang.py | 3 (inlined pie + inlined 横钩 + inlined shu_ti) | p2_radical_066_饣 (B1, pos 98) |
| 65 | 士 (shi_male) | shi_male.py | 3 (heng + shu + heng, upper heng wider) | p2_radical_067_士 (B1, pos 99) |
| 66 | 扌 (shou_pang) | shou_pang.py | 3 (heng + shu_gou + ti) | p2_radical_068_扌 (B1, pos 100) |
| 67 | 厂 (chang) | chang.py | 2 (heng + inlined nearly-vertical 丿) | p2_radical_014_厂 (B1 retry-1 graduation, pos 46) |

**Total: 67 primitives.**

## Batch B1 (2026-07-18, positions 51–100 judged + 2 retries)

27 main-curriculum PASSes recorded above (bank entries 40–66), plus 1
retry graduation (`chang.py`, entry 67 — 厂 passed on retry_1). 23
main-curriculum FAILs added to errata.md; retry #1 for 刀 also FAILed
(retry_n=1). Overall pass rate 27/50 = **54%**, marginally worse than
G1 no-memory (60%) on this batch — the second consecutive batch where
G3 underperformed the control. See `sandbox.md` "Batch B1 diagnostic"
section and `principle_bank.md` §TR8 (new inline-fresh rule).

Naming policy:
- Pure-composition entries (only bank primitive calls with scaled
  offsets): `cun`, `gan`, `gong`, `ren_pang`, `shan_radical`, `shi`,
  `shi_male`, `shou_pang`, `tou_radical`, `you`, `kou`.
- Composition-plus-inline (some bank + custom recipe): `chang`,
  `bao_gai_tou`, `chuan`, `fang`, `guang`, `jie_radical`, `mi_radical`,
  `shan`, `shi_pang`, `xi_radical`, `zou_zhi`.
- Fully inlined (no bank calls — inlining beat force-fit): `cao_zi_tou`,
  `gong_radical`, `ji` (几), `ji_radical` (彐), `qu_radical`,
  `shi_radical` (尸).

## Bootstrap batch (2026-07-17, positions 33–50 judged)

14 PASSes recorded above. Naming policy applied:
- Radicals orthographically same as a mastered stroke but whose PASS
  render is a variant (softer / thinner / longer) got a
  `<pinyin>_radical.py` file with the variant code inlined (丨, 丿, 乛, 丶).
- Radicals that are pure aliases at a fixed transform got a thin
  wrapper delegating to the primitive (亅→shu_gou, 乚→shu_wan_gou).
- Multi-stroke radicals got a plain `<pinyin>.py` composing primitives
  (八, 冫, 卜, 刂, 儿, 二).
- `yi.py` = 一 (character-and-radical coincide).
  `yi_radical.py` = 乙 (pinyin collision with 一 — files are distinct).
- Existing primitives (heng, shu, pie, dian, heng_gou, shu_gou,
  shu_wan_gou, na) reused as building blocks — none were modified.

4 FAILs (勹, 匕, 厂, 刀) added to errata.md; see sandbox.md for
failure-mode analysis and principle_bank.md updates.

Notes:
- Re-extracted after reset: `heng.py` (reconstructed from docstring —
  passing attempt only imported), `shu.py`, `dian.py`, `heng_gou.py`
  (all extracted verbatim from their passing attempts).
- **Re-reconstructed after reset**: `shu_gou.py` and `shu_wan_gou.py`
  (batch-3 retry graduations, originally passed on retry — retry_attempts
  folder was wiped during the Phase-2 restart, so these two files were
  synthesised fresh matching G3's coord format based on `shu.py` conventions).
- The Phase-1 strokes not on this list (16 斜钩, 19 横斜钩,
  21 横折弯, 25 横折弯钩, 26 横折折, 31 竖折折钩,
  32 横折折折钩) had no passing attempt in the current record and are
  intentionally absent.
- `_anchor.py` is not part of this bank — G3 uses raw coord offsets,
  not 米字格 anchors.
- Phase-2 radicals have been removed pending re-derivation in the
  Phase-2 restart.
