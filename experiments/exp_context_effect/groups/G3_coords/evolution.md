# G3 memory-structure evolution log

Append-only. One entry per structural change to G3's memory
organization. Format described in `../G2_free_form/evolution.md`.
This log is the emergence record — how G3's memory (within its
callable-Python-function constraint) evolves.

---

## 2026-07-18 @ position 150 — evolution log created

**Files changed**: created `evolution.md` and `memory_index.md`.

**Rationale**: v7 protocol change (see `README.md` v7 changelog).
Memory self-evolution unlocked after G3 underperformed in B1 (54% vs
G1's 60%) and collapsed in B2 (34% vs G1's 38%). Cumulative through
118 items: G3 49%, worst of the four groups. Diagnosis: G3's
principle bank filled with meta-cognitive rules (TR1-TR9 "when to
use bank vs inline") rather than contextual form/position knowledge
(e.g. "in left-radical position, 竖 shortens to 60-70%"). The
Success Bank stored frozen concrete instances that didn't transfer.
Deeper root cause: memory format and structure were externally
prescribed, which contradicts the research question about *emergent*
memory. The evolution unlock lets the curator restructure memory
freely within G3's callable-Python constraint. This log tracks
whether and how the curator converges on a useful structure.

**Expected help for**: nothing yet — this is the baseline entry. The
first real change (curator creates a new file, splits an existing
one, or introduces a new bank category) should describe what it
expects to help with.

---

## 2026-07-18 @ position 150 — B2 curator: signature-restriction response

**Files changed** (this is the first substantive v7 evolution):

1. **Split `principle_bank.md` into three focused files**:
   - `principles_meta.md` (new) — TR1-TR7 (how to use the bank)
   - `principles_stroke_family.md` (new) — P1-P11 (stroke-family
     observations; P11 is new)
   - `form_catalog.md` (new) — stroke × context lookup with concrete
     angle/taper/bow numbers from prior PASSes
   - `principle_bank.md` reduced to a redirect stub

2. **Retired TR8 "INLINE-FRESH TEST" and TR9 "bank-size discipline"**.
   Documented in `principles_meta.md` under "RETIRED RULES".

3. **Added adaptive helpers to `success_bank/code/_shared_helpers.py`**:
   `variant_pie(t, head, tail, bow_perp, w_head, w_tail)`,
   `variant_na(...)`, `variant_dian(...)`, plus shared `tapered_bezier`
   / `tapered_line` / `to_px` used by new B2 bank entries.

4. **Restructured `memory_index.md`** — drawer read order now goes
   form_catalog → adaptive helper → frozen bank → meta-rules. The
   previous order put meta-rules first, which drawers cited but
   didn't help their pass rate.

5. **Added 17 B2 PASS entries to `success_bank/code/`**
   (INDEX entries 68–84). Some entries use the new adaptive helpers;
   most are frozen concrete instances that also populate
   form_catalog.md rows.

**Rationale (evidence-based, from B2 result)**:

G3's pass rate collapsed in B2: 78% (bootstrap) → 54% (B1) → 34%
(B2). Cumulative 49% — WORST of four groups. All 8 retries FAILed
despite TR8 compliance.

User diagnosis (verbatim): "The problem isn't they don't know the
strokes, but rather how to change them into the proper form or put
them into the correct position. There are many types of 点, 撇,
they all look different and have different angles. Memory is
restricting them too much."

Concrete evidence from B2 fails:
- **077_忄**: needed mirrored dot — dian primitive is one-directional,
  scale can't reflect.
- **112_欠**: heng_gou primitive's x-span is fixed at 190px; scaling
  doesn't shrink it.
- **100_见**: box aspect needed is tall (like 日), kou is 1:1.
- **088_长**: 捺 sweep needs a bow_perp that scale can't produce.

These are NOT compliance failures. Drawers correctly applied TR8.
The failure is that `(ox, oy, scale)` cannot express angle
reflection, non-uniform aspect, curve bow, or per-stroke taper
variation. Meta-rules told the drawer "when to inline" but not
"what the inline should look like".

The v7 unlock made restructuring possible. Response chosen:

- KEEP callable-Python constraint (G3's identity).
- ADD adaptive helpers (variant_pie/na/dian) — callable Python that
  exposes the hidden knobs.
- ADD form_catalog.md — indexed by stroke × context, populated with
  concrete numbers from every PASS. Drawer looks up "撇 in top-left
  short position" and gets `head, tail, bow_perp, widths` to feed
  into variant_pie.
- SPLIT principle_bank so form-catalog (the real knowledge gap) is
  visually prominent rather than buried under a wall of meta-rules.
- RETIRE TR8/TR9 as documented dead memory (they fired but didn't
  help — leaving them adds noise).

**Expected help for**:
- Signature-restriction fails (077, 083, 088, 098, 100, 112, 113,
  117) — should PASS on retry with variant_pie/na/dian at
  form_catalog numbers.
- Any future radical whose 撇 or 点 form differs from the frozen
  primitive — drawer can find the right variant in form_catalog
  and skip the from-scratch derivation.
- Meta-rule read overhead — split files reduce retrieval noise.

**Measurement plan for B3 (positions 151–200)**:
- Track: does any B3 attempt import from `_shared_helpers.py`? Grep
  its `generated.py` files for `variant_pie`, `variant_na`,
  `variant_dian`, `_shared_helpers`.
- Track: does any B3 attempt cite `form_catalog.md` in comments?
- Compare B3 pass rate to G1 no-memory control. Bootstrap →B1→B2
  gap was -6 → -6 → -4. If v7 helps, B3 gap should turn positive
  (G3 ≥ G1) or at least close further.
- If B3 gap is still negative: revisit. Next lever would be
  auto-generating form_catalog entries from every PASS at the
  curator step (so drawers accumulate context recipes without
  manual curation), or reorganising bank into position-role
  subdirectories.

**Not changed (deliberately)**:
- Success Bank storage unit — still one `.py` file per mastered item.
  Only new-B2 entries use the adaptive-helper pattern; existing 67
  entries are untouched.
- The 20 curriculum rules (shared_rules.md) — those are protocol
  constants.

---

## 2026-07-22 @ position 200 — B3 curator: second-pass v7 (composition + retrieval)

**Files changed** (surgical, not a wholesale redesign — B3 evidence
pointed to a specific gap, not a total-format-failure):

1. **Extended `_shared_helpers.py`** with joint/weld helpers:
   - `bezier_point(p0, p1, p2, u)` — sample a quadratic bezier at u.
   - `line_point(p0, p1, u)` — sample a straight line at u.
   - `pie_point(head, tail, u, bow_perp)` — sample a variant_pie curve.
     Used to compute the exact pixel where a crossing/welding stroke
     should meet.
   - `kiss_apex(pie_head, pie_tail, na_tail, u_pie, bow_pie)` — returns
     the two math-coord pixels the pie and na should use for their
     heads, guaranteeing they share an exact pixel. `u_pie=0.0` for 人
     (kiss at apex), `u_pie=0.3` for 入 (na on shaft midway),
     `u_pie=0.5` for 大 (crossing at midpoint).
   - `mirror_dian_pair(shaft_x, y_center, spread, w_tail, tilt)` —
     returns a `(left, right)` tuple of kwarg-dicts you spread into
     `variant_dian`, guaranteeing the two dots mirror correctly around
     `shaft_x`. Addresses the 忄 / 丷 / 火 / 犬-side-dot family.

2. **Added `form_catalog.md` worked composition examples** for:
   - X-crossing family (人, 入, 大, 犬, 乂, 文) — full code snippet
     showing `kiss_apex` use.
   - Mirror-dot family (忄, 丷, 火) — full code snippet showing
     `mirror_dian_pair` use.
   - Radical-alias family (Phase-3 chars ≡ Phase-2 radicals) — full
     retrieval procedure.
   - **Retrieval discipline** paragraph: "copy from EXACT context,
     not similar-looking context; if no exact row exists, copy widths
     + bow_perp only, re-derive positions".

3. **Added 29 B3 PASS entries to `success_bank/code/`**
   (INDEX entries 85–113). All under standard `.py` files per the
   callable-function constraint. Six use adaptive helpers directly
   (`wen.py`, `xin.py`, `yao.py`, `yue.py`, `zhao_top.py`, `pie_char.py`,
   `yi_cross.py`); the rest are frozen concrete instances or aliases.

4. **Reorganised `memory_index.md`** rendering-approach section:
   - New priority-1 step: Phase-3 char with Phase-2 radical alias →
     try IDENTITY first.
   - New priority-2 step: if strokes must share a pixel → use
     `kiss_apex` / `pie_point` BEFORE variants.
   - New priority-3 step: for mirror-dot pairs → use `mirror_dian_pair`
     instead of hand-tuning.
   - Retained form_catalog → variant helper → bank primitive → fresh.

5. **Appended B3 satisfaction log** (63 lines) and **retry_log** (13
   lines) — standard bookkeeping, not a structural change.

**Rationale (B3 evidence-based)**:

B3 results:
- Main 29/50 = 58% PASS. Recovery from B2's 34%, but the recovery is
  largely from easy Phase-3 chars that alias to Phase-2 radicals
  (identity or near-identity). The Phase-2 tail (王, 止, 水, 见, 长, etc.)
  still fails.
- Retries: **0/13**. Even with variant_pie/na/dian available, no
  retry PASSed.
- Cumulative 200 items: 52%. Still below G1 no-memory 54%.

Helper-usage investigation:
- **7 of 13 retries USED the variant helpers**. So the drawer DOES
  reach for them.
- **5 of those 7 showed fail-mode SHIFT**: the specific stroke targeted
  by the helper improved (e.g., 忄's left dot now mirrored correctly);
  a DIFFERENT part of the character became the failure (dot position,
  or shaft-vs-dot proportion). The helpers work in isolation; they
  don't help composition.
- 6 of 13 didn't use helpers (X-crossing family — 人, 入, 大, 刀, 火, 手)
  — those drawers went inline-fresh, same fail mode as pre-v7.

Diagnosis: **the v7 first-pass solved per-stroke-form; it did NOT
solve composition (joint geometry) or retrieval discipline (copy
from exact vs. similar context)**. Both are addressed here:
- Composition: `kiss_apex` / `pie_point` / `mirror_dian_pair` make
  weld pixels explicit.
- Retrieval discipline: worked examples + explicit "copy widths only,
  re-derive positions" rule.

Options considered but NOT taken:
- **Kill the retry mechanism entirely** (0/N would justify). Held off
  because B3 evolution introduces new levers (composition helpers);
  fair to test them on the retry set before retiring.
- **Auto-generate form_catalog entries from every PASS**. Nice but
  doesn't fix retries; deferred.
- **Reorganise bank by position-role subdirectories**. Would break
  existing imports; low expected impact vs cost. Deferred.
- **Full principle-file merge back into one file**. Split was fine;
  drawers navigate the three files. Kept.

**Expected help for**:
- X-crossing retries (人 retry_4, 入 retry_4, 大 retry_4, 犬 retry_2,
  火 retry_2) — should PASS if drawers use `kiss_apex` for the apex/weld
  pixel.
- Mirror-dot retries (忄 retry_2, 丷 retry_4, 丬 retry_2) — should PASS
  if drawers use `mirror_dian_pair` instead of hand-tuning.
- Phase-3 chars whose bank alias was missed (e.g., 乛 → heng_gou_radical,
  冂 → jiong_radical) — added to memory_index priority-1 with
  identity-alias table pointer.

**Measurement plan for B4 (positions 201–250)**:
- Track: do X-crossing retries move (人, 入, 大, 犬, 火)? Grep for
  `kiss_apex` in retry generated.py files.
- Track: does the mirror-dot family finally PASS on retry? Grep for
  `mirror_dian_pair`.
- Track: does form_catalog identity-alias table save any Phase-3 char
  fails (grep new attempts for identity-alias comments)?
- If retries still ≤10%: retire the retry mechanism in B5 and put
  attention entirely on the main curriculum.
- If X-crossing family passes: the "composition" hypothesis is
  vindicated; consider adding more joint helpers (e.g., `cross_point`
  for straight-line crossings, `weld_endpoint` for L-corner joins).

**Not changed (deliberately)**:
- Success Bank storage unit — still one `.py` file per mastered item.
- Principle file split (three files) — split is working.
- TR8/TR9 retirement — still retired.
- Retry mechanism — kept for one more batch to test the new helpers.

---

## 2026-07-23 @ position 250 — B4 curator: third-pass v7 (retry-time retrieval + cross-transfer)

**Files changed** (targeted, evidence-driven — the persistent gap is now
diagnosable to a specific channel, not the memory storage format):

1. **Restructured `memory_index.md`** with a new "RETRY-TIME CHECKLIST"
   section at the top (before the read order). The checklist forces the
   drawer to answer, in a comment at the top of `generated.py`, three
   binary questions before writing any code on a retry:
   - Q1: Is this fail-mode in `errata.md`? What fix-idea does it list?
   - Q2: Does `form_catalog.md` have a row for the failing stroke×context?
   - Q3: Is there a helper (`kiss_apex`, `pie_point`, `mirror_dian_pair`,
     `variant_*`) that addresses the stroke class in the fail-mode?
   Purpose: make retrieval EXPLICIT so it can't be silently skipped by
   the retry-prompt's "fresh from GT" injunction.

2. **Added a "Char↔Radical cross-transfer" section** to `memory_index.md`
   and populated an initial table:
   - **兀**: char PASSes as `wu_char.py` (heng 0.85 + er_ren 0.95) —
     radical still FAILS at retry_2 with heavier calligraphic widths.
   - **门**: char PASSes as `men_char.py` (inline dian + 竖 + 横折钩 for
     tall aspect) — radical FAILS at retry_2 with different inline.
   - **子**: char PASSed AND radical retry graduated (aligned recipe).
   When a Phase-3 char passes and the corresponding Phase-2 radical is
   in errata: the char recipe is a valid retry candidate. Prospective
   B5 scan should pick these.

3. **Extended `form_catalog.md`** with:
   - 5 new rows for 撇 contexts (亼-roof, 丫 fork, 之 corner-continuing,
     久 top/middle).
   - 4 new rows for 捺 contexts (亼 right, 丫 mirror, 久 sweep, 之 平捺).
   - 2 new rows for 点 (之 top, 叉 crook).
   - 7 new rows for 横 (亼 base, 三 3-line pattern, 上/下/于/亍/亡/子).
   - 12 new composition patterns (刁, 丁, 勹, 亍, 于, 亡, 亼, 子, 叉, 兀char,
     门char, 卄, 孑).
   - 8 new identity-alias rows (刂, 囗, 山, 干, 口, 艹, 宀, 小).
   - **New retrieval discipline paragraph**: the "char == radical" alias
     pattern is now dominant in Phase-3 (8 of 27 B4 PASSes were 1-line
     aliases); and the "radical FAIL doesn't block char PASS" asymmetry.

4. **Added 27 B4 PASS entries to `success_bank/code/`**
   (INDEX entries 114–140). Naming: `<pinyin>_char.py` for Phase-3
   char entries. `zi_char.py` uniquely also exports `draw_zi` (radical
   graduation aliases the char recipe).

5. **Appended `curator_satisfaction_log.jsonl`** (58 lines) and
   **`retry_log.jsonl`** (8 lines) — standard bookkeeping.

**Rationale (B4 evidence-based)**:

B4 results:
- Main 27/50 = **54%** (down from B3's 58% — recovery has plateaued).
- Retries **1/8 = 12%** — the first non-zero retry batch since B1.
- Cumulative through position 250: **52%**. G1 no-memory: ~55%. G3
  still ~3pp below control. FOUR consecutive batches of underperformance.

Helper-usage grep on retries: **zero**. Not one B4 retry imported
`kiss_apex`, `pie_point`, or `mirror_dian_pair` — the exact helpers
added in B3's second pass specifically to address the retry fail
modes. This includes 夂/夊/兀 whose retry rationales EXPLICITLY named
the helpers.

Meanwhile MAIN attempts DO import them (6 files: 大, 个, 久, 亼, 夂,
及). So the retrieval mechanism works on the main prompt but breaks
on the retry prompt. The retry-dispatcher prompt likely biases the
drawer toward "fresh inline from GT + errata fix-idea", crowding out
the memory_index step-2 pointer to composition helpers.

The lone retry PASS (子) confirms this pattern: it PASSed via
hand-inline recipe with no helper imports, following the errata fix
idea verbatim. Memory helpers did NOT contribute.

**Diagnostic decomposition of the persistent 3pp gap**:

- Content (memory MISSING specific contexts): partial — form_catalog
  now covers most B3+B4 fail-mode stroke families. Adding rows helps
  main attempts. Deferred: envelope-shape family (飞, 丸, 己), mirror-提
  family (孓).
- Retrieval (drawers DON'T cite memory): **CRITICAL on retry path**.
  Main path is fine (24% import rate). Retry path is 0%. THIS is the
  gap.
- Format (callable-Python wrong unit): rejected. 27/27 main PASSes
  worked fine as callable functions. Format is not limiting.
- Radical evolution (per-radical-class subdirs, auto-gen from PASS):
  deferred. Would add navigation cost without addressing the retry
  retrieval gap.

**Options considered**:

- **Option A**: retry-time memory checklist injected into memory_index.md.
  PRO: forces explicit retrieval on retry path. CON: cosmetic — drawer
  can still ignore the questions. Mitigation: chose YES because
  the answers must be WRITTEN into the retry generated.py header, so
  they're auditable.
- **Option B**: kill the retry mechanism entirely (1/29 across three
  batches ≈ 3%). CON: retry contributes almost nothing but the ONE
  graduation (子) shows non-zero potential. Also killing removes a
  research signal (can memory improve on failure?). REJECTED for now;
  will re-evaluate at B5.
- **Option C**: char↔radical cross-transfer. CHOSEN. When a Phase-3
  char passes and the corresponding radical is in errata, the char
  recipe is documented as a retry candidate. Low cost; validated by
  子's B4 pattern (though 子 didn't need this — the recipes align
  organically for compact chars).
- **Option D**: fail-mode-categorised retry prompts. Would require
  editing the dispatcher (protocol change beyond curator scope).
  DEFERRED.
- **Option E** (radical): auto-generate a form_catalog row from every
  main PASS. Would grow catalog to 140+ rows; drawer navigation cost
  probably outweighs the recall benefit. REJECTED for now.
- **Option F** (radical): reorganise Success Bank into
  `success_bank/code/{strokes,radicals,characters}/` subdirectories.
  Would break existing imports; low expected impact (drawers are
  finding INDEX rows fine). REJECTED for now.

Chosen: **A + C**. Both cheap; both directly address the retry-retrieval
gap that is now the single largest lever.

**Expected help for B5 (positions 251–300)**:
- Retries: helper-import rate should rise from 0% to at least 30% if
  the checklist works. Retry PASS rate should follow.
- Main: identity-alias pattern is now explicit; expect more 1-line
  aliases and higher confidence on Phase-3 easy chars.
- 兀 / 门 / 女 (radical): back-port CHAR recipes as retry candidates.

**Measurement plan for B5**:
- Grep retry `generated.py` for `kiss_apex|pie_point|mirror_dian_pair|
  _shared_helpers`. Goal: ≥3 of ~8 retries import them.
- Grep retry `generated.py` for "Q1:", "Q2:", "Q3:" (the checklist
  markers). Goal: ≥6 of ~8 include the checklist header.
- If both goals hit AND retry PASS rate is still ≤10%: retire retry
  mechanism in B6 (evidence exhausted).
- If retry PASS rate rises to ≥25%: composition helpers are validated;
  add more (envelope helper, curl-terminal helper).
- If retrieval rises but PASS doesn't: the helpers are wrong, not
  the retrieval. Rewrite them or add worked composition examples.

**Not changed (deliberately)**:
- Success Bank storage unit — still `<name>.py` files with
  `def draw_<name>(t, ox=0, oy=0, scale=1.0)`. Callable Python
  constraint preserved.
- Principle file split (three files) — split still working; nothing
  new to consolidate.
- Retry mechanism — kept for one more batch to test the checklist.
- form_catalog.md structure — extended, not restructured.

**Meta-observation on the emergence record**: G3 has now taken THREE
substantive v7 evolutions (B2→B3 adaptive helpers + form_catalog;
B3→B4 composition helpers + worked examples; B4→B5 retry-time
checklist + char↔radical cross-transfer). Each addressed a
diagnostically distinct failure mode. Main pass rate has stabilised at
54-58%, and the gap against G1 has narrowed from -6 (B1) to -3 (B4).
Whether B5's retry-focused evolution can close the remainder will be
the clearest signal to date about whether the callable-Python-bank
format can reach parity with the no-memory control.

---

## 2026-07-24 @ position 300 — B5 curator: HONEST RECKONING — helper hypothesis falsified, retry mechanism killed

**Files changed** (this is a retraction, not another additive pass):

1. **Retry mechanism KILLED for G3.** No further retries will be issued
   by G3's curator scans starting position 301. Rationale below. The
   RETRY-TIME CHECKLIST section stays in `memory_index.md` as a
   historical artifact and as a research-signal generator IF the
   protocol ever restores retries; but no code path in the G3 curator
   loop will produce retry candidates going forward. `errata.md`
   TERMINAL FREEZE section documents the three permanent freezes
   (人, 入, 大) and the meta-diagnosis.

2. **New principle added to `principles_meta.md` (P-HELPER-SKEPTIC)**:
   "When your recommended helper (kiss_apex / pie_point /
   mirror_dian_pair) contradicts what you SEE in the GT, PREFER GT.
   The only B5 retry PASS (丷) came from rejecting mirror_dian_pair
   because the GT was asymmetric. Helpers are recommendations, not
   commands."  (Head curator will apply this edit; sub-agent was
   instructed not to touch principle files.)

3. **memory_index.md top-banner added** noting the B5 finding — retries
   were retrieved AND used the helpers, but only the helper-REJECTING
   attempt PASSed.

4. **form_catalog.md**: not restructured this batch. B6 curator may
   prune (see "options not taken" below).

5. **20 B5 PASS entries added to `success_bank/code/`** (INDEX rows
   141–160 + 161 for the retry graduate 丷 → ba_dot.py). Naming per
   B5 policy: `_char` suffix on collisions, disambiguation for
   同名-radical-vs-char cases.

6. **Standard bookkeeping**: 67 satisfaction lines, 17 retry log
   lines, extensive errata additions (top-of-file TERMINAL FREEZE
   block + 31 new main-FAIL diagnoses + 13 retry-FAIL updates +
   1 new GRADUATED block for 丷).

**Rationale (B5 evidence — the honest read)**:

B5 results:
- Main **19/50 = 38%** — WORST batch of any batch in any group so far
  (down from B4's 54%, and worse than B2's 34% collapse).
- Retries **1/17 = 6%** — the ONE PASS is 丷, which PASSed by
  explicitly rejecting the recommended `mirror_dian_pair` helper.
- Cumulative through 300 items: **49.6%**. Below 50% for the first
  time. G1 no-memory is at ~53% cumulative. Gap: **-3.8pp**, wider
  than at any prior batch.

Retrieval measurement (the B4→B5 lever):
- **17/17 retries** wrote the Q1/Q2/Q3 checklist header.
- **17/17 retries** imported at least one helper from
  `_shared_helpers.py`. Mean helper-import call count: 6.5.
- Compare B4: 0/8 retries used any helper. B3: 7/13 used variant_*
  but 0/13 used composition helpers. B5's compliance is COMPLETE.
- **The B4→B5 retrieval fix worked. And it did not save the pass rate.**

Terminal freezes:
- **人, 入, 大** — the X-crossing family that motivated `kiss_apex`.
  All three reached retry_n=5 and failed. In B5's retry_4 attempts,
  all three used kiss_apex with the correct u_pie parameter, matched
  the checklist to the letter, and still failed panel judgment.
- Per shared_rules terminal-freeze rule: permanently unsolvable,
  moved out of active retry pool.

**The falsification**:

Three v7 evolutions assumed successive missing ingredients:
- v7 pass 1 (B3): "wrong form" — solved by variant_pie/na/dian +
  form_catalog. Main pass rate 34%→58%. ✓
- v7 pass 2 (B4): "wrong composition" — solved by kiss_apex /
  pie_point / mirror_dian_pair. Main pass rate 58%→54%. Flat. ~
- v7 pass 3 (B5): "wrong retrieval" — solved by RETRY-TIME CHECKLIST.
  Main pass rate 54%→38%. Retry rate 12%→6%. ✗

B5 is the clean falsification of v7 pass 2. The helpers were
retrieved, imported, and called with the parameters the errata and
form_catalog explicitly recommended. They did not produce PASSes.
The one PASS came from IGNORING the recommended helper.

**Why the main rate dropped from 54% to 38%**:

Position 251–300 is the harder end of Phase-3 — 亻-radical characters
(仂 仄 仇 仑 仓 with varying right components), the X-crossing family
(义 天 太), envelope shapes (内 內 冗 冘 円), and residual compact
radicals in char form (马 巛 幺 乡 为 乌 予 长). Only ~30% of items in
this range have a Phase-2 radical alias available (compare 60% in
the 034–083 range that drove B3/B4 pass rates). The identity-alias
recipe was G3's strongest lever; it runs out here.

Under those conditions, the composition helpers and the RETRY-TIME
CHECKLIST were expected to compensate. They did not.

**Diagnostic decomposition of the -3.8pp gap**:

- Content (memory missing contexts): still partial. form_catalog is
  now ~55 rows. Adding 亻-radical right-component rows would help
  MAIN attempts on the 亻-family. But the format ceiling below binds
  the composition family regardless.
- Retrieval (drawers don't cite memory): **SOLVED**. B5 checklist
  compliance was 17/17. The one channel that was broken is now fixed.
- **Format (callable-Python as storage unit): NOW the binding
  constraint**. The X-crossing family (人, 入, 大, 义, 从, 天, 太-crotch,
  火, 见 kou-body, 长-捺, 冘, etc.) requires a "kiss" — visual flow of
  ink from one stroke into another — that TWO variant_pie / variant_na
  calls with shared head coords cannot produce. The helper guarantees
  a shared pixel; the calligraphic form requires shared flow. Pixel
  != flow in this format.

This is a real research finding, not a curator excuse:
**code-based memory (G3 callable-Python format) has a structural
ceiling for context-varying calligraphic composition. The ceiling
sits at ~50%. The no-memory control (G1) sits at ~53%. Memory in
this format is a slight liability, not a slight help.**

**Options considered — and the honest calls**:

- **Option A: Kill the retry mechanism entirely.** CHOSEN.
  Evidence: B3 0/13, B4 1/8, B5 1/17. Cumulative retry rate under v7:
  2/38 = 5.2%. The one graduation (子, B4) passed by inline-fresh
  hand-tuning with no helpers; the one graduation (丷, B5) passed by
  explicit helper REJECTION. Neither validates the retry mechanism as
  a memory-consumption channel. And each retry consumes drawer token
  budget that produces nothing. Killing frees curator scan budget for
  main-curriculum diagnosis (already the higher-yield channel).
  Cost: loses a research signal ("can memory improve on failure?").
  Mitigation: the signal was measured across 3 v7 batches and the
  answer is clearly NO in this format.

- **Option B: Radical bank reorganization (worked-verbatim vs helper).**
  DEFERRED. Would confront the ceiling; won't move it. B6 curator may
  revisit if a specific reorganization is proposed.

- **Option C: Aggressive form_catalog pruning.** DEFERRED. form_catalog
  is at ~55 rows; navigation cost is moderate, and drawers DO cite
  rows that aren't top-of-file. Prune only if it grows past ~80 rows.

- **Option D: Reverse the retrieval direction ("draw from GT then check
  against memory").** REJECTED. Requires drawer-prompt changes beyond
  curator scope (protocol change). The head-curator note here is that
  even in the current "look up then draw" flow, drawers who explicitly
  IGNORE the recommended helper (丷 retry_4) PASS more often than
  those who follow it. The reversal may already be happening organically
  and it saved the one PASS. Explicit protocol change deferred to B6
  curator with a proposal.

- **Option E: Reduce/freeze memory further.** PARTIAL: adopted by killing
  retries and adding the P-HELPER-SKEPTIC principle (i.e., licensing
  drawers to ignore helpers). The bank itself is not pruned yet;
  identity-alias remains the strongest single lever and pruning would
  reduce alias coverage.

- **Option F: Explicit paper finding.** CHOSEN as complement to (A).
  The evolution log now names the ceiling. The B6 batch will run under
  a no-retry regime and its main rate will confirm or refute the
  ceiling read. If B6 main rate stays 38–54%, the ceiling is real.

**Honest prediction for B6**:
- Main rate: 45–55% (identity-alias floor + main-only helper usage).
- Retry rate: N/A (mechanism killed).
- Cumulative through 350: 48–51%.
- Gap vs G1: -2pp to -5pp. The gap will not close in this format.

**Not changed (deliberately)**:
- Success Bank storage unit — still `<name>.py` callable functions.
  Format constraint preserved to keep the group comparison valid.
- Principle files (three-file split) — split remains useful.
- form_catalog / helpers — kept as-is. Even helpers that failed retries
  contribute to main attempts.
- INDEX at 160 entries. Continues to grow additively.

**Meta-observation on the emergence record**:

Four batches of v7 self-evolution. G3 went from 49% cumulative (pre-v7)
to 49.6% (post-B5). The bank grew from ~50 primitives to 160. The
principles grew from 1 file to 3 + form_catalog + evolution log +
memory_index. The composition helpers were added. The retrieval fix
was added. **The pass rate did not move.**

This is itself a finding. Emergent memory in the callable-Python format
converges on a rich structure that does not translate into calligraphic
competence beyond the identity-alias baseline. The evolution log
converges honestly: each pass diagnosed a specific gap, and each pass
added the specific machinery to close it, and the pass rate did not
move because the underlying constraint is structural.

The B5 curator's job is now to STOP evolving forward and to name the
ceiling. The paper writes: G3 (code-bank) reached parity with G1
(no-memory) minus 3–4pp across 300 items under 4 rounds of curator-led
self-evolution. Callable-Python is expressive enough for identity
aliases and per-stroke form variation; it is not expressive enough for
the calligraphic "kiss" and related joint semantics that dominate
Phase-3 characters.

---

## Cumulative summary (through position 300, 5 batches under v7)

| Batch | Main PASS % | Retry PASS % | G3 - G1 | v7 evolution |
|-------|-------------|--------------|---------|--------------|
| B1 (pre-v7) | 54% | (retry_1 only 厂 GRAD) | -6 | none |
| B2 | 34% | 0/8 | -4 | (v7 unlock — no changes yet) |
| B3 | 58% | 0/13 | -2 | 1st pass: adaptive helpers + form_catalog + principle split |
| B4 | 54% | 1/8 (12%, 子 GRAD) | -3 | 2nd pass: kiss_apex/pie_point/mirror_dian_pair + worked examples |
| B5 | **38%** | **1/17 (6%, 丷 GRAD via helper-rejection)** | **-3.8** (cumulative) | 3rd pass: retry-time checklist — RETRIEVAL FIXED, PASS RATE FELL |
| B6 (planned) | ~45-55% | N/A (retries KILLED) | ~-3 (predicted) | 4th pass: retire retry mechanism; add P-HELPER-SKEPTIC |

The v7 arc: 3 additive passes narrowed the gap from -6 to -3, then a
4th pass targeting the residual retry channel widened it to -3.8. The
4th pass is the tell — the mechanism does not converge to parity in
this format. B5 curator names the ceiling and stops adding.

---

## 2026-07-26 @ position 350 — B6 curator: v8 first-pass (drawer_memory.md populated, retry RE-ENABLED)

**Files changed** (targeted; v8 unlock consumed rather than restructured
wholesale — B5 curator already named the ceiling and stopped adding):

1. **`drawer_memory.md` populated** (previously seed-empty). Contents:
   - Division of labor between the six memory files (bank, helpers,
     form_catalog, principles ×2, errata, and this new file).
   - Composition playbooks for the biggest B6 failure cluster
     (亻 + right-component, box-based chars, top-cap chars, envelope
     + interior).
   - L-R composition scale table (4 rows, extracted from B6 PASSes:
     们, 对, 打, 付, 外) with ox/scale per side.
   - "Trust GT over helpers" posture codified from B5's 丷 lesson.
   - Sibling-pair observations for 化/花, 仔/孑, 甲/申/由/田, 仕/仝/仞.
   - What curator will NOT write here (no item-mastery, no hard rules).

2. **`memory_index.md` updated**:
   - v8 UPDATE header rewritten with concrete v8 read order (6 steps)
     placing `drawer_memory.md` at step 3 (before form_catalog).
   - v8 signature-freedom paragraph added: bank primitives use
     `(t, ox, oy, scale)` because that's how they were written;
     drawer's `generated.py` is not bound to that signature.
   - Change-history section updated with position 350 entry.

3. **`success_bank/INDEX.md`**: 23 B6 PASS rows appended (entries
   162–184). B6 naming-policy paragraph added at end. No structural
   restructuring — additive only.

4. **`errata.md`**: 27 B6 FAIL diagnoses appended. New cross-fail
   pattern section identifying the 亻-right-component cluster as a
   CONTENT gap (not FORMAT ceiling) — the new lever v8's free-form
   file provides for exactly this class.

5. **`curator_satisfaction_log.jsonl`**: 50 B6_main lines appended.

6. **Retry mechanism RE-ENABLED for B7 scan.** B5 curator killed it
   because helpers hit a "format ceiling" for X-crossing composition.
   v8's format unlock (signature freedom + free-form drawer_memory.md)
   invalidates that specific ceiling argument. Given that INTERVENTIONS
   also lifted the terminal freezes on 人/入/大 for one more shot each,
   it is inconsistent to leave the retry mechanism dead. Retries in B7
   will target: (a) prereqs for 351–400 (also-affected: 也, 士, 丈, 刃,
   子-in-仔 all in the errata under B6); (b) items whose fail mode looks
   addressable under v8's format-unlock (平, 主, 疒, 卩-family, and the
   B5 UN-FROZEN 人/入/大). Cooldown-50 still respected.

**Rationale (B6 evidence + v8 unlock — the honest read)**:

B6 results (first batch under no-retry regime AND under v8 format
unlock that landed between B5 curator and B6 dispatch):
- Main **23/50 = 46%**. Recovery from B5's 38%, matching B5 curator's
  honest prediction (45-55%).
- Retries: N/A (killed at B5).
- Cumulative through 350 items: ~49%. G1 no-memory: ~53%. Gap ~-4pp,
  same as B5.

The gap did not close. But: the drawers in B6 did not yet benefit from
v8's free-form file — `drawer_memory.md` was seeded EMPTY at position
350 and populated for the first time NOW, after B6 was already judged.
So B6 numbers primarily measure the "no-retry regime" (which per B5
curator was expected to be flat), not the v8 unlock effect.

**The v8 unlock's first real test is B7** (positions 351–400):
- Drawers will see the populated `drawer_memory.md` with composition
  playbooks and the L-R scale table.
- Drawers will see retry candidates back in the mix (mechanism
  re-enabled per §6 above).
- If B7 main rate stays 45-50% AND retry rate stays ~5% or below, the
  v8 unlock was ineffective and the ceiling holds even with free-form
  prose. This confirms B5 curator's structural-ceiling reading.
- If B7 main rate rises to 55%+ OR retry rate rises to 15%+, prose
  guidance beyond callable code provides real lift. Would suggest G2
  (pure prose) was the missing lever, not composition helpers.

**Diagnostic decomposition of the B6 fail cluster**:

Of 27 fails, **6 are 亻 + right-component** (化, 他, 仔, 仕, 仗, 仞):
`ren_pang` on the left composes cleanly; the right component is either
a compound with no bank primitive (匕, 也, 士, 丈, 刃) or a bank
primitive at wrong scale/position (子 in 仔 could have used zi_char).
This is a **content gap**, not a format ceiling. Prose recipes for
these five right-components are now in `drawer_memory.md` §"亻 +
right-component". If B7's 亻-family pass rate rises, prose fixed
content; if it doesn't, the content was already inferrable and
retrieval / attention is the gap.

**Other clusters**:
- 5 box-based (甴, 生, 平, 主, 正) — proportion/interior-heng
  drift; recipe explicitly linked to 申 / 甲 templates in playbook.
- 5 cursive-hook (书, 引, 必, 发, 乎) — format ceiling stays
  (B5 diagnosis carries).
- 5 multi-component (水, 刅, 队, 升, 出) — mixed (刅 is a scale error,
  water-family is format-ceiling).
- 5 rare (丱, 乍, 去, 疋, 疒) — mixed.
- 1 envelope+又 (反) + 1 more (发 counted above).

**Options considered — and calls**:

- **Option A**: populate `drawer_memory.md` with composition playbooks
  extracted from B6 evidence. CHOSEN. Free-form is the point of v8;
  the L-R scale table and 亻-right-component playbook are exactly
  the natural-language content that doesn't code as one callable.
- **Option B**: RE-ENABLE the retry mechanism for B7. CHOSEN. B5's
  format-ceiling argument doesn't survive v8's format unlock; the
  terminal-freeze lifts are already an implicit re-enable of the retry
  channel for 人/入/大. Consistency argument.
- **Option C**: reorganize the code bank into subdirectories (strokes/
  radicals/chars). DEFERRED. Would break existing imports; low
  expected gain vs. prose playbook.
- **Option D**: prune form_catalog. DEFERRED. Rows are additive-only
  and drawers do cite them in main attempts. Prune only if it grows
  past ~80 rows (currently ~55).
- **Option E**: create new principles from B6 patterns (e.g. P13 "dots
  above heng not descending" from 平's fail). NOT DONE yet — one B6
  fail is not enough evidence for a P-rule; will re-evaluate at B7 if
  the same pattern recurs.
- **Option F**: retire the RETRY-TIME CHECKLIST since B5 falsified its
  yield. NOT DONE — even though the checklist didn't raise pass rate,
  it's the only observable retrieval signal we have. Kept for B7 as
  research instrumentation.

**Expected help for B7 (positions 351–400)**:
- 亻-family Phase-3 chars: playbook + zi_char reuse should raise pass
  rate on 5-stroke 亻+X compounds.
- Retries on B6 items: 化 (匕 recipe from playbook), 他 (also inline),
  仔 (zi_char at ox=+40), 仕 (士 inline recipe), 平/主 (dots-above
  guidance), 疒 (call guang explicitly).
- Terminal-unfrozen 人, 入, 大: one more shot under v8 signature
  freedom. Drawer can now write inline fresh with any signature; not
  bound to `(ox, oy, scale)` on kiss_apex.

**Measurement plan for B7**:
- Grep B7 attempts for `drawer_memory.md` citations in comments +
  ren_pang/men_char-style L-R patterns. Goal: at least 5 of 50 attempts
  visibly cite drawer_memory.
- 亻-family Phase-3 pass rate: goal ≥ 4 of ~8 (was 1/6 in B6).
- Retry rate: goal ≥ 15% (was 5% cumulative across v7).
- If main rate rises to 55%+ or gap narrows to <-2pp: v8 unlock
  worked, add more playbooks.
- If flat: v8 unlock ineffective in this format; publish the finding
  and stop adding.

**Not changed (deliberately)**:
- Success Bank storage unit — still `.py` callable functions. The
  callable-Python constraint is G3's identity; the SIGNATURE freedom
  (v8) is orthogonal.
- Principle files (three-file split) — split still working.
- form_catalog / helpers — additive-only.

**Meta-observation on the emergence record (5 batches under v7 + 1 under v8)**:

The evolution log has now recorded FIVE substantive curator responses:
B2→B3 (adaptive helpers), B3→B4 (composition helpers), B4→B5 (retry
checklist), B5→B6 (retry killed + honest ceiling naming), B6→B7 (v8
unlock consumed: prose playbooks + retry re-enabled). The pass-rate
trajectory across these: 54, 34, 58, 54, 38, 46. Mean ~48% under v7;
one datapoint under v8 (46%, essentially = v7 mean). The next batch
(B7) is the first that both DRAWS on populated drawer_memory.md AND
runs retries. It is the cleanest test of whether v8's format unlock
converts to accuracy.

If B7 stays ~48%, the paper writes: **G3's callable-Python bank + G2-
style prose overlay reaches parity with the no-memory control minus
3-5 pp across 400 items under 5 rounds of curator-led self-evolution
including two format-freedom unlocks. The memory format expressiveness
is not the binding constraint.**

If B7 lifts to 55%+, the paper writes: **G3 finally overtakes G1 in
the sixth batch after 5 rounds of self-evolution culminating in a
prose overlay. The lever was natural-language composition recipes
alongside callable code — neither alone was sufficient.**

Either outcome is a clean paper finding.
