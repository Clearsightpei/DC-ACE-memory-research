# Cycle 6 — 3 tasks (post-reset, hard gate)

## Phase
1 (foundation — must be perfect before harder compositions)

## Hard gate (the only promotion criterion)

To master a task: **OCR conf > 0.95 AND visual_score > 0.9 AND Claude vision unambiguous**. ALL THREE.

## Tasks

### Task 1 — 一 (yī)
- GT PNG: `ground_truths/cycle_6/01_一.png`
- Output PNG: `attempts/cycle_6/01_一.png`
- Output code: `attempts/cycle_6/generated.py` (single file, all 3 tasks)
- Reuse: `from heng import draw as draw_heng` (run_4 c1 mastered primitive — turtle-based)

### Task 2 — 二 (èr)
- GT PNG: `ground_truths/cycle_6/02_二.png`
- Output PNG: `attempts/cycle_6/02_二.png`
- Reuse: `draw_heng` × 2

### Task 3 — 三 (sān)
- GT PNG: `ground_truths/cycle_6/03_三.png`
- Output PNG: `attempts/cycle_6/03_三.png`
- Reuse: `draw_heng` × 3

## Eval
`vision+ocr+gt`.

## Renderer

Use `turtle.Turtle` + `screen.getcanvas().postscript()` → PIL save, matching the Success Bank primitives' interface. The PIL experiment from c2 is reverted (see `_revoked/`).

Standard pattern:
```python
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from heng import draw as draw_heng

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")

def reset_turtle(t):
    t.reset(); t.hideturtle(); t.speed(0)
    t.pencolor("black"); t.pensize(3)
    t.penup(); t.goto(0, 0); t.setheading(90)
```

## Self-preview budget
Max 2 internal iterations per task. Check each attempt PNG vs GT PNG visually + look at MMH stroke positions.

## Notes on the hard gate

- The MMH GTs are thin (~pensize 3) and positioned per the MMH skeleton coordinates. For visual_score > 0.9, the stroke CENTERLINES of your render must align tightly with the GT centerlines. Read the GT PNG carefully and place the brushwork along the same path.
- The run_4 brushwork has width 11–19 — that's wider than the GT (~3). Some pixel mismatch is unavoidable. visual > 0.9 may not be reachable with default run_4 brushwork on MMH GTs. If your render passes vision + OCR but fails visual, log the visual_score and carry over with a note.
- Do NOT modify the Success Bank primitives (they are immutable). If brushwork is the wrong shape for this gate, leave it for the Curator to decide whether a new variant is needed.
