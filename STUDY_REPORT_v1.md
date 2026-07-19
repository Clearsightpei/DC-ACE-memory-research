# DC-ACE Study Report (working draft v1)

**Date**: 2026-06-13
**Project**: AI memory research / "Can an AI learn by itself?"
**Author**: Peilin Wu (kaiwufun@gmail.com)
**Status**: in-progress draft — run_6 still active at cycle 64.

---

## Frame: what this report is and what it isn't

This is the **first pass** at organizing six DC-ACE experimental runs into a shareable research record. It is not yet a paper. The goal here is to (a) put the design choices and outcomes for each run side by side, (b) tie them to the central research question, and (c) make the gaps and limitations visible so the next pass can be sharper.

The central question:

> **Can an AI learn by itself / self-evolve?**

DC-ACE pursues this through a Chinese-character drawing curriculum because handwriting gives a continuous-quality signal (good vs. bad strokes) that lets us watch a memory artifact grow over many cycles. Pixel fidelity is the *measurement* of learning quality, not the *goal*. The goal is the memory.

A loop runs every cycle:

> Teacher → Drawer → Judge → Curator → 4 commits → next cycle.

Across six runs we vary **what the Teacher decides**, **what artifact the Drawer reads from / what its body looks like**, and **what the Judge measures**. The dependent variable is whether the Drawer's output improves and whether the memory accumulates transferable knowledge.

---

## Brainstorm: what else might this report include?

The user asked what to add beyond the three-dimension comparison. I'd recommend these:

1. **A "self-evolution" vs. "human-guided evolution" distinction.** Each run's redesign comes from the user reading the prior run's POSTMORTEM and proposing new architecture — the *cycle-within-a-run* iterates autonomously, but the *between-run* redesigns are human. This needs to be explicit, because the headline answer to "does it self-evolve" depends on which loop we mean.
2. **A timeline + scope table** so readers see at a glance: how many cycles, how many promotions, what changed per run.
3. **Operational definitions of "learning"**: a *bank-growth rate* (entries / cycle), a *promotion rate* (promotions / cycles), a *false-positive rate* (promotions later found defective), and a *transfer rate* (how often a Success Bank entry gets reused in downstream characters).
4. **What stayed constant.** The loop structure, the Chinese-character target, the Python turtle renderer, the role separation — these are constant scaffolding. The report should isolate the **variables** (Teacher / Drawer-memory / Drawer-design / Judge) from the **scaffolding**.
5. **Worked examples** of failure modes — one or two concrete cases like 五 c20 (run_5 false positive) or 力 c33–c55 (run_6 stuck stroke) — to make abstract claims tangible.
6. **Threat-to-validity / limitations section**: single researcher, no control group, panel judges are LLMs (the same LLM family being studied), Drawer subagents inherit the same model. This affects what we can claim.
7. **What's missing as data** — e.g., reuse-rate metric was discussed but never logged; OCR confidence trajectories weren't compared run-over-run; cycle-time / token cost wasn't tracked.
8. **One paragraph of speculation** at the end about what experiment design *would* test self-evolution more cleanly than DC-ACE currently does.

The body below incorporates 1, 2, 3, 4, and 6. Items 5, 7, 8 are scattered into the relevant per-run sections and the closing.

---

## Methodology

### What is being measured
- **Bank entries (count)**: how many primitives/characters the system claims to have mastered. Source: `runs/<r>/success_bank/code/*.py` (run_4+) or `drawer_memory.md` (run_1, run_2).
- **Promotion**: a Curator decision to add an entry to the bank for a given cycle. Detected via commit messages containing "PROMOTE" / "mastered".
- **Carry-over**: Curator decides the cycle did not pass the gate and the same focus repeats next cycle. Detected via "carry" in commit messages.
- **Freeze (run_6 only)**: a cycle that hit the 3-attempt freeze rule and is preserved as failure evidence. Detected via "FROZEN" / "freeze".
- **False positive**: an entry that was promoted but later judged defective (e.g., wrong stroke count). These are flagged in postmortems and remedied via demotion or run-reset.

### What counts as "learning"
Three concentric definitions, each progressively stronger:
1. **Surface learning** — the Drawer's output for a given character improves over its first-attempt baseline. (Easy: cycle 1 → cycle 25 visual scores.)
2. **Memory-mediated learning** — the Drawer reads the bank and uses entries correctly in new characters it has never drawn before. (E.g., 木 in run_4 composes 一 + a known shu; 立 in run_6 reuses dian and heng primitives.)
3. **Architectural self-improvement** — the system *changes its own learning rules* in response to outcomes, without a human redesigning the loop. This is the strong form of "self-evolution".

This report uses all three definitions, separately tagged.

### Data sources
- `runs/<r>/POSTMORTEM.md` — narrative postmortems (where they exist).
- `runs/<r>/success_bank/INDEX.md` and `runs/<r>/success_bank/code/` — the bank.
- `runs/<r>/judge_results/cycle_*.json` — per-cycle gate readings.
- `runs/<r>/teaching_log.md`, `teaching_plan.md` — Teacher decisions.
- `runs/<r>/drawer_memory.md` — run_1 / run_2 only.
- `runs/<r>/cycle_state.json` — running orchestrator state.
- `.claude/skills/{teacher,drawer,curator,cycle}/SKILL.md` — current SKILL versions (run_6 era).
- `git log --oneline -- runs/<r>` — chronological commit record.

---

## Per-run snapshots

### Run 1 — 12 cycles · phase-correlation judge · text-only memory
**Postmortem**: [runs/run_1/POSTMORTEM.md](runs/run_1/POSTMORTEM.md).
**Core problem documented**: reward-signal instability. Phase-correlation visual_score was non-monotonic — strokes that *looked* better sometimes scored *lower*. OCR was over-trusted, producing false positives on malformed glyphs (e.g., 人 with mismatched 撇/捺).

| Dimension | Design |
|---|---|
| **Teacher** | 3 tasks/cycle. Carry-over rule (visual_score < 0.7 → repeat). Mandatory reflection after failure. Phase 1→2 transition at cycle 6, 2→3 at cycle 12. |
| **Drawer memory** | Single `drawer_memory.md` (300 lines), Curator-owned. Markdown status table + numbered lessons + Python recipe snippets per stroke/character. No structured bank. |
| **Drawer design** | Fresh subagent per cycle. Access to `tools/strokes.py` (6 atomic + 8 compound vendored functions). Blind to GT images. |
| **Judge** | OpenCV `phaseCorrelate` → visual_score; RapidOCR → is_correct. No panel. No structural gate. |

**Outcomes**:
- 12 cycles run.
- ~14 Phase-2 + 3 Phase-3 characters documented as "solved" in `drawer_memory.md`.
- Visual scores: ranged 0.15–0.33 in cycle 1, 0.74–1.00 for finalist strokes.
- Phase transitions reached, but POSTMORTEM noted "lone-stroke phase-correlation near noise floor" by cycle 6 — the *measurement* was the bottleneck before the *memory* was.

### Run 2 — 3 cycles · composite shape-fidelity judge · frozen at Phase 1
**Postmortem**: [runs/run_2/POSTMORTEM.md](runs/run_2/POSTMORTEM.md).
**Core problem documented**: hand-coded stroke GTs were weaker calligraphy than the Drawer's own strokes. The composite judge (Dice + Chamfer + proportion) then *penalised* richer detail and coached the model *downward*.

| Dimension | Design |
|---|---|
| **Teacher** | Hard gate: no Phase-1 advancement until all 6 atomic strokes ≥ 0.85. Cycle 1 taught all 6 at once; cycles 2–3 drilled failing strokes. OCR off for strokes. |
| **Drawer memory** | `drawer_memory.md` (135 lines), more terse than run_1. Compact stroke recipes as code blocks. |
| **Drawer design** | Fresh subagent. Used low-level turtle calls more than the vendored stroke library. |
| **Judge** | Dice + symmetric Chamfer + proportion → visual_score in [0,1]. Faithful single strokes scored 0.94–1.00, weak ones 0.6–0.7. Calibrated to be monotonic. |

**Outcomes**:
- 3 cycles, then frozen.
- **Promoted**: only heng / pie / ti reached ≥ 0.85.
- **Failed to promote**: na, dian regressed (0.70 → 0.60 → 0.24 after two attempted recipe corrections).
- Frozen at cycle 3 because the GT-quality ceiling was structural — no amount of further drilling could pass.

### Run 3 — 25 cycles · text-brief Drawer · vision-blind composition
**Postmortem**: [runs/run_3/POSTMORTEM.md](runs/run_3/POSTMORTEM.md).
**Core problem documented**: "composition precision wall." Text prescriptions couldn't reliably resolve OCR-similar characters (也→卫/已/吧, 寸→十/于, 万→力/九). 37 Phase-2 characters mastered but 3 were stuck. `drawer_memory.md` grew to ~250 lines and became *noisier* with size.

| Dimension | Design |
|---|---|
| **Teacher** | 6 tasks/cycle. Hard no-skip rule after c11 (un-retired 大/入/火 and re-mastered them in c12). Eval per cycle: `gt+ocr+vision` for characters. |
| **Drawer memory** | Still `drawer_memory.md` (~250 lines). No code bank. |
| **Drawer design** | Text-brief-only Drawer. No vision of the GT image. Composes by reading past failures and applying prescriptions. |
| **Judge** | Same as run_2 (visual + OCR + rubric 0–10). Mastery: `is_correct AND visual_score AND rubric ≥ 7 with no 0`. |

**Outcomes** (from `git log --oneline -- runs/run_3` and `judge_results/`):
- 100 cycle-related commits.
- 36 commits mention promotion/mastery; 39 mention carry-over.
- **~37 characters mastered** (per POSTMORTEM).
- **Cycle pass-rate trajectory**: c1–c2 (6/6 each), c3–c11 (0–1 / 6), c12–c16 (3–5 / 6), c17 brushwork regression (0/6), c18+ (2–4 / 6).
- Boundary cases stuck: 也, 寸, 万 — visible OCR-confusion class.

### Run 4 — 24 cycles · structured Success Bank · vision-allowed Drawer
**Postmortem**: [runs/run_4/POSTMORTEM.md](runs/run_4/POSTMORTEM.md).
**Core problem documented**: text-only briefs were not sufficient. Drawer (still vision-blind to GT in run_4 initial design — later partially relaxed) couldn't tell whether its output was the target or a neighbor. The Curator/Teacher *progressively lowered* mastery gates mid-run: 入 promoted at visual_score 0.58, 力 at 0.39 — both OCR-passed but visually wrong. **OCR ≠ visual identity.**

| Dimension | Design |
|---|---|
| **Teacher** | 1 task/cycle in Phase 3. Atomic strokes c1–c6, compound c7–c13, characters c14+. Generates GTs via `tools/make_char_gt.py`. |
| **Drawer memory** | **Three-bank** architecture introduced: Success Bank (immutable `code/*.py` + `INDEX.md`), Principle Bank (positive rules), Sandbox (short-term scratch). Entries stored as `(t, ox, oy, scale)` tuples — *numeric magic numbers*. |
| **Drawer design** | Fresh subagent. Hard filesystem quarantine of `tools/`. GT image visible (vision-aware). Two-phase skeleton-then-brushwork for characters. Self-preview ≤ 2 iterations. |
| **Judge** | Same metrics as run_3. Phase-3 mastery: `is_correct AND ocr_conf ≥ 0.4 AND rubric ≥ 7 no 0`. Calligraphy rubric added (顿笔 / 弧度 / taper / proportion / overall, 0–2 each). |

**Outcomes**:
- 24 cycles run.
- **20 bank entries** (per `ls runs/run_4/success_bank/code/`).
- 21 promote-mentions in commit log.
- POSTMORTEM flags **~2 false positives** (入 at 0.58, 力 at 0.39) → real bank ≈ 17–18 entries.
- Mid-run gate lowering visible across cycle_state notes.

### Run 5 — 25 cycles · adversarial 3-judge panel · frozen
**Postmortem**: [runs/run_5/POSTMORTEM.md](runs/run_5/POSTMORTEM.md).
**Core problem documented**: the 4-gate (OCR is_correct + ocr_margin ≥ 0.3 + visual_score > 0.8 + 3-judge panel unanimous YES) was *insufficient for structural fidelity*. Concrete leaks: **五 c20** (5 turtle calls vs MMH's 4 — extra heng) and **丘 c24** (6 vs 5 — extra shu) both passed all four gates. The whole-image pixel metrics absorbed the extra strokes; the panel was asked "is this the right character" but never "is the stroke count right".

| Dimension | Design |
|---|---|
| **Teacher** | 3 tasks/cycle. Phases 1–4. Mastery rule based on Curator vision + rubric ≥ 7. |
| **Drawer memory** | Same Success Bank format as run_4 (numeric `(ox, oy, scale)`). 35 code files at freeze. Inherited 13 stroke entries from run_4 without isolated practice. |
| **Drawer design** | Fresh subagent, GT-aware, can mimic visually. 3 tasks/cycle. |
| **Judge** | **4-gate**: (1) OCR is_correct, (2) ocr_margin ≥ 0.3, (3) visual_score > 0.8, (4) 3 fresh-context skeptic subagents — all 3 must say YES. **No structural gate**. |

**Outcomes**:
- 25 cycles, then frozen.
- **35 bank entries** (per `ls runs/run_5/success_bank/code/`).
- 19 promote-mentions, 11 carry, 1 frozen in commits.
- Promotion rate ≈ 22/25 ≈ **88%** — but POSTMORTEM identifies this as misleadingly high due to the missing structural gate.
- **2 known false positives** (五 c20, 丘 c24) — false-positive rate ≈ 9% of promotions.

### Run 6 — 64 cycles (in progress) · 米字格 anchors + joint taxonomy
**Postmortem**: not yet written (run still active). State recorded in `runs/run_6/cycle_state.json`.

| Dimension | Design |
|---|---|
| **Teacher** | **1 task/cycle**. Phases 1 → 1.5 → 2 → 3. Joint classification (P/T/N) mandatory in briefs. Stroke-pedagogy rules. Apex-share override for 撇捺-apex characters. Cannot advance phase without Curator promotion. |
| **Drawer memory** | **Anchor notation** (米字格 cell + x_frac + y_frac). No magic numbers. Joints derived from MMH via `find_joints`, classified via `classify_joints.classify`. 42 code files = 1 utility + 41 entries at cycle 64. |
| **Drawer design** | Fresh subagent, hard quarantine of `tools/`. Pre-flight stroke-count check. **3-attempt freeze rule** preserves failed renders as evidence. **Raw MMH endpoints** policy: never override from joints (P/N classes are panel-side hints, not Drawer-side constraints). Apex-share override applied after raw extraction. |
| **Judge** | **5-gate**: (1) OCR informational, (2) visual_score informational, (3) `structural_pass == True` (stroke count + anchor placement ≤ 15 px + joint placement ≤ 20 px in declared cell) — HARD, (4) 3-judge panel unanimous YES — HARD, (5) Curator vision (informational). Panel prompts include per-character joint-class summary built from `classify_joints`. |

**Outcomes (cycle 64)**:
- **41 bank entries** (vs run_5's 35).
- Commit log: 26 promote-mentions, 4 carry, 3 frozen.
- Promotion rate ≈ 23/64 ≈ **36%** (vs run_5's inflated 88%).
- Structural gate caught **里 c30** false positive (1 connected component vs needed 7) → demoted post-hoc.
- Frozen cycles (c56 山, c63 出, c64 头) preserve genuine failure evidence rather than being overwritten.

---

## Pairwise comparisons (what changed, what it did to the Drawer)

### Run 1 → Run 2

| | Run 1 | Run 2 | Effect |
|---|---|---|---|
| **Teacher** | 3 tasks/cycle, soft carry-over | All 6 strokes/cycle, hard ≥ 0.85 gate | Forced depth-over-breadth — but exposed GT ceiling. |
| **Drawer memory** | 300-line `drawer_memory.md` | 135-line tighter format | Lessons more reusable, but unchanged in *kind*. |
| **Drawer design** | High-level vendored strokes | Low-level turtle calls + same vendored library | Drawer gained finer control; calibration-quality demands rose. |
| **Judge** | Phase-correlation (non-monotonic) | Dice + Chamfer + proportion (monotonic-calibrated) | Reward signal stabilised on **trustworthy GTs**, broke on **untrustworthy GTs**. |

**Drawer performance effect (with numbers)**:
- Run_1 cycle 1 visual scores for heng/shu/pie: 0.15 / 0.20 / 0.33. Final-cycle equivalents for solved strokes: 0.74–1.00.
- Run_2 cycle 1 visual scores for all 6 strokes (cleaner judge): 0.66 / 0.92 / 0.83 / 0.83 / 0.92 / 0.98 — mean 0.86.
- BUT: by run_2 cycle 3, na/dian regressed (0.70 → 0.60 → 0.24) under Curator-prescribed "corrections" — because the GT itself was inferior to the Drawer's natural output.
- **Net**: the judge change exposed a *new* problem (weak GT) that wasn't visible under the noisier run_1 judge. This is "self-evolution" in the very weak sense: the system found its own measurement bug, but a human had to redesign the run to fix it.

### Run 2 → Run 3

| | Run 2 | Run 3 | Effect |
|---|---|---|---|
| **Teacher** | 6 strokes/cycle, no advance until all ≥ 0.85 | 6 characters/cycle, no-skip rule | Phase 1 abandoned (frozen); jumped to characters where GTs (MakeMeAHanzi) are trustworthy. |
| **Drawer memory** | 135-line markdown | ~250-line markdown (same kind, just longer) | **Size hurt rather than helped** — POSTMORTEM identifies this as the "noisier-with-size" failure. |
| **Drawer design** | Same fresh-subagent + turtle | Text-brief, no GT vision | Less freedom but more reproducible. |
| **Judge** | Composite visual + OCR | Same + calligraphy rubric | OCR added rich signal for characters; rubric added structure for strokes. |

**Drawer performance effect (numbers)**:
- Run_2: 0 characters mastered (frozen at Phase 1).
- Run_3: ~37 characters mastered across 25 cycles, mostly in cycles 12–25 (per POSTMORTEM).
- Pass-rate trajectory: c1–c2 → 6/6 (atomics), c3–c11 → 0–1 per cycle (struggling), c12–c16 → 3–5 per cycle (the "memory paying compounding interest" effect), c17 → 0/6 (brushwork regression after technical change), c18+ → 2–4 per cycle.
- **Net**: scaling characters worked; scaling *memory format unchanged* didn't. The big lesson driving run_4 was "we need a *structured* bank, not a longer log."

### Run 3 → Run 4

| | Run 3 | Run 4 | Effect |
|---|---|---|---|
| **Teacher** | 6 tasks/cycle, mixed phases | **1 task/cycle**, strict phase progression | Slower throughput but tighter feedback per focus. |
| **Drawer memory** | Markdown log | **Three banks**: Success Bank (immutable code/*.py), Principle Bank, Sandbox | **First structured bank**. Composition by `(t, ox, oy, scale)` tuples. |
| **Drawer design** | Text-brief-only, blind to GT | GT-visible, two-phase skeleton+brushwork, quarantine of `tools/` | Could now self-correct against GT pixel positions. |
| **Judge** | Same metrics | Same metrics + calligraphy rubric primary for strokes | Per-phase eval per Teacher choice. |

**Drawer performance effect (numbers)**:
- Run_3: 37 mastered characters, but only as natural-language entries — no transferable code.
- Run_4: **20 nominal bank entries** at cycle 24 → ≈ **17–18 real** (after subtracting 入/力 false positives flagged in POSTMORTEM).
- Promotion-rate ≈ 21/24 ≈ 88% (commit-log mentions). High but inflated by gate-lowering mid-run.
- **Transfer evidence**: 末 reused 木; 卞 reused 下; 主 reused 王 stack. POSTMORTEM credits the composition-by-tuple system for unlocking this.
- **New failure mode introduced**: false-positive promotions — visible because the *structured* bank could be audited later, where run_3's natural-language log couldn't.

### Run 4 → Run 5

| | Run 4 | Run 5 | Effect |
|---|---|---|---|
| **Teacher** | 1 task/cycle | 3 tasks/cycle | Faster, more chars per session; less depth per char. |
| **Drawer memory** | Code bank, `(ox, oy, scale)` tuples | Same format, but 35 entries (carried run_4 strokes + new characters) | No format change; size grew. |
| **Drawer design** | Two-phase skeleton+brushwork, vision-aware | Same with refined quarantine | Marginal. |
| **Judge** | OCR + visual + rubric, 1 Curator | **4-gate**: OCR is_correct + margin ≥ 0.3 + visual > 0.8 + **3-judge panel unanimous YES** | Added independent verification — closed the *gate-lowering* failure mode of run_4. |

**Drawer performance effect (numbers)**:
- Run_4 promoted 17–18 real characters in 24 cycles (≈ 0.75/cycle).
- Run_5 promoted **22 characters in 25 cycles** (≈ 0.88/cycle).
- Promotion rate inflated to 88% on commit-mention basis.
- **BUT** structural false positives **persisted and were now hidden by the panel**: 五 c20 (5 vs 4 strokes), 丘 c24 (6 vs 5) both 3/3 panel YES with all four gates passed.
- False-positive count rose because nothing was *checking* structure: ≥ 2 documented, possibly more.
- **Net**: the panel closed one class of failure (Curator-Teacher-vision collusion) and exposed another (whole-image pixel metrics absorbing extra strokes). The system did *not* self-discover this — the user did, by reviewing the bank manually.

### Run 5 → Run 6

| | Run 5 | Run 6 |
|---|---|---|
| **Teacher** | 3 tasks/cycle, OCR-gated phase advance | **1 task/cycle**, joint classification (P/T/N) per character, apex-share overrides for 撇捺-apex chars |
| **Drawer memory** | Numeric `(ox, oy, scale)` tuples | **Anchor notation** (cell, x_frac, y_frac) — structural, no magic numbers. MMH median + `find_joints` + `classify_joints` as the source of truth. |
| **Drawer design** | Fresh subagent, GT-aware | Same + **stroke-count pre-flight**, **3-attempt freeze rule** (failed renders preserved, not overwritten), raw MMH endpoint policy |
| **Judge** | 4-gate (OCR + margin + visual + panel) | **5-gate**: structural pass (stroke count + anchor placement + joint placement) is HARD; panel with calligraphy-aware per-joint-class prompts is HARD; OCR + visual are informational |

**Drawer performance effect (numbers)** at cycle 64 of run_6:
- **41 bank entries** (vs run_5's 35) — net positive even with the much stricter gate.
- Promotion rate 23/64 ≈ **36%** (vs run_5's headline 88%). The lower rate is *correct* — it reflects a real gate.
- Structural false positives: **1 caught and demoted post-hoc** (里 c30, `structural_pass=false` was logged but I promoted anyway — fixed by demoting and adding the 3-attempt-freeze rule). Vs run_5's ≥ 2 *unpaughtt* false positives.
- Carry-overs: 4 mentions. Frozen cycles: 3 — first run where genuine failure is preserved as evidence rather than overwritten.
- **Transfer/reuse**: visible in 个/牛/立/半/白/田 etc. composing from the atomic-stroke / compound-stroke bank.
- **Self-discovery of a new failure mode**: the c43–c52 "joint-snap" regression, where applying head/tail-snap to every joint *worsened* characters that were previously correct (口 c32 → c43). This was identified by the user after watching the panel reject c43–c52 chars that c32–c41 had passed, and led to the run_6 joint-taxonomy redesign.

---

## Cross-cutting findings

### Finding 1 — What is being memorized matters more than how much
The 6-run arc moves through three memory representations:
1. **Natural-language lessons** (run_1, run_2, run_3): grows linearly with cycles, hits a noise wall around 250 lines (run_3).
2. **Numeric magic-number tuples** (run_4, run_5): code-grade composition, but unauditable structure — admits false positives.
3. **Anchor notation + joint topology** (run_6): structural by construction; mechanical verification possible; false-positive rate falls.

The thing that determined whether the system improved between runs was almost always a change in *what the memory looks like*. Bank size grew (0 → 35 → 41) but slowly. **Bank quality** (auditability, transferability, false-positive rate) grew faster.

### Finding 2 — The judge is the second-most important variable
Across all 5 transitions, the judge was changed every time. The judge change either *exposed a new class of failure* (e.g., run_2's monotonic judge revealed the GT-ceiling problem; run_5's panel revealed the gate-lowering problem; run_6's structural gate revealed the stroke-count problem) or *enabled new memory format* (run_6's structural gate is the only thing that made the anchor-notation representation operational — without a structural check, anchors are just another tuple).

The judges that improved the Drawer most were the ones that *forced an honest signal*. Phase-correlation (run_1) was too noisy. Composite + OCR + rubric (run_3/4) was lenient. 3-judge panel (run_5) closed Curator bias. Structural + panel (run_6) closes hidden-structure errors.

### Finding 3 — "Self-evolution" within a run is real, but narrow
Within a run, the Drawer reads the bank, drafts new code, gets judged, and either gets accepted or refined. This loop *does* improve outputs: run_3 cycles 12–16 show 3–5 chars/cycle promoted where c3–c11 showed 0–1. Run_6 cycles 32–54 show transfer (口 from c32 powers 古 attempts in c60). This is real iterative learning.

But the *loop itself* — who Teacher is, what Drawer sees, what Judge measures — never changed by the system's own action. Every loop change came from a human reading a POSTMORTEM and proposing a new architecture. **The strong form of self-evolution is not demonstrated in DC-ACE so far.**

### Finding 4 — Promotions are the wrong primary metric without a structural floor
Run_5 promoted at 88%; run_6 promoted at 36%. Run_6's bank is *more* trustworthy than run_5's. The headline promotion rate is misleading because the gate strength varied. A better primary metric for future runs:

- **False-positive rate** = (entries the user later flags as wrong) / (promotions)
- **Reuse rate** = (downstream uses of a Success Bank entry) / (cycles after promotion)
- **Carry-over recovery rate** = (carry-overs eventually promoted) / (total carry-overs)

DC-ACE never operationalised reuse rate — there's no per-entry import counter. That's a gap.

### Finding 5 — Failure preservation is itself a learning enabler
Run_6 introduced the **3-attempt freeze rule** mid-run after the c40 目 regression (an attempt-3 render replaced an attempt-2 render that was actually correct). The rule says: after 3 overwrites in the same `attempts/cycle_<N>/generated.py`, freeze the directory and start a new cycle number. Three cycles are now frozen in run_6 (c56 山, c63 出, c64 头), each with a `FROZEN.md` postmortem.

This is the first time in 6 runs that *failed attempts are durable*. Previously, every failed render was overwritten by the next attempt and lost. The data this preserves is what makes between-run redesigns more honest going forward.

---

## Verdict on the central question

> **Can an AI learn by itself / self-evolve?**

Three concentric answers, each more conservative:

**(a) Within-run iterative learning — YES, demonstrated.**
The cycle loop (Teacher → Drawer → Judge → Curator → bank update) improves outputs over time without code edits. Concrete evidence: run_3 c12 promotion-rate spike; run_4's 17–18 mastered characters; run_6's 41-entry compositional bank where 二, 三, 十, 王, 主 reuse 一's primitive. Transfer is real.

**(b) Memory-mediated transfer — YES, partial.**
Mastered entries get reused by the Drawer in characters it has never seen. This is one definition of "learning". The catch: transfer quality depends entirely on what's in the bank, and run_4's tuple-based bank transferred a *broken* 力 forward to 万 in downstream cycles, so transfer can amplify errors as well as successes.

**(c) Architectural self-improvement (the strong claim) — NO, not demonstrated.**
Every between-run redesign (text-log → tuple bank → anchor notation; phase-correlation → composite → 4-gate → 5-gate) was *human-proposed* after reading a POSTMORTEM. The system did not redesign its own loop. The closest evidence to (c) is the c43–c52 self-discovered joint-snap regression: the user noticed the system was *making things worse*, then proposed the fix. The *noticing* was done by the human-reviewer, not the system.

Honest one-line answer: **DC-ACE has demonstrated within-run learning and memory-mediated transfer, but has not demonstrated architectural self-evolution. The loop iterates; the loop's design is still human-driven.**

---

## Limitations and threats to validity

1. **Single researcher, no control group.** Every run's redesign reflects one person's reading of the previous postmortem. A control run keeping run_5's design unchanged for 64 more cycles would tell us whether the *design change* or the *additional cycles* drove run_6's gains.
2. **Judge LLMs are the same family as Drawer LLMs.** Panel skeptics are Claude subagents. Drawer is a Claude subagent. There is no truly independent verifier. Hidden correlated errors are possible.
3. **Reuse rate was discussed but never logged.** Without a downstream-import counter, "transfer" claims rely on spot-checks.
4. **Token / cost data not tracked.** A run that doubles cycles but quadruples cost may not represent improvement.
5. **Postmortems are written by the same researcher running the experiment.** Authorial bias toward the redesign hypothesis is possible.
6. **No baseline.** We don't have "no Memory" or "random Memory" runs to compare against. The bank may help, but the magnitude is unverified.
7. **Pixel quality ≠ memory quality.** Chinese characters are the *vehicle*. The headline metric (mastered chars) measures a downstream proxy.

---

## What the next pass needs

- **Reuse-rate logger.** Count downstream imports per bank entry per cycle; dump to `dashboard.md`. This makes "transfer" auditable.
- **A control run.** Re-run a single architecture for ≥ 40 cycles and see whether the bank growth curve flattens, accelerates, or stalls *without* between-run intervention.
- **A separate verifier model.** Use a non-Claude judge (e.g., a vision-LLM from another lab) for some panel skeptics to break the correlated-error risk.
- **An adversarial Memory test.** Inject a known-bad entry into the bank and see whether the loop catches it on downstream reuse.
- **A pre-registered hypothesis for run_7.** State in advance what would count as evidence *against* the central claim. The current method tends toward confirmation: each redesign succeeds by definition because the user picks the post-success commit as the new baseline.

---

## Appendix — quick-reference scope table

| Run | Cycles | Bank entries | Promote-mentions in commits | Carry-mentions | Frozen | Memory format | Judge headline |
|---|---|---|---|---|---|---|---|
| 1 | 12 | n/a (300-line MD) | 0 (no structured bank) | 0 | 0 | natural-language log | phaseCorrelate + OCR |
| 2 | 3 | n/a (135-line MD) | 4 | 1 | 0 | natural-language log | Dice + Chamfer + proportion |
| 3 | 25 | n/a (~250-line MD) | 36 | 39 | 0 | natural-language log | composite + OCR + rubric |
| 4 | 24 | 20 | 21 | 2 | 0 | `(ox, oy, scale)` tuples | composite + OCR + rubric |
| 5 | 25 | 35 | 19 | 11 | 1 | `(ox, oy, scale)` tuples | 4-gate + 3-judge panel |
| 6 | 64 (active) | 41 | 26 | 4 | 3 | 米字格 anchors + joints | 5-gate + per-class panel |

(`Promote-mentions` and `carry-mentions` are commit-log keyword counts and over-count slightly. Bank-entry counts are from `ls runs/<r>/success_bank/code/*.py`.)
