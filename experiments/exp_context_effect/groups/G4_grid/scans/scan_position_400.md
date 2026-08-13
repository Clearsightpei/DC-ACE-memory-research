# Scan @ position 400 — B7 curator retry queue for B8

**Batch summary**:
- B7 mains: 25 PASS / 25 FAIL (50%, best G4 ever).
- B7 retries (v8 prompt): 0 PASS / 12 FAIL.
- B7r reruns (v9 visual-diff prompt): 2 PASS / 10 FAIL (比, 文
  graduated).

**Chronic primitive import rate (B7 mains, targets containing
冂/马)**: 0/6 imports; 4 comment-only mentions. Same pathology as
B6 — v8 mandatory-snippets did not lift adoption. Escalation:
dispatcher-level pre-check is next lever (deferred to position 450).

---

## Retry queue for B8 (positions 401-450)

### Category A — CANONICAL promotions (drawer writes zero anchors)

These 7 items reach or exceed retry_n=2 AND both v8/v9 prompts
failed to lift them. Under v8 canonical-promotion policy, they
become hand-written primitives in `success_bank/code/chronic/` for
B8. Drawer is told: "call `draw_<x>()` — no arguments, no anchor
freedom."

| item_id | Char | retry_n | Canonical file | Anchor plan seed |
|---------|------|---------|----------------|------------------|
| p2_radical_088_长 | 长 | 3 | `chronic/chang_long.py` | Straight-竖提 spine + 短撇 upper-left; MMH normalized to fill canvas |
| p2_radical_081_夂 | 夂 | 3 | `chronic/zhi_dive.py` | ク top + X-cross via CROSS_ANCHOR=('BC', 0.5, 0.35) (from B7r 文 pattern) |
| p2_radical_084_夊 | 夊 | 3 | `chronic/sui_slow.py` | Similar to 夂 but with T-weld ク top; CROSS_ANCHOR=('BC', 0.5, 0.35) |
| p2_radical_119_水 | 水 | 2 | `chronic/shui_water.py` | 4-stroke HARD PLAN: spine 竖钩 + left 撇 + right 撇 + right 捺; assert len==4 |
| p2_radical_116_礻 | 礻 | 2 | `chronic/shi_altar.py` | dot(top) + 横撇 + straight 竖 (spine y∈[0.35,0.95]) + 2 dots flanking |
| p2_radical_135_无 | 无 | 3 | `chronic/wu_none.py` | 短横 + 长横 + 撇 + 竖弯钩 with weld at BC |
| p2_radical_111_气 | 气 | 3 | `chronic/qi_air.py` | Compound 撇 + 3 horizontals (y=0.35/0.55) + 横斜钩 tail |

### Category B — Standard cool-down retries (fits the v9 X-cross snippet)

These 4 items have B7 main FAIL with X-cross topology bugs the v9
visual-diff snippet is designed to catch. Cool-down means they enter
the retry queue at retry_n=1 for B9 (50-item cooldown from B7's tail
at position 233).

| item_id | Char | Cool-down till | Fix idea |
|---------|------|----------------|----------|
| p3_char_0193_癶 | 癶 | position 283 | CROSS_ANCHOR pattern (both inner strokes routed through shared BC pixel) |
| p3_char_0212_处 | 处 | position 283 | CROSS_ANCHOR pattern on 夂-head |
| p3_char_0213_処 | 処 | position 283 | 几 (`ji.py`) + inner 夂 with CROSS_ANCHOR |
| p3_char_0228_乩 | 乩 | position 283 | CROSS-like on 占 + 乚 hook |

### Category C — Prerequisites for the next 50 items (401-450)

The Teacher-injected phase-3 sequence advances into more complex
compositions. Prereqs identified for B8 items:

- **阝-left primitive (`fu_left.py`)**: still missing. B6 items 队,
  B7 items 那 all lack it. If B8 dispatcher pulls any 阝-left char,
  the drawer will hand-derive again. Recommend Teacher: promote
  `fu_left.py` before B8 as a pure primitive push (not a retry).
- **乙-family family (乞, 己, 已 variants)**: repeatedly composed and
  repeatedly wrong. If B8 pulls 乞-containing chars (仡 retry, 吃,
  乞 itself), they will FAIL without a canonical 乙-family primitive.
  Recommend: promote `yi_family.py` covering 乙, 乚, 乞, 已.

### Category D — B7 mains eligible for immediate retry (bank hit but
missed)

These 3 items have a mastered bank primitive that would apply, but
the B7 drawer didn't import it. Not chronic (retry_n=1), so goes to
normal retry queue with a LITERAL fix in errata.

| item_id | Char | Missed import | Cool-down till |
|---------|------|----------------|----------------|
| p3_char_0233_那 | 那 | `fu_right.py` for 阝-right | position 283 |
| p3_char_0211_冯 | 冯 | (needs chronic/ma_horse with offset support — canonical fix needed first) | deferred |
| p3_char_0217_凹 | 凹 | none applies; hand-only. Cool-down 50 items with 5-stroke plan | position 267 |

### Category E — Skip (no clear next fix)

Items where the FAIL mode has no obvious next step; not queued for
B8. Will be re-visited at position 450 with fresh eyes.

- 仡 (needs 乞 primitive first)
- 仫 (needs 么 primitive — 幺 exists but 么 has an added upper 撇)
- 记 (needs full 己 primitive)
- 亘 / 亙 (bracketed stack — needs a new "stack primitive"?)

---

## Total B8 retry queue length

- Category A (canonical, no retry ping): 7 items get bank-installed;
  drawer just calls them.
- Category B (X-cross cluster): 4 items on cool-down till position 283.
- Category C (prereqs): 2 primitive-only promotions (阝-left,
  乙-family) — not "retries" per se.
- Category D (missed-bank-hit): 2 items on cool-down till position
  283 (那, 凹); 冯 deferred.

**Executable B8 retry queue (items dispatcher should re-run)**:
7 canonical-replacement items (长, 夂, 夊, 水, 礻, 无, 气) — these
are re-drawn by CANONICAL, not by drawer creativity. Length = **7**.

Category B/D items enter cool-down and become executable at position
283 (in B9 not B8).

## Predictions for B8

- 7 canonical items: expected 5-7 PASS (top of chronic-cluster wins
  from position 300 was 0/5 → this batch we go in with confidence
  the canonical shape has been tested).
- B8 main pass: 45-55% (v9 prompt in effect for all mains now, not
  just retries; visual-diff Step 0 should catch topology bugs at
  first attempt).
- B8 chronic-import rate on B8 mains: target 30%+ if dispatcher
  pre-check is added; otherwise expected 0-10% (baseline).
