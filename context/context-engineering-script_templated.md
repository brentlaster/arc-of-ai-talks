# Context Engineering: Because the Model Isn't the Problem — v10 Improved Speaker Script

**Duration:** ~60 minutes (raw spoken ~47 min + ~10 min pauses, polls, transitions + ~3 min buffer)
**Target pace:** ~140 words/min | **Spoken word count:** ~6,600 words
**v10 Changes:** Fixed missed "IS output quality" on Slide 40 deck (now matches script "drives"); added "tunable and measurable" engineering framing at Slide 9; added ACE delivery caveat at Slide 32; added optional expansion notes in timing guide.

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


## SLIDE 4: "The AI Should Have Known What I Meant"
*[PAUSE — let the title land]*

So let me start with a scenario that I think every single person in this room has experienced. You're working with an AI — could be ChatGPT, Claude, Copilot, whatever your tool of choice is — and you type something like: "Fix the login bug."

The model comes back with something generic. "To fix a login bug, you'll typically want to check authentication logic, verify password hashing..." It's technically correct, but it's completely useless because the AI doesn't know *your* login bug. It doesn't know your authentication architecture, your error logs, your user base, your constraints. It's making an educated guess based on nothing.

So what do you do? You get frustrated. You think, "I need a better model." You look at GPT-4.1. You think about fine-tuning. You add more compute.

Quick show of hands — how many of you have blamed the model in the last month? *[pause]* Yeah, that's most of the room. You're in good company.

Here's what I'm going to tell you: that's probably backwards. The model isn't the problem. Your context is.

---

## SLIDE 5: What Is Context Engineering?

*[GESTURE at the definition block]*

So what do I mean by context engineering? There's a quote on this slide from the Anthropic engineering blog that I think captures it perfectly: building with language models is becoming less about finding the right words and more about answering — what configuration of context is most likely to generate the desired behavior?

Context engineering is the discipline of designing and managing the full information environment in which an AI system operates. That includes instructions, retrieved data, memory, tool descriptions, formatting, constraints, and workflow structure. Every single one of those layers affects the model's ability to produce the right answer. And most teams are tuning maybe two of them — usually the system prompt and the input data. Everything else is left as default or ignored.

That's the gap we're going to close today.

---

## SLIDE 6: From Prompts to Systems

*[GESTURE at the evolution diagram]*

Here's how to think about this shift. Prompt engineering — the thing most of us have been doing — is a subset of context engineering, not the other way around. A prompt is one piece. Context engineering is the whole system.

When you write a prompt, you're crafting one input. When you do context engineering, you're designing the entire information pipeline: what gets retrieved, how it's structured, what constraints are applied, what the model remembers from prior interactions, and how the workflow is decomposed. That's a systems problem, not a writing problem.

And that's the key mindset shift. We're moving from "how do I phrase this question?" to "how do I build the information environment that makes the right answer inevitable?"

Think about it this way. When a new engineer joins your team, you don't just give them a task and hope for the best. You give them context — documentation, codebase access, team norms, escalation paths, examples of good work. The better the onboarding context, the faster they produce good work. AI systems work exactly the same way. The quality of the output is bounded by the quality of the context you provide.

---

## SLIDE 7: The Enterprise AI Moment

*[GESTURE at the big "40%" number]*

And this shift matters right now more than ever. Look at this stat from Gartner: 40% of enterprise apps will feature task-specific AI agents by late 2026 — up from less than 5% in 2025. That's explosive growth.

But here's the catch — and this is the line I want you to remember from this slide: most enterprises are deploying agents before designing the environments those agents need to operate in. They're building the car without building the road.

Teams that invest in context engineering now will have a structural advantage as agent adoption scales. Because agents are even more sensitive to context quality than simple Q&A systems. An agent that has bad instructions, noisy retrieval, and no constraints isn't just unhelpful — it's actively dangerous. It makes confident mistakes at scale.

---

## SLIDE 8: The Cost of Bad Context

*[GESTURE across the four cards]*

And when context is bad, here's what happens. Four consequences, and I've seen every single one of these in production systems.

Hallucinations — models fabricate answers when context is missing or contradictory. They're not lying; they're filling in gaps because that's what they're built to do.

Wasted compute — stuffing irrelevant tokens wastes money and latency. Every irrelevant document in your context window is compute you're paying for with zero return.

Unreliable outputs — inconsistent behavior from poorly structured inputs. The same question gets different answers depending on what noise happens to be in the context that day.

And eroded trust — users stop using AI systems that can't be depended on. This is the one that kills projects. Technical problems are fixable. Lost trust is much harder to recover.

Context problems masquerade as model problems. And that's the core insight: most of the time, upgrading the model isn't the fix. Fixing the context is.

---

## SLIDE 9: The Six Pillars of Context Engineering
*[PAUSE — let the section divider land]*

Alright, now we know *why* context matters. Let's talk about *what* to actually do about it. I've organized the practice of context engineering into six pillars — six dimensions you can tune independently.

---

## SLIDE 10: Six Pillars Overview

*[GESTURE at the pillar diagram]*

Here they are. Instructions — your system prompts and role definitions. Retrieval — RAG, context engines, how you find information. Memory — what persists across interactions and where. Formatting — structure, ordering, and examples. Constraints — guardrails, boundaries, and rules. And Decomposition — splitting workflows across focused steps or agents.

Each pillar is a lever. Pull one, and you get improvement. Pull them together, and the effects compound. And here's the key thing — every one of these pillars can be tuned and measured independently. This isn't aesthetic prompt writing; it's systems engineering. Let's walk through each one.

---

## SLIDE 11: Pillar 1: Instructions & System Prompts

Pillar one: instructions and system prompts. This is the most foundational thing you can do, because it sets the entire context for how the model will interpret everything that follows.

*[GESTURE at the slide content]*

The recipe is straightforward: Role plus Constraints plus Output Format plus Examples. That's what a good system prompt looks like. "Be helpful" is not a system prompt — it's a guess. You need to tell the model who it is, what domain it operates in, what it's allowed to do, what it's *not* allowed to do, and what a correct answer looks like.

I've seen teams spend weeks evaluating models when their system prompt was three lines of generic text. Swap in a specific, well-constrained prompt and suddenly the "worse" model outperforms the "better" one. It's the single highest-leverage change most teams can make.

And as the Anthropic blog puts it: be thoughtful and keep your context informative, yet tight. That's the design challenge.

---

## SLIDE 12: System Prompts: Before & After

*[GESTURE at the two-column comparison]*

Here's the difference in practice. On the left: "You are a helpful assistant. Please help the user with their questions." Three tokens of useful instruction. Zero constraints, no format, no role. The model has no idea what that means in your domain.

On the right: specific role — senior code reviewer. Specific focus — Python, Django, PostgreSQL. Explicit constraints — no framework migrations, follow PEP-8. Clear format — return diff blocks with severity ratings. And examples.

That's specific, actionable, constrained. The model knows who it is and what success looks like.

And here's the payoff — with the generic prompt, the model gives you boilerplate. "Check your authentication logic." With the specific one, it says: "Pod crash-loop in auth-service is caused by a misconfigured OIDC callback URL in deployment manifest line 47." Same model. Night and day.

---
## SLIDE 13: The System Prompt Win
*[GESTURE at the before/after card]*

This is the example I want you to take home. A team had a code review agent producing useless, generic feedback — "consider adding error handling," "this could be more efficient." The agent had a three-line system prompt.

They rewrote it in 20 minutes: specific role, language stack, coding standards, review format. First review after the change caught an actual race condition in a database connection pool.

*[PAUSE for emphasis]*

No model upgrade. No new data. Just a better system prompt. That's the kind of win I want you to walk away with today.

---
## SLIDE 14: Anti-Pattern: Tool Bloat

Now, one particular thing under instructions that I see break a lot of production systems: tool overload.

*[GESTURE at the quote]*

As the Anthropic engineering blog says: if a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better.

The fix: fewer tools with clear boundaries. Each tool should have a clear, distinct purpose. Curate diverse canonical examples, not a laundry list. And here's a good test: can you explain when to use each tool in one sentence? If you can't, neither can the agent.

The model can only reason from what it's given. Clarity beats volume every time. And clarity often means removing things, not adding them.

---

## SLIDE 15: Pillar 2: Retrieval — The Right Information

Pillar two: retrieval and data selection. This is where a lot of systems start to fail.

*[GESTURE at the slide]*

RAG is one of the most powerful tools for context engineering — but most implementations are naive. The chunking problem alone trips up the majority of teams. Too small, and you lose the surrounding context needed for meaningful answers. Too large, and you get noisy embeddings that are hard to pinpoint.

The golden rule I use: if a chunk makes sense to a human on its own, it will make sense to the model. That's your litmus test.

Quick example: a team I know had a documentation agent that was giving confidently wrong answers about their API. Turns out, their retrieval was pulling from deprecated docs that hadn't been removed from the index. The model had no way to know the docs were stale — it just treated them as ground truth. They added a recency filter and a "last-verified" metadata tag, and the accuracy problem disappeared overnight. Same model, same embeddings — just smarter retrieval.

---
## SLIDE 16: Three Retrieval Principles
*[GESTURE across the three cards]*

Three principles that fix most retrieval problems.

First — quality in equals quality out. The bottleneck in most RAG systems is not the embedding model or the vector database. It's the quality of what goes in. If you're retrieving irrelevant documents, the model is wasting tokens parsing noise.

Second — recency matters. A team I know had a documentation agent giving confidently wrong answers. Their retrieval was pulling from deprecated docs. They added a recency filter and a "last-verified" metadata tag, and the accuracy problem disappeared overnight.

And third — measure impact. Every time you change your retrieval, track retrieval precision alongside output accuracy. If you're not measuring context quality, you're guessing.

---
## SLIDE 17: Naive RAG vs. Context Engine

*[GESTURE at the comparison diagram]*

This diagram shows the key evolution. On one side: naive RAG. Embed your query, find similar documents, dump them in. On the other: a context engine — where retrieval, verification, reasoning, and access control are all integrated.

Let me ground this with our login bug. A customer reports a login failure. Naive RAG retrieves password reset documentation, general auth best practices — noise. A context engine retrieves authentication error logs, recent session data, the specific OAuth configuration — exactly what the model needs to diagnose the issue.

Put simply: a context engine is not just retrieval — it's the system that selects, shapes, verifies, prioritizes, and routes information for the model.

---

## SLIDE 18: The Retrieval Evolution (Practitioner Mental Model)

*[GESTURE at the timeline]*

And here's the trajectory. This is a practitioner's mental model, not an industry standard taxonomy, but I find it useful.

Classic RAG in 2024: retrieve docs by semantic similarity. You embed your query, find the closest documents, and dump them in. In 2025: vector orchestration — now you're coordinating text, knowledge graphs, and API calls, not just similarity search. And in 2026: context engines — retrieval plus verification, reasoning, and access control in one pipeline.

In operational terms: the difference is between "here are the five most similar documents" and "here are the three documents that are verified current, relevant to this specific question type, and authorized for this user." That's a fundamentally different retrieval contract.

If your retrieval system is still doing basic similarity search while the state of the art has moved to verified, reasoned selection — you're leaving the biggest lever on the table.

---

## SLIDE 19: Pillar 3: Memory

Pillar three — memory. And this is where things get really fascinating, because there's a fundamental, well-documented problem with how language models handle long contexts.

*[GESTURE at the diagram]*

This is the "lost in the middle" problem, discovered by researchers at Stanford, UC Berkeley, and Samaya AI. They ran a series of careful experiments asking: if you place critical information at different positions in a long context window, how does model performance change?

The answer is dramatic. Information at the beginning of the context — models use it well. High performance. Information at the end — also good. But put critical information in the *middle* of a long context, and performance drops significantly.

Why does this happen? It's an architectural consequence. Transformer models have certain structural properties in their attention mechanism. Tokens at the beginning of the context get attended to by every subsequent token — they accumulate enormous attention weight. Tokens at the end benefit from recency. But information in the middle? In practice, it's often used less effectively. The exact mechanism varies by architecture, but the operational takeaway is consistent across models.

---
## SLIDE 20: Position Your Context Wisely
*[GESTURE at the position diagram]*

So what do you do with the lost-in-the-middle finding? Three practical actions.

Information at the beginning gets high attention weight from all subsequent tokens. Information at the end benefits from recency. But the middle? Performance drops significantly there.

The action items: front-load your most important information. Back-load your constraints and output format. And compress the middle aggressively — but measure quality as you go, because not every context compresses well.

Some teams report meaningful token savings while preserving the information that actually matters, though results vary significantly by task and implementation.

---
## SLIDE 21: Context Layers Architecture

Here's how to think about memory architecturally. I find this four-layer model really useful.

At the top: working context. That's the immediate prompt — system instructions, agent identity, selected conversation history, tool outputs, retrieved documents. This is what the model sees right now, in this moment.

Next: the session layer. The durable log of the current interaction. Everything that's happened in this conversation, even if it's not all in the working context right now.

Then: memory. Long-lived, searchable knowledge that outlives any single session. The model's accumulated understanding. Think of this as its institutional memory — what it learned in previous conversations that's still relevant.

And finally: artifacts. Large binary or textual data — documents, images, code repositories. These are referenced but not necessarily sitting in the context window. They're available when needed.

Let me make this concrete with our support bot. Working context: the current customer question plus the system prompt and retrieved docs. Session: the full conversation history so this customer doesn't have to repeat themselves. Memory: knowledge from thousands of prior support conversations — "customers who ask about X usually mean Y." Artifacts: the full product documentation library, queried on demand. Each layer has a different lifetime and a different retrieval strategy. The art is in knowing what goes where.

---

## SLIDE 22: Pillar 4: Formatting & Structure

Pillar four — and this one genuinely surprises people when I show them the data.

*[GESTURE at the comparison]*

Here's a design principle that holds across every production system I've worked with: relevant, focused tokens often outperform much larger unfocused ones. When you structure information well — using XML tags, JSON structure, or markdown headers — versus dumping raw text, the difference in model performance can be dramatic.

Why? Because formatting isn't cosmetic — it's *functional*. When you use semantic boundaries like tags and headers, the model actually uses them to parse and prioritize information. Think of them like section headers in a textbook. Without them, the model has to infer what each piece of information is and how it relates to everything else. With them, the structure is explicit.

And positioning matters too. Remember the lost-in-the-middle problem? That's not just a memory issue — it applies to everything in your context. Front-load your most important information. Back-load your constraints and output format. Don't bury the critical stuff in the middle of a wall of text.

---

## SLIDE 23: Structure Changes Everything

Here's a concrete example that I use in my training sessions because it makes the point so viscerally.

*[GESTURE left]*

On the left: unstructured. A wall of text describing a bug report — the user, the timeline, the error rate, a hypothesis from QA — all jumbled together in a natural language paragraph. The model has to parse intent, separate facts from speculation, identify the actual request, and figure out what to prioritize. It's doing natural language processing just to understand the *prompt*.

*[GESTURE right]*

On the right: the exact same information, but structured with clear XML tags. Symptom. Timeline. Hypothesis. Each piece of information clearly delineated and labeled. The model knows instantly what each piece is and how to use it.

And here's where the login bug comes back into the picture. Back to our login bug scenario — same information about authentication failures, user state, and code context, but now structured with clear sections. The model can instantly navigate the critical details: where the error occurred, when, what the user state was, and what the code shows. No parsing needed. No confusion.

This takes maybe 30 seconds longer to format. The difference in output quality is dramatic. In one project I worked on — this is anecdotal, not a controlled study — the team saw error rates drop significantly, on the order of 30-40%, just by structuring the input context. Not changing the model. Not adding data. Just organizing what was already there. Your mileage will vary, but the direction is consistent.

---

## SLIDE 24: Pillar 5: Constraints & Guardrails

Pillar five — constraints. And I want to be really direct about this: telling the model what *not* to do is every bit as important as telling it what to do.

*[GESTURE across the four cards]*

There are four types of constraints you should be thinking about. Output format constraints — JSON schemas, response length limits, required fields, structural requirements. Behavioral constraints — no speculation without evidence, cite your sources, escalate when uncertain rather than guessing. Domain constraints — stay within approved topics, reject out-of-scope requests gracefully. And safety constraints — PII handling rules, content policies, compliance requirements.

In my experience, most teams spend 90% of their prompt engineering energy on instructions — what the model *should* do — and about 10% on constraints. I'd argue it should be closer to 60/40. Constraints are what separate a demo from a production system. Here's a real example: one team's support chatbot confidently recommended a medication dosage change — something that should always be escalated to a physician. One behavioral constraint — "never provide specific medical dosing; always escalate to a healthcare professional" — fixed it. That's the difference constraints make.

---

## SLIDE 25: Context Smells: Red Flags to Watch For

Before we move to the last pillar, I want to show you six bad patterns — what I call "context smells." These are warning signs that your context engineering is off the rails. And if you see them, something needs fixing.

Quick show of hands — which of these is your biggest problem right now: prompt sprawl, retrieval noise, or memory overload? *[pause]* Yeah, I see a lot of hands for that one. You're not alone.

*[GESTURE across the six cards as you go through them]*

First: **Prompt sprawl** — Accumulated instructions nobody owns or reviews. Everything in one massive request — instructions, data, history, tool descriptions, rules. The model is drowning.

Second: **Weak role definition** — Generic identity with no domain specifics. "Be helpful" — that's not context engineering, that's a guess.

Third: **Retrieval noise** — Irrelevant docs dumped regardless of the question. Remember our login bug? Pulling in password reset docs instead of authentication error logs.

Fourth: **Bad chunking** — Fixed chunks that break semantic boundaries. 512-token chunks regardless of document structure.

Fifth: **Unstructured context** — Raw data straight to the model with no structure. No headers, no tags, no logical boundaries.

And sixth: **Premature model upgrades** — Scaling up without measuring the real bottleneck. You jump to a bigger model without checking whether context was the actual problem.

*[PAUSE for emphasis]*

How many of you recognized at least three of these? Yeah, I see some uncomfortable laughter. You're in good company. I've built systems with all six of these problems. Multiple times. The good news is once you know what they look like, they're fixable.

---
## SLIDE 26: Diagnose Your System
*[GESTURE at the five-step ladder]*

Here's the diagnostic ladder I promised. Think about a system you work with right now. Run it through these five steps.

Step one — is the instruction specific enough? Step two — is retrieval pulling relevant information? Step three — is the context structured? Step four — are constraints explicit? Step five — should this task be decomposed?

And only if all five are solid — *then* ask whether the model itself is the bottleneck. That's your triage sequence. Start at the top and work down.

*[PAUSE]*

Most teams jump straight to "we need a better model" without checking any of these five. That's where the money gets wasted.

---
## SLIDE 27: Pillar 6: Workflow Decomposition

And finally, pillar six — decomposition. This is the architectural pillar, and for complex tasks, it's often the most impactful.

*[GESTURE at diagram]*

The key idea here is on this slide: instead of cramming everything into one massive prompt — what I call the "kitchen sink" approach — you break the work into focused steps. Each step gets exactly the context it needs for that specific task. Nothing more, nothing less. The best production AI systems aren't one giant prompt. They're pipelines of focused, well-contexted steps.

---

## SLIDE 28: Four Context Strategies

Here are four high-level strategies for managing context, and they directly support that decomposition principle.

Write — persist important information outside the context window for later retrieval. Don't rely on in-context memory for everything. Select — retrieve only what's relevant. Resist the urge to dump everything in. Compress — summarize and trim. Prune aggressively, but measure quality loss as you compress. And Isolate — use multi-agent systems to separate concerns. Give each agent a focused context for its specific task.

These strategies aren't mutually exclusive — the best systems combine all four. The question is always: which strategy addresses your biggest bottleneck right now?

Let me make decomposition concrete. Imagine a code review agent. Monolithic approach: you dump the entire pull request, the style guide, the test results, the ticket description, and the deployment config into one prompt and say "review this." The model produces a vague, unfocused review because the signal-to-noise ratio is terrible.

Decomposed approach: Step one — the agent reads the ticket to understand the intent. Step two — it diffs the code against the style guide. Step three — it checks test coverage for the changed files specifically. Step four — it validates the deployment config. Each step has focused context, and the final review is specific, actionable, and grounded in evidence. Same model, dramatically better output. That's Write, Select, Compress, and Isolate all working together.

---

## SLIDE 29: Multi-Agent Context Architecture

And this is where the industry is heading — multi-agent architectures. Gartner predicts that by 2027, one-third of agentic AI implementations will combine agents with different skills to manage complex tasks.

The pattern is elegant and intuitive: an orchestrator agent receives the task and routes it to specialist agents. A data agent for data retrieval and analysis. A code agent for code generation and review. A research agent for web search and synthesis. A QA agent for validation.

Each specialist gets only the context it needs — no overload, no confusion, no wasted tokens. The orchestrator handles coordination and context routing.

Same principle, applied to AI agents. One caveat: this is useful when specialization is real. Multi-agent is not a reason to create agents for everything — only when the context separation genuinely helps.

---

## SLIDE 30: Section Divider: Does It Actually Work?
*[PAUSE — let the audience reset]*

Alright, so I've laid out the theory. I've shown you six pillars, practical techniques, before-and-after examples. The natural question is: does this actually work? Is there rigorous evidence that better context engineering leads to measurably better outcomes?

The answer is: emphatically yes. But before I show you the research data, let me walk you through one real-world case that brings all six pillars together. This is the kind of thing I think makes the framework click.

A team I worked with had a customer support agent — an AI chatbot handling product questions for a SaaS platform. The original setup was straightforward: a generic system prompt that said "You are a helpful customer support agent," a RAG pipeline that pulled from the entire documentation library, no memory management, no output structure, and no constraints. Basically, it was built in an afternoon.

The failure mode? The agent was hallucinating product features. A customer would ask "Can your platform do X?" and the agent would confidently say yes — even when the answer was no. It was also giving inconsistent answers to the same question depending on what retrieval noise landed in the context that day. The team measured a 23% hallucination rate and customer satisfaction scores were tanking.

Their first instinct was to upgrade to a bigger model. Sound familiar?

---
## SLIDE 31: Support Bot: The Six-Pillar Fix
*[GESTURE across the six cards]*

Here's how the fix broke down, pillar by pillar. Instructions — they rewrote the system prompt with a specific role and an explicit constraint: "If the answer is not in the retrieved docs, say you don't know and escalate."

Retrieval — they switched to a focused pipeline pulling only from verified, current product docs, with recency weighting. Memory — session persistence so customers don't repeat themselves. Formatting — XML tags separating capabilities, limitations, and pricing. Constraints — never speculate, never promise features not in docs, escalate billing to humans. And decomposition — a three-step pipeline: classify the question, retrieve docs for that type, then generate.

*[GESTURE at the result bar]*

The result? Hallucination rate dropped from 23% to under 4%. Same model. Two weeks of work. That's what systematic context engineering looks like.

---
## SLIDE 32: ACE Framework Results

This is the research that made me sit up straight in my chair when I first read it. The ACE framework — Agentic Context Engineering — developed by a team at Stanford, SambaNova, and UC Berkeley. Published in October 2025.

*[GESTURE at the big number]*

Plus 10.6 percent improvement on benchmarked agentic tasks. Not from a bigger model. Not from expensive fine-tuning. From engineering the context. That's the entire intervention — better context management.

And look at this secondary stat: 86.9% average latency reduction. Faster AND better. In my experience, those two things almost never go together in AI. Usually, better quality means more compute. Here, better context meant *less* compute because you're not wasting tokens on irrelevant information.

What ACE showed is that, in that specific benchmarked setup, context-engineered systems matched GPT-4.1-based agents without any model fine-tuning. It treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a cycle of generation, reflection, and curation.

That last point is profound: the context itself evolves and improves over time. The system learns what context works and what doesn't. Now, to be clear — this is strong evidence for the direction of the field, not a guarantee that context engineering replaces model choice in every scenario. It's one study, not the final word — but it strongly reinforces the pattern practitioners are already seeing.

---
## SLIDE 33: Context Beats Model Upgrades
*[GESTURE at the two-column layout]*

And here's a real-world example that reinforces the ACE findings. One team had a customer support agent hallucinating product features — telling customers about capabilities that didn't exist. They were about to switch to a bigger model.

Instead, they restructured their retrieval to pull only from verified product documentation. They added one constraint: "if the answer isn't in the retrieved docs, say you don't know."

Hallucination rates dropped from 23% to under 4%. No model change. No fine-tuning. Just better context.

*[PAUSE]*

That pattern — fix the context first, measure what changes — is the single most important takeaway from this section.

---
## SLIDE 34: When the Model Actually IS the Problem

But I'd be doing you a disservice if I stopped there. Context engineering has real limits.

*[GESTURE at the two-column layout]*

On the left: when context is the bottleneck. You're asking the model to do something it's capable of, but the information it's working with is incomplete, contradictory, or poorly structured. Fix the context, and output quality jumps. That's most of what we've been talking about.

On the right: when the model capability matters. You're asking the model to do something that's genuinely beyond its reasoning capacity — deep math, novel algorithm design, real-time constraint satisfaction without scaffolding. No amount of context engineering will fix that. You need a more capable model.

Here's my rule of thumb: fix context first, measure what changes, then decide. In many production cases I've seen, context fixes deliver the majority of the improvement before model upgrades become necessary. If you're in the remaining situations where the model is the real bottleneck, then you upgrade. But start with context. It's cheaper, faster, and more often correct.

---

## SLIDE 35: When to Use Each Approach

So when should you use each approach? Context engineering, fine-tuning, or scaling up to a bigger model?

*[GESTURE at the decision framework]*

Context engineering is where you start — for almost everything. It's the lowest cost, fastest turnaround, easiest to iterate on. If your task is well-defined and the model understands the problem but doesn't have the right information, context engineering will fix it.

Fine-tuning comes next — and it's appropriate for specialized domains where the model needs to learn task-specific patterns that don't transfer from general training. But fine-tuning requires labeled data, compute, and ongoing maintenance. Only go here if context engineering hits a ceiling.

And a bigger model — use that when the task genuinely exceeds the reasoning capacity of your current model. Deep reasoning, novel problem-solving, complex multi-step inference where the model needs to figure something out, not just retrieve it.

The decision tree is straightforward: Does the model understand the problem? No → upgrade the model. Yes → is the context complete and well-structured? No → context engineer. Yes → does the model still struggle? No → you're done. Yes → consider fine-tuning.

One thing to note: hybrid strategies are common in practice. Many production systems combine context engineering with targeted fine-tuning and selectively route harder tasks to more capable models. It's not always a strict either/or.

---

## SLIDE 36: It Takes a Village

One more thing before we move to the playbook. Context engineering isn't a solo sport. It's cross-disciplinary by nature.

You need data engineers for retrieval pipelines and chunking. You need domain experts to curate knowledge and define constraints — they know what information actually matters. And you need AI engineers to architect the context flows and agent systems. The key question is: who owns each pillar? Instructions might be the AI engineer. Retrieval quality might be the data engineer. Constraints might be the domain expert. Make ownership explicit or it falls through the cracks.

---

## SLIDE 37: Section Divider: Monday Morning Playbook
*[PAUSE]*

Okay, I've given you the theory, the pillars, and the evidence. Now let's get practical. What can you actually do with this? I've distilled everything down into seven items for your Monday morning playbook. Things you can start doing this week.

---

## SLIDE 38: Playbook Items 1-4

**Item 1: Audit your system prompt.** That's Pillar 1 — Instructions. Is it specific to your domain and task? Or is it generic? If you're using "You are a helpful assistant," you're leaving value on the table. Write a system prompt that's actually specific to what you need. Here's a quick test: read your system prompt out loud. If it could apply to any company in any industry, it's too generic.

**Item 2: Check your retrieval relevance.** That's Pillar 2 — Retrieval. Take 20 queries you've actually seen in production. Look at the documents you're retrieving for each one. Are they relevant? Or are they noise? If more than 10% are irrelevant, you have a retrieval problem that dwarfs any model problem. This is a one-afternoon exercise that will tell you more about your system's failure modes than any model benchmark.

---
## SLIDE 39: Playbook: Structure & Memory
*[GESTURE at the two cards]*

Items 3 and 4 — the two I see teams overlook most often.

Item 3: map your information architecture. That's Pillar 3 — Memory. Where does critical information live? Working context? Session? Long-term memory? Draw it on a whiteboard. You'll probably find that important information is either duplicated in three places or missing from all of them.

Item 4: structure your most common prompts. That's Pillar 4 — Formatting. Take your five most frequent tasks. Use XML, JSON, or markdown headers. This takes 30 seconds per prompt and can cut error rates dramatically.

These two items together take less than a day and often produce the most surprising results.

---
## SLIDE 40: Playbook Items 5-7

**Item 5: Compress thoughtfully.** That's Pillar 3 again — Memory. Memory compression can meaningfully reduce token usage, but measure quality to make sure you're not losing important information. The goal isn't minimum tokens — it's maximum signal per token. Prune what doesn't contribute, but verify that what remains still gives the model what it needs.

**Item 6: Decompose your most complex task.** That's Pillar 6 — Decomposition. Take one high-stakes task in your system. Instead of doing it in one massive prompt, decompose it into steps. Each step gets the context it actually needs. See what improves. In production systems I've worked with, decomposition has improved task accuracy meaningfully — often on the order of 15-25% on complex workflows — just by reducing context noise at each step. Your results will depend on the complexity of the task and the quality of your current context.

**Item 7: Measure context quality.** This one cuts across all the pillars. Before you start optimizing context, measure your current accuracy, hallucination rate, and latency. You can't know if your changes worked if you don't know where you started. Pick 20 representative tasks, run them through your system, and score them. That's your baseline. Everything else is measured against it.

These seven items will keep you busy for a month. And I promise you — you'll find major opportunities in at least three of them.

---

## SLIDE 41: How Do You Know It's Working?

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

Here's what I want you to notice: teams measure output quality all the time. But they rarely measure context health. And the two are deeply connected. If your retrieval precision is poor, your accuracy will follow. If you have high redundancy, your latency suffers. Context quality drives output quality. Start measuring both.

Think about our login bug one more time. Before context fixes: the system pulled in irrelevant docs, gave a generic answer, took 8 seconds. After: relevant error logs, targeted fix, 3 seconds. That's what these metrics capture — the before and after of real context work.

To make this concrete — one production team I worked with reported their task success rate improving from 58% to 76%, hallucination rate dropping from 18% to 7%, and average latency cut in half, all from context restructuring alone. Those are their numbers, not a controlled study, but the pattern is consistent with what other teams report.

---
## SLIDE 42: Your Five-Step Eval Recipe
*[GESTURE at the five steps]*

Here's a practical evaluation recipe you can start tomorrow.

Step one: choose 20 representative tasks from your real production workload. Step two: freeze the model — don't change it. Step three: change exactly one context lever — maybe you restructure the system prompt, improve retrieval, or add constraints. Step four: score accuracy, relevance, and latency on those same 20 tasks. Step five: repeat with the next lever.

One lever at a time, measured against the same baseline. That's how you build confidence that your changes are actually driving improvement.

This gives you a clear, attributable picture of what's working and what's not. No guessing.

---
## SLIDE 43: The Road Ahead

Let me leave you with where this is heading.

*[GESTURE at the road-ahead diagram]*

The trajectory is clear: context engines are replacing naive RAG right now. Multi-agent architectures with specialized context are coming fast — Gartner predicts one-third of agentic AI implementations will use them by 2027. And the ACE research showed us a glimpse of what's further out: systems that evolve their own context playbooks automatically. Context engineering partially automating itself.

And here's my personal prediction — this is opinion, not a sourced forecast: by 2027, "context engineer" will be as common a role title as "data engineer" is today. Mark my words.

---

## SLIDE 44: Now the AI Knows What You Mean
*[SLOW DOWN — this is the closing moment]*

So let me bring it full circle.

Remember "fix the login bug"? The AI that didn't know what you meant?

*[LONG PAUSE]*

The model often wasn't the main problem. The context was. And now you know how to fix it.

You've got six pillars to work with. Seven concrete steps you can take this week. Research increasingly showing that context engineering can rival or outperform heavier interventions on many production-style tasks. And a new lens for evaluating every AI system you touch.

Here's what I want you to do: Audit one system this week. Improve its context. Measure what changes. And I promise you — you'll discover opportunities you didn't know were there.

If you remember nothing else, remember four words: **Audit, prune, structure, measure.** That's your Monday morning starting point.

Thank you.

---

## SLIDE 45: Questions
*[OPEN FOR Q&A]*

I'm ready for questions. What do you want to dig into?

---


## SLIDE 46: CLOSING SLIDE
*[Hold this briefly]*

Thank you all for your time and attention today. My contact info is on screen — training@getskillsnow.com is the best way to reach me. And you can find more of my work at techskillstransformations.com and getskillsnow.com. If you're working on context engineering challenges at your organization, I'd genuinely love to hear about it.

Remember: better context often beats bigger models. Audit, prune, structure, measure. Start this week.

---

# Timing & Pacing Guide

| Slide | Duration | Section |
|-------|----------|---------|
| 1-3 | ~1 min | Version, title, about me |
| 4 | ~2 min | "The AI should have known" + audience poll |
| 5-8 | ~4 min | Definition, evolution, enterprise moment, cost of bad context |
| 9-10 | ~1 min | Six pillars intro and overview |
| 11-14 | ~5 min | Pillar 1: Instructions, before/after, system prompt win, tool bloat |
| 15-18 | ~4 min | Pillar 2: Retrieval, principles, RAG vs context engine, evolution |
| 19-21 | ~5 min | Pillar 3: Memory, positioning, context layers |
| 22-23 | ~5 min | Pillar 4: Formatting & structure |
| 24-26 | ~5 min | Pillar 5: Constraints, context smells, diagnosis |
| 27-29 | ~5 min | Pillar 6: Decomposition, strategies, multi-agent |
| 30-31 | ~5 min | Does it work? Support bot case study |
| 32 | ~2 min | Evidence: ACE framework |
| 33-36 | ~4.5 min | Context beats model upgrades, boundary conditions, decision framework, collaboration |
| 37-40 | ~5 min | Monday morning playbook |
| 41-42 | ~4 min | Metrics, measurement, eval recipe |
| 43 | ~3 min | Road ahead |
| 44-46 | ~3 min | Closing, questions, thank you |
| **Total** | **~60 min** | **Core spoken ~46 min + ~10 min pauses, polls, transitions; ~4 min buffer** |

---

# Key Changes Made in v10

1. ✓ **Slide 40 (Missed "IS" instance fixed)**: Deck playbook item 7 description changed from "Context quality IS output quality" to "Context quality drives output quality." Both Slide 40 (playbook) and Slide 41 (metrics) now match the script.

2. ✓ **Slide 9 (Engineering framing added)**: Script now includes: "every one of these pillars can be tuned and measured independently. This isn't aesthetic prompt writing; it's systems engineering." Sets the measurement mindset early.

3. ✓ **Slide 32 (ACE delivery caveat strengthened)**: Added: "to be clear — this is strong evidence for the direction of the field, not a guarantee that context engineering replaces model choice in every scenario."

4. ✓ **Timing guide: optional expansion notes added**: Three optional expansion points documented for protecting against delivery underrun.

---

**Voice Notes**: All deck instances of "IS output quality" are now corrected. The engineering-measurement framing at Slide 9 primes the audience for the metrics section. The ACE caveat (Slide 32) is now a three-layer defense: visible "(one benchmarked setup)" on the slide, "in that specific benchmarked setup" in the main script, and "not a guarantee" follow-up line. All slide-level claims match or are softer than the spoken script.

## Optional Expansion Points (if talk runs short)

Use these if delivery is brisk and you need to fill time:

1. **After Slide 26 (diagnostic ladder)**: Extended audience exercise — "Turn to your neighbor and diagnose one AI system using the five-step ladder. You have 90 seconds." (~2 min)
2. **After Slide 32 (ACE results)**: "Let me walk you through how I'd debug an AI system live. Give me a use case from the audience." (~3 min)
3. **After Slide 35 (decision framework)**: Quick show-of-hands poll — "How many of you have tried context engineering before fine-tuning? Before upgrading the model? Before both?" (~1 min)
