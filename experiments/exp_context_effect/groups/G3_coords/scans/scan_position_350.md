# Errata scan @ position 350 (B6 end / B7 start) — G3 curator

**Regime**: retry mechanism was killed at B5 curator (position 300); this
scan **re-enables it** under v8's format unlock. See `evolution.md`
2026-07-26 entry §6 for rationale (v8 signature freedom + free-form
`drawer_memory.md` + INTERVENTIONS' terminal-freeze lifts on 人/入/大
together invalidate B5's format-ceiling argument).

**Cooldown-50 rule**: no item may be retried within 50 curriculum items
of its last retry. All items below either have retry_n=0 (never retried
since B5-freeze-lift) or last retry was before position 300.

## Retry candidates for B7 (positions 351-400)

**Terminal-un-frozen (highest priority — one shot each per §v8)**:
- `p2_radical_028_人` — retry_n=4 → attempt retry_5 under v8. Signature
  freedom: drawer may write any function form for the two strokes to
  visually flow. Do NOT force kiss_apex — trust GT.
- `p2_radical_030_入` — retry_n=4 → attempt retry_5 under v8. Same.
- `p2_radical_046_大` — retry_n=4 → attempt retry_5 under v8. Same.

**(a) Prospective — prereqs for 351-400**:
- **匕 (radical, retry_n=3)** — needed for 化 (B6 FAIL) + upcoming 花/华.
  Fix idea: apply the sandbox p2_radical_011_匕 diagnosis (short 撇
  landing ON top of 竖弯钩 shaft, not crossing above).
- **也** — needed for 他 (B6 FAIL) + upcoming 池/驰/她. Not currently
  in bank; inline recipe per errata p3_char_0154_他.
- **子 char (already bank #122)** — 仔 FAILed in B6 by inventing a
  fresh right-side instead of using zi_char. Retry 仔 with zi_char
  at ox=+40, scale=0.65.

**(b) Retrospective — items addressable under v8 free-form**:
- `p3_char_0176_平` — B6 FAIL. Under drawer_memory.md new "dots ABOVE
  heng, not descending" guidance, this should PASS.
- `p3_char_0174_主` — B6 FAIL. Same proportion guidance.
- `p3_char_0171_疒` — B6 FAIL. Attempt was near-empty; explicit
  reminder to CALL `guang` primitive and add interior dots inside.
- `p2_radical_021_丷` — GRADUATED B5; check if 平's mirror-dots recipe
  transfers.

**Skip (format ceiling stays)**:
- `p1_stroke_16_斜钩`, `p1_stroke_19_横斜钩`, `p1_stroke_21_横折弯`,
  `p1_stroke_25_横折弯钩`, `p1_stroke_31_竖折折钩`,
  `p1_stroke_32_横折折折钩` — hook-family; v8 doesn't add hook
  expressiveness.
- `p2_radical_015_刀` (retry_n=3), `p2_radical_058_马` (retry_n=2 cursive
  ceiling), `p2_radical_042_巛`, `p2_radical_050_弓`, `p2_radical_053_己`
  — cursive/hook families.
- All B4/B5 chars in the cursive body cluster (马 char, 巛 char, 幺, 乡,
  为, 乌, 予, 长).

## Retry queue for B7 (in dispatch order)

1. p2_radical_028_人 (retry_5, un-freeze)
2. p2_radical_030_入 (retry_5, un-freeze)
3. p2_radical_046_大 (retry_5, un-freeze)
4. p2_radical_011_匕 (retry_4)
5. p3_char_0154_他 (retry_1)
6. p3_char_0173_仔 (retry_1)
7. p3_char_0176_平 (retry_1)
8. p3_char_0174_主 (retry_1)
9. p3_char_0171_疒 (retry_1)
10. p3_char_0134_化 (retry_1)

That's 10 retries. If dispatcher cap is lower, drop lowest priority
(化) first, then 疒, then 主.

## Measurement plan for B7 retry channel

- Grep retry `generated.py` files for `drawer_memory.md` citation in
  comments. Goal: ≥ 3 of 10 cite the new playbook.
- Retry PASS rate: goal ≥ 20% (was 5% cumulative under v7).
- If retry rate stays < 10%: retire mechanism again at B7 curator; the
  v8 unlock did not rescue it.
