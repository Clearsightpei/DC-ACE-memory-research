# G2 Errata Scan — position 500 (B9 → B10 boundary)

**Scan type**: batch-boundary (end of B9, start of B10)
**Curator**: G2
**Date**: 2026-07-30
**Framework**: v7.4 (retries retired at B6/pos 388)
                v11 (pass_index.md available since B8)
                v12 (A-verdict enabled; first observed in B9)
                v13 (retrieval-only refactor permitted; memory-invariance
                     policy does NOT inhibit reshuffling)

---

## Retry queue for B10

**Length: 0.**

Retries retired at B6 (pos 388). Every B10 item is a first-attempt
p3 target. This scan verifies the retirement still holds given B9's
new signals.

### Signals considered

1. **v12 A verdicts** (你, 没). Both are compound characters where
   drawers applied calligraphic weight (teardrop taper + shoulder-dab
   + Bezier + hook flick). Would re-running any specific past-FAIL
   with the same drawer behavior lift it to PASS or A? Possibly, but
   the mechanism is drawer-side (spontaneous calligraphic default),
   not curator-supplyable. Adding it to memory (see drawer_memory
   pos-500 note) documents the pattern; it does not force retrieval.
   Not a reason to reopen retries.

2. **v11 pass_index.md** — every past PASS/A now discoverable with
   PNG path. Curators can consult specific past-PASS renders. B9's
   B10-eligible fails (e.g. 还 whose component 不 PASSed at p3_094)
   suggest the drawer could benefit from opening a past-PASS PNG
   during first-attempt. That's a drawer-prompt affordance, NOT a
   retry queue. Not a reason to reopen retries.

3. **B9 main-pass recovered to 24%** (12/50 vs B8's 12%). Still below
   B7's 42% band but within the item-difficulty envelope. No signal
   that retry would systematically add. Retirement holds.

4. **CBV density** (~4/38 = 11%): 光, 来, 运, 条 rendered with
   signature intact but labeler rejected. If any B10 rescoring shows
   these as PASS on re-view, we'd have a labeler-noise argument for
   revisiting the retry mechanism as a candidate-disagreement channel.
   Not this scan.

**Conclusion**: retry queue remains 0. Retirement policy per
evolution.md pos-388 stands.

---

## Retrieval-only refactor consideration (v13)

**Decision: NO refactor this scan.**

Reasoning:
- Memory footprint (8 files, ~250 KB) is stable since pos-388.
  drawer_memory + form_catalog + sibling_signature_checklist +
  radical_position_rules + composition_rules + memory_index +
  errata + evolution — each has a distinct owner-role.
- No B9 evidence that any specific file is HARD to locate. Sibling
  content was not retrieved by the drawer on 615, 619 伶 (bottom-hook
  flick) or 620 声 (尸 signature), but that's a retrieval-probability
  failure at first-attempt scale, not a file-organization failure.
  Moving the row to a different file would not raise retrieval prob.
- The pos-500 drawer_memory addition (calligraphic-weight note) is a
  content addition, not a refactor. It lives at the tail of
  drawer_memory where technique notes live.
- If B10-B11 show sustained sub-25% main-pass with continued CBV
  density, the next scan may consider promoting the CBV mode-tag to
  memory_index TIER-0 so drawers can proactively defend against it
  (e.g. "leave 5% margin around box boundaries so labeler doesn't
  read as neighboring char"). Not this scan.

---

## Frozen cohort — no changes

Still 6 items frozen (马, 夂, 车, 风, 旡, 牛 — 尢 also historically
listed but freeze status stable). No B9 evidence for unfreeze.

---

## B9 signal-of-record

- **12/50 = 24% main-pass** (10 PASS + 2 A). B8→B9 recovery of 12
  points. B7-B8-B9 rolling: 42% → 12% → 24%. Item-mix explains most
  of the swing (亻-compounds this batch: 12; B8: 17; B7: 3).
- **First A verdicts G2 has ever received**: 你, 没. Both compound
  characters; both applied calligraphic weight spontaneously. See
  drawer_memory.md pos-500 for the extracted pattern.
- **No new failure MECHANISMS**. All 38 fails fit modes documented
  in B4-B8 memory (compound-drift, sibling-bit, radical-body
  fragmentation, FROZEN-recur, CBV, rare/traditional, detachment).
  Retrieval-ceiling claim (pos-438) reinforced by absence of novelty
  in failures paired with absence of novelty in successes.
- **New quality ceiling emerged**: PASS→A lift via calligraphic
  weight. This is orthogonal to the retrieval-ceiling and does not
  falsify it.

---

## Summary

- **Errata size at scan**: ~101 open items post-B9 additions (38 new).
  MINUS 6 frozen = 95 active.
- **Retries scheduled**: **0** (retirement holds).
- **Retrieval-only refactor**: **not applied**.
- **B10 hypothesis**: main-pass rate 25-45% depending on item-mix.
  A rate 0-3 per 50 (if drawers retrieve calligraphic-weight note).
- **Ceiling policy status**: HELD. B9's 24% is inside the ceiling
  band. B8's 12% was an item-mix trough. Continue watching.
