## SLIDE 1: VERSION
[Skip]

---


## SLIDE 2: TITLE
[Skip]

---




Good morning, everyone. Before we start, quick show of hands. How many of you saved 15 minutes this week using AI? [PAUSE for hands] Good number. Now how many of you had it cost you 30?

[PAUSE] Yeah. That's the talk.

I'm Brent Laster. I've been working in engineering and technical training for over two decades now. I've seen a lot of technology shifts. But I've never seen one that created this much frustration alongside this much promise. We're all using AI. Every single one of us. And yet when engineers, team leads, and architects are surveyed about how it's going, the honest answer is usually some version of: "It's fine, I guess. I'm not sure it's actually helping." That sentiment shows up consistently in research from Stack Overflow, BCG, and Pew.

That's what we're going to dig into today. We'll look at five specific barriers that are making AI feel harder than it should. Then we'll walk through five achievable shifts — things you can implement this week — that change the experience. And we'll close with a playbook you can take back to your team on Monday.

[TIMING: 2:30]

---


## SLIDE 3: ABOUT ME

[Brief personal introduction - use content on slide]

---


## SLIDE 4: A SHOW OF HANDS

Let's start with the numbers. Across recent workforce studies, a clear pattern is emerging. About 52% of workers are actively using AI tools — that's from Qualtrics. But here's the catch — a separate study from ManpowerGroup found that worker confidence in using technology at work fell sharply by 18 percentage points over roughly the same period, even as AI use rose. Two different studies, same story: adoption going up, confidence going down.

Now, these are broad workforce numbers — not engineering-specific. But the same pattern shows up very clearly in developer workflows, and I'll show you the engineering data in a moment. The point is: this isn't one team's problem. It's structural.

[TIMING: 3:30]

---

## SLIDE 5: AI PRODUCTIVITY PARADOX

Now let me hit you with the uncomfortable numbers. Only about one in four organizations have achieved repeatable ROI from AI across multiple use cases — that's from research by MIT and Wharton. The rest are still trying to figure out how to make this work beyond pilots and proofs of concept.

And among developers specifically, Stack Overflow's 2025 survey tells a stark story: only about one in three developers say they trust AI output accuracy. And 46% actively distrust it. More developers distrust AI-generated code than trust it. That's not a rounding error — that's a fundamental confidence problem.

Meanwhile, Pew Research found that 52% of workers are more worried than hopeful about AI in their workplace. And ActivTrak's analysis of over 443 million hours of work activity found that focus sessions dropped 9% while collaboration time surged after AI adoption. The tools multiply, but the deep-focus time shrinks.

We're using it more. We're enjoying it less. Let's figure out why.

[TIMING: 5:00]

---

## SLIDE 6: THE TEST THAT PASSED

Let me walk you through a scenario that plays out constantly across engineering teams — it's a well-documented pattern, not a single incident.

A team asks their AI assistant to write a unit test for an authentication module. The AI generates a beautiful test. Correct syntax, proper assertions, good structure. It passes on the first run. Team ships it.

Three days later, during a security review, they discover the test never actually validated the token expiry path. Here's the key part — the test checked that a valid token returns 200 OK. But it never tested that an expired token returns 401. It never tested that a token from the wrong issuer gets rejected. It never tested that a revoked session token is caught.

The AI tested the happy path perfectly and skipped the parts that mattered for this team's security posture. The code looked right. It compiled. It passed. But it wasn't testing what it claimed to test.

That gap — between looking correct and being correct — is exactly what makes AI so frustrating for engineers. The failure mode isn't "obviously broken code." The failure mode is "subtly incomplete code that passes every automated check."

[TIMING: 7:15]

---

## SLIDE 7: THE TEST DETAILS

Here's the breakdown of what the AI test actually covered and what it missed.

The test checked three things: token validation returns 200 for valid input, endpoint exists, HTTP structure is correct. Standard happy-path tests.

It never touched the edge cases: expired tokens, wrong issuer, revoked sessions. These weren't in the test at all. The AI's test suite was technically correct for what it tested — but incomplete for the team's actual threat model.

This is why "the code compiles" and "the code passes" aren't the same as "the code is correct for this team." Correctness is application-specific.

[TIMING: 7:45]

---
## SLIDE 8: SECTION DIVIDER — "WHY DOES AI FEEL SO HARD?"

So why is this happening? Why does a tool that's supposed to make our lives easier feel like it's making things harder? After digging into the research — surveys from Stack Overflow, BCG, Pew, and others — plus community discussions across engineering forums, five specific barriers keep surfacing. Not philosophical barriers. Concrete, fixable problems. Let's walk through them.

[TIMING: 7:45]

---

## SLIDE 9: FIVE BARRIERS OVERVIEW

Here are the five:

Too many tools, not enough glue. Nobody told us where AI fits. Promise versus reality. AI brain fry. And pressure to keep up.

Each one feeds the others. Tool sprawl creates confusion about where AI fits, which creates unrealistic expectations, which creates cognitive overload, which creates pressure. It's a cycle. But the good news is that each one is individually addressable. Break one, and the others get easier.

[TIMING: 8:30]

---

## SLIDE 10: BARRIER 1 — TOO MANY TOOLS, NOT ENOUGH GLUE

First barrier. Survey data tells us developers are juggling more AI tools than ever — ActivTrak's 2026 report found the average organization now uses seven AI tools, up from two just two years ago, with 83% of organizations using six or more. IDE copilot, chat interfaces, code search, review assistants, doc generators. Each one is independently useful. But none of them share context with each other.

So YOU become the integration layer. You re-explain the same problem four times to four different systems. AI didn't remove work. It just promoted all of us to unpaid reviewers. That human middleware cost is eating the productivity gains the tools are supposed to provide. The result? Widespread "shadow AI" use when the official tools are weak or slow.

[TIMING: 9:45]

---

## SLIDE 11: THREE-TOOL THRESHOLD

Here's a finding from BCG's 2026 brain fry research that stuck with me: when they looked at AI tool usage patterns, productivity gains rose from one to two tools, peaked at three, and actually dropped past four. At the same time, cognitive strain kept climbing.

It's not a universal law, but it holds up well as a planning heuristic. Think of it like this: if you have one database, you understand your data. Three databases, you're managing replication. Five, you're debugging consistency issues. Same principle applies to AI tools. Past a certain point, the cost of managing the tools exceeds the benefit of having them.

My recommendation: pick your best two to three tools. Go deep. Learn their strengths. Build muscle memory. Let the rest go.

[TIMING: 11:15]

---

## SLIDE 12: ENGINEER'S AI TOOLBOX

Let me make this concrete. Look at a typical engineer's AI stack. You've got an IDE Copilot for inline suggestions. A chat interface for broader questions. A code search tool for codebase Q&A. A review assistant for PR analysis. A ticket summarizer.

Now look at the overlap. Three of those five generate code. Two of them summarize context. And none of them share state. So when you switch from your chat interface to your IDE copilot, you lose all the context from that conversation. You're starting cold every single time.

You're sitting there thinking, "AI is supposed to save me time." But you're spending half that saved time re-establishing context across tools. You are the integration layer, and that is exhausting.

[TIMING: 12:45]

---

## SLIDE 13: BARRIER 2 — NOBODY TOLD US WHERE AI FITS

Second barrier. Most organizations adopted AI by bolting it onto existing workflows. They didn't redesign anything. They just said, "Here's a new tool. Figure out where it goes." And so developers are making ad hoc decisions — sometimes using AI, sometimes not — with no shared understanding of where it adds value and where it doesn't.

In engineering, the problem isn't just "where can AI help?" It's "who now owns correctness, edge cases, and final judgment at each step?" When nobody defines that, AI-generated work creates hidden review debt — more code to verify, more tests to validate, more assumptions to check — and no one is explicitly responsible for catching what AI missed.

BCG found that organizations that communicated clearly about where AI fits in specific workflows saw notably better adoption and satisfaction. It's not mysterious. If people don't know where a tool belongs, they either avoid it or misuse it.

[TIMING: 14:30]

---

## SLIDE 14: ENGINEERING WORKFLOW — THREE REALITIES

Let me show you what this looks like in practice. Three columns — remember this one, because we'll come back to it.

On the left: traditional workflow. Read the ticket, design, code, test, PR, deploy. Slow but clear.

In the middle: bolted-on AI. Same steps, but AI jammed in at random points. You verify everything manually, re-prompt three times, and the review overhead kills you. This is where most teams are right now.

On the right: human-plus-AI. Context fed upfront. Clear roles — you lead design, AI drafts, you review and add edge cases. Clear handoffs, and you submit the PR with confidence.

The middle column is the frustration zone. The right column is what we're aiming for.

[TIMING: 16:30]

---

## SLIDE 15: BARRIER 3 — PROMISE VS. REALITY

Third barrier. AI is almost right a lot of the time. And "almost right" is the most dangerous kind of wrong. If it were obviously broken, you'd catch it. If it were always correct, you could trust it. But "almost right" means you have to verify everything, and the review feels pointless because the output usually looks fine.

Here's how Stack Overflow's 2025 survey put it: 45% of developers said their number one frustration is "AI solutions that are almost right but not quite." That was the top response. And it tracks with the broader research — MIT's 2025 study found that 95% of AI pilots failed to deliver measurable business impact, largely because organizations couldn't get past the verification and scaling challenges.

Many organizations still struggle to demonstrate repeatable, measurable ROI from AI beyond pilots — and a big part of that is the hidden verification cost. The teams that push through it and build good review discipline recover. The ones that don't either give up or ship bugs.

[TIMING: 18:15]

---

## SLIDE 16: WHEN AI CODE LOOKS RIGHT BUT ISN'T

Here's an illustrative example of what "almost right" looks like in code. This slide shows a JWT token validation function. Syntactically perfect. Well-structured. It validates the token signature. It would pass generic unit tests.

But look at what's missing from the team's specific requirements. No expiry check on their timeline. No issuer validation. No audience scope verification. No token revocation check. The AI wrote correct generic code — but it omitted the application-specific checks that actually matter for this team's security posture.

It's like hiring a contractor to build a beautiful kitchen — granite countertops, perfect tile work — and then realizing they never connected the plumbing. Everything looks right until you turn on the faucet. That's the "almost right" problem.

[TIMING: 19:15]

---
## SLIDE 17: PR SUMMARY — LOOKS RIGHT BUT ISN'T

Here's a composite example drawn from a pattern that shows up consistently in engineering teams adopting AI review tools.

A team starts using AI for PR summaries. The AI tool reads the diff and generates: 'Refactored retry mechanism for improved clarity.' Looks perfect. Well-written summary. The reviewer sees that, approves the PR, ships it.

But what actually changed: the retry logic for payment processing. The conditions shifted. The backoff delays changed. The failure recovery path changed. The summary described these as 'minor cleanup.' The reviewer approved without reading the diff closely because the summary made it sound safe.

That's not a code bug. That's a process failure created by incomplete AI output that passed the '80% credibility threshold.' The summary WAS mostly right — it just omitted the part that mattered most.

[TIMING: 19:45]

---

## SLIDE 18: BARRIER 4 — AI BRAIN FRY

Fourth barrier, and this is the one that hits hardest. AI brain fry. For engineers, it's the constant loop of prompting, validating output line by line, re-prompting when it's wrong, and context-switching between tools — all while keeping your own mental model intact. A March 2026 study by BCG and Harvard Business Review surveyed nearly 1,500 workers and coined the term "AI brain fry" — mental fatigue from excessive AI oversight. They found meaningful increases among heavy AI users: 14% more mental effort, 12% more mental fatigue, 19% more information overload, and 33% more decision fatigue. Fourteen percent of knowledge workers reported significant cognitive strain, with software development flagged as one of the highest-prevalence roles. For engineering, that pattern is likely intensified by the verification load we've been talking about.

And here's the irony: AI was supposed to lighten workloads. But ActivTrak's analysis of 443 million hours of work data found that focus sessions dropped 9% while collaboration time surged after AI adoption. The workload didn't shift — it stacked. For engineers, that means more diff review fatigue, more re-prompt cycles, more context reconstruction between tools, and less uninterrupted time for the deep thinking that produces good architecture. You're debugging AI's understanding of your codebase instead of debugging the codebase itself.

[TIMING: 21:15]

---

## SLIDE 19: DEVELOPER BRAIN FRY CYCLE

For engineers specifically, the cycle looks like this. Step one: write a detailed prompt. Step two: inspect the output line by line. Step three: compare against your requirements. Step four: patch what AI got wrong. Step five: re-run and test. Step six: re-validate — did the patch break something else? Step seven: context-switch to the next task.

And this isn't once a day. This cycle happens ten, fifteen, twenty times a day. Every single AI interaction. The generation is fast, sure. But the validation tax — the cognitive cost of verifying every single output — that's where the time goes. And that's what's burning people out.

[TIMING: 22:15]

---
## SLIDE 20: WHERE THE TIME ACTUALLY GOES

Here's the data behind brain fry. BCG's research found directional evidence — not universal benchmarks — that for organizations using AI heavily, collaboration overhead increased meaningfully while focused work time dropped. ActivTrak's large-scale tracking confirmed the pattern: focus sessions down 9%, now averaging just 13 minutes each.

That sounds like small numbers. But for an engineer, even a few percentage points of focused time is 3-4 hours per week. That's your deep-thinking time. Your architecture time. Your 'understand the system better' time.

And the added collaboration time? That's context-rebuilding. Re-explaining problems across tools. Validating outputs. Re-prompting when AI gets it wrong. It's not necessarily bad work — but it's not the high-value work engineers signed up for.

So the paradox: a tool that's supposed to save mental effort actually increases cognitive load because the verification tax is higher than you budgeted for.

[TIMING: 22:45]

---

## SLIDE 21: THE VERIFICATION TAX

There's a pattern here that I want to make visual. Think about what happens every time you use AI for a coding task. The AI generates code in about two minutes. But then you need to read it line by line, compare it against requirements, check for edge cases, test it, and fix what's wrong. That verification process often takes fifteen minutes or more.

So the math doesn't work out. You saved two minutes of writing but spent fifteen minutes reviewing. That's the verification tax — and it's the hidden cost that makes AI adoption feel so frustrating. When the review overhead exceeds the generation time, you're not automating. You're just moving work from one column to another.

This is the single biggest insight from the brain fry research: the generation is fast, but the validation tax is where the time actually goes.

[TIMING: 23:30]

---

## SLIDE 22: AUDIENCE CHECK — WHICH BARRIER?

Quick check. Look around this room for a second. [PAUSE] How many people here are dealing with all five of these barriers at once? [PAUSE — count hands] Yeah, that's about what I expected.

Which of these five is costing your team the most right now?

Tool sprawl? [PAUSE] Workflow confusion? [PAUSE] Trust and correctness? [PAUSE] Cognitive overload? [PAUSE] Pressure to keep up? [PAUSE]

Cognitive overload tends to get the most recognition — BCG's survey found 14% of AI users reporting significant mental fatigue, with rates notably higher in software development and IT roles. Here's a follow-up to think about: what percent of your team's AI time is generation versus verification? If your review overhead exceeds your generation time, you're not automating — you're just moving work. The shifts we're about to cover address that directly.

[TIMING: 24:30]

---

## SLIDE 23: BARRIER 5 — PRESSURE TO KEEP UP

Last barrier. Pew Research found that 52% of US workers are more worried than hopeful about AI at work. And BCG identifies skill erosion — the fear that AI is hollowing out human capabilities — as a top workforce concern. For engineers specifically, that shows up as: fear of losing debugging skill when you stop writing code from scratch. Fear of developing shallow understanding of systems you only interact with through generated code. Fear of being judged slower than AI-heavy peers. And fear of losing the engineering judgment that comes from working through hard problems yourself.

That pressure creates rush adoption, which creates poor implementation, which creates more frustration. It's a vicious cycle.

But here's the important part: when organizations provided structured support — five or more hours of real hands-on training — that anxiety dropped substantially. The pressure isn't inherent to AI. It's created by lack of support. And that's fixable.

[TIMING: 25:00]

---

## SLIDE 24: SECTION DIVIDER — "FIVE ACHIEVABLE SHIFTS"

Okay. We've mapped the problem. Now let's talk about what to do about it. Five shifts. Not theoretical. Not "maybe someday." Things you can implement this week.

[TIMING: 25:30]

---

## SLIDE 25: FIVE SHIFTS OVERVIEW

Shift one: assign AI the right jobs. Shift two: lighter mental models. Shift three: context-first prompting. Shift four: workflow pairing. Shift five: guardrails.

Each one addresses one of the barriers we just covered. Together, they restore control and clarity to how you work WITH AI instead of around it. Let's go through them.

[TIMING: 26:00]

---

## SLIDE 26: EACH SHIFT ADDRESSES A BARRIER

[GESTURE across the five mapping rows on screen]

Let me show you the connections explicitly. Tool sprawl — that's barrier one — gets addressed by shift one, assigning AI the right jobs, and shift five, putting guardrails in place so tools don't multiply unchecked. Unclear workflows — barrier two — maps to shift one again plus shift four, workflow pairing, which builds repeatable processes. The promise-versus-reality gap — barrier three — is where shift two, lighter mental models, and shift three, context-first prompting, come in. They reset expectations and improve actual output quality. Brain fry — barrier four — needs shift two to reduce cognitive load and shift five to create safety nets. And pressure — barrier five — is primarily addressed by shift five, especially the training and organizational support component.

Notice that some shifts address multiple barriers, and some barriers need multiple shifts. That's why we need all five — they work as a system, not a checklist.

[TIMING: 26:30]

## SLIDE 27: SHIFT 1 — ASSIGN AI THE RIGHT JOBS

First shift. Not every task should be AI-assisted. The question to ask: "Is this a task where AI's strengths — pattern matching, fast generation, handling repetitive structure — actually solve a real problem?" If yes, great. If you're just using AI because it's there, you're adding overhead for no benefit.

The delegation test: think of AI as a capable junior engineer with no project context. Would you hand this task to that person? If the cost of being wrong is low and you can verify the output quickly — that's an AI task. If accuracy is critical, if deep domain knowledge is needed to evaluate the output — that's a human task, with AI as support at most.

[TIMING: 27:15]

---

## SLIDE 28: TASK MATRIX

Here's a simple matrix. One axis is cognitive load — how much thinking does this task require? The other is human judgment value — how much does quality depend on human decision-making?

Low thinking, low human touch: scaffolding. AI goes full speed. Test stubs, CI/CD configs, API route boilerplate, Dockerfiles.

High thinking, high human touch: core engineering. Architecture decisions, tradeoff analysis, security reviews. AI supports, but you drive.

The danger zone is when teams put high-touch tasks in the AI-leads bucket. That's where bugs ship and trust erodes.

[TIMING: 28:30]

---

## SLIDE 29: KNOW YOUR AI SWEET SPOTS

Let me make this specific for engineers.

Green light tasks — where AI earns its keep: scaffolding and boilerplate generation. Code explanation and documentation. Test generation when you provide proper context. Refactoring known patterns. PR summarization and codebase Q&A.

Red light tasks — where engineers should stay in the driver's seat: security reviews and auth logic. Architecture decisions. Performance tuning without knowing your specific constraints. Anything where hidden domain assumptions can cause silent failures.

Here's a quick example of what this looks like in practice. Think about PR summary descriptions — many teams have engineers spending 15 to 20 minutes per PR writing them. Move that to AI — feed it the diff plus the ticket context — and you get accurate PR summaries in seconds. Low risk, easy to verify, pure time savings. That's a green-light task.

Simple rule: if the time you spend validating AI output exceeds the time it saved generating it, you're not getting leverage — you're just adding steps.

[TIMING: 30:15]

---

## SLIDE 30: SHIFT 2 — LIGHTER MENTAL MODELS

Second shift. Think of AI as a capable junior engineer with no project context. Smart, fast, eager, sometimes wrong about important things. You wouldn't micromanage them into paralysis. But you also wouldn't hand them the keys to production.

You give them tasks. You review the output. You provide directional feedback. You send them back to fix things. And over time, as you learn where they're strong and where they're weak, the collaboration gets smoother.

Or think of it another way: we said we wanted pair programming. We just forgot to specify that our pair should understand the codebase. Once you internalize that, you stop expecting oracle-level answers and start expecting useful first drafts. And that brings the checking cost back to something reasonable.

[TIMING: 31:45]

---

## SLIDE 31: TRUST SWEET SPOT

There's a spectrum. On one end: blind trust. You accept whatever AI gives you. Dangerous. On the other end: total skepticism. You verify every single line. Exhausting.

The sweet spot is in the middle, and it moves based on the task. For boilerplate? Lean toward trust. For security code? Lean toward verification. For architecture decisions? Heavy verification.

Being intentional about where you sit on that spectrum for each task type — that's what turns AI from a source of anxiety into a source of predictable leverage.

[TIMING: 33:00]

---

## SLIDE 32: SHIFT 3 — CONTEXT-FIRST PROMPTING

Third shift, and this one will change how you use AI tomorrow. Most people prompt with a task: "Write tests for this module." And then they're surprised when the output is generic.

Flip the order. Context first, then task, then constraints. Tell AI what it needs to know about YOUR system before you tell it what to do. The formula is simple: Context plus Task plus Constraints equals notably better output.

[TIMING: 34:00]

---

## SLIDE 33: CONTEXT MAKES THE DIFFERENCE

Look at the difference on this slide. On the left: "Write unit tests for the authentication module." No context. The AI generates generic happy-path tests. Misses token expiry, role-based access, rate limiting, session invalidation. You spend 20 minutes re-prompting.

On the right: you specify JWT with Flask and pytest. You list the edge cases — expired tokens, invalid issuer, missing scopes, revoked sessions. You specify the framework and constraints. And the AI generates a comprehensive test suite that's ready with minimal edits.

Same model. Same capability. Here's a rule of thumb I keep coming back to: thirty extra seconds of context tends to save twenty minutes of re-prompting. It's not a precise measurement — it's a pattern I've seen consistently. That's the most efficient investment you'll make all day.

[TIMING: 35:45]

---

## SLIDE 34: SPOT THE MISSING CONTEXT

Let's try this. Here's a prompt: "Refactor the database query in users.py to be faster. It's running slow in production."

Take 10 seconds. What context is missing? [PAUSE — 10 seconds]

Alright, what did you come up with? [Take 2-3 audience answers]

Here's what's missing: The current query and schema structure. Which database engine. How slow — 100ms or 10 seconds? Data volume — 100 rows or 10 million? Existing indexes. Whether it's read-heavy or write-heavy.

Without that context, AI will suggest generic optimizations that may not apply to your case. With it, you get specific, actionable recommendations. Start asking "what context is missing?" before every prompt.

[TIMING: 37:45]

---

## SLIDE 35: SHIFT 4 — WORKFLOW PAIRING

Fourth shift. Stop bolting AI onto your existing process. Instead, design workflows where AI and humans take turns. AI drafts, human reviews. AI refines based on feedback, human approves. It's like pair programming, but your pair is the AI.

Here's an illustrative example of the pattern. Imagine asking AI to refactor a data access layer for performance. AI cleans up the queries beautifully — passes all unit tests. But in production, the refactored code hits the database with a new query pattern that bypasses connection pool limits and causes timeouts under load. The unit tests didn't cover production concurrency. That's a bolt-on failure: AI did the work, human skipped the integration review. When the workflow is redesigned so that AI refactors and a human explicitly checks production behavior — connection pooling, caching assumptions, query plans — the same task works reliably.

The key insight is that organizations that redesigned workflows WITH AI got ROI. Organizations that just added AI to existing workflows didn't. The difference is integration versus bolt-on.

[TIMING: 39:30]

---

## SLIDE 36: CASE STUDY — AI CODE REVIEW

Here's a composite pattern drawn from multiple engineering teams adopting AI review tools. A team starts using AI for code review. Initially it works well — AI catches formatting issues, obvious bugs, style inconsistencies. But then the team starts letting AI approve PRs on its own. Human reviewers start rubber-stamping. "AI already looked at it."

A subtle concurrency bug ships. Quality drops.

So they redesign. AI handles the routine stuff — formatting, basic structure, obvious issues. Humans focus on what humans are good at — logic, edge cases, architecture, security implications. Specifically: AI flags potential null pointer dereferences, humans evaluate whether the fix changes the API contract. AI catches missing error handling, humans decide which errors are recoverable.

Quality improves. Because now humans and AI each have clear roles. The fix wasn't removing AI. It was defining where AI leads and where humans lead.

[TIMING: 41:00]

---

## SLIDE 37: SHIFT 5 — GUARDRAILS

Fifth shift. Put structure around your AI use. Not management overhead — engineering discipline. Same idea as linting or CI gates: structure that protects quality without slowing you down.

Five guardrails. Pick your two to three tools and commit — less context rebuilding. Time-box AI work — if the correctness burden exceeds what the task would take manually, switch approaches. Build in AI-free time — deep-focus work is how you keep your core engineering skills sharp. Require human review before anything ships. And invest in training — that's what lowers the integration friction of every AI interaction going forward.

When everyone knows the rules, you stop second-guessing yourself. The mental load drops. That's how you beat brain fry.

[TIMING: 42:30]

---

## SLIDE 38: TRAINING CHANGES EVERYTHING

Remember that finding about skill erosion anxiety dropping when organizations provided support? The key number is five hours. Five hours of structured, hands-on training with your actual tools and workflows. Not a webinar. Not a Slack link to documentation. Actual practice time.

Teams that get this training stop being afraid. They become confident. They know where the tool fits. They know when to trust it and when to slow down. They know how to prompt for results they can actually use. Confidence improves when the hidden checking cost drops — and training is what drops it.

[TIMING: 43:45]

---

## SLIDE 39: WHEN AI ACTUALLY SHINES

I don't want to leave you thinking AI is the problem. AI is extraordinary when you use it right. Let me give you three places where it genuinely transforms engineering work.

Boilerplate and scaffolding. Config files, API route stubs, Dockerfiles, CI/CD YAML. The stuff you've written a hundred times. Let AI handle it. You're 80% done in minutes.

Code explanation and docs. Understanding unfamiliar codebases, generating docstrings, writing README sections, summarizing PR changes. A new engineer joins a team with a legacy Java service — ten thousand lines, minimal docs. They feed the core classes to AI with context and get a structured walkthrough in 30 minutes instead of two weeks of reading. That's AI earning its keep.

Test generation with context. When you give AI the function signature, the edge cases, and the framework — it generates solid test foundations you can build on.

The key is intentionality. You know what job you're assigning AI, and it's a job AI is actually good at.

[TIMING: 45:30]

---

## SLIDE 40: VIBE CODING — THE FUN AND THE RISK

Now, some of you have been thinking — "What about vibe coding? That's the part I actually enjoy." And you're right. Andrej Karpathy coined the term in early 2025: "Fully give in to the vibes, embrace exponentials, and forget that the code even exists." It was Collins Dictionary's Word of the Year. It's become how a lot of developers describe their best AI experience.

And I get it. The flow state is real. When AI is generating code as fast as you can describe what you want, and it's working, and you're shipping features in hours instead of days — that feels amazing. Developers report three to five times productivity gains on scaffolding and prototyping tasks. That's enjoyment. That's what we're after.

But here's the flip side. Security researchers found that 45% of AI-generated code contains vulnerabilities. Fast.ai coined the term "dark flow" — that feeling of productive momentum where you don't realize until weeks later that the code is unmaintainable. And analysis of vibe-coded projects showed significantly higher rates of logic errors, misconfigurations, and security holes.

So vibe coding without guardrails is Barrier 3 at scale — the "almost right" problem, turbocharged. But vibe coding WITH the five shifts? That's the sweet spot. Assign AI the right tasks — scaffolding and prototyping are green-light territory. Use context-first prompting even when you're in the zone. Keep a human review checkpoint before anything ships to production. And time-box the vibe sessions so dark flow doesn't eat your whole sprint.

The goal isn't to kill the vibe. It's to keep the vibe AND keep the quality. That's what the five shifts enable.

[TIMING: 47:30]

---

## SLIDE 41: LEAD THE SHIFT — AUGMENTATION, NOT AUTOMATION

If you have any leadership influence — whether you're a tech lead, a manager, or an architect — here's the mindset shift that matters most. Stop thinking about automation. Start thinking about augmentation. The goal isn't "replace the human." The goal is "make the human better."

Don't mandate AI adoption without support. That's where brain fry comes from. A tool you dread using is a tool you'll use badly.

Instead: invest in real training. Pick fewer tools and go deep. Explain where AI fits in specific workflows — not at the department level, but at the task level. Tell your team what to use it for and what to keep human. Build a shared understanding.

That's not just better for productivity. It's better for your team. Engineers who feel supported adopt AI with confidence. Engineers who feel pressured adopt AI with resentment.

[TIMING: 47:15]

---
## SLIDE 42: YOUR SANE ADOPTION PLAYBOOK

Here's your playbook for this week. Five things, one per day.

Monday: audit your AI tools. List every one your team is using. If it's more than three, pick the best three and commit to them.

Tuesday: pick one workflow to redesign. Not five. One. Where does AI create the most friction right now? That's your target.

Wednesday: define your red zones. Where does AI NOT go? Security decisions? Architecture? Edge cases? Write it down. Make it explicit.

Thursday: require a human review checkpoint. Before anything AI-generated ships — code, docs, analysis — one person reads it fully. No exceptions.

Friday: schedule five hours of hands-on training. Put it on the calendar. This week or next. Use your actual tools on your actual work.

[TIMING: 48:45]

---

## SLIDE 43: USING AI AND ENJOYING IT

Let me bring this home.

We started with a gap: widespread adoption, but confidence dropping. We mapped five barriers causing that gap. And we walked through five shifts that close it. Assign AI the right jobs. Adopt lighter mental models. Prompt with context first. Pair your workflows. Put guardrails in place.

Remember that three-column workflow diagram? The goal is to move your team from the middle column — the bolted-on frustration zone — to the right column — where humans and AI each have clear roles.

Remember the opening? "Saved 15 minutes, lost 30." The five shifts are how you flip that ratio. Not by using less AI — by using it with clear task boundaries and a reasonable verification budget.

Here's your challenge: where is AI genuinely reducing effort on your team, and where is it just creating review work in a new interface? Pick one workflow where it's the latter. Redesign it using the five shifts. See what changes.

The goal isn't more AI. The goal is less friction. AI becomes useful when task boundaries are clear and the correctness burden drops.

One week. One workflow. That's how you start.

[TIMING: 50:00]

---

## SLIDE 44: QUESTIONS

I'd love to hear what's on your mind. What resonated? What didn't? What's the biggest challenge you're facing with AI on your team right now?

[Q&A: ~10 minutes]

---


## SLIDE 45: CLOSING SLIDE

Thank you so much. If you want to stay in touch, my contact info is on the slide. I'd love to hear how the playbook works for your team.

The goal isn't more AI. The goal is less friction. Take that with you.

Thank you. Enjoy the rest of the conference.

[TIMING: 50:00 + Q&A = ~60:00]

---

## TIMING CHECKPOINTS

| Section | Slides | Cumulative Time |
|---------|--------|----------------|
| Opening & framing | 1-5 | 7:15 |
| Illustrative scenario | 6-7 | 7:45 |
| Barriers intro | 8-9 | 8:30 |
| Barrier 1: Tool sprawl | 10-12 | 12:45 |
| Barrier 2: Workflow fit | 13-14 | 16:30 |
| Barrier 3: Promise vs reality | 15-17 | 19:45 |
| Barrier 4: Brain fry | 18-21 | 23:30 |
| Midpoint interaction | 22 | 24:30 |
| Barrier 5: Pressure | 23 | 25:00 |
| Shifts intro | 24-26 | 26:30 |
| Shift 1: Right jobs | 27-29 | 30:15 |
| Shift 2: Mental models | 30-31 | 33:00 |
| Shift 3: Context-first | 32-34 | 37:45 |
| Shift 4: Workflow pairing | 35-36 | 41:00 |
| Shift 5: Guardrails + training | 37-38 | 43:45 |
| When AI shines + vibe coding | 39-40 | 47:30 |
| Leadership + playbook | 41-42 | 49:30 |
| Close + challenge | 43 | 50:45 |
| Q&A | 44 | ~59:00 |
| Ending | 45 | ~60:00 |

---

## WORD COUNT: ~7,600 spoken words | ~51 min content + ~9 min Q&A = 60 min

NOTE ON TIMING: At a natural speaking pace with audience pauses, show-of-hands moments, and laughter, expect content delivery closer to 54-56 minutes before Q&A. Budget 4-6 minutes for Q&A rather than 10 if the talk runs long in rehearsal. The vibe coding section is self-contained — if you're running hot in rehearsal, it's the easiest section to tighten or cut.
