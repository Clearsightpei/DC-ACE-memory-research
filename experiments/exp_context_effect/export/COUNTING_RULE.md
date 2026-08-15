# Counting rules used in REPORT_DRAFT.md tables

This document specifies **exactly which counting rule** produced the summary tables in the paper draft. Ambiguity here would poison every downstream statistic, so we list each rule with a worked reference.

---

## Rule R1 — first-attempt verdict, no retry credit

**Applied to all tables in REPORT_DRAFT.md §3 (Tables 1, 2, 3, 4) and to all cross-group comparisons.**

For each (group × item), we count only the **first-attempt (retry_n = 0) verdict** in the earliest batch where the group encountered that item. Retry results are logged separately in `retry_summary.csv` and are NOT folded into the paper's per-batch tables. Rationale: (a) retry channel counts confound "how good is the drawer + memory at first pass" with "how well do the curator's retry hints route back into a rescue attempt"; (b) retry sample sizes are small and vary per group; (c) the fair-comparison window (B9+) is largely dominated by first-attempt attempts.

Concretely, in `item_grades.csv`:
- **Table 1 "Success rate (A+PASS)"** = count(rows where verdict ∈ {A, PASS} AND attempt_no = 1) / count(rows where attempt_no = 1) per (group, batch).
- **Table 2 "A count per batch"** = count(rows where verdict = A AND attempt_no = 1) per (group, batch), restricted to batches B9-B13.
- **Table 3 "Cumulative"** = sum across all main-experiment batches (bootstrap → B13) of attempt_no=1 rows per group.
- **Table 4 "A rate B9+"** = same as Table 3 but batches restricted to B9-B13 (250 items per group).

To reproduce Table 3 for G4:
```python
import csv
rows = list(csv.DictReader(open("item_grades.csv")))
g4 = [r for r in rows if r["group"]=="G4" and r["attempt_no"]=="1"
      and r["batch"] not in ("001_pilot","002","G5_bootstrap","G5_B1","G5_B2","G5_B3","G5_B4","G5_B5","G5_B6","G5_B7","G5_B8","G5_B9","G5_B10","G5_B11","G5_B12","G5_B13")]
# Filter to bootstrap + B1..B13
from collections import Counter
c = Counter(r["verdict"] for r in g4)
# → A=51, PASS=281, C=41, FAIL=295 (Table 3 row for G4)
```

---

## Rule R2 — verdict scheme evolution across batches

The A / C verdicts were introduced at batch **B9** via the v12 intervention (see INTERVENTIONS.md). Prior batches (bootstrap through B8, plus the two earliest pilot batches) use a **binary PASS / FAIL rubric**. Consequences:

- **Table 1** (success = A+PASS) treats pre-B9 batches as if they had zero A verdicts (which is correct — A wasn't available as a verdict) and includes their PASS + FAIL counts unchanged.
- **Table 2 and Table 4** (A-rate analysis) **restrict to B9-B13 only**, because pre-B9 batches cannot produce A verdicts by definition. Cross-group A-rate comparison would be unfair otherwise.
- **Table 3** (cumulative) includes all batches. A count is the true count (mostly zero for early batches), success rate is A+PASS.

In `item_grades.csv`, the `verdict_scheme` column marks each row: `4tier` if the specific verdict is A or C (implies the batch used the 4-tier rubric); `binary_or_4tier` otherwise (batch could be either — check batch label; bootstrap through B8 = binary).

---

## Rule R3 — C-verdict counting

C verdicts are **counted as failures** for the success-rate metric (i.e., only A and PASS count as success). Rationale: C is defined as "close but incorrect," which is not usable output. The C count is preserved in Table 3 and in the raw CSV for downstream near-miss / retry-candidate analyses, but does not roll up into success.

---

## Rule R4 — G5 pre-B8 A-verdict exclusion

The G5 catch-up group was scored under the same A/PASS/C/FAIL rubric from its bootstrap batch onward. However, in G5's early catch-up batches (bootstrap through B7), the judge applied A verdicts more loosely as **"memory-benefit signal"** tags — flagging renders that were particularly good so that G5's downstream curators would have exemplars to promote to the bank, rather than as fully-calibrated fair-comparison A verdicts.

For paper Table 4 ("A rate B9+ only"), G5's A count is taken from B9-B13 only (5 batches × 50 items = 250 items). Pre-B8 G5 A verdicts (bootstrap through B7 = 9 A verdicts) are recorded in `item_grades.csv` for provenance but **excluded from A-rate statistics**. Their inclusion in Table 3's cumulative row is done for structural symmetry with G1-G4 (whose cumulative includes all batches), but the A rate in Table 3 for G5 (7.0%) is diluted by this and should not be compared to G4's 7.6% directly — the fair comparison is Table 4 (G5 15.2% vs G4 20.4% on B9-B13).

---

## Rule R5 — Pilot-batch exclusion

The two earliest pilot batches, **`batch_001_pilot`** and **`batch_002`**, are **excluded from all paper tables**. They ran under an earlier experimental protocol (before the v3 scaffold, pre-Phase-3 structure) and their labels are not aligned with the 668-item main curriculum used in the paper. They are retained in `item_grades.csv` and in the `judgments/` tree for full data provenance, and can be filtered out via `batch NOT IN ("001_pilot", "002")` for any paper-comparable computation.

Rationale for retention in the raw export: the paper's methods section references the pilot phase indirectly (as "an earlier configuration that surfaced curriculum ordering choices"), and any reviewer wanting to audit the choice deserves to see the pilot data.

---

## Rule R6 — retry credit (excluded from paper tables, retained in raw CSV)

Rows with `attempt_no > 1` in `item_grades.csv` correspond to retry attempts. The paper does not fold these into per-batch counts. The `retry_summary.csv` file provides per-group per-batch retry recovery rates (retries → PASS or A) for the paper's §3.7 retry-mechanism discussion. The columns `first_attempt_verdict` and `final_verdict` in `item_grades.csv` allow post-hoc analysis under either counting rule.

---

## Reproducibility summary

Every claim in REPORT_DRAFT.md §3 can be reproduced from `item_grades.csv` under the rules above. `runs_metadata.json` provides model + timestamp provenance for each batch. `INTERVENTIONS.md` provides the chronology of protocol changes (v7 through v14). Should anything not reproduce, the discrepancy is a bug worth reporting.
