# run_4 POSTMORTEM — The Curator/Teacher Lenience Problem

**Frozen at:** cycle 24 (24 cycles, ~20 entries in Success Bank).
**Stated thesis:** three-bank memory (Success Bank + Principle Bank +
Sandbox) + skeleton-then-brushwork two-phase, with hard Drawer
isolation (no GT access), would yield characters that look more like
the target than run_3.

## What the run actually showed

The two-phase architecture worked for **stroke primitives** and the
first ~8 characters (一 二 三 十 八 — visual_score 0.42–0.85, OCR
consistent, rubric ≥ 7). The mastery gate
(`is_correct AND ocr_conf ≥ 0.4 AND rubric ≥ 7 no 0`) was a real
filter for those.

It stopped being a real filter starting at the 人/入 family. The
Drawer, with no GT to look at, had to *compute* compositions from
text prescriptions alone — and the Teacher (me) and Curator (also
me) progressively lowered the standard to keep the run moving:

- **c20 入** promoted at `visual_score 0.58`. The render is a sliver
  shape; OCR landed on 入 but a human eye reads "ambiguous slash."
- **c23 力** promoted at `visual_score 0.39`. The 横折钩 is
  disconnected from the 撇; OCR landed on 力 because RapidOCR's
  character set is small and it's the nearest token, not because the
  glyph reads as 力.

Both are **false positives**: OCR-passes that the Curator (vision)
should have rejected as not-unambiguously-the-target-character.
They entered the Success Bank, polluted later compositions (万 in
c24 OCR'd as 方 because the 力-shaped subcomponent it inherited was
already off), and inflated the bank size from ~17 real entries to 20
nominal entries.

## Why the gate failed

Three causes, in order of weight:

1. **OCR ≠ visual identity.** RapidOCR returning the correct token
   was treated as evidence of visual correctness. It is not. RapidOCR
   has a ~7k-character vocabulary; many low-stroke characters have
   no near-neighbors in that vocabulary, so the OCR head will return
   the nominal char even on a render that a human sees as a blob.

2. **Text-prescription ceiling.** With the Drawer fully blind to the
   GT, the upper bound on render quality is set by how precisely the
   Teacher can prescribe geometry in natural language. For 1–4-stroke
   characters that's fine; for compositions with subtle
   distinguishing features (人 vs 入, 力 vs 刀, 万 vs 方) it isn't —
   the Drawer literally cannot tell whether its output is one
   character or its neighbor, because it never sees either.

3. **Same-Claude Teacher and Curator with momentum.** The same
   conversation produced the brief, judged the result, and decided
   mastery. Once 入 was promoted at 0.58, the implicit precedent
   ("0.58 is fine") relaxed all subsequent judgments. The "100%
   confident" criterion was nominally there but operationally became
   "OCR passed and the render is in the right ballpark."

## What this run rules out

The hypothesis "text prescription + Curator-mediated vision check is
sufficient" is not supported. The hard-isolation Drawer cannot self-
correct on compositions where the failure mode is visible only in
the image, and a Curator who has to repeatedly judge "close to
target" cannot maintain a strict bar across 20+ cycles.

## What run_5 changes (the next experiment)

- **Drawer sees the GT.** `ground_truths/` is no longer quarantined.
  The Drawer's first action on each task is to look at the GT PNG
  with vision and treat it as the goal to mimic. `tools/` stays
  quarantined (the parameter-leak concern from run_2 is unchanged).
- **Teacher returns to its original light role.** Pick tasks, fetch
  characters from `graphics.txt` (not limited to the small
  pre-seeded list), and generate GT PNGs via the
  `draw_character.ipynb` logic (already vendored as
  `tools/make_char_gt.py`). No prescriptive geometry in the brief.
- **3 characters per cycle**, restoring run_3's pacing.
- **Curator's promotion test is strict-vision.** Open the attempt
  PNG and the GT PNG together in Claude vision and answer: *is this
  unambiguously the target character?* If not 100% confident, no
  promotion, and the Teacher cannot skip to a new focus next cycle.
  OCR is logged but not a sufficient signal.

The shift is deliberate: run_4 traded cheating-prevention against
self-correction and found the latter dominates for hard cases.
run_5 swaps the trade.
