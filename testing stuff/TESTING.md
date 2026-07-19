# DC-ACE Testing Framework

Testing framework for evaluating LLM performance on Chinese character and shape drawing tasks using **local DeepSeek 32B**.

## Overview

The testing framework evaluates LLM performance under different memory conditions:

1. **Zero-Shot** (baseline): No memory or context between tasks ← **START HERE**
2. **Hoarder** (future): Linear, unorganized history
3. **Architect** (future): Refactored hierarchical function library

## Prerequisites

### 1. Install Python Dependencies

```bash
pip install -r requirements_testing.txt
```

Required packages:
- `openai` - OpenAI-compatible API client for local models
- `Pillow` - Image processing
- `scikit-image` - SSIM comparison
- `numpy` - Numerical operations

### 2. Set Up Local DeepSeek 32B

You need DeepSeek 32B running locally with an OpenAI-compatible API endpoint.

**Option A: Using vLLM (Recommended)**
```bash
# Install vLLM
pip install vllm

# Run DeepSeek 32B
python -m vllm.entrypoints.openai.api_server \
  --model deepseek-ai/DeepSeek-V3 \
  --host localhost \
  --port 8000
```

**Option B: Using Ollama**
```bash
# Install Ollama from https://ollama.ai

# Pull and run DeepSeek
ollama run deepseek-r1:32b

# Run with OpenAI-compatible API
OLLAMA_HOST=http://localhost:11434 ollama serve
```

**Option C: Using LM Studio**
- Download LM Studio from https://lmstudio.ai
- Load DeepSeek 32B model
- Start local server (default: http://localhost:1234/v1)

### 3. Verify Local Model is Running

```bash
# Test API endpoint
curl http://localhost:8000/v1/models

# Should return model list including DeepSeek
```

## Testing Progression: L1 → L2 → L3

### Level 1: Chinese Strokes (Start Here)

**What:** 32 basic calligraphy strokes (点、横、竖、撇、捺、etc.)
**Why:** Fundamental building blocks - test if LLM understands basic geometric primitives

```bash
python test_zero_shot.py \
  --dataset chinese_strokes_dataset/chinese_strokes.json \
  --ground-truth chinese_strokes_dataset \
  --output output/L1_strokes
```

**Expected:** ~160 stroke samples (32 types × 5 samples each)

### Level 2: Basic Chinese Characters

**What:** 30 simple characters (一、人、木、火、水、etc.)
**Why:** Test composition of Level 1 strokes into meaningful characters

```bash
python test_zero_shot.py \
  --dataset Chinese_2/characters.json \
  --ground-truth Chinese_2 \
  --output output/L2_basic_chars
```

**Expected:** 90 character samples (30 chars × 3 samples each)

### Level 3: Compound Characters

**What:** 30 compound characters (二、三、从、众、林、森、etc.)
**Why:** Test hierarchical composition - characters built from characters

```bash
python test_zero_shot.py \
  --dataset Chinese_L3/characters_L3.json \
  --ground-truth Chinese_L3 \
  --output output/L3_compound
```

**Expected:** 60 character samples (30 chars × 2 samples each)

## Advanced Usage

### Custom Local Endpoint

If your model runs on a different port:

```bash
python test_zero_shot.py \
  --dataset chinese_strokes_dataset/chinese_strokes.json \
  --ground-truth chinese_strokes_dataset \
  --output output/L1_strokes \
  --base-url http://localhost:1234/v1
```

### Different Model

```bash
python test_zero_shot.py \
  --dataset Chinese_2/characters.json \
  --ground-truth Chinese_2 \
  --output output/L2_basic \
  --model deepseek-coder-33b-instruct
```

### Test Geometric Shapes (Task Factory)

```bash
python test_zero_shot.py \
  --dataset dataset_pilot/tasks.json \
  --ground-truth dataset_pilot \
  --output output/shapes
```

## Output Structure

```
output/L1_strokes/
├── baseline_results.csv       # Results: task_id, stroke, SSIM, errors
├── generated/                 # Generated stroke images
│   ├── 01_点_1.png
│   ├── 02_横_1.png
│   └── ...
└── code/                      # Generated Python code
    ├── 01_点_1.py
    ├── 02_横_1.py
    └── ...
```

## Results Analysis

### View Results

```bash
# Pretty print CSV
cat output/L1_strokes/baseline_results.csv | column -t -s,

# Calculate statistics
python -c "
import csv
with open('output/L1_strokes/baseline_results.csv') as f:
    rows = list(csv.DictReader(f))
    successful = [r for r in rows if r['success'] == 'True']
    scores = [float(r['ssim_score']) for r in successful if r['ssim_score']]
    print(f'Success Rate: {len(successful)}/{len(rows)} ({len(successful)/len(rows)*100:.1f}%)')
    print(f'Avg SSIM: {sum(scores)/len(scores):.4f}' if scores else 'No scores')
"
```

### Understanding SSIM Scores

**SSIM (Structural Similarity Index)** ranges from 0 to 1:

| Score | Quality |
|-------|---------|
| 0.9-1.0 | Excellent - Nearly perfect match |
| 0.7-0.9 | Good - Recognizable with minor differences |
| 0.5-0.7 | Moderate - Correct general shape |
| 0.3-0.5 | Poor - Wrong proportions or orientation |
| < 0.3 | Failed - Unrecognizable |

### Compare Visually

```bash
# Open side-by-side
open output/L1_strokes/generated/01_点_1.png
open chinese_strokes_dataset/L1_Stroke_Dian_1.png
```

## Troubleshooting

### "Connection refused" Error

Model not running. Start your local model server:
```bash
# vLLM
python -m vllm.entrypoints.openai.api_server --model deepseek-ai/DeepSeek-V3

# Or check if running
curl http://localhost:8000/v1/models
```

### "Model not found" Error

Check model name matches your local setup:
```bash
# List available models
curl http://localhost:8000/v1/models

# Use correct model name
python test_zero_shot.py --model <your-model-name> ...
```

### Code Extraction Failed

LLM returned explanations instead of code. This is common with some models. Check:
1. System prompt is being used (some endpoints ignore it)
2. Temperature is set to 0.0 for deterministic output
3. Model supports code generation

### Execution Timeout

Code has infinite loops or `exitonclick()`. Check `code/` directory and manually review generated scripts.

### Low SSIM Scores

Common causes:
- **Orientation:** Stroke drawn in wrong direction
- **Position:** Not centered on canvas
- **Thickness:** Wrong pen size (should be 3)
- **Color:** Not black (should be "black")

## Research Workflow

1. **Baseline (Zero-Shot):** Establish performance floor
2. **Analyze Failures:** Which strokes/characters are hardest?
3. **Test Hoarder:** Add linear memory of previous attempts
4. **Test Architect:** Provide refactored function library from task_factory.py
5. **Compare:** Does memory help? Does organization matter?

## Level 1 Primitives from task_factory.py

When testing with the Architect strategy (future), you'll provide these functions:

```python
# Geometric primitives (from task_factory.py)
draw_regular_polygon(t, n, size, color)
draw_circle(t, size, color)
draw_rectangle(t, width, height, color)
draw_star(t, size, color)
draw_leaf(t, size, angle_deg, color)

# Compound shapes (Level 2)
draw_flower(t, petal_count, petal_size, angle_deg, colors)
draw_house(t, size, c1, c2)
draw_snowman(t, bottom, color)
# ... and 20+ more
```

These will be in the system prompt for Architect tests, allowing the LLM to compose rather than generate from scratch.

## Citation

DC-ACE (Dynamic Context - Agentic Context Engineering) Research
Professor You, Palo Alto High School
