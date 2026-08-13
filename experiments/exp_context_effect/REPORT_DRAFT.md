# Memory Formats and Structural Priors in AI Iterative Learning:
## An Ablation Study on Compositional Visual Generation

*Draft — v1, 2026-08-13*

---

## Abstract

We investigate how memory format influences an AI agent's ability to iteratively improve on a compositional, out-of-distribution task, using Chinese-character drawing (668 curriculum items) as a proxy for the kind of niche, quality-gradable tasks that motivate AI-for-science applications. We compare five conditions: a memoryless control, a free-form markdown memory, a callable-code memory bank, a 米字格 grid memory paired with structural data injection, and a code memory paired with the same data injection. The design isolates two candidate contributors to iterative gains — memory format itself, and injected structural priors — and permits a factorial decomposition on identical items.

Our central findings: **(i)** memory-format sophistication alone (without a structural prior) lifts pass rate only 3-4 percentage points above a memoryless control across 668 items and does not raise quality ratings; **(ii)** injecting structured stroke-endpoint priors lifts pass rate by 24 points and unlocks the quality ("A") verdict tier from ~0% to 15%; **(iii)** rendering-format richness (per-endpoint stroke width) trades baseline correctness for further quality gains — grid format beats code format on A rate (20% vs 15%) but the code format beats grid on aggregate pass rate (47% vs 43%). We conclude that structured priors — not memory scaffolding per se — are the dominant lever for iterative improvement on this task, and discuss what that implies for the AI-for-science research agenda.

---

## 1. Introduction

### 1.1 Motivation: memory as a substrate for AI-for-science

A long-standing claim in AI research is that persistent, updatable memory should enable open-ended iterative improvement on tasks where a single forward pass is insufficient. This claim underpins much of the current interest in AI-for-science: the hope is that agentic systems, given a hard problem, can produce attempts, evaluate their own failures, update memory, and progressively converge on high-quality solutions — much like a human scientist iterating on hypotheses in a notebook.

For this claim to be actionable, two empirical questions matter:

1. **Does the *format* of memory affect the trajectory of improvement?** If markdown notes, structured databases, and code banks all produce the same trajectory, the format-design problem is not interesting.
2. **How much of measured "iterative improvement" is attributable to memory versus other contributors** — task priors, model capacity, retrieval scaffolding?

Direct observation on frontier AI-for-science tasks (novel biological discovery, materials design) is difficult: the problems are open-ended, ground truth is scarce, and per-item cost is high. We need a **proxy task** with three properties: out-of-distribution enough that direct model recall is not the story; compositional enough that memory has room to help; and quality-gradable so we can distinguish "correct" from "correct and well-formed."

### 1.2 Chinese-character drawing as a proxy

Rendering Chinese characters programmatically (as Python scripts producing 300×300 PNGs) satisfies all three criteria:

- **OOD**: Frontier language models are not trained to write executable rendering code for specific characters at pixel-level fidelity. Every attempt is a fresh compositional problem.
- **Compositional**: Characters decompose into radicals, radicals into strokes; the same sub-components recur across many characters. Successful memory should crystallize component-level knowledge and reuse it.
- **Quality-gradable**: Human judges can distinguish (a) *incorrect* attempts, (b) *correct but crude* attempts, (c) *correct and calligraphically clean* attempts, on the same rubric they'd apply to student handwriting. This gives us a two-tier verdict — pass vs. quality — that AI-for-science needs but rarely measures cleanly.

### 1.3 The research question, sharpened

Given the setup, the core question becomes: **on a niche compositional task with a human judge, what actually drives iterative improvement across many attempts — memory alone, memory of a specific format, or structural priors delivered independently of memory?** We designed a five-group ablation to answer this.

### 1.4 Contributions

- A five-group factorial ablation of memory-format effect and structural-prior effect on 668 items over ~15 batches per group.
- A two-factor decomposition showing that structural priors dominate the pass-rate lift while memory format alone barely improves over control.
- Evidence for a second-order effect: **rendering-format richness** (per-endpoint stroke width vs. uniform-width lines) trades baseline correctness for quality-verdict gains.
- A methodological artifact worth reporting: **a research-integrity confound we caught mid-experiment** — one memory group was receiving privileged structural data the others were not, requiring a post-hoc pivot group (G5) to disentangle the format effect from the data-injection effect.
- Public data + code enabling replication.

---

## 2. Methods

### 2.1 Task specification

For each of 668 curriculum items (135 Phase-2 radicals + 533 Phase-3 characters, ordered by ascending stroke count), an AI drawer subagent is dispatched with (a) the character label, (b) group-specific memory access, and (c) a ground-truth PNG for visual comparison. The drawer writes a Python script (`generated.py`) using PIL and optional bank primitives, executes it to produce a 300×300 PNG (`01_<char>.png`), and may revise once after visual self-check.

Batch structure: 14 batches (bootstrap + B1-B13) of 50 items each. After each batch, a human judge blind-labels each attempt on a 4-level rubric: **A** (calligraphically clean, print-quality), **PASS** (recognizable and correct), **C** (close but incorrect), **FAIL** (unrecognizable). The A and C tiers were introduced at batch B9 (v12 intervention); prior batches use binary PASS/FAIL.

After judgment, per-group curator agents update memory files, promote bank primitives from PASS/A attempts, and queue retry candidates. Retries follow a cool-down + terminal-freeze protocol.

### 2.2 The five groups

| Group | Memory format | Structural prior injection | Curator |
|---|---|---|---|
| G1 | none (memoryless control) | none | none |
| G2 | free-form markdown files | none | yes |
| G3 | callable-Python code bank (frozen primitives with `(ox, oy, scale)` signature) | none | yes |
| G4 | 米字格 grid anchor language + `fat_line(w1, w2)` per-endpoint-width primitive | **yes** — stroke count, per-stroke endpoint anchors, joint typology injected per attempt from MakeMeAHanzi (MMH) medians | yes |
| G5 | callable-Python code bank (**identical to G3**) | **yes** (same MMH injection as G4) | yes |

**G5 is a post-hoc pivot group.** In its original form the experiment had only G1-G4, but midway through we discovered that only G4 was receiving MMH structural injection — a confound that would have made the G4-vs-others comparison uninterpretable as a pure format-effect test. We resolved this by (a) documenting the confound in the interventions log, (b) leaving G4 unchanged to preserve its cumulative trajectory, and (c) introducing G5, whose memory format matches G3's but which receives the same MMH injection G4 has always had. G5 was subsequently reset and re-run through the entire curriculum from bootstrap to B13 to provide parallel coverage. See §2.5 for the detailed timeline.

### 2.3 Memory architecture

All memory-having groups (G2/G3/G4/G5) share the same curator/drawer separation: the drawer produces attempts but never writes to memory files; the curator reads attempts + judge verdicts and writes memory. Under a v7-and-later unlock, curators may freely restructure their own memory (create new files, retire unhelpful ones, split large files) subject only to the group's core format constraint. Structural changes are logged to a per-group `evolution.md`.

A `pass_index.md` file is auto-generated per group listing every PASS/A attempt with a pointer to the rendered PNG; drawers and curators may consult prior successes visually rather than only through the memory abstractions.

### 2.4 The MMH structural prior — what is and isn't in it

The MakeMeAHanzi `graphics.txt` database contains, for each character, a list of stroke medians (SVG-path-derived polylines sampled at ~30 points). At drawer-dispatch time for G4 and G5, our code (`tools/mmh_joints.py`) reads this file live, extracts each stroke's head/tail endpoints, computes joint expectations (welded / small-gap / tangent classifications with expected pixel gap), and prepends a "structural expectations" block to the drawer prompt containing: (a) expected stroke count, (b) per-stroke head+tail pixel coordinates (precise to ~1px on 300px canvas), (c) joint typology.

**What MMH does not provide:**
- The curve shape between stroke endpoints — the drawer must interpolate.
- Stroke widths or calligraphic modulation — MMH is skeletal.
- Any hint about ink flow, hook aesthetics, or brush pressure.

**What no group receives**: raw `graphics.txt` (all groups are forbidden from opening it). The rendered ground-truth PNG (a thin uniform-width rendering of MMH medians via `make_char_gt.py`) is visible to all groups.

### 2.5 Interventions timeline

Fourteen human interventions across the experiment, all documented in `INTERVENTIONS.md`. The most consequential:

- **v7 (position 150)**: Memory self-evolution unlocked. Prior to this, memory schemas were fixed by us; from B4 onward, curators may restructure freely within format constraints.
- **v8 (position 350)**: Bank primitives declared REFERENCE-ONLY. Drawers may skip bank entries in favor of fresh inline renders. Motivated by observed "over-compliance" — drawers using bank primitives even when they visibly clashed with the GT.
- **v12 (batch B9)**: A / C verdicts introduced to distinguish quality tiers. Prior batches carry only PASS / FAIL.
- **v13 (position 500)**: BANK_DEVIATION channel — drawers may skip bank primitives and inline fresh renders, with a note to the curator; if the composition passes, curator may promote the fresh sub-element as a bank variant. Enabled evidence-driven bank variant growth without curator speculation.
- **v14 (post-B11, 2026-08-03)**: An attempt to disable MMH injection for G4 as a pure format-effect test. Rolled back the same day after B12v1 showed G4 pass rate collapsed from 62% to 16%. The finding was preserved by introducing G5 (see §2.2) instead.

### 2.6 Judgment protocol

The judge is a single human (the first author) blind to group identity per attempt. `tools/judge_blind.py` shuffles group labels within each item so the judge sees only the character label + target PNG + one anonymized attempt, with the A/PASS/C/FAIL keys.

A verdict of A ("calligraphically clean and print-quality") is stringent — items with correct stroke counts and shapes but uniform-width crude rendering will typically score PASS, not A. The judge did not consistently issue A verdicts in G5's early catch-up batches, where they were used as "memory-benefit signals" (i.e., not fair-comparison) rather than fully calibrated A-quality tags; consequently our fair A-rate comparisons in Table 4 exclude G5's pre-B8 A count and count only from B9 (the batch where all groups first had A-verdict opportunity).

---

## 3. Results

### 3.1 Per-batch trajectory (success rate = A+PASS)

```
Batch    Range (idx)                G1     G2     G3     G4     G5
bootstrap P2 001-018                83%    83%    78%    67%    83%
B1        P2 019-068                60%    70%    54%    70%    62%
B2        P2 069-118                38%    40%    34%    40%    38%
B3        P2 119-135 + P3 001-033   54%    60%    58%    58%    70%
B4        P3 034-083                58%    58%    54%    62%    58%
B5        P3 084-133                46%    48%    38%    52%    54%
B6        P3 134-183                32%    52%    46%    52%    64%
B7        P3 184-233                30%    42%    32%    50%    66%
B8        P3 234-283                12%    12%    18%    40%    40%
B9        P3 284-333                22%    24%    28%    40%    44%
B10       P3 334-383                12%    20%    24%    38%    52%
B11       P3 384-433                12%    16%    28%    62%    56%
B12       P3 434-483                20%    24%    14%    40%    46%
B13       P3 484-533                12%     4%    20%    36%    38%
```

**All groups exhibit a difficulty-driven collapse from ~60% on radicals to ~15-40% on Phase-3 characters, most pronounced at B8 where all four originally-planned groups drop to 12-40%.** G4 and G5 (the two MMH-injected groups) sustain 40-60% through Phase-3 depth while G1/G2/G3 (no-MMH) settle at 12-30%. G5 crossed G4's per-batch pass rate at B10 and led on 3 of the last 4 batches.

### 3.2 A-verdict count per batch (B9 onward, the fair-comparison window)

```
Batch    G1    G2    G3    G4    G5
B9        0     2     0    10     4
B10       1     2     0    10     7
B11       1     0     0    17     9
B12       1     1     1     8    10
B13       3     0     0     6     8
Total     6     5     1    51    38
```

**G4 leads A-count on 4 of 5 batches** (B12 the exception, where G5 edges out 10 vs 8). G3 (the no-MMH code group) has 1 A across 250 items — a near-absolute quality ceiling. G1 (memoryless control) accumulates 6 A verdicts across 250 items, all in the second half of the curriculum — see §3.5.

### 3.3 Cumulative through B13 (668 items each)

| Group | A | PASS | C | FAIL | Success | A rate |
|---|---|---|---|---|---|---|
| G1 (no memory, control) | 6 | 213 | 25 | 424 | **33%** | 0.9% |
| G2 (free-form markdown) | 5 | 245 | 34 | 384 | **37%** | 0.7% |
| G3 (code bank, no MMH) | 1 | 237 | 34 | 396 | **36%** | 0.1% |
| G4 (grid + MMH) | 51 | 281 | 41 | 295 | **50%** | **7.6%** |
| G5 (code + MMH) | 47 | 312 | 122 | 187 | **54%** | 7.0% |

The ordering by pass rate is **G5 > G4 > G2 ≈ G3 > G1**. By A rate it is **G4 > G5 > G1 > G2 > G3**.

### 3.4 The two-factor decomposition

Restricted to the fair-comparison window (B9-B13, 250 identical items each):

**MMH effect** (G3 vs G5, both same code memory format, only MMH differs):

| Group | A | PASS | C | FAIL | Success | A rate |
|---|---|---|---|---|---|---|
| G3 (no MMH) | 1 | 56 | 34 | 159 | 23% | 0.4% |
| G5 (MMH added) | 38 | 80 | 33 | 99 | **47%** | **15.2%** |
| **Δ from MMH** | +37 | +24 | −1 | −60 | **+24pt** | **+14.8pt** |

**Format effect** (G4 vs G5, both same MMH prior, only rendering format differs):

| Group | A | PASS | C | FAIL | Success | A rate |
|---|---|---|---|---|---|---|
| G4 (grid + fat_line) | 51 | 57 | 41 | 101 | 43% | **20.4%** |
| G5 (code + PIL uniform) | 38 | 80 | 33 | 99 | **47%** | 15.2% |
| **Δ from grid+fat_line** | +13 | −23 | +8 | +2 | **−4pt** | **+5.2pt** |

Structural priors and rendering format thus have **partially orthogonal contributions and in one dimension trade off against each other**: adding MMH massively raises pass rate and modestly raises A rate; substituting grid+fat_line for code+PIL-uniform trades ~4pt of pass rate for ~5pt of A rate. Together they compound (G4 = both, achieves the highest A rate; G3 = neither, achieves the lowest A rate).

### 3.5 Memory-only effect (G1 vs G2 vs G3, all no-MMH)

- G1 (no memory): 33% success, 0.9% A rate.
- G2 (markdown memory): 37% success, 0.7% A rate.
- G3 (code-bank memory): 36% success, 0.1% A rate.

**Memory alone, without a structural prior, adds only 3-4 percentage points to pass rate over the memoryless control across 668 items and does not lift A rate above control**. Code-bank format even *reduces* A rate below control, which we attribute to the frozen primitive constraint: G3's callable code cannot easily modulate stroke width per endpoint, which is the calligraphic degree of freedom that judges reward as A.

### 3.6 The G1 solo-A phenomenon

Six A verdicts came from G1 (the memoryless control) — a small count in absolute terms but strikingly clustered. Four of the six are **solo wins**: G1 was the only group whose attempt on that item scored A, while every memory-equipped group's attempt on the same item scored FAIL or C:

| Batch | Item | G1 | G2 | G3 | G4 | G5 |
|---|---|---|---|---|---|---|
| B10 | 佧 (idx 354) | A | A | PASS | A | — |
| B11 | 侉 (idx 416) | A | FAIL | FAIL | FAIL | — |
| B12 | 俎 (idx 482) | A | C | C | PASS | A |
| B13 | 俜 (idx 496) | A | FAIL | FAIL | FAIL | FAIL |
| B13 | 畟 (idx 510) | A | FAIL | C | FAIL | FAIL |
| B13 | 热 (idx 529) | A | FAIL | FAIL | C | FAIL |

All six occur at curriculum position 354 or later — the late-Phase-3 range where compositional complexity forces memory-equipped drawers to commit to specific decomposition strategies. The phenomenon suggests that on the subset of items where the "obvious" naive rendering is actually optimal, memory can act as a **constraint** that pulls the drawer away from it. On items where memory does not help, the memory-free control retains freedom to land the clean rendering.

We interpret this as evidence for two independent roads to A-quality: (i) structural-modulation-enabled rendering (G4's format), which produces A verdicts on items where the calligraphic modulation opportunity is discoverable through memory; (ii) cold-attempt compositional serendipity (G1's mode), which occasionally succeeds on items where memory-directed reasoning overshoots. The phenomenon is rare (~1% of items) but recurring, and worth citing as a cautionary note against uncritical "more memory = better" claims.

### 3.7 Retry mechanisms and self-evolution

All memory groups had access to a retry mechanism (up to 4 retries per item with cool-down) and, from v7 onward, permission to restructure their own memory files. Each group's curator invented substantially different memory organizations:

- **G2** ended with a TIER-0/1 markdown taxonomy indexed by stroke class and radical family, plus per-batch failure catalogs.
- **G3** ended with ~250 callable primitives split by signature class (stroke-endpoint vs. radical-position), a form_catalog indexed by stroke-class × context, and a hierarchy of principle-bank files (P-RET, P-DEV, P-MMH principles).
- **G4** ended with a grid-anchor + joint-typed bank of ~200 chronic primitives plus an A-recipe evolved to 8 explicit points.
- **G5** independently converged on 177 primitives in the same code-bank format as G3 and developed 10 A-recipe principles (P-A-001 through P-A-010) codifying when to reuse bank primitives, when to inline fresh, and when to freeze retry candidates.

Retry recovery rates varied by batch and group in the 12-38% range, with G5's B12 P-A-010 taxonomy achieving 60% recovery on a targeted 5-item queue — the highest we recorded — validating that curator diagnosis quality matters more than retry-mechanism sophistication.

The v13 BANK_DEVIATION channel produced measurable memory growth: G3 promoted 7 evidence-driven bank variants across the last three batches; G4 codified 8 grid patterns as named entries; G5 grew its bank from empty to 177 primitives in 14 batches, each addition traceable to a specific PASSed attempt.

---

## 4. Discussion

### 4.1 What this says about memory for iterative AI improvement

The dominant empirical finding — memory format alone lifts pass rate ~3-4 pts over control, while structural data injection lifts it 24 pts and unlocks quality-tier verdicts — is inconvenient for the framing that motivated the experiment. If the AI-for-science story is "memory + iteration converges to good solutions," our data suggests **the memory + iteration piece produces small, sub-linear gains**, and the load-bearing intervention is a **structural prior** grounded in some external source of truth.

For an AI-for-science practitioner, the operational reading is:

- Investing in memory-format sophistication (which type of database, which retrieval strategy, which curator prompt) has a small ceiling if the task has no grounded prior available.
- Investing in **grounded prior scaffolding** — bringing an external verifiable data source into the prompt at inference time — dominates. On our task this was MMH's stroke skeletons; in other domains it might be a physics simulator, a proof assistant, an experimental oracle.
- Format still matters, but for a different reason than commonly claimed: **format determines what quality ceiling the drawer can express**, not what baseline correctness it can achieve. G4's per-endpoint-width primitive enables calligraphic modulation; G3's uniform-width line cannot. The equivalent choice in another domain would be primitives that can express the discipline-appropriate quality distinction.

### 4.2 Memory can be a constraint

The G1 solo-A phenomenon (§3.6) is small in absolute count but conceptually important: on the ~1% of items where naive rendering is optimal, having any memory measurably hurts. This is consistent with the general observation that scaffolding narrows the search space — usually beneficial, occasionally not. For AI-for-science this suggests that a memory-equipped agent should retain the ability to *ignore* memory when the memory-directed path looks worse than a naive attempt. In practice this would require a per-item confidence estimate, which we did not evaluate here.

### 4.3 The rendering-format / correctness tradeoff

The G4 vs G5 comparison (§3.4) reveals a tradeoff that is unlikely to be specific to our task: **richer rendering primitives raise the quality ceiling but slightly lower the correctness baseline**. G4's fat_line-with-per-endpoint-widths gives drawers more degrees of freedom, which they exploit for A-quality calligraphy but occasionally misuse and produce a wrong-shape output. G5's uniform-width lines constrain the drawer to a simpler output space with less room for both A-quality and for creative error.

For an analogous AI-for-science task, this suggests a tension between primitive expressiveness and reliability that a system designer should test empirically rather than resolve a priori.

### 4.4 The confound we caught, and why we report it

Section 2.5's v14 intervention (attempted MMH removal from G4, rolled back same day, replaced by G5 pivot) is unusual for a paper's methods section. We include it because:

- The confound was real and load-bearing — without correction, our G4-vs-others comparison would have been uninterpretable as a memory-format test, because G4 was receiving a structural prior the other groups were not.
- The correction was structurally impossible to run cleanly in G4 itself (removing MMH mid-experiment would split G4's cumulative trajectory across two configurations and prevent within-group comparison). The G5 pivot is the cleaner alternative.
- Documenting the confound and its resolution is more informative than presenting the corrected result as if it had always been the design.

We recommend future work in this vein perform an early **data-flow audit** of what exactly reaches each experimental condition, before results accumulate.

### 4.5 Limitations

**Single model, single task.** All drawer subagents and curator agents used the same underlying frontier model. The findings should not be extrapolated to other model families without replication.

**Single judge.** The A/PASS/C/FAIL rubric was applied by a single human. Inter-rater reliability was not measured. The A tier especially may be sensitive to judge calibration; we note that A rates differ substantially across groups even under a single judge, suggesting the effect is real, but a formal panel study would strengthen the claim.

**Curriculum sequencing.** Items are ordered by ascending stroke count, so difficulty and position are confounded. We cannot separate "later in training" from "harder items" cleanly.

**Interventions.** Fourteen human interventions across the experiment, each of which perturbs the memory landscape. We logged each one, but a clean version of this experiment would fix all rules a priori. The v14 rollback in particular illustrates that a research team learning about its own experiment mid-run is unavoidable in this kind of exploratory setup.

**Rendering format is task-coupled.** The A-quality dimension we measure (calligraphic modulation) is specific to visual generation. Whether "quality vs. correctness tradeoff" generalizes to non-visual AI-for-science tasks is an empirical question.

### 4.6 Comparison to prior work

*(Placeholder — to be written after literature scan of memory-augmented LLM iteration, particularly Voyager, Reflexion, and related agentic-memory papers.)*

---

## 5. Conclusions

Across 668 items and five memory conditions, we find that **the dominant lever for iterative AI improvement on our compositional visual-generation task is structural prior injection, not memory format sophistication**. Memory-format richness alone lifted pass rate 3-4 points above a memoryless control; adding a structured stroke-skeleton prior lifted pass rate 24 points and unlocked a quality-verdict tier that memory alone could not reach. Rendering-format expressiveness (per-endpoint stroke width) provided an additional 5-point lift on the quality dimension but slightly reduced baseline correctness — a tradeoff that appears intrinsic rather than resolvable through better memory.

For the AI-for-science research agenda that motivated this study, the operational implication is that **memory should be a downstream investment**: prioritize identifying and injecting a domain's grounded structural priors first; then choose a memory format that expresses the discipline-appropriate quality distinctions; treat memory sophistication itself as a modest additional gain rather than the primary lever.

An open direction is whether the correctness/quality tradeoff we observe in rendering format has a general analog in AI-for-science tasks (e.g., proof-assistant primitives vs. natural-language mathematical reasoning; molecule-editor primitives vs. SMILES-string manipulation). Our data is consistent with such a tradeoff being real, but establishing it requires the same factorial ablation in a second domain.

---

## Data availability

All batch judgments (`judgments/batch_*/labels.json`), per-group memory files (`groups/G*/*.md`, `groups/G*/success_bank/`), and the ~3300 attempt PNGs are in the repository. Interventions log at `INTERVENTIONS.md`. Cross-batch observations at `OBSERVATIONS.md`.

## Acknowledgments

*(placeholder)*

## References

*(placeholder — literature review to be added)*

---

## Appendix A. Per-group memory-file structures at end of B13

*(to be filled in from each group's final `memory_index.md`)*

## Appendix B. Full list of terminal-freeze items per group

*(to be filled in from each group's `retry_log.jsonl`)*

## Appendix C. G1 solo-A verdict PNGs for figure-panel construction

- B10 `p3_char_0354_佧`
- B11 `p3_char_0416_侉`
- B12 `p3_char_0482_俎`
- B13 `p3_char_0496_俜`, `p3_char_0510_畟`, `p3_char_0529_热`

Each PNG file at `groups/G1_no_memory/attempts/<id>/01_<char>.png`.
