# Radical Position Rules

*Created 2026-07-18 @ position 168. Lightweight companion to
`form_catalog.md`. Where the catalog describes SPECIFIC strokes in
context, this file describes WHOLE-RADICAL layout rules — how
components sit against the 米字格 mental grid, and how the human
eye "reads" a radical's identity from silhouette.*

## The silhouette-first heuristic

Chinese radicals are recognized more from their **bounding-box
silhouette + component count** than from stroke-level detail. If
your render's silhouette is wrong, no amount of hook-detail rescues
it. Before drawing, decide:

1. What's the bounding-box aspect ratio? (tall-narrow, square,
   wide-flat, off-center)
2. What are the visual "planes" the eye sees? (top / body / base)
3. Where is the visual center of mass? (top-heavy, centered,
   bottom-heavy, left-leaning)

Only after these three are set should you place individual strokes.

## Aspect-ratio families

| family | examples | canvas fill |
|--------|----------|-------------|
| tall-narrow | 亻 彳 犭 忄 巾 中 | x-extent ~40%, y-extent ~85% |
| square | 口 日 田 目 囗 木 大 | x ~70%, y ~70% |
| wide-flat | 一 灬 冖 亠 冫 二 | x ~85%, y ~25% |
| off-center L | 厂 广 尸 户 卜 | 顶+左 filled, 右下 empty |
| off-center 匚 | 匚 匸 凵 冂 | 3-sided box, 1 side open |

Match your first-attempt bounding box to the family BEFORE drawing.
Getting this wrong is a fast track to a FAIL.

## Center-of-mass rules

- **Top-heavy** (户, 广, 尸, 亠, 立): the visual mass sits in the
  upper third; the tail/legs are lighter. Draw the top elements at
  full weight and let the legs taper or shorten.
- **Bottom-heavy** (山, 凵, 皿, 灬 as bottom): mass in the lower
  third. The top of the glyph should feel like it "sprouts" from
  a broad base.
- **Left-heavy** (辶, 廴, 阝-left): mass concentrated on the left,
  right side is a placeholder for the compound character's other
  half.
- **Centered** (口, 日, 田): symmetric around the middle vertical
  axis.

## The 米字格 mental grid (for G2 use only as an eyeball aid)

We are G2 (free-form). We do NOT use 米字格 anchors as machine-
readable coordinates. But we may use them as an EYEBALL AID during
the reflection step:

- Divide canvas into 3×3 = 9 cells. Top row, middle row, bottom
  row; left column, middle column, right column.
- For each named stroke in the target, ask "which cells does it
  START, PASS THROUGH, and END in?"
- Then verify your render matches.

Example: 士 top-横 starts in TOP-LEFT cell, passes through
TOP-MIDDLE, ends in TOP-RIGHT. Middle 竖 starts in TOP-MIDDLE,
passes through MIDDLE-MIDDLE, ends in BOTTOM-MIDDLE. Bottom 横
starts in BOTTOM-CENTER-LEFT, ends in BOTTOM-CENTER-RIGHT (not
touching bottom-left or bottom-right corner cells because 士's
bottom 横 is shorter than the top).

This is a mental check — nothing to write in code.

## Failure modes cross-indexed

- **"reads as sibling glyph"** (e.g. 匕→七, 士→土, 力→几):
  usually a silhouette/aspect-ratio or length-ratio error. Check
  `form_catalog.md` for the sibling pair signature.
- **"reads as two disconnected pieces"** (e.g. 门 with top gap,
  马 with floating bottom 横): joint/shared-corner failure. Adjacent
  named strokes should share their meeting pixel.
- **"reads as generic shape not a radical"** (e.g. 巛 → three
  curves, 彑 → 工): missing a signature detail — a hook, a
  chevron, or a folded body. Consult the label; every named part
  MUST render as its named form.
- **"reads as compressed / cramped"** (e.g. 巾 with short 竖):
  bounding box too small. Use the full canvas allocation for the
  aspect-ratio family.
