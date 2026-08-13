# G5 drawer memory

*Curator writes here. Free-form composition playbooks, sibling-pair notes, scale/position tables, retrieval rules — whatever the curator finds useful.*

*Bootstrap 2026-08-08: initial structure seeded. B1 (2026-08-08): expanded retrieval table with the 6 new stroke primitives + 21 new radical primitives. B2 (2026-08-08): +2 new stroke primitives (xie_gou, heng_gou) + 18 new radical primitives (氵 土 囗 小 忄 灬 车 木 日 犬 攵 户 父 戈 欠 牛 巾 饣). B3 (2026-08-08): **first A verdicts** (爻, 了, 人, 又 — 4/50); +3 new stroke primitives (wan_gou, heng_zhe_ti, pie_zhe) + 16 new radical primitives (王 文 爻 曰 月 爫 支 止 无 肀 幺 门 讠 阝 宀 女). Left-radical shrink table validated at Phase-3 (亻). B4 (2026-08-08): **A verdicts collapsed to 0/50** despite heavy P-A-001 identity-reuse — 11 identity-call PASSes (勹 匕 大 门 山 女 宀 口 干 小 艹) all landed PASS not A. Bank +9: retry-PASS radicals 韦/礻/长 + 6 whole-char primitives (上 下 三 千 亡 之). Hook/curve family remains uncovered (刁 丸 也 卂 与 飞 all FAILed).*

---

## Table of contents

- [Bank retrieval hints](#bank-retrieval-hints)
- [Whole-radical retrieval](#whole-radical-retrieval)
- [Composition playbooks](#composition-playbooks)
- [Sibling / minimal-pair notes](#sibling--minimal-pair-notes)
- [MMH anchor calibration notes](#mmh-anchor-calibration-notes) — **MOVED** to `drawer_memory_anchors.md`
- [B7-era retrieval hints](#b7-era-retrieval-hints-2026-08-08)
- [B8-era retrieval hints](#b8-era-retrieval-hints-2026-08-09)
- [B9-era retrieval hints](#b9-era-retrieval-hints-2026-08-09-position-518)
- [B9-era rules of thumb (P-A-007 sharpened, P-A-008 mandatory)](#b9-era-rules-of-thumb-p-a-007-sharpened-p-a-008-mandatory)

---

## Bank retrieval hints

When the MMH block names a stroke class, use this table:

| MMH stroke class            | Bank primitive (file · fn)                              | Signature                          |
|-----------------------------|---------------------------------------------------------|------------------------------------|
| 横 (heng)                   | `heng.py · draw_heng`                                   | (d, head, tail, w_head, w_tail)    |
| 竖 (shu)                    | `shu.py · draw_shu`                                     | (d, head, tail, width, top_curl)   |
| 点 (dian)                   | `dian.py · draw_dian`                                   | (d, head, tail, w_head, w_tail, bow) |
| 撇 (pie)                    | `pie.py · draw_pie`                                     | (d, head, tail, bow_perp, w_head, w_tail) |
| 捺 (na)                     | `na.py · draw_na`                                       | (d, head, tail, bow_perp, w_head, w_tail) |
| 提 (ti) **NEW B1**          | `ti.py · draw_ti`                                       | (d, head, tail, w_head, w_tail)    |
| 横折 (short, soft-arc 乛)   | `heng_zhe_short.py · draw_heng_zhe_short`               | (d, head, tail, corner_offset)     |
| 横折 (BOXY 口/日/月 style) **NEW B1** | `heng_zhe_box.py · draw_heng_zhe_box`         | (d, top_left, bottom_right, width) |
| 横折钩 (compound) **NEW B1**| `heng_zhe_gou.py · draw_heng_zhe_gou`                   | (d, heng_head, corner, gou_tail, hook_tip) |
| 横撇 (heng-pie) **NEW B1**  | `heng_pie.py · draw_heng_pie`                           | (d, head, tail, apex_x, corner_x)  |
| 竖折 (down-then-right) **NEW B1** | `shu_zhe.py · draw_shu_zhe`                       | (d, head, corner, tail, width)     |
| 竖钩 (shu-gou)              | `shu_gou.py · draw_shu_gou`                             | (d, head, tail, width, hook_start_offset) |
| 竖弯钩 (shu-wan-gou)        | `shu_wan_gou.py · draw_shu_wan_gou`                     | (d, head, tail, width, bottom_extra, knee_ratio) |
| 平捺 (flat, wide na) **NEW B1** | `ping_na.py · draw_ping_na`                         | (d, head, tail, belly_drop)        |
| 斜钩 (xie-gou; long diagonal + up-hook) **NEW B2** | `xie_gou.py · draw_xie_gou`     | (d, head, tail, width, bow, hook_up, hook_back) |
| 横钩 (heng-gou; short heng + tight down-hook) **NEW B2** | `heng_gou.py · draw_heng_gou` | (d, head, corner, hook_tip, w_start, w_corner, w_tip) |
| 弯钩 (wan-gou; curved-right vertical + LEFT hook flick) **NEW B3** | `wan_gou.py · draw_wan_gou` | (d, head, tail, belly_right, hook_len, hook_up, w_head, w_body, w_tail) |
| 横折提 (heng-zhe-ti; horizontal + corner + descend + rising ti) **NEW B3** | `heng_zhe_ti.py · draw_heng_zhe_ti` | (d, head, tail, corner=None, descend_mid=None, ti_head=None, width=6) |
| 撇折 (pie-zhe; curved pie + short zhe corner) **NEW B3** | `pie_zhe.py · draw_pie_zhe` | (d, head, corner, tail, pie_bow, zhe_bow, w_head, w_corner, w_tail) |
| 卧钩 (wo-gou; wide smile + up-left hook flick) **NEW B5** | `wo_gou.py · draw_wo_gou` | (d, head, tail, belly_y, width, hook_up, hook_back) |
| 横折 (WIDE mid-body variant, near-square corner + straight drop) **NEW B5** | `heng_zhe_wide.py · draw_heng_zhe_wide` | (d, head, tail, corner=None, w_head, w_tail, corner_dab) |

**Reminder (v13 BANK_DEVIATION)**: bank primitives are REFERENCE. If the current GT wants a different aspect/bow/taper/orientation than the bank entry gives, deviate — and add a `BANK_DEVIATION` block naming what you skipped and why.

---

## Whole-radical retrieval

**Position-signature `(d, ox=0, oy=0, scale=1.0)`.** Callers translate/scale into the composition. Reference canvas is 300×300; when embedding as a sub-component, choose ox/oy/scale so the primitive fits its cell in the target character.

### Bootstrap-era radicals
八 → `ba.py`; 乙 → `yi_second.py`; 乚 → `yi_hook.py`; 勹 → `bao_wrap.py`;
匕 → `bi_dagger.py`; 冫 → `bing_ice.py`; 卜 → `bu_divine.py`;
厂 → `chang_cliff.py`; 刀 → `dao_knife.py`; 刂 → `dao_right.py`; 二 → `er_two.py`.

### B1-era radicals (**high-reuse for Phase 3**)
- 亠 → `tou_lid.py` — top of 六/亡/交/京/亦/...
- 冖 → `mi_cover.py` — bare roof (like 宀 minus left dot)
- 人 → `ren.py`; **亻 → `ren_left.py`** — left-position, appears in 你/他/什/们/作/...
- 入 → `ru.py` — differs from 人 (na extends up past pie)
- 十 → `shi_ten.py` — component of 古/克/直/...
- 又 → `you_again.py` — appears in 权/汉/难/欢/发/...
- 力 → `li_power.py` — appears in 加/努/劳/男/...
- 大 → `da_big.py` — appears in 天/太/夹/夺/头/...
- 工 → `gong_work.py` — appears in 左/式/巧/项/...
- 士 → `shi_scholar.py` — top-heng LONGER than bottom (distinguishes from 土)
- 干 → `gan_dry.py` — TWO heng + shu (distinguishes from 于/千)
- 广 → `guang_wide.py` — encloses 应/床/店/府/座/...
- 山 → `shan_mountain.py`
- 川 → `chuan_river.py`
- 艹 → `cao_grass.py` — top of 花/草/茶/苹/...
- 辶 → `chuo_walk.py` — encloses 这/进/远/近/道/...
- 口 → `kou_mouth.py` — appears in 吃/吗/呢/听/名/号/员/... (very high reuse)
- **扌 → `shou_hand.py`** — left-position, appears in 打/找/把/接/拿/挂/...

**Not promoted from B1 PASS (still available inline in `attempts/`):**
匚, 丷, 卩, 冂, 凵, 厶, 匸, 屮, 彳, 廾, 彐, 彑 (some FAIL), 彡.

### B2-era radicals (**high-reuse for Phase 3**)

Left-position / bottom / enclosing:
- 氵 → `sanshui.py` — WATER left-radical (河/海/江/清/游/汉/洗/汽) — very high freq
- 忄 → `xin_left.py` — HEART left-radical (快/性/情/怕/怀/悟)
- 饣 → `shi_food.py` — FOOD left-radical (饭/饮/饱/馆/饼) [retry PASS]

Bottom radicals:
- 灬 → `si_fire_bot.py` — FIRE-bottom (点/热/然/黑/煮/照/熊/无)
- 小 → `xiao.py` — small (also appears as bottom: 尔/示/京/常)

Right-side radicals:
- 攵 → `pu_action.py` — action-radical (收/教/散/敌/放/敬/故/救)
- 欠 → `qian_owe.py` — owe-radical (次/欢/歌/欲/歇)
- 戈 → `ge_dagger.py` — dagger-axe (我/找/成/战/戏/戒)

Whole-glyph B2 radicals reusable as sub-components:
- 土 → `tu_earth.py` — (地/坐/城/块/坑/场). Distinguish 士 vs 土 (top-heng longer for 士).
- 木 → `mu_wood.py` — (林/森/树/杯/校) — very high freq
- 日 → `ri_sun.py` — (明/时/早/星/暗/昨/晚) — very high freq
- 牛 → `niu_cow.py` — (物/特)
- 犬 → `quan_dog.py` — 大 + top-right dian (哭/伏/献)
- 车 → `che_car.py` — (转/软/连/轻/较)
- 户 → `hu_door.py` — (房/所/扇/雇). Distinguish 户 vs 尸 (户 has top dot).
- 父 → `fu_father.py` — (爸/爷/爹)
- 囗 → `wei_enclose.py` — enclosure (国/回/图/固/围/四/因/园/圆); different scale/shape from 口

**Not promoted from B2 PASS (still available inline in `attempts/`):**
弋 (low-freq bare-radical; xie_gou stroke primitive extracted from it),
丬 (low-freq), 斗 (low-freq), 廴 (multi-turn drawer-specific — MMH suffices).

### B3-era radicals (**high-reuse for Phase-3 & beyond**)

Whole-glyph radicals:
- 王 → `wang_king.py` — 4-stroke (heng+heng+shu+heng bottom long). VERY high-freq (玉/珠/理/球/环/瑞/皇/望). Sibling of 土/士.
- 月 → `yue_moon.py` — VERY high-freq (明/朋/朝/期/服/胖/胜/朗). Composition: pie + heng_zhe_gou + 2 inner hengs.
- 曰 → `yue_say.py` — 4-stroke box; sibling of 日 (WIDER/SHORTER; inner heng stops SHORT of right wall).
- 支 → `zhi_branch.py` — 十 top + 又 bottom (支/枝/技/歧).
- 止 → `zhi_stop.py` — high-freq (企/正/此/歧/步).
- 无 → `wu_none.py` — 4-stroke (heng+heng+pie+shu_wan_gou); sibling of 旡/既.
- 文 → `wen_text.py` — 4-stroke (dian+heng+pie+na); medium-freq.
- 爻 → `yao_lines.py` — **A verdict** — two-X stacked; low-freq but encoded bottom-X recipe.
- 爫 → `zhao_claw_top.py` — top-position (爱/爬/受/爵).

Left-position radicals:
- 讠 → `yan_speech.py` — VERY HIGH-freq (说/话/记/让/请/词/许/该). Compose via draw_yan_speech, scale ~0.60-0.70 shift right when embedded.
- 阝 → `er_ear.py` — VERY HIGH-freq (那/都/阳/院/防/际/陈/阿/隔). 3-shape ear must stay COMPACT (belly max x=175) with clear waist cinch.

Enclosing / top / left mixed:
- 门 → `men_gate.py` — 3-stroke frame (们/闲/间/闭/闪/闷). Dot at TOP-LEFT above horizontal.
- 宀 → `mian_roof.py` — VERY HIGH-freq roof (家/字/客/它/宝/守/宁/宗).
- 女 → `nu_woman.py` — VERY HIGH-freq (好/她/妈/如/姐/妹/婚). Inline compound to preserve P-P-T joint constraint.

Compound / low-reuse:
- 肀 → `yu_brush_top.py` — low-freq, central shu PIERCES all hengs.
- 幺 → `yao_tiny.py` — low-freq; sibling of 纟 (s3 is diagonal not ti).

**Not promoted from B3 PASS but available inline:**
Phase-3 characters 001–033 that matched an existing bank primitive (人/又/入/亻/力/冖/亠/冫/厂/凵/刀/八/十/二/丷/乂 + single-stroke chars 0001-0010) reused existing bank primitives cleanly — no new promotion needed. See INDEX for the list.

### B4-era radicals + whole-char primitives

Retry-PASSed radicals (medium-to-high reuse):
- 韦 → `wei_leather.py` — 4-stroke; component of 伟/违/苇/纬/韩 (medium reuse). Contains an inline BANK_DEVIATION helper for the bottom-hook compound (not extracted separately).
- 礻 → `shi_spirit.py` — HIGH-freq left-position radical (社/礼/福/祝/神/视/祖). Callers embed with `(ox=-30..-40, oy=0, scale=0.9)` starting point.
- 长 → `chang_long.py` — HIGH-freq (张/帐/涨/胀/账). Uses PIL polylines directly; 竖提 compound is baked-in.

Phase-3 whole-char primitives (high-freq componentry):
- 上 → `shang_up.py` — 3-stroke; direct reuse limited but pattern is a stable template for similar shu+heng+heng compositions.
- 下 → `xia_down.py` — 3-stroke; sibling of 上/卜.
- 三 → `san_three.py` — 3 hengs; useful as a component in 王-family and 春/奉/泰-tops.
- 千 → `qian_thousand.py` — 3-stroke; HIGH-freq (千, and component of 迁/舌-partial). Sibling of 干/于.
- 亡 → `wang_gone.py` — 3-stroke; HIGH-freq (忘/忙/慌/望/妄/盲/氓 all contain it).
- 之 → `zhi_this.py` — 3-stroke standalone.

**Not promoted from B4 PASS but available inline** (low-reuse or inline-only):
- 尣 (retry PASS) — low-freq wang variant; inline shu_wan_gou tuning.
- 毋 (retry PASS) — low-freq; polyline frame with 5 P-joints, difficult to reuse.
- Identity-reuse Phase-3 chars (勹/匕/大/门/山/女/宀/口/干/小/艹) already covered by existing radical primitives.
- 之/上/下/三/千/亡 are promoted above; other B4 3-stroke PASSes (丫/丬/个/亼/卄/叉/习/纟/亾) are inline-only (low reuse or fully covered by stroke bank).

### B6-era whole-char primitives (**high-reuse for Phase-3 idx 184+**)

Promoted from B6 mains + first-ever retry A:

- 义 → `yi_x.py` — 3-stroke; **first A verdict from retry channel (B6)**.
  Recipe (P-A-005): dian tapered w_head=3/w_tail=9; pie NEGATIVE bow_perp=-45
  to force mid-belly toward BC; na positive bow + strong tail w_tail=12.
  Reuse: 仪 (人+义), 议 (讠+义), 艺 (艹-derivative).
- 化 → `hua_change.py` — 4-stroke L-R (亻+匕). Reuse: 花, 华.
- 反 → `fan_reverse.py` — 4-stroke (厂+又 inline for interior weld).
  HIGH-reuse: 板, 饭, 返, 贩, 版, 叛.
- 元 → `yuan_first.py` — 4-stroke; sibling of 无 (differs: 元's pie
  starts at LOWER heng level, doesn't cross top heng). HIGH-reuse: 完,
  园, 院, 远, 玩, 冠.
- 主 → `zhu_lord.py` — 5-stroke (dian + 王-lowered + shu). HIGH-reuse:
  住, 注, 柱, 驻, 蛀.
- 正 → `zheng_correct.py` — 5-stroke (top-heng + 止 shifted down).
  HIGH-reuse: 证, 政, 征, 症.
- 生 → `sheng_born.py` — 5-stroke (pie + heng + heng + shu + heng).
  Sibling of 龶 (with added top pie). HIGH-reuse: 性, 星, 姓, 胜, 牲.
- 平 → `ping_flat.py` — 5-stroke (heng + dian + pie + heng + shu; shu
  clamped to y=298 for canvas). HIGH-reuse: 评, 坪, 苹, 秤.

**Not promoted from B6 PASS but available inline** (character-specific or
identity-reuse of existing):
- 22 chars (礻, 刈, 区, 勻, 勿, 卅, 升, 卞, 甲, 出, 申, 甴, 对, 乍, 乎,
  疒, 只, 仔, 仕, 外, 仝, 内-retry-PASS) — see INDEX.md B6 sections.
- Character-specific DEVIATIONs awaiting 2nd occurrence per P-COMP-002:
  队 (er_ear_for_left_position), 书 (shu_book_body), 们 (narrower 门),
  去 (compressed 土 top).

---

## Composition playbooks

*(Populated when a repeated composition pattern earns a name. Phase-3
compositions are the natural source; radicals-only batches don't provide
multi-radical evidence yet. Starter hypotheses below — validate in Phase 3.)*

### Hypothesis: Left-radical shrink table (unvalidated pre-Phase-3)

Left-position radicals shrink to fit ~1/3 of char width and drift right
of their reference canvas center. Predicted transforms (until B2/Phase-3
supplies evidence):

| Radical | Bank fn         | Predicted (ox, oy, scale)  |
|---------|-----------------|-----------------------------|
| 亻      | `draw_ren_left` | (-40, 0, 0.72)              |
| 扌      | `draw_shou`     | (-40, 0, 0.72)              |
| 彳      | (inline)        | (-40, 0, 0.72)              |
| 犭      | (inline — FAIL) | (-40, 0, 0.72)              |
| 冫/氵/讠 | position-radicals | (-45, 20, 0.70)           |

These are guesses. Do not treat as memory until a Phase-3 PASS validates.

### Hypothesis: Top-radical shrink

| Radical | Bank fn      | Predicted (ox, oy, scale) |
|---------|--------------|----------------------------|
| 艹      | `draw_cao`   | (0, -40, 0.70)             |
| 亠      | `draw_tou`   | (0, -40, 0.65)             |
| 冖      | `draw_mi_cover` | (0, -30, 0.75)          |

### Hypothesis: Enclosing radical (广/辶) — anchor as-is, embed sub-component in the enclosed cell

For 广: sub-component sits in the upper-right (~ (110, 80) with scale ~0.6).
For 辶: enclosed component sits in the upper-right quadrant, ping_na sweeps under it.

### Composition rule (validated B2): compose 4-stroke variants from stroke bank, not radical wrappers

日 (4 strokes) does NOT call draw_kou (3 strokes). 囗 (3 strokes, big) does NOT call draw_kou either
because the anchor spread differs. Rule: **if MMH gives a different stroke count OR anchors that differ
by > ~30 px from the whole-radical primitive's baked-in geometry, inline from stroke bank instead**.
This preserves anchor fidelity (which is what MMH is for) and is what the PASSed 日/囗/犬 attempts did.

### v13 BANK_DEVIATION extraction pattern (validated B2)

Two independent BANK_DEVIATIONs on the SAME missing primitive (弋 s2 + 戈 s2 both needed 斜钩; 欠 s2 for 横钩 first appearance) is a strong-enough signal to promote the fresh_component as a new stroke primitive. Do NOT wait for 3 occurrences — that's how B1 delayed heng_zhe_box unnecessarily.

### A-recipe (validated B3, first 4 A verdicts)

Two independent routes to A-quality PASS observed in B3:

**Route 1 — Identity bank reuse** (人 A, 又 A): when a Phase-3 char is literally the same shape as a PASSed Phase-2 radical, and MMH anchors match the bank primitive's baked-in geometry exactly, calling the bank primitive with `ox=0, oy=0, scale=1.0` produces A quality. Zero-parameter deviation. **This is a signal that P-RET-002 (whole-radical over stroke recomposition) not only reduces error but can lift quality.**

**Route 2 — Meticulous MMH-anchor-verbatim composition** (爻 A, 了 A): 4-stroke composition (爻) or BANK_DEVIATION inline crafting (了) can reach A when:
- Stroke count matches MMH exactly (no over/under-count)
- MMH anchors used verbatim OR overridden with justified per-stroke reason
- Every stroke has EXPLICIT taper (w_head != w_tail) — no default widths
- Compound strokes (like 弯钩) use multiple bezier segments with explicit control points, not linear approximations
- For crossing X-patterns: differentiated bow_perp per stroke so the two strokes read as distinct swings, not parallel lines

**A-recipe checklist for future dispatches**:
1. Does a bank primitive exist for this exact shape? → identity-call it (Route 1).
2. Otherwise: compose from stroke bank + explicit MMH anchors + differentiated taper + per-stroke bow (Route 2).
3. Missing primitive class? → BANK_DEVIATION with careful bezier crafting; may seed a Route-1 candidate for future.

**B4 update (2026-08-08) — A-recipe generalized to PASS but NOT to A quality**:
The B3 A-recipe (identity-reuse → A verdict) predicted A verdicts on
Phase-3 chars that ARE bootstrap/B1/B2/B3 radicals. B4 dispatched 11
such items (勹 匕 大 门 山 女 宀 口 干 小 艹). Drawers correctly
applied P-A-001 identity calls on all 11 (verified from generated.py
inspection). **Result: 11 PASS, 0 A.** Similarly, one 千 attempt used
Route-2 (P-A-002 meticulous inline) and landed PASS not A.

**Working hypothesis (test in B5)**: The B3 A-verdicts (人, 又 in
particular) may have been for the simplest/shortest chars (2 strokes).
As char complexity rose (3+ strokes) the human judge's discrimination
tightened — identity-reuse now lifts to PASS but no longer to A.
P-A-001/P-A-002 remain the **correct default recipe** (they produce
clean PASSes and prevent FAILs) — but A quality now needs an extra
push. Candidate additional constraints to try in B5:
- Fine calibration of bow/taper against GT PNG post-render (not just MMH endpoints)
- Explicit joint-gap tuning at N-joints (many identity primitives use
  whatever gap the bootstrap render happened to have)
- Extra visual weight (thicker strokes for standalone chars vs when
  used as sub-radicals)

Do NOT abandon P-A-001. Do NOT stop identity-calling. But if the
dispatch is for a single-radical Phase-3 char AND the drawer has
capacity for a post-render pass, tune bow/taper against the GT
directly (not just MMH) before submitting.

### Heng-zhe-wan-gou family (B3 sandbox — NOT yet in bank)

**Missing primitive class identified B3**: 横折弯钩 (heng-zhe-wan-gou) — horizontal segment + corner-down + curving right belly + small upward hook. Needed by 几, 九, 乃 (variant 横折折折钩), 瓦 (variant), 风 (variant 横斜弯钩). All 3 Phase-3 items with this class FAILed in B3 (0016_乃, 0021_几, 0023_九).

Following P-COMP-002: two independent DEVIATIONs on the same fresh_component (几 s2 + 九 s2 both used `heng_zhe_wan_gou_for_几/九` inline), BUT both attempts FAILed. Cannot promote from failing attempts. **Terminal-freeze deferred**: B4 should retry 几/九 with a curator-provided geometric spec (in sandbox.md B3 postmortem). If either PASSes with an explicit inline heng_zhe_wan_gou, promote at B4 curator time.

---

## Sibling / minimal-pair notes

Add sibling-pair reminders here whenever two nearly-identical radicals
could be confused by the drawer.

- **人 vs 入**: pie head at TC for 人 vs at C for 入; na for 入 extends UP past the pie head.
- **士 vs 土**: top-heng LONGER for 士; top-heng SHORTER for 土. Enforce in reference geometry.
- **干 vs 于 vs 千**: 干 = 2 heng + shu piercing both. 于 = 1 heng + heng-zhe with hook + shu. 千 = pie + heng + shu.
- **己 vs 已 vs 巳**: top-loop closure (己 = open TL, 已 = half-closed, 巳 = closed).
- **刀 vs 力**: 力 has PIERCING pie through the heng_zhe_gou (P-joint); 刀 has neighbor-only spacing.
- **匚 vs 匸**: 匚 = 2-stroke left-bracket, straight lines. 匸 = 2-stroke with hook.
- **户 vs 尸 vs 肀**: 户 has TOP-DOT (dian s1); 尸 has no top dot; 肀 has middle vertical piercing.
- **攴 vs 攵**: 攴 = 卜-top + 又-bottom (4 strokes, distinct); 攵 = pie+heng+pie+na (bottom X). B2: 攴 FAIL, 攵 PASS — attempts confuse them. Reference GT strictly.
- **手 vs 毛**: 手 has shu_gou (central hook) piercing 3 hengs; 毛 has shu_wan_gou (curved-right bottom, terminal hook). Both B2 C.
- **弋 vs 戈**: 戈 has 4 strokes (heng+xie_gou+pie+dian); 弋 has 3 (heng+xie_gou+dian, NO pie). Both use xie_gou primitive.
- **兀 vs 元**: 兀 has 3 strokes (heng+pie+shu_wan, NO upward hook on right leg). 元 adds a top-heng.
- **纟 vs 幺 vs 么**: 纟 has 3 strokes (2 pie_zhe + ti); 幺 has 2-3 strokes ending in dian (no ti); 么 has pie+厶.
- **气 vs 乞**: 气's 4th stroke is 横斜钩 (wraps down + hook); 乞's is 竖弯钩 shorter.
- **士 vs 土 vs 王** (B3): 士 top-heng LONGER than bottom; 土 top-heng SHORTER than bottom; 王 has 3 hengs total with bottom LONGEST.
- **日 vs 曰** (B3): 日 is narrower/TALLER; 曰 is WIDER/SHORTER, and 曰's inner middle heng stops SHORT of the right wall (N-joint, doesn't touch); 日's usually touches.
- **儿 vs 几 vs 九** (B3): 儿 = pie + shu_wan_gou (bottom-right upward hook); 几 = pie + 横折弯钩 (top-horizontal then wrap+hook); 九 = pie + 横折弯钩. NONE currently PASS at Phase-3; missing heng_zhe_wan_gou primitive.
- **无 vs 旡 vs 既** (B3): all 4-stroke; 无 PASSed (draw_wu_none). 旡 is still C — its top pie hooks down-right into a wan-gou variant differing from 无's shu_wan_gou.
- **了 vs 子 vs 字** (B3): all use 弯钩 (`wan_gou.py`, newly promoted from 了 A verdict). 了 = heng_pie + wan_gou. 子 = heng_pie + wan_gou + heng (still FAIL — retry with new wan_gou primitive in B4).
- **文 vs 又 vs 攵** (B3): 文 = dian + heng + pie + na (draw_wen); 又 = heng_pie + na (draw_you); 攵 = pie + heng + pie + na (draw_pu). All four-stroke with bottom-X patterns; the dian and top heng distinguish 文.
- **上 vs 下 vs 卜** (B4): 上 = shu + short-heng + long-heng (heng-tail-up on top); 下 = heng + shu + dian (dot INSIDE the pocket, on the right of shu); 卜 = shu + dian (2 strokes, no top heng).
- **千 vs 干 vs 于** (B4, refined): 千 = pie + heng + shu (top pie sweeps down-left); 干 = 2 hengs + shu (top heng shorter than bottom); 于 = heng + heng_zhe_gou (with hook) + shu. Distinguishing feature = top-most stroke class.
- **三 vs 王 vs 士 vs 土** (B4): 三 = 3 hengs (bottom longest); 王 = 3 hengs + central shu (4 strokes); 士 = 2 hengs + shu (top longer); 土 = 2 hengs + shu (bottom longer).
- **孑 vs 孓 vs 子** (B4): all 3-stroke with heng_pie + wan_gou. 孑 = wan_gou + LEFT ti flick at bottom (no cross-heng — sibling C-radical form). 孓 = wan_gou + heng crossing horizontally (child form). 子 = heng_pie + wan_gou + heng (cross-bar). 孑 PASSed with heng_pie BANK_DEVIATION (shorter/deeper); 孓 PASSed with default heng_pie; 子 FAILed both as main and R2.
- **也 vs 卂** (B4 fails): 也 = heng + shu + shu_wan_gou (wraps right with terminal hook); 卂 = xie_gou (long diagonal) + heng + shu. Both FAILed — composition of the compound stroke vs the small crossing strokes needs refinement.
- **刁 vs 习 vs 力** (B4): 刁 = heng_pie + curved-shu-with-left-hook (like 弯钩 tuned); 习 = heng_zhe-with-hook + 2 dians; 力 = heng_zhe_gou + pie. Sibling family — hook direction distinguishes.
- **夂 vs 夊 vs 攵 vs 久** (B4): 夂 = pie + pie + na (3 strokes, top P-joint at C); 夊 = pie + pie + na with the pies more spread (3 strokes); 攵 = pie + heng + pie + na (4 strokes, has middle heng); 久 = pie + heng-pie + na (3 strokes, middle is compound heng-pie not heng). 夂/夊 both FAILed R2; 久 was C main.

---

## MMH anchor calibration notes

**MOVED (B9 split, 2026-08-09)** — See [`drawer_memory_anchors.md`](drawer_memory_anchors.md)
for the full catalog of MMH-vs-GT override cases (丿/力/艹/... and per-Phase-3-char
notes through B6).

---


## B7-era retrieval hints (2026-08-08)

**B7 promoted 13 whole-char primitives** (4 A + 9 PASSes). Consult these
BEFORE inlining if your target char is one of these or in the reuse family:

| Char | File | Reuse family |
|------|------|--------------|
| 业 | `yi_ye.py` | 业, 邺, 亚 (sibling: baseline heng + top block) |
| 仟 | `qian_person.py` | 仟 identity; **L-R 亻+X 5-stroke template** — reuse anchors for 仔/什/仁/化/付/仕/仗/任 |
| 冉 | `ran.py` | 冉, 苒, 再 (frame + wide-piercing bar) |
| 乓 | `ping_pang.py` | 乓 (identity); 乒 (mirror s6) |
| 立 | `li_stand.py` | 立, 站, 位, 泣, 拉, 粒, 翌, 竖, 竣, 竟, 亲 top, 童 top, 章 top |
| 白 | `bai_white.py` | 白, 百, 伯, 柏, 怕, 拍, 泊, 珀, 迫, 皂, 皇, 皆, 泉 top, 的 left |
| 由 | `you_by.py` | 由, 抽, 油, 宙, 届, 邮, 袖, 轴, 笛 |
| 四 | `si_four.py` | 四 (identity), 泗, 驷 |
| 会 | `hui_meet.py` | 会, 绘, 桧, 侩, 烩, 荟 |
| 有 | `you_have.py` | 有, 侑, 宥, 贿, 郁, 囿, 洧 |
| 年 | `nian_year.py` | 年 (usually standalone; rarer as phonetic) |
| 自 | `zi_self.py` | 自, 息, 鼻, 臭, 嗅, 洎, 咱, 皋 (bottom) |
| 世 | `shi_world.py` | 世, 贳, 泄, 屉, 蝶 right, 揲 right |

### B7-era anchor calibration (per A / high-value PASS)

- **业 (B7 A, p3_char_0184)**: 2 tall central shus (widths 7) topped
  above baseline heng by 11-14 px (**N joints preserved**), outer
  dians as short slanted taper strokes (w_head=3, w_tail=7, bow=3).
  Baseline heng width_head=9, width_tail=11 (heaviest stroke — visually
  anchors the char).
- **仟 (B7 A, p3_char_0185)**: **L-R 亻+X template**. 亻 pie head
  (85, 61) → tail (14, 183) bow_perp=13; 亻 shu (67, 137) → (67, 278).
  Right radical 千 pie head (228, 78) → tail (124, 114) bow_perp=6;
  heng head (93, 173) → (276, 157); shu (163, 107) → (178, 298).
  Bypasses draw_ren_left in favor of MMH-anchor 1:1 stroke primitives.
- **仨 (B7 A, p3_char_0189)** — **NOT PROMOTED, but same template**:
  亻 inline at pie (92,68)→(14,203) bow=16, shu (68,157)→(70,296);
  三 hengs at right (100-270 x-range). Same P-A-006 recipe as 仟.
- **冉 (B7 A, p3_char_0201)**: heng_zhe_gou for s2 with heng_head
  (97, 125), corner (215, 122), gou_tail (215, 262), hook_tip
  (165, 279). s5 wide heng drawn LAST → overdraws s1/s2 for welded
  P-joints.
- **乓 (B7 A, p3_char_0224)**: 6 strokes, all N-gap joints. s2 (left
  long slant) uses bow_perp=**-4** (negative — arcs slightly left).
  s6 (final pie) tail (231, 303) intentionally runs off-canvas at BR.
- **立 (B7 PASS)**: top dian (124, 74) → (165, 98) w_head=3, w_tail=9,
  bow=4. Upper heng (81, 154) → (220, 135). 2 short slants (s3 down-
  right, s4 down-left) as tapered short lines (w_head=4, w_tail=9-10).
  Baseline heng (33, 273) → (271, 272) heavy.
- **白 (B7 PASS)**: top pie (132, 63) → (91, 143) bow_perp=10. Box:
  left shu (54, 144) → (86, 274) width=8; heng_zhe_box top_left=(69, 145),
  bottom_right=(204, 286). Inner: heng s4 (84, 202) → (182, 196) w=6/7;
  heng s5 (91, 256) → (192, 253) w=7/8. Cousin of 日 (`ri_sun.py`).
- **由 (B7 PASS)**: box + central shu that extends BOTH above and
  below the box. Left shu (52, 149) → (86, 281); heng_zhe_gou-shape
  (no hook, `hook_tip=gou_tail`) for top+right frame. Middle heng
  (101, 208) → (188, 200). Central shu (132, 63) → (140, 255) —
  extends past top by ~55 px, ends inside box just above bottom bar.
- **四 (B7 PASS)**: box + pie-inside-left + shu_zhe-inside-right + heng-seal.
  Inner marks are pie (s3) + shu_zhe (s4) — NOT two straight shus (that's
  田/由/甲). Sibling-pair caution: 四 vs 田 depends on inside shape.
- **会 (B7 PASS)**: 人-top (pie+na sweeps wide, spanning most of canvas
  width), then 云-body (2 hengs), then 厶-bottom (pie_zhe + dian).
  na tail reaches (290, 186) — near MR-cell edge. Bottom pie_zhe
  corner at (135, 268).
- **有 (B7 PASS)**: top heng + long pie crossing it (bow_perp=14) +
  月 inlined with heng_zhe_gou at RIGHT position (S4_HEAD=(128, 158),
  corner=(161, 158), gou_tail=(161, 286), hook_tip=(149, 279)). Do
  NOT scale down `draw_yue_moon` for the 月 sub-component; inline it
  at the right cell.
- **年 (B7 PASS)**: 6 strokes. Central shu (144, 104) → (156, 295)
  pierces both s3 (mid heng) AND s5 (bottom heng) as P-joints. Draw
  s6 LAST for overdraw weld. MMH tail was y=322 — CLAMP to y=295 for
  canvas.
- **自 (B7 PASS)**: pie-on-top + 白-body-with-extra-heng. Very close
  cousin of 白 (basically `bai_white.py` + one more middle heng).
  Top pie uses bow_perp=**-8** (negative — arcs right).
- **世 (B7 PASS)**: heng + 2 inner shus piercing it (P-joints via
  overdraw) + short bottom heng + outer 竖折 wrapping bottom-left.
  s5 shu_zhe corner at (77, 265) — pierces s1 in ML cell.

### B7 A-recipe playbook — P-A-006 quick reference

**When to apply**: 4+ stroke Phase-3 char, MMH block gives clean per-
stroke endpoint anchors, char has "grid-like" or "L-R" structure where
sub-components share alignment.

**Steps**:
1. Do NOT call whole-radical primitives (`draw_ren_left`, `draw_qian_thousand`,
   `draw_san_three`, etc.) even if they match your target.
2. Call **stroke-signature** primitives with MMH endpoints as
   `head`/`tail`/`corner` arguments **verbatim** (no override, no
   pixel translation).
3. Assign taper widths per stroke: outer/baseline strokes heavier
   (w_head/w_tail 8-11); interior strokes lighter (w_head/w_tail 6-8);
   dians thin-to-thick (w_head 3, w_tail 7-9).
4. For welded P-joints where a stroke pierces another, DRAW THE PIERCING
   STROKE LAST — the overdraw naturally welds. (Alternative to bow-forcing
   from P-A-005; simpler and works when anchors already provide the crossing.)
5. For N-joints (natural gaps at corners/near-touches), MMH anchors typically
   already give the correct gap — don't fudge.

**When NOT to apply**:
- 1-3 stroke identity chars — use P-A-001 (call whole-radical primitive).
- Chars with a compound stroke that requires bow-forcing to weld a
  crossing at the MMH anchor — use P-A-005 (negative-bow recipe).

### B7-era sibling notes

- **业 vs 亚 vs 亞**: 业 = 5-stroke as above. 亚 = 业 + top-heng
  (6-stroke); appears in B8 idx 234. 亞 is a rare traditional variant.
- **四 vs 田 vs 由 vs 甲**: 四 has pie-inside-left + shu_zhe-inside-right;
  田/由/甲 have straight shus inside. 由's central shu extends above box;
  甲's below; 田's stays inside.
- **白 vs 自 vs 百 vs 泉**: 自 = 白 + one extra middle heng. 百 = 一 top +
  白 body. All share the top-pie + box structure.
- **有 vs 冇** (rare): 有 = 一/丿/月; 冇 has hollow 月.
- **世 vs 卅 vs 廿**: 世 has 竖折 wrap at bottom; 卅 (idx 147, PASSed) is
  3 shus + heng; 廿 (rare) is a bracket-shape.
- **仟 vs 千 vs 干 vs 于**: 仟 = 亻+千. 千 has pie + heng + shu.
  干 = 2 hengs + shu. 于 = heng + short-heng + shu-hook.
- **冉 vs 再 vs 苒**: all frame-with-wide-piercing-bar. 冉 has central
  vertical shaft extending above top; 再 has an extra middle bar; 苒 =
  艹 + 冉.
- **乓 vs 乒 vs 兵 vs 丘**: 乒 mirrors 乓's s6 (bottom-left, not
  bottom-right descender). 兵 has 八 bottom (2 short slants) instead
  of the single descender. 丘 has NO bottom descender at all.
- **年 vs 甲 vs 早**: 年 has diagonal top pie + 2 hengs + shu piercing
  bottom heng. 甲 has box + central shu. 早 has 日 + 十.
- **会 vs 合 vs 令**: all 人-top + variant middle + bottom. 会 has 2
  hengs middle + 厶 bottom. 合 (idx 269) has 一 middle + 口 bottom.
  令 has heng middle + 龴 bottom.
- **X-cross cluster (P-COMP-010)**: 癶 (C), 矢 (PASS), 失 (PASS), 処
  (FAIL — 几 not X-cross), 乩 (PASS), 那 (FAIL — 阝 not X-cross).
  The X-cross weld itself PASSes reliably in G5 given MMH anchors;
  freezes cluster on OTHER components (chronic 几/阝 gaps).

### B7 failure calibration (for B8 sibling-char retries)

- **仡 (p3_char_0187 FAIL)**: 亻 (bank) + 乞 (inline 乙-body). Failure
  mode = 乞's bezier hook body mis-shaped. For 乞-family (乞/吃/吃) do
  NOT combine bank-left with inline-乞; if 乞 is right radical, apply
  P-A-006 (stroke primitives with MMH anchors for BOTH halves).
- **边 (p3_char_0188 FAIL)**: 辶+力 double-transform. See P-COMP-009.
  For 辶-wrap chars (这/进/近/远/道), apply P-A-006 for the wrapped
  component — inline `力/寸/元/艮` etc. rather than calling whole-radical.
- **东 (p3_char_0196 FAIL)**: BANK_DEVIATION on shu_gou-at-diagonal.
  The fresh `dong_spine_diagonal` composition didn't cohere. 东's s2 is
  MMH-median diagonal (dx=82, dy=143) not vertical — genuine bank gap
  for "diagonal-with-hook" primitive. If future PASS emerges, promote
  `xie_gou_hooked` or similar.
- **冎 (p3_char_0209 FAIL)**: rare-char; anchor cluster mis-interpreted.
  Do not retry.
- **处/処 (p3_char_0212/0213 both FAIL)**: chronic 几-hook + composition.
  処 explicitly BANK_DEVIATIONed for no-夂/no-几 bank. **Do not retry
  either** — same P-COMP-008 update as 乌/仇/仉/冗.
- **记 (p3_char_0214 FAIL)**: 讠+己 L-R. 己 needs heng_zhe_wan_gou
  compound (chronic gap). Do not retry until 己 gets a PASSing inline.
- **那 (p3_char_0233 FAIL)**: 冄+阝 6-stroke. Left 冄 was reasonable;
  right 阝 (via `draw_er_ear` ox-shifted) mis-positioned. For 阝-right
  chars (那/邦/郊/邻/郎/都/部/邮), consider promoting `er_ear_right.py`
  variant when a PASS attempt appears.

### B7 retry outcomes

- **发 R1 FAIL** (terminal-freeze) — P-A-005-style trajectory diff
  (negative-bow forcing) attempted; STILL FAILed. 发 top-heavy layout
  is proportion-level, not joint-geometry — no mechanism-change viable.
- **仗 R1 FAIL** (terminal-freeze) — shrunk 亻 (scale=0.85), extended
  丈 anchors right, negative-bow on pie. Pie/na crossing landed at
  wrong y. Same P-COMP-006 diagnosis.
- **用 R1 PASS** — moved s1 pie head from MMH-verbatim (72, 81) to
  (95, 82) so it shares top-left with box (per errata note "trust GT
  over MMH-median when > 40 px off centroid"). Bank primitives
  unchanged; **tuning-only retry PASS**.
- **必 R1 C** — deepened wo_gou belly, thickened dians. Improved but
  not PASS. Terminal-freeze.
- **付 R1 C** — thinned strokes, shifted s4 head right to force MR-cell
  crossing. Improved but not PASS. Terminal-freeze.
- **打 R1 C** — shrunk 扌 to scale=0.88, extended 丁 heng rightward.
  Improved but not PASS. Terminal-freeze.
- **比 R1 PASS** — sibling-pair discipline: rebalanced left/right 竖弯钩
  halves (bottom_extra 36/42), flipped right-pie bow_perp to -8 (per
  P-A-005), thickened 提. **P-RET-005 evidence**: retry PASS from
  applying existing sibling-pair note without new bank.

---

## B8-era retrieval hints (2026-08-09)

**B8 promoted 8 whole-char primitives + 1 stroke primitive**. Consult
these BEFORE inlining for their family or reuse targets:

| Char | File | Reuse family |
|------|------|--------------|
| 亚 | `ya_asia.py` | 亚 (identity), 恶, 垩 (sibling of 业 / `yi_ye.py`) |
| 后 | `hou_after.py` | 后, 逅, 垢, 姤 |
| 行 | `xing_walk.py` | 行 (identity), 街, 衍, 冲, 徽, 衔 |
| 多 | `duo_many.py` | 多 (identity), 名 (sibling top 夕), 岁, 够, 夜 |
| 同 | `tong_same.py` | 同 (identity), 铜, 桐, 洞, 筒, 峒, 侗 |
| 回 | `hui_return.py` | 回 (identity), 苘, 迴, 徊, 洄 |
| 问 | `wen_ask.py` | 问 (identity), 闷, 阔, 阗 |
| 合 | `he_together.py` | 合 (identity), 拾, 给, 塔, 蛤, 鸽, 恰, 洽 |

**Stroke primitive**:
- 横撇-slim (`heng_pie_slim.py`) — slimmer bow (~6) variant of `heng_pie.py`;
  for 夕-family (多/名/夜/岁), 又/欠 tuning. From 多's PASSing BANK_DEVIATION
  (2nd occurrence per P-COMP-002).

### B8-era anchor calibration

- **多 (p3_char_0245, PASS via BANK_DEVIATION)**: 2 stacked 夕. Each 夕 =
  pie + heng_pie_slim + dian. Key: `bow_perp≈6` on heng_pie (default 18
  is too fat for 夕's thin compact shape). Top 夕 sits in TC/ML; bottom
  夕 sits in C/BL. Small natural N-gaps between all 7 joints; do NOT
  weld.
- **同 (PASS)**: 冂 frame (heng + shu_zhe_gou-like right shoulder) +
  inner heng + inner 口. Use draw_kou for the inner mouth at
  approximately `ox=+40, oy=+95, scale=0.55`. Do NOT try to inline
  the 口.
- **回 (PASS)**: draw_wei_enclose (outer 囗) + inline 口 (inner) at
  approximately `ox=+60, oy=+75, scale=0.55`.
- **问 (PASS)**: draw_men_gate + inline 口 at `ox=+60, oy=+95, scale=0.5`.
- **合 (PASS)**: 人-top (pie+na wide) + heng + draw_kou (bottom mouth
  at `ox=+50, oy=+165, scale=0.60`). The 人-top spans nearly full canvas
  width; heng middle just below (~y=170); 口 bottom centered.
- **行 (PASS)**: L-R 彳+亍. 彳 = pie + pie + shu (3 strokes, left); 亍 =
  heng + shu (2 strokes, right) + short pie top. Both halves inline
  stroke-primitive (P-A-006) with 亻-style x-offset for left half.
- **亚 (PASS)**: sibling of 业. Structure = top heng + 业-body (4 strokes:
  2 shus + baseline heng + 2 short dians outside baseline). Could call
  draw_yi_ye + inline top heng — most drawers inlined all 6 in B8.

### B8-era sibling notes

- **亚 vs 业 vs 亞** (B8, refined): 亚 = 业 + top heng crown (6 strokes;
  crown longer than baseline). 业 alone (5 strokes) is `yi_ye.py`.
  亞 is a rare traditional variant (usually not dispatched).
- **多 vs 名 vs 岁 vs 夜** (B8): 多 = 2 stacked 夕; 名 = 夕 top + 口
  bottom; 岁 = 山 top + 夕 bottom; 夜 = 亠 top + 亻 left + 夕 bottom-right.
  All share the 夕 unit — use `duo_many.py`'s per-夕 anchor recipe (with
  heng_pie_slim) as the template.
- **同 vs 冋 vs 冂-family** (B8): 同 = 冂 + heng + 口 (6 strokes, inner
  口 sits in bottom half of frame). 冋 (rare) = 冂 + 口 only (no middle
  heng). 冈 = 冂 + 乂 inside. Distinguishing = what's inside the 冂.
- **回 vs 囗 vs 口 vs 日** (B8, nested-frames): 回 = double 口 (outer +
  inner, 6 strokes). 囗 = single big 囗 (3 strokes). 口 = single small
  口 (3 strokes). 日 = 口 + inner heng (4 strokes). MMH stroke count is
  the primary discriminator.
- **合 vs 令 vs 今 vs 龴** (B8): 合 = 人-top + heng + 口 (6 strokes,
  bottom 口). 令 = 人-top + heng + 龴 (5 strokes, bottom 龴 not 口).
  今 = 人-top + 龴 (4 strokes, no middle heng). Use `he_together.py`
  for 合; 令 goes inline.
- **行 vs 彳 vs 衍 vs 街** (B8): 行 = 彳+亍 (6 strokes, standalone).
  街 = 行 + 圭 in middle (12 strokes). 衍 = 行 + 氵 in middle (9
  strokes). 彳 alone is the left-3 strokes only. Bank has 行 for
  standalone; compose 街/衍/etc. via draw_xing + inline middle.

### B8 failure calibration (for B9 R1 retries / sibling chars)

**Cluster A — 亻+X hook-compound right (do NOT retry per P-COMP-011)**:
- **伄 (亻+吊 — 冂+巾 with hook)**: right radical has hook_compound;
  no mechanism-change available. Chronic gap family.
- **伉 (亻+亢)**: 亢 needs shu_wan_gou tuned for wide bottom (per B5 note);
  drawer attempted; still FAILed. Composition-level.
- **伎 (亻+支)**: 支 = 十 top + 又 bottom. 又 has heng_pie which welds
  awkwardly with 亻 shu. Composition proportion issue.
- **伙 (亻+火)**: 火's pie-dian ordering wants specific 4-stroke topology;
  P-A-006 inline doesn't capture.
- **伢 (亻+牙)**: 牙 has heng_zhe compound + shu_gou; bank gap.
- **伧 (亻+仓)**: 仓 has 人-cover + top wraparound; bank gap.
- **佤 (亻+瓦)**: 瓦 wave-hook — chronic gap, P-COMP-008 refuted.

**Cluster B — whole-radical refusal FAILs (queue for B9 R1 per P-A-007)**:
- **军 (冖+车 = 2+7 strokes; MMH gives 6 combined)**: drawer inlined all
  6; NEVER used `draw_mi_cover` or `draw_che_car`. **Retry with bank
  primitives** — `draw_mi_cover(d, ox=0, oy=-40, scale=0.9)` top +
  `draw_che_car(d, ox=0, oy=+40, scale=0.75)` bottom.
- **名 (夕+口)**: drawer inlined all 6; NEVER used `draw_kou`. **Retry
  with `draw_kou(d, ox=+30, oy=+65, scale=0.65)` for bottom + inline 夕
  top** (or use new `duo_many.py`'s per-夕 pattern for the top).
- **成 (5-stroke 戈-piercing)**: drawer inlined; did NOT use
  `draw_ge_dagger`. **Retry with draw_ge_dagger as 戈 base + inline
  piercing shu at MMH crossing.**
- **西 (frame + inner)**: drawer inlined 6; did NOT identity-call
  `draw_si_four`. **Retry with `draw_si_four` as base** — 西 differs
  from 四 by inner shu_zhe direction; diff inner marks vs MMH.

**Cluster C — chronic-freeze (terminal-freeze)**:
- **亥 (idx 236)**: G4-frozen chronic; interlaced hook body.
- **色 (idx 279)**: 巴 heng_zhe_wan_gou chronic gap.
- **传 (亻+专 idx 283)**: 专 curl-hook chronic gap family.

**Cluster D — 女-inline (queue 好 R1 per P-A-007; do-not-queue 如)**:
- **好 (女+子)**: drawer inlined `nu_left_compressed` fresh_component;
  could have called `draw_nu_woman(d, ox=-40, oy=0, scale=0.75)` (bank
  since B3 R2) + inline 子 (子 chronic gap on right). **Retry with
  bank 女**.
- **如 (女+口)**: same P-A-006 refusal of `nu_woman.py`; would benefit
  from same treatment BUT 如 also has 口 on right which is fine —
  drawer's 女-inline was the problem. Marginal retry candidate; queue
  as MEDIUM only if capacity.

**Cluster E — hook-body full-char**:
- **仰 (亻+卬)**: 卬 heng_zhe descender proportion off. Composition-level.
- **老 (top+匕 bottom, 6 strokes)**: shu_wan_gou default params
  (bottom_extra=60, knee_ratio=0.75) too compact for 老's wide bottom.
  **Retry with `shu_wan_gou(bottom_extra=75, knee_ratio=0.62)` per
  P-RET-004** (same tuning as 也 in B4 note).
- **再 (frame + wide piercing bar)**: drawer adapted from `ran.py`
  (冉 A). Close. **Retry with refined adaptation** — 再's central bar
  extends past frame's right side by ~10 px more than 冉's.

### B8 A-drought interpretation (see also principle_bank STRUCTURAL A CEILING)

B8 delivered 0 A verdicts on 20 PASSes. Sample of 3 PASSes shows P-A-006
discipline intact (仲/多/次 all have explicit taper per stroke, MMH-verbatim
anchors, correct N-joint gap preservation). The 0-A is **NOT a drawer
discipline collapse**. Fair-A comparison shows G4 got 10 A on identical
items using per-endpoint `fat_line` width control; G5's uniform PIL line
width is the ceiling. On 6-stroke chars without headroom, G5 tops out at
PASS. This is a STRUCTURAL A CEILING that curator should NOT diagnose as
regression. Future curators: if 0-A, sample 3 PASSes; if discipline intact,
move on.


## B9-era retrieval hints (2026-08-09, position 518)

**B9 promoted 12 whole-char primitives** (4 A + 3 R1 P-A-007 + 5 high-reuse
mains). Consult these BEFORE inlining if your target char is one of these
or in the reuse family:

| Char | File | Reuse family / notes |
|------|------|----------------------|
| 龹  | `juan_yong.py` | RARE. NOVEL top-radical with bent-pie A-recipe (bezier through 2 P-joints). Extends to 龸/巻/眷/券/勝 family. |
| 还  | `hai_still.py` | 辶+X wrap template (A-recipe). Reuse for 这/进/远/近/追/送/边/达. Calls `draw_chuo_walk` for 辶, inlines 不-half. |
| 位  | `wei_position.py` | 亻+立 template (A-recipe via P-A-007 clause 2). Extends to 竝/竟/章-family + any 亻+X where X = 立-family. |
| 伾  | `pi_flourish.py` | 亻+丕 template. Records the "reject draw_ren_left when MMH pie head is higher than baked" clause-2 pattern. |
| 军  | `jun_army.py`  | 冖+车 wrap (P-A-007 validation). Reuse for 冠/冢/冥/冤. Calls draw_mi_cover + draw_che. |
| 老  | `lao_old.py`   | 耂+匕 template. Reuse for 考/耆/耊/孝. Records shu_wan_gou tuning (bottom_extra=32, knee_ratio=0.72). |
| 成  | `cheng_become.py` | 5-stroke xie_gou-family (成/戏/咸/威/戌). Records xie_gou tuning (bow=14, hook_up=36, hook_back=8). |
| 来  | `lai_come.py`  | Central-spine template (未/末/朱/木-family compounds). Horizontal + 2 mirror dians + horizontal + spine + pie + na. |
| 里  | `li_inside.py` | 日+土 stack template. Reuse for 量/重/野/黑. Central 竖 pierces 3 hengs (3 P-welds). |
| 时  | `shi_time.py`  | 日+寸 L-R template. Reuse for 村/衬/対-family. shu_gou hook_start_offset=32. |
| 作  | `zuo_make.py`  | 亻+乍 template (P-COMP-011 clean straight-stroke right). Also useful for 咋/怎/炸/昨. |
| 但  | `dan_but.py`   | 亻+旦 template. 旦 sub-structure (日 box + long bottom heng) also useful for 亘/宣. |

**Reuse-target map for B10 idx 334-383** (predict which promoted primitives
will apply):

- 亻+X L-R chars: check if X is straight-stroke (→ use zuo_make/dan_but/wei_position
  as sibling template) or hook-compound (→ Cluster A do-not-queue per P-COMP-011/012).
- 日+X or 田+X compounds: consult `li_inside.py`, `shi_time.py`, `dan_but.py`
  for the 日-box + right-side render pattern.
- 辶-wrap chars: template = call `draw_chuo_walk` for 辶 + inline the enclosed
  radical per MMH anchors. Reference `hai_still.py`.
- 冖+X wrap chars: template = call `draw_mi_cover` + underlying radical.
  Reference `jun_army.py`.
- Any char containing 立: consult `wei_position.py` for the aspect-skewed 立
  render + P-A-007 clause-2 reasoning.

## B9-era rules of thumb (P-A-007 sharpened, P-A-008 mandatory)

1. **Before inlining any sub-component**: ask "does a bank whole-radical
   primitive match this sub-component's structural identity? If YES, does
   it sit at scale ∈ [0.55, 1.2]? If both YES, CALL the bank primitive."
   This is P-A-007-v2 hard-check.

2. **Docstring must record per-sub-component decision**: for each sub-component
   name it, state whether a bank whole-radical matches, and if it does,
   either call it OR justify inlining with an aspect/scale reason. Silent
   inlining where bank primitive exists is a bug (P-A-008).

3. **P-A-007 clause-2 fallback is common and correct**: if the bank primitive
   would double-transform (aspect skew, MMH endpoint doesn't match baked
   geometry, sub-component severely compressed < 0.55 scale), fall back to
   P-A-006 stroke-primitive layer. But WRITE THE REASONING in the docstring.

4. **辶-wrap has a stable template**: draw_chuo_walk at native scale
   (with small ox/oy shift if MMH targets differ from bank) + inline the
   enclosed radical. Do NOT inline the 辶 unless the wrap is severely
   compressed. See `hai_still.py`.

5. **Central-spine template (来-family)**: when a Phase-3 char has a
   dominant central vertical crossing multiple hengs, use the
   `lai_come.py` reference: shu spans full height, hengs cross at P joints,
   symmetric side strokes (dians + pie/na pair).


## B10-era retrieval hints (2026-08-09, position 568)

**B10 promoted 16 whole-char primitives** (7 A + 9 high-reuse PASSes).
This is the largest single-batch bank growth. Bank now at 152 primitives
(22 stroke + 130 radical/char).

**Whole-char primitives from B10 A verdicts:**

| Char | File | Reuse family / notes |
|------|------|----------------------|
| 佔  | `zhan_occupy.py` | 亻+占 A-recipe. 占-family extends to 沾/粘/店/贴/砧/苫. Records BANK_DEVIATION on bu_divine + kou_mouth (both aspect-skew per P-A-009). |
| 佟  | `dong_person.py` | 亻+冬 A-recipe. 冬 sub-template extends to 终/疼/腾/图. P-A-006 pure. |
| 佥  | `qian_all.py`   | Rare; retained as A-recipe record for small-pie/dian variants. |
| 的  | `de_target.py`  | **HIGHEST-freq char in Chinese**. 白+勺 A-recipe with 2 BANK_DEVIATIONs (P-A-009 quantitative). |
| 並  | `bing_and.py`   | 8-stroke sibling of 亚/业. Records stroke-count-mismatch BANK_DEVIATION (P-A-007-v2 for stroke-count). |
| 和  | `he_harmony.py` | **HIGH freq**. 禾+口 A-recipe. 禾 sub-template extends to 秋/秒/科/秤/秘/税/秃/穗/程/租/穆. |
| 些  | `xie_some.py`   | 此+二 (triple BANK_DEVIATION). 此-top pattern extends to 柴/紫/呰. |

**Whole-char primitives from B10 high-reuse PASSes:**

| Char | File | Reuse family / notes |
|------|------|----------------------|
| 花  | `hua_flower.py` | 艹+化 wrapper — HIGH REUSE. Extends to any 艹+X (草/苗/苦/苹/茶/蓝/菜/著). |
| 国  | `guo_country.py`| 囗+玉 — VERY HIGH REUSE. Any 囗+X compound (图/困/固/圆/园/围). |
| 者  | `zhe_person.py` | 耂+日 — VERY HIGH REUSE. 都/署/著/煮/暑 family. |
| 法  | `fa_law.py`    | 氵+去 — VERY HIGH REUSE. Any 氵+X (河/海/江/清/游/汉/洗/汽/波). |
| 定  | `ding_fix.py`  | 宀+疋 — VERY HIGH REUSE. 宿/宁/它/宅/守/宇 (宀-top calibration). |
| 证  | `zheng_prove.py`| 讠+正 wrapper. Any 讠+X (说/话/讲/询/记/让/请). |
| 找  | `zhao_seek.py` | 扌+戈 wrapper. Any 扌+X (打/把/接/拿/挂/推) + 戈-family L-R. |
| 所  | `suo_place.py` | 户+斤 — 户 top (房/扇/雇), 斤-family (析/新/斧/欣). |
| 志  | `zhi_will.py`  | 士+心 — 心-bottom family (忠/念/思/急/怒/怎/怨/恨/悲). |

**Reuse-target map for B11 idx 384-433** (predict which promoted
primitives will apply):

- 亻+X L-R chars: consult zhan_occupy (亻+占 with hook right) as
  precedent for P-A-006 with BANK_DEVIATION when right-half compound
  strokes exceed aspect band. Also dong_person for 冬-family right.
- 禾+X compounds (秋/秒/科/秤/程/租): use he_harmony's 禾-side coords.
- 艹+X compounds (any 花/草/茶): call draw_hua_flower's cao layer +
  underlying primitive.
- 氵+X compounds (any 河/海/江): use fa_law's 氵-side coords.
- 讠+X compounds: use zheng_prove template.
- 扌+X compounds: use zhao_seek template.
- 心-bottom compounds: use zhi_will's 心 (wo_gou + 3 dian) coords.
- 宀-top compounds: use ding_fix's 宀 (dian + pie + heng_zhe_short).
- 囗-enclosed compounds: use guo_country's inset spacing.

### B10-era sibling notes

- **佔 vs 沾 vs 粘 vs 占**: all share 占 sub-component. 占 = 卜 top +
  口 bottom (5 strokes). When occurring inside a L-R compound, 占's
  inner 口 tends toward near-square aspect (bank kou_mouth landscape
  fails aspect check). Use zhan_occupy's inline 口 coords.
- **和 vs 秋 vs 秒 vs 秃**: all share 禾 left. 禾 = 撇 + 横 + 竖 + 撇 + 捺
  (5 strokes). In L-R compounds, 禾's 竖 spans nearly full height, and
  下-half 撇/捺 splay wide. Reference he_harmony's 禾-side coords.
- **法 vs 沙 vs 河 vs 汉**: all share 氵 left with 3-stroke pattern
  (2 dians + ti). fa_law records the canonical 氵 x-positions for
  L-R compounds — reuse for any 氵+X where X occupies right ~60%.
- **定 vs 宿 vs 宁 vs 宅**: 宀 top calibration comparable. In 定,
  the 宀 dot sits at TC(0.28, 0.53); pie starts C(-0.33, 0.06); heng
  extends across ~60% width. Reference ding_fix's coords.

### B10 failure calibration (for B11 R1 retries / sibling chars)

**Cluster A — 疒-family bank gap (all terminal-freeze)**:
- 疙, 疟, 疠, 疝, 疌 all FAILed at 疒 inline. No bank primitive; do
  NOT retry until a passing 疒-composition surfaces organically.

**Cluster B — 亻+X (some retry-eligible)**:
- **佚** (亻+失, X-cross right) — 亻 correctly bank-called; 失 inline.
  Terminal-freeze — no P-A-007 mechanism-change for 失 (no whole-radical).
- **社** (礻+土) — drawer refused both shi_spirit and tu_earth per
  aspect/scale. **B11 R1 P-A-007 candidate**: quantitative recheck —
  礻 target width 175 vs bank 155 = 1.13× (INSIDE window); recall
  P-A-007-v2 says CALL bank. Queue with instruction.
- **佛** (亻+弗 — hook-compound right; do-not-queue per P-COMP-011).
- **即** (皀+卩 — 皀 no bank; do-not-queue).
- **佞** (亻+二+女, 3-part). Drawer DEVIATIONed both nu_woman and er_two.
  **B11 R1 P-A-007 candidate**: quantitative recheck — 女 pie head
  ratio 108/137 = 0.79 (INSIDE); 二 sep ratio 1.50 (compared to bank
  1.80 = 0.83 — INSIDE window). Both should have been CALLED per
  P-A-007-v2. Queue with instruction.

**Cluster C — novel 8-stroke compositions**:
- **事, 乖, 乶** — unique layouts, no decomposition; do-not-queue.
- **畅** — 甲/申 left. **B11 R1 MEDIUM**: try draw_you_by (由) as base
  with s5 shu extension for 申's top overshoot vs 由's compact top.
- **经** (纟+圣). B11 R1 MEDIUM: try inline 纟 + call you_again 又 +
  tu_earth 土 (both in bank) for right-half.

### B10 A-batch verification (P-A-008 discipline holding)

7 of 7 B10 A-verdict docstrings contain per-sub-component P-A-007-v2
hard-check reasoning (either "called bank because aspect matches" or
"BANK_DEVIATION because aspect X vs bank Y = ratio Z, outside window").
4 of 7 have QUANTITATIVE aspect/scale numbers in the BANK_DEVIATION
reason (new principle P-A-009). This is the highest A count on
compound chars (6-8 strokes) in G5's history and validates B9's
P-A-008 codification. Discipline is holding.


## B10-era rules of thumb (P-A-009 quantitative BANK_DEVIATION added)

1. **P-A-007-v2 hard-check remains mandatory** (from B9). Ask "does a
   bank whole-radical match? Is scale in [0.55, 1.2]? Is aspect skew
   in [0.83, 1.20]?" Call bank if YES to both.

2. **P-A-008 reasoning trace remains mandatory** (from B9). Every
   compound-char docstring names each sub-component and states the
   bank vs inline decision.

3. **NEW P-A-009 quantitative BANK_DEVIATION** (from B10): if you
   BANK_DEVIATION, the reason MUST include numeric aspect/scale/
   endpoint deltas — not qualitative claims. Compute native bbox +
   target bbox, report ratios. If ratios inside window, cancel the
   DEVIATION and CALL the bank primitive.

4. **B10 reveals P-COMP-011 not as strict as B8 stated**: hook-compound
   right halves CAN reach A when hook lives inside a stroke primitive
   at usable scale (see zhan_occupy 亻+占, dong_person 亻+冬). Do NOT
   auto-DEVIATION on hook-compound; run P-A-007-v2 hard-check first.

5. **疒-family terminal-freeze**: do NOT attempt to build a 疒 primitive
   without an organic PASS. All 4 B10 疒-family FAILs used consistent
   inline; the inline recipe doesn't cohere calligraphically.

---

## B12-era retrieval hints (2026-08-09, position 668)

### New whole-char primitives promoted (10 A verdicts + 1 R1 A)

Consult these when you see a matching item in future batches. The wrapper
is directly callable; the inline templates are attempt-file recipes to
read and adapt.

| Char | Wrapper | Attempt-file template | Reuse target |
|------|---------|-----------------------|--------------|
| 神 shén | `shen_god.py`: `draw_shen(d, ox, oy, scale)`, `draw_shen_left_hemisphere(d, ox, oy, scale)` | `attempts/p3_char_0463_神/generated.py` | Any 礻-left compound — call `draw_shen_left_hemisphere()` for the 礻 half at compound-shifted anchors (社/祈/福/祝/礼) |
| 面 miàn | — (inline template) | `attempts/p3_char_0443_面/generated.py` | 面 / 緬 / 麵 — 9-stroke frame with all-N joints |
| 点 diǎn | — (inline template) | `attempts/p3_char_0445_点/generated.py` | 占-top compounds (店/占) + 灬-bottom compounds — 3 whole-radicals with per-radical quant BANK_DEVIATION |
| 信 xìn | — (inline template) | `attempts/p3_char_0447_信/generated.py` | 亻+言-family (誠/請/謝/認/訪) — ren_left called, 言 inlined (dian + 3 hengs), 口-flat DEVIATIONed |
| 美 měi | — (inline template) | `attempts/p3_char_0449_美/generated.py` | 羊-top compounds (羚/差/群/善/羞) — 羊 6 strokes + 大-compressed-flat DEVIATION |
| 盃 bēi | — (inline template) | `attempts/p3_char_0466_盃/generated.py` | X+皿 vertical stacks — **Archetype-2 template stack**: 不 (0094) + 皿 (0195), NO BANK_DEVIATION |
| 盅 zhōng | — (inline template) | `attempts/p3_char_0468_盅/generated.py` | X+皿 vertical stacks — 中 (0100) + 皿 (0195) stack pattern |
| 俅 qiú | — (inline template) | `attempts/p3_char_0476_俅/generated.py` | 亻+求-family (球/救/裘/球) — 亻 DEVIATIONed for compound-left, 求 7 strokes inlined |
| 俎 zǔ | — (inline template) | `attempts/p3_char_0482_俎/generated.py` | 且 sub-pattern for 助/組/宜/查 — 仌 (pie+dian×2) + 且 (shu+heng_zhe_box+3 hengs) |
| 草 cǎo | — (inline template) | `attempts/p3_char_0483_草/generated.py` | 3-band vertical compounds (艹+X+Y) — 艹 + 日 + 十 all DEVIATIONed on band-break aspect >2.1× |
| 实 shí (R1 A) | — (inline template) | `attempts/p3_char_0393_实__retry_1/generated.py` | **CRITICAL**: for compressed-宀 compounds, call `mian_roof(d, scale=0.85)` (NOT default scale=1.0); documented in B12 R1 A |

### B12-era rules of thumb (P-A-010-v2)

1. **P-A-010-v2 STRICT: "What single object gets changed?"** Before
   queueing an R1 or before writing a BANK_DEVIATION block, ask
   yourself this question:
   - ONE bank primitive gets called (was skipped) → kind (a) ✓ safe
   - ONE bank primitive's parameters/scale change → kind (b1) ✓ safe
   - ONE stroke's endpoints move to fix visual problem → kind (b1) ✓ safe
   - Gap/weld/alignment BETWEEN two sub-components changes → kind (d) ✗ dangerous
   - Multiple independent sub-components need DEVIATION with correct
     math → kind (e) ✗ dangerous

2. **P-A-007-v2 tolerance is ~15px for uniform-shift**. If your
   BANK_DEVIATION reason says "systematic left-shift of ~70 px" — that
   IS uniform-adjustable (just set ox=-70). Do NOT skip the primitive
   for pure translation. Check the head/tail shifts:
   - If differential <= ~15px → uniform-adjustable → CALL primitive.
   - If differential > 15px → non-uniform → DEVIATION justified.
   Example B12 failure pattern: 侯/便/俊 all cited ~70px uniform shift
   as reason to skip ren_left → WRONG. Diff for 侯 was 7.3px (head
   -72.7 vs tail -65.4) — well inside tolerance.

3. **Two A-recipe archetypes in B12**:
   - Archetype 1 — **DEVIATION-heavy inline** (7/10 B12 A's): drawer
     BANK_DEVIATIONs whole-radical primitives with quantitative math,
     inlines from stroke primitives at MMH anchors. Requires strong
     P-A-009 quant discipline.
   - Archetype 2 — **bank-template-stack** (3/10 B12 A's — 盃/盅/俎):
     drawer stacks two prior-passing inline templates with NO
     BANK_DEVIATION. Bank-critical-mass enables this route when both
     halves have prior templates.

4. **Compound-context 亻 (亻+X patterns)**: when 亻 shifts left in a
   compound, check the differential (pie shift vs shu shift). If small
   (≤15px), CALL ren_left with ox=-N. If genuinely non-uniform (differing
   compressions), DEVIATION and inline. **Do NOT default to DEVIATION**
   just because the shift number looks large.

5. **compressed-宀 recipe**: for any 宀-top compound (家/客/寒/宾/宽/实),
   call `mian_roof(d, scale=0.85)` NOT the default scale=1.0. Validated
   by 实 R1 A. Default scale renders 宀 too tall for compressed-top
   compositions.

6. **Bank-template-stack archetype**: when a compound is X-top + Y-bottom
   (vertical stack), scan for prior templates for BOTH halves. If both
   exist and neither needs BANK_DEVIATION, straight-stack them (盃/盅
   pattern). This is the LOWEST-effort A path.

7. **Do NOT bank-push for 疒**: 9 cumulative 疒-family FAILs. Terminal-freeze
   holds; wait for organic PASS (unlikely; consider stroke primitive
   layer only).
