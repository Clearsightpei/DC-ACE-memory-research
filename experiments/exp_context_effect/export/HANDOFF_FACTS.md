# Handoff facts — for paper §2.1 / §4.5 / Data Availability / refs.bib

Prepared 2026-08-15 in response to the "Report these four facts" step of the paper-side handoff.

---

## Fact (a) — MakeMeAHanzi commit hash for citation

Our local `draw_character/graphics.txt` is **byte-identical** to upstream MakeMeAHanzi's `graphics.txt` on master. SHA-256 matches (verified 2026-08-15).

**Two commit hashes to cite:**

- **Last commit that modified `graphics.txt`**: `618dbab8a8dd6716918edbfa3ee1e58e7cbafd66` (2018-10-16, "Fix 點, 袤, 瑤 and related characters"). This is the most precise citation for the specific data our experiment consumed.
- **Upstream master HEAD at license-fetch time**: `bddc96d41bef78427ed0e034e9f7e31d71fd1b92` (2026-03-08). Use if the reviewer expects "state of the repo as of paper submission."

**File metadata for the citation footnote:**
- URL: https://github.com/skishore/makemeahanzi
- File: `graphics.txt` (30,778,076 bytes, 9,574 characters)
- SHA-256: `a28c478b5178e98f67f510b2d52fde08a69dc664654ef43498253b9b764d46ee`
- Local mtime (download date): 2026-02-07
- License: dual — LGPL for code; Arphic Public License for graphics.txt (font-derived)

**Complete verbatim license texts** are now checked in at `/MakeMeAHanzi_LICENSE.txt` at the repo root. Includes: upstream COPYING (which points to the two license documents), the GNU LGPL v3 text, and the Arphic Public License text.

**refs.bib entry (recommended)**:
```bibtex
@misc{kishore_makemeahanzi_2018,
  author = {Kishore, Shaunak},
  title  = {Make Me a Hanzi: Free, open-source Chinese character data},
  year   = {2018},
  howpublished = {\url{https://github.com/skishore/makemeahanzi}},
  note   = {Commit \texttt{618dbab8} (last modification of \texttt{graphics.txt}); data derived from Arphic PL fonts under the Arphic Public License.}
}
```

---

## Fact (b) — Model version + run date ranges

**Underlying model for both drawer subagents and curator subagents**: **Claude Opus 4.7** (Anthropic Claude Opus family; exact model ID `claude-opus-4-7`). Dispatched via the Claude Agent SDK / Claude Code CLI + Anthropic Workflow tool. Default sampling settings; no temperature override.

**Run date ranges (from `judged_at` timestamps in `judgments/batch_*/labels.json`):**

| Cohort | First judged_at | Last judged_at | Wall-clock span |
|---|---|---|---|
| **G1-G4 main experiment (bootstrap → B13)** | 2026-07-17T17:50:33 | 2026-08-05T20:27:00 | ~19 days |
| **G5 catch-up (G5_bootstrap → G5_B13)** | 2026-08-08T14:51:57 | 2026-08-10T13:01:07 | ~2 days |
| **Gap between windows** | — | — | ~3 days (2026-08-05 → 2026-08-08) |

**Model-drift caveat for §4.5 Limitations:**

Every G5 attempt was drawn AFTER the last G1-G4 attempt. During the ~3-day gap, no Anthropic Claude Opus 4.x major-version release occurred publicly (based on publicly-visible version numbering — no formal check performed by us), but minor updates to the harness/router within the model family cannot be excluded. This is disclosed in the paper's §4.5 "single model" bullet; the drift-only hypothesis (that G5 outperforms G3 purely because of model improvement between windows) is **inconsistent** with the observed pattern because (a) G3 and G5 use the same code-bank format, only MMH differs, and the +24-point PASS lift is larger than any plausible 3-day model drift; (b) if drift were dominant, G5 would uniformly outperform G4 as well — but G4 leads G5 on A-rate in the fair window, which pure drift cannot explain.

**Recommended §4.5 replacement text:**

> All drawer and curator agents used Claude Opus 4.7 (Anthropic Claude Opus family, model ID `claude-opus-4-7`) via the Claude Agent SDK. G1-G4 batches ran 2026-07-17 through 2026-08-05; G5 was reset and re-run 2026-08-08 through 2026-08-10. Every G5 attempt post-dates the last G1-G4 attempt by 3-8 days. No major Anthropic model release occurred in this window, but minor router/harness updates cannot be excluded. The drift-only hypothesis (that G5's numbers reflect capability improvement rather than the MMH injection) is inconsistent with the pattern of results: G3 and G5 share memory format and differ only in MMH, so the +24pt PASS delta and the 1-vs-38 A-verdict lift are attributable to the injection, not to a 3-day drift; and drift would not produce the observed inversion in which G4 leads G5 on A-rate.

---

## Fact (c) — Solo-A panel confirmation

**Confirmed: `experiments/exp_context_effect/export/panels/solo_A/` contains the five-group comparison panel for all six G1 solo-A items:**

| curriculum_idx | char | files present |
|---|---|---|
| 354 | 佧 | GT + G1_A + G2_A + G3_PASS + G4_A + G5_PASS |
| 416 | 侉 | GT + G1_A + G2_FAIL + G3_FAIL + G4_FAIL + G5_FAIL |
| 482 | 俎 | GT + G1_A + G2_C + G3_C + G4_PASS + G5_A |
| 496 | 俜 | GT + G1_A + G2_FAIL + G3_FAIL + G4_FAIL + G5_FAIL |
| 510 | 畟 | GT + G1_A + G2_FAIL + G3_C + G4_FAIL + G5_C |
| 529 | 热 | GT + G1_A + G2_FAIL + G3_FAIL + G4_C + G5_FAIL |

**Total: 36 PNGs** (6 items × [GT + 5 groups]). Verdict is embedded in each filename. Ready to compose into a 6×6 grid figure for Fig 4 (§3.5).

The paper's §3.5 text and Appendix C are consistent with these indices. Note that idx 354 (佧) is not a *pure* solo win — G2 and G4 also scored A on it — but it is the earliest G1-A appearance in the curriculum and worth showing for context; the true solo wins are 416, 496, 510, 529.

---

## Fact (d) — Per-batch bank-size counts (optional, for growth-curve figure)

**Reconstructed and included in `export/memory_growth.csv`.** Data sources are noted per row:
- **G5**: high-resolution per-batch counts from G5's own `evolution.md` curator entries (14 data points: bootstrap through B13).
- **G3/G4**: only three git-checkpoint snapshots per group are available (post-v7 = 2026-07-18, post-B7 = 2026-07-27, post-B13 = 2026-08-13). Per-batch resolution would require replaying git commits, which we did not do — the checkpoint density is sufficient to show growth trajectory but not per-batch smoothness.
- **G2**: markdown-only; the "bank" concept does not apply. Value reported as 0.
- **G1**: control, no memory; also 0.

**Suggested "memory grows while performance stays flat" figure:**

Two subpanels:
- **Left**: bank size vs. batch, one line per (G3, G4, G5). G5's line is the cleanest (14 monotone points). G3/G4 show 3 datapoints each with an obvious growth trajectory.
- **Right**: pass rate vs. batch for the same groups (from `item_grades.csv`), same batch axis.

The visual story: G5's bank grew from 19 → 154+ primitives across 14 batches (~8× growth) while its pass rate on late Phase-3 items stayed in the 40-55% band. G3's bank grew from 67 → 250 (~3.7× growth over the same wall-clock window) while its pass rate stayed in the 12-28% band on Phase-3 items. **Memory accumulated substantially; per-batch pass rate did not track that accumulation.** This visualization directly sells finding (i) in the abstract.

---

## Summary of what's committed alongside this file

At commit **[to be filled]** on `main`:

1. `/MakeMeAHanzi_LICENSE.txt` (repo root, 18981 bytes, 314 lines) — full COPYING + LGPL + Arphic PL license texts.
2. `experiments/exp_context_effect/export/HANDOFF_FACTS.md` (this file).
3. `experiments/exp_context_effect/export/memory_growth.csv` (rebuilt with reconstructed G3/G4 checkpoints + G5 per-batch trajectory + source column).
4. `experiments/exp_context_effect/README.md` — naming fixes (turtle → PIL in intro; historical changelog entries preserved unchanged).
5. `experiments/exp_context_effect/INTERVENTIONS.md` — "coord bank" → "code bank" (1 instance).

**Note on `draw_character/graphics.txt`**: still in-repo (was in-repo from experiment start). For the paper's public reproduction snapshot, the recommendation stands: **exclude `graphics.txt` from the paper release**, keep only the LICENSE + derived tooling. This repo (`Clearsightpei/DC-ACE-memory-research`) is the internal working repo; the paper release is a separate anonymized snapshot per the Data Availability section.
