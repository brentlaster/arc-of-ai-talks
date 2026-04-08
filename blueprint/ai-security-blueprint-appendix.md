# Appendix: Timing, Word Count & Humor Notes

---

## Timing Checkpoints
| Slide | Elapsed Time | Section |
|-------|-------------|---------|
| 1 | ~2 min | Title + setup |
| 2 | ~7 min | Opening incidents + audience poll |
| 3 | ~10 min | 97% stat |
| 5 | ~13 min | End of current state stats (compressed) |
| 8 | ~19 min | Blueprint overview + Before/After + E2E + Policy Engine |
| 13 | ~23 min | End of Layer 1 (Identity) — compressed |
| 16 | ~30 min | End of Layer 2 (Context Isolation + RAG chain) |
| 20 | ~39 min | End of Layer 3 (Prompt Injection + walkthrough + decision) + mid-talk recap — MIDPOINT |
| 25 | ~47 min | End of Layer 4 (Model Governance + vendor risk) |
| 28 | ~52 min | End of Layer 5 (Audit + threat-model exercise) — compressed |
| 36 | ~61 min | End of Layer 6 + cross-cutting (RACI compressed) + failure chain |
| 41 | ~65 min | End of Scenarios |
| 44 | ~67 min | MVP Checklist + Quick Wins (compressed) |
| 47 | ~70 min | 5 Questions + Anti-Patterns (compressed) + Closing + challenge question |
| 49 | ~71 min | Q&A + End |

## Word Count Estimate
~10,500 spoken words | At 140 wpm = ~75 min (tight fit for 75-min slot; compress back third if running long)

---

# Appendix: Humor, Irony & Anecdote Opportunities

These are preserved from the original script with placement updated for the new slide order. Use as drop-in additions or improvisational springboards.

---

### SLIDE 3 — 97% Had No Controls
**After the 97% stat:**
> "97% had no proper AI access controls. Which means if you're in a room of 100 companies that got breached, 97 of them basically left the front door open with a sign that said 'AI systems — come on in.' And somehow we're still surprised when things go wrong."

---

### SLIDE 4 — Agent Containment Stats
**After "60% cannot terminate a misbehaving agent":**
> "60% have no kill switch. Let me rephrase that: they deployed an autonomous system that can access their data, call their APIs, and interact with their customers — and there's no off button. That's not cutting-edge technology. That's the opening scene of a movie where things go very wrong very fast."

---

### SLIDE 12 — Layer 1: Identity & Access Control
**After explaining AI agents need their own identity:**
> "Most organizations give their AI agents the same credentials as the developer who deployed them. That's like giving the intern the CEO's badge because it was easier than getting them their own. It works — right up until it really, really doesn't."

---

### SLIDE 16 — Layer 3: Prompt Injection
**After explaining direct vs. indirect injection:**
> "Prompt injection is the new SQL injection — except this time, the attack vector is natural language, and the defense is... also natural language. We're defending computers with English. If that doesn't keep you up at night, you haven't thought about it enough."

---

### SLIDE 20 — Layer 4: Model Governance / Shadow AI
**After mentioning shadow AI:**
> "A developer finds a model on Hugging Face that works great in a notebook, deploys it behind an API on a Friday afternoon, and nobody knows it exists until a customer complaint surfaces three weeks later. We spent twenty years fighting shadow IT. Now we have shadow AI. Same problem, higher stakes, worse vibes."

---

### SLIDE 24 — Layer 5: Audit Trails — 33% Have None
**After "33% have no audit trails whatsoever":**
> "33% have no audit trails. Zero record of what the AI did. That's like running a bank where nobody writes down the transactions. 'How much money is in the vault?' 'We... don't actually know. But the AI seems confident about it.'"

---

### SLIDE 29 — Canary Deployments
**After explaining canary phases:**
> "5% of traffic, then 10%, then 25%, then full. That's how you deploy AI safely. What most organizations do instead is 0% on Tuesday, 100% on Wednesday, and 'oh no' on Thursday."

---

### SLIDE 49 — Closing
**Before the final call to action:**
> "The fastest way to kill AI adoption is a breach. One data leak, one hallucination in a customer interaction, one compliance violation — and the whole program gets shut down. Security doesn't slow innovation. It's what keeps innovation alive."
