# G1 (control / no-memory) — curator notes

## B10 (2026-07-31)

B10 success rate for G1 was 6/50 = 12% (1 A + 5 PASS). This is the first-ever A verdict for the control group across all batches — item `p3_char_0354_佧` cleared the strict bar despite G1 carrying no memory between attempts. The C count (7 near-misses: `p3_char_0335_别`, `p3_char_0340_佚`, `p3_char_0344_佝`, `p3_char_0357_花`, `p3_char_0362_甾`, `p3_char_0365_和`, `p3_char_0377_法`) is a useful signal: even without accumulated memory the drawer is landing in the near-miss band on ~14% of items, meaning the base model has non-trivial residual competence on these character shapes. FAIL remains dominant at 37/50 (74%), as expected for the memoryless control.

## B11 (2026-08-03)

B11 success rate for G1 was 6/50 = 12% (1 A + 5 PASS), unchanged from B10. The A verdict is the second-ever for the control group — item `p3_char_0416_侉` cleared the strict bar. The C count rose to 8 near-misses (`p3_char_0397_空`, `p3_char_0400_佶`, `p3_char_0413_采`, `p3_char_0414_侈`, `p3_char_0419_知`, `p3_char_0422_侍`, `p3_char_0424_侑`, `p3_char_0425_具`), a modest uptick from B10's 7. FAIL remains dominant at 36/50 (72%), consistent with the memoryless control's steady-state behavior across B10–B11.

## B12 (2026-08-04)

B12 success rate for G1 was 10/50 = 20% (1 A + 9 PASS), a notable jump from the 12% steady state observed on B10 and B11. The A verdict is the third-ever for the control group — item `p3_char_0482_俎` cleared the strict bar. The C count fell to 6 near-misses, and FAIL was 34/50 (68%). The uptick to 20% is worth flagging for cross-group comparison but requires no action here — the control carries no memory and is not adjusted between batches.

## B13 (2026-08-05)

B13 success rate for G1 was 6/50 = 12% (3 A + 3 PASS), returning to the B10/B11 baseline and reframing B12's 20% as the outlier. The headline event is an unprecedented 3-A spike for the control group — items `p3_char_0496_俜`, `p3_char_0510_畟`, and `p3_char_0529_热` all cleared the strict bar, constituting the 4th, 5th, and 6th cumulative G1 A verdicts on record. All three were solo-wins: every memory-equipped group (G2/G3/G4) FAILed or C'd on the same items, meaning the memoryless control uniquely succeeded where the accumulated memory systems did not. C count was 4 near-misses and FAIL was 40/50 (80%). See `experiments/exp_context_effect/OBSERVATIONS.md` Obs-01 for the cross-batch analysis of this 3-A spike phenomenon.
