# export/ — Data package for PALM workshop @ NeurIPS 2026 submission

Prepared 2026-08-15 for handoff to the paper draft. Everything below unblocks paired statistics and final figures for `../REPORT_DRAFT.md`.

**Deadline reference**: PALM workshop @ NeurIPS 2026, Aug 24 AoE.

---

## P0 — statistics unblockers (needed by Aug 17)

### `item_grades.csv`
One row per (group × item × attempt) across every batch bootstrap → B13, including all G5 catch-up batches. 3948 rows total. Columns:
`group, batch, item_id, char, curriculum_idx, strokes, tier, phase, attempt_no, is_retry, verdict, verdict_scheme, judged_at, first_attempt_verdict, final_verdict`.

`first_attempt_verdict` and `final_verdict` repeat per (group × item_base) so both counting rules can be analyzed downstream without re-aggregation.

Pilot batches `001_pilot` and `002` are included for provenance but should be filtered out for paper tables (`batch NOT IN ('001_pilot','002')`). See `COUNTING_RULE.md` R5.

### `COUNTING_RULE.md`
Six rules (R1-R6) specifying exactly how REPORT_DRAFT §3.1 / §3.3 tables were computed: first-attempt-only counting, C-as-failure, verdict-scheme evolution across batches, G5 pre-B8 A-verdict exclusion, pilot-batch exclusion, retry-credit handling. Includes a reproduction snippet for Table 3.

### `runs_metadata.json`
Per-batch metadata: `judged_earliest` / `judged_latest` timestamp per (group, batch), total attempt count, drawer harness notes. Includes explicit **model-drift disclosure**: the G5 catch-up window (2026-08-08 through 2026-08-13) is entirely after the G1-G4 main-experiment window (2026-07-12 through 2026-08-03), so any model capability shift in the interim is systematically attributed to G5's numbers.

### `../judgments/` (in-repo, already pushed)
Every batch's `labels.json` + `manifest.json` at `experiments/exp_context_effect/judgments/batch_<name>/`. 31 batches total: main experiment (bootstrap, B1-B13, B7r) + G5 catch-up (G5_bootstrap, G5_B1..B13). Also `001_pilot` and `002` (excluded from paper tables — see COUNTING_RULE R5).

---

## P1 — figure assets (needed by Aug 18)

### `panels/solo_A/`
Six G1 solo-A items catalogued: 佧 (idx 354), 侉 (416), 俎 (482), 俜 (496), 畟 (510), 热 (529). For each: the GT PNG + all five groups' attempt PNGs, with verdict in the filename. 36 files total.

Filename convention: `<idx>_<char>__GT.png` and `<idx>_<char>__<G>_<verdict>.png`. Ready to paste into a 6×6 panel figure for §3.6 of the paper.

### `panels/representative/`
Two mid-curriculum items showing typical cross-group patterns:
- **`0162_生__MMH_lift__*`**: G4 + G5 PASS (both have MMH); G1 + G2 + G3 FAIL (no MMH). Illustrates MMH-effect visually.
- **`0206_白__all_pass__*`**: all five groups PASS. Illustrates the "everyone can render this" easy end of the distribution.

### `panels/format_pair/`
**果 (idx 387)** — both G4 and G5 rendered this as A. Includes both PNGs + both `generated.py` files + the GT. Purpose: show the visible per-endpoint-width signature of G4's `fat_line` primitive vs G5's uniform-width PIL line, and the code that produced each.

### `memory_growth.csv`
Per-group per-batch memory metrics. G5 has full trajectory (bank grew 19 → 177 primitives across 14 batches). G1-G4 report final state only — no historical bank size logging was archived per batch during the earlier run.

**Caveat**: G1-G4 rows report `B13_final` state only. Per-batch bank sizes for G1-G4 would require git-history spelunking; ask if that's needed for the paper.

---

## P2 — methods + appendix (needed by Aug 19)

### `INTERVENTIONS.md` and `OBSERVATIONS.md`
Copies of the two documents referenced in REPORT_DRAFT. `INTERVENTIONS.md` catalogs the 14 human interventions (v1-v14) with rationale. `OBSERVATIONS.md` documents Obs-01 (G1 solo-A phenomenon).

### `memory_final/G*/`
Per group: the final `memory_index.md` + a `tree.txt` listing all memory files (excluding attempt PNGs and per-item generated.py files). Ranges from G1 (5 files, no memory) to G3 (264 files including 250+ bank primitives).

### `prompts/`
- `protocol/` — the full protocol directory (`shared_rules.md` + per-group `rules.md`).
- `dispatcher.py`, `print_drawer_prompt.py`, `mmh_joints.py`, `judge_blind.py` — the actual code that builds prompts and runs judgment. Current post-v13 state.
- `sample_prompt_<G>_p3_char_0387_果.txt` — a fully-rendered drawer prompt for the character 果 (idx 387) per group. Includes the MMH structural block for G4 and G5.

### `retry_summary.csv`
Per (group, batch) retry stats: `retries_executed, recovered_PASS, recovered_A, recovered_C, recovery_rate_pct`. This is the basis for the 12-38% and 60% recovery-rate claims in REPORT_DRAFT §3.7. 45 rows.

### `ANSWERS.md`
Five short answers to the naming-drift / item-identity / license / re-grade questions: G3_coords ≡ "code bank"; PIL not turtle; item-identical curriculum with temporal caveats; 9 non-calibrated G5 A verdicts excluded from B9+ stats; **MakeMeAHanzi license unresolved in-repo — do NOT push raw graphics.txt without a license review**; no judge re-grades.

---

## P3 — nice to have (optional)

### `optional/curator_satisfaction_summary.csv`
Per (group, batch) STOP/KEEP-GOING counts from `curator_satisfaction_log.jsonl` files.

### `optional/TOKEN_COST_NOTE.md`
Aggregate token-usage estimate (~112M subagent tokens total; approximately USD $2-3K at API prices). Per-attempt breakdown was not archived — acknowledged as a limitation.

---

## What you (the corresponding author) need to do

1. **Legal review of the MakeMeAHanzi license situation before submission.** See ANSWERS.md item (d). Concrete action items:
   - Do NOT include `draw_character/graphics.txt` in the reproduction package.
   - Download the upstream MakeMeAHanzi LICENSE + Arphic Public License texts and commit as `MakeMeAHanzi_LICENSE.txt`.
   - Cite MakeMeAHanzi with a specific commit hash (pinned when we snapshot).

2. **Paper-side naming audit** on REPORT_DRAFT.md per ANSWERS.md summary bullet 3: replace any lingering "turtle" reference with "PIL"; confirm "code bank" everywhere (not "coord bank").

3. **Verify Tables 1-4 in REPORT_DRAFT.md** reproduce from `item_grades.csv` under `COUNTING_RULE.md` R1-R5. If any table disagrees, that's a bug — flag it before it goes to a reviewer.

4. **Pick figure captions** for the solo-A panel (§3.6), the MMH-lift representative panel, and the G4-vs-G5 format-pair panel. The panel PNGs are ready in `panels/`; captions are yours.

5. **Add limitations text** per ANSWERS.md summary bullet 3 (partial-unblinding disclosure for G5).

6. If per-batch bank-size data for G1-G4 is needed for a growth curve figure, ask — I can reconstruct from git history.

---

## Provenance

Prepared by Claude Code from repository state at commit 6b761109 on branch `feature/rapidocr-judge`. Every file in this export is derived from data already committed to the repository; no new judgments were run to produce this package.
