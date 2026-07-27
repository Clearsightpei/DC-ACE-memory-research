# Human Interventions Log

Every human change that alters memory structure, retrieval rules, bank
constraints, or the experimental protocol from v8 forward is recorded
here. Purpose: cleanly separate what came from AI self-evolution vs.
what came from human unlock, for the paper's analysis.

Each entry:
- **Position** — curriculum position when the intervention took effect.
- **Boundary snapshot** — the snapshot ID that captures the pre-
  intervention state (post-intervention state is captured by the next
  scheduled snapshot).
- **What changed** — concrete file diffs.
- **Rationale** — why the human decided to intervene (be honest — the
  paper's story needs to know when self-evolution alone was
  insufficient).
- **What was deliberately NOT changed** — human observations the AI
  was *not* told about, so the AI's self-diagnostic capability can
  still be tested downstream.
- **Expected impact** — what should shift and how to measure it.
- **Post-hoc note** (added later) — what actually happened.

Format: newest at top.

---

## v8 — 2026-07-25 @ position 350 — Format ceilings unlocked

**Boundary snapshot**: `snapshots/G*/snapshot_0350/` (pre-v8 state).

**What triggered**: B6 exposed two distinct structural failure modes
(see README v8 changelog for full trajectory + numbers):
- G3 hit a **format ceiling**: bank primitives all followed the
  initial-example signature `(t, ox=0, oy=0, scale=1.0)`, and the
  convention had ossified across ~150 promoted files. Curators added
  richer helpers (`variant_pie`, `kiss_apex`, `pie_point`,
  `mirror_dian_pair`) but drawers never adopted them on retries (0
  usage across B3+B4+B5 retry attempts). B5 curator diagnosed
  correctly and killed the retry mechanism.
- G4 hit a **capacity ceiling**: evolved memory (form_catalog ~600
  lines + joint_atlas + principles_meta + chronic/ + auto-injected
  MMH spec + MANDATORY LOOKUP CHECKLIST + 140+ bank files) grew large
  enough that 6/16 G4 retries in B6 literally stalled — drawer
  subagents never wrote a PNG. Not memory content; retrieval
  overhead.

**Human diagnosis after 6 batches of observation**: G3's format
constraint was **unintentionally over-restrictive** in the original
design. The initial `rules.md` used `(ox, oy, scale)` as an *example*
but curators treated it as gospel. The intent was always that Success
Bank signatures could carry arbitrary knobs and the Principle Bank
would evolve to describe *how* to adjust strokes across contexts.
That's not what happened. Unlocking the format is fixing an original
design flaw, not adding a research crutch.

**What changed**:

1. **G3 unlock** (`protocol/G3_coords/rules.md`):
   - Core constraint rewritten: *storage unit is a callable Python
     function*, but signature is drawer's choice. `(ox, oy, scale)`
     is a starting example, not a limit. Encode whatever knobs the
     composition needs (angle, curve, taper, aspect, orientation,
     ...).
   - Bank and principles explicitly reframed as **reference only**.
     Nothing strictly required. Drawer may adjust any stroke at any
     time without consulting the bank.
2. **G4 unlock** (`protocol/G4_grid/rules.md`):
   - Same "reference only" reframe. 米字格 anchors + P/T/N/S joint
     spec remain the *convention* for bank entries, not a mandate on
     every drawing.
3. **G3/G4 free-form access grant**:
   - Both gain `drawer_memory.md` — same shape as G2's. Curator may
     write anything, anywhere.
   - Architecture is now: **G2 = free-form only. G3 = free-form +
     code bank. G4 = free-form + grid bank.** G3/G4 strictly
     dominate G2 in access.
4. **G4 prune/canonical permission** (`protocol/G4_grid/rules.md`):
   - Curator may prune uncited memory entries and promote any
     retry_n≥2 fail to a canonical hand-written primitive (extending
     the existing chronic-cluster mechanism).
5. **Terminal freezes lifted**:
   - G3's 人/入/大 (frozen at retry_n=5 in B5) get one more attempt
     under the unlocked convention. Their retry_n is reset to 4 so
     one more shot is available before re-freeze.
6. **`tools/dispatcher.py` memory-index text**: adjusted to note
   both memory_index.md and drawer_memory.md exist for G3/G4.

**What was deliberately NOT changed** (research-integrity notes):

- **No position/orientation/silhouette gate added to
  shared_rules.md**. The human observed 刀→力 sibling-position
  failures across all 4 groups (curator diagnostic evidence for
  weeks). The human did NOT tell any curator about it. Whether AI
  curators discover this failure mode from vision alone under the
  v8 unlock is a direct test of self-diagnostic capability. If they
  discover it: emergent self-improvement covers relative-position
  reasoning. If they don't: emergent self-improvement has a specific
  documented limit.
- **No hint to curators about which specific memory content is
  wrong**. Prune permission is granted; the *decision* to prune, and
  *what* to prune, must be the curator's.
- **No hint to G3 that its "kill retries" decision might have been
  premature** now that the format ceiling is lifted. Curator may
  re-evaluate on its own.

**Expected impact** (three testable outcomes for each of G3, G4):

| Post-v8 outcome | Interpretation |
|-----------------|----------------|
| G3/G4 > G2 | Structured bank + free-form together beats free-form alone; grid vocabulary / callable code adds real value beyond markdown |
| G3/G4 ≈ G2 | Structured bank is redundant with free-form's expressiveness |
| G3/G4 < G2 | Structured bank is a distraction even when optional (retrieval overhead > format benefit) |

**Measurement plan**:
- Compare G3/G4 batches B7+ against B0-B6 same-group cumulative.
- Compare G3/G4 vs G2 post-v8 (which was previously handicapped by
  having only free-form and no structured backup).
- Grep curator satisfaction logs and evolution.md entries B7+ for
  spontaneous discovery of position/orientation failure mode.
- Track G4 memory-size trajectory — does the curator actually prune
  when given permission, or continue accretion?

**Post-hoc note** (2026-07-27, after B7 judgment @ position 400):

- **B7 main pass rates**: G1 30% · G2 42% · G3 32% · G4 50%. G4 hit
  its highest main-pass score to date (up from 43% at B6).
  G3 stayed flat vs B6 (46%→32%, within noise band).
- **B7 retry pass rate: 0/22** (G3 10/10 fail; G4 12/12 fail).
  All retries under v8 unlock (signature freedom + free-form file +
  terminal-freeze lifts on 人/入/大) failed. Zero recovery.
- **Retry-file inspection**: reflection *did* run. Every retry
  generated.py opens with a detailed diagnostic block (errata
  reference + GT observation + revised hypothesis). Examples: 人
  retry_5 correctly diagnosed why prior kiss_apex attempts failed;
  主 retry_1 correctly identified spacing issues from prior fail.
  But (a) the diagnoses focus on the axis errata named (spacing,
  crossing coordinates), often *not* the axis the human judge fails
  on (calligraphic line-weight variation, stroke connectedness);
  (b) there is no post-render visual-recheck loop — drawers write
  the "fixed" script, render, submit. G4 retries have a hardcoded
  `SELF_CHECK = {'overall_pass': True}` template dict, i.e. no
  actual reflection artifact.
- **Human intervention this turn: NONE**. User explicitly declined
  to strengthen the retry prompt with a mandatory "render → view own
  PNG → compare to GT → name one visual gap → revise-or-submit"
  block. Reasoning preserved verbatim from the AskUserQuestion
  answer: "Accept 0/22 as-is; move to B7 curators + B8" — "Log this
  as the research finding: retry channel dead at position 400,
  self-diagnostic reflection has a documented ceiling under this
  exact prompt regime. Let B7 curators react on their own (they may
  retire retries themselves like G2/G3 did before)." This preserves
  the experiment's premise: AI's spontaneous discovery of the
  retry-channel dead-end is itself the finding, not the fix.
- **What to watch for at B7 curator run**: does G3's curator now
  retire the retry mechanism (matching G2's B6 decision and G3's own
  B5 decision — which was overturned only under v8 unlock)? Does G4
  do so? If any group retires retries, that IS the emergent
  self-diagnostic conclusion. If they keep re-attempting with new
  hopes, that's also a data point.
- **Format-ceiling vs capacity-ceiling verdict**: v8 unlocks did
  NOT rescue the retry channel on their own. G4's chronic-primitive
  import rate is still to be measured this turn from B7 mains
  (curator instrumentation). Main-channel improvement for G4 (43→50%)
  is encouraging and suggests the prune+drawer_memory work paid off
  on FIRST attempts even without helping RETRY attempts.

---
