# Context Engineering: Because the Model Isn't the Problem — v11 Improved Speaker Script

**Duration:** ~65 minutes (raw spoken ~50 min + ~10 min pauses, polls, transitions + ~5 min buffer)
**Target pace:** ~140 words/min | **Spoken word count:** ~7,000 words
**v12 Changes:** Removed Slide 24 (Context Rot) entirely. Condensed Slides 35-36, 43-45, and 46. Applied light trims to Slides 17, 20, 28, 31, 37. Renumbered slides 25+ to fill gap. Cut ~1,000 words total to meet 50-minute spoken content target.

---

## SLIDE 1: VERSION
[Skip]

---

## SLIDE 2: TITLE
*[Skip — advance immediately]*

*[Wait for audience to settle]*

Good morning, everyone. Thanks for being here at Arc of AI. I'm Brent Laster, and today we're going to talk about something that I think is one of the most underappreciated skills in AI right now.

Here's the premise of this talk in one sentence: **Most of the time, the model isn't the problem. The context is.** And for the next hour, I'm going to show you exactly what that means, why it matters, and — most importantly — how to fix it.

I should say upfront — this isn't an abstract, theoretical talk. This is about practical, repeatable techniques that you can start using this week. And by the end, I think you'll look at every AI system you work with in a fundamentally different way.

---

## SLIDE 3: ABOUT ME

[Brief personal introduction - use content on slide]

---

## SLIDE 4: "This Isn't Funny" - Viral Post Hook
*[GESTURE at the screenshot]*

Before we dive in, I want to show you something. This post went viral in the AI community recently. *[PAUSE for effect]* Take a look at what it says. Someone claiming Claude Code replicated a year of their team's work in about an hour.

Your gut reaction is probably — wow, these models are getting incredible. That's the obvious read. And yeah, these tools are powerful. But hold that thought. We're going to come back to this slide later in the talk, and I think you'll see it very differently.

*[PAUSE]*

Because the answer to "how did that happen?" is going to reveal everything I want you to understand about context engineering. Stick with me.

---

## SLIDE 5: "The AI Should Have Known What I Meant"
*[PAUSE — let the title land]*

So let me start with a scenario that I think every single person in this room has experienced. You're working with an AI — could be ChatGPT, Claude, Copilot, whatever your tool of choice is — and you type something like: "Fix the login bug."

The model comes back with something generic. "To fix a login bug, you'll typically want to check authentication logic, verify password hashing..." It's technically correct, but it's completely useless because the AI doesn't know *your* login bug. It doesn't know your authentication architecture, your error logs, your user base, your constraints. It's making an educated guess based on nothing.

So what do you do? You get frustrated. You think, "I need a better model." You look at GPT-4.1. You think about fine-tuning. You add more compute.

Quick show of hands — how many of you have blamed the model in the last month? *[pause]* Yeah, that's most of the room. You're in good company.

Here's what I'm going to tell you: that's probably backwards. The model isn't the problem. Your context is.

---

## SLIDE 6: What Is Context Engineering?

*[GESTURE at the definition block]*

So what do I mean by context engineering? There's a quote on this slide from the Anthropic engineering blog that I think captures it perfectly: building with language models is becoming less about finding the right words and more about answering — what configuration of context is most likely to generate the desired behavior?

Context engineering is the discipline of designing and managing the full information environment in which an AI system operates. That includes instructions, retrieved data, memory, tool descriptions, formatting, constraints, and workflow structure. Every single one of those layers affects the model's ability to produce the right answer. And most teams are tuning maybe two of them — usually the system prompt and the input data. Everything else is left as default or ignored.

That's the gap we're going to close today.

---

## SLIDE 7: From Prompts to Systems

*[GESTURE at the evolution diagram]*

Here's how to think about this shift. Prompt engineering — the thing most of us have been doing — is a subset of context engineering, not the other way around. A prompt is one piece. Context engineering is the whole system.

When you write a prompt, you're crafting one input. When you do context engineering, you're designing the entire information pipeline: what gets retrieved, how it's structured, what constraints are applied, what the model remembers from prior interactions, and how the workflow is decomposed. That's a systems problem, not a writing problem.

And that's the key mindset shift. We're moving from "how do I phrase this question?" to "how do I build the information environment that makes the right answer inevitable?"

Think about it this way. When a new engineer joins your team, you don't just give them a task and hope for the best. You give them context — documentation, codebase access, team norms, escalation paths, examples of good work. The better the onboarding context, the faster they produce good work. AI systems work exactly the same way. The quality of the output is bounded by the quality of the context you provide.

---

## SLIDE 8: The Enterprise AI Moment

*[GESTURE at the big "40%" number]*

And this shift matters right now more than ever. Look at this stat from Gartner: 40% of enterprise apps will feature task-specific AI agents by late 2026 — up from less than 5% in 2025. That's explosive growth.

But here's the catch — and this is the line I want you to remember from this slide: most enterprises are deploying agents before designing the environments those agents need to operate in. They're building the car without building the road.

Teams that invest in context engineering now will have a structural advantage as agent adoption scales. Because agents are even more sensitive to context quality than simple Q&A systems. An agent that has bad instructions, noisy retrieval, and no constraints isn't just unhelpful — it's actively dangerous. It makes confident mistakes at scale.

---

## SLIDE 9: The Cost of Bad Context

*[GESTURE across the four cards]*

And when context is bad, here's what happens. Four consequences that show up repeatedly in production systems across the industry.

Hallucinations — models fabricate answers when context is missing or contradictory. They're not lying; they're filling in gaps because that's what they're built to do.

Wasted compute — stuffing irrelevant tokens wastes money and latency. Every irrelevant document in your context window is compute you're paying for with zero return.

Unreliable outputs — inconsistent behavior from poorly structured inputs. The same question gets different answers depending on what noise happens to be in the context that day.

And eroded trust — users stop using AI systems that can't be depended on. This is the one that kills projects. Technical problems are fixable. Lost trust is much harder to recover.

Context problems masquerade as model problems. And that's the core insight: most of the time, upgrading the model isn't the fix. Fixing the context is.

---

## SLIDE 10: The Six Pillars of Context Engineering
*[PAUSE — let the section divider land]*

Alright, now we know *why* context matters. Let's talk about *what* to actually do about it. I've organized the practice of context engineering into six pillars — six dimensions you can tune independently.

---

## SLIDE 11: Six Pillars Overview

*[GESTURE at the pillar diagram]*

Here they are. Instructions — your system prompts and role definitions. Retrieval — RAG, context engines, how you find information. Memory — what persists across interactions and where. Formatting — structure, ordering, and examples. Constraints — guardrails, boundaries, and rules. And Decomposition — splitting workflows across focused steps or agents.

Each pillar is a lever. Pull one, and you get improvement. Pull them together, and the effects compound. And here's the key thing — every one of these pillars can be tuned and measured independently. This isn't aesthetic prompt writing; it's systems engineering. Let's walk through each one.

---

## SLIDE 12: Pillar 1: Instructions & System Prompts

Pillar one: instructions and system prompts. This is the most foundational thing you can do, because it sets the entire context for how the model will interpret everything that follows.

*[GESTURE at the slide content]*

The recipe is straightforward: Role plus Constraints plus Output Format plus Examples. That's what a good system prompt looks like. "Be helpful" is not a system prompt — it's a guess. You need to tell the model who it is, what domain it operates in, what it's allowed to do, what it's *not* allowed to do, and what a correct answer looks like.

Teams routinely spend weeks evaluating models when their system prompt is three lines of generic text. Swap in a specific, well-constrained prompt and suddenly the "worse" model outperforms the "better" one. It's the single highest-leverage change most teams can make.

And as the Anthropic blog puts it: be thoughtful and keep your context informative, yet tight. That's the design challenge.

---

## SLIDE 13: System Prompts: Before & After

*[GESTURE at the two-column comparison]*

Here's the difference in practice. On the left: "You are a helpful assistant. Please help the user with their questions." Three tokens of useful instruction. Zero constraints, no format, no role. The model has no idea what that means in your domain.

On the right: specific role — senior code reviewer. Specific focus — Python, Django, PostgreSQL. Explicit constraints — no framework migrations, follow PEP-8. Clear format — return diff blocks with severity ratings. And examples.

That's specific, actionable, constrained. The model knows who it is and what success looks like.

And here's the payoff — with the generic prompt, the model gives you boilerplate. "Check your authentication logic." With the specific one, it says: "Pod crash-loop in auth-service is caused by a misconfigured OIDC callback URL in deployment manifest line 47." Same model. Night and day.

---

## SLIDE 14: The System Prompt Win
*[GESTURE at the before/after card]*

This is the example I want you to take home. Imagine a code review agent producing useless, generic feedback — "consider adding error handling," "this could be more efficient." The agent has a three-line system prompt.

Rewrite it in 20 minutes: specific role, language stack, coding standards, review format. The first review after that change could catch an actual race condition in a database connection pool — because the agent finally knows what to look for.

*[PAUSE for emphasis]*

No model upgrade. No new data. Just a better system prompt. That's the kind of win I want you to walk away with today.

---

## SLIDE 15: Anti-Pattern: Tool Bloat

Now, one particular thing under instructions that breaks a lot of production systems: tool overload.

*[GESTURE at the quote]*

As the Anthropic engineering blog says: if a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better.

The fix: fewer tools with clear boundaries. Each tool should have a clear, distinct purpose. Curate diverse canonical examples, not a laundry list. And here's a good test: can you explain when to use each tool in one sentence? If you can't, neither can the agent.

The model can only reason from what it's given. Clarity beats volume every time. And clarity often means removing things, not adding them.

---

## SLIDE 16: Pillar 2: Retrieval — The Right Information

Pillar two: retrieval and data selection. This is where a lot of systems start to fail.

*[GESTURE at the slide]*

RAG is one of the most powerful tools for context engineering — but most implementations are naive. The chunking problem alone trips up the majority of teams. Too small, and you lose the surrounding context needed for meaningful answers. Too large, and you get noisy embeddings that are hard to pinpoint.

A good litmus test: if a chunk makes sense to a human on its own, it will make sense to the model.

Here's a common failure pattern. A documentation agent gives confidently wrong answers about an API. The root cause? Retrieval is pulling from deprecated docs that haven't been removed from the index. The model has no way to know the docs are stale — it treats them as ground truth. Add a recency filter and a "last-verified" metadata tag, and the accuracy problem can disappear overnight. Same model, same embeddings — just smarter retrieval.

---

## SLIDE 17: Three Retrieval Principles
*[GESTURE across the three cards]*

Three principles that fix most retrieval problems.

First — quality in equals quality out. If you're retrieving irrelevant documents, the model wastes tokens parsing noise.

Second — recency matters. Remember the deprecated docs example from a moment ago? That pattern is everywhere. Stale documents in the index are one of the most common retrieval failures. A recency filter and "last-verified" metadata tag are straightforward fixes that can eliminate an entire class of errors.

And third — measure impact. Every time you change your retrieval, track retrieval precision alongside output accuracy. If you're not measuring context quality, you're guessing.

---

## SLIDE 18: Naive RAG vs. Context Engine

*[GESTURE at the comparison diagram]*

This diagram shows the key evolution. On one side: naive RAG. Embed your query, find similar documents, dump them in. On the other: a context engine — where retrieval, verification, reasoning, and access control are all integrated.

Let me ground this with our login bug. A customer reports a login failure. Naive RAG retrieves password reset documentation, general auth best practices — noise. A context engine retrieves authentication error logs, recent session data, the specific OAuth configuration — exactly what the model needs to diagnose the issue.

Put simply: a context engine is not just retrieval — it's the system that selects, shapes, verifies, prioritizes, and routes information for the model.

---

## SLIDE 19: Inside a Context Engine (NEW)

*[GESTURE at the 5-stage pipeline diagram]*

So what does a context engine actually look like under the hood? Let me walk you through it — five stages, left to right.

Stage one: **Query Analysis**. Before you retrieve anything, you analyze and expand the query. "Fix the login bug" becomes a classified intent — authentication issue, production severity — with expanded search terms. This is Pillar 6, Decomposition, in action.

Stage two: **Multi-Source Retrieval**. Now you're pulling from multiple sources in parallel — embedding similarity against your knowledge base, but also knowledge graphs, live APIs, memory stores. Not just "find similar documents." This is Pillar 2.

Stage three: **Rerank and Verify**. This is where most naive RAG falls down. You score the retrieved results for actual relevance to the expanded query, check whether they're current, and filter out noise. A document about connection pooling might be semantically similar to an auth token error, but it's irrelevant. This stage catches that. Pillar 5 — Constraints.

Stage four: **Compress**. You've got verified, relevant context now, but maybe too much of it. Summarize, deduplicate, trim to your token budget. Pillar 3 — Memory management.

And stage five: it all flows into **Structured Context** that gets sent to the LLM — your system prompt, XML-tagged context, constraints, formatted output spec. Pillars 1 and 4.

Look at that bottom bar — every stage maps back to one or more of the six pillars we just introduced. The context engine is what happens when you orchestrate all six pillars into a single automated pipeline. That's the key insight: it's not one clever trick. It's systematic engineering.

---

## SLIDE 20: The Retrieval Evolution (Practitioner Mental Model)

*[GESTURE at the timeline]*

And here's the trajectory. This is a practitioner's mental model, not an industry standard taxonomy, but I find it useful.

Classic RAG in 2024: retrieve docs by semantic similarity. You embed your query, find the closest documents, and dump them in. In 2025: vector orchestration — now you're coordinating text, knowledge graphs, and API calls, not just similarity search. And in 2026: context engines — retrieval plus verification, reasoning, and access control in one pipeline.

In operational terms: the difference is between "here are the five most similar documents" and "here are the three documents that are verified current, relevant to this specific question type, and authorized for this user." That's a fundamentally different retrieval contract.

If your retrieval system is still doing basic similarity search while the state of the art has moved to verified, reasoned selection — you're leaving the biggest lever on the table.

---

## SLIDE 21: Pillar 3: Memory

Pillar three — memory. And here's a fundamental problem with how language models handle long contexts.

*[GESTURE at the diagram]*

This is the "lost in the middle" problem, discovered by researchers at Stanford, UC Berkeley, and Samaya AI. They ran a series of careful experiments asking: if you place critical information at different positions in a long context window, how does model performance change?

The answer is dramatic. Information at the beginning of the context — models use it well. High performance. Information at the end — also good. But put critical information in the *middle* of a long context, and performance drops significantly.

Why does this happen? It's an architectural consequence. Transformer models have certain structural properties in their attention mechanism. Tokens at the beginning of the context get attended to by every subsequent token — they accumulate enormous attention weight. Tokens at the end benefit from recency. But information in the middle? In practice, it's often used less effectively. The exact mechanism varies by architecture, but the operational takeaway is consistent across models.

---

## SLIDE 22: Position Your Context Wisely
*[GESTURE at the position diagram]*

So what do you do with the lost-in-the-middle finding? Three practical actions.

Information at the beginning gets high attention weight from all subsequent tokens. Information at the end benefits from recency. But the middle? Performance drops significantly there.

The action items: front-load your most important information. Back-load your constraints and output format. And compress the middle aggressively — but measure quality as you go, because not every context compresses well.

Some teams report meaningful token savings while preserving the information that actually matters, though results vary significantly by task and implementation.

---

## SLIDE 23: Context Layers Architecture

Here's how to think about memory architecturally. I find this four-layer model really useful.

At the top: working context. That's the immediate prompt — system instructions, agent identity, selected conversation history, tool outputs, retrieved documents. This is what the model sees right now, in this moment.

Next: the session layer. The durable log of the current interaction. Everything that's happened in this conversation, even if it's not all in the working context right now.

Then: memory. Long-lived, searchable knowledge that outlives any single session. The model's accumulated understanding. Think of this as its institutional memory — what it learned in previous conversations that's still relevant.

And finally: artifacts. Large binary or textual data — documents, images, code repositories. These are referenced but not necessarily sitting in the context window. They're available when needed.

Let me make this concrete with our support bot. Working context: the current customer question plus the system prompt and retrieved docs. Session: the full conversation history so this customer doesn't have to repeat themselves. Memory: knowledge from thousands of prior support conversations — "customers who ask about X usually mean Y." Artifacts: the full product documentation library, queried on demand. Each layer has a different lifetime and a different retrieval strategy. The art is in knowing what goes where.

---

## SLIDE 24: Pillar 4: Formatting & Structure

Pillar four — and this one genuinely surprises people when I show them the data.

*[GESTURE at the comparison]*

Here's a design principle that holds across production systems generally: relevant, focused tokens often outperform much larger unfocused ones. When you structure information well — using XML tags, JSON structure, or markdown headers — versus dumping raw text, the difference in model performance can be dramatic.

Why? Because formatting isn't cosmetic — it's *functional*. When you use semantic boundaries like tags and headers, the model actually uses them to parse and prioritize information. Think of them like section headers in a textbook. Without them, the model has to infer what each piece of information is and how it relates to everything else. With them, the structure is explicit.

And positioning matters too. Remember the lost-in-the-middle problem? That's not just a memory issue — it applies to everything in your context. Front-load your most important information. Back-load your constraints and output format. Don't bury the critical stuff in the middle of a wall of text.

---

## SLIDE 25: Structure Changes Everything

Here's a concrete example that makes the point viscerally.

*[GESTURE left]*

On the left: unstructured. A wall of text describing a bug report — the user, the timeline, the error rate, a hypothesis from QA — all jumbled together in a natural language paragraph. The model has to parse intent, separate facts from speculation, identify the actual request, and figure out what to prioritize. It's doing natural language processing just to understand the *prompt*.

*[GESTURE right]*

On the right: the exact same information, but structured with clear XML tags. Symptom. Timeline. Hypothesis. Each piece of information clearly delineated and labeled. The model knows instantly what each piece is and how to use it.

And here's where the login bug comes back into the picture. Back to our login bug scenario — same information about authentication failures, user state, and code context, but now structured with clear sections. The model can instantly navigate the critical details: where the error occurred, when, what the user state was, and what the code shows. No parsing needed. No confusion.

This takes maybe 30 seconds longer to format. The difference in output quality is dramatic. According to a 2025 FlowHunt analysis of prompt engineering techniques, structured inputs with clear semantic boundaries consistently outperform unstructured equivalents — with teams reporting error rate reductions on the order of 30-40% just by structuring the input context. Not changing the model. Not adding data. Just organizing what was already there. Your mileage will vary, but the direction is consistent.

---

## SLIDE 26: Pillar 5: Constraints & Guardrails

Pillar five — constraints. And I want to be really direct about this: telling the model what *not* to do is every bit as important as telling it what to do.

*[GESTURE across the four cards]*

There are four types of constraints you should be thinking about. Output format constraints — JSON schemas, response length limits, required fields, structural requirements. Behavioral constraints — no speculation without evidence, cite your sources, escalate when uncertain rather than guessing. Domain constraints — stay within approved topics, reject out-of-scope requests gracefully. And safety constraints — PII handling rules, content policies, compliance requirements.

Most teams spend 90% of their prompt engineering energy on instructions — what the model *should* do — and about 10% on constraints. I'd argue it should be closer to 60/40. Constraints are what separate a demo from a production system. Consider this scenario: a support chatbot confidently recommends a medication dosage change — something that should always be escalated to a physician. One behavioral constraint — "never provide specific medical dosing; always escalate to a healthcare professional" — prevents it entirely. That's the difference constraints make.

---

## SLIDE 27: Context Smells: Red Flags to Watch For

Before the last pillar, here are six bad patterns — "context smells" that signal your context engineering needs fixing.

Quick show of hands — which of these is your biggest problem right now: prompt sprawl, retrieval noise, or memory overload? *[pause]* Yeah, I see a lot of hands for that one. You're not alone.

*[GESTURE across the six cards as you go through them]*

First: **Prompt sprawl** — Accumulated instructions nobody owns or reviews. Everything in one massive request — instructions, data, history, tool descriptions, rules. The model is drowning.

Second: **Weak role definition** — Generic identity with no domain specifics. "Be helpful" — that's not context engineering, that's a guess.

Third: **Retrieval noise** — Irrelevant docs dumped regardless of the question. Remember our login bug? Pulling in password reset docs instead of authentication error logs.

Fourth: **Bad chunking** — Fixed chunks that break semantic boundaries. 512-token chunks regardless of document structure.

Fifth: **Unstructured context** — Raw data straight to the model with no structure. No headers, no tags, no logical boundaries.

And sixth: **Premature model upgrades** — Scaling up without measuring the real bottleneck. You jump to a bigger model without checking whether context was the actual problem.

*[PAUSE for emphasis]*

How many of you recognized at least three of these? Yeah, I see some uncomfortable laughter. You're in good company. These six patterns are endemic in early-stage AI deployments — most teams have dealt with at least three of them. The good news is once you know what they look like, they're fixable.

---

## SLIDE 28: Diagnose Your System
*[GESTURE at the five-step ladder]*

Here's the diagnostic ladder I promised. Think about a system you work with right now. Run it through these five steps.

Step one — is the instruction specific enough? Step two — is retrieval pulling relevant information? Step three — is the context structured? Step four — are constraints explicit? Step five — should this task be decomposed?

And only if all five are solid — *then* ask whether the model itself is the bottleneck. That's your triage sequence. Start at the top and work down.

*[PAUSE]*

Most teams jump straight to "we need a better model" without checking any of these five. That's where the money gets wasted.

---

## SLIDE 29: Pillar 6: Workflow Decomposition

And finally, pillar six — decomposition. This is the architectural pillar, and for complex tasks, it's often the most impactful.

*[GESTURE at diagram]*

The key idea here is on this slide: instead of cramming everything into one massive prompt — what I call the "kitchen sink" approach — you break the work into focused steps. Each step gets exactly the context it needs for that specific task. Nothing more, nothing less. The best production AI systems aren't one giant prompt. They're pipelines of focused, well-contexted steps.

---

## SLIDE 30: Four Context Strategies

Four strategies for managing context: Write — persist data outside the context window. Select — retrieve only what's relevant. Compress — summarize and prune (but measure quality loss). Isolate — use multi-agent systems to separate concerns. The best systems combine all four. Ask: which strategy addresses your biggest bottleneck?

Let me make decomposition concrete. Imagine a code review agent. Monolithic approach: you dump the entire pull request, the style guide, the test results, the ticket description, and the deployment config into one prompt and say "review this." The model produces a vague, unfocused review because the signal-to-noise ratio is terrible.

Decomposed approach: Step one — the agent reads the ticket to understand the intent. Step two — it diffs the code against the style guide. Step three — it checks test coverage for the changed files specifically. Step four — it validates the deployment config. Each step has focused context, and the final review is specific, actionable, and grounded in evidence. Same model, dramatically better output. That's Write, Select, Compress, and Isolate all working together.

---

## SLIDE 31: Multi-Agent Context Architecture

And this is where the industry is heading — multi-agent architectures. Gartner predicts that by 2027, one-third of agentic AI implementations will combine agents with different skills to manage complex tasks.

The pattern is elegant and intuitive: an orchestrator agent receives the task and routes it to specialist agents. A data agent for data retrieval and analysis. A code agent for code generation and review. A research agent for web search and synthesis. A QA agent for validation.

Each specialist gets only the context it needs — no overload, no confusion, no wasted tokens. The orchestrator handles coordination and context routing.

Same principle, applied to AI agents. One caveat: this is useful when specialization is real. Multi-agent is not a reason to create agents for everything — only when the context separation genuinely helps.

---

## SLIDE 32: [LIVE DEMO] Context Engine in Action (NEW)

*[SWITCH to terminal — run demo-context-engine.py]*

Alright — I've shown you six pillars, retrieval principles, the context engine architecture. Now let's see it work. Live, with a real model running locally.

I have a script that asks the exact same question three times — "Fix the login bug" — but with three different levels of context. Same model each time. Let's watch what happens.

*[Run Round 1 — Naive prompt]*

Round 1: vague prompt, no context. Watch the response — generic, could apply to any codebase. The model is guessing because we gave it nothing to work with.

*[Hit Enter for Round 2 — Structured context]*

Round 2: same question, but now we send a system prompt, error logs, the actual code, and user state — all in structured XML. Notice the bordered box showing exactly what we're sending. Watch the difference in the response.

*[Hit Enter for Round 3 — Full context engine]*

Round 3: full context engine. Embeddings, semantic retrieval, ranking, all six pillars assembled. Look at that pillar summary table — every one of the six pillars we just discussed is active. And look at the response quality.

*[Hit Enter for comparison table]*

Same model. Same question. Three rounds. The quality difference isn't subtle — it's dramatic. And the only variable was context.

That's context engineering in practice. Let's look at the research evidence that backs this up.

---

## SLIDE 33: Section Divider: Does It Actually Work?
*[PAUSE — let the audience reset]*

Alright, so I've laid out the theory. I've shown you six pillars, practical techniques, before-and-after examples. The natural question is: does this actually work? Is there rigorous evidence that better context engineering leads to measurably better outcomes?

The answer is: emphatically yes. But before I show you the research data, let me walk you through one real-world case that brings all six pillars together. This is the kind of thing I think makes the framework click.

Consider a common scenario: a customer support agent — an AI chatbot handling product questions for a SaaS platform. The original setup is straightforward: a generic system prompt that says "You are a helpful customer support agent," a RAG pipeline that pulls from the entire documentation library, no memory management, no output structure, and no constraints. Basically, built in an afternoon.

The failure mode? The agent hallucinated product features. A customer would ask "Can your platform do X?" and the agent would confidently say yes — even when the answer was no. It was also giving inconsistent answers to the same question depending on what retrieval noise landed in the context that day. The hallucination rate hit 23% and customer satisfaction scores were tanking.

The first instinct was to upgrade to a bigger model. Sound familiar?

---

## SLIDE 34: Support Bot: The Six-Pillar Fix
*[GESTURE across the six cards]*

Here's how the fix broke down. They rewrote the system prompt with strict constraints, switched to focused retrieval (verified docs only with recency weighting), added session persistence, used XML formatting, and decomposed into a three-step pipeline: classify, retrieve, generate.

*[GESTURE at the result bar]*

The result? Hallucination rate dropped from 23% to under 4%. Same model. Two weeks of work.

---

## SLIDE 35: ACE Framework Results

The ACE framework — Agentic Context Engineering — was developed at Stanford, SambaNova, and UC Berkeley, published October 2025.

*[GESTURE at the big number]*

Results: +10.6% improvement on agentic tasks. 86.9% latency reduction. Faster *and* better — usually those don't go together. The entire intervention was better context management. No model fine-tuning needed. This is strong evidence that context engineering can match GPT-4.1-based agents. To be clear — it's one study, not the final word — but it strongly reinforces what practitioners are seeing.

---

## SLIDE 36: Context Beats Model Upgrades
*[GESTURE at the two-column layout]*

The ACE findings match practical experience. The support bot hallucination dropped from 23% to under 4% from restructured retrieval and constraints — not from model upgrade. Whether academic or production, well-engineered context delivers more improvement than model upgrades.

*[PAUSE]*

That pattern — fix the context first, measure what changes — is the single most important takeaway from this section.

---

## SLIDE 37: When the Model Actually IS the Problem

But I'd be doing you a disservice if I stopped there. Context engineering has real limits.

*[GESTURE at the two-column layout]*

On the left: when context is the bottleneck. You're asking the model to do something it's capable of, but the information it's working with is incomplete, contradictory, or poorly structured. Fix the context, and output quality jumps. That's most of what we've been talking about.

On the right: when the model capability matters. You're asking the model to do something that's genuinely beyond its reasoning capacity — deep math, novel algorithm design, real-time constraint satisfaction without scaffolding. No amount of context engineering will fix that. You need a more capable model.

Here's the rule of thumb: fix context first, measure what changes, then decide. In many production cases documented in the literature, context fixes deliver the majority of the improvement before model upgrades become necessary. If you're in the remaining situations where the model is the real bottleneck, then you upgrade. But start with context. It's cheaper, faster, and more often correct.

---

## SLIDE 38: When to Use Each Approach

So when should you use each approach? Context engineering, fine-tuning, or scaling up to a bigger model?

*[GESTURE at the decision framework]*

Context engineering is where you start — for almost everything. It's the lowest cost, fastest turnaround, easiest to iterate on. If your task is well-defined and the model understands the problem but doesn't have the right information, context engineering will fix it.

Fine-tuning comes next — and it's appropriate for specialized domains where the model needs to learn task-specific patterns that don't transfer from general training. But fine-tuning requires labeled data, compute, and ongoing maintenance. Only go here if context engineering hits a ceiling.

And a bigger model — use that when the task genuinely exceeds the reasoning capacity of your current model. Deep reasoning, novel problem-solving, complex multi-step inference where the model needs to figure something out, not just retrieve it.

Let me walk you through the decision tree — it's on the next slide.

---

## SLIDE 39: The Decision Tree

*[GESTURE at the decision flow]*

The decision tree is straightforward. Start at the top: does the model understand the problem? If no — upgrade the model. That's a capability issue, not a context issue.

If yes — is the context complete and well-structured? If no — context engineer. That's where the six pillars come in.

If yes — does the model still struggle? If no — you're done. If yes — consider fine-tuning.

One thing to note: hybrid strategies are common in practice. Many production systems combine context engineering with targeted fine-tuning and selectively route harder tasks to more capable models. It's not always a strict either/or.

---

## SLIDE 40: It Takes a Village

One more thing before we move to the playbook. Context engineering isn't a solo sport. It's cross-disciplinary by nature.

You need data engineers for retrieval pipelines and chunking. You need domain experts to curate knowledge and define constraints — they know what information actually matters. And you need AI engineers to architect the context flows and agent systems. The key question is: who owns each pillar? Instructions might be the AI engineer. Retrieval quality might be the data engineer. Constraints might be the domain expert. Make ownership explicit or it falls through the cracks.

---

## SLIDE 41: Section Divider: Monday Morning Playbook
*[PAUSE]*

Okay, I've given you the theory, the pillars, and the evidence. Now let's get practical. What can you actually do with this? I've distilled everything down into seven items for your Monday morning playbook. Things you can start doing this week.

---

## SLIDE 42: Playbook Items 1-4

**Item 1: Audit your system prompt.** Is it specific to your domain and task, or generic? Read it aloud — if it could apply to any company, it's too generic.

**Item 2: Check your retrieval relevance.** Sample 20 production queries. Are the retrieved docs relevant? If more than 10% are noise, you have a retrieval problem that dwarfs any model issue.

---

## SLIDE 43: Playbook: Structure & Memory
*[GESTURE at the two cards]*

**Item 3: Map your information architecture.** Where does critical information live — working context, session, long-term memory? Draw it out. You'll find it's either duplicated or missing.

**Item 4: Structure your common prompts.** Use XML, JSON, or markdown headers. Takes 30 seconds per prompt. Often produces surprising results.

---

## SLIDE 44: Playbook Items 5-7

**Item 5: Compress thoughtfully.** Measure quality — prune aggressively but verify signal remains.

**Item 6: Decompose your most complex task.** Break it into steps. Each step gets focused context. Decomposition typically improves accuracy by 15-25% on complex workflows by reducing context noise.

**Item 7: Measure context quality.** Before optimizing, establish your baseline: accuracy, hallucination rate, latency on 20 representative tasks.

---

## SLIDE 45: How Do You Know It's Working?

Now, how do you actually measure whether your context engineering efforts are paying off? Here are eight key metrics, organized in two categories.

*[GESTURE at the left column — Output Quality]*

**Output Quality** tells you if the system is actually working:

- **Accuracy** — does the AI produce the right answer?
- **Relevance** — is the output on-topic and useful?
- **Consistency** — do repeated similar queries get similar answers?
- **Confidence** — how often is the model tentative versus overconfident?

*[GESTURE at the right column — Context Health]*

**Context Health** tells you if your context engineering is actually good:

- **Retrieval precision** — are the retrieved documents actually relevant to the question?
- **Coverage** — are you capturing all the information the model needs?
- **Redundancy** — how much duplicate information is in there?
- **Latency** — how fast is context retrieval and processing?

Teams measure output quality constantly but rarely measure context health. Yet the two are deeply connected: poor retrieval precision → poor accuracy; high redundancy → poor latency. Context quality drives output quality.

Before context fixes: irrelevant docs, generic answer, 8 seconds. After: relevant error logs, targeted fix, 3 seconds. Production data shows success rates improving from 58% to 76%, hallucination dropping from 18% to 7%, latency cut in half — all from context restructuring.

---

## SLIDE 46: Your Five-Step Eval Recipe
*[GESTURE at the five steps]*

Here's a practical evaluation recipe you can start tomorrow.

Step one: choose 20 representative tasks from your real production workload. Step two: freeze the model — don't change it. Step three: change exactly one context lever — maybe you restructure the system prompt, improve retrieval, or add constraints. Step four: score accuracy, relevance, and latency on those same 20 tasks. Step five: repeat with the next lever.

One lever at a time, measured against the same baseline. That's how you build confidence that your changes are actually driving improvement.

This gives you a clear, attributable picture of what's working and what's not. No guessing.

---

## SLIDE 47: The Road Ahead

Let me leave you with where this is heading.

*[GESTURE at the road-ahead diagram]*

The trajectory is clear: context engines are replacing naive RAG right now. Multi-agent architectures with specialized context are coming fast — Gartner predicts one-third of agentic AI implementations will use them by 2027. And the ACE research showed us a glimpse of what's further out: systems that evolve their own context playbooks automatically. Context engineering partially automating itself.

And here's my personal prediction — this is opinion, not a sourced forecast: by 2027, "context engineer" will be as common a role title as "data engineer" is today. Mark my words.

---

## SLIDE 48: Reveal Part 1 - The Viral Post Unpacked
*[GESTURE back to the opening]*

So let me bring it full circle, and answer the question I posed at the very beginning.

Remember that viral post I showed you? "This isn't funny." Claude Code replicated a year of work in an hour?

*[LONG PAUSE]*

Let's look at what actually happened.

The team posting had been iterating on distributed agent orchestrators for a year. Not from scratch — they'd built several versions already. They'd figured out the architecture. They'd iterated on the prompts. They'd refined what to ask for. They'd debugged the context.

A year's worth of context engineering work.

What they did with Claude Code was take all of that accumulated understanding and, yes, implement the polished version much faster than they could manually code it. That's what the model is good at. But the intelligence in that implementation? The architecture? The constraints? The context? All of that came from a year of human work understanding the problem deeply.

*[PAUSE]*

The model didn't magically know what to build. The context was so well-engineered that the model could execute on it perfectly.

---

## SLIDE 49: Reveal Part 2 - The Real Insight
*[GESTURE at the big reveal]*

And this is the real insight I want you to carry with you.

That post that went viral — everyone read it as "look how powerful the model is." But if you understand context engineering, you read it as something else entirely: "look what becomes possible when you engineer your context right."

The model isn't the problem. The context is. And conversely, when the context is good, the model becomes phenomenally capable.

That's not diminishing the model. That's clarifying the relationship. The model and the context are partners. A capable model with bad context fails. A capable model with good context succeeds spectacularly.

*[PAUSE]*

You now have the six pillars. You understand the stakes. You have a playbook. You know how to measure. You know when context is the bottleneck and when to escalate to the model.

And you understand that that viral post wasn't about the model at all.

It was about context engineering.

---

## SLIDE 50: Now the AI Knows What You Mean
*[SLOW DOWN — this is the closing moment]*

So let me bring it all together.

Remember "fix the login bug"? The AI that didn't know what you meant?

*[LONG PAUSE]*

The model often wasn't the main problem. The context was. And now you know how to fix it.

You've got six pillars to work with. Seven concrete steps you can take this week. Research increasingly showing that context engineering can rival or outperform heavier interventions on many production-style tasks. And a new lens for evaluating every AI system you touch.

And you now know the story behind that viral post — that wasn't about the model's raw power. It was about context engineering done right.

Here's what I want you to do: Audit one system this week. Improve its context. Measure what changes. And I promise you — you'll discover opportunities you didn't know were there.

If you remember nothing else, remember four words: **Audit, prune, structure, measure.** That's your Monday morning starting point.

Thank you.

---

## SLIDE 51: Questions
*[OPEN FOR Q&A]*

I'm ready for questions. What do you want to dig into?


*Expand any question below for a suggested response.*

<div class="qa-index">

<div class="qa-section-title">Questions About the Core Concept</div>

<details>
<summary>How is context engineering different from prompt engineering?</summary>
<div class="qa-answer">Prompt engineering is a subset of context engineering. Prompt engineering focuses on crafting the text of a single input. Context engineering is the full system: instructions, retrieval pipelines, memory architecture, formatting, constraints, and workflow decomposition. It's the difference between writing one email well and designing the entire communication system. The Anthropic engineering blog frames it as "what configuration of context is most likely to generate the desired behavior" — that's a systems design question, not a copywriting question.</div>
</details>

<details>
<summary>Isn't this just RAG with extra steps?</summary>
<div class="qa-answer">RAG is one pillar (Retrieval) out of six. A team can have excellent RAG and still fail because their system prompt is generic, their context window is unstructured, they have no constraints, and they're cramming everything into one massive prompt. Context engineering treats all six pillars as an integrated system. RAG is necessary but not sufficient.</div>
</details>

<details>
<summary>Does context engineering work with all models, or only frontier models?</summary>
<div class="qa-answer">It works across models — that's actually one of the key findings. The ACE framework research showed context-engineered systems matching GPT-4.1-based agents without fine-tuning. In practice, a well-contexted smaller model often outperforms a poorly-contexted larger one. Start with context engineering on whatever model you have; upgrade the model only after you've optimized context.</div>
</details>

<details>
<summary>You mentioned the ACE framework showed +10.6% accuracy. Is that a meaningful improvement?</summary>
<div class="qa-answer">In the context of agentic tasks, yes — these are complex, multi-step workflows where even small accuracy gains cascade across steps. But the more striking number is the 86.9% latency reduction. Faster AND better is rare in AI. The mechanism is straightforward: focused context means fewer wasted tokens, which means faster inference and less noise for the model to parse. As noted in the talk, it's one study — strong directional evidence, not the final word.</div>
</details>

<hr>

<div class="qa-section-title">Questions About Implementation</div>

<details>
<summary>Where do I start? All six pillars feel overwhelming.</summary>
<div class="qa-answer">Use the diagnostic ladder from the talk: (1) Is your system prompt specific? (2) Is retrieval pulling relevant docs? (3) Is context structured? (4) Are constraints explicit? (5) Should the task be decomposed? Work top to bottom. Most teams find their biggest win in pillar 1 (rewriting a generic system prompt) or pillar 2 (fixing retrieval relevance). The Monday morning playbook gives you seven concrete steps — start with items 1 and 2 this week.</div>
</details>

<details>
<summary>How do I measure context quality vs. model quality?</summary>
<div class="qa-answer">Use the five-step eval recipe: freeze the model, change exactly one context lever, score 20 representative tasks on accuracy/relevance/latency, then repeat with the next lever. Track both output quality metrics (accuracy, relevance, consistency, confidence) and context health metrics (retrieval precision, coverage, redundancy, latency). If improving context moves the output metrics, context was the bottleneck.</div>
</details>

<details>
<summary>How much time does context engineering actually take?</summary>
<div class="qa-answer">The system prompt rewrite example in the talk took 20 minutes and caught a race condition the old prompt missed. Structuring prompts with XML tags takes 30 seconds per prompt. The support bot case study was two weeks of work for a hallucination drop from 23% to under 4%. The ROI is typically very fast because you're not training models or building new infrastructure — you're reorganizing information you already have.</div>
</details>

<details>
<summary>What tools should I use for context engineering?</summary>
<div class="qa-answer">There's no single "context engineering tool" — it's a practice applied across your stack. For retrieval: whatever vector DB you're using (ChromaDB to start, Pinecone/Weaviate at scale). For memory: session stores and summarization pipelines. For evaluation: custom scoring scripts against your 20 representative tasks. The tooling is less important than the methodology.</div>
</details>

<details>
<summary>How do I handle context rot in production?</summary>
<div class="qa-answer">Four practical mitigations: context pruning (remove irrelevant old messages), summarization (condense conversation history into digests), session resets (start fresh when context gets too long), and sliding windows (keep only the last N relevant turns). Monitor conversation length vs. output quality — when you see accuracy drop at a consistent turn count, that's your pruning threshold.</div>
</details>

<hr>

<div class="qa-section-title">Questions About Retrieval & RAG</div>

<details>
<summary>What's the right chunk size for RAG?</summary>
<div class="qa-answer">There's no universal answer, but the litmus test from the talk is useful: if a chunk makes sense to a human on its own, it will make sense to the model. Fixed 512-token chunks that break mid-paragraph are a common anti-pattern. Use semantic chunking that respects document structure — paragraphs, sections, code blocks. Start with larger chunks and shrink only if retrieval precision drops.</div>
</details>

<details>
<summary>How do I handle deprecated docs in my RAG index?</summary>
<div class="qa-answer">Add a "last-verified" metadata tag and a recency filter to your retrieval pipeline. When docs are updated, flag old versions. The talk describes a documentation agent giving wrong API answers because deprecated docs were still in the index — a recency filter and metadata tag eliminated the problem overnight.</div>
</details>

<details>
<summary>What's the difference between naive RAG and a context engine?</summary>
<div class="qa-answer">Naive RAG: embed query → find similar documents → dump them in the prompt. A context engine: retrieval + verification (is this doc current and accurate?) + reasoning (is this relevant to THIS specific question?) + access control (is this user authorized to see this?). The operational difference is between "here are the 5 most similar documents" and "here are the 3 documents that are verified current, relevant to this question type, and authorized for this user."</div>
</details>

<hr>

<div class="qa-section-title">Questions About Memory & Formatting</div>

<details>
<summary>Can you explain the "lost in the middle" problem more?</summary>
<div class="qa-answer">Stanford/UC Berkeley/Samaya AI research found that LLMs use information at the beginning and end of the context window effectively, but information placed in the middle gets significantly less attention. This is an architectural property of transformer attention mechanisms. The practical fix: front-load your most important information, back-load constraints and output format, compress the middle aggressively.</div>
</details>

<details>
<summary>How should I structure my prompts? XML, JSON, or markdown?</summary>
<div class="qa-answer">All three work — the key is using any consistent semantic structure rather than unstructured text. XML tags are popular because they create clear, labeled boundaries the model can parse. JSON works well for structured data. Markdown headers work for document-style context. The FlowHunt analysis cited in the talk found 30-40% error rate reductions just from structuring inputs. Pick one format and be consistent.</div>
</details>

<hr>

<div class="qa-section-title">Questions About Multi-Agent & Decomposition</div>

<details>
<summary>When should I use multi-agent architectures vs. a single prompt?</summary>
<div class="qa-answer">Use multi-agent when specialization is real — when different steps of your workflow genuinely benefit from different context. The code review example in the talk decomposes into: understand the ticket → diff against style guide → check test coverage → validate deployment config. Each step has focused context and produces better results. Don't create agents for the sake of it — only when context separation genuinely helps.</div>
</details>

<details>
<summary>How do agents share context without losing information?</summary>
<div class="qa-answer">Through an orchestrator that manages context routing. Each specialist agent gets only what it needs, and the orchestrator aggregates results. The key is explicit interfaces between agents — what information flows in, what flows out. Think of it like microservices: clear contracts, focused responsibilities.</div>
</details>

<hr>

<div class="qa-section-title">Skeptical / Pushback Questions</div>

<details>
<summary>Isn't this just good software engineering applied to AI?</summary>
<div class="qa-answer">Yes, and that's the point. The talk frames context engineering as "systems engineering, not aesthetic prompt writing." The same principles that make software systems reliable — clear interfaces, focused components, structured data, explicit constraints, measurable outcomes — apply directly to AI systems. The gap is that most teams treat AI prompts as one-off text rather than engineered systems.</div>
</details>

<details>
<summary>My team doesn't have time for this. We're shipping features.</summary>
<div class="qa-answer">The system prompt rewrite takes 20 minutes. Structuring your 5 most common prompts takes an afternoon. The support bot case study was 2 weeks. Compare that to weeks spent debugging inconsistent AI outputs, or months evaluating model upgrades that don't solve the actual problem. Context engineering is typically the fastest path to better AI output because you're reorganizing existing information, not building new systems.</div>
</details>

<details>
<summary>Won't this all be automated away as models get smarter?</summary>
<div class="qa-answer">Possibly some of it — the talk's road ahead section mentions context engineering partially automating itself. But even the ACE research showed that structured context still dramatically outperforms unstructured context on frontier models. As long as models operate on context windows, the quality of what goes in will determine the quality of what comes out. And as agents become more autonomous, context engineering becomes more important, not less — an agent with bad context makes confident mistakes at scale.</div>
</details>

<details>
<summary>We tried RAG and it didn't work. Why would context engineering be different?</summary>
<div class="qa-answer">RAG failing is often a symptom of broader context problems — bad chunking, no recency filtering, no relevance verification, irrelevant docs in the index. The six-pillar framework helps you diagnose which specific aspect failed. Was it the retrieval itself, the formatting of retrieved content, missing constraints, or trying to do too much in one prompt? "RAG didn't work" usually means one specific pillar needs fixing, not that the approach is wrong.</div>
</details>

<hr>

</div>

---

## SLIDE 52: CLOSING SLIDE
*[Hold this briefly]*

Thank you all for your time and attention today. My contact info is on screen — training@getskillsnow.com is the best way to reach me. And you can find more of my work at techskillstransformations.com and getskillsnow.com. If you're working on context engineering challenges at your organization, I'd genuinely love to hear about it.

Remember: better context often beats bigger models. Audit, prune, structure, measure. Start this week.

---

# Timing & Pacing Guide

| 26-28 | ~5 min | Pillar 5: Constraints, context smells, diagnosis |
| 29-31 | ~5 min | Pillar 6: Decomposition, strategies, multi-agent |
| 32-33 | ~5 min | Does it work? Support bot case study |
| 34 | ~2 min | Evidence: ACE framework |
| 35-39 | ~4.5 min | Context beats model upgrades, boundary conditions, decision framework, collaboration |
| 40-43 | ~5 min | Monday morning playbook (7 items) |
| 44-45 | ~4 min | Metrics, measurement, eval recipe |
| 46 | ~3 min | Road ahead |
| 47-48 | ~2 min | Reveal Part 1 & 2 — viral post callback |
| 49-51 | ~3 min | Closing, questions, thank you |
| **Total** | **~65 min** | **Core spoken ~50 min + ~10 min pauses, polls, transitions; ~5 min buffer** |

---

# Key Changes Made in v11



---
