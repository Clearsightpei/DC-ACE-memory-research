# CLAUDE.md: DC-ACE Research Context

This file provides the "Memory Architecture" for Claude Code when working in this repository.

## 🧠 Research Purpose: DC-ACE
This project is not just a shape generator; it is the **DC-ACE (Dynamic Context - Agentic Context Engineering)** framework. We are researching if an LLM "Curator" can refactor linear memory into a hierarchical function library to prevent model collapse in complex reasoning.

### The Three Experimental Strategies
1. **Zero-Shot:** No memory.
2. **The Hoarder:** Linear, unorganized history (raw code).
3. **The Architect (ACE):** Refactored library of Level 1 & 2 functions.

## 📐 Strict Geometric Standards
To maintain the "Ground Truth" integrity for Professor You at Palo Alto High School:

- **Centered Drawing:** All functions must treat the current turtle position as the center/stem.
- **Leaf Formula:** `repeat 2 [repeat angle [fd 2 rt 1] rt 180-angle]`.
- **Flower/Mandala:** All petals must share the exact center point `(cx, cy)`.
- **State Reset:** Functions **must** return the turtle to `heading(90)` with `penup()` after drawing to prevent carry-over errors.
- **Color Constraint:** **DO NOT USE** `"vanilla"`. Use `"cornsilk"` or `"beige"` for vanilla-colored scoops.

## 📂 Environment & Commands
- **Dependencies:** `Pillow`, `ghostscript` (Mac: `brew install ghostscript`).
- **Output:** `/Users/peilinwu/Documents/dataset_pilot`.
- **Generate Oracle Data:** `python task_factory.py`.

## 🧪 Dataset Metrics (L1-L3)
- **Level 1 (Atomic):** 25 Polygons, 10 Rectangles, 5 Circles, 5 Stars, 5 Leaves.
- **Level 2 (Molecular):** 5 samples each for 24 compound types.
- **Level 3 (Systemic):** Tested via the model's ability to call refactored Level 1 & 2 functions to solve high-complexity prompts.

## 🖌️ Chinese Character Drawing Tool (`draw_character/`)
A stroke-based Chinese character rendering system using Turtle graphics.

### What It Does
- Loads Chinese character stroke data from `graphics.txt` (29MB JSON database)
- Renders authentic Chinese characters using median stroke coordinates
- Supports 9000+ Chinese characters with proper stroke order and structure

### How to Use
```python
from draw_character.test import CharacterTurtleGenerator

# Initialize with the graphics database
gen = CharacterTurtleGenerator('draw_character/graphics.txt')

# Draw a character interactively (opens window)
gen.draw_locally("你", scale=0.5)  # scale controls size

# For batch generation, use Chinese_Char.py
python Chinese_Char.py  # Generates 30 basic characters × 3 samples each
```

### Data Structure
Each character in `graphics.txt` contains:
- `character`: The Chinese character (string)
- `strokes`: SVG path data (for high-fidelity rendering)
- `medians`: Simplified coordinate arrays `[[x,y], ...]` for each stroke

### Integration with DC-ACE
- Characters are drawn using **relative coordinates** (like the stroke library)
- Each character becomes a Level 1 primitive that can be composed into words (Level 2)
- Enables testing LLM's ability to learn hierarchical Chinese writing rules

