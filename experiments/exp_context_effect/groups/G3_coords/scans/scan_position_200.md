# Errata Scan — G3 (coord-bank) — Curriculum Position 200

Scan performed at position 200 (end of B3 / start of B4). This is the
**second scan under v7 self-evolution** (see `evolution.md` position
200 second-pass entry). Upcoming 50 items span 201–250 (all Phase-3
characters at 3–4 画): 刁 丁 刂 勹 匕 之 丫 大 丬 个 丸 上 久 也
乇 子 亍 于 亡 下 亼 三 小 兀 么 卂 与 卄 门 叉 及 囗 山 纟 干
夂 口 夊 飞 孑 千 孓 习 艹 已 宀 女 尢 才.

## Batch context

**B3 retry pass rate = 0/13 (0%)** — far below the 40% floor set at
scan_150. Meta-pattern noted in errata: 7 of 13 retries used the new
v7 adaptive helpers (variant_pie/na/dian); 5 of those had fail-mode
SHIFT (per-stroke variant improved but composition still failed).
Curator response for B4: added **composition-geometry helpers**
`kiss_apex`, `pie_point`, `mirror_dian_pair` to
`success_bank/code/_shared_helpers.py`, and added **worked composition
examples** to `form_catalog.md` (X-crossing / mirror-dot /
radical-alias families).

The new helpers directly address the exact composition failures the B3
retries showed. However, all 13 items that would most naturally test
them (人, 入, 大, 犬, 力, 刀, 火, 丷, 忄, 丬, 长, 手, 见) are in
**50-item cooldown** (retried at position 200 → next eligible at
position 250). This scan therefore cannot test the helpers on their
primary target family.

Instead, this scan targets:
1. **Cooldown-free items with STRONG (a) prospective match** to the
   201-250 window — some of which also happen to benefit from the new
   composition helpers on adjacent shape families (夂/夊 apex-kiss,
   女 crossing).
2. **Retry_n=2 cooldown-expired items** whose (a) is strong AND whose
   composition failure mode plausibly maps to `kiss_apex` (女).

## Cooldown status @ position 200

- **13 items just retried at position 200 (0/13 PASS)** — cooldown
  until position 250. **BLOCKED**: 015_刀, 021_丷, 025_力, 028_人,
  030_入, 046_大, 077_忄, 083_丬, 088_长, 098_火, 100_见, 113_犬,
  117_手.
- **retry_n=2 items last retried at scan_100 (position 100)** —
  cooldown expired at position 150; not retried in scan_150 (053_己,
  038_㔾, 061_女, 062_犭). Still eligible.
- **retry_n=0 items** (B1/B2/B3 fails never retried) — always
  eligible.

## Prospective (a) map — errata × 201–250

| errata item | curriculum slot in 201–250 | notes |
|---|---|---|
| 074 兀 | pos 224 兀 (Phase-3 char) | direct — identity alias if radical solved |
| 080 尢 | pos 248 尢 (Phase-3 char) | direct — same family as 兀 |
| 081 夂 | pos 236 夂 (Phase-3 char) | direct |
| 084 夊 | pos 238 夊 (Phase-3 char) | direct — same family as 夂 |
| 059 门 | pos 229 门 (Phase-3 char) | direct |
| 047 飞 | pos 239 飞 (Phase-3 char) | direct |
| 082 子 | pos 216 子 + pos 240 孑 + pos 242 孓 | direct + component prereq |
| 061 女 | pos 247 女 (Phase-3 char) | direct |
| 025 力 | pos 185 (already passed window) | — cooldown-blocked anyway |
| 015 刀 | pos 200 (already passed window) | — cooldown-blocked anyway |
| 053 己 | — (245 已 is similar but not identical shape) | weak |
| 038 㔾 | — | none direct |
| 062 犭 | — | none direct |
| 096 戈 | — | none direct |
| all others | — | none direct |

Notable non-errata upcoming: 208 大, 209 丬, 232 囗 already covered by
bank (大 through fu.py X-crossing template; 丬 via 083_丬 recipe — but
cooldown blocks retry; 囗 via wei_radical.py) or by identity alias
(233 山 == shan.py).

## Retrospective (b) map — B3 new helpers × errata

B3 curator added three composition helpers. Their primary targets are
in cooldown, so we evaluate (b) fit against non-cooldown items:

| item | failure mode (from errata) | B3 helper that could apply | (b) strength |
|---|---|---|---|
| 081 夂 | "apex geometry lost" (two crossing 撇/捺-like) | `kiss_apex` (u_pie=0.0 or 0.3) — literal apex-share | **strong** |
| 084 夊 | same family as 夂 | same as 夂 | **strong** |
| 074 兀 | "leg widths mismatched + 竖弯钩 flat" | `pie_point` for pie-to-heng weld; not a pure X-crossing but joint-explicit | moderate |
| 080 尢 | same family as 兀 | same as 兀 | moderate |
| 061 女 | crossing 撇+heng+撇/na | `kiss_apex` u=0.5 for the interior crossing | moderate–strong |
| 082 子 | wan_gou hook detached | none direct; but `bezier_point` helper enables shaft-hook weld | moderate |
| 059 门 | frame + inner | none direct; validated jiong_radical.py inline recipe stands | moderate |
| 047 飞 | 横撇 + inner curl | none direct | weak |

Also worth noting: the `mirror_dian_pair` helper does not have a
non-cooldown target this window (the 3 mirror-dot items — 忄, 丷, 丬
— are all blocked).

## Decisions

### RETRY (8)

Per shared-rules "balance not minimalism": aim slightly HIGHER than
scan_150's 33% eligible-retry rate for items with strong (a), since
B3's 0% retry pass rate exposed a real signal that must be
re-benchmarked with the new composition helpers.

| # | item_id | retry_n before → after | (a) | (b) | primary rationale |
|---|---|---|---|---|---|
| 1 | p2_radical_081_夂 | 0 → 1 | **strong** (pos 236) | **strong** (kiss_apex u=0.0/0.3 literal apex-share) | prime B4 test of `kiss_apex` on a non-cooldown item; recipe = fu.py template with u_pie chosen from 夂 GT geometry |
| 2 | p2_radical_084_夊 | 0 → 1 | **strong** (pos 238) | **strong** (same as 夂) | validates 夂 recipe transfers; low incremental cost |
| 3 | p2_radical_074_兀 | 0 → 1 | **strong** (pos 224) | moderate (pie_point for pie-to-heng weld + matched widths) | prospective; failure mode named "leg width mismatch" is now addressable with explicit joint pixel |
| 4 | p2_radical_080_尢 | 0 → 1 | **strong** (pos 248) | moderate (same as 兀) | validates 兀 recipe transfers |
| 5 | p2_radical_059_门 | 0 → 1 | **strong** (pos 229) | moderate (validated jiong_radical.py inline-3-segment recipe from B1 retry) | prospective; the B1 retry that produced jiong_radical.py explicitly validates the recipe for 门 |
| 6 | p2_radical_082_子 | 0 → 1 | **strong** (pos 216, 240, 242 — triple slot) | moderate (`bezier_point` for hook weld) | 3-item prospective coverage is the strongest (a) in this scan |
| 7 | p2_radical_047_飞 | 0 → 1 | **strong** (pos 239) | weak but justified by (a) alone per balance rule | prospective-only; only shot before terminal-freeze if this item never gets retried |
| 8 | p2_radical_061_女 | 2 → 3 | **strong** (pos 247) | moderate–strong (`kiss_apex` u=0.5 for interior crossing) | cooldown-expired at pos 150; new `kiss_apex` gives the specific new lever scan_150 waited for; approaches retry_n=3 terminal-freeze warning per shared_rules |

### SKIP (rationale summary)

- **13 cooldown-blocked items** (015_刀, 021_丷, 025_力, 028_人,
  030_入, 046_大, 077_忄, 083_丬, 088_长, 098_火, 100_见, 113_犬,
  117_手): 50-item cooldown after position 200 retry. Next eligible
  position 250. **These are the primary B4-target family for the new
  composition helpers** but the cooldown rule is inviolable.
- **Phase-1 hook fails (7 items)** including STALE p1_stroke_26_横折折:
  same as prior scans — no new lever for standalone hook strokes.
- **retry_n=2 cooldown-expired without new lever** (053_己, 038_㔾,
  062_犭): no direct (a) in 201–250; no B3 helper directly addresses
  curl-envelope / small-elbow-hook. Retrying would burn retry_n=3 for
  no reason. Continues scan_150's SKIP decision.
- **Retry_n=0 with no (a) and no (b) match**: 020_阝, 032_厶, 035_讠,
  036_廴, 040_屮, 041_彳, 042_巛, 050_弓, 055_彑, 056_巾, 058_马,
  096_戈, 097_户, 099_旡, 101_斤, 105_肀, 107_爿, 108_片, 109_攴,
  110_攵, 111_气, 112_欠, 115_氏, 118_殳, 078_幺, 079_弋, 085_贝,
  086_比, 089_车, 091_斗, 093_方, 094_风. Defer to a window with
  prospective utility or a matched helper.
- **B3 new fails without direct helper**: 119_水, 120_瓦, 121_尣
  (kissing-cousin of 兀 — could be added if 兀 passes), 122_王,
  123_韦, 125_毋, 127_牙, 132_支, 133_止, 134_爪, 135_无, 007_乛,
  0016_乃, 0018_乜, 0023_九, 0026_冂 (bank has jiong_radical — this
  is retrieval-discipline, not a retry candidate). Defer.

## Summary

- **Errata items considered**: ~55 net-active.
- **RETRY**: 8 items.
- **SKIP**: ~47 items (13 of which are cooldown-blocked, not
  discretionary skips).
- **Discretionary retry rate = 8 / (55 − 13) ≈ 19%** — lower than
  scan_150's 33% because the highest-value candidates (X-crossing +
  mirror-dot family that best match the new B3 composition helpers)
  are all in cooldown. The 8 chosen items all have STRONG (a) or
  STRONG (b), no marginal picks.

The scan is deliberately restrained: attempting 20+ items just to
"exercise" the new helpers on ill-matched shape families would repeat
scan_150's over-reach. Better to reserve the composition-helper test
for the position-250 scan when the cooldown lifts.

## Retry priority order (Drawer, attempt in this order)

1. **子 (082)** — 3-slot prospective coverage; wan_gou hook weld is a
   clean `bezier_point` demonstration.
2. **夂 (081)** — strongest (b) fit for `kiss_apex`; validates the
   composition helper on a non-cooldown family.
3. **夊 (084)** — validates 夂 recipe transfers.
4. **门 (059)** — reuse jiong_radical.py inline recipe.
5. **兀 (074)** — prospective + explicit pie-heng joint via
   `pie_point`.
6. **尢 (080)** — validates 兀 recipe transfers.
7. **女 (061)** — retry_n=3 approaches terminal-freeze; use
   `kiss_apex` u=0.5 for interior crossing.
8. **飞 (047)** — prospective-only; last chance before freeze.

## Post-scan validation criterion

If B4 retry pass rate on these 8 items < 30%, the composition-helper
direction needs another round of introspection (perhaps the helpers
need per-family default profiles baked in). If ≥ 50%, the helpers
work when applied to the correct shape family, and the position-250
scan should aggressively retry the cooldown-lifted X-crossing +
mirror-dot family.
