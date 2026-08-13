# G2 Free-Form Drawer Memory

## Reset notice

Memory reset after Phase-2 restart. Preserved: Phase-1 stroke mastery
(items 1–32) plus general technique principles (PIL brush-dabs,
tangent-continuous arc primitive, 折-family beat-count rule,
segment-length hierarchy, standalone vs compound scale-up). Removed:
all Phase-2 radical mastery, identity checklists, diagnostics, and
the prior PROTOCOL CHANGE section. Phase 2 restarts fresh under the
GT-supported protocol.

**Spirit**: memory is **supplementary**. Use a proven entry when it
cleanly fits; when brief and memory disagree, trust the brief and the
GT PNG. Numeric parameters decay faster than principles; principles
decay faster than direct observation. **Renderer**: PIL brush-dabs
(below) preferred over `turtle` for calligraphic quality. All
Phase-1 entries below rendered PIL, black ink, 300×300 white.

---

## Radical-composition principles (batch B1, phase-2)

Distilled from the 15 fails in batch B1 (阝 力 人 入 厶 巛 飞 干 弓 己
彑 巾 马 门 士). Five new generalizable rules; complement the four
bootstrap-batch principles below.

### 5. Draw the flick — a stroke's identity often rides on its hook

For any stroke whose canonical class ends in 钩 (竖钩, 竖弯钩, 横折钩,
横折弯钩, 斜钩, 卧钩, 弯钩), the terminal 2-3 px flick is not decorative
— it IS the differentiating signature. Omitting it or misdirecting it
by more than ~30° collapses the character into a wrong sibling: 匕
without its hook reads as 七; 己 without its 竖弯钩 sweep reads as 巳;
弓 without its bottom hook reads as three stacked 横; 飞 with a
down-flick instead of up-left flick reads as a numeral 7. **Rule**:
draw the hook as an explicit final step of the compound stroke, not
as an afterthought that may or may not survive a taper-loop.

**Corollary — joining-dab discipline**: at the hook base, the joining
dab MUST NOT exceed segment radius. r+2 dabs at hook bases bleed below
the intended endpoint and produce a stray-nub artifact (see 刀 retry_1).
Use r+2 only at 折 shoulders and 顿 starts, never at hook joints.

### 6. Length-ratio distinguishers for stacked-horizontal radicals

Two-horizontal-plus-vertical radicals differ ONLY by which 横 is
longer, and getting this wrong silently reads as the sibling character:

| radical | top 横 | bottom 横 | vertical |
|---------|--------|-----------|----------|
| 士     | LONGER (~150 px) | shorter (~110 px) | pass-through |
| 土     | shorter | LONGER | pass-through |
| 干     | shorter (~65% of bottom) | LONGER (~170 px) | pass-through, no hook |
| 干-if-hook | shorter | LONGER | ends in 钩 → 千 |

Always check the length ratio against the intended character; do not
default to symmetric horizontals.

### 7. Topology overhang: 人 vs 入 and similar sibling pairs

人 and 入 share the same two strokes (撇 + 捺) but differ in where
they meet. 人: strokes meet at a single apex (both tops at same y). 入:
捺 starts HIGHER and OVERHANGS the 撇 by ~30 px — the 撇 begins BELOW
the 捺's top, and the 捺's upper end sticks out to the left of the
撇's start. This "overhang" is 入's ONLY distinguishing signature from
人. Same pattern applies to 八 vs 儿 (八 has two disjoint strokes with
gap at top; 儿 has 撇 + 竖弯钩 meeting near the top on the left).

### 8. Multi-fold body-connection: bottom stroke often runs THROUGH

For radicals whose bottom stroke visually terminates the internal
zig-zag body (马, 与, 号), the bottom 横 must ORIGINATE at the left
edge (aligned with the body's left wall) and run rightward THROUGH
the terminal hook. A floating bottom 横 disconnected from the body
reads as two separate glyphs, not a single character.

### 9. Never invent structure the label doesn't name

厶 = 撇折 + 点. Do NOT extend the 撇折's 折-tail into a shape that
"looks like" the closing 点 — draw the 点 as a separate primitive at
its own coordinates. 巛 = three ㄑ shapes (each = short 撇 + curved
竖), NOT three plain curves. Radicals are the sum of their named
primitives; substituting a "simpler" continuous shape usually drops
critical structural information.

---

## Radical-composition principles (bootstrap batch, phase-2)

Distilled from 3 fails in the 33–50 bootstrap batch (匕, 厂, 刀). All
three failed the same way: the drawer talked itself out of the correct
stroke-class semantics while GT-tracing.

### 1. Label > GT-tracing when they seem to conflict

When the item's label unambiguously names a stroke class (匕 = 撇 +
竖弯钩), **render that stroke class in its canonical direction**. Do
not let ambiguous-looking pixels in the GT convince you the 撇 is
"actually a 提" or "actually a horizontal." Directional identity of
each named stroke comes from the label, not from measurement of the
GT. In 匕, the top stroke is a 撇 — top-right → bottom-left throw —
even if a low-resolution GT rendering makes it look near-horizontal.

Corollary: watch your own docstring for waffling ("wait actually...
no wait..."). Waffling in the reasoning trail is a signal you're
about to render the wrong stroke class. Commit to the label, not
to your own re-reading.

### 2. Compound radicals: adjacent strokes SHARE joints, no inset

For radicals whose two strokes meet at a corner (厂, 广, 尸, 匚, 匸,
etc.), the two strokes share **the same corner pixel**, not "close but
inset." A gap of even 10–15 px at the corner destroys the radical's
signature silhouette (厂 without its corner reads as two disconnected
scribbles). Rule:

    stroke_2.start == stroke_1.start   (or stroke_1.end, whichever is the
                                        shared vertex)

Draw one 顿 press at the shared corner (r+2) to seat the joint. Do
NOT invent "signature notches" or "hook-nubs" that aren't in the GT.

### 3. Crossing strokes: the crossing must be visible

For radicals where stroke B crosses through stroke A (刀's 撇 crosses
the top 横; 匕's 撇 crosses the 竖弯钩's vertical), the crossing
stroke must **start on one side of A and end on the other side of A**,
with A's line visibly cutting through it. If B starts inside A's
bounding region and never crosses out, the crossing signature is
missing and the character reads wrong.

Concrete check: after rendering, mentally trace stroke B. Does its
start-endpoint sit ABOVE (or LEFT of) the crossed line, and its
end-endpoint BELOW (or RIGHT of) it? If both endpoints are on the
same side, B does not cross — it merely tangents.

### 4. Hook-flick angle discipline for standalone radicals

竖钩 / 竖弯钩 hooks flick **up-and-slightly-left**, roughly -100° to
-125° in image coords (NOT -90° straight up, NOT -150° near-horizontal).
A near-vertical hook reads as a rigid nub; a near-horizontal hook reads
as a 提. When rendering a standalone radical (not embedded in a larger
character), aim for -105° to -115° as the safe default, and give the
hook enough length (~30-40 px) to read as a swept flick rather than a
bump. Joining-dab radius at the hook base should equal segment radius
(NOT r+1 or r+2), else a stray sub-hook nub appears below the flick.

---

## General technique — tapered strokes via PIL brush-dabs

For strokes with directional taper (提 ti, 撇 pie, 捺 na, 钩 gou tips),
stacking many small filled circles ("brush dabs") along the stroke
path with a linearly varying radius produces smooth calligraphic
taper without needing turtle pensize tricks. Formula:

    for t in 0..1:
        x = x0 + (x1-x0)*t
        y = y0 + (y1-y0)*t
        r = r_start + (r_end - r_start)*t
        draw.ellipse((x-r, y-r, x+r, y+r), fill="black")

- Use ~400 steps for a 150–300 px stroke to avoid visible bumps.
- For 顿笔 (initial press), add one slightly-larger dab at the
  starting endpoint before the ramp.
- For a sharp tip, set r_end near 1.0 (not 0, so the last dab is
  still visible).

## Bezier-sampling alternative to brush-dabs

For curved strokes (弯钩, 横折钩, arcs of 撇/捺 tails), sampling a cubic
or quadratic Bezier at ~100 points and drawing short `draw.line`
segments with per-segment `width` gives smoother curvature control
than dabs, at slight cost to endpoint softness. Round-cap the entry
with one filled ellipse at P0 to hide the flat line-cap.

## Stroke-direction reminders (image coords, y grows DOWN)

- 提 (rising): start lower-left → end upper-right, thick→thin,
  angle ~25–35° above horizontal.
- 撇 (throw-away): start upper-right → end lower-left, thick→thin.
- 捺 (press-down): start upper-left → end lower-right, thin→thick
  ending in a flat/broad foot.
- 横 (heng): left → right, roughly uniform with small end press.
- 竖 (shu): top → bottom, roughly uniform.

## Hook (钩) family — general shape rules

A 钩 is a short secondary segment attached to the *end* of a primary
stroke; direction of the flick is fixed by the parent stroke class:

- 弯钩 / 竖钩: primary is a (near-)vertical from top → bottom; hook
  flicks up-and-left from the bottom endpoint. 弯钩 differs from 竖钩
  in that the primary is a smooth arc (top starts slightly right,
  curves down-and-left) rather than a straight vertical.
- 横钩: primary is a 横 left→right; hook flicks down-and-left from the
  right endpoint.
- 斜钩 (戈钩): primary slants down-and-right; hook flicks up from the
  bottom-right endpoint. Curvature clarification: the primary is NOT a
  ruler-straight diagonal — it bows with its **belly on the lower-left
  side** (concave toward upper-right). In quadratic-Bezier terms with
  P0 = upper-left start, P2 = lower-right tip, pull P1 toward the
  lower-left of the P0→P2 chord (e.g., P0=(95,55), P2=(245,245),
  P1=(125,195) at 300×300). The hook flick is ~40 px long, angled
  roughly -110° to -120° in image coords (up-and-slightly-left), and
  tapers to a sharp tip. A ruler-straight primary reads as 撇 or 斜, not
  斜钩.
- 卧钩 (lying hook, as in 心/必): primary is a shallow "smile" arc —
  concave-up body dipping down from upper-left toward lower-right;
  hook flicks up-and-left (~NW, ~145°) from the right endpoint. Body
  should be noticeably shallower than 弯钩; the belly of the smile is
  the visual anchor.
- The hook itself tapers sharply into its tip (start width ≈ end-of-
  primary width, end width ≈ 1–2 px).

## Compound "turn" strokes (横撇, 横折, 横钩, 竖折, ...)

Two-segment strokes with a hard corner share a template:

1. Draw primary segment (usually 横 or 竖) with normal uniform width.
2. At the joint, drop ONE slightly-larger dab (~ r + 2..3 px) — this
   is the visible 顿 press that gives the corner its calligraphic
   weight and cleanly hides the seam between segments.
3. Draw secondary segment starting at the joint with r_start ≈ joint
   dab radius, tapering to whatever the tail requires (sharp tip for
   撇/钩, uniform for 折, thick for 捺).

Aesthetic tip: for 横撇 specifically, give the 撇 tail a gentle bow
(quadratic Bezier with control point pulled toward the primary's
direction) rather than a straight diagonal — a ruler-straight tail
reads as 横斜, not 横撇.

## 折 (zhe) corner family — general shape rules

A 折 is a sharp ~90° change of direction inside a single stroke. Rules
that generalize across 横折 / 竖折 / 横折钩 / 竖折折钩:

- The corner is not a smooth arc — it is a squared "shoulder": the ink
  presses briefly (slight thickening) just before the turn, then
  restarts in the new direction. In brush-dab code this is one
  slightly-larger dab at the corner point.
- The primary segment's end radius should ramp *up* slightly toward
  the corner (opposite of a taper) to visualise the press.
- The secondary segment starts at ~ the same radius as the shoulder,
  then holds roughly uniform (or tapers if the stroke ends in a hook /
  point).
- Distinguish 横折 (no bottom flick) from 横折钩 (upward-left flick at
  the bottom endpoint of the vertical). 横折 ends in a blunt press only.
- The 横 in 横折 conventionally tilts up 3–5° (same as a standalone 横).
  The 竖 drops straight down, not slanted.

## 弯 (wan) family — smooth arc vs 折 shoulder

Distinguish 竖弯 / 横弯-style strokes from 竖折 / 横折:

- 弯 (wan) = the direction change is a SMOOTH quarter-arc (tangent-
  continuous). No press dab at the transition; radius stays uniform
  through the curve. In dab code: parameterize the quarter-arc as
  `x = cx - R*cos(t*pi/2), y = cy + R*sin(t*pi/2)` for a
  vertical→right-horizontal 竖弯 (R ~ 30–45 px works at 300×300).
- 折 (zhe) = sharp shouldered corner with one slightly-larger 顿 dab
  at the joint (see the 折 section above).
- 竖弯 specifically: vertical descends, arcs cleanly into a horizontal
  running rightward, ends with a small terminal press (blunt round end,
  no upward flick — that would make it 竖弯钩).

## 撇点 / 撇折 family — 撇 followed by a second segment

Compound strokes whose primary is a 撇 (throw-away) followed by a
second beat share this structure:

- Primary 撇: upper-right start → lower-left tip, thick→thin taper,
  gentle rightward bow (quadratic Bezier control point pulled toward
  the primary's interior/right). 顿笔 dab at the start.
- **The two beats SHARE A JOINT.** The second segment's start point
  must coincide with (or overlap by one dab-radius) the 撇's tip.
  Drop one joining 顿-dab at the joint (~ local radius + 2 px) to
  hide the seam. A whitespace gap between the two beats reads as
  two independent strokes, not as a compound stroke.
- 撇点 specifically: second segment is a short 反捺-style dot going
  down-and-right at ~30–45°, thin→thick, length ~60–80 px, ending in
  a broad terminal press (~10 px radius). Starts AT the 撇 tip.
- 撇折: second segment starts at the 撇 tip with a 折 shoulder dab,
  then either a short 提 rising up-and-right (thick→thin, sharp tip)
  OR a short 横 going rightward with slight upward tilt and a small
  terminal press. When the brief's text mentions 横, render as
  折-shoulder + 横; when it says 提 or "rising", render as the
  taper-tip 提 form. Trust the brief over prior memory when they
  disagree.

## 折提 family — 折 with a rising tail instead of a plain vertical

Strokes like 横折提 / 竖折提 have three beats: primary, 折 shoulder, then
a **提 (rising)** tail springing off the end of the 折's secondary
segment. Rules that generalize:

- The middle segment (the 竖 in 横折提, the 横 in 竖折提) is
  **noticeably shorter** than in the plain 折 version, because room must
  be left for the 提 to rise into. Rule of thumb: middle segment ~40-60%
  the length it would take in a plain 横折 / 竖折.
- The 提 attaches at the end of the middle segment with a small joining
  顿 dab (~ r + 2 px) to hide the seam, then tapers thick→thin to a
  sharp tip at ~25-35° above horizontal.
- Middle segment may lean slightly inward toward the direction the 提
  will rise (in 横折提, the short 竖 leans slightly left because the 提
  will spring up-and-right — this is characteristic, not a bug).

## KEY PRIMITIVE — tangent-continuous vertical→horizontal arc

**Use this parametrization whenever a downward-going 竖 must curve
smoothly into a rightward-going 横 (i.e. for 弯 turns).** Proven on
横折弯钩 and 乚. Hand-computed arc centers with `theta = pi` /
`theta = 3pi/2` produced disconnected geometry.

```
# starting at end-of-竖 (x0, y0), arc of radius R sweeping into a
# rightward horizontal.  At t=0 tangent is (0,+) matching downward
# motion; at t=1 tangent is (+,0) matching rightward motion.
for i in range(steps+1):
    t = i / steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, r)
# arc ends at (x0 + R, y0 + R) — chain the next segment from THAT
# endpoint, do NOT compute it independently.
```

Symmetric variant (verified in 乚):
- descending-vertical → LEFTWARD-horizontal (rare):
    `x = x0 - R*(1 - cos(t*pi/2)), y = y0 + R*sin(t*pi/2)`.

**Rule**: never compute the arc endpoint and the next-segment start
point independently. Always drive one from the other.

The **mirror** (belly-on-right arc opening LEFTWARD) is UNPROVEN.
Any item whose canonical shape requires belly-on-right must validate
the mirrored parametrization on a simple synthetic curve first.

## Beat-count rule for 折-family compound strokes

    beats = 1 (primary) + number of 折 characters in the label
    shoulder dabs = number of 折 characters

| label       | beats | shoulders | terminal      |
|-------------|-------|-----------|---------------|
| 横折        | 2     | 1         | 竖 blunt      |
| 横折钩      | 2 + flick | 1     | 竖 with hook  |
| 横折折      | **3** | **2**     | 横 blunt (NOT a second 竖!) |
| 横折折撇    | 3 + tail | 2      | long bowed 撇 |
| 横折折折    | 4     | 3         | 竖 blunt      |
| 横折折折钩  | 4 + flick | 3     | 竖 with hook  |
| 竖折折      | 3     | 2         | 竖 blunt      |
| 竖折折钩    | 3 + flick | 2     | 竖 with hook  |

**Direction alternation**: after each 折, direction alternates
(horizontal ↔ vertical). Starting from a 横, beat 1 is horizontal,
beat 2 is vertical, beat 3 is horizontal, beat 4 is vertical, …
Starting from a 竖, invert.

Any trailing 钩 / 提 / 撇 is a FLICK on the final beat, not itself a
beat for shoulder-counting.

## Segment-length hierarchy for zigzag-plus-hook strokes

In a multi-fold stroke that ends in a 钩, the segment lengths are
NOT uniform:

- **Top / opening beat**: longest of the horizontal beats.
- **Retrograde middle 横**: SHORT (≤ 40% the length of the top 横).
- **Terminal beat (the one carrying the hook)**: LONGEST overall — its
  length gives the hook its swing.
- **Hook flick**: ~1/3 to 1/2 the terminal beat's length, angled
  -135° to -150° (up-and-left) for down-flowing strokes.

Also: the terminal 竖 usually LEANS slightly toward the retrograde
direction. This lean is characteristic, not a bug.

## Standalone vs compound-stroke — scale-up discipline

Recipes proven inside compound strokes do NOT transfer verbatim to
standalone rendering. Standalone items fill the entire 300×300
canvas, which magnifies subtle defects:

- **Curvature must be more pronounced.** Bezier control points pulled
  ≥45 px off the chord midpoint (vs ~30 px inside compound strokes).
- **Start-press must be smaller relative to canvas.** A r=12 顿 dab
  that looks correct inside a character reads as a comma-head balloon
  on a standalone. Use r=6–8 for standalones.
- **Terminal flicks / hooks must be longer.** Scale to ~1/3 of the
  primary's length; consider a gentle bow (Bezier) rather than a
  straight line.
- **Proportions matter more.** A standalone must feel balanced within
  its own frame.

### No visible 顿-dab "balls" at standalone endpoints

The r+2 顿 dab at endpoints is calibrated for stroke-scale (~150 px
strokes inside a character). On a standalone at 300×300, r+2 becomes
a visible ball/tumor. For standalone endpoints that simply TERMINATE
(no shoulder, no hook), use plain radius or r+1 (very subtle). Only
use r+2 or larger at CORNERS with real 折 shoulders, at starts of
primary strokes, or at visually "loaded" beginnings like the 顿笔
of 横 / 竖.

### "Move the knob further than intuition suggests"

When a first attempt fails on a proportion/angle/length knob, the
retry should move that knob **1.5× to 2× further** than the initial
"corrected" attempt. Standalone-scale magnifies subtle defects;
subtle fixes remain subtle failures.

---

## Batch-1 mastery ledger (Phase-1 strokes 1–19)

Rendered on 300×300 white canvas, black ink, PIL brush-dab technique.
Coordinates in image-coords (y grows DOWN).

| item | verdict | proven parameters (300×300 canvas) |
|------|---------|------------------------------------|
| 横 (heng)   | PASS | left→right, uniform r≈5, small 顿-dab (r+2) at start & end |
| 竖 (shu)    | PASS | top→bottom, uniform r≈5, 顿-dab (r+2) at start & end |
| 撇 (pie)    | PASS | Bezier P0=(215,70)→P2=(95,210), ctrl=(185,115); r 10→1.5; 顿 dab r=12 at start |
| 捺 (na)     | PASS | thin→thick, ends in broad flat foot (terminal press) |
| 点 (dian)   | PASS | short teardrop, thin→thick, ~30–50 px long |
| 提 (ti)     | PASS | rising ~25–35°, thick→thin, sharp tip |
| 弯钩        | PASS | smooth arc primary (top starts slightly right), hook flicks up-left from bottom |
| 卧钩        | PASS | shallow "smile" arc concave-up, hook flicks NW (~145°) from right end; body shallower than 弯钩 |
| 横撇        | PASS | 横 then gently-bowed 撇 tail (Bezier, not ruler-straight) |
| 横钩        | PASS | 横 primary, hook flicks down-and-left from right end |
| 横折        | PASS | 横 (slight up-tilt) + shoulder-dab + 竖 straight down; blunt end (no flick) |
| 竖提        | PASS | 竖 + joining dab + 提 rising up-right |
| 竖弯        | PASS | 竖 arcs SMOOTHLY into rightward 横 (no shoulder dab); quarter-arc R≈30–45 px; blunt terminal press |
| 竖钩        | PASS | straight 竖 + hook flicks up-and-left from bottom |
| 竖折        | PASS | 竖 + shoulder-dab + 横 rightward; blunt end |
| 斜钩        | PASS | Bezier P0=(95,55)→P2=(245,245), ctrl=(125,195) — belly on lower-left; hook flick ~-110° |
| 撇折        | PASS | 撇 primary + shoulder-dab at tip + short 横 rightward with slight up-tilt + terminal press. Params: 撇 P0=(210,60)→P2=(95,175) ctrl=(185,130); 横 end=(215,167) |
| 横斜钩      | PASS | short 横 (55,70)→(155,62) + shoulder dab + 斜钩 Bezier to (255,240) ctrl=(170,200) belly lower-left + hook flick length 40, angle -110° |
| 橫折提      | PASS | 横 (55,105)→(215,92) + shoulder-dab + SHORT 竖 to (207,168) + joining-dab + 提 to (270,122); middle 竖 shorter than in plain 横折 |

## Batch B1 phase-2 radical PASSes (35 items, positions 51–100)

Human-PASSed radicals from batch B1 — recorded as coverage evidence,
not as parameter recipes. Common denominator: silhouette + stroke count
correct + all named primitives present. Where a general rule was
freshly-relevant, cross-reference is given.

- **Bracket-family** (匚 匸 冂 凵 冖): PASS with shared-corner joints
  (bootstrap principle 2). Horizontal + vertical share the corner
  pixel; small 顿 at that pixel; no inset.
- **Compound-with-hook** (几 卩 亻 又 廴 辶 尸 饣 犭 门): PASS.
  The hook is drawn as an explicit final beat (new principle 5). 亻
  is the plain 撇+竖 pair — no hook, taper only.
- **Cross-based** (十 大 干 工 廾 艹 士 寸 扌): PASS. Cross/plus
  primitives with correct length ratios (new principle 6 — top vs
  bottom 横 lengths matter for 士/土/干).
- **Two-dot-style** (丷 亠 彡): PASS. Pairs of small teardrop 点
  with correct opposite slants.
- **Complex compound** (卩 屮 彳 川 女 山 彐 口 宀 㔾 讠 又): PASS.
  Two-to-four primitives combined with shared joints where the label
  requires them.

**Renderer**: PIL brush-dabs across the board. `turtle` not used in B1.

## B6 emergent principle (position 388): Sibling bits apply at COMPONENT level, not just standalone

B6 fails 仕 (亻+士 → 亻+工), 去 (士+厶 with equal-length 横), and 比 LEFT (匕→七)
share a single root: sibling_signature_checklist rows were designed for the
STANDALONE character (匕, 士, 己 as whole targets) but the drawer treated
them as "not applicable" when the sibling-risk radical appeared as a COMPONENT
in a compound character. It is applicable. Rule:

> If your compound character contains a component whose bare form appears on
> sibling_signature_checklist (e.g. 士, 土, 匕, 七, 己, 已, 巳, 人, 入, 未,
> 末, 木, 大, 尸, 户, 贝, 见, 未, 木), apply that row's signature bit to the
> component sub-glyph, not just to standalone renders. Length ratios
> (士's top-longer, 干's bottom-longer, 未's top-shorter, 末's top-longer)
> must be visibly decisive INSIDE the compound too.

For repeated-radical compounds (比 = 匕+匕, 从 = 人+人, 品 = 口+口+口, 森 = 木×3,
林 = 木+木), the row must be applied ONCE PER OCCURRENCE. B6 比 retry_1
applied it to the RIGHT 匕 only and got the LEFT wrong.

## Batch B2 phase-2 radical PASSes (20 items, positions 101–150)

Human-PASSed radicals from batch B2 curated at position 168. Recorded
as coverage evidence, not as parameter recipes. Where each item
contributed to `form_catalog.md`, cross-reference is inline.

- **Water/thread strokes** (氵 纟): both PASS. 氵 = 3 dots with
  bottom-dot-as-提 signature (see form_catalog "点 as 氵").
- **Boxes & body-through-竖** (囗 土 兀 子): PASS. Straight box +
  through-going 竖. Cross-ref form_catalog "竖 as through-going axis"
  and "left-wall of a box".
- **Compact upper radicals** (巳 小 弋): PASS. Silhouette-first
  worked; 巳's middle 横 correctly attached at TOP-left signature
  differentiating from 己/已 (form_catalog sibling table).
- **Bottom-splay & multi-dot** (灬 歹 斗): PASS. 灬 alternating outer
  splay of 4 legs (form_catalog "点 as 灬"). 斗 = 冫-left + 十-right
  composite. 歹 = 一 + 夕-like body.
- **Cross-based** (毛 木 手): PASS. Central 竖 through, top-vs-bottom
  横 length rules preserved. 手 has a top 撇 lid (form_catalog "撇
  as top-lid").
- **Wind-cluster & compound** (气 欠 犬 日 殳): PASS. 气 = 一 top +
  乞-body; 欠 = 撇+横钩 top + 人-body; 犬 = 大 + 点 upper-right (sibling
  table entry); 日 = box with single internal 横 (form_catalog "横
  as internal cross-bar"); 殳 = 几-like top + 又-body.

Common denominator across the 20 PASSes: silhouette + component count
correct + one signature bit per sibling-pair-risk item. This is the
first batch where the silhouette-first approach was applied
retroactively, and the form_catalog entries above were seeded from
what worked here.

---

## Batch-2 mastery ledger (Phase-1 strokes 20–32)

Same 300×300, PIL brush-dab technique. Coordinates in image-coords
(y grows DOWN).

| item | verdict | proven parameters |
|------|---------|-------------------|
| 横折钩 | PASS | 横 (55,100)→(220,88), shoulder r+3 at (220,88), 竖 to (208,235), hook (208,235)→(168,205) taper r=6→1.2 |
| 横折弯钩 | PASS | Short 横 (70,80)→(185,72), shoulder, short 竖 to (185,155), **tangent-continuous arc** (see KEY PRIMITIVE) R=32 landing at (217,187), short rightward 横 to (240,187), hook 55 px @ -115° taper r+0.5→1.2 |
| 竖折撇 | PASS | 竖 (130,55)→(130,175), shoulder r+3, short rightward 横 to (190,173), Bezier 撇 P0=(190,173)→P2=(65,260) ctrl=(175,220) r=7→1.2 |
| 竖折折 | PASS | 竖 (110,70)→(110,165), shoulder, 横 to (220,160), shoulder, 竖 to (220,250), blunt end (r+2) |
| 横折折撇 | PASS | 横 (70,78)→(170,70), shoulder, short down-left slant to (135,120), shoulder, short rightward 横 to (200,118), then LONG bowed 撇 Bezier P0=(200,118)→P2=(70,250) ctrl=(185,190) r=8→1.2. Key: zigzag body kept short so the final 撇 dominates. |
| 横折折折 | PASS | 4 alternating beats (横 竖 横 竖) with 3 shoulder dabs, blunt terminal press. Anchors (55,90)-(215,82)-(207,140)-(265,132)-(257,235) |
| 竖折折钩 | PASS | 3 body beats (竖-横-竖) with 2 shoulder dabs, hook flicks up-left @ -135° from bottom endpoint, taper r=5→1 |
| 丨 | PASS | Straight uniform vertical, x=150 y=45→255, r=5 uniform, 顿 r+2 both ends |
| 亅 | PASS | Straight 竖 x=150 y=55→225 r=5.5, hook 34 px @ -140° from bottom, taper r+1→1 |
| 一 | PASS | Uniform horizontal y=150 x=45→255 r=5, 顿 r+2 both ends |
| 乙 | PASS | 4-beat Z: 横 (75,80)→(200,72) + shoulder + bowed 撇-Bezier to (95,210) ctrl=(175,140) + concave-up arc center (165,195) R=75 from 168°→12° + hook 32 px @ -125° |
| 乚 | PASS | 竖 (130,70)→(130,170) + smooth arc center (170,170) R=40 parameterized `x=cx-R*cos(t*pi/2), y=cy+R*sin(t*pi/2)` + 横 to (240,210) + hook to (218,172) taper r+2→1.2 |
| 丶 | PASS | Teardrop dot (135,130)→(175,175), r=2→11 with easing `tt=t**1.4`, terminal press r+1 |

## Position 500 (B9 curator) — Calligraphic weight is the A-lift signal

B9 produced G2's first-ever A verdicts: 你 (亻+尔) and 没 (氵+殳).
Both are compound characters that would have passed as bare PASSes on
signature alone. What lifted them to A was consistent application of
**calligraphic weight-shaping** across every stroke, not any new
structural knowledge. The pattern is small and copyable — add these
four moves to any 5+-stroke compound render:

1. **Teardrop taper** — every 撇, 捺, 点 uses width array or `easing`
   parameter so ink starts thin, peaks mid-stroke, and either tapers
   to 1.2 px (撇/point) or presses to a heavy 顿 (捺 tail, 点 head).
   Straight-line uniform-radius strokes read as "computer draft," not
   handwriting. 你's 亻-撇 used `[5.0, 4.8, 4.3, 3.5, 1.8]`;
   没's 氵 used a `teardrop(easing=1.4)` helper.
2. **Shoulder dab at every 折 joint** — a single extra `d.ellipse`
   ~1.3× stroke radius at the corner, applied BEFORE the second
   segment starts. This is the ink-pool a real brush leaves when it
   pauses to change direction. 没's 殳 roof-shoulder used r=5.8 at
   the 横→竖 corner; 你's 尔 roof used r+2 top dab.
3. **Bezier for any curved sweep** — 撇 (bowed), 捺 (S-curve),
   横撇 (hooked pie), 竖弯钩 (arc). Straight-line 撇 is a fail-mode
   signature; bowed 撇 is A-quality. Use quadratic Bezier with the
   control point pulled OUT from the straight line by ~15-25 px.
4. **Correct hook flick direction** (TIER-0 rule, retained) — UP-and-
   LEFT, never straight up or down. Both A's got this right on their
   central 亅 (你's 尔-亅, 没 has no hook but 殳-arc terminates cleanly).

These four moves are orthogonal to structural knowledge — you can
apply them on top of any correct signature. They do NOT help a wrong
signature pass. They lift a correct signature from PASS to A.

**Why this is worth remembering even under pos-438 memory-invariance**:
The pos-438 anti-goal was about not adding STRUCTURAL knowledge in
hopes of raising pass rate. Calligraphic-weight is an orthogonal
QUALITY axis — it does not affect pass rate (a wrong signature still
fails, a right signature still passes). It affects the ceiling of
whether a passing render also earns A. Adding this note therefore
does not falsify the retrieval-ceiling claim; it documents a NEW
quality ceiling on top of it.

**Retrieval concern**: if this section is not retrieved by B10
drawers on their compound-character targets, the 0-A rate resumes and
this note joins the "known but unretrieved" pile the pos-438
retrieval-ceiling claim describes. B9's two As came from drawers who
retrieved teardrop-taper + shoulder-dab + Bezier by default (see 你
and 没 generated.py comments), NOT because those techniques were
newly instructed. So this section is descriptive of what already
works when drawers do it, not prescriptive to make them do it.

## Position 550 (B10 curator) — A signal replicates + 疒-drift + C-band diagnosis

B10: 10 PASS + **2 A** + 8 C + 32 FAIL = **20% main-pass** (down 4pp
from B9 but with 2 A holding — the A signal replicated). New "C"
verdict introduced v12 caught 8 close-but-not-exact renders that
previously would have been buried inside the FAIL bucket. Diagnosing
the C band exposed two orthogonal patterns worth documenting:

### 1. C-band is dominated by "signature intact, but calligraphic-flat"

Six of the 8 C's had the correct component parts in the correct
positions but were drawn as **uniform-radius straight-line polylines
with detached components**. Look at the C fingerprint:

- 别 (口+另+刂): 口 as a square, 力 hook missing, 刂 as two ruler-
  straight verticals. No taper, no shoulder dab.
- 佚 (亻+失): correct pieces but 亻 stretched to full canvas height,
  no taper on 撇, 失 top-一 missing.
- 盯 (目+丁): 目 clean but 丁 sits ~50 px right of 目 with a huge
  white gap; 丁 stem is uniform-radius.
- 的 (白+勺): 勺 rendered as a loose oval loop instead of 撇+横折钩+丶
  — the hook direction and interior 丶 are absent even though the
  wrap outline is present.
- 甾 (巛+田): components present and positioned correctly — CBV
  candidate. Signature intact.
- 疚 (疒+久): 疒 outer signature present + 久 recognizable, but ~10 px
  detachment between components. CBV.
- 法 (氵+去): 氵 drawn as three separate 丶 dots — the **bottom dot
  should be a 提 (rising)**, not a plain dot. 去 clean.
- 疝 (疒+山): 疒 outer collapsed to 广+丶 (missing the inner 冫), 山
  present. Borderline.

**Rule of thumb** (B10 evidence): When the C-band drawer knows the
structure but ships a flat render, applying the pos-500 four-move
(teardrop + shoulder dab + Bezier + hook flick) would likely lift 3-4
of these 8 to PASS. So calligraphic-weight is not just an A-lift — it
is also a **C→PASS lift** when the underlying signature is correct.

### 2. 氵 water-radical bottom stroke is a 提, not a plain 丶

Explicit reminder because 法's C verdict was cleanly attributable:
**氵 = 丶 + 丶 + 提**. The bottom mark rises up-and-right thick→thin
with a sharp tip, angled ~25-35° above horizontal — NOT a downward
teardrop like the top two. Failing this reads the radical as three
generic dots stacked (which is what 法's B10 render produced). B2's
form_catalog "点 as 氵" entry names this; the drawer did not retrieve
it. Adding here as a redundant surface.

### 3. 疒 sickness-radical body is 5 strokes, not 3

Three fresh FAILs — 疙, 疟, 疠 — all rendered 疒 as if it were 广
(丶 + 一 + 丿, three strokes). The **inner 冫 pair (丶 + 提) on the
upper-left inside the wedge is a required identity bit**. Missing it
reads as 广+X. See form_catalog.md new "疒 as compound-left-wrap"
entry (B10 addition). This joins the B7 疔 fail (same mode); 疒 is now
attested-3x-failed and the entry is warranted at form_catalog level.

### 4. Left+right compound spacing: pieces must touch or nearly touch

盯's C was primarily a **spacing failure** — the 目 and 丁 stood ~50
px apart with a large white gap between them. Left+right compounds
should be laid out with a gap of at most ~10-15 px between component
bounding boxes at 300×300. Same failure surface on B9's 员 and 听
(both got detachment fails). The rule to encode:

    left_box.right + gap ≤ right_box.left, gap ∈ [5, 15] px

If your left component ends at x=140 and your right component starts
at x=190, you have a visible gap. Compress.

### 5. What worked in B10's two A's

- **佘** (人-lid + 二 + 小 stack): drawer used quadratic Bezier for
  every 撇/捺, tapered widths on every stroke (11→5 for 撇, 5→13 for
  捺 with a foot flare), and the 小-center hook correctly flicked
  UP-and-LEFT. Silhouette wide, calligraphic feel present.
- **佧** (亻 + 卡): drawer used the polyline+disc-sample technique
  (draw dense discs at ~1 px spacing), taper=True on 撇, correct
  proportions with tight left-right spacing (~30 px between 亻 tail
  and 卡 left edge). No fancy Bezier — just clean taper.

Both A drawers had explicit stroke-list docstrings at the top of
generated.py naming every stroke's role. This planning-front-load
pattern seems to correlate with A verdicts across B9+B10 (n=4).

### B10 fail-mode composition (n=32 FAIL, curator vision)

- **5 亻-compound-drift**: 佔, 佗, 佛, 佞, 佟 — down from B9's 12,
  down from B8's 17. Item-mix rotating off 亻-compounds; B10
  concentrated more on 疒-compounds (5 items: 疙, 疟, 疠, 疌, 疝-C)
  and misc rare (乶, 疌).
- **3 疒-compound-drift** (NEW as a top-3 mode this batch): 疙 (乞
  right collapsed), 疟 (虐 fragment), 疠 (万 disintegrated). Two more
  疒 items (疚 C, 疝 C) came close. See point 3 above.
- **6 sibling-bit failures**: 张 (弓/引), 佥 (∧+一+从 collapsed),
  找 (戈-hook, FROZEN 戈 dup), 步 (止/少 stack length ratios), 每
  (母 signature), 定 (疋 body vs 元/兄).
- **5 radical-body fragmentation**: 事 (multi-fold + central 亅), 乖
  (千+北 fusion), 学 (子-hook missing), 其 (八+甘 stack), 並 (5-stack).
- **4 composition/detachment/spacing**: 志 (士+心 stack), 到 (至+刂
  spacing), 畅 (申+昜 stack), 所 (户+斤 spacing).
- **4 duplicates-of-FROZEN**: 找 (戈 dup), 改 (己 dup), 即 (卩 dup),
  经 (纟 dup).
- **3 讠/礻 left-radical drift**: 证 (讠 dup), 社 (礻+土), 佛 (亻+弗
  actually 亻-compound too).
- **2 rare/traditional**: 乶 (rare Korean-loan), 疌.
- **NEW mechanisms**: 0. All 32 fits documented modes.

**CBV density**: 8 C's caught what would previously have been "close"
FAILs. Two (甾, 疚) are strong CBV candidates by signature-intact
standard; the other six are signature-intact-but-flat, argued above
as a calligraphic-weight lift target.

## Position 600 (B11 curator) — the 0-A regression + retrieval-ceiling holds n=5

B11: 8 PASS + **0 A** + 7 C + 35 FAIL = **16% main-pass** (down 4pp
from B10's 20%, down 8pp from B9's 24%). Third consecutive decline.
The A signal from B9 (n=2) + B10 (n=2) did NOT replicate — first
zero-A batch since A first appeared. The C-band held at 7 (vs 8 in
B10) with a nearly identical fingerprint. Combined: this is a
**calligraphic-weight-technique retrieval regression**, not a new
failure mode. Diagnosis follows.

### 1. Why 0 A this batch — the recipe was in memory but not retrieved

Every C item in B11 is drawn with the exact anti-pattern pos-500
warns against: **uniform-radius straight-line polylines**.

Audit of the 7 C items' `generated.py` files:

| item | technique | verdict-cause |
|------|-----------|---------------|
| 佬 (亻+老) | `d.line(pts, width=6)` throughout; no ellipse-taper, no Bezier | signature intact but 亻 竖 detached from 撇, 耂 长撇 uniform stick |
| 佶 (亻+吉) | `d.line(pts, width=8)` polylines; 亻 竖 begins mid-撇 as separate call | 口 rendered as sharp rectangle; no shoulder dab at any 折 |
| 佼 (亻+交) | uniform width, no dabs, no Bezier | 亻 竖 disconnected from 撇 apex; 交 top-lid missing 亠's crossing |
| 佾 (亻+八+月) | uniform width | 亻 竖 detached; 八 present; 月 rendered as bare rectangle (no shoulder dab, no hook flick) |
| 采 (爫+木) | uniform width, cap-only ellipses | 爫 as three raw sticks; 木 as ×-cross without 撇/捺 taper |
| 知 (矢+口) | uniform width | 矢 top-一 detached from 大; 口 as sharp rectangle |
| 说 (讠+兑) | uniform width | 讠 as detached fragments; 兑 rendered with 冂 body + hook straight-down (FROZEN hook-flick dup) |

Compare the B10 A recipe (佘) which used variable-width brush-dabs
(`stroke(pts, widths=(11, 5))`), quadratic Bezier for every 撇/捺,
foot-flare on the 捺 tail, and correct hook-flick — every one of the
four pos-500 moves. B11 drawers uniformly reverted to
`d.line(pts, width=6)` for the entire glyph. **The A-recipe knowledge
is present in this memory file (pos-500 + pos-550 point 5) but was
not retrieved by any B11 drawer.**

This is the pos-438 retrieval-ceiling pattern reappearing on a NEW
axis (quality, not pass-rate). Adding words did not induce retrieval;
now zero-A is the natural regression when a batch of drawers happens
to not retrieve the technique file. Same mechanism as the recurring-
signature FAILs.

### 2. Main-pass rate: 24→20→16% is item-mix + still-no-retrieval

B11 curriculum shifted BACK to heavy 亻-compounds (14 亻-items:
佬, 佯, 佰, 佴, 佻, 佽, 侃, 例, 侉, 侖, 佾, 佶, 侌, 佼, 侍, 侔, 侑,
侈, 併). That's more than B9's 12 and B10's 5. Historical 亻-compound
pass-rate is ~4/12 (B9) → 1/5 (B10) → ~4/14 (B11, counting 佴, 佾-C,
佬-C, 佼-C, 佶-C, 侈, 侑, 併-F/PASS). Adding to that: 3 讠-compounds
(话 F, 说 C, 转 F), 3 田-compounds (畈 F, 畋 F, 甾-history), 4 疒-
family carryover fear (none actually appeared this batch — 疒 out).

Same fail-mode composition breakdown (n=35 FAIL + 7 C = 42 non-PASS,
curator vision):

- **12 亻-compound-drift** (up sharply from B10's 5): 佯, 佰, 佻, 佽,
  侃, 例, 侉, 侖, 侌, 侍, 侔, 併 — same mechanism as B7/B8/B9. Right
  component semantically wrong or fragmented; 亻 itself mostly clean.
- **4 亻-compound C-band** (signature intact but flat): 佬, 佶, 佼,
  佾 — see table above. Pos-500 4-move would likely lift 2-3.
- **5 讠-family drift**: 话, 说 (C), 转, 线, 规 — 讠 rendered as
  detached sticks (FROZEN 讠 dup, on the frozen-cohort list).
- **4 sibling / body-signature loss**: 亟, 表, 实, 或 — inner
  signature collapsed. 亟's central-鱼 core lost; 表's 衣 body missing
  bottom fan; 实 (宀+头) fragmented; 或's 戈 hook missing (FROZEN 戈).
- **3 radical-body fragmentation**: 疡 (疒+昜, 疒 as 广 dup B10), 亞
  (double-口 stack lost), 亟 (multi-part fusion).
- **3 田-family**: 畈, 畋 — 田 clean but 反/攵 fragmented into sticks.
- **4 LR-spacing / detachment**: 取 (耳+又 gap), 放 (方+攵 detached),
  转 (车+云 gap), 例 (亻+列 spacing). Dup B10 pos-550 point 4.
- **3 stack-fusion loss**: 空 (穴+工 gap), 单 (⺍+田+十 collapse),
  受 (爫+冖+又 detached ladder).
- **2 rare/traditional**: 侖 (traditional 仑), 來 (traditional 来).
- **2 采/知-family sibling**: 采 (C, 爫+木 flat), 知 (C, 矢+口 flat).
- **重复 FROZEN modes** (attested across ≥3 batches now — memory
  guidance did not transfer):
    - 讠 family: B7 记, B10 证, B11 话/说/转/线/规. attested-5x-failed.
    - 戈 hook: B7 代, B8 伐, B9 我, B10 找, B11 或. attested-5x-failed.
    - 匕/兑 hook: B6/B7/B10, B11 说. attested-continuing.
    - 攵/攴 splay: B7, B10 改, B11 放/畋/畈. attested-3x-failed.

Additions to the frozen-cohort file (`frozen_cohort.md`) proposed
below at point 5.

### 3. Publishable-finding update — retrieval-ceiling n=5

Pos-438 retrieval-ceiling claim now attested across 5 consecutive
batches: B7 (39%), B8 (~30%), B9 (24%), B10 (20%), B11 (16%). Not
just held — **declining**. The declining trend cannot be blamed on
one confound: item-mix rotates, technique memory grows, protocol
holds (memory-invariance from pos-438). What remains constant is
that ~70% of failures are documented modes the drawer did not
retrieve. Adding memory content does not fix retrieval; if anything,
the growing file footprint (~4400 lines / ~280 KB now) further
depresses per-item retrieval likelihood.

**The extended finding G2 now supports at n=5**:

"In a free-form-markdown memory architecture with a curator that
accumulates diagnosis + technique memory monotonically across
batches, the fraction of documented-but-unretrieved failure modes
per batch grows superlinearly with memory footprint. The main-pass
ceiling (~40% at pos 438) has decayed to 16% at ~4400 lines. A
distinct A-quality ceiling (rare, ~0-2/50 batches) is entirely
retrieval-gated on the same technique memory: when drawers happen
to retrieve calligraphic-weight moves the A appears; when they
don't (B11), A goes to zero. Neither ceiling has been raised by
adding memory content; both track the drawer's stochastic retrieval
of what is already documented."

This is a stronger claim than pos-438's original. Add this to the
paper draft.

### 4. What (small) memory change might help without falsifying the invariance claim

Under pos-438 memory-invariance, we do NOT add new structural
knowledge in hopes of raising pass-rate. But two RETRIEVAL-side
changes are still legitimate:

**a. Promote calligraphic-weight rule to TIER-0 in memory_index.md**
(structural change — reshape drawer's entry point, not add new
content). The B11 evidence is unambiguous: pos-500's 4-move recipe
buried at line 539 of drawer_memory.md was NOT retrieved by any of
7 C-band drawers. Moving a 6-line summary into memory_index.md's
TIER-0 puts it in front of the drawer before the first stroke is
planned. This is not adding content — the content exists at pos-500.
It is a retrieval-only refactor per v13 rules (see evolution.md
guidance).

**b. Add FROZEN-mode reminder to TIER-0** — the 5 讠 fails and 5 戈
fails in B11 are all in frozen_cohort.md but that file is not linked
from TIER-0. A single "if your target contains 讠, 戈, 攵, 匕, ⺈,
纟, 弓 — open frozen_cohort.md first" line would surface those
attested-multi-batch-failed radicals.

I will apply both changes below. Neither adds new content; both are
retrieval refactors.

### 5. Frozen-cohort additions (per point 2 above)

Update `frozen_cohort.md` to reflect the attested-count updates:
- 讠 family: attested-5x-failed now (was 4x)
- 戈 family: attested-5x-failed now (was 4x)
- 攵 family: attested-3x-failed now (was 2x)
- 亻-compound-drift as a MODE (not a single radical): attested every
  batch B6-B11. Not a single radical to freeze — it's an interaction
  problem with the right-side component. Note as "attested but not
  freezeable — it is a compound-composition mode".

### 6. What worked in B11's 8 PASSes

Sample check on 3 PASS items (果, 佴, 具) — all had:
- Silhouette planned before strokes (docstring names layout)
- Component-touching rather than component-detached
- 木 / 皿 / 具 kind of chars have simple stack structure that
  survives even uniform-width rendering
- 亻+compound 佴 succeeded because 耳 rendered fully (all 6 strokes)
  and beneath-line touching 亻 tail

None of the PASS items used calligraphic-weight technique either.
This confirms: pass-rate is signature-gated (which stack you produce),
A-rate is calligraphic-weight-gated. B11 drawers got signature right
often enough to hit 8 PASS but never got calligraphic weight → 0 A.

---

## B12 curator notes (pos ~650, 2026-08-04)

### 0. Headline

**Results**: 1A + 11 PASS + 11 C + 27 FAIL = **12/50 = 24%** — a
partial recovery from B11's 16% dip. Confirms B11 was sample-noise
against a stable ~20-30% ceiling, not a permanent regression. The A
returned (畎) after the pos-600 TIER-0.F promotion.

### 1. Follow-up on B11 — did the TIER-0.F promotion help?

**YES, on retrieval; NO on failure floor.** Retrieval is now
stabilizing:

- All 11 PASSes explicitly reference "TIER-0 F 4-move" or an
  equivalent phrase in the docstring. All use `bez()` + `stroke(pts,
  widths=(a,b))` helpers.
- All 11 C-band items also reference the recipe, but their component
  decomposition was wrong (structural fail beneath calligraphic
  weight). This is a *different* failure mode from B11's C-band
  (uniform width=6 lines) — the recipe is being pulled but its
  effect is masked by structural errors.
- 畎 (the A) is a near-clone of the 佘 template with `bez()` + tapered
  strokes + shoulder dab at 田's top-right corner. **Recipe was
  correctly retrieved AND correctly applied on a simple compound.**

**Retrieval-ceiling status**: promoted to "stabilized-stochastic."
The B11 hypothesis (recipe present but not pulled) is falsified for
B12 — recipe IS pulled ~100% of the time this batch. What remains
stochastic is *structural correctness of the component decomposition*,
which memory does not encode at the per-glyph level (would violate
invariance and G2's supplementary-memory spirit).

### 2. NEW cluster failure — 疒 (illness) radical, 7 fails in one batch

**Attested-7x in B12 alone**: 疣, 疤, 疥, 疫, 疬, 疭, 疮. This is the
single largest cluster failure this batch — 14% of the whole batch.

疒 decomposition (per GT observation):
- 点 top-left (short, above the 一)
- 横 top (long, spans radical width)
- 撇 long sweep from right-end-of-横 down to bottom-left (this is the
  identity-carrying 撇 — MUST be long, curved, and dominant)
- 点 inside upper-left of the canopy (below the 一, right of the 撇)
- 提 inside lower-left of the canopy (rising short flick, below the
  inner 点)

**Total: 5 strokes for 疒 alone**, then whatever body fits inside the
canopy (bottom-right, tucked under the 撇).

Common B12 failure modes on 疒:
1. Drew 疒 as `广` (missing the two inner 点+提 dots) → collapses to
   `广` + body, wrong signature.
2. Drew inner body OUTSIDE the canopy (bottom-right but not tucked
   inside the 撇 sweep) → looks like left-right compound, not a
   canopy character.
3. Drew 疒 with only 3 strokes (点 + 横 + 撇) — again missing the
   inner 点/提 pair.

See `frozen_cohort.md` for the new 疒-family alarm row.

### 3. 亻 compounds — moderating

B11 flagged 12 亻-compound-drift FAILs + 4 C. B12 has:
- FAIL: 侯, 便, 侷, 係, 俅, 俊 (6)
- C: 俎 (1)
- PASS: 信, 侶, 俉, 保 (4)

Same total exposure (11 items) but pass-rate moved from 0/16 (0%)
→ 4/11 (36%). What made the 4 PASS items work?
- 信 — 亻 竖 STARTS BELOW the 撇 apex (touching, not detached), and
  right-side 言 stack was drawn as continuous fused pieces.
- 保 — same pattern: 亻 attached, 木-body kept its 撇+捺 taper.
- 侶 / 俉 — right components (吕 / 吾) rendered as stacked-口 with
  shoulder dabs, no gaps between the top-口 and the bottom-口.

**Common denominator**: touching/fusion between 亻 and its right
component. Detached 亻 = FAIL. This wasn't captured explicitly before
— see new addition to `sibling_signature_checklist.md` below.

### 4. Rare + traditional items — same low-transfer story

- 面 (9 strokes, complex inner-fill) — FAIL, composition drift.
- 乹 (rare form) — FAIL.
- 亲 — FAIL, 立+木 stack fusion lost.
- 皴 (皲?) — the 皈 PASSed however (皮+反), suggests 皮-family with
  simple right components can pass; 反 was rendered as a splayed 又
  and still passed because canonical topology of the whole char is
  distinct enough.

### 5. What worked in B12's 12 successes

Sampled 6 PASSes (畐, 信, 给, 相, 保, 草) + 1 A (畎):
- 100% used the 4-move recipe (bez + variable width + shoulder dab).
- 100% cited TIER-0 F in docstring.
- 100% had components TOUCHING (no gaps between radical + body).
- 5/7 had explicit sibling-check in the docstring (相 checked 木,
  草 checked 艹, 信 checked 亻-attach).

**Emergent rule**: TIER-0 F alone is not the differentiator; TIER-0
F + component-touching + correct component-count is. Add
"components must touch" as a TIER-0-adjacent reminder.

### 6. Retrieval verdict — B12 status

Retrieval STABILIZED but did not raise the ceiling. Pass-rate stays
in the 16-40% band that has held since B4. What TIER-0.F did:
- Recovered A-quality potential (was 0 in B11, back to 1 in B12).
- Eliminated the "signature-intact-but-flat" C-band mode (0 such
  items in B12 vs 7 in B11).
- Did NOT reduce structural fails (still 27 in B12 vs 27 in B11).

The residual failure mode is now **component decomposition
correctness at the semantic level**, which is a knowledge gap G2's
free-form markdown can partially address (per-radical decomposition
recipes) but cannot exhaustively enumerate (10K+ Han glyphs, each
with idiosyncratic decomposition).

### 7. What (small) memory change this batch

Under memory-invariance, we do NOT add new structural knowledge to
raise the pass-rate ceiling. But B12 shows one clear high-transfer
opportunity that is *observation-driven*, not speculative:

**Add a 疒 canopy row to frozen_cohort.md** with the 5-stroke
decomposition above. This is documenting an already-attested failure
mode (7x in one batch is not speculative), and the fix hypothesis is
directly extracted from the GTs of the 7 failed items — not invented.

**Add "components must touch" as a hint in memory_index.md** as a
one-liner under TIER-0. This is not new knowledge (composition_rules.md
line references it obliquely), it is a retrieval-side surfacing.

Both changes applied below.


---

## B13 lessons (2026-08-05, pos ~700) — the 4% collapse

B13 landed 2/50 = 4%, worst batch of the experiment. Trajectory now:
B10 24% → B11 16% → B12 24% → B13 4%. This section documents the
verified failure modes and what the curator did in response.

### 1. 疒 fix hypothesis (added B12) is falsified

Curator inspected 5 of the 8 B13 疒-family generated.py files
(疰/疱/疳/疴/疸/疹/疽/痂). **All 5** implement the frozen_cohort.md
5-stroke decomposition:
- (1) top-left 点, (2) long 横, (3) long identity-carrying 撇,
  (4) inner 点 below 横, (5) 提 rising flick below inner 点.
- All 5 use bez() + stroke() helpers with tapers.
- All 5 tuck the body inside the 撇 sweep.

Result: 7 FAIL + 1 C (痂). The B12 recipe is topologically correct
but the resulting canopy STILL reads as `广` + extra-marks to a human
judge, not as 疒. Something about the visual gestalt is missing beyond
"5 strokes in the right topology". Possibly the inner 点+提 pair must
sit visibly INSIDE the wedge bounded by 横 (above) and 撇 (left); in
the B13 attempts they sit ambiguously alongside the 撇 stem. See
frozen_cohort.md updated 疒 row for this untested refinement.

**Practical drawer guidance**: applying the 5-stroke decomposition
is necessary but not proven sufficient. Do apply it, but shrink the
body ~20% and pack it fully under the 撇's belly. Also try placing
the inner 点 with x < 横's midpoint (well inside the canopy
triangle), and the 提 immediately below with the same x-range. This
is untested — no verified example yet.

### 2. NEW 辶/走-wrap-family cluster

B13 had 5 wrap-radical items (适/通/造/速/起). All FAIL. Common mode:
辶 rendered as a flat wave BESIDE the interior body. The 平捺 sweep
was present but did not carry the interior visually.

Correct topology (from GTs):
- Interior body sits in y ≈ 30..200.
- 辶's 平捺 starts to the LEFT of the interior body (~ x=30-50), at
  y ≈ 205-215.
- 平捺 sweeps rightward and slightly-down, then curves back UP at
  its right end, terminating around x=270, y=230 with a foot-flare.
- Interior body's BOTTOM stroke must overlap (touch) the 平捺's
  starting arc so the interior visually rests ON the 捺.

If your target has 辶 (or 走/廴): **draw the interior body FIRST**,
occupying the upper-right quadrant. THEN draw the 辶 wrap. Do NOT
place body and 辶 as left-right siblings.

### 3. NEW 田-body-with-rare-top cluster

B13 had 6 田-body items with rare tops: 畚 (龹), 畛 (㐱), 畜 (玄),
畝 (亠+攵), 畟 (dou+夂), 畢 (華). All FAIL. 田 itself is fine
(compare 田/由/町/畎 PASSes).

Guidance: for these, DO NOT try to name the top's structural class
from the label alone. Trace the GT PNG stroke-by-stroke and emit
each stroke as a separate call in GT order. Do not invent
decomposition semantics for unfamiliar radicals — trust the GT.

### 4. What the 2 PASSes had in common

- **俚** (亻+里): standard 亻-attached-to-body composition; the
  sibling_signature checklist row was applied verbatim (`SIGNATURE
  CHECK` block in docstring); 亻's 竖 starts within the 撇 body
  and touches 里's left column.
- **原** (厂+白+小): 厂 canopy correctly rendered with 一+丿 sharing
  the top-left corner (顿 dab at corner); 白 tucked directly under
  the 一, 小 centered below; 竖钩 with UP-and-LEFT flick; all
  components touch.

Common denominator: standard-composition characters with all
radicals in the pass-index precedent set (亻, 里, 厂, 白, 小,
竖钩 with correct flick). No rare-radical items in either PASS.

### 5. What did NOT work this batch

- 家 (C-band): 豕 body over-decomposed into 5 撇 (豕 = 短横 + 撇 +
  弯钩 + 3 short + 捺, not 5 straight 撇). Lesson: don't invent
  stroke sequences for compound bodies you haven't seen; use the
  GT PNG stroke count and match visually.
- 高 (C-band): overall structure OK but inner 口 missing bottom 一.
  Lesson: for characters with nested 口s, count 口 strokes as 3
  each (竖 + 横折 + 一).
- 响 (F): drawer used uniform d.line strokes without applying the
  4-move recipe — first recipe-regression in weeks. TIER-0 F is
  still not fully sticky.

### 6. Curriculum-difficulty note

B13 is a systematic difficulty spike vs B12. Rough counts:
- B12 rare-radical items: 疒×7 + 皮/皿-family + 面 + 乹 ≈ 12/50.
- B13 rare-radical items: 疒×8 + 辶×4 + 走×1 + 田-rare-top×6
  + rare 亻×5-7 + 乘/亳/丵 ≈ 26/50.

Half the batch was from rare/uncovered families. Even with
retrieval working well, the memory has no encoding for most of
these. This is the primary driver of the 24→4% drop.

### 7. What did NOT change

Not a structural memory reorganization. The 5900-line memory is
functional: retrieval works, TIER-0 F is stable, sibling checklist
transfers. The gap is knowledge coverage of rare radicals — which
markdown notes can capture but only after PASSes accrue for those
families.

### 8. Falsifiable B14 predictions

1. **Curriculum-driven hypothesis** (primary): if B14's rare-radical
   density drops back to <20% (approximately B12 level), G2 pass-rate
   rebounds to the 15-30% band. If B14 has similarly-high rare-radical
   density (>40%), pass-rate stays <10%.
2. **辶/走 hypothesis**: any 辶/走 items in B14 continue to fail at
   ~100% (0/N), UNLESS the drawer independently discovers the
   wrap-topology by looking at a PASS-index entry. G2 has only ONE
   past 辶-compound PASS (进 at B9); the newly-added frozen_cohort
   row + memory_index note may or may not surface it.
3. **疒 hypothesis**: any 疒 items in B14 continue to fail at 85%+.
   The 5-stroke decomposition alone does not transfer. IF a curator
   adds `p3_char_0530_痂` (the sole B13 C) as a canonical PASS-index-
   like example, and B14 has ≥3 疒 items, one might squeak to C or
   PASS. Otherwise all fail.
4. **Common-character hypothesis**: for common-frequency items in
   B14 (家/高/都-band), pass-rate stays in 40-60% band (unchanged
   from prior batches). The collapse is not a common-character
   regression — 家/高/特/部/都 in B13 mostly landed at C not FAIL,
   and 原 PASSed cleanly.

If B14 lands 4% again but the rare-radical density is <20%, the
diagnosis is wrong and we need to investigate a retrieval
regression instead.

