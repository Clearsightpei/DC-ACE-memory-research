# G2 Errata Scan — Position 100

Scan performed at curriculum position 100 (end of second 50-item batch
B1, boundary into B2). Retry decisions follow shared_rules v6:
(a) prospective / (b) retrospective, with 50-item cooldown after any
prior retry.

## Upcoming curriculum window (positions 101-150 = radicals 069-118)

069 氵 · 070 纟 · 071 巳 · 072 土 · 073 囗 · 074 兀 · 075 夕 · 076 小 ·
077 忄 · 078 幺 · 079 弋 · 080 尢 · 081 夂 · 082 子 · 083 丬 · 084 夊 ·
085 贝 · 086 比 · 087 灬 · 088 长 · 089 车 · 090 歹 · 091 斗 · 092 厄 ·
093 方 · 094 风 · 095 父 · 096 戈 · 097 户 · 098 火 · 099 旡 · 100 见 ·
101 斤 · 102 耂 · 103 毛 · 104 木 · 105 肀 · 106 牛 · 107 爿 · 108 片 ·
109 攴 · 110 攵 · 111 气 · 112 欠 · 113 犬 · 114 日 · 115 氏 · 116 礻 ·
117 手 · 118 殳

## Cooldown check

- Scan-50 retries (匕, 厂, 刀 at pos ~50) become eligible at pos 100+.
  All are eligible now.
- Batch-6 refresh (positions ~33) for stroke_24 and stroke_32:
  eligible from pos ~83; both eligible now.

## Decisions

### p1_stroke_24_横撇弯钩 (retry_n≥1, last: batch-6 refresh ~pos 33)

**[SKIP]** — Cooldown expired but the belly-on-right arc parametrization
that this stroke requires remains UNPROVEN (memory: KEY PRIMITIVE
section explicitly says "any item requiring belly-on-right must
validate the mirrored parametrization on a simple synthetic curve
first"). No prospective anchor either — 阝 (also in errata for the
same reason) is not itself in the next 50 items. Blocked, not
minimalist.

### p1_stroke_32_横折折折钩 (retry_n=2, batch-6 refresh ~pos 33)

**[SKIP]** — No (a) match: this rare 4-fold-plus-hook stroke does
not appear as a component of any radical in positions 101-150.
No new proven insight since scan_position_050. retry_n already at 2.

### p2_radical_011_匕 (batch bootstrap, retry_n=2, last retry ~pos 50)

**[RETRY]** — Very strong (a) prospective. Position 086 is 比, whose
canonical decomposition is **匕 + 匕** — literally two 匕 side by
side. Passing 匕 now would supply the proven primitive for 086
directly. Also (b) retrospective: batch-B1 diagnosis pinpointed the
missing terminal 钩 flick; new principle 5 "Draw the flick" (added
end-B1) directly addresses that exact defect. Cooldown expired
(pos 50 + 50 = 100).

### p2_radical_015_刀 (batch bootstrap, retry_n=2, last retry ~pos 50)

**[RETRY]** — Moderate (a): position 093 方 contains 横折钩 + 撇
in the same topology as 刀. (b) Retrospective: new "joining-dab
discipline" corollary (r_dab = r_seg, not r+2) at hook bases in
principle 5 directly targets the stray-nub artifact that failed the
prior retry. Cooldown expired.

### p2_radical_020_阝 (B1, retry_n=0)

**[SKIP]** — Requires the same unproven belly-on-right arc as
stroke_24. Memory explicitly blocks. No prospective match in
101-150 (left-ear 阝 does not decompose into anything upcoming).

### p2_radical_025_力 (B1, retry_n=0)

**[RETRY]** — (a) Prospective: position 093 方 contains the same
横折钩 + 撇 pair; passing 力 now proves the topology for 方. Also
100 见 has a similar hooked-vertical + inner stroke. (b) Retrospective:
principle 3 (crossing strokes must be visible) fixes the exact defect
(a stray dot instead of a full crossing 撇). No cooldown.

### p2_radical_028_人 (B1, retry_n=0)

**[RETRY]** — Strong (a): 人-topology appears in three upcoming items:
098 火 (bottom two strokes = 人), 112 欠 (bottom = 人-like), 113 犬
(contains 大 which is 人 + 一). Fixing the 撇 + 捺 (bowed 撇, thin→thick
捺 with press-foot) here unlocks all three. (b) new principle 7
(人 vs 入 topology-overhang) directly speaks to the confusion.

### p2_radical_030_入 (B1, retry_n=0)

**[RETRY]** — (b) Retrospective: new principle 7 explicitly names the
入-overhang as the distinguishing signature (捺 starts higher than 撇,
overhangs to the left of 撇's start). This principle did not exist
when the item first failed. (a) weaker: no direct 入 embedding in
101-150, but 095 父 has an 入-like bottom half.

### p2_radical_032_厶 (B1, retry_n=0)

**[SKIP]** — No prospective match in 101-150. Weak retrospective:
principle 9 ("never invent structure the label doesn't name") is
relevant but the composition 撇折 + 点 is idiosyncratic and rehearsing
it doesn't unlock upcoming items. Save the attempt slot.

### p2_radical_042_巛 (B1, retry_n=0)

**[SKIP]** — No prospective match (no wave-radical or ㄑ-triplet
in 101-150). Retry costs a slot for zero downstream leverage.

### p2_radical_047_飞 (B1, retry_n=0)

**[RETRY]** — (b) Strong retrospective: the failure was a missing /
misdirected 横折弯钩 hook, and 横折弯钩 is now the memory's KEY
PRIMITIVE with a proven tangent-continuous arc recipe (see batch-2
mastery: 横折弯钩 PASSED). Applying the proven recipe should land
飞 cleanly. (a) weaker but present: 099 旡 has a hook-terminated
compound reminiscent of 飞's silhouette.

### p2_radical_048_干 (B1, retry_n=0)

**[RETRY]** — Very strong (a): position 072 土 is the length-ratio
sibling of 干 (both have two horizontals + vertical, distinguished
only by which 横 is longer). Also 106 牛 has a 干-like top structure.
(b) new principle 6 (length-ratio distinguishers table) codifies
exactly the fix. No cooldown.

### p2_radical_050_弓 (B1, retry_n=0)

**[SKIP]** — No prospective match in 101-150 (no 弓-family radicals
upcoming). Retrospective only marginal (beat-count rule was already
in memory when 弓 failed).

### p2_radical_053_己 (B1, retry_n=0)

**[RETRY]** — Strong (a): position 071 巳 is a direct sibling of 己
(己/已/巳 differ only in where the middle 横 attaches to the left
wall — principle already in errata diagnosis). Also 099 旡 has a
top box + bottom hook echo. (b) new principle 5 (draw the flick)
addresses the specific 竖弯钩 tail-sweep failure. No cooldown.

### p2_radical_055_彑 (B1, retry_n=0)

**[SKIP]** — No prospective match. 彑 is a niche chevron+彐 shape
that does not appear as a component of any radical in 101-150.
No new principle since B1 specifically addresses the missing chevron
defect.

### p2_radical_056_巾 (B1, retry_n=0)

**[SKIP]** — No prospective match in 101-150. 巾 does not embed
into any upcoming radical.

### p2_radical_058_马 (B1, retry_n=0)

**[RETRY]** — (b) Strong retrospective: new principle 8
("Multi-fold body-connection: bottom stroke often runs THROUGH")
was added specifically to name 马's failure mode (floating bottom
横 vs a 横 that runs through the terminal hook). Applying the
principle to its origin-item is the cleanest validation.
(a) weaker: 100 见 has a similar "bottom curl runs through" pattern.

### p2_radical_059_门 (B1, retry_n=0)

**[SKIP]** — No 门-family radical in 101-150. The 门 gap-at-top
defect is worth fixing eventually but no downstream item pulls
on it in the next 50.

### p2_radical_067_士 (B1, retry_n=0)

**[RETRY]** — Very strong (a): position 072 土 is the length-ratio
mirror of 士 (top-longer vs bottom-longer). Fixing 士 forces
codification of the ratio directly before drawing 土. (b) principle 6
length-ratio table already in memory. No cooldown.

## Summary

- **10 RETRY**: 匕, 刀, 力, 人, 入, 飞, 干, 己, 马, 士.
- **9 SKIP**: stroke_24, stroke_32, 阝, 厶, 巛, 弓, 彑, 巾, 门.
- Retry rate this scan: 10/19 = 53%. Balanced (not minimalist);
  every RETRY has a real (a) or (b) reason; every SKIP is justified
  by either cooldown, an unproven primitive, or absent downstream
  leverage.
- All 10 retries carry strong (a) or (b) evidence tied to items in
  positions 101-150 or to a new principle added since first failure.
