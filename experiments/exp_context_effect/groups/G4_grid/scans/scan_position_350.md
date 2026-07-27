# Errata scan @ position 350 (post-B6, pre-B7) — v8 unlock

## Context

This is the FIRST scan under v8 (unlocked at position 350). B6 was
G4's worst batch: main 26/50 = 52%, retry 0/10 (with 6/16 STALL_DNC).
Diagnosis in `evolution.md` position-350 entry.

## Errata inventory (post-B6)

Active errata items with cool-downs eligible for B7 (positions 184-233):

### Under normal cool-down (50 items since last retry, retry_n<3)

None. All B6 retries were either STALL_DNC (didn't render) or FAILed;
the 6 STALL items have not consumed a real retry, but the drawer's
inability to complete them under v7 checklist load is itself evidence.
Under v8's slim checklist, retry them:

### v8 retry decisions for positions 184-233 (B7)

**Retry (canonical-promotion candidates — do FIRST, promote if fail again)**:
- **p2_radical_088_长** (retry_n=3, SATURATED) — action: promote to
  `chronic/chang_long.py` at position 400 if B7 attempt fails.
- **p2_radical_081_夂** (retry_n=3, SATURATED) — action: promote to
  `chronic/zhi_dive.py` at position 400 if B7 attempt fails.
- **p2_radical_084_夊** (retry_n=3, SATURATED) — action: promote to
  `chronic/sui_slow.py` at position 400 if B7 attempt fails.

**Retry under v8 drawer_memory.md discipline** (a: prospective use for
positions 184-233):
- **p2_radical_086_比** (retry_n=1, was STALLed / rendered wrong)
  — prereq for many left-right symmetric chars in B7 curriculum.
- **p2_radical_119_水** (retry_n=1) — prereq for 泳/永/氺/黎-family.
- **p2_radical_116_礻** (retry_n=1) — prereq for 视/礼/祈/福-family.
- **p2_radical_094_风** (retry_n=1) — high-frequency component.
- **p2_radical_124_文** (retry_n=2, canonical candidate if B7 fails)
  — prereq for 齐/交/亦-family.
- **p2_radical_135_无** (retry_n=2, was STALLed) — prereq for 抚-family.
- **p2_radical_111_气** (retry_n=2, was STALLed) — prereq for 汽/氧-family.

**Retry under v8 (b: retrospective — v8 unlock addresses their failure mode)**:
- **p2_radical_045_寸** (retry_n=1) — errata fix now literal in
  drawer_memory.md high-value shortlist.
- **p2_radical_075_夕** (retry_n=1) — same.

**Skip (no prereq and no v8-relevant learning)**:
- 003_丿, 015_刀, 024_冂, 050_弓, 058_马 — all SUPPLANTED at position
  300 to `chronic/`, retry mechanism retired. If drawer imports the
  chronic primitive in B7 for characters containing these radicals,
  we'll get de-facto retry PASSes as a side effect.
- 038_㔾, 047_飞, 053_己, 062_犭 (all retry_n≥2, low B7 prereq
  frequency) — leave in errata, no active retry this batch.
- 070_纟 (retry_n=3, was STALLed) — canonical candidate at position 400
  IF B7 exposes 纟-containing chars requiring it.
- 082_子 (retry_n=3, was STALLed) — same; 子 already has zi_char.py
  bank entry that mostly works, low urgency to promote to chronic.
- 093_方 (retry_n=3, was STALLed), 100_见 (retry_n=3, was STALLed) —
  chronic candidates at position 400.

## Overall B7 retry slate (12 items — moderate, not aggressive)

Per v6+ balance rule ("retry when you have a real (a) or (b) reason,
not minimalism, not maximalism"), retry 12 of the 20+ eligible items.
Chronic-cluster promotion decisions for pos 400 are the main pending
action.

## v8 unlock action items (this scan)

1. [DONE] Created `drawer_memory.md` (v8 free-form file).
2. [DONE] Slimmed `memory_index.md` mandatory checklist from 6 → 3
   files.
3. [DONE] Pruned 12 bank files (p3_char_bank.py, p3_char_bank_b5.py,
   10 thin wrappers) — see `evolution.md` position-350 entry.
4. [DONE] Appended B6 errata + INDEX rows + evolution log.
5. [DEFERRED to pos 400] Chronic canonical promotions for
   长/夂/夊/纟/方/见 (only if B7 fails again with slim-checklist).
6. [DEFERRED to B7] `fu_left.py` primitive for 阝-left (missing bank
   entry, B6 队 failure).

## Predictions to verify at position 400

- Chronic-primitive import rate ≥ 50% (was 0% pre-v8).
- Retry STALL_DNC rate < 20% (was 60% in B6).
- Main pass rate ≥ 55% (v7 floor).
