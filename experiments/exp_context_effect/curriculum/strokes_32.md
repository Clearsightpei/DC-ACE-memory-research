# Phase 1 — 32 笔画 (strokes) curriculum

The primer. Every group learns these 32 canonical strokes as isolated shapes
before moving to radicals or characters. Order matches the standard Chinese
pedagogy sequence (single-segment first, then compound strokes).

## Display rule during judgment

When the human judges a stroke attempt, the tool shows:
- **Target label**: `<stroke name>` (e.g. `竖`)
- **Target shape**: the primitive rendered at 300×300 (`｜`)
- **Attempt PNG**: the AI's rendering

The stroke name is text; the target shape is a PNG. The human never sees a
character that USES the stroke — only the stroke shape itself.

## The 32 strokes

Order = curriculum order (index 1..32).

### Single-segment strokes (8)

| Idx | Name | Shape (canonical) | Example characters using this stroke |
|---:|---|---|---|
|  1 | 横 (héng) | horizontal line | 一 天 日 |
|  2 | 竖 (shù)  | vertical line   | 下 旧 正 |
|  3 | 撇 (piě)  | down-left sweep | 八 反 师 |
|  4 | 捺 (nà)   | down-right sweep| 人 八 之 远 |
|  5 | 点 (diǎn) | dot / short diagonal | 小 点 欢 |
|  6 | 提 (tí)   | up-right rising | 习 把 河 |
|  7 | 弯钩 (wāngōu) | curved hook | 狗 家 象 |
|  8 | 卧钩 (wògōu)  | lying hook   | 心 必 您 |

### Two-segment compound strokes (10)

| Idx | Name | Shape | Example |
|---:|---|---|---|
|  9 | 横撇 (héng-piě) | ¬ then down-left | 又 水 多 |
| 10 | 横钩 (héng-gōu) | ¬ ending with hook | 了 买 宝 |
| 11 | 横折 (héng-zhé) | ¬ (90° corner) | 口 五 骨 |
| 12 | 竖提 (shù-tí) | ⌊ up-right | 以 长 收 |
| 13 | 竖弯 (shù-wān) | ⌊ curved | 四 西 酉 |
| 14 | 竖钩 (shù-gōu) | ⌊ with hook | 小 了 把 |
| 15 | 竖折 (shù-zhé) | ⌊ | 山 发 牙 |
| 16 | 斜钩 (xié-gōu) | diagonal-down-right + hook | 我 成 戏 |
| 17 | 撇点 (piě-diǎn) | pie then dot-turn | 女 巡 巢 |
| 18 | 撇折 (piě-zhé) | pie then horizontal | 车 去 红 |

### Three-segment / hook compound strokes (11)

| Idx | Name | Shape | Example |
|---:|---|---|---|
| 19 | 横斜钩 (héng-xié-gōu) | héng + diagonal + hook | 飞 气 风 |
| 20 | 橫折提 (héng-zhé-tí) | héng + drop + rising | 认 鸠 颓 |
| 21 | 横折弯 (héng-zhé-wān) | héng + drop + curved | 设 朵 船 |
| 22 | 横折钩 (héng-zhé-gōu) | héng + drop + hook | 月 习 也 |
| 23 | 竖弯钩 (shù-wān-gōu) | shù + curve + hook | 儿 电 巴 |
| 24 | 横撇弯钩 (héng-piě-wān-gōu) | héng+撇+弯+钩 | 阳 那 |
| 25 | 横折弯钩 (héng-zhé-wān-gōu) | complex hook | 九 乙 吃 |

### Four-segment stroke and rarer compounds (7)

| Idx | Name | Shape | Example |
|---:|---|---|---|
| 26 | 横折折 (héng-zhé-zhé) | héng + drop + héng | 凹 |
| 27 | 竖折撇 (shù-zhé-piě) | shù + héng + piě | 专 |
| 28 | 竖折折 (shù-zhé-zhé) | shù + héng + shù | 鼎 |
| 29 | 横折折撇 (héng-zhé-zhé-piě) | 4 segments | 及 建 边 |
| 30 | 横折折折 (héng-zhé-zhé-zhé) | 4 segments | 凸 |
| 31 | 竖折折钩 (shù-zhé-zhé-gōu) | 4 seg + hook | 马 写 号 |
| 32 | 横折折折钩 (héng-zhé-zhé-zhé-gōu) | 5 seg + hook | (rare glyphs) |

## GT rendering for strokes

Each stroke's GT PNG is rendered from the FIRST stroke's median of a
representative character in `draw_character/graphics.txt`, isolated in a
300×300 canvas. The choice of representative character per stroke is fixed
in `curriculum/stroke_gt_sources.json` (to be generated) — so every group
sees the identical target shape.

Example: for stroke #1 (横), the GT is the first stroke's median of `一`
isolated at 300×300 center.

## Sub-agent brief note

All 4 groups draw these 32 strokes first. G1 sees no memory; G2/G3/G4
can populate their memory during this phase (a valid "stroke primitive
memory" is a plausible first bank entry). This phase seeds the memory,
so how each group encodes strokes will affect all downstream phases.
