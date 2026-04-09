#!/usr/bin/env python3
"""
Context Engineering Demo: Live Ollama API Integration
======================================================
Live demonstration of "Most AI failures are context problems, not model problems"

This script makes REAL HTTP calls to a local Ollama instance to show how identical
model, identical question, but different context produces dramatically different results.

The running example: A login authentication token refresh bug in production.
The lesson: The model isn't stupid. The context was incomplete.

Usage: python3 demo-context-engine.py
Requires: ollama serve running on localhost:11434
"""

import urllib.request
import urllib.error
import json
import time
import math
import sys
import re as _re
import unicodedata
from typing import List, Tuple, Dict, Any


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
            # Tokenize into (text, ansi_escape) chunks so we can truncate
            # while preserving color codes
            parts = _re.split(r'(\033\[[0-9;]*m)', line)
            truncated = ''
            cur_w = 0
            for part in parts:
                if _re.match(r'\033\[[0-9;]*m', part):
                    truncated += part          # zero-width — always keep
                    continue
                for ch in part:
                    cw = 2 if unicodedata.east_asian_width(ch) in ('W', 'F') else 1
                    if cur_w + cw > width - 4:
                        break
                    truncated += ch
                    cur_w += cw
                else:
                    continue
                break
            line = truncated + RESET + '..'
            vis = _display_width(line)
        pad = width - 2 - vis
        print(f"  │ {line}{' ' * pad} │")
    print(f"  └{'─' * width}┘")


# ANSI color codes for terminal output
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def wait_for_key(label: str = "") -> None:
    """Pause until the user presses Enter."""
    msg = f"\n  ⏎  Press ENTER to continue"
    if label:
        msg += f"  →  {label}"
    input(f"\033[2m{msg}\033[0m")


OLLAMA_API_BASE = "http://localhost:11434/api"
GENERATION_MODEL = "llama3.1:8b"
EMBED_MODEL = "nomic-embed-text"

# Global metrics storage
metrics = {
    "round1": {"time": 0, "tokens": 0},
    "round2": {"time": 0, "tokens": 0},
    "round3": {"time": 0, "tokens": 0},
}


def check_ollama_connection():
    """Verify Ollama is running and accessible."""
    try:
        req = urllib.request.Request(f"{OLLAMA_API_BASE}/tags")
        with urllib.request.urlopen(req, timeout=2) as response:
            data = json.loads(response.read().decode())
            return True, data
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
        return False, str(e)


def call_ollama_generate(prompt: str, system_prompt: str = "", context: str = "") -> Tuple[str, int, float]:
    """
    Make a real HTTP call to Ollama's generate API.
    Returns: (response_text, token_count, response_time)
    """
    full_prompt = prompt
    if system_prompt or context:
        full_prompt = f"{system_prompt}\n\n{context}\n\nQuestion: {prompt}"

    payload = {
        "model": GENERATION_MODEL,
        "prompt": full_prompt,
        "stream": False,
        "temperature": 0.7,
        "num_predict": 500,
    }

    start_time = time.time()

    try:
        req = urllib.request.Request(
            f"{OLLAMA_API_BASE}/generate",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode())
            elapsed = time.time() - start_time

            response_text = result.get("response", "")
            eval_count = result.get("eval_count", 0)

            return response_text, eval_count, elapsed
    except urllib.error.URLError as e:
        raise ConnectionError(f"Failed to connect to Ollama: {e}")


def call_ollama_embed(texts: List[str]) -> List[List[float]]:
    """
    Make real HTTP calls to Ollama's embed API for text embeddings.
    Returns: List of embedding vectors
    """
    embeddings = []
    for text in texts:
        payload = {
            "model": EMBED_MODEL,
            "input": text,
        }

        try:
            req = urllib.request.Request(
                f"{OLLAMA_API_BASE}/embed",
                data=json.dumps(payload).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode())
                embeddings.append(result.get("embeddings", [[]])[0])
        except urllib.error.URLError as e:
            raise ConnectionError(f"Failed to embed text: {e}")

    return embeddings


def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    if not vec_a or not vec_b:
        return 0.0

    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = math.sqrt(sum(a * a for a in vec_a))
    mag_b = math.sqrt(sum(b * b for b in vec_b))

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot_product / (mag_a * mag_b)


def print_header():
    """Print demo header and connection status."""
    print(f"\n{BOLD}{CYAN}")
    print("=" * 80)
    print("CONTEXT ENGINEERING DEMO: Live Ollama API Demonstration")
    print("=" * 80)
    print(f"{RESET}")
    print(f"Thesis: {BOLD}Most AI failures are context problems, not model problems{RESET}")
    print(f"Example: The Login Bug in Production\n")

    # Check Ollama connection
    connected, info = check_ollama_connection()
    if connected:
        print(f"{GREEN}✓ Ollama is running (localhost:11434){RESET}")
        print(f"  Models checked: {GENERATION_MODEL} and {EMBED_MODEL}\n")
    else:
        print(f"{RED}✗ Ollama connection failed: {info}{RESET}")
        print(f"  Start Ollama with: {BOLD}ollama serve{RESET}")
        sys.exit(1)


def round_1_naive_prompt():
    """ROUND 1: Vague prompt with NO context"""
    print(f"\n{RED}{BOLD}ROUND 1: NAIVE PROMPT{RESET}")
    print("-" * 80)
    print("Approach: Vague question, no system prompt, no context")
    print(f"Model: {GENERATION_MODEL}")
    print(f"Prompt: {BOLD}\"Fix the login bug\"{RESET}\n")

    prompt = "Fix the login bug"

    # SHOW the audience what we're sending — nothing!
    print(f"{RED}SYSTEM PROMPT: (none){RESET}")
    print(f"{RED}CONTEXT: (none){RESET}")
    print(f"{RED}QUESTION:{RESET} \"{prompt}\"")
    print(f"\n  The model gets a bare question with zero information about our system.\n")

    print("Calling Ollama API...")
    response, tokens, elapsed = call_ollama_generate(prompt)

    metrics["round1"]["time"] = elapsed
    metrics["round1"]["tokens"] = tokens

    print(f"\n{RED}Response:{RESET}")
    print("-" * 80)
    print(response)
    print("-" * 80)
    print(f"\nMetrics:")
    print(f"  Response time: {elapsed:.2f}s")
    print(f"  Tokens generated: {tokens}")
    print(f"  Quality: {RED}Generic, vague, unhelpful{RESET}")
    print(f"\n{RED}Problem: Model is flying blind. Could mean anything.{RESET}")

    wait_for_key()


def round_2_structured_context():
    """ROUND 2: Same question with rich system prompt and structured context"""
    print(f"\n\n{YELLOW}{BOLD}ROUND 2: STRUCTURED CONTEXT{RESET}")
    print("-" * 80)
    print("Approach: System prompt + structured XML context")
    print(f"Model: {GENERATION_MODEL} (same as Round 1)")
    print(f"Prompt: {BOLD}\"Fix the login bug\"{RESET} (same as Round 1)\n")

    system_prompt = """You are a senior backend engineer specializing in Python/Flask authentication systems.
Diagnose issues precisely. Reference specific code, line numbers, and config values.
Be concise and actionable."""

    context = """
<system_prompt>You are a senior backend engineer specializing in Python/Flask authentication systems. Diagnose issues precisely. Reference specific code, line numbers, and config values. Be concise and actionable.</system_prompt>

<error_log>
2026-04-09 03:14:22 ERROR auth.token_manager: TokenRefreshError
Traceback: token_manager.py line 142, in refresh()
  jwt.decode(token, key, algorithms=["HS256"])
jwt.ExpiredSignatureError: Signature has expired
Affected users: 342 in last hour (cluster: us-east-1)
Pattern: tokens issued before 02:00 UTC failing after rotation
</error_log>

<code_context>
# token_manager.py lines 138-155
def refresh(self, token):
    decoded = jwt.decode(token, self.signing_key, algorithms=["HS256"])
    # BUG: uses current key, not the key that signed the original token
    # Key rotation at 02:00 UTC invalidated all pre-rotation tokens
    new_token = jwt.encode({**decoded, "exp": time.time() + 3600}, self.signing_key)
    return new_token
</code_context>

<user_state>
Sessions affected: 342 active, all tokens issued pre-02:00 UTC
Key rotation event: 02:00:00 UTC (signing_key_v3 → signing_key_v4)
Current error rate: 12.4% of auth requests failing
</user_state>
"""

    prompt = "Fix the login bug"

    # SHOW the audience what we're sending
    print(f"{YELLOW}SYSTEM PROMPT being sent:{RESET}")
    print_box(system_prompt.strip().split("\n"))

    print(f"\n{YELLOW}STRUCTURED XML CONTEXT being sent:{RESET}")
    print_box(context.strip().split("\n"))

    print(f"\n{YELLOW}QUESTION:{RESET} \"{prompt}\" (same as Round 1)")
    print(f"\n  Notice: Same question, but now the model has error logs, code, and user state.\n")

    print("Calling Ollama API with structured context...")
    response, tokens, elapsed = call_ollama_generate(prompt, system_prompt, context)

    metrics["round2"]["time"] = elapsed
    metrics["round2"]["tokens"] = tokens

    print(f"\n{YELLOW}Response:{RESET}")
    print("-" * 80)
    print(response)
    print("-" * 80)
    print(f"\nMetrics:")
    print(f"  Response time: {elapsed:.2f}s")
    print(f"  Tokens generated: {tokens}")
    print(f"  Quality: {YELLOW}Specific, references code, suggests actionable fix{RESET}")
    print(f"\n{YELLOW}Win: Same model, same question, VASTLY better response.{RESET}")

    wait_for_key()


def round_3_full_context_engine():
    """ROUND 3: Full context engine with retrieval, embedding, and ranking"""
    print(f"\n\n{GREEN}{BOLD}ROUND 3: FULL CONTEXT ENGINE{RESET}")
    print("-" * 80)
    print("Approach: Real embedding-based retrieval + context ranking + structured prompt")
    print(f"Model: {GENERATION_MODEL} (same as Rounds 1 & 2)\n")

    # Step 1: Knowledge base documents
    knowledge_base = [
        {
            "id": "doc_1",
            "title": "JWT Key Rotation Best Practices",
            "content": """JWT key rotation requires a grace period to handle in-flight tokens.
    CRITICAL: During rotation, validate tokens against BOTH the old and new keys.
    Implement a dual-key validation window (typically 5-15 minutes).
    Store key versions with each token. Example: encode version in 'kid' (Key ID) claim.
    Check: Is your refresh() method only using current_key or also checking previous_key?""",
        },
        {
            "id": "doc_2",
            "title": "Token Expiration vs Signature Validation",
            "content": """Expired token signature errors indicate the key used to sign the original token is no longer available.
    jwt.ExpiredSignatureError during refresh() means: token was signed with old key, current key doesn't match.
    Solution: Keep a small cache of recent keys (5-10 versions). Identify the key version from token metadata.
    Pattern: If all failures happened after a specific timestamp, suspect key rotation.""",
        },
        {
            "id": "doc_3",
            "title": "Debugging Token Refresh Failures",
            "content": """Production incident: Token refresh failures in waves = likely root cause is a change to signing infrastructure.
    Step 1: Check if key rotation or signing key update happened near error spike
    Step 2: Verify the exact time of the change vs time of first error
    Step 3: Check if pre-rotation tokens are being rejected by post-rotation validation
    Action: Look at token_manager.py refresh() method. Does it need to handle key rotation gracefully?""",
        },
        {
            "id": "doc_noise_1",
            "title": "Database Connection Pooling",
            "content": """Connection pooling reduces latency by maintaining persistent DB connections.
    Configure pool size: min=5, max=20 based on your workload. Monitor pool exhaustion.
    This is about database performance, not authentication tokens.""",
        },
        {
            "id": "doc_noise_2",
            "title": "Rate Limiting Strategies",
            "content": """Rate limiting can be implemented at multiple layers: API gateway, application logic, or database.
    Use token buckets or sliding windows. This prevents abuse but is separate from token validity.""",
        },
    ]

    # Step 2: Embed all documents
    print("STEP 1: Building knowledge base embeddings...")
    doc_texts = [doc["content"] for doc in knowledge_base]
    doc_embeddings = call_ollama_embed(doc_texts)
    print(f"  Embedded {len(doc_texts)} documents")

    # Step 3: Embed the query
    query = "login authentication token refresh failure after key rotation"
    print(f"STEP 2: Embedding query: '{query}'")
    query_embedding = call_ollama_embed([query])[0]

    # Step 4: Calculate similarities and rank
    print("STEP 3: Ranking documents by relevance...")
    similarities = []
    for i, doc in enumerate(knowledge_base):
        sim = cosine_similarity(query_embedding, doc_embeddings[i])
        similarities.append((sim, doc, i))

    similarities.sort(reverse=True, key=lambda x: x[0])

    print("\n  Document Relevance Scores:")
    for sim, doc, idx in similarities:
        status = f"{GREEN}SELECTED{RESET}" if sim >= similarities[2][0] else f"{RED}FILTERED{RESET}"
        print(f"    [{idx}] {doc['title']}: {sim:.4f} - {status}")

    retrieved_docs = [doc for sim, doc, _ in similarities[:2]]
    print(f"\n  Retrieved top 2 relevant documents for context")

    # Step 5: Build enhanced prompt
    system_prompt = """You are a senior backend engineer specializing in Python/Flask authentication.
Diagnose production issues precisely. Reference specific code patterns and configuration values.
CRITICAL: Only reference information from the provided context and documents.
If you're unsure about something, explicitly say so. Be concise and actionable."""

    context_docs = "\n\n---\n\n".join(
        [f"[{doc['title']}]\n{doc['content']}" for doc in retrieved_docs]
    )

    context = f"""
<system_prompt>You are a senior backend engineer specializing in Python/Flask authentication.
Diagnose production issues precisely. Reference specific code patterns and configuration values.
CRITICAL: Only reference information from the provided context and documents.
If you're unsure about something, explicitly say so. Be concise and actionable.</system_prompt>

<error_log>
2026-04-09 03:14:22 ERROR auth.token_manager: TokenRefreshError
Traceback: token_manager.py line 142, in refresh()
  jwt.decode(token, key, algorithms=["HS256"])
jwt.ExpiredSignatureError: Signature has expired
Affected users: 342 in last hour (cluster: us-east-1)
Pattern: tokens issued before 02:00 UTC failing after rotation
</error_log>

<retrieved_knowledge>
{context_docs}
</retrieved_knowledge>

<memory>
Previous incident: March 2026, similar key rotation issue resolved by implementing dual-key validation window.
Pattern: All failures affect only tokens issued before the rotation event.
</memory>

<constraints>
- Only reference information from the provided context
- Suggest specific code changes, not generic advice
- If unsure, say so rather than guessing
</constraints>
"""

    prompt = "Fix the login bug"

    # SHOW the audience the assembled context
    print(f"\n{GREEN}ASSEMBLED CONTEXT (6 pillars active):{RESET}")
    pillar_labels = [
        ("PILLAR 1 - Instructions", "Senior backend engineer, Python/Flask auth"),
        ("PILLAR 2 - Retrieval",    f"2 docs selected from {len(knowledge_base)} via embedding similarity"),
        ("PILLAR 3 - Memory",       "Prior incident: March 2026, dual-key validation"),
        ("PILLAR 4 - Formatting",   "XML tags: error_log, retrieved_knowledge, memory"),
        ("PILLAR 5 - Constraints",  "Only reference provided context; say unsure if unsure"),
        ("PILLAR 6 - Decomposition","Retrieve → Rank → Assemble → Generate"),
    ]
    pillar_lines = [f"{GREEN}{label}{RESET}  {detail}" for label, detail in pillar_labels]
    print_box(pillar_lines)
    print(f"\n  {GREEN}QUESTION:{RESET} \"{prompt}\" (same as Rounds 1 & 2)\n")

    print("STEP 4: Generating diagnosis with retrieved context and embedding ranking...")
    response, tokens, elapsed = call_ollama_generate(prompt, system_prompt, context)

    metrics["round3"]["time"] = elapsed
    metrics["round3"]["tokens"] = tokens

    print(f"\n{GREEN}Response:{RESET}")
    print("-" * 80)
    print(response)
    print("-" * 80)
    print(f"\nMetrics:")
    print(f"  Response time: {elapsed:.2f}s")
    print(f"  Tokens generated: {tokens}")
    print(f"  Context strategy: {GREEN}Embedding-based retrieval + ranking{RESET}")
    print(f"  Quality: {GREEN}Highly specific, grounded in retrieved knowledge{RESET}")

    print(f"\n{GREEN}Full win: Smart retrieval + structured context = production-ready diagnosis{RESET}")

    wait_for_key()


def print_comparison_table():
    """Print side-by-side comparison of all 3 rounds."""
    print(f"\n\n{BOLD}{CYAN}")
    print("=" * 120)
    print("COMPARISON: Same Model, Same Question, Different Context")
    print("=" * 120)
    print(f"{RESET}\n")

    headers = [
        "Round",
        "Approach",
        "Response Time",
        "Tokens",
        "Context Strategy",
        "Quality",
    ]

    rows = [
        [
            f"{RED}1 (Naive){RESET}",
            "Vague prompt\nNo context",
            f"{metrics['round1']['time']:.2f}s",
            str(metrics["round1"]["tokens"]),
            "None",
            f"{RED}Generic{RESET}",
        ],
        [
            f"{YELLOW}2 (Structured){RESET}",
            "Structured XML\nSystem prompt",
            f"{metrics['round2']['time']:.2f}s",
            str(metrics["round2"]["tokens"]),
            "Manual context",
            f"{YELLOW}Specific{RESET}",
        ],
        [
            f"{GREEN}3 (Engine){RESET}",
            "Smart retrieval\nRanking + context",
            f"{metrics['round3']['time']:.2f}s",
            str(metrics["round3"]["tokens"]),
            "Embedding-based\nretrieval",
            f"{GREEN}Production-ready{RESET}",
        ],
    ]

    # Print ASCII table — use _display_width so ANSI codes don't break alignment
    col_widths = [16, 20, 15, 8, 20, 18]

    def _pad(text: str, width: int) -> str:
        """Left-align *text* in *width* terminal columns, ANSI-aware."""
        vis = _display_width(text)
        return text + " " * max(0, width - vis)

    # Resolve multiline cells: split each row into sub-lines
    def _resolve_rows(row):
        """Split cells containing \\n into multiple display lines."""
        split_cells = [cell.split("\n") for cell in row]
        max_lines = max(len(c) for c in split_cells)
        sub_rows = []
        for line_idx in range(max_lines):
            sub = []
            for col_idx, cell_lines in enumerate(split_cells):
                sub.append(cell_lines[line_idx] if line_idx < len(cell_lines) else "")
            sub_rows.append(sub)
        return sub_rows

    # Header
    header_str = " | ".join(_pad(h, col_widths[i]) for i, h in enumerate(headers))
    print(header_str)
    print("-" * _display_width(header_str))

    for row in rows:
        for sub_row in _resolve_rows(row):
            line = " | ".join(_pad(sub_row[i], col_widths[i]) for i in range(len(sub_row)))
            print(line)

    print("=" * _display_width(header_str))
    print(f"\n{BOLD}{GREEN}KEY INSIGHT:{RESET}")
    print(f"  Identical model. Identical question.")
    print(f"  The {BOLD}model wasn't the limiting factor{RESET} — the {BOLD}context was{RESET}.")
    print(f"\n  Round 1: Model was guessing in the dark.")
    print(f"  Round 2: Model had enough info to diagnose the issue.")
    print(f"  Round 3: Model had *relevant* info through retrieval + ranking.")
    print(f"\n{BOLD}Lesson: Most AI failures are context problems, not model problems.{RESET}\n")


def main():
    """Main execution."""
    try:
        print_header()

        print("\nStarting live API demonstrations...")
        print("(Real HTTP calls to http://localhost:11434)\n")

        round_1_naive_prompt()
        round_2_structured_context()
        round_3_full_context_engine()

        print_comparison_table()


    except ConnectionError as e:
        print(f"{RED}Error: {e}{RESET}")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n{RED}Demo interrupted by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{RED}Unexpected error: {e}{RESET}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
