# G3 memory index — entry point for the drawer

## v8 UPDATE (2026-07-25 @ position 350 — populated by B6 curator @ 2026-07-26)

A free-form file **`drawer_memory.md`** now exists alongside the code
bank (same shape as G2's `drawer_memory.md`). Under v8 the code bank +
principles are **REFERENCE ONLY** — no strict requirement to call or
comply. If GT contradicts a bank primitive or a helper's abstraction,
**trust GT** (B5 丷-graduation lesson).

### Read order under v8 (B6 curator recommendation)

Do all of these BEFORE writing any code. Skip any that clearly don't
apply.

1. **Look at the GT PNG.** Decompose into strokes. Note position/role
   of each. Ask "how would G1 draw this fresh?"
2. **Check `errata.md`** for this item or close cousins (e.g. its
   radical, its sibling in the char↔radical table).
3. **Read `drawer_memory.md`** — free-form composition playbooks,
   L-R scale tables, sibling-pair notes, "trust GT" posture.
4. **Consult `form_catalog.md`** for stroke×context numbers if a
   specific stroke is uncertain.
5. **Scan `success_bank/INDEX.md`** for an identity alias or a
   close-enough starting scaffold. **You are NOT required to use one.**
   Under v8, if no bank entry fits without extreme transformation,
   inline fresh.
6. **`principles_stroke_family.md`** (P1-P12) and **`principles_meta.md`**
   (TR1-TR7) LAST, only if a specific question remains. REFERENCE.

### v8 signature freedom

Bank primitives have `(t, ox=0, oy=0, scale=1.0)` because that's how
they were written. **You are not bound to that signature when writing
your `generated.py`.** If your composition needs an angle, a curve, a
taper, or an aspect knob — put it in your function or hand-render
inline. The unit constraint (callable Python) is still G3's identity;
the parameter vocabulary is your choice.

> **B5 update (2026-07-24)**: helper hypothesis FALSIFIED. Retrieval was
> fixed (17/17 retries used checklist + helpers) but only 1 retry PASSed
> (丷, by REJECTING the recommended helper). If your recommended helper
> conflicts with what you SEE in the GT, prefer GT. See evolution.md
> 2026-07-24 for the honest reckoning.

*Maintained by the curator. Drawer reads this file first every cycle,
then follows the pointers below. Reorganised 2026-07-18 (v7 evolution,
position 150) — read order changed: form-catalog and adaptive helpers
come FIRST; frozen bank primitives second; meta-rules last.
Reorganised again 2026-07-22 (v7 second-pass, position 200) — worked
composition examples added to form_catalog; joint/weld helpers added
to `_shared_helpers.py`.
Reorganised again 2026-07-23 (v7 THIRD-pass, position 250) —
RETRY-TIME CHECKLIST added (retries were bypassing memory entirely
in B2/B3/B4); char↔radical cross-transfer table added (multiple B4
chars PASSed while their radicals stayed in errata).
B5 (2026-07-24) falsified the helper-composition hypothesis: retrieval
was fixed but only 1/17 retries PASSed. The RETRY-TIME CHECKLIST is
kept as a research signal but its promotion power is proven limited —
the head curator's evolution.md 2026-07-24 entry decides B6 direction.*

## RETRY-TIME CHECKLIST (READ FIRST if this is a retry attempt)

**Evidence from B2, B3, B4**: on retry attempts, drawers imported the
composition helpers 0/8, 7/13, 0/8 times respectively — and even in
B3's 7/13 the helpers didn't rescue the composition. Main attempts
DO use helpers (24% import rate). The retry channel is where memory
retrieval is broken.

**If your prompt indicates this is a retry** (item_id ends in
`__retry_N`), before writing ANY code write a header comment in
`generated.py` answering these three questions:

```python
# RETRY MEMORY CHECKLIST (B4→B5 v7 evolution)
# Q1 (errata): Look up this item in errata.md. What is the fix idea?
#   <ANSWER>
# Q2 (form_catalog): Search form_catalog.md for rows matching the
#   stroke(s) that caused the fail. Which rows are relevant?
#   <ANSWER>
# Q3 (helpers): Does the fail category match any of these helpers?
#   - X-crossing / apex-kiss / cross-shaft weld → `kiss_apex`, `pie_point`
#   - Mirror-dot pair (忄, 丷, 火, 犬 side dot) → `mirror_dian_pair`
#   - Per-stroke form (angle/taper/bow) → `variant_pie/na/dian`
#   - Uniform thin lines (MMH GT) → thin widths per P12, NOT calligraphic
#   <ANSWER — name the helper you'll import, or explain why none apply>
```

Only after writing these three ANSWERS may you proceed to code.
Curator will grep for `# Q1` `# Q2` `# Q3` in every retry attempt to
verify compliance. This is not a bureaucratic hurdle — it is the
only observable signal that memory was consulted at all.

## Char ↔ Radical cross-transfer (B4 addition)

When a Phase-3 char PASSes but the corresponding Phase-2 radical is
in errata, the char's recipe is a valid retry candidate for the
radical. Do NOT block a Phase-3 char attempt on a radical FAIL.

| Item | Char status | Radical status | Recipe transfer |
|------|-------------|----------------|-----------------|
| 兀 | PASS (wu_char.py) — heng 0.85 + er_ren 0.95, moderate widths | FAIL retry_2 — calligraphic 10px legs vs GT's thin ~4px | Back-port wu_char widths to radical retry |
| 门 | PASS (men_char.py) — inline dian + 竖 + 横折钩 for tall aspect | FAIL retry_2 — different inline recipe | Back-port men_char inline recipe |
| 子 | PASS (zi_char.py) + GRAD retry_1 | GRADUATED — same recipe works both | Aligned |
| 尢 | FAIL | FAIL retry_2 — same fail as 兀 family | Await wu recipe transfer |
| 夂 / 夊 | FAIL char + FAIL radical | Both same fail mode (apex-kiss composition) | Neither has PASSing template — both need kiss_apex |

## Core format constraint (fixed — do not violate)

## Core format constraint (fixed — do not violate)

G3's memory unit is **callable Python functions**. The Success Bank
contains `.py` files defining functions of the form:
```python
def draw_<item>(t, ox=0, oy=0, scale=1.0):
    ...  # calls to sub-primitives OR inline PIL rendering
```
You may design new function signatures (adaptive width, taper args,
etc.), but you may not abandon the callable-function unit. See
`../protocol/G3_coords/rules.md` for the full constraint.

## Read order when drawing (v7)

**1. Look at target GT first.** Decompose into strokes. Note
position/role of each stroke (top / left / crossing / envelope / etc.).

**2. For each stroke, consult `form_catalog.md`** (NEW file).
Indexed by stroke × context (e.g. "撇 in 大-family crossing arm",
"点 in 灬 leftmost 左点"). Gives concrete head / tail / bow_perp /
w_head / w_tail numbers from prior PASSes. This is the primary
retrieval aid.

**3. Choose a rendering approach in this priority order**:
   - **If the target is a Phase-3 character AND a Phase-2 radical with
     the same shape exists in the bank** → try IDENTITY alias first
     (see form_catalog's "Character-vs-radical scaling" table). Many
     B3 PASSes were 1-line aliases.
   - If two strokes MUST share a pixel (X-crossing, weld, kiss) →
     use `kiss_apex` / `pie_point` from `_shared_helpers.py` to
     compute the exact shared pixel BEFORE calling the variants.
     See form_catalog "X-crossing family" worked example.
   - If the target has a mirror-dot pair (忄, 丷, 火, side dots) →
     use `mirror_dian_pair` — do NOT hand-tune each dot separately
     (B3 evidence: hand-tuning breaks the mirror).
   - If `form_catalog.md` has a matching row → use the adaptive
     helper `variant_pie` / `variant_na` / `variant_dian` in
     `_shared_helpers.py` with the catalog numbers. **Copy widths
     and bow_perp; re-derive head/tail positions against YOUR
     character's proportions** (do not copy positions wholesale).
   - Else if `success_bank/INDEX.md` has a mastered item whose SHAPE
     matches after uniform scale → use the bank primitive with
     deliberate `(ox, oy, scale)` per TR1-TR3 in `principles_meta.md`.
   - Else → derive fresh. If the fresh recipe passes judgment,
     the Curator will add its numbers to `form_catalog.md` for reuse.

**4. Check `errata.md`** if you've seen this item before — the fix
idea may already be there.

**5. Consult `principles_stroke_family.md`** for width profiles
(P4), hook conventions (P1), math convention (P5), and P11 (the
form-variant lesson from B2).

**6. Consult `principles_meta.md`** LAST for TR1-TR7 (how to
transform primitives). TR8 and TR9 are RETIRED — do not follow them.

## What memory G3 currently holds

### New in v7 (2026-07-18)
- **`form_catalog.md`** — stroke × context lookup with concrete
  numbers from prior PASSes. THE primary retrieval aid. Grows every
  time a PASS reveals a new form variant. **Second-pass (2026-07-22):
  added worked composition examples for X-crossing / mirror-dot /
  radical-alias families, plus retrieval-discipline notes.**
- **`success_bank/code/_shared_helpers.py`** — adaptive helpers
  (`variant_pie`, `variant_na`, `variant_dian`, `tapered_bezier`,
  `tapered_line`, `to_px`). Callable Python primitives that expose
  angle/taper/width knobs the frozen `(ox, oy, scale)` signature
  hides. **Second-pass (2026-07-22): added joint/weld helpers
  `pie_point`, `kiss_apex`, `mirror_dian_pair` to make composition
  geometry explicit.**
- **`principles_meta.md`** — meta-rules (TR1-TR7).
- **`principles_stroke_family.md`** — stroke-family knowledge (P1-P11).
- **`principle_bank.md`** — stub, split into the three files above.

### Persistent
- **`success_bank/INDEX.md`** — master list of mastered items
  (now **140 entries** after B4's 27 PASSes + 1 retry graduate).
- **`success_bank/code/`** — frozen concrete bank entries. Each is a
  `draw_<item>` function you may call at deliberate `(ox, oy, scale)`.
- **`sandbox.md`** — persistent free-form scratch; per-batch
  diagnostic notes.
- **`errata.md`** — 错题集; failed items with per-item diagnosis and
  fix idea.
- **`scans/`** — per-position errata scan decisions.
- **`retry_log.jsonl`** — append-only retry log.
- **`curator_satisfaction_log.jsonl`** — per-attempt "would-I-stop?"
  verdicts.
- **`evolution.md`** — append-only log of structural changes to
  memory organization (v7).

## When to consult what — quick lookup

- **Drawing a new radical / character**: form_catalog → adaptive
  helper → INDEX (frozen primitive if fit) → derive fresh.
- **Similar item failed before**: errata.md.
- **Uncertain about width / hook direction**: principles_stroke_family
  P1, P4.
- **Uncertain about (ox, oy, scale) derivation**: principles_meta
  TR1-TR7.

## Change history

See `evolution.md` for the append-only log of structural changes.
Latest: **position ~651 (2026-08-05, B13 curator) — 2 PIL-native envelope
variants promoted + P-DEV5 (sibling-slot verification).** New bank
primitives: `ren_pang_pil_for_LR_left.py` (canonical 亻 for LR-left,
PIL px, motivating context 俚; template for ~40 remaining 亻-chars) and
`zou_zhi_thin_pil_envelope.py` (canonical 辶 envelope, PIL px MMH-thin,
motivating context 适; template for ~30 remaining 辶-chars). Both fully
parameterized. Added P-DEV5 codifying that variant "reuse targets" are
speculative until the sibling slot has a bank primitive or documented
recipe (motivating case: B12's `quan_tian_for_LR_left` was promoted
with 畈/畋 as reuse targets; both R1'd on B13 and FAILED because 反/攵
have no bank recipe — the 田 rendered cleanly but the sibling collapsed).
B13 main pass rate 20% (10/50, up from B12's 14% — normal band). Retry
1/8 (盃 recovery). ★ FIRST batch G3 (20%) beat G5 (18%) on PASS —
research signal that crystallized bank envelopes (疒/辶/亻) can
compensate for MMH absence. INDEX now at row 252. Terminal-freeze pool
unchanged (9 items). pass_index.md now 270 rows (269 PASS + 1 A) after
tool rebuild — B13's 10 new mains added; 盃 R1 recovery PNG not picked
up by tool (retry attempt dir naming quirk, non-blocking).
Prior: **position 601 (2026-08-04, B12 curator) — ★★★ FIRST-EVER A
VERDICT ★★★ after 600 items / 12 batches / 4 format unlocks:
`p3_char_0434_畎` broke through as A via L-R-slot compression of the
X-crossing 犬 radical. 2 variants promoted (rows 249-250):
`quan_tian_for_LR_left.py` (compressed 田 for LR-left; templates for
略/畔/畝/畦/畯/畈/畋) and `quan_dog_for_LR_right.py` (犬 with explicit
shared-pixel cross-apex; template for 猷 + P-DEV4 pathway). Composite
wrapper at row 248 (`quan_char.py`). Added **P-DEV4** (X-crossing
compression pathway) to principle_bank.md — the FIRST documented
A-verdict pathway for the format-ceiling family; narrow (does NOT
unfreeze standalone 大/矢/失). B12 main pass rate: 14% (7/50 = 1A + 6
PASS; below G1 control ~20%; diagnosis: item-pool spike + noise +
slower bank growth, monitor B13). Retry 0/3 → **3 TERMINAL_FROZEN**
(疖/亨/声 all R3 last-try). Terminal-freeze pool now: 人/入/大/匕/矢/失/
疖/亨/声. INDEX now at row 250. Language update: from "0 A across 550
items" to "1 A in 600 items (0.17%), via P-DEV4 pathway; full-canvas
X-crossing ceiling unchanged".
Prior: position 550 (2026-08-03, B11 curator) — zero A CONFIRMED
across 11 consecutive batches (0/550 items). v13 channel producing
steady variant flow: 4 new variants promoted (rows 244-247):
`zhu_master_for_LR_right.py` (from 往; template for 住/注/柱/驻),
`you_frame_up.py` (from 油; 由-frame with shu-up, new shape family),
`tu_cun_stacked_for_LR_right.py` (from 侍; template for 待/恃/詩/峙),
`you_have_for_LR_right.py` (from 侑; template for 郁/洧). All original
primitives untouched. Added P-DEV3 (variant-promotion signal) to
principle_bank.md. TERMINAL_FROZEN 矢/失 at R4 C (X-crossing format
ceiling). Main pass rate 14/50 = 28%. Retry 0/5. INDEX now at row 247.
Prior: position 500 (2026-07-31, B10 curator) — v13 BANK_DEVIATION
channel first exercised (16 deviations, 3 promoted as variants:
`bai_char_compressed_for_LR.py`, `bai_char_for_top_stack.py`,
`er_ren_for_bottom_stack.py`; original primitives untouched). Two
retry graduations from B9 leak-fix (时, 串). Zero A verdicts confirmed
across 500 items. Added P-DEV1 (when to deviate) and P-DEV2
(retrieval-leak fix scope) to principle_bank.md. INDEX rows now
213–229 (14 B10 PASSes + 3 variants).
Prior: position 400 (2026-07-27, B7 curator) — v9 visual-diff prompt
proved out on retry channel: 3/10 v9 reruns PASS (大, 主, 疒) vs 0/10
under v8 wording. The three graduations share a `VISUAL DIFF` +
`REJECT baked-in helper` recipe now codified in drawer_memory.md.
INDEX grew by 19 (rows 185–203). Main pass rate 16/50 = 32% — B7 hit
the cursive/complex-char density band; new X-crossing observation
(矢/失/乔/会 all fail same as 大) added to drawer_memory.md.
Prior: position 350 (2026-07-26, B6 curator) — v8 first-pass consumed:
`drawer_memory.md` populated (composition playbooks + L-R scale table
+ trust-GT posture); memory_index.md read order rewritten to place
drawer_memory.md at step 3 (before form_catalog); INDEX grew by 23
B6 PASSes (rows 162–184).
Prior: position 300 (2026-07-24) — v7 fourth-pass (retry mechanism
killed; P-HELPER-SKEPTIC principle added).
Prior: position 250 (2026-07-23) — v7 third-pass consumed:
RETRY-TIME CHECKLIST added to this file (retry channel had 0% helper
adoption in B2/B4, 7/13 in B3 but 0 passes — retrieval is the gap);
char↔radical cross-transfer table added (兀/门/子 pattern showed
chars pass while radicals fail with different recipes); INDEX grew
by 27 B4 PASSes + 1 retry graduation (子, now bank #122).
Prior: position 200 (2026-07-22) — kiss_apex/pie_point/mirror_dian_pair
helpers added to `_shared_helpers.py`; worked composition examples
added to `form_catalog.md`.
Prior: position 150 (2026-07-18) — v7 unlock consumed: form_catalog
created; principle_bank split into 3 files; TR8, TR9 retired; adaptive
helpers added to `_shared_helpers.py`.
