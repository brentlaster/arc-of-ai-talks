# Appendix: Timing & Humor Notes

---


## Timing Checkpoints
| Slide | Elapsed Time | Section | Notes |
|-------|-------------|---------|-------|
| 3 | ~3 min | End of opening hook | |
| 5 | ~6 min | End of intro/numbers | |
| 6 | ~10 min | End of CAI definition + AIOps distinction | |
| 7 | ~11 min | Three Levels visual (expansion) | |
| 9 | ~14 min | End of integration points + scenario intro | |
| 10 | ~15 min | Section divider: patterns | |
| 12 | ~20 min | AI Test Synthesis code | COMPRESSIBLE — highlight 2 lines only |
| 13 | ~23 min | End of Pattern 1 (Test Synthesis) | COMPRESSIBLE — 30 sec max |
| 15 | ~31 min | End of Pattern 2 + audience moment | |
| 18 | ~36 min | Log Summarization Before/After (expansion) | |
| 19 | ~38 min | End of Pattern 3 (Log Summarization) — MIDPOINT | |
| 22 | ~44 min | End of Pattern 4 (RAG Debugging) | COMPRESSIBLE — RAG code slide |
| 24 | ~48 min | Five Risk Scoring Factors (expansion) | |
| 25 | ~50 min | End of Pattern 5 (Risk Scoring) | COMPRESSIBLE — risk routing code |
| 28 | ~56 min | End of Pattern 6 (Release Gates) | COMPRESSIBLE — gate config YAML |
| 30 | ~59 min | Six CAI Failure Modes (expansion) | |
| 32 | ~62 min | Autonomy Ladder visual (expansion) | |
| 35 | ~66 min | End of end-to-end scenario + synthesis | |
| 36 | ~67 min | Sarah's PR visual (expansion) | |
| 41 | ~70 min | Six-Component CAI Stack (expansion) | |
| 44 | ~72 min | Real Tools for Real Pipelines | COMPRESSIBLE — 30 sec max |
| 49 | ~74 min | Six CAI Metrics visual (expansion) | |
| 50 | ~75 min | Five-Step Evaluation Methodology | |
| 51 | ~76 min | Adoption Path closing | |

## Word Count Estimate
~10,800 spoken words | At 140 wpm = ~77 min speaking — leaves ~3 min for audience interaction and questions
(Net ~+900 words from v10: expansion slide scripts for 9 new cue/visual slides added by talk expander)

---

# Appendix: Humor, Irony & Anecdote Opportunities

Use these as drop-in additions or improvisational springboards at the indicated slide moments. Developers love dry humor about pipeline pain — lean into shared frustrations.

---

### SLIDE 3 — "Your Pipeline Is Still Dumb"
**After "it learned absolutely nothing":**
> "Your pipeline processed ten thousand builds last year. It learned nothing from any of them. It's like a student who takes the same exam ten thousand times and never studies. At some point you have to ask: is the student the problem, or is the system?"

*[NOTE: This humor beat is now integrated into the main script at slide 3.]*

---

### SLIDE 4 — From CI/CD to CAI
**After describing "automated but unintelligent":**
> "Today's CI/CD pipeline is basically a very expensive, very fast, very reliable... conveyor belt. It moves things from point A to point B with zero thought about what's on it. A one-line README fix gets the same 45-minute test suite as a rewrite of the auth system. That's not intelligent. That's just... organized."

*[NOTE: This humor beat is integrated into the main script at slide 4, now trimmed.]*

---

### SLIDE 10 — AI Test Synthesis: Coverage Gaps
**After "coverage gaps are everywhere":**
> "Be honest — how many of you have a codebase where test coverage is described as 'aspirational'? *[Pause for laughs.]* Yeah. We write tests for the happy path, maybe throw in a null check, and call it 'comprehensive.' AI test synthesis is for the 80% of edge cases that we all know exist and collectively pretend don't."

*[NOTE: This humor beat is now integrated into the main script at slide 10.]*

---

### SLIDE 13 — Failure Classification: Manual Triage
**After describing the manual log-reading process:**
> "The current workflow: build fails. Developer opens a 10,000-line log. Scrolls for fifteen minutes. Discovers it was a stale Docker cache. Sighs deeply. Restarts the pipeline. Loses an hour of their life they'll never get back. We've all lived this. Some of us lived it this morning. Some of us are living it right now on their phone under the table."

*[NOTE: This humor beat is integrated into the main script at slide 13.]*

---

### SLIDE 14 — Before/After Triage
**After "Time: 2-3 minutes" on the AI side:**
> "From 45 minutes to 3 minutes. I've had developers tell me this single change made them believe in AI again. One guy said, 'I went from dreading red builds to almost looking forward to them because the AI summary is actually interesting.' I mean, he's a little weird. But the point stands."

*[NOTE: This humor beat is trimmed from the main script at slide 14.]*

---

### SLIDE 16 — Log Summarization: The #1 Recommendation
**After explaining why this is the best starting point:**
> "This is the 'gateway drug' of CAI. Twenty minutes of setup, and your Slack channel goes from '🔴 Build #4521 failed' to '🔴 Build #4521 failed: ran out of memory compiling 847 TypeScript files. Increase runner to 8GB.' That's the difference between a notification and actual information. One makes you groan. The other makes you say 'oh, I know exactly what to do.'"

*[NOTE: This humor beat is now integrated into the main script at slide 16.]*

---

### SLIDE 18 — RAG Debugging: Institutional Memory
**After "the knowledge walked out the door":**
> "Have we seen this error before? Usually yes. Someone fixed it six months ago, in PR #4521. The fix is in the commit message. And that someone? They updated their LinkedIn in January and now they're 'open to opportunities.' RAG debugging is how you stop your institutional knowledge from having an exit interview."

*[NOTE: This humor beat is now integrated into the main script at slide 18.]*

---

### SLIDE 21 — Risk Scoring: Not All Changes Are Equal
**After "why give every PR the same pipeline?":**
> "Right now, your pipeline treats a one-line typo fix in the README the same as a 500-line refactor of the payment processing system. Both get the full 45-minute test suite. The README change isn't offended by the lack of scrutiny. But your developers waiting 45 minutes for a typo fix? They're offended."

*[NOTE: This humor beat is integrated into the main script at slide 21.]*

---

### SLIDE 23 — Release Gates: "Ship or Hold?"
**After introducing AI release gates:**
> "'Ship or hold?' is currently decided by a developer looking at a green checkmark and their gut feeling on a Friday afternoon at 4:30. We can do better than gut feelings at 4:30 on a Friday. In fact, 'gut feelings at 4:30 on a Friday' is basically the origin story of every production incident I've ever investigated."

*[NOTE: This humor beat is integrated into the main script at slide 23.]*

---

### SLIDE 33 — The Feedback Loop
**After explaining how the system captures signal from every failure:**
> "This is what separates CAI from 'we added a ChatGPT call to our pipeline and called it innovation.' A ChatGPT call is a party trick. A learning system is an engineering practice. Know the difference."

*[NOTE: This humor beat is now integrated into the main script at slide 33.]*

---

### SLIDE 39 — Don't Boil the Ocean
**After "let the value do the selling":**
> "Don't go to your VP and say 'I need six months and a team of five to implement an AI-powered autonomous deployment system.' Go to your VP and say 'I added a thing to Slack that tells us why builds fail in plain English. It took me a day.' Then watch them come back asking for more. That's how you fund a CAI program — one undeniable win at a time."

*[NOTE: This humor beat is now integrated into the main script at slide 17.]*
