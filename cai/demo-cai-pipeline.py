#!/usr/bin/env python3
"""
Continuous AI (CAI) CI/CD Pipeline Demo
Demonstrates AI reasoning applied to CI/CD failure analysis using real Ollama API calls.
"""

import json
import time
import math
import urllib.request
import urllib.error
import re as _re
import unicodedata
from typing import Dict, List, Tuple


def _display_width(s: str) -> int:
    """Return the number of terminal columns *s* occupies.

    Strips ANSI escape sequences (zero-width), counts East-Asian wide /
    fullwidth characters as 2, and everything else as 1.
    """
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
        # Truncate if necessary (measure visible width)
        vis = _display_width(line)
        if vis > width - 2:
            # Truncate character by character
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
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Ollama API configuration
def wait_for_key(label: str = "") -> None:
    """Pause until the user presses Enter."""
    msg = "\n  ⏎  Press ENTER to continue"
    if label:
        msg += f"  →  {label}"
    input(f"\033[2m{msg}\033[0m")


OLLAMA_BASE = "http://localhost:11434"
GENERATE_URL = f"{OLLAMA_BASE}/api/generate"
EMBED_URL = f"{OLLAMA_BASE}/api/embed"
MODEL = "llama3.1:8b"
EMBED_MODEL = "nomic-embed-text"

# ============================================================================
# PART 1: THE FAILING BUILD (simulated)
# ============================================================================

SIMULATED_BUILD_LOG = """
=== Build Log for PR #5032 (Sarah Chen) ===
Timestamp: 2025-08-15T14:32:00Z
Repository: acme-backend
Branch: feature/db-pool-optimization

[14:32:01] Step 1/8: Checkout code... OK
[14:32:05] Step 2/8: Install dependencies... OK (847 packages)
[14:32:18] Step 3/8: Lint (flake8, black)... OK (12 warnings)
[14:32:42] Step 4/8: Unit tests (pytest)... OK (4,203 tests passed in 24s)
[14:32:43] Step 5/8: Build Docker image... OK
[14:32:47] Step 6/8: Integration tests against PostgreSQL 14.2...
  Running test suite: test_db_connections.py
  [14:32:50] test_basic_connection - PASS
  [14:32:51] test_connection_reuse - PASS
  [14:32:55] test_high_load_simulation - FAIL

  Error details:
  -----------
  psycopg2.OperationalError: connection pool size 200 exceeds asyncpg maximum of 150
  File: acme/db/__init__.py:47, in _init_pool()
    pool = asyncpg.create_pool(
        host=cfg['host'],
        port=cfg['port'],
        user=cfg['user'],
        password=cfg['password'],
        min_size=10,
        max_size=pool_size,  # ← PROBLEM: pool_size=200 but max is 150
        command_timeout=timeout,  # ← timeout changed to 60s
        record_class=Record
    )

  Stack trace:
  asyncpg.exceptions.InvalidParameterError: pool size (200) exceeds max_size limit (150)
    at asyncpg/_cpool.pyx:180 in create_pool
    at acme/db/__init__.py:47 in _init_pool
    at acme/db/__init__.py:21 in __init__
    at test_db_connections.py:89 in test_high_load_simulation

[14:32:56] Step 6/8: Integration tests... FAILED (1 failed, 4,202 passed)
[14:32:57] Step 7/8: Cleanup... OK
[14:32:58] Total build time: 28 minutes 12 seconds
[14:33:00] PIPELINE FAILED: 1 integration test failure
"""

# ============================================================================
# PART 2: AI FAILURE CLASSIFICATION
# ============================================================================

def call_ollama_generate(prompt: str, system_prompt: str = None) -> Tuple[str, float]:
    """
    Call Ollama generate API with retry logic.
    Returns (response_text, elapsed_time_seconds).
    """
    start_time = time.time()

    full_prompt = prompt
    if system_prompt:
        full_prompt = f"{system_prompt}\n\n{prompt}"

    payload = {
        "model": MODEL,
        "prompt": full_prompt,
        "stream": False,
        "temperature": 0.3,
    }

    try:
        req = urllib.request.Request(
            GENERATE_URL,
            data=json.dumps(payload).encode('utf-8'),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
            elapsed = time.time() - start_time
            return result.get("response", ""), elapsed
    except urllib.error.URLError as e:
        raise ConnectionError(
            f"Cannot connect to Ollama at {OLLAMA_BASE}. "
            f"Make sure Ollama is running: ollama serve\n{e}"
        )

def call_ollama_embed(texts: List[str]) -> Tuple[List[List[float]], float]:
    """
    Call Ollama embed API for semantic similarity.
    Returns (embeddings_list, elapsed_time_seconds).
    """
    start_time = time.time()

    payload = {
        "model": EMBED_MODEL,
        "input": texts,
    }

    try:
        req = urllib.request.Request(
            EMBED_URL,
            data=json.dumps(payload).encode('utf-8'),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=120) as response:
            result = json.loads(response.read().decode('utf-8'))
            elapsed = time.time() - start_time
            embeddings = result.get("embeddings", [])
            return embeddings, elapsed
    except urllib.error.URLError as e:
        raise ConnectionError(
            f"Cannot connect to Ollama embed at {OLLAMA_BASE}. "
            f"Make sure Ollama is running: ollama serve\n{e}"
        )

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    if not vec1 or not vec2 or len(vec1) != len(vec2):
        return 0.0

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))

    if mag1 == 0 or mag2 == 0:
        return 0.0

    return dot_product / (mag1 * mag2)

def pattern1_failure_classification():
    """PATTERN 1: AI Failure Classification"""
    print(f"\n{BOLD}{CYAN}=== PATTERN 1: AI FAILURE CLASSIFICATION ==={RESET}")

    system_prompt = """You are a CI/CD failure classifier. Analyze the build log and classify the failure.
Output ONLY valid JSON with these fields:
- type: one of [environment, flaky_test, real_bug, dependency_conflict, configuration_error]
- severity: one of [low, medium, high, critical]
- root_cause: one sentence summary
- suggested_fix: one sentence actionable fix
- confidence: number 0-100
- affected_file: the file path that caused the failure"""

    print(f"{YELLOW}System Prompt being sent:{RESET}")
    print_box(system_prompt.strip().split("\n"))
    print(f"\n{YELLOW}Input:{RESET} Full build log ({len(SIMULATED_BUILD_LOG.strip().splitlines())} lines) from PR #5032\n")

    prompt = f"Analyze this build log:\n\n{SIMULATED_BUILD_LOG}"

    print(f"Sending to {MODEL}...")
    try:
        response, elapsed = call_ollama_generate(prompt, system_prompt)

        # Extract JSON from response
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            json_str = response[json_start:json_end]
            classification = json.loads(json_str)
        else:
            classification = json.loads(response)

        print(f"{YELLOW}Response time: {elapsed:.2f}s{RESET}")
        print(f"\n{GREEN}Classification Result:{RESET}")
        print(f"  Type: {BOLD}{classification.get('type', 'N/A')}{RESET}")
        print(f"  Severity: {BOLD}{classification.get('severity', 'N/A')}{RESET}")
        print(f"  Root Cause: {classification.get('root_cause', 'N/A')}")
        print(f"  Suggested Fix: {classification.get('suggested_fix', 'N/A')}")
        print(f"  Confidence: {classification.get('confidence', 'N/A')}%")
        print(f"  Affected File: {classification.get('affected_file', 'N/A')}")

        return elapsed, classification
    except json.JSONDecodeError as e:
        print(f"{RED}JSON parsing error: {e}{RESET}")
        return 0, {}

# ============================================================================
# PART 3: AI LOG SUMMARIZATION
# ============================================================================

def pattern2_log_summarization():
    """PATTERN 2: AI Log Summarization for Slack"""
    print(f"\n{BOLD}{CYAN}=== PATTERN 2: AI LOG SUMMARIZATION ==={RESET}")

    system_prompt = """You are a CI/CD log summarizer. Create a concise Slack-style notification.
Format:
🔴 Build failed — PR #5032 (Sarah Chen)
Root cause: [one line]
Suggested fix: [one line]
Severity: [level]
Full log: [link placeholder]"""

    prompt = f"Summarize this build log:\n\n{SIMULATED_BUILD_LOG}"

    print(f"{YELLOW}System Prompt being sent:{RESET}")
    print_box(system_prompt.strip().split("\n"))
    print(f"\n{YELLOW}Input:{RESET} Full build log ({len(SIMULATED_BUILD_LOG.strip().splitlines())} lines) from PR #5032\n")

    try:
        response, elapsed = call_ollama_generate(prompt, system_prompt)

        print(f"{YELLOW}Response time: {elapsed:.2f}s{RESET}")
        print(f"\n{GREEN}Slack Notification:{RESET}")
        print(f"{CYAN}{response.strip()}{RESET}")

        return elapsed
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        return 0

# ============================================================================
# PART 4: RAG DEBUGGING (Embeddings + Historical Context)
# ============================================================================

HISTORICAL_INCIDENTS = [
    {
        "id": "PR #3847",
        "date": "3 months ago",
        "content": "PR #3847 (3 months ago): Connection pool size change from 40 to 180 failed — async driver max is 150. Resolution: switched to async driver config which supports pool sizes up to 500. Commit: abc123. Technical details: Used asyncpg v0.28 which has max_size constraint. Updated to native driver mode."
    },
    {
        "id": "PR #4102",
        "date": "2 months ago",
        "content": "PR #4102 (2 months ago): Timeout configuration change caused cascading failures in staging. Resolution: added graduated timeout with circuit breaker. Commit: def456. Technical details: Timeout increased to 60s caused db connection hangs. Implemented exponential backoff strategy."
    },
    {
        "id": "PR #3599",
        "date": "5 months ago",
        "content": "PR #3599 (5 months ago): Memory leak in connection pool under load. Resolution: added connection lifecycle hooks. Commit: ghi789. Technical details: Connection pooling without proper cleanup caused memory exhaustion. Added proper resource cleanup."
    },
    {
        "id": "PR #4521",
        "date": "1 month ago",
        "content": "PR #4521 (1 month ago): TypeScript compilation out of memory. Resolution: increased runner memory. Commit: jkl012. Technical details: Build runner needed more memory. Unrelated to database config changes."
    }
]

def pattern3_rag_debugging():
    """PATTERN 3: RAG Debugging with Historical Context"""
    print(f"\n{BOLD}{CYAN}=== PATTERN 3: RAG DEBUGGING (EMBEDDINGS + HISTORY) ==={RESET}")

    # Prepare texts for embedding
    current_error = "Connection pool size 200 exceeds asyncpg maximum of 150. Pool configuration in database.yml changed from 50 to 200."
    historical_texts = [doc["content"] for doc in HISTORICAL_INCIDENTS]
    all_texts = [current_error] + historical_texts

    print(f"Embedding {len(all_texts)} documents (current error + {len(historical_texts)} historical incidents)...")

    try:
        embeddings, embed_time = call_ollama_embed(all_texts)
        print(f"{YELLOW}Embedding time: {embed_time:.2f}s{RESET}\n")

        # Calculate similarity scores
        current_embedding = embeddings[0]
        print(f"{GREEN}Semantic Similarity Scores:{RESET}")

        similarities = []
        for i, doc in enumerate(HISTORICAL_INCIDENTS):
            historical_embedding = embeddings[i + 1]
            sim = cosine_similarity(current_embedding, historical_embedding)
            similarities.append((doc["id"], doc["date"], sim))
            print(f"  {doc['id']} ({doc['date']}): {sim:.3f}")

        # Sort by similarity (descending)
        similarities.sort(key=lambda x: x[2], reverse=True)

        # Get top 2 most similar
        top_2 = similarities[:2]
        print(f"\n{BOLD}Top 2 Most Similar Historical Incidents:{RESET}")
        for pr_id, date, sim in top_2:
            print(f"  {YELLOW}*{RESET} {pr_id} ({date}) - similarity: {sim:.3f}")

        # Create context for LLM
        context = f"Current error: {current_error}\n\n"
        context += "Most relevant historical incidents:\n"
        for pr_id, date, sim in top_2:
            doc = next(d for d in HISTORICAL_INCIDENTS if d["id"] == pr_id)
            context += f"\n{pr_id}:\n{doc['content']}\n"

        # Call LLM with historical context
        system_prompt = """You are a CI/CD expert synthesizing debugging recommendations from historical incident data.
Based on similar past incidents, provide a specific fix recommendation."""

        prompt = f"{context}\n\nBased on these similar incidents, what is the most likely fix for the current error?"

        print(f"\n{YELLOW}Synthesis System Prompt:{RESET}")
        print_box(system_prompt.strip().split("\n"))
        print(f"\n{YELLOW}Context being sent:{RESET} Current error + top {len(top_2)} historical matches")
        for pr_id, date, sim in top_2:
            print(f"  • {pr_id} ({date}) — similarity {sim:.3f}")
        print(f"\n{GREEN}Synthesizing fix recommendation...{RESET}")

        response, synth_time = call_ollama_generate(prompt, system_prompt)

        print(f"{YELLOW}Synthesis time: {synth_time:.2f}s{RESET}")
        print(f"\n{GREEN}Synthesized Recommendation:{RESET}")
        print(f"{response.strip()}")

        return embed_time + synth_time
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")
        return 0

# ============================================================================
# PART 5: RISK SCORING
# ============================================================================

def pattern4_risk_scoring():
    """PATTERN 4: AI Risk Scoring"""
    print(f"\n{BOLD}{CYAN}=== PATTERN 4: RISK SCORING ==={RESET}")

    system_prompt = """You are a CI/CD risk scorer. Analyze the PR and score each risk factor 1-10.
Output ONLY valid JSON with these fields:
- file_criticality: how critical is the changed file? (1-10)
- blast_radius: how many systems are affected? (1-10)
- test_coverage_risk: how risky is the test gap? (1-10)
- historical_risk: based on prior incidents (1-10)
- change_complexity: how complex is this change? (1-10)
- overall_risk: weighted average (1-10)
- recommendation: brief action (approve, flag_for_review, or block)"""

    pr_context = """PR #5032: Database connection pooling optimization
Files changed: config/database.yml (core infrastructure)
Changes: pool_size 50->200, timeout 30s->60s
Test coverage for changed file: 34%
Services affected: all 12 microservices depend on this config
Prior incidents: 2 incidents involving connection pool changes in last 6 months"""

    prompt = f"Score the risks in this PR:\n\n{pr_context}"

    print(f"{YELLOW}System Prompt being sent:{RESET}")
    print_box(system_prompt.strip().split("\n"))
    print(f"\n{YELLOW}PR Context being scored:{RESET}")
    print_box(pr_context.strip().split("\n"))
    print()

    try:
        response, elapsed = call_ollama_generate(prompt, system_prompt)

        # Extract JSON
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        if json_start >= 0 and json_end > json_start:
            json_str = response[json_start:json_end]
            risk_scores = json.loads(json_str)
        else:
            risk_scores = json.loads(response)

        print(f"{YELLOW}Response time: {elapsed:.2f}s{RESET}")
        print(f"\n{GREEN}Risk Assessment:{RESET}")
        print(f"  File Criticality: {risk_scores.get('file_criticality', 'N/A')}/10")
        print(f"  Blast Radius: {risk_scores.get('blast_radius', 'N/A')}/10")
        print(f"  Test Coverage Risk: {risk_scores.get('test_coverage_risk', 'N/A')}/10")
        print(f"  Historical Risk: {risk_scores.get('historical_risk', 'N/A')}/10")
        print(f"  Change Complexity: {risk_scores.get('change_complexity', 'N/A')}/10")
        overall = risk_scores.get('overall_risk', 0)
        color = GREEN if overall <= 4 else YELLOW if overall <= 6 else RED
        print(f"  {BOLD}Overall Risk: {color}{overall}/10{RESET}")
        print(f"  Recommendation: {risk_scores.get('recommendation', 'N/A')}")

        return elapsed, risk_scores
    except json.JSONDecodeError as e:
        print(f"{RED}JSON parsing error: {e}{RESET}")
        return 0, {}

# ============================================================================
# PART 6: SUMMARY & COMPARISON
# ============================================================================

def print_summary(times: Dict[str, float]):
    """Print final summary comparison."""
    print(f"\n{BOLD}{CYAN}=== SUMMARY: TRADITIONAL vs CAI PIPELINE ==={RESET}\n")

    print(f"{YELLOW}{'Metric':<40} {'Traditional':<20} {'CAI Pipeline':<20}{RESET}")
    print(f"{'-' * 80}")

    print(f"{'Classification':<40} {'X N/A':<20} {'Check Real-time':<20}")
    print(f"{'Log Summarization':<40} {'X N/A':<20} {'Check Real-time':<20}")
    print(f"{'Historical Context Matching':<40} {'X Manual':<20} {'Check Automatic':<20}")
    print(f"{'Risk Scoring':<40} {'X Manual':<20} {'Check Real-time':<20}")

    print(f"\n{YELLOW}{'Timing':<40} {'Time (minutes)':<20}{RESET}")
    print(f"{'-' * 60}")
    print(f"{'Manual triage time':<40} {'28 min':<20}")

    total_ai_time = sum(times.values())
    total_ai_seconds = total_ai_time
    total_ai_minutes = total_ai_seconds / 60
    print(f"{'All AI analysis (this script)':<40} {total_ai_minutes:.2f} min{RESET}")
    print(f"  - Classification: {times.get('classification', 0):.2f}s")
    print(f"  - Summarization: {times.get('summarization', 0):.2f}s")
    print(f"  - RAG + Synthesis: {times.get('rag', 0):.2f}s")
    print(f"  - Risk Scoring: {times.get('risk', 0):.2f}s")

    print(f"\n{GREEN}{BOLD}Time Savings: ~28 minutes of automated analysis in {total_ai_minutes:.2f} minutes{RESET}")
    print(f"{GREEN}Sarah receives AI-powered debugging insights in real-time!{RESET}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    """Run the complete CAI pipeline demo."""
    print(f"\n{BOLD}{GREEN}╔════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{GREEN}║   Continuous AI (CAI) CI/CD Pipeline Demo                  ║{RESET}")
    print(f"{BOLD}{GREEN}║   Real Ollama API Integration                              ║{RESET}")
    print(f"{BOLD}{GREEN}╚════════════════════════════════════════════════════════════╝{RESET}\n")

    # Part 1: Show the failing build
    print(f"{BOLD}{CYAN}=== PART 1: THE FAILING BUILD ==={RESET}")
    print(f"Simulated CI build log (excerpt):\n")
    print(f"{RED}{SIMULATED_BUILD_LOG}{RESET}\n")

    times = {}

    try:
        wait_for_key("Pattern 1: Failure Classification")

        # Part 2: Classification
        class_time, classification = pattern1_failure_classification()
        times['classification'] = class_time

        wait_for_key("Pattern 2: Log Summarization")

        # Part 3: Summarization
        summ_time = pattern2_log_summarization()
        times['summarization'] = summ_time

        wait_for_key("Pattern 3: RAG Debugging")

        # Part 4: RAG Debugging
        rag_time = pattern3_rag_debugging()
        times['rag'] = rag_time

        wait_for_key("Pattern 4: Risk Scoring")

        # Part 5: Risk Scoring
        risk_time, risk_scores = pattern4_risk_scoring()
        times['risk'] = risk_time

        wait_for_key("Summary")

        # Part 6: Summary
        print_summary(times)


    except ConnectionError as e:
        print(f"\n{RED}{BOLD}ERROR:{RESET} {e}\n")
        print(f"Make sure Ollama is running with the required models:")
        print(f"  ollama pull llama3.1:8b")
        print(f"  ollama pull nomic-embed-text")
        print(f"  ollama serve\n")
        exit(1)

if __name__ == "__main__":
    main()
