# G2 Frozen Retry Cohort (v7.3, pos 300)

*Created 2026-07-24 as part of B5 self-evolution decision (evolution.md
pos 326). These items reached `retry_n ≥ 3` with identical failure
modes across three separate batches (B3, B4, B5) and received no
transferable memory guidance. They are FROZEN from the active retry
scan cohort until UNFROZEN by explicit evidence.*

**Freeze policy**:
1. Items in this file are **NOT** candidates for the errata scan.
2. They remain in `errata.md` for provenance and cross-reference.
3. Their existence does NOT count against retry-pass-rate metrics
   (denominator now excludes them).
4. **Unfreeze condition**: if a structurally-adjacent character
   PASSes in a later batch (e.g. 攵 for the 夂 family, or a 二-lid
   compound for the 旡 family), the curator may explicitly unfreeze
   the item in evolution.md and return it to the active pool.

---

## Frozen items (as of B5 close, pos 300)

| item_id | target | retry_n | first_fail | frozen_at | failure pattern (invariant across retries) |
|---------|--------|---------|------------|-----------|---------------------------------------------|
| p2_radical_058_马 | 马 | 3 | B1 | B5/pos 250 | top-box + tail schema unstable; body-height fixes never transfer |
| p2_radical_080_尢 | 尢 | 3 | B2 | B5/pos 250 | missing top-一 lid → reads as 九 across 3 fixes |
| p2_radical_081_夂 | 夂 | 3 | B2 | B5/pos 250 | 捺 fails to dominate 撇; length-differential knob never sufficient |
| p2_radical_089_车 | 车 | 3 | B2 | B5/pos 250 | differential-横 lengths never distinctive; symmetric-王 collapse |
| p2_radical_094_风 | 风 | 3 | B2 | B5/pos 250 | 横折弯钩 boxy-corner persists; ambiguous with 冈 |
| p2_radical_099_旡 | 旡 | 3 | B2 | B5/pos 250 | copy-无-layout protocol fails; leg-pair splay ambiguous |
| p2_radical_106_牛 | 牛 | 3 | B2 | B5/pos 250 | 65-vs-165 differential never decisive vs 午 |

Additionally: **p2_radical_093_方** and **p2_radical_100_见** and
**p2_radical_042_巛** and **p2_radical_088_长** are at `retry_n=2` or
have crossed into retry_n=3 in prior fails but are NOT frozen yet.
They remain eligible for the active scan pool. If they fail again in
B6, they graduate into this file at that point.

---

## B6 duplicate-of-frozen guard

If a B6 curriculum item is itself one of the frozen chars (e.g.
**311 风** is a frozen radical item, drawn again as a P3 char), the
Drawer draws it normally as a P3 main attempt — the freeze applies
only to the RETRY mechanism, not to the main curriculum. Main-curriculum
attempts on frozen chars are watched for accidental unfreeze evidence
(if the fresh main attempt PASSes with no explicit retry effort, that's
a strong signal to unfreeze the corresponding radical retry).

**B6 items to watch for accidental-unfreeze signals**:
- pos 311 风 → if PASSes on main attempt, unfreeze p2_radical_094_风.

---

## Change log

- **2026-07-24 @ pos 300**: file created; 7 items frozen from B5 close
  (per evolution.md pos 326 decision).
- **2026-08-03 @ pos 600 (B11 curator)**: added frozen-radical MODE
  tracker below. These are not per-item freezes (retries retired at
  pos 388) — they are attested-multi-batch failure modes for the
  drawer's TIER-0 G alarm in `memory_index.md`.
- **2026-08-04 @ pos ~650 (B12 curator)**: added 疒 row — 7-attested
  in a single batch (all 7 疒-family items in B12 FAILed with the
  same "drawn as 广" mode). Decomposition fix hypothesis derived
  from direct GT observation, not speculation.
- **2026-08-05 @ pos ~700 (B13 curator)**: **疒 fix hypothesis
  FALSIFIED.** B13 had 8 疒-family items (疰/疱/疳/疴/疸/疹/疽/痂).
  Curator inspected 5 generated.py files — ALL applied the frozen_cohort
  5-stroke decomposition (点/横/长撇/内点/提) AND tucked body inside
  the 撇 sweep AND used bez+stroke helpers. Result: 7 FAIL + 1 C
  (痂 — 加 body is more compact). Hypothesis is **structurally
  followed but calligraphically insufficient**. The 5-stroke sequence
  is correct topologically but the resulting canopy still reads as
  `广`-with-extra-marks to the human judge — the inner 点/提 pair
  needs to sit visibly *inside* the canopy's upper triangle, not
  dangling on the 撇 stem. Downgraded to "unverified — recipe was
  applied without transfer". No new hypothesis proposed (would be
  speculation without pass evidence).
- **2026-08-05 @ pos ~700 (B13 curator)**: **NEW 辶/走 row added.**
  B13 had 5 wrap-radical items (适/通/造/速/起). All FAIL, uniform
  mode: 辶 rendered as a flat wave-shape BESIDE the interior body,
  not as a wrap that runs UNDER-and-around the body. The 平捺
  sweep-tail was drawn but did not carry the interior visually.
  This mode was previously attested once in B12 (选 FAIL) but is
  now attested-5x-in-one-batch. Wrap topology is the missing
  encoding.
- **2026-08-05 @ pos ~700 (B13 curator)**: **NEW 田-body-compound row
  added.** 6 田-body items with rare tops (畚/畛/畜/畝/畟/畢) all
  FAIL. 田 itself is not the issue (田/由/四/町 pass in isolation).
  The rare tops (龹/㐱/玄/亳/華-lookalike) have no decomposition
  encoding and drawer produces scatter.

---

## Frozen-radical MODES (attested-multi-batch, not per-item)

| radical | attested batches | fail count | typical mode | fix hypothesis (unverified) |
|---------|------------------|------------|--------------|------------------------------|
| 讠 | B7, B10, B11 | 5 (记, 证, 话, 说, 转, 线, 规) | left component drawn as detached sticks; 亠-lid + 3-tick body separated | render 讠 as 亠(dot-横) + coiled-3-flick with `stroke(pts, widths=(3, 5))` — draw as ONE continuous polyline, not 3 separate `d.line` calls |
| 戈 | B7, B8, B9, B10, B11 | 5 (代, 伐, 我, 找, 或) | hook missing or straight-down; top 丶 dot detached | 斜钩 with quadratic Bezier arc from top-right down-then-right, then hook flick UP-and-LEFT ~-115°. Top 丶 must sit above 一 crossbar with ~5 px overlap |
| 攵/攴 | B7, B10, B11 | 3 (改, 放, 畋, 畈) | rendered as 4 detached sticks; splay lost | 攵 = 撇 + 撇 + 横 + 捺. Third stroke 横 crosses BOTH 撇s at ~y-midpoint. Fourth 捺 originates from same midpoint |
| 匕 / 兑-hook | B6, B7, B10, B11 | continuing | hook goes DOWN or straight up instead of UP-and-LEFT | see TIER-0 B; render 竖弯钩 as bez arc, THEN hook flick as separate 20-pt curve |
| 纟 | B7 recent, B10 (经) | 2+ | fragmented into detached loops | render 纟 as 撇 + 撇折 + 提 — the 3 middle segments should share joint pixels |
| 弓 | (张 B10) | 1 | not yet attested-3x | monitor |
| 疒 | B12 (7) + B13 (7 more) | 14 (疣/疤/疥/疫/疬/疭/疮 B12 + 疰/疱/疳/疴/疸/疹/疽 B13,痂 C only) | B12: drawn as `广` (missing inner 点/提). B13: **recipe applied but still FAIL** — inner 点/提 pair drawn as isolated ticks alongside 撇 stem rather than visually nested inside the canopy triangle | ~~B12 hypothesis: 5-stroke decomposition~~ **FALSIFIED B13.** Applying the 5-stroke sequence is necessary but not sufficient. Open question: needs canopy-triangle geometric constraint (inner 点+提 must sit in the wedge bounded by 横 above, 撇 to the left) — untested. Also try: shrink body 20% and pack fully under 撇's belly. Neither verified. |
| 辶/走 (wrap) | B12 (1 选) + B13 (5) | 6 (选 B12; 适/通/造/速/起 B13) | 辶 rendered as a flat wave BESIDE the interior body; wrap topology (捺-tail sweeps UNDER interior, interior nests INSIDE the fold) not encoded | **Untested.** 辶 = 3 strokes: (1) 点 top-left, (2) 横折折撇 shepherd-hook from just-below-点 down-left-down, (3) 平捺 long sweep from directly BELOW interior body's LEFT edge, sweeping right past the interior's RIGHT edge, terminating in an up-right foot-flare. Interior body sits ABOVE the 平捺, with its bottom stroke overlapping the 捺's start point. `bez()` for the 捺, taper thick→thin→thick (foot flare). No verified example yet — G2's 辶-radical alone PASSed at B1 but 辶-compounds have never PASSed. |
| 田-compound (rare top) | B13 (6) | 6 (畚/畛/畜/畝/畟/畢 B13) | 田 itself renders correctly (compare 田/由/町 PASSes) but rare tops (龹/㐱/玄/亳/華-lookalike) have no decomposition and produce scatter | Untested. General heuristic: for any 田-body compound with a rare top, do NOT invent the top from label alone — trace the GT stroke-by-stroke and emit each stroke as a separate call in the order the GT presents them. Do not attempt to name the top's structural class. |

**Note**: These are drawer-side retrieval alarms, not curriculum
freezes. Main curriculum still schedules items containing these
radicals. Attested-count crossing 3 means: "you have been warned this
radical fails; open this row and apply the fix hypothesis before
drawing." Whether the fix hypothesis actually works is currently
untested — memory-invariance policy (pos-438) forbids testing fix
hypotheses via curriculum change; we can only wait for the natural
appearance of such items and observe.
