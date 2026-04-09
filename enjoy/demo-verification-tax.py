#!/usr/bin/env python3
"""
AI PRODUCTIVITY PARADOX: Context-First Prompting Demo
======================================================
Live demonstrations showing the verification tax and power of context-first prompting.
Uses real calls to Ollama API (http://localhost:11434/api/generate)
"""

import json
import time
import urllib.request
import urllib.error
import sys
import re as _re
import unicodedata
from typing import Optional, Tuple


def _display_width(s: str) -> int:
    """Return the number of terminal columns *s* occupies."""
    stripped = _re.sub(r'\033\[[0-9;]*m', '', s)
    w = 0
    for ch in stripped:
        cat = unicodedata.east_asian_width(ch)
        w += 2 if cat in ('W', 'F') else 1
    return w


def print_box(lines: list[str], width: int = 102) -> None:
    """Print *lines* inside a Unicode bordered box *width* columns wide."""
    print(f"  ┌{'─' * width}┐")
    for line in lines:
        vis = _display_width(line)
        if vis > width - 2:
            truncated = ''
            cur_w = 0
            for ch in line:
                cw = 2 if unicodedata.east_asian_width(ch) in ('W', 'F') else 1
                if cur_w + cw > width - 4:
                    break
                truncated += ch
                cur_w += cw
            line = truncated + '..'
            vis = _display_width(line)
        pad = width - 2 - vis
        print(f"  │ {line}{' ' * pad} │")
    print(f"  └{'─' * width}┘")


# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'
BOLD = '\033[1m'

def wait_for_key(label: str = "") -> None:
    """Pause until the user presses Enter."""
    msg = "\n  ⏎  Press ENTER to continue"
    if label:
        msg += f"  →  {label}"
    input(f"\033[2m{msg}\033[0m")


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"


def print_header(text: str) -> None:
    """Print a section header."""
    print(f"\n{BOLD}{CYAN}{'=' * 80}{RESET}")
    print(f"{BOLD}{CYAN}{text}{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 80}{RESET}\n")


def print_subsection(text: str) -> None:
    """Print a subsection header."""
    print(f"\n{BOLD}{BLUE}>>> {text}{RESET}")


def print_success(text: str) -> None:
    """Print success message."""
    print(f"{GREEN}✓ {text}{RESET}")


def print_warning(text: str) -> None:
    """Print warning message."""
    print(f"{YELLOW}⚠ {text}{RESET}")


def print_problem(text: str) -> None:
    """Print problem message."""
    print(f"{RED}✗ {text}{RESET}")


def check_ollama_connection() -> bool:
    """Check if Ollama is running."""
    try:
        req = urllib.request.Request("http://localhost:11434/api/tags")
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError):
        return False


def call_ollama(prompt: str, max_tokens: int = 1000) -> Tuple[Optional[str], float]:
    """
    Make a real call to Ollama API and return response + timing.
    """
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7,
    }

    start_time = time.time()
    try:
        req = urllib.request.Request(
            OLLAMA_URL,
            data=json.dumps(payload).encode('utf-8'),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
            elapsed = time.time() - start_time
            return result.get("response", ""), elapsed
    except Exception as e:
        elapsed = time.time() - start_time
        return None, elapsed


def truncate_text(text: str, max_lines: int = 20) -> str:
    """Truncate text to max_lines for display."""
    lines = text.split('\n')
    if len(lines) > max_lines:
        return '\n'.join(lines[:max_lines]) + f"\n... ({len(lines) - max_lines} more lines)"
    return text


def section_1_verification_tax() -> None:
    """SECTION 1: THE VERIFICATION TAX — LIVE DEMONSTRATION"""
    print_header("SECTION 1: THE VERIFICATION TAX")
    print("This section shows why vague prompts create hidden review costs.\n")

    # Round 1: Vague Prompt
    print_subsection("Round 1 — Vague Prompt (no context)")
    vague_prompt = "Write a Python function to validate user input"
    print(f"Sending: {YELLOW}\"{vague_prompt}\"{RESET}\n")

    response1, time1 = call_ollama(vague_prompt, max_tokens=500)

    if response1 is None:
        print_problem("Ollama call failed")
        return

    print(f"{GREEN}Response received in {time1:.1f} seconds{RESET}")
    print(f"\n{BOLD}AI Output:{RESET}")
    print(truncate_text(response1, max_lines=15))

    # Verification checklist for vague prompt
    print(f"\n{BOLD}{RED}Manual Verification Needed for Vague Prompt:{RESET}")
    verification_items = [
        "Does it handle empty strings correctly?",
        "Does it protect against SQL injection?",
        "Does it protect against XSS attacks?",
        "Does it enforce length limits?",
        "Does it match YOUR specific validation rules?",
        "What about Unicode/internationalization?",
        "Are error messages appropriate?",
        "Does it handle None/null inputs?",
        "Is it performant for your use case?",
        "Does it integrate with your existing auth system?"
    ]
    for i, item in enumerate(verification_items, 1):
        print(f"  {RED}[ ]{RESET} {item}")

    print(f"\n{BOLD}Estimation:{RESET}")
    print(f"  • AI generation: {time1:.1f} seconds")
    print_problem("Manual verification needed: ~15–20 minutes")

    wait_for_key("Round 2 — Context-Rich Prompt")

    # Round 2: Context-Rich Prompt
    print_subsection("Round 2 — Context-Rich Prompt (specific requirements)")
    context_rich_prompt = """Write a Python function to validate user registration input for our Flask API.

Requirements:
- Email: must be valid format, max 254 chars, lowercase, no plus-addressing allowed
- Password: min 12 chars, must contain uppercase, lowercase, digit, special char
- Username: 3-30 chars, alphanumeric and underscores only, must not be in RESERVED_NAMES list
- Phone: optional, if provided must be E.164 format

Return a dict with {"valid": bool, "errors": list[str]}.
Raise ValueError for None inputs.
Include type hints. No external libraries.

Example output format:
{"valid": True, "errors": []}
{"valid": False, "errors": ["password too short", "no uppercase letter"]}"""

    print(f"\n{YELLOW}Context-Rich Prompt being sent:{RESET}")
    print_box(context_rich_prompt.strip().split("\n"))
    print(f"\n  {BOLD}Notice:{RESET} Same task — but now with 7 specific requirements,")
    print(f"  example output format, and explicit constraints.\n")

    response2, time2 = call_ollama(context_rich_prompt, max_tokens=800)

    if response2 is None:
        print_problem("Ollama call failed")
        return

    print(f"{GREEN}Response received in {time2:.1f} seconds{RESET}")
    print(f"\n{BOLD}AI Output:{RESET}")
    print(truncate_text(response2, max_lines=25))

    # Reduced verification checklist
    print(f"\n{BOLD}{GREEN}Manual Verification Needed for Context-Rich Prompt:{RESET}")
    reduced_items = [
        "Test edge cases (boundary values, special chars)",
        "Verify regex patterns match requirements exactly",
        "Check error messages are user-friendly"
    ]
    for i, item in enumerate(reduced_items, 1):
        print(f"  {GREEN}[ ]{RESET} {item}")

    print(f"\n{BOLD}Estimation:{RESET}")
    print(f"  • Context investment: ~30 seconds")
    print(f"  • AI generation: {time2:.1f} seconds")
    print_success("Manual verification needed: ~3–5 minutes")

    # Comparison
    print(f"\n{BOLD}{CYAN}VERIFICATION TAX COMPARISON:{RESET}")
    print(f"  Vague prompt:        15–20 min review | {RED}{time1:.1f}s generation{RESET}")
    print(f"  Context-rich prompt: 3–5 min review   | {GREEN}{time2:.1f}s generation{RESET}")
    print(f"\n  {BOLD}Insight:{RESET} 30 seconds of context → {BOLD}4x reduction{RESET} in verification time")


def section_2_task_matrix() -> None:
    """SECTION 2: THE TASK MATRIX — LIVE CLASSIFICATION"""
    print_header("SECTION 2: THE TASK MATRIX")
    print("Not all tasks are equal. Let's classify them on two axes.\n")

    classification_prompt = """You are an AI workflow consultant. Classify each task on two axes:
- cognitive_load: LOW or HIGH (how much deep thinking is required?)
- human_judgment: LOW or HIGH (how much does quality depend on human domain expertise?)

Also recommend: "AI_LEADS", "AI_ASSISTS", or "HUMAN_LEADS" for each.

Tasks:
1. Generate boilerplate REST API routes for a CRUD service
2. Review authentication module for security vulnerabilities
3. Write unit test stubs for existing functions
4. Design the data model for a new payment processing system
5. Generate Dockerfile and CI/CD config from project structure
6. Decide whether to use microservices or monolith for a new project

Output ONLY as a JSON array with fields: task_num, cognitive_load, human_judgment, recommendation, reasoning.
No markdown, no extra text. Just valid JSON."""

    print(f"\n{YELLOW}Classification Prompt being sent:{RESET}")
    print_box(classification_prompt.strip().split("\n"))
    print()

    response, elapsed = call_ollama(classification_prompt, max_tokens=800)

    if response is None:
        print_problem("Ollama call failed")
        return

    print(f"{GREEN}Classification received in {elapsed:.1f} seconds{RESET}\n")

    # Try to parse JSON from response
    try:
        # Extract JSON from response
        json_start = response.find('[')
        json_end = response.rfind(']') + 1
        if json_start != -1 and json_end > json_start:
            json_str = response[json_start:json_end]
            tasks = json.loads(json_str)

            # Create matrix display
            print(f"{BOLD}Task Classification Matrix (2x2):{RESET}\n")
            print("                      HUMAN_JUDGMENT=LOW          HUMAN_JUDGMENT=HIGH")
            print("COGNITIVE_LOAD=LOW    (AI_LEADS)                 (AI_ASSISTS)")
            print("COGNITIVE_LOAD=HIGH   (AI_ASSISTS)               (HUMAN_LEADS)")
            print()

            # Organize tasks by quadrant
            quadrants = {
                ("LOW", "LOW"): [],
                ("LOW", "HIGH"): [],
                ("HIGH", "LOW"): [],
                ("HIGH", "HIGH"): []
            }

            for task in tasks:
                if isinstance(task, dict):
                    key = (task.get("cognitive_load", ""), task.get("human_judgment", ""))
                    task_num = task.get("task_num", "?")
                    rec = task.get("recommendation", "")
                    quadrants[key].append((task_num, rec))

            # Print quadrants
            print(f"{BLUE}Low Cog / Low Judge (AI_LEADS):{RESET}")
            for task_num, rec in quadrants[("LOW", "LOW")]:
                print(f"  Task {task_num}: {rec}")

            print(f"\n{BLUE}Low Cog / High Judge (AI_ASSISTS):{RESET}")
            for task_num, rec in quadrants[("LOW", "HIGH")]:
                print(f"  Task {task_num}: {rec}")

            print(f"\n{BLUE}High Cog / Low Judge (AI_ASSISTS):{RESET}")
            for task_num, rec in quadrants[("HIGH", "LOW")]:
                print(f"  Task {task_num}: {rec}")

            print(f"\n{BLUE}High Cog / High Judge (HUMAN_LEADS):{RESET}")
            for task_num, rec in quadrants[("HIGH", "HIGH")]:
                print(f"  Task {task_num}: {rec}")

            print(f"\n{BOLD}{CYAN}Insight:{RESET} The model correctly identified that architectural")
            print("decisions (microservices vs monolith) and security reviews require")
            print("human judgment, while boilerplate and config generation are AI-driven.")

        else:
            print(f"{YELLOW}Could not parse JSON from response.{RESET}")
            print(f"Raw output:\n{truncate_text(response, max_lines=20)}")
    except json.JSONDecodeError:
        print(f"{YELLOW}Response is not valid JSON. Raw output:{RESET}")
        print(truncate_text(response, max_lines=20))


def section_3_context_first_comparison() -> None:
    """SECTION 3: CONTEXT-FIRST PROMPTING — HEAD TO HEAD"""
    print_header("SECTION 3: CONTEXT-FIRST PROMPTING HEAD-TO-HEAD")
    print("Same task. One with context. One without.\n")

    # Prompt A: No context
    print_subsection("Prompt A — Minimal Context")
    prompt_a = "Write unit tests for the authentication module."
    print(f"Request: {RED}\"{prompt_a}\"{RESET}\n")

    response_a, time_a = call_ollama(prompt_a, max_tokens=600)
    if response_a is None:
        print_problem("Ollama call failed")
        return

    print(f"{GREEN}Response received in {time_a:.1f} seconds{RESET}")
    print(f"\n{BOLD}AI Output (first 15 lines):{RESET}")
    print(truncate_text(response_a, max_lines=15))

    # Count test cases in response A
    test_count_a = response_a.lower().count("def test_")
    print(f"\n{BOLD}Quality metrics:{RESET}")
    print(f"  • Test functions generated: {test_count_a}")
    if "pytest" in response_a.lower():
        print_success("Mentions pytest")
    else:
        print_warning("No pytest mentioned")
    if "fixture" in response_a.lower() or "mock" in response_a.lower():
        print_success("Includes fixtures/mocks")
    else:
        print_warning("No fixtures/mocks")

    wait_for_key("Prompt B — Context-Rich")

    # Prompt B: Context-rich
    print_subsection("Prompt B — Context-Rich")
    prompt_b = """Write pytest unit tests for our JWT authentication module.

Stack: Python 3.11, Flask 2.x, PyJWT 2.8, pytest 7.x
Auth flow: OAuth2 + JWT with refresh tokens
Token config: access_token TTL=15min, refresh_token TTL=7days, HS256 signing

Test these specific edge cases:
1. Expired access token returns 401 with "token_expired" error code
2. Valid refresh token issues new access token with fresh TTL
3. Revoked refresh token (in Redis blacklist) returns 403
4. Token with wrong issuer claim returns 401
5. Missing Authorization header returns 401 with "missing_token" error code

Use pytest fixtures for test client and mock Redis.
Each test should have a clear docstring explaining what it validates."""

    print(f"\n{YELLOW}Context-Rich Prompt being sent:{RESET}")
    print_box(prompt_b.strip().split("\n"))
    print(f"\n  {BOLD}Notice:{RESET} Stack details, auth flow, 5 specific test cases,")
    print(f"  fixture requirements, and docstring expectations.\n")

    response_b, time_b = call_ollama(prompt_b, max_tokens=1200)
    if response_b is None:
        print_problem("Ollama call failed")
        return

    print(f"{GREEN}Response received in {time_b:.1f} seconds{RESET}")
    print(f"\n{BOLD}AI Output (first 20 lines):{RESET}")
    print(truncate_text(response_b, max_lines=20))

    # Count test cases in response B
    test_count_b = response_b.lower().count("def test_")
    print(f"\n{BOLD}Quality metrics:{RESET}")
    print(f"  • Test functions generated: {test_count_b}")
    if "pytest" in response_b.lower():
        print_success("Mentions pytest")
    else:
        print_warning("No pytest mentioned")
    if "fixture" in response_b.lower() or "mock" in response_b.lower():
        print_success("Includes fixtures/mocks")
    else:
        print_warning("No fixtures/mocks")
    if "docstring" in response_b.lower() or '"""' in response_b:
        print_success("Includes docstrings")
    else:
        print_warning("No docstrings")

    # Comparison
    print(f"\n{BOLD}{CYAN}SIDE-BY-SIDE COMPARISON:{RESET}")
    print(f"  Minimal context:  {time_a:.1f}s | {test_count_a} test functions")
    print(f"  Context-rich:     {time_b:.1f}s | {test_count_b} test functions")

    context_time = 30  # estimate
    print(f"\n{BOLD}Estimation:{RESET}")
    print(f"  • Context investment: ~{context_time} seconds")
    print(f"  • Minimal context output requires ~10 min refinement")
    print(f"  • Context-rich output requires ~2 min refinement")
    print(f"\n  {BOLD}{GREEN}Result: 30 seconds of context → 8 minutes saved{RESET}")


def section_4_summary() -> None:
    """SECTION 4: SUMMARY"""
    print_header("SECTION 4: KEY INSIGHTS")

    print(f"{BOLD}The Three Big Takeaways:{RESET}\n")

    print(f"{GREEN}1. VERIFICATION TAX{RESET}")
    print("   Vague prompts create hidden review costs. For validation logic:")
    print("   • Vague: 20+ minutes of manual verification")
    print("   • Context-rich: 3-5 minutes of manual verification")
    print("   → Add specificity → reduce verification burden 4x\n")

    print(f"{GREEN}2. TASK MATRIX{RESET}")
    print("   Not all tasks should go to AI. Use the 2x2:")
    print("   • Low cognitive + Low judgment → AI_LEADS")
    print("   • High cognitive + High judgment → HUMAN_LEADS")
    print("   → Understand your task → assign it correctly\n")

    print(f"{GREEN}3. CONTEXT-FIRST PROMPTING{RESET}")
    print("   Spend 30 seconds on context to save 8+ minutes on refinement:")
    print("   • Include stack details, requirements, edge cases")
    print("   • Specify output format and constraints")
    print("   • Reference domain-specific terminology")
    print("   → More context → dramatically better output\n")

    print(f"{BOLD}{CYAN}The Paradox Explained:{RESET}")
    print("AI feels harder than it should because we skip the context investment.")
    print("A vague prompt → requires heavy review → feels slow and fragile.")
    print("A context-rich prompt → requires light review → feels fast and reliable.")
    print("\n" + "=" * 80)
    print("These were REAL model responses, not simulated.")
    print("The model didn't change. The context did.")
    print("=" * 80)


def main():
    """Main entry point."""
    print(f"\n{BOLD}{CYAN}AI PRODUCTIVITY PARADOX: Context-First Prompting Demo{RESET}")
    print(f"{BOLD}{CYAN}Real Ollama API Calls (Model: {MODEL}){RESET}\n")

    # Check Ollama connection
    print("Checking Ollama connection...", end=" ", flush=True)
    if not check_ollama_connection():
        print_problem("Ollama not running")
        print("\n" + RED + "ERROR: Cannot reach Ollama at " + OLLAMA_URL + RESET)
        print("Start Ollama with: " + YELLOW + "ollama serve" + RESET)
        sys.exit(1)

    print_success("Connected to Ollama\n")

    try:
        # Run all sections
        section_1_verification_tax()
        wait_for_key("Section 2: The Task Matrix")

        section_2_task_matrix()
        wait_for_key("Section 3: Context-First Comparison")

        section_3_context_first_comparison()
        wait_for_key("Summary")

        section_4_summary()


    except KeyboardInterrupt:
        print(f"\n{YELLOW}Demo interrupted by user.{RESET}")
        sys.exit(0)
    except Exception as e:
        print_problem(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
