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
