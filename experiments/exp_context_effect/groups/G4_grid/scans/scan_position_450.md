# Scan @ position 450 — B8 curator retry queue for B9

**Batch summary**:
- B8 mains: 20 PASS / 30 FAIL (40%, down from B7's 50%).
- B8 retries (v10 prompt): 0 PASS / 7 FAIL.
- Chronic import rate (B8 mains): 0/50 imports; 19/50 comment mentions.
  0/3 imports on the 3 mains whose target contains a chronic component
  (再/同/西).
- Canonical import rate on 7 retries: 0/7 (target files do not exist —
  see position-450 delivery-failure note in `evolution.md`).

## The position-400 delivery failure — dispatch-level root cause

At position 400 the curator QUEUED 7 canonical primitives
(chang_long.py, zhi_dive.py, sui_slow.py, shui_water.py, shi_altar.py,
wu_none.py, qi_air.py) and marked the 7 retry items for B8 with
"drawer just calls them." **The primitive files were never actually
hand-written into `success_bank/code/chronic/`.** The 7 retry drawers
in B8 had no new file to import, fell back to v9 visual-diff +
MMH-verbatim + inline base primitives, and FAILed uniformly.

**Terminal-freeze verdict**: after 4 batches of escalation (v7
mandatory citation → v8 slim + import snippets → v9 visual-diff Step 0
→ v10 full-trajectory + queued canonical) plus this delivery failure,
marginal ROI of another attempt with the SAME memory state is near
zero. All 7 items marked **TERMINAL_FROZEN** and dropped from B9
retry queue.

---

## Retry queue for B9 (positions 451-500)

### Category A — TERMINAL_FROZEN (DROPPED, not retried)

| item_id | Char | retry_n | Reason |
|---------|------|---------|--------|
| p2_radical_088_长 | 长 | 4 | 4 batches saturated + canonical file not delivered |
| p2_radical_081_夂 | 夂 | 4 | same |
| p2_radical_084_夊 | 夊 | 4 | same |
| p2_radical_119_水 | 水 | 2 | canonical file not delivered; retry_n at cutoff |
| p2_radical_116_礻 | 礻 | 2 | canonical file not delivered; retry_n at cutoff |
| p2_radical_135_无 | 无 | 3 | canonical file not delivered |
| p2_radical_111_气 | 气 | 3 | canonical file not delivered |

Re-attempt is not blocked forever — a future curator who hand-writes
the 7 chronic primitive files and updates `drawer_memory.md`'s
mandatory-imports section can unfreeze these items. This batch
declines to do so because the mechanism itself (canonical `chronic/`)
has produced 0 imports across 3 batches for the 5 existing files, so
adding 7 more may not help.

### Category B — B8 main FAILs addressable under v10 trajectory-view

Items where the FAIL mode was a topology or coherence bug that a v10
trajectory-visible retry can plausibly fix. Cool-down 50 items;
executable at position 500 (in B9 batch).

| item_id | Char | Fix idea | Rationale |
|---------|------|----------|-----------|
| p3_char_0249_同 | 同 | MANDATORY `from chronic.jiong_frame import draw_jiong_frame` | chronic 冂 exists; B8 drawer mentioned but did not import |
| p3_char_0241_如 | 如 | Enforce column widths: 女 fills x∈[0.05,0.45], 口 fills x∈[0.50,0.95] | primitives OK, placement wrong |
| p3_char_0253_好 | 好 | import both `nv` and `zi` | left+right both have mastered primitives; drawer used none |
| p3_char_0263_她 | 她 | import `nv` + inline 也 with 3-stroke plan | reuse OK; right side needs 3-stroke correction |
| p3_char_0265_名 | 名 | import `kou`; hand 夕 = pie + heng-zhe-gou + dian | mastered primitive exists |
| p3_char_0270_伧 | 伧 | import `ren.py` + `bi.py` for right 仑 | both primitives mastered |
| p3_char_0274_伫 | 伫 | import `mian.py` for 宀 top + hand 亍 | roof primitive mastered |
| p3_char_0279_色 | 色 | MANDATORY `from chronic.dao_char import draw_dao_char` for 刀 top | chronic exists; not imported |
| p3_char_0237_行 | 行 | import `chi_step.py` for 彳 left | mastered primitive exists |
| p3_char_0283_传 | 传 | import `ren_side` + hand 专 as heng+heng+shu-zhe-hook+dian | ren_side mastered |

**Category B size**: 10 items.

### Category C — Prerequisites for the next 50 items (451-500)

Missing primitives that will likely be needed as B9 dispatches:
- **`fu_left.py`** (阝-left) — still missing since B6 队 FAIL.
  If B9 pulls 阻/陕/陋/陕/院 or similar, they will FAIL for lack.
  **Recommend Teacher: hand-write `fu_left.py` before B9 dispatch.**
- **`yan_side.py`** (讠) — B8 设 FAIL for lack. Common on P3.
  **Recommend Teacher: hand-write `yan_side.py` before B9.**
- **`zou_zhi.py`** (辶) — B8 过 FAIL for lack; also needed for
  近/远/追/送. **Recommend Teacher: hand-write `zou_zhi.py`.**

These are pure primitive promotions (not retries).

### Category D — Skip (no clear next fix)

Items with no obvious next mechanism under the current memory state.
Deferred to position 500.

- 亥 (X-cross-below topology; needs `CROSS_ANCHOR` snippet applied)
- 亦 (same X-cross topology)
- 成 (compound `xie_gou` + inner X-cross)
- 过 (blocked on `zou_zhi.py`)
- 军 (needs 车 primitive — not in bank)
- 伄 (needs 刁 primitive — not in bank)
- 伊 (ren_side default-anchor rejection — real primitive-API issue)
- 伎 (needs 又 in 支 — `you_again` exists but composition tricky)
- 伕 (over-count problem, drawer keeps drawing 10 strokes for 6)
- 伢 (needs 牙 primitive)
- 伥 (blocked on 长 canonical delivery)
- 西 (frame-closure issue; hand-derive)
- 伪 (right 为 shape reproduces but panel rejects; visual weight)
- 次 (needs 欠 primitive)
- 佤 (needs 瓦 primitive with compound heng-zhe-wan-gou)
- 兆 (er_legs + 2 dot-clusters — hand-derive)
- 仰, 仲, 伉, 伉, 伉, 伉 (misc 亻+X where the right side is not
  in the bank and inlining under-draws)

### Category E — B7 items still pending (revisited)

From B7 scan_position_400 Category B (X-cross cluster with cool-down
till position 283):
- **癶** (p3_char_0193_癶) — cool-down expires; enter B9 retry queue
  with `CROSS_ANCHOR` snippet applied.
- **处** (p3_char_0212_处) — enter B9 retry queue.
- **処** (p3_char_0213_処) — enter B9 retry queue.
- **乩** (p3_char_0228_乩) — enter B9 retry queue.

And from B7 Category D (missed-bank-hit with cool-down till 283):
- **那** (p3_char_0233_那) — enter B9 retry queue with mandatory
  `fu_right.py` import.
- **凹** (p3_char_0217_凹) — enter B9 retry queue with 5-stroke plan.

---

## Total B9 retry queue length

- Category A: 0 (all 7 dropped as TERMINAL_FROZEN).
- Category B (B8 main FAILs, cool-down till pos 500): 10.
- Category C: 3 primitive promotions (not retries — done pre-B9 by
  Teacher).
- Category D: 0 executable (skip until position 500 minimum).
- Category E (B7 pending, cool-down expiring): 6.

**Executable B9 retry queue (items dispatcher should re-run)**:
10 (Cat B) + 6 (Cat E) = **16 items**.

## Predictions for B9

- B9 mains: 40-50% (item pool continues 亻+X heavy; no structural
  memory change since B7).
- B9 retries: expected ~30-40% pass. Rationale: Category B items
  have specific "import X" fixes surfaceable via v10 trajectory-view
  + errata; Category E X-cross items have the ready-to-copy snippet
  in `drawer_memory.md`.
- Chronic-import rate on B9 mains containing 丿/刀/冂/弓/马: predict
  0-10% again unless the dispatcher-pre-check is built. This is the
  same falsification target as B7 and B8 — 3 negative batches on the
  same mechanism argues for retiring it.

## Structural notes carried into B9

- No new primitives added by curator (0 promotions this batch).
- No prunes (deferred — see evolution.md position-450 audit).
- No memory-file restructure (v8 slim checklist still active).
- v10 trajectory-view continues (retries see full past-attempt PNGs).
- Recommend Teacher: hand-write `fu_left.py`, `yan_side.py`,
  `zou_zhi.py` before B9 dispatch (see Category C).
