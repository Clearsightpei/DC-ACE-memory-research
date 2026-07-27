# Sibling Signature Checklist (v7.2, pos 277)

*Created 2026-07-23 in response to B4 retry-rate drop (31% → 21%).
This file is a small, dense pre-drawing checklist for items that
recur in the retry cohort. Every retry FAIL in B4 traces to either
(a) a signature-bit override (draw the wrong sibling) or (b) a
terminal-flick omission. This file surfaces the check as a
single-scan artifact so the drawer doesn't have to grep
form_catalog under time pressure.*

**Consult BEFORE drawing any item whose label appears below.**
If your target is in this table, verbatim-copy the bit-check row
into your generated.py docstring; write "SIGNATURE BIT: <bit>" and
render it exactly. Do NOT deviate on GT-tracing grounds — the bit
IS the identity.

---

## The bright-line bits

| target | one-sentence signature bit | common wrong-render |
|--------|----------------------------|---------------------|
| 人 | apex SHARED at same y; both strokes throw outward; 捺 has thick foot | 入 (捺 overhangs) |
| 入 | 捺 STARTS HIGHER than 撇 by 30+ px; 捺 overhangs 撇 at top | 人 (shared apex) |
| 士 | TOP 横 LONGER than bottom (~1.5×) | 土 |
| 土 | BOTTOM 横 LONGER than top (~1.5×) | 士 |
| 干 | TOP 横 SHORTER (~65%); through-竖 no hook | 千, 士 |
| 千 | 撇-LID top + straight through-竖 (no hook) | 干, 于 |
| 于 | TWO 一 + central 亅 (with hook) | 千 (撇-lid) |
| 己 | middle 横 FLOATS from BOTH walls (start x≈95, end x≈200) | 已, 巳 |
| 已 | middle 横 TOUCHES left wall midway | 己, 巳 |
| 巳 | middle 横 TOUCHES at top | 己, 已 |
| 匕 | top stroke is a 撇 (upper-right→lower-left); terminal hook flicks UP-and-LEFT | 七 (top 横) |
| 七 | top stroke is a 横 (left→right) | 匕 (top 撇) |
| 大 | 一 + 撇+捺 sharing apex ON the 一 | 六 (亠 lid + 八) |
| 户 | top 丶 dot ABOVE the 一 | 尸 (no dot) |
| 尸 | top starts with 一 directly (no dot above) | 户 |
| 贝 | 冂 + TWO internal 横 stacked in LOWER 2/3 of box + legs | 见 (ONE 横 + ㄦ legs) |
| 见 | 冂 + ONE 横 IN LOWER THIRD of box (~y=180+ on 300px canvas) + 撇+竖弯钩 legs | 贝; also 凡 if 横 sits at top of box |
| 木 | 一 + 竖 + 人-body (撇+捺) | 术/未/末 |
| 未 | SHORT top 横, LONG bottom 横 (short-over-long) | 末 |
| 末 | LONG top 横, SHORT bottom 横 | 未 |
| 术 | 木 + interior 点 upper-right | 木 |
| 刁 | 横折钩 + top-flick 撇 ON shoulder (short) | 丁 (no flick), 习 |
| 丁 | 一 + straight 亅 (no top flick) | 刁 |
| 亍 vs 于 | 亍: two 一 vertically farther apart; 于: two 一 close | ambiguity risk |
| 个 | 人-lid (proper thin-thick 捺 foot) + hanging 竖 | 亇 (two 撇 lid) |
| 丸 | 九 body + interior 丶 | 九 (no dot), 内 |
| 孑 | horizontal tick to LEFT of 竖钩 | 子, 孓 |
| 孓 | horizontal tick to RIGHT of 竖钩 | 子, 孑 |
| 子 | full 一 crossing 竖钩 | 孑/孓 (partial tick) |
| 尢 | 一 top + 撇 + 竖弯钩 (3 strokes with LID) | 九 (no lid) |
| 九 | 撇 + 横折弯钩 (2 strokes, 撇 CROSSES ABOVE the top 横) | 尢, 勺, 丸 |
| 之 | 丶 + 横撇 + 平捺 (top dot, 3 strokes) | 乏 (4 strokes) |
| 山 | 凵 base + tall MIDDLE 竖 rising ABOVE sides | 凵 alone, 屮 |
| 门 | top-left dot + 横折钩 with UP-LEFT hook | 冂 (no dot, no hook) |
| 上 | bottom 一 base + central 竖 + right-side tick 一 | 下 (mirror) |
| 下 | top 一 + central 竖 + right-side 点 | 上 (mirror) |
| 亾 | 亡 outer + 人 INSIDE (not stacked separately) | 亠+人 stack |

---

## The bright-line flicks

*B4 evidence: half of retry FAILs were hook-flick failures. The flick
IS the last 30 px of a stroke — if it flicks the wrong direction,
the whole stroke fails identity.*

| stroke-family | flick direction |
|---------------|-----------------|
| 竖钩 (亅) | UP-and-slightly-LEFT (~-100° to -110°) |
| 竖弯钩 | UP-and-LEFT after the arc (~-105° to -115°) |
| 横折钩 (any) | UP-and-LEFT at the terminal (~-105° to -120°) |
| 横折弯钩 (飞, 几, 九) | UP-and-LEFT after the sweeping arc (~-115°) |
| 斜钩 (戈) | UP-and-LEFT at the arc's end (~-110° to -120°) |
| 卧钩 (心) | UP-and-LEFT from the bowl's right end (~-145°) |

**Never** flick DOWN, DOWN-right, or straight up. When in doubt: the
hook always flicks back INTO the character body (toward the interior),
not outward.

---

## When this file transfers vs when it doesn't

Cite this file in your generated.py docstring when your target is
in either table above. Format:

```
# SIGNATURE CHECK (per sibling_signature_checklist.md):
#   target = <char>
#   bit = <verbatim from table>
#   flick = <verbatim if applicable>
```

If the target is NOT in either table, this file does not apply —
consult form_catalog.md and radical_position_rules.md normally.
