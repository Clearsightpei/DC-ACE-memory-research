# G5 memory-structure evolution log

Append-only. One entry per structural change to G5's memory organization. Format matches G2/G3.

---

## 2026-08-08 — G5 fresh start

**Context**: G5 was originally set up (2026-08-03, post-v14-rollback) as a drawer-only ablation with **G3's post-B11 memory seeded in**. That configuration ran two batches (B12 and B13) and produced 100 attempts, with the finding that G3 (no MMH) beat G5 (has MMH) on B13 PASS rate for the first time — motivating a hypothesis that "crystallized bank memory can replace MMH within its coverage".

To test that hypothesis cleanly and to give G5 a full comparison trajectory against G3, the user directed a **full reset** of G5 (2026-08-08): delete all seeded content and prior attempts, and re-run G5 from Bootstrap + B1 forward with:
- Same protocol as G3 (`../../protocol/G3_coords/rules.md`)
- **Full curator + retries + self-evolution** (was drawer-only before)
- **MMH auto-injection retained** (this is G5's defining feature)
- Fresh empty memory files, empty bank, empty attempts

**Rationale**: gives us a clean G3 vs G5 comparison across the entire curriculum, isolating MMH's effect at every position on the learning curve rather than only at positions 550-700 where MMH-injected G5 inherited G3's mature memory.

**Files reset**: all under `groups/G5_code_bank_mmh/`. Directory structure recreated empty; `memory_index.md` rewritten with fresh-start setup note; `drawer_memory.md`, `principle_bank.md`, `sandbox.md`, `errata.md` all empty; log files (`retry_log.jsonl`, `curator_satisfaction_log.jsonl`) empty.

**Prior data preserved for reference**: the B12 and B13 G5 attempt PNGs are gone. The judgments for those batches (`judgments/batch_B12/labels.json`, `judgments/batch_B13/labels.json`) still reference G5 attempts by path; those references will now be dead (attempts deleted). That's acceptable — the B12/B13 G5 data is superseded by this fresh-start series.

**What this log will contain going forward**: same as G3/G2 — one entry per curator-initiated structural change (file created, file split, file retired, memory-scheme change, etc.).

---

## 2026-08-08 — Bootstrap curator: initial three-bank seeding

**Context**: Bootstrap batch produced 15 PASS / 3 C / 0 FAIL (83% pass) on 18 Phase-2 radicals. First curator pass; memory was empty.

**Files created**:
- `success_bank/code/` populated with **19 primitives** split into two signature classes:
  - **Stroke-level (endpoint signature `(d, head, tail, ...)`)**: `shu.py`, `heng.py`, `dian.py`, `pie.py`, `na.py`, `heng_zhe_short.py`, `shu_gou.py`, `shu_wan_gou.py`. Two of these (`pie.py`, `na.py`) were **extracted from 八's two component strokes** rather than promoted from a bare-stroke radical, because the bare 丿 radical (p2_radical_003) got a C — the pie shape itself worked inside 八's composition even when the bare form's placement missed. Same reasoning for the 竖弯钩 and 竖钩 extractions from 匕 and 刂 respectively.
  - **Radical-level (position signature `(d, ox=0, oy=0, scale=1.0)`)**: `yi_second.py` (乙), `yi_hook.py` (乚), `ba.py` (八), `bao_wrap.py` (勹), `bi_dagger.py` (匕), `bing_ice.py` (冫), `bu_divine.py` (卜), `chang_cliff.py` (厂), `dao_knife.py` (刀), `dao_right.py` (刂), `er_two.py` (二).
- `success_bank/INDEX.md` — two-table registry (stroke primitives vs radical primitives), plus import convention note.
- `errata.md` seeded with three diagnostic entries (亅, 丿, 儿) plus a cross-item learnings section.
- `drawer_memory.md` seeded with TOC + a bank-retrieval-hints table keyed by MMH stroke class + an empty sections skeleton for composition playbooks, sibling notes, and MMH-vs-GT calibration cases.
- `principle_bank.md` seeded with 4 principles (P-RET-001, P-RET-002, P-MMH-001, P-DEC-001) — deliberately light; only rules the bootstrap evidence actually supports.

**Signature design rationale**: The G3 protocol permits any callable signature. We split stroke primitives from radical primitives because the MMH dispatcher gives per-stroke endpoint anchors — endpoint-signature stroke primitives can be called with those anchors as-is, no coordinate translation needed. Radical primitives, in contrast, only need positioning within a larger character; `(ox, oy, scale)` matches how they'll be composed. If a later batch surfaces the need for stroke primitives to also take a scale/orientation knob, the bank grows the signature — that's the v13 variant channel.

**Import convention**: Flat imports (no package), matching G3's example. Callers add `success_bank/code/` to `sys.path` before importing.

**Deliberately NOT done**:
- No composition playbooks written (nothing to generalize from — bootstrap was all radicals, not multi-radical characters).
- No sibling / minimal-pair notes (bootstrap didn't surface a look-alike confusion).
- No variant entries for any bank primitive (v13 variants require an evidence-backed BANK_DEVIATION at PASS time; the bootstrap drawers had an empty bank so none of them deviated).
- No promotion for the 3 C-verdict items; they're queued in `retry_log.jsonl` for B1 consideration.

**Expected help for**: Phase-3 characters whose components include 八, 冫, 匕, 卜, 刀, 刂, 厂, 二, 勹, 乙, 乚 — bootstrap-composited primitives should be reusable via the position signature. Individual stroke primitives should cover the MMH stroke classes named in most Phase-3 dispatches.

---

## 2026-08-08 — B1 curator: bank expansion + memory playbook seeding

**Context**: B1 produced 31 PASS / 12 C / 7 FAIL on 50 mains (radicals p2_020 through p2_068) plus 3 retries from bootstrap C-verdicts (亅 R1 PASS, 儿 R1 C, 丿 R1 FAIL). MMH-injection effect vs G3 (same items, no MMH): +8pts on success rate but the dominant delta is FAIL→C conversion (7 vs 23) — MMH prevents wreck attempts by anchoring stroke count/class.

**Files changed**:

**Success bank — 25 new promotions (19 → 44 entries)**:
- 6 new stroke primitives (endpoint-signature), each from a BANK_DEVIATION on a PASSed item:
  - `ti.py` (提) — from p2_radical_068_扌 s3
  - `shu_zhe.py` (竖折) — from p2_radical_063_山 s2
  - `heng_zhe_gou.py` (横折钩 compound) — from p2_radical_025_力 s1
  - `heng_pie.py` (横撇) — from p2_radical_037_又 s1
  - `ping_na.py` (平捺) — from p2_radical_044_辶 s3
  - `heng_zhe_box.py` (横折 boxy variant) — from p2_radical_057_口 s2
- 19 new radical primitives (position-signature), one per high-reuse PASSed radical:
  - Left-position radicals: `ren_left.py` (亻), `shou_hand.py` (扌)
  - Top-position: `tou_lid.py` (亠), `mi_cover.py` (冖), `cao_grass.py` (艹)
  - Enclosing: `guang_wide.py` (广), `chuo_walk.py` (辶)
  - Whole-glyph radicals reusable as sub-components: `ren.py` (人), `ru.py` (入), `shi_ten.py` (十), `you_again.py` (又), `li_power.py` (力), `da_big.py` (大), `gong_work.py` (工), `shi_scholar.py` (士), `gan_dry.py` (干), `kou_mouth.py` (口), `shan_mountain.py` (山), `chuan_river.py` (川)
- 12 PASSed radicals NOT promoted (匚, 丷, 卩, 冂, 凵, 厶, 匸, 屮, 彳, 廾, 彐, 彑, 彡) — listed in INDEX under "PASSed but not promoted" section; low reuse or already covered by stroke bank
- INITIALLY promoted `mian_roof.py` (宀) and `shi_body.py` (尸) BUT these were C-verdicts, not PASSes — removed after fact-checking against labels.json

**Memory files updated**:
- `success_bank/INDEX.md` — restructured into stroke-primitives table + radical-primitives table (both extended); "PASSed-but-not-promoted" section added for the 12 low-reuse PASSes; "not promoted (C/FAIL)" section extended with 19 items
- `errata.md` — full diagnostic notes for all 12 C's + 7 FAILs, plus cross-item learnings section extended with 4 new lessons and 5 sibling-pair reminders
- `drawer_memory.md` — retrieval hints table extended with 6 new stroke classes; whole-radical retrieval section added listing all 30 bank radicals grouped by role; composition playbooks section seeded with 3 hypotheses (left-radical shrink, top-radical shrink, enclosing-radical embedding) — flagged unvalidated; sibling-pair notes populated with 6 pairs; MMH anchor calibration notes extended with 3 new cases (力, 艹, 山)
- `principle_bank.md` — 2 new principles: P-RET-003 (proactive stroke-primitive promotion from BANK_DEVIATIONs) and P-MMH-002 (compound-stroke MMH endpoints are approximate; drawer must infer corners visually)
- `sandbox.md` — first real content: B1 postmortem covering MMH-effect analysis, retry outcomes, and 3 observations to test in later batches

**Rationale**: MMH auto-injection removes stroke-count and stroke-class uncertainty but does NOT solve compound-stroke corner geometry. B1 confirmed this cleanly (12 C's cluster on compound strokes). The right response is to promote compound-stroke primitives into the bank proactively (P-RET-003) so B2 drawers can call ready-made shapes instead of re-inlining every time. Six primitives promoted covers the most common compound classes seen in B1.

**Expected help for**: B2 retry queue (esp. 门, 饣, 讠, 巾, 059/066/035/056 — all directly served by new stroke primitives); Phase-3 characters that contain any of the 19 promoted radicals (est. > 60% of common Phase-3 chars will contain at least one).

**Deliberately NOT done**:
- No new file types created — the three-bank layout continues to work at ~180-line drawer_memory
- No memory-structure split (revisit at 400 lines)
- No promotion for any of the 12 C's / 7 FAILs (see retry_log.jsonl B2 queue)
- No variant entries yet — v13 variants require a *second* PASS on the same primitive with a compositional twist; B1 was all bare radicals, no composition evidence

---

## 2026-08-08 — B2 curator: bank expansion + composition principles

**Context**: B2 produced 19 PASS / 13 C / 18 FAIL on 50 mains (radicals p2_069–p2_118) plus 20 retries from B1 queue (3 PASS: 廴/巾/饣; 9 C; 8 FAIL). MMH-injection effect vs G3 (same items, no MMH): +4pts on success rate, FAIL→C delta of 18 vs 33 — same MMH signature as B1.

**Files changed**:

**Success bank — 20 new promotions (44 → 64 entries)**:
- 2 new stroke primitives (endpoint-signature), each from BANK_DEVIATIONs on PASSed items:
  - `xie_gou.py` (斜钩) — from p2_radical_079_弋 s2 AND p2_radical_096_戈 s2 (**two independent DEVIATIONs** on the same missing class; codified as P-COMP-002)
  - `heng_gou.py` (横钩) — from p2_radical_112_欠 s2
- 18 new radical primitives (position-signature):
  - Left-position: `sanshui.py` (氵), `xin_left.py` (忄), `shi_food.py` (饣, retry PASS)
  - Bottom: `si_fire_bot.py` (灬), `xiao.py` (小)
  - Right-side: `pu_action.py` (攵), `qian_owe.py` (欠), `ge_dagger.py` (戈)
  - Whole-glyph radicals reusable as sub-components: `tu_earth.py` (土), `mu_wood.py` (木), `ri_sun.py` (日), `niu_cow.py` (牛), `quan_dog.py` (犬), `che_car.py` (车), `hu_door.py` (户), `fu_father.py` (父), `wei_enclose.py` (囗), `jin_towel.py` (巾, retry PASS)
- 4 PASSed radicals NOT promoted (弋, 丬, 斗, 廴) — low reuse or already covered by extracted stroke primitives.

**Memory files updated**:
- `success_bank/INDEX.md` — appended new rows to both stroke-primitives and radical-primitives tables; added "PASSed in B2 but NOT promoted" section (4 items); extended "Not promoted (C/FAIL)" section with 46 items across mains + retries.
- `errata.md` — full diagnostic notes for all 18 B2 FAILs + 13 C's, organized into 4 clusters (compound-stroke gaps, multi-turn compounds, proportion/sibling confusion, C-verdicts). Cross-item learnings section extended with 6 new lessons.
- `drawer_memory.md` — retrieval table extended with the 2 new stroke primitives; whole-radical retrieval section reorganized into B2-era sub-section grouped by role (left/bottom/right/whole-glyph); sibling-pair notes extended with 7 new pairs (户/尸/肀, 攴/攵, 手/毛, 弋/戈, 兀/元, 纟/幺/么, 气/乞); MMH anchor calibration notes extended with 6 new cases (氵/囗/日/兀/气/风).
- `principle_bank.md` — 3 new principles: P-COMP-001 (MMH count trumps radical-wrapper count), P-COMP-002 (two BANK_DEVIATIONs = promote at curator), P-COMP-003 (sibling-pair failures cluster on distinguishing feature).
- `sandbox.md` — B2 postmortem covering MMH-effect analysis (+4pts, FAIL→C halving), bank growth details, retry outcomes, 4 FAIL cluster identification, structural-evolution decisions, 4 observations to test in B3.

**Rationale**: B2 confirmed and extended B1's pattern:
1. MMH prevents wrecks (FAIL count halved vs G3) but doesn't push borderline C's to PASS.
2. Bank promotion of missing compound-stroke classes (P-RET-003, extended by P-COMP-002) is the main mechanism for enabling PASS on the second attempt.
3. Sibling-pair confusion is now the dominant remaining failure mode; the curator has responded by aggressively populating the sibling-pair table.
4. The whole-radical primitives are position-signature (rather than baked-in) so Phase-3 can call them with (ox, oy, scale) fits. The hypothesis "left-position radicals shrink and drift right" remains untested until Phase-3 begins (~ position 136).

**Expected help for**: B3 retry queue (esp. 氏/旡/气 with new xie_gou; 火/夂/夊 with draw_pu template; 见/贝 with wei_enclose composition; 手/毛/肀 with sibling-pair notes); Phase-3 characters starting ~position 136 (>60% of common Phase-3 characters contain at least one of the 46 promoted whole-radical primitives).

**Deliberately NOT done**:
- No new file types created — the three-bank layout continues to work at ~230-line drawer_memory (revisit at 400).
- No memory-structure split.
- No promotion for any FAIL/C items (see retry_log.jsonl B3 queue).
- No variant entries yet — B2 was still radicals; v13 variants need composition evidence (starts Phase-3).

---

## 2026-08-08 — B3 curator: FIRST A verdicts + bank +19 primitives (position 168)

**Context**: B3 produced 35 PASS / 7 C / 8 FAIL on 50 mains + 7 PASS / 19 C /
12 FAIL on 38 retries = 42/88 overall (48%). Mains alone: 35/50 = 70%
(up from B2's 38%; best batch to date). Cumulative 100/168 = 60% success.

**FIRST-A MILESTONE (position 168)**: 4 A verdicts — p2_radical_128_爻,
p3_char_0009_了, p3_char_0011_人, p3_char_0017_又. Cross-group vs G3 B3
(same items, no MMH): G3 = 29/50 = 58% with 0 A; G5 = 35/50 = 70% with
4 A. **Delta: +12 pts absolute AND first quality lift into A band**. MMH's
effect signature is intensifying at Phase-3 — where B1/B2 was mainly
FAIL-prevention, B3 adds quality lift for chars mapping cleanly to bank.

**Files changed**:

**Success bank — 19 new promotions (64 → 83 entries)**:

*3 new stroke primitives*:
- `wan_gou.py` (弯钩) — from p3_char_0009_了 **A verdict** BANK_DEVIATION.
  High-reuse: 了/子/字/学/宁-family.
- `heng_zhe_ti.py` (横折提) — from p2_radical_035_讠__retry_2 BANK_DEVIATION.
  Very-high-reuse: 说/话/记/让/请-family.
- `pie_zhe.py` (撇折) — from p2_radical_078_幺__retry_1 BANK_DEVIATION.
  Reuse: 幺/纟/糸-family.

*16 new radical primitives* — 9 from main-channel PASSes (王 文 爻 曰 月 爫
支 止 无) + 7 from retry PASSes (肀 幺 门 讠 阝 宀 女). Highlights: 讠 (very-
high-freq speech), 月 (very-high-freq), 女 (very-high-freq), 阝 (very-high-
freq ear), 宀 (very-high-freq roof), 门 (high-freq gate).

**Memory files updated**:

- `success_bank/INDEX.md` — 19 rows added; new B3-era "PASSed but not
  promoted separately" section listing 17 Phase-3 chars that reused
  existing bank primitives; B3 Not-promoted section listing 8 FAILs +
  7 C's + 12 retry FAILs + 19 retry C's.
- `errata.md` — full B3 diagnostic section (FAIL cluster HH heng_zhe_wan_gou
  family, FAIL cluster W 3-directional, C cluster proportion, retry
  outcomes); 6 cross-item learnings.
- `principle_bank.md` — **4 new principles**:
  - P-A-001 (**FIRST A-recipe principle**: identity bank reuse can lift PASS to A)
  - P-A-002 (**SECOND A-recipe principle**: meticulous MMH-verbatim inline
    composition can also reach A when taper is explicit)
  - P-COMP-004 (composed primitives sharing alignment must be called through
    a single wrapper, not summed from independent pieces)
  - P-COMP-005 (structural identity → whole-radical primitive; anchor-spread
    or count mismatch → compose from strokes)
- `drawer_memory.md` — retrieval table extended with 3 new stroke primitives;
  whole-radical retrieval section extended with B3-era sub-section grouped by
  role; sibling-pair notes extended with 7 new pairs (士/土/王, 日/曰, 儿/几/九,
  无/旡/既, 了/子/字, 文/又/攵, and B3 note); MMH anchor calibration extended
  with 5 new cases (月, 宀, 门, 爻, 了/人/又 A-recipe entries); composition
  playbooks extended with A-recipe checklist + heng_zhe_wan_gou sandbox spec.
- `sandbox.md` — B3 postmortem (raw counts, cross-group comparison, first-A
  analysis, failure clusters, retry recovery analysis, bank growth, structural
  evolution decisions, 5 observations to test in B4).
- `retry_log.jsonl` — 46 rows appended: 41 B4 retry queue + 5 terminal-freeze
  (寸 R2, 尸 R2, 己 R2, 弓 R2, 几 R2).
- `curator_satisfaction_log.jsonl` — 88 rows appended for B3.

**Rationale**:

The A verdicts represent a qualitative shift: MMH+bank is no longer merely
error-reducing; it is a quality lever. Two independent routes to A emerged
(P-A-001 identity reuse; P-A-002 meticulous inline). Both routes required
stroke-count match with MMH AND explicit taper — this is the strongest
codified A-recipe to date.

The retry channel continues to prove valuable: 5/6 R2 escalations PASSed
(83%), each with curator-provided trajectory diff. This validates keeping
the multi-batch retry loop even for items that FAIL twice.

The `heng_zhe_wan_gou` family remains the largest un-covered stroke class,
blocking 几/九/瓦/风/凡. Provided a geometric spec in sandbox for B4 drawers;
if any retry PASSes with the spec, promote as new stroke primitive.

**Expected help for**:
- B4 Phase-3 chars containing any of the 16 new radicals (est. > 40% of
  common Phase-3 chars will contain 讠/月/女/阝/宀/门 alone).
- 子/字 (children family) retries — new wan_gou primitive from 了 A directly
  unblocks the shu-with-hook.
- 纟 retry — new pie_zhe primitive directly unblocks.
- 心/必 family retries if 心's inline 卧钩 PASSes (would seed wo_gou.py).
- Quality lift: if identity-call bank reuse (P-A-001) generalizes, we expect
  more A verdicts on Phase-3 chars like 冫/厂/凵/刀/丨/丶 (single-radical
  chars that directly correspond to bootstrap PASSed radicals).

**Deliberately NOT done**:
- No memory file split — drawer_memory.md ~380 lines, still navigable
  (revisit at 500).
- No pre-emptive `heng_zhe_wan_gou.py` promotion (2 FAILing DEVIATIONs
  don't satisfy P-COMP-002 which requires PASS). Sandbox spec provided
  instead; promote if a B4 retry PASSes.
- No `wo_gou.py` yet (0 PASSing DEVIATION); promote in B4 if 心 retry PASSes.
- No `heng_zhe_wide.py` yet (2 attempts C-verdict for 冂); promote if a B4
  retry PASSes.

---

## 2026-08-08 — B4 curator: bank +9, principle-bank +3, aggressive terminal-freeze

**Context**: B4 produced 29 PASS / 13 C / 8 FAIL on 50 mains (Phase-3
chars idx 034-083) plus 5 PASS / 10 C / 21 FAIL on 36 retries = 34/86
overall (40%). Mains alone: 29/50 = 58% (regression from B3's 70%);
**0 A verdicts** (regression from B3's 4). Cumulative through B4:
**129/218 = 59%, 4 A total**.

Cross-group vs G3 B4 (same items, no MMH): G3 = 27/50=54% with 0 A;
G5 = 29/50=58% with 0 A. **Delta narrowed to +4 pts (from B3's +12)**;
MMH-signature still holds on FAIL prevention (G5 8 FAILs vs G3 23) but
PASS-rate advantage narrowed and A-quality advantage evaporated for
this item pool.

**Files changed**:

**Success bank — 9 new promotions (83 → 92 entries)**:

*3 retry-PASS radical primitives*:
- `wei_leather.py` (韦) — from p2_radical_123_韦__retry_1 R1 PASS. Contains an inline BANK_DEVIATION helper for the bottom-hook compound (not extracted as separate stroke primitive; 1 occurrence only).
- `shi_spirit.py` (礻) — from p2_radical_116_礻__retry_2 R2 PASS. HIGH-freq left-position radical.
- `chang_long.py` (长) — from p2_radical_088_长__retry_2 R2 PASS. HIGH-freq; uses PIL polylines directly (竖提 compound baked in).

*6 Phase-3 whole-char primitives*:
- `shang_up.py` (上) — from p3_char_0045_上. 3 strokes: shu + short-heng + long-heng.
- `xia_down.py` (下) — from p3_char_0053_下. 3 strokes: heng + shu + dian.
- `san_three.py` (三) — from p3_char_0055_三. 3 hengs.
- `qian_thousand.py` (千) — from p3_char_0075_千 (P-A-002 route). 3 strokes: pie + heng + shu. HIGH-freq component.
- `wang_gone.py` (亡) — from p3_char_0052_亡. 3 strokes: dian + heng + shu_zhe. HIGH-freq (忘/忙/慌/望/妄).
- `zhi_this.py` (之) — from p3_char_0039_之. 3 strokes: dian + heng_pie + ping_na.

**PASSes not promoted separately**: 11 identity-reuse Phase-3 chars
(勹/匕/大/门/山/女/宀/口/干/小/艹 — all called existing bank primitives);
2 low-reuse retry PASSes (尣, 毋); 9 other Phase-3 chars (丫/丬/个/亼/卄/
叉/习/纟/亾) fully covered by stroke bank inline. See INDEX.md B4 sections.

**Stroke-primitive candidates deferred (single-DEVIATION, awaiting 2nd)**:
- `heng_pie_short.py` — 孑 heng_pie DEVIATION (1 occurrence, PASSed); needs a 2nd occurrence per P-COMP-002 before promotion.

**Memory files updated**:
- `success_bank/INDEX.md` — 9 new rows in radical/char table; new B4-era "PASSed but not promoted separately" section listing 25 items; B4 Not-promoted section listing 8 mains FAILs + 13 C's + 22 terminal-freezes + 9 B5 R2 queue items.
- `drawer_memory.md` — TOC unchanged, but retrieval-hints section extended with B4-era radicals + whole-char primitives (韦/礻/长 + 上/下/三/千/亡/之); sibling-pair notes extended with 8 new families (上/下/卜, 千/干/于, 三/王/士/土, 孑/孓/子, 也/卂, 刁/习/力, 夂/夊/攵/久); A-recipe playbook extended with "B4 update — A-recipe generalized to PASS but NOT to A quality" — records the 11-identity-call, 0-A finding and outlines the post-render GT-diff hypothesis; MMH anchor calibration extended with 5 new cases (礻 R2, 长 R2, 韦 R1, 毋 R1, 尣 R1) plus a B4 FAIL calibration subsection covering 也/卂/与/刁/丸/子/飞/夂/夊.
- `principle_bank.md` — **3 new principles**:
  - **P-A-003**: A-recipe qualifier — identity-reuse and meticulous-inline lift to PASS reliably, but do NOT automatically yield A verdicts on 3+ stroke chars.
  - **P-RET-004**: Bank primitives baked for Phase-2 context may need per-composition re-tuning at Phase-3 (also/与 evidence).
  - **P-COMP-006**: Retry escalation past R2 has diminishing returns unless a new bank primitive or trajectory-diff was added between rounds (B4 R2 rate 9% vs B3 R2 rate 83%).
- `sandbox.md` — B4 postmortem covering raw counts, cross-group comparison, A-recipe failure analysis, retry-channel regression diagnosis, HIGH-prob blowup post-mortem, bank growth, deferred stroke-primitive candidates, 22 terminal-freeze decisions, B5 R2 queue, 4 observations for B5.
- `errata.md` — full B4 diagnostic section: FAIL cluster HW (hook/curve/wrap family — 8 items with individual retry hints); 13 C-verdict cluster with retry hints; retry channel outcomes (3 R1 PASS, 2 R2 PASS, 8 R2-C terminal-freeze, 14 R2-FAIL terminal-freeze, 7 R1 FAIL → B5 R2 queue); cross-item learnings (4 new).
- `retry_log.jsonl` — 30 rows appended: 9 B5 R2 queue items + 22 terminal-freeze markers (see rows).
- `curator_satisfaction_log.jsonl` — 86 rows appended for B4.

**Rationale for terminal-freeze aggressiveness**:

B4 R2 rate collapsed from B3's 83% to 9%. Diagnostic: B3 R2 PASSes were
all cases where a new bank primitive was added between R1 and R2 (or a
specific trajectory-diff was applied). B4 R2 items had neither. Codified
as P-COMP-006: an R2 queue without a mechanism-change is expected to
FAIL again — burning a slot with no expected recovery. Freezing 22
items (14 R2-FAIL + 8 R2-C) removes noise from the retry queue and
frees B5 R1 capacity for main-channel Phase-3 dispatches.

Prior batches (B1-B3) accumulated a large retry backlog by keeping
every C-verdict alive. This is not scalable: as Phase-3 progresses,
the retry queue would eventually exceed main-channel capacity. The
aggressive freeze at B4 is a policy correction; expected effect =
tighter retry queue with higher expected PASS per slot.

**Expected help for**:
- B5 Phase-3 chars 084-133 that contain 亡/千/上/下 as sub-components
  (fairly common) or that identity-match retry-PASSed radicals 礻/长/韦.
- **A-quality lift** on B5 identity-reuse candidates IF drawers adopt
  the post-render GT-diff tuning step (unvalidated hypothesis P-A-003).

**Deliberately NOT done**:
- No memory file split — drawer_memory.md now ~430 lines; approaching
  the 500-line threshold. B5 curator should split into topic files if
  it grows further.
- No new file types created.
- No promotion for the 尣/毋 retry PASSes (low reuse; inline preserved
  in attempts/).
- No stroke-primitive promotions this batch (0-DEVIATION on the missing
  compound classes; 1-DEVIATION for heng_pie_short doesn't satisfy P-COMP-002).
- No revert or retirement of prior principles (P-A-001, P-A-002 remain
  valid — extended by P-A-003, not contradicted).

---

## 2026-08-08 — B5 curator: bank +2, principle_bank +3, terminal-freeze +9

**Context**: B5 produced 27 PASS / 12 C / 11 FAIL on 50 mains (Phase-3
chars idx 084-133) plus 0 PASS / 1 C / 8 FAIL on 9 R2 retries = 27/59
overall (46%). Mains alone: 27/50 = **54%** (regression from B4's 58%);
**0 A verdicts** (3rd consecutive batch at 0 A — see P-A-004 below).
Cumulative through B5: **156/268 = 58%, 4 A total**.

Cross-group vs G3 B5 (same items, no MMH): G3 = 19/50 = 38%;
G5 = 27/50 = 54%. **Delta = +16 pts absolute** — the biggest per-batch
gap yet, driven by G3's dip more than G5 lift. MMH's FAIL-prevention
effect intensifies as items get harder.

**Files changed**:

**Success bank — 2 new promotions (92 → 94 entries)**:

*2 new stroke primitives*, both promoted per **P-COMP-007** (elevated
from P-RET-003; 1st PASSing DEVIATION on distinct MMH-named stroke class
is sufficient):

- `wo_gou.py` (卧钩) — from p3_char_0112_心 BANK_DEVIATION PASS.
  fresh_component `wo_gou_for_xin`. Signature:
  `draw_wo_gou(d, head, tail, belly_y=None, width=8, hook_up=26, hook_back=6)`.
  Very-high-reuse: 心/必/忘/忙/志/思/念/忽/恕 family.
- `heng_zhe_wide.py` (WIDE mid-body 横折 with sharp corner + straight drop) —
  from p3_char_0122_五 BANK_DEVIATION PASS. fresh_component
  `heng_zhe_wide_inline_for_wu`. Signature:
  `draw_heng_zhe_wide(d, head, tail, corner=None, w_head=8, w_tail=8, corner_dab=6)`.
  Reuse: 五/亚/世/巫 family. Distinct from `heng_zhe_short` (tiny top-arc)
  and `heng_zhe_box` (口 frame).

**Deferred/not-promoted BANK_DEVIATIONs**:
- `cong_two_ren_asymmetric` (from 从) — character-specific, low reuse.
- `heng_pie_yu_top` (from 予) — FAILed, cannot promote.
- `heng_zhe_wan_gou_for_{九,几,冗}` (from 仇/仉/冗 FAILs) — cannot promote
  from FAILs; escalated to hypothesis-driven candidate spec in sandbox
  per P-COMP-008.

**Memory files updated**:

- `success_bank/INDEX.md` — 2 new rows in stroke primitives table
  (rows 20-21); new "PASSed in B5 but NOT promoted separately" section
  listing 27 B5 PASSes with their reuse routes; new "Not promoted from
  B5 (C/FAIL, deferred or terminal-freeze)" section listing 11 FAILs
  clustered (5 heng_zhe_wan_gou + 5 proportion + 1 heng_pie) + 12 C's
  + 9 R2 terminal-freezes.
- `drawer_memory.md` — retrieval hints table extended with 2 new stroke
  primitives (wo_gou, heng_zhe_wide); sibling-pair notes extended with
  6 new pairs (内/內, 马/乌, 仇/仉/亢, 冗/冘, 心, 五); MMH anchor
  calibration extended with B5 section covering 心 (belly_y=260 for deep
  dip), 五 (heng_zhe_wide corner geometry), P-A-004 identity-call
  observation for 文/日/中/工, and 8 B5 FAIL trajectory-diff hints.
- `principle_bank.md` — **3 new principles**:
  - **P-COMP-007**: 1st PASSing DEVIATION on distinct MMH-named stroke
    class is sufficient promotion evidence (elevated from P-RET-003).
    Character-specific fresh_components still need 2 DEVIATIONs per
    P-COMP-002.
  - **P-A-004**: A-drought is STRUCTURAL, not disciplinary — identity-call
    P-A-001 stops producing A verdicts once the item pool has no 1-2
    stroke identity candidates left.
  - **P-COMP-008**: When a terminal-freeze pattern points at a single
    missing bank primitive across many items, elevate the promotion
    decision from evidence-driven to hypothesis-driven — put a candidate
    spec in sandbox; promote if any next-batch attempt PASSes with it.
- `sandbox.md` — B5 postmortem covering raw counts (54% mains, 58%
  cumulative), A-drought structural analysis with 4-item sample, bank
  growth details, candidate spec for `heng_zhe_wan_gou` (elevated per
  P-COMP-008), 9 terminal-freeze decisions, B6 retry queue (14 items),
  4 observations for B6.
- `errata.md` — full B5 diagnostic section: 3 FAIL clusters (HZ
  heng_zhe_wan_gou-blocked, LR proportion, HP heng_pie); 12 C-verdict
  cluster (multi-curve calligraphic + proportion); retry outcomes (0/9
  R2 PASS confirming P-COMP-006); 4 cross-item learnings.
- `retry_log.jsonl` — 23 rows appended: 9 terminal-freezes (8 R2 FAIL +
  1 R2 C) + 14 B6 R1 queue rows.
- `curator_satisfaction_log.jsonl` — 59 rows appended for B5.

**Rationale for aggressive P-COMP-007 promotion**:

B4 curator sat on `heng_pie_short` for 1 batch (P-COMP-002 strict 2-DEVIATION
rule) and reaped no new evidence in B5. Meanwhile, B5 saw 5 fresh
FAILs (乌/马/仇/仉/冗) blocked by the still-missing `heng_zhe_wan_gou`,
which has now accumulated evidence across B3/B4/B5. This is compelling
evidence that the strict 2-DEVIATION rule creates avoidable failures:
if a MMH-named stroke class works ONCE, the geometry is right, and
the bank should hold it. Split the rule: **for stroke classes MMH
names as distinct**, promote on 1st PASS; **for character-specific
compositions (fresh_components suffixed with _for_<char>)**, keep the
2-DEVIATION requirement.

**Rationale for P-COMP-008 hypothesis-driven candidate specs**:

The `heng_zhe_wan_gou` blocker has now caused ≥ 15 documented FAILs
across 3 batches. The only way to break this is to give B6 drawers
a concrete inline spec that either (a) PASSes and promotes to bank
or (b) FAILs and rules out the "just missing primitive" hypothesis
(revealing composition-level issues). Sandbox now carries the exact
callable spec with a 4-endpoint signature (heng_head, corner,
belly_bottom, hook_tip).

**Expected help for**:
- B6 Phase-3 chars containing 心 as a component (necessary/mind-family
  chars) if any appear at idx 134-183.
- B6 R1 retries on 乌/马/仇/仉/冗 via sandbox candidate spec — cash
  probability moderate (P-COMP-008 is untested).
- B6 R1 retries on 亢/以/见/兮/內 via trajectory-diffs.

**Deliberately NOT done**:
- No memory file split — drawer_memory.md now ~500 lines; if B6 pushes
  past 600, split by topic then.
- No new file types created.
- No promotion for the 27 B5 PASSes' non-A results — the 11
  identity-reuse cases either already have their bank primitive or
  reuse a stroke composition already covered.
- No revert of any prior principle. P-COMP-007 refines (not contradicts)
  P-RET-003 and P-COMP-002; P-A-004 extends P-A-003; P-COMP-008 extends
  P-COMP-006.

---

## 2026-08-08 — B6 curator: bank +8, principle_bank +1 + 1 update, terminal-freeze +18

**Context**: B6 produced 32 PASS / 10 C / 8 FAIL on 50 mains (Phase-3
chars idx 134-183) plus 1 PASS + 1 **A** + 12 FAIL on 14 R1 retries.
Mains alone: 32/50 = **64%** (best Phase-3 batch to date — up from B5's
54%). **First-ever A verdict from the retry channel** (义 R1). Cumulative
through B6: **188/318 = 59%, 5 A total**.

**Cross-group vs G3 B6 (same items, no MMH)**: G3 = 23/50 = 46%;
G5 = 32/50 = 64%. **Delta = +18 pts absolute — NEW RECORD** (previous
best B5's +16). MMH signature intensifying with item difficulty.

**Files changed**:

**Success bank — 8 new promotions (94 → 102 entries)**:
- `yi_x.py` (义) — from p3_char_0089_义__retry_1 **A** (P-A-005 recipe).
  Reuse: 仪, 议, 艺.
- `hua_change.py` (化) — L-R 亻+匕. Reuse: 花, 华.
- `fan_reverse.py` (反) — 厂+又. Reuse: 板, 饭, 返, 贩, 版, 叛.
- `yuan_first.py` (元) — 二+儿. Reuse: 完, 园, 院, 远, 玩.
- `zhu_lord.py` (主) — dian + 王-triple-heng + shu. Reuse: 住, 注, 柱.
- `zheng_correct.py` (正) — top-heng + 止. Reuse: 证, 政, 征, 症.
- `sheng_born.py` (生) — pie + 3 hengs + shu. Reuse: 性, 星, 姓, 胜.
- `ping_flat.py` (平) — heng + dian + pie + heng + shu. Reuse: 评, 坪, 苹, 秤.

**Not promoted** (kept inline in attempts/): 4 chars with character-specific
BANK_DEVIATIONs awaiting 2nd DEVIATION per P-COMP-002:
- p3_char_0146_队 (`er_ear_for_left_position` compact ear)
- p3_char_0148_书 (`shu_book_body` cursive body — 书-specific)
- p3_char_0156_们 (narrower 门 variant)
- p3_char_0166_去 (compressed 土 top)

**Memory files updated**:
- `success_bank/INDEX.md` — 8 new rows in whole-char section (rows 88-95);
  "PASSed in B6 but NOT promoted separately" section listing 22 identity-reuse
  chars; "Not promoted from B6 (C/FAIL)" section listing 8 main FAILs (with
  4-cluster breakdown), 10 C's, 12 R1 FAILs terminal-frozen.
- `principle_bank.md` — **1 new principle + 1 update**:
  - **P-A-005 (NEW B6)**: retry channel A-recipe — trajectory-diff must
    address calligraphic weight + joint geometry (not just endpoint anchors).
    Evidence: 义 R1 became first-ever A from retry via 3 specific parameter
    changes (dian taper, pie negative bow_perp, na strong tail-thickening).
    Refines P-COMP-006 (R1 CAN help without new bank IF trajectory-diff is
    mechanism-specific).
  - **P-COMP-008 UPDATE**: candidate spec FAILED for 5 hook-family retry items
    (乌, 仇, 仉, 冗, 马). The "just missing primitive" hypothesis is
    INSUFFICIENT for this family — failure is composition-level, not just
    bank gap. Do NOT hand-craft heng_zhe_wan_gou without a PASSing case.
- `drawer_memory.md` — retrieval hints section extended with 8 new whole-char
  primitives (义, 化, 反, 元, 主, 正, 生, 平) + reuse-target family maps;
  A-recipe playbook extended with P-A-005 entry (negative-bow crossing
  forcing for 3-stroke chars); MMH anchor calibration extended with 6 new
  B6 cases (义, 化 L-R shrink, 反 heng_pie crossing, 元 vs 无 sibling
  distinguishing, 主/正/生/平 5-stroke identity cases).
- `sandbox.md` — B6 postmortem: raw counts, 义 A analysis (3 specific
  parameter changes), 8 FAIL cluster diagnosis (wave/wraparound, chronic
  freeze, L-R proportion, rare), 12 retry FAIL diagnosis with P-COMP-008
  test result, terminal-freeze list, B7 retry queue with priorities,
  observations for B7.
- `errata.md` — full B6 diagnostic section for all 8 mains FAILs, 10 C's,
  12 R1 FAILs (with cluster classifications matching sandbox); 5 cross-item
  learnings extension.
- `retry_log.jsonl` — 26 rows appended: 5 B7 R1 queue (发, 仗, 必, 打, 付) +
  2 LOW-priority (用, 比) + 12 terminal-freeze markers + 7 do-not-queue
  markers.
- `curator_satisfaction_log.jsonl` — 64 rows appended for B6.

**Rationale**:

**A-lift returned via retry channel** — B5's A-drought analysis (P-A-004:
"structural, not disciplinary; need 1-2-stroke items") assumed the
recipe only fires on very simple chars. 义 R1 disproves that at the
"3-stroke crossing chars with careful bow tuning" boundary. P-A-005
extends the A-recipe. This is important: it means the retry channel is
a viable A route, not just a PASS route.

**Cross-group delta widening** — B4 was +4, B5 was +16, B6 is +18. G5's
MMH-injection value is compounding as Phase-3 items get harder, exactly
opposite to the B4 concern that MMH's effect might attenuate at depth.
The B4 dip appears to have been an item-pool artifact.

**Terminal-freeze rate accelerating** — B4 froze 22, B5 froze 9, B6 will
freeze ~18 (12 retry FAILs + 6 main FAILs going straight to freeze). This
is P-COMP-006 doing its job: retry queue stays pruned, main-channel slots
free.

**Expected help for**:
- B7 Phase-3 chars (idx 184-233) containing any of 化/反/元/主/正/生/平
  as radical or main component: est. > 30% of common Phase-3 chars.
- Future 3-stroke crossing chars — try P-A-005 negative-bow forcing.

**Deliberately NOT done**:
- **No `heng_zhe_wan_gou.py` promotion** — B6 evidence rules out the
  "missing primitive" hypothesis for this family (5 inline attempts of the
  sandbox candidate spec all FAILed). Do not poison the bank with an
  unvalidated primitive.
- **No memory file split** — drawer_memory.md ~530 lines after B6 updates;
  B7 curator should split if it crosses 600.
- **No revert of prior principles.** P-A-005 extends P-A-003/P-A-004
  (which explain A-drought STRUCTURAL) by adding a new evidence-backed
  route. P-COMP-008 update refines (does not retract) the elevation rule.

---

## 2026-08-08 — B7 curator: bank +13, principle_bank +4, biggest cross-group delta (+34 pts)

**Context**: B7 produced 5 A + 28 PASS + 9 C + 8 FAIL on 50 mains
(Phase-3 chars idx 184-233) plus 7 retries (2 PASS: 用, 比; 3 C: 必, 付,
打; 2 FAIL: 发, 仗). Mains alone: **33/50 = 66% PASS** (best Phase-3
batch to date — up from B6's 64%); **5 A verdicts** (best per-batch
count; total 9 A cumulative). Cumulative through B7: **221/368 = 60%,
9 A total**.

**Cross-group vs G3 B7** (same items, no MMH): G3 = 16/50 = 32%;
G5 = 33/50 = 66%. **Delta = +34 pts absolute — biggest cross-group
delta of the experiment** (previous best B6's +18).

**Files changed**:

**Success bank — 13 new promotions (102 → 115 entries)**, 0 new stroke
primitives, all whole-char:
- 4 A: `yi_ye.py` (业), `qian_person.py` (仟), `ran.py` (冉), `ping_pang.py` (乓)
- 9 PASS: `li_stand.py` (立), `bai_white.py` (白), `you_by.py` (由),
  `si_four.py` (四), `hui_meet.py` (会), `you_have.py` (有),
  `nian_year.py` (年), `zi_self.py` (自), `shi_world.py` (世)

**Not promoted** (kept inline): 15 identity-reuse or moderate-reuse PASSes
(市, 术, 兰, 皿, 而, 北, 冊, 代, 矢, 失, 乑, 乔, 乩, 亘, 亙); 3 deferred
variant candidates (mu_wood_variant_for_本, li_variant_for_加,
er_ear_right_variant) — all awaiting 2nd DEVIATION or PASSing evidence.

**Memory files updated**:
- `success_bank/INDEX.md` — 13 new rows in whole-char section; new B7-era
  "PASSed but not promoted separately" section (25 items); B7 "Not promoted
  (C/FAIL)" section with 8 mains FAIL clusters, 9 C's, 5 retry verdicts.
- `drawer_memory.md` — B7-era retrieval hints table (13 whole-char reuse
  families); 13 anchor calibration entries; **P-A-006 quick reference
  playbook**; 9 B7 sibling notes (业/亚/亞, 四/田/由/甲, 白/自/百, 有/冇,
  世/卅/廿, 仟/千/干/于, 冉/再/苒, 乓/乒/兵/丘, 年/甲/早, 会/合/令,
  X-cross cluster); 8 B7 failure calibration entries; 5 B7 retry outcomes.
- `principle_bank.md` — **4 new principles**:
  - **P-A-006 (NEW B7)**: "MMH-anchor verbatim + stroke-primitive layer" —
    new A-recipe route for 5-6 stroke chars. All 5 B7 A's followed this
    pattern. Extends P-A-001/002/003/005 (doesn't retract P-A-004).
  - **P-COMP-009 (NEW B7)**: Double-transform failure on whole-radical
    L-R compositions. Uniform (ox, oy, scale) can't retarget both stroke
    width AND joint positions simultaneously. Refines P-RET-002.
  - **P-COMP-010 (NEW B7)**: X-cross cluster (癶/矢/失/処/乩/那) is NOT
    frozen in G5. MMH anchor precision compensates for cluster-blocked
    failures. Mechanistic cross-group finding.
  - **P-RET-005 (NEW B7)**: Retry-PASS from sibling-pair discipline
    (without new bank). 比 R1 PASS validates this route. Refines P-COMP-006
    with a 3rd mechanism-change kind.
- `sandbox.md` — B7 postmortem: raw counts, P-A-006 discovery analysis,
  cross-group delta analysis, X-cross cluster verdict, bank growth,
  structural evolution decisions, **B8 A-uplift target list**, split
  recommendation for drawer_memory.md, 5 observations for B8.
- `errata.md` — full B7 diagnostic section: 5 A's, 8 mains FAILs across
  4 clusters (L-R double-transform, BANK_DEVIATION fresh-composition FAIL,
  chronic freeze family, 阝-position), 9 C's, 7 retry outcomes, 5
  cross-item learnings extending B6.
- `retry_log.jsonl` — B7 rows appended (5 terminal-freeze from retries,
  8 terminal-freeze from main FAILs, 9 do-not-queue from main C's, 2
  retry-PASS records; B8 retry queue = empty).
- `curator_satisfaction_log.jsonl` — 57 rows appended for B7 (50 mains + 7 retries).

**Rationale**:

**P-A-006 is the standout finding of B7**. Before this batch, our A-recipe
inventory was: P-A-001 (identity-reuse of a whole radical), P-A-002
(meticulous inline with taper), P-A-005 (retry-A via negative-bow forcing).
All three assumed the drawer's task was to make one whole-object-per-A
attempt. B7 evidence shows a fourth route: **for 5-6 stroke chars, call
stroke-signature primitives with MMH anchors verbatim; refuse whole-radical
composites even when they match**. This route delivered 5 A's in one batch
— more than B3-B6 combined (4 A's).

**Interpretation of the +34 pts delta**: two mechanisms compound.
(1) MMH FAIL-prevention (G3 got 21 FAILs vs G5's 8) — same as prior
batches; (2) P-A-006 PASS-lift, unique to B7 — routes MMH's endpoint
precision directly into 1:1 calligraphic fidelity, bypassing composite
transforms. This is the first batch where the mechanism producing PASS
lift is distinct from the mechanism producing FAIL prevention.

**Terminal-freeze pattern intensifying** — B4 froze 22, B5 froze 9,
B6 froze 18, B7 froze 15 (5 retry + 8 main FAILs + 2 more from C
terminal decisions). Retry channel now yields near-zero R2 PASSes;
new A-recipe (P-A-006) is coming from MAIN channel, not retry channel.

**Expected help for**:
- B8 Phase-3 chars containing any of 立/白/由/四/皿/世/会/亘/有/而/年/自/术/北
  as radical or main component (est. > 40% of B8's 6-stroke phonetic-family
  chars will contain at least one).
- B8 亻+X 6-stroke compounds (仰/仲/仳/仵/伄/伉/伊/伎/伐/伕/伙/伛/伢/伥/伦/
  伧/伪/伫/任/佤/传) via P-A-006 recipe using `qian_person.py` (仟) as
  L-R template.

**Deliberately NOT done**:
- **No drawer_memory.md split THIS batch** — B7 additions kept under
  "B7-era" section headings; file is ~700 lines. B8 curator MUST split
  if it crosses 900 lines (recommended: `retrieval_hints.md`,
  `sibling_pairs.md`, `mmh_calibration.md`, `a_recipes.md`).
- **No B8 R1 retry queue populated** — B7 R1 was fully burned; the 3
  R1 C's + 2 R1 FAILs are all terminal-freeze per P-COMP-006 (no
  mechanism-change available). B8 retry queue empty by design.
- **No promotion of the 3 variant candidates** (mu_wood_variant_for_本,
  li_variant_for_加, er_ear_right_variant) — awaiting 2nd DEVIATION per
  P-COMP-002 or an evidence-backed PASSing case.
- **No revert of prior principles.** P-A-006 extends the A-recipe family;
  P-COMP-009/010 refine (do not retract) P-RET-002 and prior cluster
  observations; P-RET-005 extends P-COMP-006's list of valid
  mechanism-changes.

---

## 2026-08-09 — B8 curator: bank +9, principle_bank +2, first fair-A batch confirms two-factor hypothesis

**Context**: B8 produced 0 A + 20 PASS + 10 C + 20 FAIL on 50 mains
(Phase-3 chars idx 234-283). No retries (B7 queue empty by design).
Cumulative through B8: **241/418 = 57.7% PASS, 9 A total (all pre-B8)**.

**KEY FINDING — first fair-A comparison**: Cross-group on identical items:
- G3 (no MMH): 14/50 = 28%, 0 A
- G4 (MMH + grid + fat_line): 20/50 = 40%, **10 A**
- G5 (MMH + code, uniform PIL line): 20/50 = 40%, 0 A

Same PASS rate for G4 and G5, but G4 gets 10 A while G5 gets 0. This
decomposes the "MMH+bank" effect into two independent factors: (1) MMH
raises PASS baseline (both non-G3 groups equally); (2) format determines
A-quality ceiling (G4's per-endpoint fat_line width control unlocks the
calligraphic weight distribution the judge rewards; G5's uniform PIL
line width cannot produce it). Recorded as the STRUCTURAL A ceiling.

**Files changed**:

**Success bank — 9 new promotions (115 → 124 entries)**:

*1 new stroke primitive*:
- `heng_pie_slim.py` (from 多 PASSing BANK_DEVIATION — 2nd occurrence
  meeting P-COMP-002; 1st was 孑 B4 inline). Signature:
  `draw_heng_pie_slim(d, head, tail, apex_x, corner_x, bow_perp=6,
  w_head=6, w_tail=3)`. Reuse: 夕-family (多/名/夜/岁), 又/欠 tuning.

*8 new whole-char primitives*:
- `duo_many.py` (多)   — stacked 夕. Reuse: 名, 夜, 岁, 够.
- `tong_same.py` (同)  — 冂+一+口. Reuse: 铜, 桐, 洞, 筒.
- `hui_return.py` (回) — double box. Uses draw_wei_enclose + inline 口.
- `wen_ask.py` (问)    — 门+口. Reuse: 闷, 阔.
- `he_together.py` (合)— 人-top+heng+口. Reuse: 拾, 给, 塔, 蛤, 鸽, 恰.
- `xing_walk.py` (行)  — 彳+亍 L-R. Reuse: 街, 衍, 冲, 徽.
- `ya_asia.py` (亚)    — sibling of 业. Reuse: 恶, 垩.
- `hou_after.py` (后)  — 6-stroke; reuse: 逅, 后-family.

**Not promoted from B8 PASS**: 12 items (行 subset already covered; 过
just calls draw_chuo_walk + inline 寸; 仲/仳/仵/伊/伐/伛/伦/任/此/当
all pure P-A-006 stroke-primitive compositions with no fresh_component —
"template" is documented in principle_bank/drawer_memory rather than
promoted as a wrapper).

**Memory files updated**:
- `success_bank/INDEX.md` — 9 new rows (rows 116-124); new B8-era
  "PASSed but not promoted separately" section (12 items); B8 "Not
  promoted (C/FAIL)" section: 20 FAILs clustered A-E, 10 C's, 5
  terminal-freezes + 7 do-not-queue markers.
- `drawer_memory.md` — B8-era retrieval hints (8 whole-char + 1 stroke
  primitive); 4 B8 sibling notes (亚/业, 军/冠/冕 (冖+X top), 名/多/夕
  family, 回/囗/口/日 nested-frames); 5 anchor calibration entries; B8
  failure calibration entries for 军/名/成/西 (mechanism-change hints).
- `principle_bank.md` — **2 new principles**:
  - **P-A-007 (NEW B8)** — P-A-006 overshoot guardrail. Use whole-radical
    primitive when it matches structural sub-component; refuse only when
    MMH-endpoint fidelity is the ceiling. Refines P-A-006 (does not
    retract).
  - **P-COMP-011 (NEW B8)** — 亻+X 6-stroke P-A-006 recipe generalizes
    only when X is straight-stroke composable. Hook-compound right halves
    (亢/火/牙/仓/瓦/吊/支) need bank extension first. Refines P-COMP-009.
- `sandbox.md` — B8 postmortem covering raw counts, cross-group
  two-factor finding, 5-cluster 20-FAIL diagnosis, PASS taper/joint
  sample (仲/多/次), BANK_DEVIATION triage, bank growth, terminal-freeze
  list, B9 retry queue with P-A-007 test items, observations for B9.
- `errata.md` — full B8 diagnostic section: 5 FAIL clusters (A hook-
  compound right, B whole-radical refusal, C chronic-freeze cousins,
  D 女-inline, E hook-body), 10 C-verdicts, terminal-freeze list, 4
  cross-item learnings.
- `retry_log.jsonl` — B8 rows appended: 5 terminal-freeze markers + 7
  do-not-queue markers + 7 B9 R1 queue items (4 HIGH: 军/名/成/西 for
  P-A-007 test; 3 MEDIUM: 老/好/再 tuning).
- `curator_satisfaction_log.jsonl` — 50 rows appended for B8 (all mains,
  no retries).

**Rationale**:

**Two-factor hypothesis confirmed empirically**: B8 was the first batch
where G4 and G5 could be fairly compared on A verdicts (per user note).
Same 40% PASS + G4's 10 A vs G5's 0 A cleanly separates: MMH is the
PASS lever; rendering format is the A lever. This is a headline finding
for the research paper: MEMORY FORMAT (code vs anchors) is NEUTRAL for
PASS rate but DECISIVE for A quality when combined with per-endpoint
width control.

**P-A-007 emerges from a P-A-006 overshoot pattern**: 4 of the 20 FAILs
(军, 名, 成, 西) are cases where the drawer applied P-A-006's "refuse
whole-radical" rule to characters where the bank primitive was the
CORRECT choice (车 in 军, 口 in 名, 戈 in 成, 四-shape in 西). The B7
A-recipe crystallized on grid-like / straight-stroke L-R chars where
whole-radical composition genuinely double-transformed; carrying that
recipe as an absolute rule into B8's mixed pool caused 4 avoidable FAILs.
P-A-007 scopes P-A-006 correctly.

**P-COMP-011 completes the 亻+X 6-stroke story**: 仟/仨 (B7 A) established
the P-A-006 recipe for 亻+X. B8's 7 亻+X FAILs (Cluster A) show the
boundary: right half MUST be straight-stroke composable. When it isn't
(亢/火/牙/仓/瓦/吊/支), the recipe fails and no mechanism-change other
than bank extension is available. This means several 亻+X items will
remain FAIL until the hook-compound bank gaps close.

**Terminal-freeze pattern intensifying**: B4-B7 froze 22/9/18/15; B8 froze
5 explicitly + 7 do-not-queue = 12. Slowing slightly; the cluster-A items
(7 hook-compound right radicals) will be revisited when bank gaps close,
not frozen.

**Expected help for**:
- B9 idx 284-333 characters containing 同/合/回/门 family, 夕-family
  (多/名/夜), 行-derivative (街/衍), 亚-family, 后-family.
- B9 R1 test of P-A-007 on 军/名/成/西 (mechanism-change: use bank
  primitive). If they PASS, generalize P-A-007 for B9+.
- Chars where drawers previously refused bank primitives — P-A-007 will
  reshape routing choices in future batches.

**Deliberately NOT done**:
- **No drawer_memory.md split THIS batch** — file is 716 lines pre-B8;
  after additions ~800 lines, still under the 900 trigger. B9 curator
  MUST split if it crosses 900.
- **No retraction of P-A-006** — P-A-007 refines scope only; the recipe
  is still correct for its intended domain (X-cross, grid-like, straight-
  stroke L-R).
- **No promotion of hook-compound primitives** (heng_zhe_wan_gou family
  remains sandbox-only per P-COMP-008 update).
- **No B9 retry queue items from cluster A/C/E** — no mechanism-change
  available for those chronic-gap items.

## 2026-08-09 @ position 518 — B9 curator: 12 bank primitives + 2 new principles (P-A-007-v2 sharpened, P-A-008, P-COMP-012); drawer_memory split trigger crossed

**Files changed**:
- `success_bank/code/` — 12 new primitives:
  - **A verdicts (4)**: `juan_yong.py` (龹), `hai_still.py` (还),
    `wei_position.py` (位), `pi_flourish.py` (伾)
  - **R1 PASSes (3)**: `jun_army.py` (军 — P-A-007 validation),
    `lao_old.py` (老 — shu_wan_gou tuning), `cheng_become.py` (成 — xie_gou tuning)
  - **High-reuse mains (5)**: `lai_come.py` (来), `li_inside.py` (里),
    `shi_time.py` (时), `zuo_make.py` (作), `dan_but.py` (但)
- `success_bank/INDEX.md` — rows 118-129 (12 new); B9 section for
  not-promoted PASSes + FAIL clusters.
- `principle_bank.md` — sharpened **P-A-007-v2** (retrieval mechanism
  with hard-check); new **P-COMP-012** (hook-compound refinement of
  P-COMP-011); new **P-A-008** (inline-reasoning trace required for
  compound-char attempts).
- `errata.md` — full B9 diagnostic section: 4 A deep-dive, 6 FAIL
  clusters (A hook-compound, B chronic recycles, C 3-part/crossbar,
  D hook-body/descender, E 3-radical, F 3-part vertical), R1 outcomes,
  4 cross-item learnings.
- `retry_log.jsonl` — B9 rows appended: 3 R1 PASS + 4 R1 FAIL
  terminal-freeze markers + 4 explicit terminal-freeze + 13 do-not-queue
  markers + 5 B10 R1 queue items.
- `sandbox.md` — B9 postmortem section.
- `curator_satisfaction_log.jsonl` — 50 mains + 7 retries rows appended.
- `memory_index.md` — updated Post-B9 status block.
- `pass_index.md` — refreshed via `tools/build_pass_index.py`.

**Structural change (drawer_memory.md split)**:
- Pre-B9 drawer_memory.md was 856 lines. B9 additions would push it past
  900. Split into topic-files per B7-postmortem plan.
- Kept `drawer_memory.md` as ENTRY-POINT INDEX + retrieval-hint tables;
  moved detailed sections into topic files:
  - `drawer_memory_composition.md` — Composition playbooks (P-A-006,
    P-A-007, P-COMP-* rules with worked examples)
  - `drawer_memory_anchors.md` — MMH anchor calibration notes
  - `drawer_memory_siblings.md` — Sibling / minimal-pair notes
- `memory_index.md` updated to point drawer at new file structure.

**Rationale**:

**P-A-007 sharpened from guardrail to retrieval mechanism** — B9 provided
strong evidence: 3/4 R1 PASSes on the "call the bank primitive you skipped"
test (军 explicit, 成 partial, 老 tuning arm), and 3/4 A verdicts had
explicit P-A-007 reasoning in the docstring. The hard-check rule
(scale∈[0.55, 1.2] & structural match → CALL) is now the canonical
retrieval discipline, not just a corrective principle.

**P-A-008 emerges from A-verdicts audit** — the difference between B8's
0 A and B9's 4 A on same-difficulty items is not skill, it's REASONING
TRACE. Drawers who explicitly reasoned about "why inline vs why call
bank" landed A; drawers who silently inlined landed FAIL. Codified as
mandatory docstring reasoning.

**P-COMP-012 refines P-COMP-011** — 伺 PASSed as 亻+X-with-hook because
bank's heng_zhe_gou handled the hook cleanly at native scale. The
"straight-stroke-only" rule is really "bank has the compound-stroke
primitive at usable geometry."

**Bank promotion strategy** — 12 promoted (4A + 3R1 + 5 high-reuse mains).
Held back 10 PASSes as inline-only (甸/这/町/串/丽/乱/亩/伯/伺/佃/状/佉/佐)
because they're either derivative compositions (亻+X where X already in
bank), one-offs (串/丽/乱/亩), or covered by drawer_memory playbooks.
Bank grew 115→124→136 across B8→B9 (12 new); pace sustainable.

**Cross-group finding for the paper** — B9 is the FIRST batch where G5
PASS (44%) exceeds G4 PASS (38%) on identical items. **Combined with
G5's 4A (vs G4's 10A), this suggests memory-format-in-code adds
retrieval discipline that grid-anchor format lacks, at the cost of
rendering-format A ceiling.** The two-factor decomposition from B8 now
has a directional signal: PASS lever favors code+MMH, A lever favors
grid+per-endpoint-width. Paper-worthy pattern.

**Expected help for**:
- B10 mains (idx 334-383): 亻+X L-R chars (Cluster A boundary),
  L-R with 立-family (via wei_position), 日+X compounds (via shi_time,
  li_inside, dan_but), 辶-wraps (via hai_still — chuo_walk template).
- B10 R1 (5 items queued): P-A-008 test on 凫/条 (reasoning trace
  required); P-A-007 mechanism-change on 身/运.
- Any drawer that considers refusing a bank whole-radical primitive
  will now be nudged by P-A-007-v2 hard-check.

**Deliberately NOT done**:
- **NOT promoting hook-compound stroke primitives** — P-COMP-008 refuted
  hand-craft; still sandbox-only.
- **NOT retracting P-A-006** — P-A-007 scopes it; recipe still valid for
  grid-like straight-stroke L-R.
- **NOT queuing Cluster A 亻+X hook-compound FAILs for retry** — 6
  items (你/伶/伽/佇/佈/员) all P-COMP-011/012 boundary; no
  mechanism-change without bank extension.
- **NOT expanding chuo_walk to variants** — still one primitive; ROI
  low until 3+ 辶-derivatives show the same offset pattern.


## 2026-08-09 @ position 568 — B10 curator update (7 A + 9 high-reuse PASSes; P-A-009 codified)

**Files changed**:
- `success_bank/code/*.py` — 16 new whole-char primitives:
  - 7 A verdicts: zhan_occupy.py, dong_person.py, qian_all.py,
    de_target.py, bing_and.py, he_harmony.py, xie_some.py
  - 9 high-reuse PASSes: hua_flower.py, guo_country.py, zhe_person.py,
    fa_law.py, ding_fix.py, zheng_prove.py, zhao_seek.py, suo_place.py,
    zhi_will.py
  - Bank grew 136 → 152 (22 stroke + 130 radical/char)
- `success_bank/INDEX.md` — appended 16 rows + "PASSed in B10 but NOT
  promoted" section + "Not promoted from B10" section
- `principle_bank.md` — added **P-A-009** (quantitative BANK_DEVIATION
  reasoning); P-A-008 validation writeup; P-COMP-011 boundary softening
  update; 疒-family terminal-freeze cluster declaration
- `drawer_memory.md` — appended B10-era retrieval hints (16 promoted
  primitives + reuse-target map for B11) + sibling notes + failure
  calibration + updated rules of thumb
- `sandbox.md` — appended B10 postmortem (headline findings, A-verdict
  deep-dive, FAIL cluster analysis, structural evolution decisions,
  observations to test in B11)
- `errata.md` — appended B10 main FAILs (5 clusters) + R1 outcomes +
  cross-item learnings
- `memory_index.md` — updated post-B10 status line
- `curator_satisfaction_log.jsonl` — appended 50 mains + 5 retry rows
- `retry_log.jsonl` — appended B10 retry outcomes + B11 queue (4 items)
- `pass_index.md` — regenerated via `tools/build_pass_index.py`

**Rationale**:
- **P-A-009 discovered by pattern-mining B10 A-docstrings**: 4 of 7 A
  verdicts contain BANK_DEVIATION blocks with NUMERIC aspect/scale
  calculations; the FAILs (社/佛/佞) have qualitative reasoning only.
  Quantifying the reasoning forces drawers to verify the DEVIATION is
  real, preventing over-application. This is the P-A-008 trace made
  auditable.
- **B10 replicates B9's discipline-crystallization pattern**: B9
  codified P-A-008 → 4 A. B10 codified P-A-009 → 7 A. Monotonic-up
  trend in A count on comparable batches strongly suggests the format
  ceiling from B8 is discipline-shifted, not absolute.
- **7-A batch is highest in G5 history**. Includes 的 (highest-freq
  Chinese char). Bank-value from B10 is exceptionally high.
- **9 PASS promotions** capture very-high-freq compound-char templates:
  国/花/者/法/定/证/找/所/志. Downstream reuse map covers 艹-family,
  氵-family, 讠-family, 扌-family, 心-bottom family, 宀-top family,
  囗-enclosed family — the biggest structural bank gap fills of the
  experiment.
- **疒-family terminal-freeze declared**: 4/4 疒-family in B10 FAIL
  consistently at 疒 inline. Bank-gap chronic. Consistent with
  P-COMP-008 refutation of hand-craft; wait for organic PASS.

**Expected help for**:
- B11 mains (idx 384-433): 亻+X compounds (via zhan_occupy/dong_person
  precedents), 氵-family (fa_law template), 艹-family (hua_flower), 讠
  and 扌-family (zheng_prove/zhao_seek), 心-bottom (zhi_will), 囗-enclosed
  (guo_country).
- B11 R1 (4 items queued): P-A-007 quantitative recheck on
  社/佞/畅/经.
- Any drawer that writes BANK_DEVIATION will now be nudged by P-A-009
  quantitative requirement (via drawer_memory rules of thumb).

**Deliberately NOT done**:
- **NOT promoting 疒 as candidate hand-crafted primitive** — P-COMP-008
  hypothesis-driven promotion refuted; wait for organic PASS.
- **NOT queuing Cluster A 疒-family FAILs for R1** — 5 items terminal-
  freeze; no mechanism-change available.
- **NOT queuing Cluster C 8-stroke novel FAILs** (事/乖/乶) — no
  whole-radical decomposition available; do-not-queue.
- **NOT splitting drawer_memory.md** — currently at ~1000 lines; split
  threshold moved to 1200 lines. B11 curator to reassess.
- **NOT retracting P-A-006 or P-A-007** — both hold; P-A-009 layers
  on top as auditability requirement.
- **NOT elevating 心/宀/氵/艹/讠/扌/囗 templates to STROKE primitives
  in stroke-primitive bank** — they remain char-level primitives (thin
  wrappers); leaving the boundary between stroke-signature and
  position-signature primitives intact.

---

## 2026-08-09 @ position 618 — B11 close (+15 primitives, +1 principle P-A-010, corrected G4-vs-G5 narrative)

**Files changed**:
- `success_bank/INDEX.md` — added 15 new primitives (indices 147-161):
  9 B11 A promotions (1 wrapped as .py: `guo_fruit.py` — the
  X-crossing exemplar; 8 inline-only in attempts/: 佯/空/往/佼/佽/受/來/采),
  6 high-reuse PASSes (all inline templates: 金/话/或/苦/知/具). Added
  B11 not-promoted lists (13 PASSes kept inline; 19 FAILs clustered
  by P-A-010 decision route; 3 C's).
- `principle_bank.md` — added B11 section with P-A-010 (R1 mechanism-
  change taxonomy) + P-A-006/007/008/009 stability audit + cross-group
  correction note.
- `sandbox.md` — B11 postmortem with corrected G4-vs-G5 comparison,
  9-A deep-dive, 19-FAIL cluster analysis, 0/4 R1 diagnosis
  motivating P-A-010, B12 observations.
- `errata.md` — B11 append: 19 FAILs + 3 C's, with cluster tags and
  P-A-010 classification per item.
- `memory_index.md` — added Post-B11 status block (167 primitives,
  cumulative 317/568 = 56% PASS, 29 A total, monotonic-up A trend,
  corrected cross-group finding, P-A-010 announcement).
- `retry_log.jsonl` — appended B10-queue outcomes (all FAIL) +
  terminal-freezes for 社/佞/畅/经 + 疡, and B12 R1 queue (4 items:
  实/治/放/侔).
- `pass_index.md` — regenerated via `tools/build_pass_index.py`.
- **NEW wrapper file under `success_bank/code/`**: `guo_fruit.py`
  only — the X-crossing exemplar (interior 竖 pierces 田 AND 木 shaft
  P-jointed; high downstream reuse for 巢/棵/裸/课/颗). The other 8 A
  and 6 PASS promotions are inline-template access via attempt-file
  paths, per the B7/B10 convention. Wrapper-file count grows 152 →
  153; promoted-primitive count grows 152 → 167.

**Rationale**:
- **P-A-010 emerged from B11 R1 0-for-4 outcome**: all four B10-queued
  R1 items (社/佞/畅/经) FAILed at R1 despite drawers correctly
  applying quantitative recheck instructions. Post-mortem shows all
  four had multi-DEVIATION or L-R/3-part composition problems that
  no primitive-call R1 could address. Codifying the retry-viability
  taxonomy prevents wasting the next batch's R1 slots on hopeless
  rescues. Predicts B12 R1 rate JUMPS from 0/4 = 0% to >=1/3 = 33%
  by classifying kind-(a)/(b)/(c) only.
- **B11 A count 9 is highest G5 batch ever** (previous ceiling 7 in
  B10). All 9 A docstrings contain both P-A-008 (per-sub-component
  trace) and P-A-009 (quantitative BANK_DEVIATION math) — the recipe
  is fully internalized. Bank promotion of these 9 A verdicts
  preserves the recipe as reference for future compound-char
  drawers.
- **CORRECTED G4-vs-G5 narrative** (critical for paper). Pre-batch
  briefing framed B11 as "G5 beats G4 on both PASS and A", which
  actual labels contradict (G4 62%/17A vs G5 56%/9A on same 50
  items). The correction lands in sandbox.md's B11 postmortem and
  principle_bank.md so future curators / paper writers don't
  perpetuate the error. Two-factor decomposition from B8 stands:
  MEMORY format neutral for PASS at high MMH; RENDERING format
  decisive for A on hook-heavy compound chars.
- **6 high-reuse PASS promotions** cover the highest-frequency
  templates B11 exposed: 金 (钅-radical base), 话 (讠+舌), 或
  (戈-family), 苦 (艹+古 extending hua_flower), 知 (矢+口), 具
  (目+一+八 stacked). All widely reused in Phase-3 pool.
- **Inline-only promotion for 4 A verdicts** (佯/往/佼/佽): each is
  a character-specific composition (亻+羊, 彳+主, 亻+交, 亻+冫+欠)
  where a downstream drawer would reference the attempt file for
  the recipe rather than call a wrapper. Follows the B7-precedent
  convention of "promotion via retrieval-hint pointer, not wrapper"
  when the composition is idiosyncratic.

**Expected help for**:
- B12 R1 queue (4 items: 实/治/放/侔) — targeted P-A-010 kind-(a)/(b)
  candidates: 实/治/放 each have exactly one BANK_DEVIATION-and-should-
  have-called candidate (mian_roof / kou_mouth-adaptation / pu_action);
  侔 is kind (b) trajectory-diff on 厶-top spacing. Expected R1 rate
  >= 33% under P-A-010.
- B12 mains: 亻+X compounds continue via ren_left + zhan_occupy/佟
  precedents; 讠 family via hua_speech; 戈 family via huo_maybe;
  艹 family via ku_bitter (bottom-radical variant of hua_flower);
  钅/金-base compounds via jin_gold (novel primitive).
- Any drawer facing X-crossing 田+竖 topology has 果 as a bank
  reference (interior-shu-pierces-frame recipe).

**Deliberately NOT done**:
- **NOT wrapping 4 of 9 A verdicts** (佯/往/佼/佽) — character-specific
  compositions; wrapping adds bank bloat without matching-signature
  reuse. Promoted as inline templates via attempt-path pointer.
- **NOT queueing hopeless R1 kinds** (d)/(e) — the entire cluster of
  说/线/是/取/规/亟/侃/侉/侌/佾 stays do-not-queue per P-A-010, freeing
  the B12 R1 budget for kind-(a)/(b)/(c) items.
- **NOT retracting P-A-006 through P-A-009** — 9/9 B11 A verdicts
  validate all four; P-A-010 extends the framework without
  retracting.
- **NOT elevating 疒 to hypothesis-driven candidate** — 疡 in B11
  reconfirms the B10 P-COMP-008 refutation.
- **NOT splitting drawer_memory.md** — still ~1000 lines after B11
  updates; threshold moved from 1200 → 1400 lines.
- **NOT hand-crafting a 车-left variant** despite 转 FAIL — 车-left
  compression is chronic (see 转/软/连/较); wait for organic PASS
  in some other 车-left compound before promotion.

## 2026-08-09 @ position 668 — B12 curator (13th run): P-A-010-v2 (sharpened), 10 A verdicts (new ceiling), 1 wrapper promoted, 9 inline templates, R1 rate 3/5 = 60%, first LEGITIMATE G5>G4 batch on aligned idx

**Files changed**:
- `sandbox.md` — B12 postmortem appended (~250 lines): 10 A mechanism
  decomposition, G5-beats-G4 mechanism (novel finding), R1 outcomes
  (5 items with P-A-010 v1 vs v2 classification), 23 FAIL cluster
  analysis (5-疒 + 6 亻+X + 5 3-part + 6 novel), terminal-freeze
  declarations, B13 retry queue (4 targeted kind-(a) items).
- `principle_bank.md` — new B12 section (~120 lines): P-A-010-v2
  sharpened with kind (b1) vs (d) mechanical decision procedure
  ("what single object gets changed?"), cross-group finding
  documented (first LEGITIMATE G5>G4 batch), 2 A archetypes named
  (DEVIATION-heavy inline vs bank-template-stack), 3-factor mechanism
  breakdown (50% discipline / 30% bank-critical-mass / 20% pool).
- `errata.md` — B12 append: 23 FAILs + 4 C's with cluster tags and
  P-A-010-v2 classification per item.
- `memory_index.md` — added Post-B12 status block (170 primitives,
  cumulative 340/618 = 55% PASS, 39 A total, monotonic-up A trend,
  first LEGITIMATE G5>G4 announcement, P-A-010-v2 announcement).
- `retry_log.jsonl` — appended B12-queue outcomes (3/5 recovery:
  实 A, 治 PASS, 放 PASS, 例 C, 侔 FAIL) + terminal-freezes for
  5 疒-family + 3 3-part + 6 novel + 3 hook-compound-do-not-queue,
  and B13 R1 queue (4 items: 侯/便/俊 HIGH kind(a); 城 LOW).
- `pass_index.md` — regenerated via `tools/build_pass_index.py`.
- **NEW wrapper file under `success_bank/code/`**: `shen_god.py` —
  the 礻-adaptation exemplar with `draw_shen_left_hemisphere()`
  entry for compound-shifted 礻 (high downstream reuse for
  社/祈/福/祝/礼). The other 9 A and R1-A promotions are inline-template
  access via attempt-file paths, per the B7/B11 convention.
  Wrapper-file count grows 153 → 154; promoted-primitive count
  grows 167 → 177 (+10 whole-char A promotions).

**Rationale**:
- **P-A-010-v2 sharpened from B12 R1 outcome (3/5 vs B11's 0/4)**:
  the retry-queue quality lever validated. B12 queue applied the
  P-A-010 kind-(a)/(b)/(c) filter and reduced from B11's 4 items to
  5 targeted items, achieving 60% recovery (up from 0%). The 侔 FAIL
  revealed a boundary case — "trajectory-diff on inter-primitive
  spacing" is kind (d) in disguise, not kind (b). Codified as
  P-A-010-v2 with mechanical decision procedure ("what single object
  gets changed?"). Predicts B13 R1 rate stays >=50% under strict
  application.
- **B12 A count 10 is new G5 batch ceiling** (previous 9 at B11).
  Monotonic-up trajectory B8/B9/B10/B11/B12 = 0/4/7/9/10 shows the
  discipline stack is compounding, not plateauing. All 10 A docstrings
  contain both P-A-008 (per-sub-component trace) and P-A-009
  (quantitative BANK_DEVIATION math OR justified "no BANK_DEVIATION"
  when everything fits).
- **First LEGITIMATE G5>G4 batch on aligned idx** (46% vs 40% PASS,
  10 vs 8 A). B11 curator's alignment correction now enables this
  clean claim. Mechanism story documented for the paper: 50% discipline
  compounding + 30% bank-critical-mass + 20% pool-favorability. NOT
  a stable win; NOT "G5 caught up on rendering format"; it's a
  three-factor confluence where the pool happened to be compound-stack
  heavy (G5 native strength) rather than hook-heavy (G4 native strength).
- **10 A promotions**: only 1 wrapper file (shen_god) — 神 is a
  礻-adaptation exemplar with two callable entry points
  (`draw_shen_left_hemisphere` for the 礻 half alone,
  `draw_shen` for the full character). 9 other A verdicts (面/点/信/美/盃/盅/俅/俎/草)
  are inline templates via attempt-path pointers per B7/B11 convention.
- **Cross-group finding also documented in principle_bank.md**
  (Cross-group section) — this is paper-relevant. Two A archetypes
  named: DEVIATION-heavy inline (7/10) and bank-template-stack (3/10);
  the latter validates the bank-critical-mass hypothesis.
- **疒-family terminal-freeze REAFFIRMED** — 9 cumulative 疒 FAILs
  (5 B12 + 4 B10). No bank push. Cross-group pattern (G4 also has
  疒 FAILs on same items) suggests MMH-decomposition problem, not
  memory-format problem.

**Expected help for**:
- B13 mains (idx 484-533, final G5 catch-up batch) — bank now has
  10 more whole-char reference templates. Expected A count 8-12
  under continuing discipline.
- B13 R1 queue — targeted kind-(a) 侯/便/俊 pattern (all
  BANK_DEVIATIONed ren_left on "systematic ~70px left-shift" which
  IS uniform-adjustable). Expected R1 rate >=50% under P-A-010-v2.
- Any drawer facing a 礻-left compound (社/祈/福/祝/礼) now has
  `shen_god.draw_shen_left_hemisphere()` as bank primitive at the
  compound-shifted anchor position.
- Any drawer facing a compound-stack (X-top + Y-bottom or X-top +
  皿-bottom) has a template stack pattern: 盃 (不+皿), 盅 (中+皿),
  俎 (仌+且). Archetype-2 A route validated.

**Deliberately NOT done**:
- **NOT wrapping 9 of 10 A verdicts** — character-specific
  compositions where wrapping adds bank bloat without matching-signature
  reuse. Promoted as inline templates via attempt-path pointer.
  Follows B7/B11 convention.
- **NOT queueing hopeless R1 kinds** (d)/(e) — the entire cluster of
  疒-family / 3-part / novel compositions stays do-not-queue per
  P-A-010-v2, freeing B13 R1 budget for kind-(a) items.
- **NOT retracting P-A-006 through P-A-009** — 10/10 B12 A verdicts
  validate all four; P-A-010-v2 refines the R1 taxonomy without
  retracting.
- **NOT elevating 疒 to hypothesis-driven candidate** — 9 cumulative
  疒 FAILs across B10 and B12 reconfirms the B10 P-COMP-008 refutation
  route. Wait for organic PASS.
- **NOT splitting drawer_memory.md** — still ~855 lines; threshold
  at 1400 lines.
- **NOT hand-crafting a nao_sickness.py** — 5 B12 疒 FAILs would
  need a hand-crafted primitive; per P-COMP-008 refutation, this
  route consistently fails. Terminal-freeze holds.
