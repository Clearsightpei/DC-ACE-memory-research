# Phase 2 — 部首 (radicals) curriculum

After the 32 strokes, all groups learn common radicals. Radicals are the
intermediate compositional units between strokes and characters; most
characters decompose as `radical + phonetic` or `radical + radical`.

Order = curriculum order. Grouped by stroke count for smooth difficulty
progression.

## Display rule during judgment (same as strokes)

- **Target label**: `<radical name/reading>`
- **Target shape**: the radical PNG at 300×300
- **Attempt PNG**: the AI's rendering

The human sees the shape and the label. The tool does NOT render the label
as the target image.

## 1画 (8 radicals)

丨 亅 丿 乛 一 乙 乚 丶

Some of these overlap with Phase 1 strokes (一 = 横, 丨 = 竖, 丿 = 撇, 丶 = 点,
乛 = 横钩). When a radical is the same shape as a stroke, the group's
memory can (and should) reuse the Phase-1 entry. Track this in per-group
memory as a "reuse" record.

## 2画 (30 radicals)

八 勹 匕 冫 卜 厂 刀 刂 儿 二 匚 阝 丷 几 卩 冂 力 冖 凵 人 亻 入 十 厶 亠 匸 讠 廴 又 㔾

## 3画 (46 radicals)

艹 屮 彳 巛 川 辶 寸 大 飞 干 工 弓 廾 广 己 彐 彑 巾 口 马 门 宀 女 犭 山 彡 尸 饣 士 扌 氵 纟 巳 土 囗 兀 夕 小 忄 幺 弋 尢 夂 子 丬 夊

## 4画 (51 radicals — 卝 and 牜 removed per Phase-2 restart, no MMH GT available)

贝 比 灬 长 车 歹 斗 厄 方 风 父 戈 户 火 旡 见 斤 耂 毛 木 肀 牛 爿 片 攴 攵 气 欠 犬 日 氏 礻 手 殳 水 瓦 尣 王 韦 文 毋 心 牙 爻 曰 月 爫 支 止 爪 无

## Totals

- 1画: 8
- 2画: 30
- 3画: 46
- 4画: 51 (was 53; 卝 and 牜 removed — not in MMH graphics.txt)
- **Total: 135 radicals**

## GT rendering for radicals

Each radical's GT PNG is rendered by finding a `graphics.txt` entry
whose `character` field matches the radical codepoint. Rendered isolated
at 300×300 with the same 米字格 conventions as run_6 (centered at
canvas center, math-y up).

Some radicals (like 阝, 亻, 犭) are structural components that appear in
characters but exist as their own codepoint in the Unicode Radicals
block. `graphics.txt` has separate entries for many of them. If a
radical is NOT in `graphics.txt`, we fall back to a hand-mapped
representative character where the radical stands alone or is the
top-most component (e.g. render 忄 by first-stroke medians of 忙).
The mapping table lives in `curriculum/radical_gt_sources.json` (to
be generated during setup).

## Sub-agent brief note

By the end of Phase 2, G3/G4's Success Bank should contain 138
radical entries (~150 counting strokes + reuse tags). G2 may
organize differently. This intermediate layer is critical: Phase 3
characters that decompose into learned radicals should require FAR
less memory work than characters that don't. A key hypothesis is
that G4's memory format (米字格 + joint spec) lets it compose
radicals into characters more accurately than G3's coordinate format.
