# CLAUDE.md: DC-ACE Research Context

This file provides the "Memory Architecture" for Claude Code when working in this repository.

## Research Purpose: DC-ACE
This project is the **DC-ACE (Dynamic Context - Agentic Context Engineering)** framework. We are researching whether an LLM can form useful memory from its own outputs, and comparing two opposing strategies: **learning from success** vs. **learning from failure**.

### The Three Experimental Modes

| Mode | Strategy | Memory Source | Hypothesis |
|------|----------|---------------|------------|
| 1 | **No Memory** (Baseline) | None. Zero-shot generation. | Inconsistent. High variance; cannot replicate success. |
| 2 | **Failure Learning** | `failure_memory.json` — natural-language error descriptions from past failures | Moderate improvement but risk of context overflow as errors accumulate. |
| 3 | **Success Learning** | `success_memory.json` — verified working code + DeepSeek's first-principle annotations | Superior. Efficient; reusable code snippets scale without context bloat. |

### Three Training Phases (Progressive)
1. **Phase 1 — Strokes**: Train on atomic strokes (horizontal, vertical, pie, na...), build stroke memory
2. **Phase 2 — Simple Characters**: Using stroke memory, train on simple characters (human, eight, ten...)
3. **Phase 3 — Complex Characters**: Using character memory, tackle compound characters

- **Centered Drawing:** All functions must treat the current turtle position as the center/stem.

---

## Automated Pipeline

The full loop runs with a single command. No human intervention after launch.

```
python "generator 1.py" --mode N --dataset chars.json

  Generator (mode N)
  │  Mode 1: zero-shot prompt (no memory)
  │  Mode 2: prompt + failure_memory.json
  │  Mode 3: prompt + success_memory.json
  │
  │  Output: AI_Generated_PNG_N/ + generated_characters_N.py
  │
  ├──► judge.py --mode N  (auto-triggered via subprocess)
  │    │  4 outputs per character (same scoring for all modes):
  │    │  1. visual_score     — OpenCV phase correlation
  │    │  2. recognized_char  — DeepSeek-OCR recognition
  │    │  3. is_correct       — boolean match
  │    │  4. comparison_markdown — position/size analysis of both images
  │    │
  │    │  Output: judge_results_N.json
  │    │
  │    └──► memory_builder.py --mode N  (auto-triggered via subprocess)
  │         │  Mode 1: skip (no memory needed)
  │         │  Mode 2: select failures → DeepSeek R1 reflector → failure_memory.json
  │         │  Mode 3: select successes → DeepSeek R1 reflector → success_memory.json
  │         │
  │         └──► Memory file ready for next iteration
```

### Memory Selection Criteria (hardcoded threshold = 0.75)

- **Success** (`is_correct == true` AND `visual_score >= 0.75`): Code is verified correct. DeepSeek R1 annotates it with first-principle knowledge (stroke decomposition, angles, positions).
- **Failure** (`is_correct == false` OR `visual_score < 0.75`): Interesting failures. DeepSeek R1 analyzes the code + judge feedback to explain the root cause.

---

## Infrastructure

### Models (all on local Ollama: `http://100.120.168.33:11434`)
- **Generator LLM**: `gemma4` (or configurable) — generates turtle code
- **Judge OCR**: `deepseek-ocr` — image recognition, character classification, markdown comparison
- **Reflector**: `deepseek-r1:32b` — text-only reasoning; analyzes code to build memory

### Dependencies
- `Pillow`, `ghostscript` (Mac: `brew install ghostscript`)
- `opencv-python`, `numpy`, `ollama`, `openai`

### Key Files

| File | Purpose |
|------|---------|
| `generator 1.py` | LLM code generator. `--mode 1\|2\|3` selects memory strategy. Auto-triggers judge + memory builder. |
| `judge.py` | Evaluates AI PNGs vs GT. OpenCV + DeepSeek-OCR. Outputs `judge_results_N.json`. |
| `memory_builder.py` | Builds `success_memory.json` or `failure_memory.json` using DeepSeek R1 reflector. |
| `generated_characters_N.py` | LLM-generated turtle functions (N = mode). |
| `judge_results_N.json` | Evaluation results per mode. |
| `success_memory.json` | Verified code + first-principle annotations (feeds Mode 3). |
| `failure_memory.json` | Natural-language error descriptions (feeds Mode 2). |
| `stroke_medians.json` | Ground truth stroke trajectories (30 canonical strokes). |

### Output Directories
- `AI_Generated_PNG_N/` — rendered PNGs per mode (N = 1, 2, 3)
- `PNG Ground Truth/` — ground truth reference images

---

## Chinese Character Drawing Tool (`draw_character/`)
A stroke-based Chinese character rendering system using Turtle graphics.

### What It Does
- Loads Chinese character stroke data from `graphics.txt` (29MB JSON database)
- Renders authentic Chinese characters using median stroke coordinates
- Supports 9000+ Chinese characters with proper stroke order and structure

### How to Use
```python
from draw_character.test import CharacterTurtleGenerator
gen = CharacterTurtleGenerator('draw_character/graphics.txt')
gen.draw_locally("你", scale=0.5)
```

### Data Structure
Each character in `graphics.txt` contains:
- `character`: The Chinese character (string)
- `strokes`: SVG path data (for high-fidelity rendering)
- `medians`: Simplified coordinate arrays `[[x,y], ...]` for each stroke

---

## Judge: 4-Output Structure

Each character evaluation produces:

| Output | Source | Description |
|--------|--------|-------------|
| `visual_score` | OpenCV `phaseCorrelate` | Frequency-domain alignment (0.0–1.0) |
| `recognized_char` | DeepSeek-OCR | What the model thinks the AI image shows |
| `is_correct` | DeepSeek-OCR | Boolean: does AI image match target character? |
| `comparison_markdown` | DeepSeek-OCR | Detailed markdown comparing both images (strokes, relative positions, sizes) |

**Final score:** `0.5 * visual_score + 0.5 * (1.0 if is_correct else 0.0)`

---

## Memory Builder: Two Strategies

### Success Memory (feeds Mode 3)
For each passing character (`is_correct && visual_score >= 0.75`):
1. Extract the turtle code that produced the correct result
2. Send code + judge feedback to DeepSeek R1
3. DeepSeek uses its own knowledge as first principle (e.g., "人 = 撇 + 捺")
4. Identifies WHICH code parts successfully implement what it knows
5. Stores annotated code snippet as reusable memory

### Failure Memory (feeds Mode 2)
For each failing character:
1. Extract the turtle code + all 4 judge outputs
2. Send to DeepSeek R1
3. DeepSeek analyzes the code and explains WHY it failed
4. Stores natural-language error description as memory
