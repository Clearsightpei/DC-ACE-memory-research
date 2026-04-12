"""DC-ACE Memory Builder

Reads judge_results_N.json and builds memory files for the next iteration:
  - Mode 2 (Failure Learning): selects failures → DeepSeek R1 explains errors → failure_memory.json
  - Mode 3 (Success Learning): selects successes → DeepSeek R1 annotates code → success_memory.json
  - Mode 1: no memory needed, exits immediately.

Usage:
    python memory_builder.py --mode 2 --input judge_results_1.json
    python memory_builder.py --mode 3 --input judge_results_1.json

Requirements:
    pip install openai
"""

import os
import re
import json
import argparse
from typing import Dict, List

from openai import OpenAI

# ─────────────────── Success / Failure Threshold ──────────────────────────

PASS_THRESHOLD = 0.75  # visual_score >= this AND is_correct == true → success


# ─────────────────────────── DeepSeek R1 Reflector ────────────────────────

def _strip_thinking(text: str) -> str:
    """Remove DeepSeek R1 <think>...</think> reasoning blocks."""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def reflect_on_success(
    client: OpenAI,
    model: str,
    character: str,
    pinyin: str,
    code: str,
    vision_feedback: Dict,
) -> Dict:
    """Ask DeepSeek R1 to annotate WHY this code is correct.

    Uses DeepSeek's own knowledge of Chinese characters as first principle.
    Returns structured memory entry with annotated code + first principles.
    """
    comparison = vision_feedback.get("comparison_markdown", "")
    error_desc = vision_feedback.get("error_description", "")

    prompt = (
        f"你是一位中文书写专家。以下是一个成功的turtle绘图代码，它正确画出了汉字「{character}」({pinyin})。\n\n"
        f"代码：\n```python\n{code}\n```\n\n"
        f"评委反馈：\n{error_desc}\n\n"
        f"图像对比：\n{comparison}\n\n"
        f"请用你对「{character}」的知识（笔画数、笔画类型、相对位置）分析这段代码：\n"
        f"1. 这个字由哪些笔画组成？\n"
        f"2. 代码中哪些部分对应了哪些笔画？\n"
        f"3. 笔画之间的相对位置关系是什么？\n\n"
        f"只返回JSON：\n"
        f"{{\n"
        f'  "character": "{character}",\n'
        f'  "pinyin": "{pinyin}",\n'
        f'  "stroke_count": 笔画数量(数字),\n'
        f'  "strokes": ["笔画1类型", "笔画2类型", ...],\n'
        f'  "first_principles": "用中文描述这个字的笔画组成、角度、相对位置关系",\n'
        f'  "code_annotation": "用中文标注代码中每个关键部分对应的笔画"\n'
        f"}}"
    )

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是中文书法分析专家。只返回JSON，不要其他文字。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
            max_tokens=1500,
            timeout=120,
        )
        raw = _strip_thinking(resp.choices[0].message.content)
        cleaned = re.sub(r"```(?:json)?\n?", "", raw)
        cleaned = re.sub(r"```$", "", cleaned).strip()

        try:
            parsed = json.loads(cleaned)
            return parsed
        except json.JSONDecodeError:
            return {
                "character": character,
                "pinyin": pinyin,
                "first_principles": raw[:500],
                "code_annotation": "parse_error",
            }

    except Exception as e:
        return {
            "character": character,
            "pinyin": pinyin,
            "first_principles": f"Reflection failed: {e}",
            "code_annotation": "",
        }


def reflect_on_failure(
    client: OpenAI,
    model: str,
    character: str,
    pinyin: str,
    code: str,
    vision_feedback: Dict,
) -> Dict:
    """Ask DeepSeek R1 to analyze WHY this code failed.

    Returns a natural-language error explanation for the failure memory.
    """
    comparison = vision_feedback.get("comparison_markdown", "")
    error_desc = vision_feedback.get("error_description", "")
    error_type = vision_feedback.get("error_type", "unknown")
    recognized = vision_feedback.get("recognized_char", "unknown")

    prompt = (
        f"你是一位中文书写专家。以下是一个失败的turtle绘图代码，目标是画汉字「{character}」({pinyin})，"
        f"但评委识别出来的是「{recognized}」。\n\n"
        f"代码：\n```python\n{code}\n```\n\n"
        f"错误类型：{error_type}\n"
        f"评委反馈：{error_desc}\n\n"
        f"图像对比：\n{comparison}\n\n"
        f"请分析代码错误的根本原因：\n"
        f"1. 代码中哪些具体的部分导致了错误？\n"
        f"2. 正确的「{character}」应该是什么样的？（笔画、角度、位置）\n"
        f"3. 错误的核心原因是什么（角度不对？位置偏了？缺少笔画？）\n\n"
        f"只返回JSON：\n"
        f"{{\n"
        f'  "character": "{character}",\n'
        f'  "pinyin": "{pinyin}",\n'
        f'  "recognized_as": "{recognized}",\n'
        f'  "error_type": "{error_type}",\n'
        f'  "root_cause": "用中文解释代码错误的根本原因",\n'
        f'  "correct_description": "正确的字应该怎么画（笔画类型、角度、相对位置）",\n'
        f'  "specific_fixes": "具体哪些代码行需要改，为什么"\n'
        f"}}"
    )

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是中文书法错误分析专家。只返回JSON，不要其他文字。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
            max_tokens=1500,
            timeout=120,
        )
        raw = _strip_thinking(resp.choices[0].message.content)
        cleaned = re.sub(r"```(?:json)?\n?", "", raw)
        cleaned = re.sub(r"```$", "", cleaned).strip()

        try:
            parsed = json.loads(cleaned)
            return parsed
        except json.JSONDecodeError:
            return {
                "character": character,
                "pinyin": pinyin,
                "recognized_as": recognized,
                "error_type": error_type,
                "root_cause": raw[:500],
                "correct_description": "parse_error",
                "specific_fixes": "",
            }

    except Exception as e:
        return {
            "character": character,
            "pinyin": pinyin,
            "recognized_as": recognized,
            "error_type": error_type,
            "root_cause": f"Reflection failed: {e}",
            "correct_description": "",
            "specific_fixes": "",
        }


# ─────────────────────────── Main ─────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DC-ACE Memory Builder: generate success/failure memory from judge results"
    )
    parser.add_argument("--mode", type=int, choices=[1, 2, 3], required=True,
                        help="1=skip, 2=build failure memory, 3=build success memory")
    parser.add_argument("--input", required=True,
                        help="Path to judge_results_N.json")
    parser.add_argument("--output", default=None,
                        help="Output memory file (default: success_memory.json or failure_memory.json)")
    parser.add_argument("--ollama-host", default="http://100.120.168.33:11434",
                        help="Ollama server URL for DeepSeek R1")
    parser.add_argument("--reflector-model", default="deepseek-r1:32b",
                        help="DeepSeek R1 model name (default: deepseek-r1:32b)")
    args = parser.parse_args()

    # Mode 1: no memory needed
    if args.mode == 1:
        print("Mode 1 (Baseline): no memory to build. Exiting.")
        return

    # Determine output filename
    if args.output is None:
        args.output = "success_memory.json" if args.mode == 3 else "failure_memory.json"

    # Load judge results
    with open(args.input, "r", encoding="utf-8") as fh:
        results: List[Dict] = json.load(fh)

    # Initialize DeepSeek R1 client
    client = OpenAI(
        api_key="ollama",
        base_url=f"{args.ollama_host}/v1",
    )

    mode_names = {2: "Failure Learning", 3: "Success Learning"}
    print("=" * 60)
    print(f"DC-ACE Memory Builder  [Mode {args.mode}: {mode_names[args.mode]}]")
    print("=" * 60)
    print(f"Input      : {args.input}  ({len(results)} characters)")
    print(f"Reflector  : {args.reflector_model}")
    print(f"Threshold  : visual_score >= {PASS_THRESHOLD}")
    print(f"Output     : {args.output}")
    print()

    memory: List[Dict] = []

    if args.mode == 3:
        # ── Success Learning: select passing characters ───────────────
        successes = [
            r for r in results
            if r.get("is_correct") is True
            and r.get("visual_score", 0) >= PASS_THRESHOLD
            and r.get("generated_code", "").strip()
        ]
        print(f"Passing characters: {len(successes)}/{len(results)}")
        print()

        for r in successes:
            char = r["character"]
            pin = r["pinyin"]
            print(f"  Reflecting on {char} ({pin}) ... ", end="", flush=True)
            annotation = reflect_on_success(
                client, args.reflector_model,
                char, pin,
                r["generated_code"],
                r.get("vision_feedback") or {},
            )
            annotation["verified_code"] = r["generated_code"]
            annotation["visual_score"] = r["visual_score"]
            memory.append(annotation)
            print("done")

    elif args.mode == 2:
        # ── Failure Learning: select failing characters ───────────────
        failures = [
            r for r in results
            if (r.get("is_correct") is not True
                or r.get("visual_score", 0) < PASS_THRESHOLD)
            and r.get("generated_code", "").strip()
        ]
        print(f"Failing characters: {len(failures)}/{len(results)}")
        print()

        for r in failures:
            char = r["character"]
            pin = r["pinyin"]
            print(f"  Reflecting on {char} ({pin}) ... ", end="", flush=True)
            analysis = reflect_on_failure(
                client, args.reflector_model,
                char, pin,
                r["generated_code"],
                r.get("vision_feedback") or {},
            )
            analysis["visual_score"] = r["visual_score"]
            memory.append(analysis)
            print("done")

    # ── Save memory file ──────────────────────────────────────────────
    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(memory, fh, ensure_ascii=False, indent=2)

    print(f"\nMemory entries: {len(memory)}")
    print(f"Saved: {args.output}")


if __name__ == "__main__":
    main()
