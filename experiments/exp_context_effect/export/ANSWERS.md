# ANSWERS.md — clarifications for the paper draft

These answer the questions posed in the data-export brief item 13. Each answer is a **statement of the current, authoritative truth** — if any prior document contradicts it, the prior document is stale.

---

## (a) Naming: is `G3_coords` the group the paper calls "code bank"?

**Yes.** `groups/G3_coords/` on disk = "G3 (callable-Python code bank, no MMH)" in `REPORT_DRAFT.md` and in every table in the paper draft. The directory name `G3_coords` is a legacy from an earlier phase when the format was thought of as a "coord bank"; the paper's terminology ("code bank" / "callable-Python primitives") is the final one. There is no separate directory for what the paper calls G3.

**Rendering primitive drift**: earlier repo documentation (e.g. the top-level README) refers to G3's drawers as using `turtle`. **The current authoritative truth is: G3 drawers use PIL almost exclusively**. Empirically, of 854 G3 generated.py files in the repo, 852 import `from PIL import Image, ImageDraw` and only 2 use `import turtle`. The paper's claim "code + PIL uniform line width" is correct; the README's "turtle" reference is a historical artifact from run_1's earlier orchestration and should not be trusted for the current experiment. Same for G5 — it inherited G3's protocol and uses PIL.

G4 uses a different substrate — PIL's `ImageDraw` polygon fills wrapped in a `fat_line(w1, w2)` helper that produces varying-width strokes, plus optional `quad_bezier` primitives. G4 is the only group whose primitives can produce per-endpoint width modulation (which is what enables A-quality calligraphy per §3.4 of the draft).

---

## (b) Did all five groups face the identical 668 items?

**Yes, item-identical.** All five groups (including G5's rerun) drew from the same curriculum: 135 Phase-2 radicals (indexed by MakeMeAHanzi radical list) + 533 Phase-3 characters (indexed 001-533 from `curriculum/chars_1000.json`, ordered by ascending stroke count within tier). Every batch's manifest dispatches the identical item IDs to every group in that batch.

**Two caveats**:
1. G1-G4 drew each item in the same wall-clock batch (e.g., G1's 佔 attempt and G4's 佔 attempt happen in the same B10 dispatch, timestamped within minutes of each other). G5's identical 佔 attempt happened weeks later in G5's catch-up B10. This is a temporal drift concern documented in `runs_metadata.json` `possible_model_drift_windows`.
2. Retries are per-group and thus per-group idiosyncratic — G4 might have retried 亥 four times while G5 retried it twice. Retry logs are per-group in each `retry_log.jsonl`. **Retry attempts are NOT counted in the paper's per-batch tables** — see COUNTING_RULE.md R1 and R6. First-attempt fair comparison is preserved because every group's first attempt at any item happened in that item's originally scheduled batch.

---

## (c) Which G5 early batches had non-calibrated A verdicts, and how many were excluded from A-rate statistics?

**Bootstrap through B7** for G5 had non-calibrated A verdicts — the judge issued A verdicts during those catch-up batches as **"memory-benefit signal"** flags (tagging renders that were particularly good so downstream G5 curators would have exemplars to promote to the bank), rather than as fully-calibrated fair-comparison A verdicts.

Count of non-calibrated G5 A verdicts to exclude from fair-comparison A-rate statistics:

| G5 batch | Non-calibrated A count | Item IDs |
|---|---|---|
| G5_bootstrap | 0 | — |
| G5_B1 | 0 | — |
| G5_B2 | 0 | — |
| G5_B3 | 4 | 爻, 了, 人, 又 |
| G5_B4 | 0 | — |
| G5_B5 | 0 | — |
| G5_B6 | 0 | — (义 was a retry A) |
| G5_B7 | 5 | 业, 仟, 仨, 冉, 乓 |
| **Total excluded** | **9** | |

**The paper's Table 4 ("A rate B9+") uses G5's B9-B13 A count of 38.** G5's cumulative Table 3 row includes all 47 A verdicts (including the 9 excluded) for structural symmetry with G1-G4, but its A rate in Table 3 (7.0%) should not be compared directly to G4's Table 3 A rate (7.6%) — see Table 4 for the fair comparison (G5 15.2% vs G4 20.4%).

---

## (d) MakeMeAHanzi version, commit, and license

**MakeMeAHanzi source information (best available):**

- Project: [makemeahanzi](https://github.com/skishore/makemeahanzi) by Shaunak Kishore.
- File used: `graphics.txt` (30,778,076 bytes, 9,574 characters).
- **Commit/version**: not recorded at time of ingestion. The file's mtime is 2026-02-07, which predates the experiment start (2026-07-12). No git submodule was configured; the file was placed into `draw_character/graphics.txt` as a static resource.
- **License situation is UNRESOLVED in-repo**: no `LICENSE` file exists for `graphics.txt` in this repository. Per upstream, MakeMeAHanzi's stroke-median data derives from the **Arphic PL Kai TTF font** (Arphic Public License lineage), and the project itself is dual-licensed: LGPL for code, Arphic PL for font-derived data.

**Action required before paper submission:**

1. **Do NOT push `draw_character/graphics.txt` to the paper's public GitHub snapshot.** The current repo has it in `draw_character/graphics.txt`; the paper release should exclude it via `.gitignore` or a filtered snapshot.
2. **Add an in-repo `MakeMeAHanzi_LICENSE.txt`** downloaded verbatim from the upstream project's LICENSE + ARPHIC PUBLIC LICENSE. Include a `MakeMeAHanzi_SOURCE.md` noting the specific upstream commit (to be pinned when we snapshot for submission).
3. **In the paper**: cite MakeMeAHanzi as the data source; note the Arphic PL derivation; state that our released reproduction package includes derived structural data (stroke endpoints + joint typology JSON extractable via `tools/mmh_joints.py`) but does **not redistribute** the upstream `graphics.txt` file itself — reproducers should install MakeMeAHanzi separately.
4. **What our code publishes**: `tools/mmh_joints.py` (a wrapper that reads `graphics.txt` and outputs per-character stroke count + endpoint anchors + joint classifications). This is a derivative work; releasing it under LGPL matches upstream. The output JSON per character (endpoint coords + joint typology, ~1 KB per character) is a further derivative but at a much higher abstraction than the raw font-glyph strokes; we believe releasing this is fine under Arphic PL fair use, but a legal review before publication is prudent.

**Bottom line: this needs a legal review pass before public release.** The safest defensible position is: do not redistribute `graphics.txt`; require reproducers to install MakeMeAHanzi separately; release only our derived tools + per-character output tables.

---

## (e) Judge re-grades

**No judge re-grades occurred.** Every attempt was labeled once. `judge_blind.py` produces `labels.json` files that are append-only in practice; there is no re-scoring pass. The single-judge, single-blind protocol is a known limitation acknowledged in REPORT_DRAFT.md §4.5.

**Two minor caveats that reviewers might raise:**

1. During the G5 catch-up window (2026-08-08 through 2026-08-13), the judge was aware that G5 was being compared to G4's earlier trajectory. This is not a re-grade of G4's attempts but does mean G5 was judged under partial awareness of the comparison target. Blinding per-attempt (group randomization within each item's shuffle) was preserved via `judge_blind.py` for every batch, but the judge inevitably had cumulative knowledge of which batch they were judging.
2. The A/C verdicts introduced at B9 (v12 intervention) were applied prospectively only. Pre-B9 batches were **not retroactively re-labeled** for A/C. This is why the paper's A-rate analysis restricts to B9+ (COUNTING_RULE.md R2).

---

## Summary of what to change in the paper before submission

1. **§2.4 (MMH prior)**: add a citation to MakeMeAHanzi and a footnote on the license situation.
2. **Reproduction package**: exclude `draw_character/graphics.txt`, add `MakeMeAHanzi_LICENSE.txt`, provide `tools/mmh_joints.py` + per-character output table (~530 KB total).
3. **§4.5 (Limitations)**: add "the G5 judge had non-blind cumulative knowledge of the G5-vs-G4 comparison target during G5's catch-up window" — currently implied but worth being explicit.
4. **REPORT_DRAFT.md line-by-line naming audit**: the group is always "code bank" (not "coord bank"); the primitive is always "PIL uniform-width line" (not turtle); "callable Python" is the accurate framing throughout.
