# Second-rater reliability record

A second rater, fluent in written Chinese, independently graded a frozen
random sample of first attempts, blind to condition, source path, the
original verdict, and the study's hypotheses.

## Files

| file | contents |
|---|---|
| `second_rater_labels.csv` | **the artifact most reproducers want** — one row per sampled item with both raters' verdicts |
| `SAMPLE_SPEC.json` | random seed, sampling rule, selection SHA-256 |
| `manifest.json` | the exact 150 items presented, repo-relative paths |
| `ANSWER_KEY.json` | token -> condition, item, original verdict |
| `labels_raw.json` | second rater's verdicts as written by the judging tool |
| `RUBRIC.md` | the four-tier rubric, identical to the one used in the main run |

## Sample

- Drawn with **seed 20261006** from the common four-tier window (B9-B13,
  curriculum positions 419-668; 250 items per condition).
- **150 items, 30 per condition, item-disjoint**: 150 distinct characters,
  so no character is shown twice and no rater can anchor on an earlier
  verdict for the same reference.
- Presentation order shuffled with the same seed.
- Selection SHA-256 `d40a3554f8b8fedc...` (full value in `SAMPLE_SPEC.json`).

## Analysis plan, fixed before judging

- **Primary**: Success (Perfect or Pass) vs Failure (Close or Fail) —
  raw agreement and Cohen's kappa.
- **Secondary**: four-tier agreement (unweighted, linear- and
  quadratic-weighted kappa); Perfect vs non-Perfect agreement.
- Disagreements are **not adjudicated**, and the original labels are
  unchanged. The study measures the instrument; it does not revise the
  measurements.

## Reproducing the numbers

    python3 tools/score_reliability.py --dir export/reliability

or directly from `second_rater_labels.csv` using the `rater1_verdict` and
`rater2_verdict` columns.

## Results

| measure | raw agreement | Cohen's kappa |
|---|---|---|
| Success vs Failure (primary) | 92.7% | 0.827 (95% CI 0.728-0.925) |
| Four tiers, unweighted | 71.3% | 0.554 |
| Four tiers, linear-weighted | — | 0.721 |
| Four tiers, quadratic-weighted | — | 0.846 |
| Perfect vs non-Perfect | 96.0% | 0.730 |

41 of 43 disagreements were a single adjacent tier; none spanned more than
two. 26 fell at the Fail/Close boundary, which no reported statistic
distinguishes. The second rater confirmed all nine original Perfect
verdicts and added six, all in structurally supervised conditions.

## A note on the images

`manifest.json` references `reliability_study/images/`, the blinded PNG copies
shown to the second rater. Those copies are not in the repository (they
duplicate files already under `groups/*/attempts/` and `gt/`). They are not
needed to recompute agreement — `second_rater_labels.csv` is sufficient.

To re-run the judging itself, regenerate the identical blinded sample from the
recorded seed:

    python3 tools/make_reliability_sample.py --seed 20261006

This reproduces the same 150 items in the same presentation order; verify
`selection_sha256` in the regenerated `SAMPLE_SPEC.json` matches the value
above. It requires `draw_character/graphics.txt` only if reference images need
rebuilding; otherwise `gt/phase3/` suffices.
