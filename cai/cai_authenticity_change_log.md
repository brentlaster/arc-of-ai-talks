# Script Authenticity Fixes — CI/CD in the Age of CAI

## Summary
- **Total claims flagged:** 6 (plus 3 Q&A echoes)
- **Replacements by strategy:**
  - Research citations: 2
  - Reframed as general knowledge: 3
  - Published case study: 1
- **Deck changes needed:** None (all fabricated claims were in spoken script only, not on slides)

## Changes by Slide

### SLIDE 4 — Your Pipeline Is Still Dumb

**Original:**
> Quick story: a team I work with had a PR merged late on a Tuesday. CI failed with a misleading timeout error. Two developers spent 40 minutes combing through logs before discovering the root cause was a stale Docker cache — something that had happened before and been fixed before, but nobody remembered. Forty minutes of engineering time, wasted on something a system with memory would have solved in seconds. That's exactly the gap we're talking about.

**Issue:** Claims personal experience working with a specific team. Fabricated anecdote with specific details (Tuesday, 40 minutes, stale Docker cache).

**Strategy:** Reframe as common industry scenario + research citation

**Replacement:**
> Here's a scenario that plays out constantly across the industry. A PR gets merged late on a Tuesday. CI fails with a misleading timeout error. Two developers spend 40 minutes combing through logs before discovering the root cause is a stale Docker cache — something that had happened before and been fixed before, but nobody remembered. A case study published by techbuddies.io found that cache-related failures accounted for up to 15% of all CI failures before teams implemented proper caching strategies. Forty minutes of engineering time, wasted on something a system with memory would have solved in seconds. That's exactly the gap we're talking about.

**Source:** https://www.techbuddies.io/2025/12/17/case-study-how-we-optimized-ci-cd-pipelines-in-github-actions-and-gitlab-ci/

---

### SLIDE 38 — The Smallest Useful CAI Stack

**Original:**
> I've seen teams send raw build logs — complete with API keys — straight to an external LLM. Don't be that team.

**Issue:** Claims firsthand observation of teams making this security mistake.

**Strategy:** Research citation — real security incidents

**Replacement:**
> This isn't hypothetical — in March 2025, the tj-actions/changed-files GitHub Action was compromised, exposing CI secrets including AWS keys and GitHub tokens across 23,000 repositories. GitHub reported detecting over 39 million leaked secrets on their platform in 2024 alone. Don't let your AI pipeline become another vector.

**Sources:**
- https://thehackernews.com/2025/03/github-action-compromise-puts-cicd.html (CVE-2025-30066)
- https://medium.com/@instatunnel/github-secret-leaks-the-13-million-api-credentials-sitting-in-public-repos (GitHub 39M leaked secrets stat)

---

### SLIDE 41 — Where CAI Pays for Itself (line 554)

**Original:**
> Now — and this is a question I get every time — what does all this cost?

**Issue:** Implies regular audience interaction history the speaker doesn't have.

**Strategy:** Reframe as general knowledge

**Replacement:**
> Now — and this is the natural next question — what does all this cost?

**Source:** N/A — simple reframe

---

### SLIDE 41 — Where CAI Pays for Itself (line 568)

**Original:**
> Most teams find that 80% of their CAI value comes from the cheapest 20% of their AI spend.

**Issue:** Implied practitioner knowledge from working with multiple teams, with no source.

**Strategy:** Reframe as general principle (Pareto)

**Replacement:**
> Think of it as the Pareto principle applied to AI spend — the bulk of your pipeline intelligence comes from the cheapest, highest-volume tasks, not from the expensive frontier model calls.

**Source:** N/A — reframed as well-known principle

---

### SLIDE 45 — Six CAI Metrics & Targets (line 626)

**Original:**
> To make this concrete: one team tracked triage time before and after adding classification. Before: median 28 minutes. After 60 days: median 4 minutes. Gate override rate started at 31% and dropped to 8% after two months of threshold tuning.

**Issue:** Fabricated specific team statistics (28→4 min, 31%→8%) with no citation. Most dangerous claim — specific numbers imply real data.

**Strategy:** Published case study (Metaview)

**Replacement:**
> To make this concrete: Metaview published a case study on their engineering blog showing they cut triage time by 80% using AI-powered observability. Their traditional incident triage took 30 to 45 minutes per incident — almost all of that time spent gathering data, not thinking. After automating the data-gathering step with AI, that time dropped dramatically. And that's the pattern you'll see: classification and triage are where the immediate, measurable wins show up first.

**Source:** https://www.metaview.ai/resources/blog/how-we-cut-engineering-triage-time-by-80-with-ai-powered-observability

---

### Q&A — "This sounds like a lot of complexity" (line 803)

**Original:**
> The team that failed in the talk tried all six patterns across three pipelines simultaneously and got nothing. The team that succeeded started with one pattern on one pipeline.

**Issue:** References fabricated teams as if they were real examples from the talk.

**Strategy:** Reframe as general principle

**Replacement:**
> The anti-pattern is trying all six patterns across three pipelines simultaneously — that's a recipe for getting nothing done. The approach that works is starting with one pattern on one pipeline, proving value, then expanding.

**Source:** N/A — reframed as principle

---

## Q&A Echo Fixes

Three Q&A answers repeated claims from the main script and were updated to match:

1. **"How do we handle sending build logs to external LLMs?"** — Replaced "I've seen teams..." quote with the tj-actions incident citation and GitHub 39M secrets stat.

2. **"What about the cost of API calls in CI?"** — Replaced "Most teams find 80% of CAI value comes from the cheapest 20% of AI spend" with Pareto principle framing.

3. **"How do we get buy-in from leadership?"** — Replaced "median triage time went from 28 minutes to 4 minutes" with "Metaview published an 80% reduction in triage time using AI-powered observability."
