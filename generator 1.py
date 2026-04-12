"""DC-ACE Generator

Prompts a local Ollama model (default: gemma4) to generate structured Python
turtle code for Chinese characters. Supports three memory modes:

  Mode 1: No Memory (Baseline) — zero-shot generation
  Mode 2: Failure Learning     — injects error descriptions from failure_memory.json
  Mode 3: Success Learning     — injects verified code + first principles from success_memory.json

After generation, automatically triggers judge.py and memory_builder.py.

Semantic Map comment format:
    # [MOVE]: Step N        — pen-up repositioning before a stroke
    # [STROKE: TYPE]: Step N — the drawing action (HENG, SHU, PIE, etc.)

Output: generated_characters_N.py + AI_Generated_PNG_N/ (N = mode number)
"""

import os
import re
import json
import sys
import time
import argparse
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional

from openai import OpenAI, APIStatusError, APITimeoutError, APIConnectionError

# ─────────────────────────── Prompt Templates ─────────────────────────────

SYSTEM_PROMPT_BASE = """You are an expert Chinese calligraphy encoder. Your job is to generate \
Python turtle code that draws a Chinese character stroke-by-stroke.

STRICT REQUIREMENTS:
1. Output ONLY a single Python function named  draw_<pinyin>(t)  where <pinyin> is \
the romanization of the character and `t` is a turtle object already configured \
(600×600 canvas, center=(0,0), pensize=3, pencolor="black").

2. Annotate EVERY movement and stroke with these EXACT comment labels:
       # [MOVE]: Step N          before any penup/goto block
       # [STROKE: TYPE]: Step N  before any pendown/drawing block
   where:
     - N is a sequential integer starting at 1
     - TYPE is one of: HENG, SHU, PIE, DIAN, NA, TI, ZHE, GOU, WAN, WO
     - MOVE and STROKE for the SAME action share the SAME N

3. Keep each step atomic — one fundamental stroke per step number.

4. Use setheading() with absolute angles: 0°=East 90°=North 180°=West 270°=South

5. Never call turtle.Screen(), screen.setup(), or any save/exit command — \
the caller handles setup and teardown.

EXAMPLE (for 木 mù):
def draw_mu(t):
    # [MOVE]: Step 1
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    # [STROKE: HENG]: Step 1
    t.setheading(0)
    t.forward(100)

    # [MOVE]: Step 2
    t.penup()
    t.goto(0, 30)
    t.pendown()
    # [STROKE: SHU]: Step 2
    t.setheading(270)
    t.forward(80)

    # [MOVE]: Step 3
    t.penup()
    t.goto(0, -10)
    t.pendown()
    # [STROKE: PIE]: Step 3
    t.setheading(225)
    t.forward(50)

    # [MOVE]: Step 4
    t.penup()
    t.goto(0, -10)
    t.pendown()
    # [STROKE: NA]: Step 4
    t.setheading(315)
    t.forward(50)

Output ONLY the function. No imports. No screen setup. No save commands."""


# ─────────────────────────── Memory Injection ─────────────────────────────

def build_system_prompt(mode: int, memory: List[Dict]) -> str:
    """Build the full system prompt, optionally injecting memory."""
    prompt = SYSTEM_PROMPT_BASE

    if mode == 2 and memory:
        prompt += "\n\n## Common Mistakes to Avoid\n"
        prompt += "The following are errors from previous attempts. Learn from them:\n\n"
        for entry in memory:
            char = entry.get("character", "?")
            pin = entry.get("pinyin", "?")
            root_cause = entry.get("root_cause", "")
            correct_desc = entry.get("correct_description", "")
            fixes = entry.get("specific_fixes", "")
            prompt += f"### {char} ({pin})\n"
            if root_cause:
                prompt += f"- Root cause: {root_cause}\n"
            if correct_desc:
                prompt += f"- Correct form: {correct_desc}\n"
            if fixes:
                prompt += f"- Fixes needed: {fixes}\n"
            prompt += "\n"

    elif mode == 3 and memory:
        prompt += "\n\n## Verified Reference Implementations\n"
        prompt += "The following code has been verified as correct. Use these as reference:\n\n"
        for entry in memory:
            char = entry.get("character", "?")
            pin = entry.get("pinyin", "?")
            code = entry.get("verified_code", "")
            principles = entry.get("first_principles", "")
            score = entry.get("visual_score", 0)
            prompt += f"### {char} ({pin}) — verified score: {score}\n"
            if principles:
                prompt += f"Structure: {principles}\n"
            if code:
                prompt += f"```python\n{code}\n```\n"
            prompt += "\n"

    return prompt


def load_memory(memory_file: Optional[str]) -> List[Dict]:
    """Load a memory JSON file. Returns empty list if file doesn't exist."""
    if not memory_file or not os.path.exists(memory_file):
        return []
    with open(memory_file, "r", encoding="utf-8") as fh:
        return json.load(fh)


# ─────────────────────────── Helpers ──────────────────────────────────────

def _strip_thinking(text: str) -> str:
    """Remove DeepSeek R1 <think>...</think> reasoning blocks."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)


def _extract_function(text: str) -> Optional[str]:
    """Pull the draw_* function out of the LLM response."""
    # Try a fenced code block first
    m = re.search(r"```python\n(.*?)```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    # Fall back: look for a def draw_ line and take everything after it
    m = re.search(r"(def draw_\w+\(t\):.*)", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None


# ─────────────────────────── LLM Call ─────────────────────────────────────

def generate_function(client: OpenAI, model: str, task: Dict,
                      system_prompt: str,
                      retries: int = 3, backoff: float = 5.0) -> str:
    """Call the LLM and return the raw draw_<pinyin>(t) function string."""
    char    = task.get("character", task.get("stroke", ""))
    pinyin  = task.get("pinyin", "")
    meaning = task.get("meaning", "")
    desc    = task.get("description", "")

    user_msg = (
        f"Draw Chinese character: {char}\n"
        f"Pinyin: {pinyin}\n"
        f"Meaning: {meaning}\n"
        f"Description: {desc}\n\n"
        f"Generate the  draw_{pinyin}(t)  function with a [MOVE] + [STROKE] comment "
        f"pair for every stroke, numbered sequentially from Step 1."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_msg},
    ]

    wait = backoff
    for attempt in range(1, retries + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.0,
                max_tokens=2048,
                timeout=120,
            )
            raw     = response.choices[0].message.content
            cleaned = _strip_thinking(raw)
            func    = _extract_function(cleaned)
            if func is None:
                return f"# WARNING: could not extract function for {char} ({pinyin})\n" + cleaned
            return func

        except (APITimeoutError, APIConnectionError) as e:
            print(f"\n    ⚠  Attempt {attempt}/{retries} failed (timeout/connection): {e}")
        except APIStatusError as e:
            if e.status_code in (502, 503, 504):
                print(f"\n    ⚠  Attempt {attempt}/{retries} failed ({e.status_code} gateway error)")
            else:
                raise

        if attempt < retries:
            print(f"    ↻  Retrying in {wait:.0f}s...")
            time.sleep(wait)
            wait *= 2

    return f"# ERROR: all {retries} attempts failed for {char} ({pinyin})\n# def draw_{pinyin}(t): pass"


# ─────────────────────────── PNG Rendering ────────────────────────────────

def render_function_to_png(func_code: str, output_path: str) -> bool:
    """Execute a generated draw_<pinyin>(t) function and save as PNG via ghostscript."""
    import turtle as turtle_mod

    success = False
    try:
        screen = turtle_mod.Screen()
        screen.setup(600, 600)
        screen.bgcolor("white")
        turtle_mod.tracer(0, 0)

        t = turtle_mod.Turtle()
        t.hideturtle()
        t.speed(0)
        t.pensize(3)
        t.pencolor("black")

        namespace = {}
        exec(func_code, namespace)

        draw_fn = None
        for name, obj in namespace.items():
            if name.startswith("draw_") and callable(obj):
                draw_fn = obj
                break

        if draw_fn is None:
            print("(no draw_ function) ", end="")
            return False

        draw_fn(t)

        turtle_mod.update()
        canvas = screen.getcanvas()

        with tempfile.NamedTemporaryFile(suffix=".ps", delete=False) as tmp:
            tmp_ps = tmp.name
        canvas.postscript(file=tmp_ps, colormode="color")

        result = subprocess.run(
            [
                "gs", "-dNOPAUSE", "-dBATCH", "-dSAFER",
                "-sDEVICE=png16m", "-r150",
                f"-sOutputFile={output_path}",
                tmp_ps,
            ],
            capture_output=True,
            text=True,
        )
        os.unlink(tmp_ps)

        success = result.returncode == 0
        if not success:
            print(f"(gs error: {result.stderr[:60]}) ", end="")

    except turtle_mod.Terminator:
        pass
    except Exception as e:
        print(f"(render error: {e}) ", end="")
    finally:
        try:
            turtle_mod.Screen().bye()
        except Exception:
            pass
        turtle_mod.TurtleScreen._RUNNING = True

    return success


# ─────────────────────────── Output Assembly ──────────────────────────────

def _file_header(mode: int) -> str:
    mode_names = {1: "No Memory (Baseline)", 2: "Failure Learning", 3: "Success Learning"}
    return f'''\
"""
Auto-generated by DC-ACE Generator — Mode {mode}: {mode_names[mode]}

Each Chinese character is encapsulated in a  draw_<pinyin>(t)  function.
The Semantic Map comment format used throughout:

    # [MOVE]: Step N           — pen-up repositioning to stroke entry point
    # [STROKE: TYPE]: Step N   — the atomic drawing action

These labels are parsed by judge.py for evaluation.
"""
import turtle


def _make_turtle() -> tuple:
    """Create a configured screen + turtle for standalone testing."""
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgcolor("white")
    turtle.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.pencolor("black")
    return screen, t

'''


def build_output_file(
    characters: List[Dict],
    functions: List[str],
    output_path: str,
    mode: int = 1,
) -> None:
    """Write all generated functions into a single annotated Python file."""
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(_file_header(mode))

        for task, func_code in zip(characters, functions):
            char    = task.get("character", task.get("stroke", ""))
            pinyin  = task.get("pinyin", "")
            meaning = task.get("meaning", "")
            idx     = task.get("index", 0)
            gt_file = ""
            samples = task.get("samples", [])
            if samples:
                gt_file = samples[0].get("filename", "")

            fh.write(
                f"# ── Task {idx:02d} | {char} ({pinyin}) | {meaning} "
                f"| GT: {gt_file}\n"
            )
            fh.write(func_code)
            fh.write("\n\n\n")

    print(f"Saved → {output_path}")


# ─────────────────────────── Auto-Trigger Pipeline ────────────────────────

def run_judge(mode: int, ai_png_dir: str, gt_png_dir: str,
              dataset: str, generated_code: str, ollama_host: str,
              vision_model: str) -> str:
    """Run judge.py as a subprocess. Returns the output JSON path."""
    output = f"judge_results_{mode}.json"
    cmd = [
        sys.executable, "judge.py",
        "--mode", str(mode),
        "--ai-png-dir", ai_png_dir,
        "--gt-png-dir", gt_png_dir,
        "--dataset", dataset,
        "--generated-code", generated_code,
        "--output", output,
        "--ollama-host", ollama_host,
        "--vision-model", vision_model,
    ]
    print(f"\n{'='*60}")
    print(f"Auto-triggering judge.py (mode {mode})")
    print(f"{'='*60}\n")
    subprocess.run(cmd)
    return output


def run_memory_builder(mode: int, judge_results: str, ollama_host: str,
                       reflector_model: str) -> None:
    """Run memory_builder.py as a subprocess."""
    if mode == 1:
        return  # No memory for baseline
    cmd = [
        sys.executable, "memory_builder.py",
        "--mode", str(mode),
        "--input", judge_results,
        "--ollama-host", ollama_host,
        "--reflector-model", reflector_model,
    ]
    print(f"\n{'='*60}")
    print(f"Auto-triggering memory_builder.py (mode {mode})")
    print(f"{'='*60}\n")
    subprocess.run(cmd)


# ─────────────────────────── Main ─────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DC-ACE Generator: produce annotated turtle code for Chinese characters"
    )
    parser.add_argument("--mode", type=int, choices=[1, 2, 3], default=1,
                        help="1=No Memory, 2=Failure Learning, 3=Success Learning (default: 1)")
    parser.add_argument("--dataset",  required=True,
                        help="Path to dataset JSON (characters.json / chinese_strokes.json)")
    parser.add_argument("--memory-file", default=None,
                        help="Path to memory JSON (auto-detected if not specified)")
    parser.add_argument("--output",   default=None,
                        help="Output Python file path (default: generated_characters_N.py)")
    parser.add_argument("--base-url", default="http://100.120.168.33:11434/v1",
                        help="Ollama API base URL (default: http://100.120.168.33:11434/v1)")
    parser.add_argument("--model",    default="gemma4",
                        help="Generator model name (default: gemma4)")
    parser.add_argument("--limit",    type=int, default=None,
                        help="Process only the first N characters (for debugging)")
    parser.add_argument("--skip-render", action="store_true", default=False,
                        help="Skip PNG rendering of generated functions")
    parser.add_argument("--png-output-dir", default=None,
                        help="Directory for rendered PNGs (default: AI_Generated_PNG_N/)")
    parser.add_argument("--gt-png-dir", default="PNG Ground Truth/Chinese_2/",
                        help="Ground truth PNG directory (for judge auto-trigger)")
    parser.add_argument("--ollama-host", default="http://100.120.168.33:11434",
                        help="Ollama host for judge + memory builder")
    parser.add_argument("--vision-model", default="deepseek-ocr",
                        help="Vision model for judge (default: deepseek-ocr)")
    parser.add_argument("--reflector-model", default="deepseek-r1:32b",
                        help="Reflector model for memory builder (default: deepseek-r1:32b)")
    parser.add_argument("--skip-judge", action="store_true", default=False,
                        help="Skip auto-triggering judge.py after generation")
    parser.add_argument("--skip-memory", action="store_true", default=False,
                        help="Skip auto-triggering memory_builder.py after judging")
    args = parser.parse_args()

    mode = args.mode

    # Default output paths based on mode
    if args.output is None:
        args.output = f"generated_characters_{mode}.py"

    # Auto-detect memory file
    if args.memory_file is None:
        if mode == 2:
            args.memory_file = "failure_memory.json"
        elif mode == 3:
            args.memory_file = "success_memory.json"

    # Load memory
    memory = load_memory(args.memory_file) if mode in (2, 3) else []
    system_prompt = build_system_prompt(mode, memory)

    client = OpenAI(
        api_key="ollama",
        base_url=args.base_url,
    )

    with open(args.dataset, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    # Support two JSON formats
    if isinstance(data, list):
        characters = []
        for i, entry in enumerate(data):
            p = entry.get("params", {})
            characters.append({
                "index":       i + 1,
                "character":   p.get("stroke", ""),
                "pinyin":      p.get("pinyin", ""),
                "meaning":     p.get("meaning", ""),
                "description": entry.get("prompt", ""),
                "samples":     [{"filename": entry.get("id", "")}],
            })
    else:
        characters = data["characters"]

    if args.limit:
        characters = characters[: args.limit]

    # Determine PNG output directory
    png_dir: Optional[Path] = None
    if not args.skip_render:
        if args.png_output_dir:
            png_dir = Path(args.png_output_dir)
        else:
            png_dir = Path(args.output).parent / f"AI_Generated_PNG_{mode}"
        png_dir.mkdir(parents=True, exist_ok=True)

    # ── Banner ────────────────────────────────────────────────────────
    mode_names = {1: "No Memory (Baseline)", 2: "Failure Learning", 3: "Success Learning"}
    print("=" * 60)
    print(f"DC-ACE Generator  |  Mode {mode}: {mode_names[mode]}")
    print("=" * 60)
    print(f"Dataset : {args.dataset}  ({len(characters)} characters)")
    print(f"Model   : {args.model}")
    print(f"Memory  : {args.memory_file or '(none)'}")
    if memory:
        print(f"          {len(memory)} entries loaded")
    print(f"Output  : {args.output}")
    if png_dir:
        print(f"PNG Dir : {png_dir}")
    print()

    generated: List[str] = []
    render_ok = 0
    render_fail = 0

    for i, task in enumerate(characters):
        char   = task.get("character", task.get("stroke", ""))
        pinyin = task.get("pinyin", "")
        idx    = task.get("index", i + 1)
        print(f"[{i+1:3d}/{len(characters)}] {char} ({pinyin}) ... ", end="", flush=True)
        func = generate_function(client, args.model, task, system_prompt)
        generated.append(func)

        # Render PNG
        if png_dir is not None:
            png_name = f"{idx:02d}_{char}_{pinyin}.png"
            png_path = png_dir / png_name
            ok = render_function_to_png(func, str(png_path))
            if ok:
                render_ok += 1
                print(f"done -> {png_name}")
            else:
                render_fail += 1
                print("done (render failed)")
        else:
            print("done")

    build_output_file(characters, generated, args.output, mode=mode)

    print(f"\nFinished. {len(characters)} functions written to {args.output}")
    if png_dir is not None:
        print(f"PNG rendering: {render_ok} succeeded, {render_fail} failed -> {png_dir}")

    # ── Auto-trigger judge + memory builder ───────────────────────────
    if not args.skip_judge and png_dir is not None:
        judge_output = run_judge(
            mode=mode,
            ai_png_dir=str(png_dir),
            gt_png_dir=args.gt_png_dir,
            dataset=args.dataset,
            generated_code=args.output,
            ollama_host=args.ollama_host,
            vision_model=args.vision_model,
        )

        if not args.skip_memory:
            run_memory_builder(
                mode=mode,
                judge_results=judge_output,
                ollama_host=args.ollama_host,
                reflector_model=args.reflector_model,
            )


if __name__ == "__main__":
    main()
