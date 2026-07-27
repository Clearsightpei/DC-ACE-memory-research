# Errata Scan — position 150 (G4 grid-bank)

Scan performed at curriculum position 150 (B2 → B3 boundary, right
after B2 batch judgment and the memory-restructure event at pos 150).
This is the FIRST scan under **v7 self-evolution**. Structural
context: principle_bank was split into three files at this position
— `principles_meta.md` (TR1-TR10, TR12; TR11 retired), `joint_atlas.md`
(P/T/N/S conventions), and NEW `form_catalog.md` (stroke class ×
context anchor patterns). The new lookup axis (stroke-in-context)
changes what "retrospective" now means for retry decisions: an item
whose failure mode was "no place to look up the correct 撇 shape for
this context" now has a place to look — and every PASSing attempt
seeds the catalog for future retries.

Cooldown rule: an item retried at curriculum position P is on
cooldown until P+50.

## New memory since previous scan (position 100)

- **File split (2026-07-18 @ pos 150)** — principles_meta / joint_atlas
  / form_catalog. Memory reading order re-ordered: form-context first,
  meta-rules second, joint-atlas on demand. Directly addresses the
  "drawer ran out of context on meta-rules" B2 failure pattern.
- **`form_catalog.md` (NEW)** — indexed by stroke × context. Currently
  populated with 12+ contextual patterns from B2 PASSes (氵, 灬, 忄,
  大/木/犬 X-crossings, 门 enclosing, 幺 stacked 撇折, 尢/毛 竖弯钩
  variants, 二/冫 S-class 点, etc.). Also seeded with a "known gaps"
  list naming 5 items I know I'm missing: **女, 寸, 弓, 马, 飞** —
  all of which are in active errata. These 5 are retrospectively
  unlocked: even without a full recipe, the catalog now names the
  missing pattern explicitly, and errata already has the concrete fix.
- **TR11 retired** — Named-agreement rule dropped from meta-rules.
  B1 empirical showed 63% pass with TR11 vs 74% without; on B2 the
  gap widened. Retries that "rubber-stamped" TR11 fields still hit
  the human PASS at similar rate.
- **B2 retry outcomes fresh (pos 150)** — 彐 and 门 PASSed (TR8
  rule 5 / TR9 enclosing-span both validated). 冂 & 己 & 弓 & 马 &
  㔾 & 飞 & 犭 FAILed with concrete new diagnosis notes in errata
  (see B2 retry entries).

## Cooldown status

- **B2 retries (冂, 㔾, 飞, 弓, 己, 马, 犭)** were attempted at
  position ~100 with retry_n=1. Cool-down of 50 items expires
  exactly at position 150 — they are **eligible again**, and every
  one has a fresh B2-retry-fail diagnosis to build the next attempt
  on. This is a natural moment to give them a second retry.
- **B1 retries (丿, 刀)** were at retry_n=1 during B1 (position ~60).
  Cool-down long expired. Both have prospective and retrospective
  reasons — Phase-3 head at 172/200 IS the exact same character.
- **B1 main FAILs** (卩, 力, 艹, 寸, 彑, 女, 025_力, etc.) all still
  retry_n=0, not on cooldown.
- **B2 main FAILs** (30 items, positions 070-118) all still retry_n=0,
  not on cooldown.
- **Phase-1 items** (横斜钩, 横折弯钩, 横折折撇) at retry_n=2. Cool-down
  expired long ago. No new compound-stroke primitive since B2.

## Item-by-item decisions

### Phase-1 items — SKIP all (unchanged from pos 100)

Retry_n=2 already. No new inlining primitive since batch 6 refresh.
Downstream 151-200 doesn't use these strokes as visible components.
**SKIP** 横斜钩, 横折弯钩, 横折折撇.

### p2_radical_003_丿 — RETRY (STRONG (a) + (b))

- **(a) Prospective — STRONGEST**: 丿 IS Phase-3 curriculum
  position 172. If retried before 172 and it PASSes, it graduates to
  bank; if it fails, position 172 gets to try again with the fresh
  diagnosis. Either way, having a validated 丿-standalone recipe
  before position 172 is a direct win. Also 丿-as-component appears
  in 人 (178), 入 (194), 乃 (176), 乂 (177), 九 (191).
- **(b) Retrospective — STRONG**: `form_catalog.md` § 撇 → "standalone
  丿 radical" now has the anti-diagonal recipe verbatim: head
  ('TR', 0.85, 0.15), tail ('BL', 0.15, 0.85), head_w 14-16, curve
  0.10-0.15. This is the errata fix promoted into the catalog. Drawer
  will look at the catalog first (per updated memory_index.md) and
  see the exact anchors. No excuse for another under-span attempt.
- **Verdict**: **RETRY.**

### p2_radical_015_刀 — RETRY (STRONG (a) + (b))

- **(a) Prospective — STRONGEST**: 刀 IS Phase-3 curriculum position
  200. Same argument as 丿.
- **(b) Retrospective — STRONG**: The B1 retry-1 failure diagnosis
  in errata gives a very concrete anchor plan (shorten top 横 corner
  to MR 0.10; vertical descender to BC 0.60, 0.60; 撇 tail BL 0.35,
  0.85). `joint_atlas.md` § T explicitly documents the head-share
  T-weld pattern for two-stroke radicals. `form_catalog.md` context
  entries for 横折钩 in enclosing role directly transfer.
- **Verdict**: **RETRY.**

### p2_radical_025_力 — RETRY (STRONG (a) + (b))

- **(a) Prospective — STRONGEST**: 力 IS Phase-3 curriculum position
  192. Also same compound structure recurs in 勺, 勿 (though not in
  151-200). Building 力's mastery before 192 is direct prerequisite.
- **(b) Retrospective — STRONG**: `joint_atlas.md` § T explicitly
  requires 撇 head to share anchor with 横折钩 head (upper-LEFT,
  T-weld). `form_catalog.md` 撇-in-side-position entry directly
  applies. Errata fix from B1 (撇 head shares anchor with 横折钩
  head at TL) is literal and now supported by the catalog.
- **Verdict**: **RETRY.**

### p2_radical_024_冂 — RETRY (STRONG (a) + (b))

- **(a) Prospective — STRONGEST**: 冂 IS Phase-3 curriculum position
  193. Also transferable to 冖 (196), which needs enclosing-radical
  discipline. 门 (already B2 retry-PASS via TR9 enclosing-span) is
  the sibling proof of concept.
- **(b) Retrospective — STRONG**: B2 retry-1 fail diagnosis is
  crisp: "s1 head at y=25 drops below s2 top-bar left endpoint at
  y=10 — left corner has visible overshoot; reduce frame width to
  ~230 for canonical proportion." Combined with `form_catalog.md`
  § 竖 → "enclosing left wall" entry (from 门 PASS), the fix has
  a concrete recipe.
- **Verdict**: **RETRY.**

### p2_radical_050_弓 — RETRY (STRONG (b), moderate (a))

- **(a) Prospective — MODERATE**: 弓 doesn't appear directly in
  151-200. But the 3-tier stacked-loop discipline recurs in 3-stroke
  characters with vertical-stack composition.
- **(b) Retrospective — STRONG**: `form_catalog.md` "Known gaps"
  section explicitly names "弓 tier-separation" as a documented
  missing pattern with concrete y-band recipe (s1 y_frac 0.0-0.35;
  s2 y_frac 0.45-0.50; s3 y_frac 0.65-1.0). B2 retry-1 fail added
  further diagnosis: "s1 drop went down-left (column mismatch,
  TR8 rule 6 violation); s3 loop inverted." Fresh diagnosis + catalog
  gap = ripe for another try. Reuse `shu_zhe_zhe_gou.py` for s3.
- **Verdict**: **RETRY.**

### p2_radical_058_马 — RETRY (STRONG (b), weak (a))

- **(a) Prospective — WEAK**: 马-family not in 151-200. But
  compound-descender-plus-hook pattern (shu_zhe_zhe_gou) recurs in
  many characters with right-side descender+hook composition.
- **(b) Retrospective — STRONG**: `form_catalog.md` "Known gaps"
  names "马 as 3 strokes: 横折 top + 竖折折钩 right-descender-hook +
  horizontal through middle" as a documented gap. B2 retry-1 fail
  added: "top-box too small; S2 first leg slants left-down; S3
  bottom heng overlaps S2 hook_pt." Concrete fix in errata (enlarge
  top-box, straighten S2 first leg to strict vertical per TR8
  column-share, separate S3 heng from S2 hook_pt by ≥25 px in y).
- **Verdict**: **RETRY.**

### p2_radical_047_飞 — RETRY (STRONG (b), moderate (a))

- **(a) Prospective — MODERATE**: 飞 not in 151-200. But sandbox
  Pattern E ("long compound strokes = one inlined variable-width
  polyline") transfers to any character with a large sweeping top
  piece. Positions 176 (乃), 187 (九), 191 (九 dup) all have
  large-sweep top pieces.
- **(b) Retrospective — STRONG**: `form_catalog.md` "Known gaps"
  names "飞 as ONE inlined variable-width top piece + one small
  inner mark" as a documented gap. B2 retry-1 fail added the
  precise pixel measurement: "s1 rises 115 px over 225 px x →
  reads as diagonal not horizontal." Concrete fix: single polyline
  with head ML(0.2, 0.3) + bend TR(0.5, 0.4) + tip BR(0.5, 0.9).
- **Verdict**: **RETRY.**

### p2_radical_061_女 — RETRY (STRONG (b), weak (a))

- **(a) Prospective — WEAK**: 女 as radical not in 151-200. Some
  女-family characters (奶/她) not upcoming this batch.
- **(b) Retrospective — STRONG**: `form_catalog.md` "Known gaps"
  explicitly names "撇 in 女 (must P-weld with the top horizontal at
  upper-mid, NOT lower-left — B1 failed here)". Concrete B1 errata
  fix: s1 撇点 head ('TC', 0.35, 0.20) with pivot ('C', 0.30, 0.85);
  s2 撇 crossing s1 near center; s3 horizontal arm at y_frac ≈ 0.60
  spanning wide, all 3 joints P-welded per MMH. `joint_atlas.md`
  § P shared-pixel rule directly applies to the 3× P-welds.
- **Verdict**: **RETRY** (retrospective triggered by catalog gap).

### p2_radical_053_己 — RETRY (MODERATE (b), weak (a) now that 巳 passed)

- **(a) Prospective — WEAK-MODERATE**: 巳 (pos 103) already PASSed
  as `si.py`, so the strongest prospective driver from pos 100 is
  gone. However, the 竖弯钩-with-canonical-up-hook idiom recurs in
  Phase-3 upcoming characters with 己/巳/已 components.
- **(b) Retrospective — MODERATE**: B2 retry-1 fail diagnosis is
  concrete: "s1 head and s3 head both at ~(85, 80) — overlapping;
  s1 tail y (130) is 130 px above s3 corner y (240); three tiers
  disconnected even with s2." Errata fix: enforce s1.tail y aligned
  with s2 body region; use `heng_zhe.py` with straight down drop;
  share anchor tuples at intended endpoints per TR4. TR8 rule 5
  (same-row 横) directly applies. `form_catalog.md` § 竖弯钩 in 儿
  vs 尢 variant table gives an adaptable canonical up-hook recipe.
- **Verdict**: **RETRY** (fresh B2 diagnosis + catalog references).

### p2_radical_114_日 — RETRY (STRONG (a) + moderate (b))

- **(a) Prospective — STRONG**: 曰 (pos 161) is essentially 日's
  wider-shorter sibling — same enclosing box + middle horizontal.
  Passing 日 first would produce a `ri.py` primitive that 曰 can
  reuse (widen the box, keep the middle bar). 月 (pos 162) also
  benefits from the enclosing-box-with-inner-strokes discipline.
- **(b) Retrospective — MODERATE**: B2 diagnosis was precise:
  "middle 横 only 65 px wide (frame is ~200) — doesn't reach right
  wall. 日 requires middle bar touching both walls." Errata fix:
  "extend s3 tail to C or MR so it reaches right wall (x=250);
  same for s4 tail." `form_catalog.md` § 横 → "long middle 横
  crossing a 竖" entry (from 木, 车 PASSes) gives full-width
  anchors ('ML', 0.1, 0.45) → ('MR', 0.9, 0.45). Adapt for
  the middle-bar-inside-囗 idiom.
- **Verdict**: **RETRY** (strong (a) via 曰/月, moderate (b)).

### Items I considered and SKIP

- **p2_radical_062_犭** — Sibling 犬 (145) already PASSed as
  `quan.py`; no upcoming 犭-family in 151-200. B2 retry-1 fail
  diagnosis is subtle (belly hooks wrong direction — mirror-of-犬
  needed). Fix is anchor-tuning, not new principle. SKIP for now;
  can retry post-B3 if 犭-family appears.
- **p2_radical_038_㔾** — 巳 (103) already PASSed. Prospective
  gone. B2 retry-1 fail says J-shape belly issue. Fix is inlining
  wan_gou tighter. SKIP — no compelling driver now.
- **p2_radical_023_卩** — No 卩-family in 151-200. Only
  stroke-count-parity discipline (already generalized elsewhere).
  SKIP.
- **p2_radical_039_艹** — 艹-family not upcoming. SKIP.
- **p2_radical_045_寸** — 寸-family (对/村/守) not in 151-200.
  Catalog gap named but no upcoming beneficiary. SKIP.
- **p2_radical_055_彑** — No 彑/彐-family upcoming (彐 already
  PASSed as retry). SKIP.
- **All 30 B2 main FAILs except 日** — spot-checked each for
  overlap with 151-200; only 日 has direct sibling (曰). Others:
  纟/夕/夂/子/夊/贝/比/长/歹/斗/厄/方/风/戈/户/火/旡/见/斤/耂/肀/爿/攴/气/欠/氏/礻/手/殳
  — none appear as component in the upcoming 50 items. **SKIP
  all 29.** They remain in errata and eligible for scan @ pos 175.

## Summary

**RETRY (10)** — balanced, not minimalist, driven by concrete (a)/(b):

1. p2_radical_003_丿   — (a) Phase-3 pos 172 IS 丿, (b) catalog recipe
2. p2_radical_015_刀   — (a) Phase-3 pos 200 IS 刀, (b) errata + joint_atlas T
3. p2_radical_024_冂   — (a) Phase-3 pos 193 IS 冂, (b) retry-1 diagnosis
4. p2_radical_025_力   — (a) Phase-3 pos 192 IS 力, (b) form_catalog + T-weld
5. p2_radical_047_飞   — (b) catalog "Known gap" + retry-1 pixel diagnosis
6. p2_radical_050_弓   — (b) catalog "Known gap" + tier y-band recipe
7. p2_radical_053_己   — (b) fresh B2 retry-1 diagnosis + TR8 rule 5
8. p2_radical_058_马   — (b) catalog "Known gap" + shu_zhe_zhe_gou reuse
9. p2_radical_061_女   — (b) catalog "Known gap" + 3× P-weld recipe
10. p2_radical_114_日  — (a) 曰 (pos 161) sibling, (b) full-width middle bar

**SKIP** — 3 Phase-1 items (no new primitive) + 犭 + 㔾 + 卩 + 艹 +
寸 + 彑 + 29 B2 main FAILs (no upcoming overlap). Total skipped ~40.

## Rationale for size (10 retries)

- Position 100 scan retried 9; 2/9 PASSed (22%), 7/9 FAILed. The
  22% rate would ordinarily argue for more conservatism, BUT the
  memory landscape has changed materially at position 150:
  - form_catalog.md exists as a lookup layer that didn't exist at
    position 100.
  - 5 of the 10 retries are on the catalog's explicit "Known gaps"
    list (弓, 马, 飞, 女, 寸-skipped, plus form/errata support for
    others).
  - The 7 B2 retry-FAILs from pos 100 now each carry a NEW concrete
    B2-retry-1 fail diagnosis pinpointing the exact px error — this
    is qualitatively better ammunition than pos 100 had.
- 4 of 10 retries have the strongest possible prospective: the item
  IS in upcoming curriculum 151-200 as a Phase-3 character.
- Prior-run guidance: 2/18 was TOO conservative. Balance not
  minimalism. 10/27 ≈ 37% eligibility use, all with real triggers.
- 犭, 㔾 skipped because the prospective driver (犬 sibling, 巳
  sibling) has already passed — retrospective alone is weak here.

Re-evaluate at scan position 175.
