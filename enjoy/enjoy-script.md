## SLIDE 1: VERSION
[Skip]

---


## SLIDE 2: TITLE
[Skip]

---


Good morning, everyone. Before we dig in to our topic in depth, let's take a quick trip down memory lane. Remember when AI's biggest problems were actually... entertaining?

[ADVANCE to bloopers]

---


## SLIDE 3: AI BLOOPERS -- "REMEMBER WHEN AI WAS JUST... FUNNY?"

These are all real. Actually served to real users by Google's AI Overviews. Cook your spaghetti in gasoline. Eat at least one small rock per day -- for your health, of course. And my personal favorite -- add a little non-toxic glue to your pizza sauce for better cheese adhesion.

[PAUSE for laughter]

---

## SLIDE 4: AI BLOOPERS -- "THOSE WERE THE FUN FAILURES"

And it gets better. Need to figure out if your neighbor is an alien? AI's got you covered. And apparently, doctors recommend two to three cigarettes per day during pregnancy.

[PAUSE for laughter]

Those were the fun failures. They went viral, we all laughed, Google was embarrassed. But here's the thing -- those failures are obvious. You KNOW not to eat rocks. You KNOW not to cook with gasoline. The problem we're going to talk about today is that the failures aren't funny anymore. They're subtle. And subtle wrong is much more dangerous than obviously wrong.

Quick show of hands. How many of you saved 15 minutes this week using AI? [PAUSE for hands] Good number. Now how many of you had it cost you 30?

[PAUSE] Yeah. That's the talk.

I'm Brent Laster. I've been working in technology for decades. I've seen a lot of technology shifts. But I've never seen one that created this much frustration alongside this much promise. I'd venture to say we're all using AI. Every single one of us. And yet when engineers, team leads, and architects are surveyed about how it's going in production, the honest answer is usually some version of: "It's helpful for some use cases, but we're not actually sure we're doing it right or that it's actually helping overall." That sentiment shows up consistently in research from Stack Overflow, BCG, and Pew.

That's what we're going to dig into today. We'll look at five specific barriers that are making AI feel harder than it should. Then we'll walk through five achievable shifts -- things you can implement this week -- that change the experience. And we'll close with a playbook you can take back to your team on Monday.

[TIMING: 3:30]

---


## SLIDE 5: ABOUT ME

[Brief personal introduction - use content on slide]

---


## SLIDE 6: A SHOW OF HANDS

Let's start with the numbers. Across recent workforce studies, a clear pattern is emerging. About 52% of workers are actively using AI tools -- that's from Qualtrics. But here's the catch -- a separate study from ManpowerGroup found that worker confidence in using technology at work fell sharply -- by 18% -- over roughly the same period, even as AI use rose. Two different studies, same story: adoption going up, confidence going down.

Now, these are broad workforce numbers -- not engineering-specific. But the same pattern shows up very clearly in developer workflows, and I'll show you the engineering data in a moment. The point is: this isn't one team's problem. It's structural.

[TIMING: 3:30]

---

## SLIDE 7: AI PRODUCTIVITY PARADOX

Now let's talk about some uncomfortable business numbers. MIT's 2025 "State of AI in Business" report found that 95% of generative AI pilots failed to deliver measurable business impact. Let that land. Ninety-five percent. The vast majority of organizations are still trying to figure out how to make this work beyond pilots and proofs of concept.

And among developers specifically, Stack Overflow's 2025 survey tells a stark story: only about one in three developers say they trust AI output accuracy. And 46% actively distrust it. More developers distrust AI-generated code than trust it. That's not a rounding error -- that's a fundamental confidence problem.

Meanwhile, Pew Research found that 52% of workers are more worried than hopeful about AI in their workplace. And ActivTrak's analysis of over 443 million hours of work activity found that average focus session length dropped 9% -- down to just 13 minutes -- while collaboration time surged 34% after AI adoption. The tools multiply, but the deep-focus time shrinks.

We're using it more. We're enjoying it less. Let's figure out why.

[TIMING: 5:00]

---

## SLIDE 8: THE TEST THAT PASSED

Let me walk you through a scenario that plays out constantly across engineering teams -- it's a well-documented pattern, not a single incident.

A team asks their AI assistant to write a unit test for an authentication module. The AI generates a beautiful test. Correct syntax, proper assertions, good structure. It passes on the first run. Team ships it.

Three days later, during a security review, they discover the test never actually validated the token expiry path. Here's the key part -- the test checked that a valid token returns 200 OK. But it never tested that an expired token returns 401. It never tested that a token from the wrong issuer gets rejected. It never tested that a revoked session token is caught.

The AI tested the happy path perfectly and skipped the parts that mattered for this team's security posture. The code looked right. It compiled. It passed. But it wasn't testing what it claimed to test.

You can see the visual shorthand on the slide -- green checkmark for "passed," red X for "failed badly." That gap -- between looking correct and being correct -- is exactly what makes AI so frustrating for engineers. The failure mode isn't "obviously broken code." The failure mode is "subtly incomplete code that passes every automated check."

[TIMING: 7:15]

---

## SLIDE 9: THE TEST DETAILS

Here's the breakdown of what the AI test actually covered and what it missed.

The test checked three things: token validation returns 200 for valid input, endpoint exists, HTTP structure is correct. Standard happy-path tests.

It never touched the edge cases: expired tokens, wrong issuer, revoked sessions. These weren't in the test at all. The AI's test suite was technically correct for what it tested -- but incomplete for the team's actual threat model.

This is why "the code compiles" and "the code passes" aren't the same as "the code is correct for this team." Correctness is application-specific.

[TIMING: 7:45]

---
## SLIDE 10: SECTION DIVIDER -- "WHY DOES AI FEEL SO HARD?"

So why is this happening? Why does a tool that's supposed to make our lives easier feel like it's making things harder? After digging into the research -- surveys from Stack Overflow, BCG, Pew, and others -- plus community discussions across engineering forums, five specific barriers keep surfacing. Not philosophical barriers. Concrete, fixable problems. Let's walk through them.

[TIMING: 7:45]

---

## SLIDE 11: FIVE BARRIERS OVERVIEW

Here are the five:

Too many tools, not enough glue. Nobody told us where AI fits. Promise versus reality. AI brain fry. And pressure to keep up.

Each one feeds the others. Tool sprawl creates confusion about where AI fits, which creates unrealistic expectations, which creates cognitive overload, which creates pressure. It's a cycle. But the good news is that each one is individually addressable. Break one, and the others get easier.

[TIMING: 8:30]

---

## SLIDE 12: BARRIER 1 -- TOO MANY TOOLS, NOT ENOUGH GLUE

First barrier. Survey data tells us developers are juggling more AI tools than ever -- ActivTrak's 2026 report found the average organization now uses seven AI tools, up from two just two years ago, with 83% of organizations using six or more. IDE copilot, chat interfaces, code search, review assistants, doc generators. Each one is independently useful. But none of them share context with each other.

Now -- there ARE efforts to fix this. Anthropic's Model Context Protocol -- MCP -- has gained real traction, with 97 million monthly SDK downloads and adoption by OpenAI, Google, Microsoft, and AWS. Teams are writing structured context files like CLAUDE.md and .cursorrules. But here's the honest status: MCP connects tools to data sources, not tools to each other. Your Cursor session still can't hand context to your Claude Code session. Context engineering is becoming a discipline, but the integration gap is still very real.

So YOU become the integration layer. You re-explain the same problem four times to four different systems. AI didn't remove work. It just promoted all of us to unpaid reviewers. That human middleware cost is eating the productivity gains the tools are supposed to provide. The result? Widespread "shadow AI" use when the official tools are weak or slow.

[TIMING: 9:45]

---

## SLIDE 13: THREE-TOOL THRESHOLD

Here's a finding from BCG's 2026 brain fry research that stuck with me: when they looked at AI tool usage patterns, productivity gains rose from one to two tools, peaked at three, and actually dropped past four. At the same time, cognitive strain kept climbing.

It's not a universal law, but it holds up well as a planning heuristic. Think of it like this: if you have one database, you understand your data. Three databases, you're managing replication. Five, you're debugging consistency issues. Same principle applies to AI tools. Past a certain point, the cost of managing the tools exceeds the benefit of having them.

My recommendation: pick your best two to three tools. Go deep. Learn their strengths. Build muscle memory. Let the rest go.

[TIMING: 11:15]

---

## SLIDE 14: ENGINEER'S AI TOOLBOX

Let me make this concrete. Look at a typical engineer's AI stack. You've got an IDE Copilot for inline suggestions. A chat interface for broader questions. A code search tool for codebase Q&A. A review assistant for PR analysis. A ticket summarizer.

Now look at the overlap. Three of those five generate code. Two of them summarize context. And none of them share state. So when you switch from your chat interface to your IDE copilot, you lose all the context from that conversation. You're starting cold every single time.

You're sitting there thinking, "AI is supposed to save me time." But you're spending half that saved time re-establishing context across tools. You are the integration layer, and that is exhausting.

[TIMING: 12:45]

---

## SLIDE 15: BARRIER 2 -- NOBODY TOLD US WHERE AI FITS

Second barrier. Most organizations adopted AI by bolting it onto existing workflows. They didn't redesign anything. They just said, "Here's a new tool. Figure out where it goes." And so developers are making ad hoc decisions -- sometimes using AI, sometimes not -- with no shared understanding of where it adds value and where it doesn't.

In engineering, the problem isn't just "where can AI help?" It's "who now owns correctness, edge cases, and final judgment at each step?" When nobody defines that, AI-generated work creates hidden review debt -- more code to verify, more tests to validate, more assumptions to check -- and no one is explicitly responsible for catching what AI missed.

BCG found that organizations that communicated clearly about where AI fits in specific workflows saw notably better adoption and satisfaction. It's not mysterious. If people don't know where a tool belongs, they either avoid it or misuse it.

[TIMING: 14:30]

---

## SLIDE 16: ENGINEERING WORKFLOW -- THREE REALITIES

Let me show you what this looks like in practice. Three columns -- remember this one, because we'll come back to it.

On the left: traditional workflow. Read the ticket, design, code, test, PR, deploy. Slow but clear.

In the middle: bolted-on AI. Same steps, but AI jammed in at random points. You verify everything manually, re-prompt three times, and the review overhead kills you. This is where most teams are right now.

On the right: human-plus-AI. Context fed upfront. Clear roles -- you lead design, AI drafts, you review and add edge cases. Clear handoffs, and you submit the PR with confidence.

The middle column is the frustration zone. The right column is what we're aiming for.

[TIMING: 16:30]

---

## SLIDE 17: BARRIER 3 -- PROMISE VS. REALITY

Third barrier. AI is almost right a lot of the time. And "almost right" is the most dangerous kind of wrong. If it were obviously broken, you'd catch it. If it were always correct, you could trust it. But "almost right" means you have to verify everything, and the review feels pointless because the output usually looks fine.

Here's how Stack Overflow's 2025 survey put it: 66% of developers said their biggest frustration is "AI solutions that are almost right but not quite." Two-thirds. That was the top response -- and 45% said debugging AI-generated code is more time-consuming than writing it themselves. It tracks with the broader research -- MIT's 2025 study found that 95% of AI pilots failed to deliver measurable business impact, largely because organizations couldn't get past the verification and scaling challenges.

Many organizations still struggle to demonstrate repeatable, measurable ROI from AI beyond pilots -- and a big part of that is the hidden verification cost. The teams that push through it and build good review discipline recover. The ones that don't either give up or ship bugs.

[TIMING: 18:15]

---

## SLIDE 18: WHEN AI CODE LOOKS RIGHT BUT ISN'T

Here's an illustrative example of what "almost right" looks like in code. This slide shows a JWT token validation function. Syntactically perfect. Well-structured. It validates the token signature. It would pass generic unit tests.

But look at what's missing from the team's specific requirements. No expiry check on their timeline. No issuer validation. No audience scope verification. No token revocation check. The AI wrote correct generic code -- but it omitted the application-specific checks that actually matter for this team's security posture.

It's like hiring a contractor to build a beautiful kitchen -- granite countertops, perfect tile work -- and then realizing they never connected the plumbing. Everything looks right until you turn on the faucet. That's the "almost right" problem.

[TIMING: 19:15]

---
## SLIDE 19: PR SUMMARY -- LOOKS RIGHT BUT ISN'T

Here's a composite example drawn from a pattern that shows up consistently in engineering teams adopting AI review tools.

A team starts using AI for PR summaries. The AI tool reads the diff and generates: 'Refactored retry mechanism for improved clarity.' Looks perfect. Well-written summary. The reviewer sees that, approves the PR, ships it.

But what actually changed: the retry logic for payment processing. The conditions shifted. The backoff delays changed. The failure recovery path changed. The summary described these as 'minor cleanup.' The reviewer approved without reading the diff closely because the summary made it sound safe.

That's not a code bug. That's a process failure created by incomplete AI output that passed the '80% credibility threshold.' The summary WAS mostly right -- it just omitted the part that mattered most.

[TIMING: 19:45]

---

## SLIDE 20: BARRIER 4 -- AI BRAIN FRY

Fourth barrier, and this is the one that hits hardest. AI brain fry. For engineers, it's the constant loop of prompting, validating output line by line, re-prompting when it's wrong, and context-switching between tools -- all while keeping your own mental model intact. A March 2026 study by BCG and Harvard Business Review surveyed nearly 1,500 workers and coined the term "AI brain fry" -- mental fatigue from excessive AI oversight. They found meaningful increases among heavy AI users: 14% more mental effort, 12% more mental fatigue, 19% more information overload, and 33% more decision fatigue. Fourteen percent of knowledge workers reported significant cognitive strain, with software development flagged as one of the highest-prevalence roles. For engineering, that pattern is likely intensified by the verification load we've been talking about.

And here's the irony: AI was supposed to lighten workloads. But ActivTrak's analysis of 443 million hours of work data found that average focus session length dropped 9% -- down to just 13 minutes -- while collaboration time surged 34% after AI adoption. The workload didn't shift -- it stacked. For engineers, that means more diff review fatigue, more re-prompt cycles, more context reconstruction between tools, and less uninterrupted time for the deep thinking that produces good architecture. You're debugging AI's understanding of your codebase instead of debugging the codebase itself.

[TIMING: 21:15]

---

## SLIDE 21: DEVELOPER BRAIN FRY CYCLE

For engineers specifically, the cycle looks like this. Step one: write a detailed prompt. Step two: inspect the output line by line. Step three: compare against your requirements. Step four: patch what AI got wrong. Step five: re-run and test. Step six: re-validate -- did the patch break something else? Step seven: context-switch to the next task.

And this isn't once a day. This cycle happens ten, fifteen, twenty times a day. Every single AI interaction. The generation is fast, sure. But the validation tax -- the cognitive cost of verifying every single output -- that's where the time goes. And that's what's burning people out.

[TIMING: 22:15]

---
## SLIDE 22: WHERE THE TIME ACTUALLY GOES

Here's the data behind brain fry. ActivTrak's large-scale tracking tells the story: collaboration time surged 34%, while average focus session length dropped 9% -- down to just 13 minutes each.

That sounds like small numbers. But for an engineer, even 9% of focused time is 3-4 hours per week. That's your deep-thinking time. Your architecture time. Your 'understand the system better' time.

And the added collaboration time? That's context-rebuilding. Re-explaining problems across tools. Validating outputs. Re-prompting when AI gets it wrong. It's not necessarily bad work -- but it's not the high-value work engineers signed up for.

So the paradox: a tool that's supposed to save mental effort actually increases cognitive load because the verification tax is higher than you budgeted for.

[TIMING: 22:45]

---

## SLIDE 23: THE VERIFICATION TAX

There's a pattern here that I want to make visual. Think about what happens every time you use AI for a coding task. The AI generates code in about two minutes. But then you need to read it line by line, compare it against requirements, check for edge cases, test it, and fix what's wrong. That verification process often takes fifteen minutes or more.

So the math doesn't work out. You saved two minutes of writing but spent fifteen minutes reviewing. That's the verification tax -- and it's the hidden cost that makes AI adoption feel so frustrating. When the review overhead exceeds the generation time, you're not automating. You're just moving work from one column to another.

This is the single biggest insight from the brain fry research: the generation is fast, but the validation tax is where the time actually goes.

[TIMING: 23:30]

---

## SLIDE 24: BARRIER 5 -- PRESSURE TO KEEP UP

Last barrier. Pew Research found that 52% of US workers are more worried than hopeful about AI at work. And BCG identifies skill erosion -- the fear that AI is hollowing out human capabilities -- as a top workforce concern. For engineers specifically, that shows up as: fear of losing debugging skill when you stop writing code from scratch. Fear of developing shallow understanding of systems you only interact with through generated code. Fear of being judged slower than AI-heavy peers. And fear of losing the engineering judgment that comes from working through hard problems yourself.

That pressure creates rush adoption, which creates poor implementation, which creates more frustration. It's a vicious cycle.

But here's the important part: when organizations provided structured support -- five or more hours of real hands-on training -- that anxiety dropped substantially. The pressure isn't inherent to AI. It's created by lack of support. And that's fixable.

[TIMING: 25:00]

---

## SLIDE 25: AUDIENCE CHECK -- WHICH BARRIER?

Now before we move on to solutions, let's take the temperature of the room. Quick check. Look around for a second. [PAUSE] How many people here are dealing with all five of these barriers at once? [PAUSE -- count hands] Yeah, that's about what I expected.

And how many of you are being measured on AI usage as a job metric? [PAUSE] Right. We'll talk about that in a moment.

Which of these is costing your team the most right now?

Tool sprawl? [PAUSE] Workflow confusion? [PAUSE] Trust and correctness? [PAUSE] Cognitive overload? [PAUSE] Pressure to keep up? [PAUSE]

Cognitive overload tends to get the most recognition -- BCG's survey found 14% of AI users reporting significant mental fatigue, with rates notably higher in software development and IT roles. Here's a follow-up to think about: what percent of your team's AI time is generation versus verification? If your review overhead exceeds your generation time, you're not automating -- you're just moving work. The shifts we're about to cover address that directly.

But first -- a couple of you raised hands about being measured on AI usage. Let's talk about what happens when AI becomes the metric.

[TIMING: 26:00]

---

## SLIDE 26: WHEN AI USAGE BECOMES THE METRIC

And here's what makes that pressure even worse. Organizations are now tracking AI adoption as a performance metric. Microsoft's Work Trend Index found 75% of knowledge workers using AI regularly -- and management noticed. Some companies are mandating AI usage as a KPI without clear guidance on WHAT to use it for or HOW to measure whether it's helping.

The risk is Goodhart's Law in action: "When the metric becomes the target, it ceases to be a good metric." If you're being judged on how much you use AI rather than on outcomes, you'll optimize for token consumption instead of code quality. And that's exactly what we're seeing in some organizations.

The solution isn't to stop tracking adoption. It's to define clear outcome metrics -- code quality, time to resolution, developer satisfaction -- alongside adoption metrics. Usage without outcomes is just activity.

[TIMING: 26:45]

---

## SLIDE 27: TOKENS ARE THE NEW LINES OF CODE

Let me make this concrete with numbers. Agentic tools like Claude Code can cost $200 to $2,000+ per engineer per month in token spend. Industry benchmarks show 41% of all code is now AI-generated. And here's the productivity paradox that METR's research captured: developers self-report feeling 20% faster, but when measured objectively, they're actually about 19% slower -- because of longer review cycles and higher bug rates.

Sound familiar? We've been here before. In the 1990s and 2000s, organizations tried to measure developer productivity by counting lines of code. That metric was famously terrible -- it incentivized verbose code, copy-paste, and bloat. Counting tokens spent on AI is the same mistake in a new costume. Neither measures outcomes. Neither tells you whether the work is good.

What does make sense as a metric? Code quality over time. Time to resolution. Developer confidence surveys. Reduction in production incidents. Those measure whether AI is actually helping -- not just whether it's being used.

[TIMING: 27:30]

---

## SLIDE 28: SECTION DIVIDER -- "FIVE ACHIEVABLE SHIFTS"

Okay. We've mapped the problem. Now let's talk about what to do about it. Five shifts. Not theoretical. Not "maybe someday." Things you can implement this week.

[TIMING: 28:00]

---

## SLIDE 29: FIVE SHIFTS OVERVIEW

Shift one: assign AI the right jobs. Shift two: lighter mental models. Shift three: context-first prompting. Shift four: workflow pairing. Shift five: guardrails.

Each one addresses one of the barriers we just covered. Together, they restore control and clarity to how you work WITH AI instead of around it. Let's go through them.

[TIMING: 28:30]

---

## SLIDE 30: EACH SHIFT ADDRESSES A BARRIER

[GESTURE across the five mapping rows on screen]

Let me show you the connections explicitly. Tool sprawl -- that's barrier one -- gets addressed by shift one, assigning AI the right jobs, and shift five, putting guardrails in place so tools don't multiply unchecked. Unclear workflows -- barrier two -- maps to shift one again plus shift four, workflow pairing, which builds repeatable processes. The promise-versus-reality gap -- barrier three -- is where shift two, lighter mental models, and shift three, context-first prompting, come in. They reset expectations and improve actual output quality. Brain fry -- barrier four -- needs shift two to reduce cognitive load and shift five to create safety nets. And pressure -- barrier five -- is primarily addressed by shift five, especially the training and organizational support component.

Notice that some shifts address multiple barriers, and some barriers need multiple shifts. That's why we need all five -- they work as a system, not a checklist.

[TIMING: 29:00]

## SLIDE 31: SHIFT 1 -- ASSIGN AI THE RIGHT JOBS

First shift. Not every task should be AI-assisted. The question to ask: "Is this a task where AI's strengths -- pattern matching, fast generation, handling repetitive structure -- actually solve a real problem?" If yes, great. If you're just using AI because it's there, you're adding overhead for no benefit.

The delegation test: think of AI as a capable junior engineer with no project context. Would you hand this task to that person? If the cost of being wrong is low and you can verify the output quickly -- that's an AI task. If accuracy is critical, if deep domain knowledge is needed to evaluate the output -- that's a human task, with AI as support at most.

[TIMING: 29:45]

---

## SLIDE 32: TASK MATRIX

Here's a simple matrix. One axis is cognitive load -- how much thinking does this task require? The other is human judgment value -- how much does quality depend on human decision-making?

Low thinking, low human touch: scaffolding. AI goes full speed. Test stubs, CI/CD configs, API route boilerplate, Dockerfiles.

High thinking, high human touch: core engineering. Architecture decisions, tradeoff analysis, security reviews. AI supports, but you drive.

The danger zone is when teams put high-touch tasks in the AI-leads bucket. That's where bugs ship and trust erodes.

[TIMING: 31:00]

---

## SLIDE 33: KNOW YOUR AI SWEET SPOTS

Let me make this specific for engineers.

Green light tasks -- where AI earns its keep: scaffolding and boilerplate generation. Code explanation and documentation. Test generation when you provide proper context. Refactoring known patterns. PR summarization and codebase Q&A.

Red light tasks -- where engineers should stay in the driver's seat: security reviews and auth logic. Architecture decisions. Performance tuning without knowing your specific constraints. Anything where hidden domain assumptions can cause silent failures.

Here's a quick example of what this looks like in practice. Think about PR summary descriptions -- many teams have engineers spending 15 to 20 minutes per PR writing them. Move that to AI -- feed it the diff plus the ticket context -- and you get accurate PR summaries in seconds. Low risk, easy to verify, pure time savings. That's a green-light task.

Simple rule: if the time you spend validating AI output exceeds the time it saved generating it, you're not getting leverage -- you're just adding steps.

[TIMING: 32:45]

---

## SLIDE 34: SHIFT 2 -- LIGHTER MENTAL MODELS

Second shift. Think of AI as a capable junior engineer with no project context. Smart, fast, eager, sometimes wrong about important things. You wouldn't micromanage them into paralysis. But you also wouldn't hand them the keys to production.

You give them tasks. You review the output. You provide directional feedback. You send them back to fix things. And over time, as you learn where they're strong and where they're weak, the collaboration gets smoother.

Or think of it another way: we said we wanted pair programming. We just forgot to specify that our pair should understand the codebase. Once you internalize that, you stop expecting oracle-level answers and start expecting useful first drafts. And that brings the checking cost back to something reasonable.

[TIMING: 34:15]

---

## SLIDE 35: TRUST SWEET SPOT

There's a spectrum. On one end: blind trust. You accept whatever AI gives you. Dangerous. On the other end: total skepticism. You verify every single line. Exhausting.

The sweet spot is in the middle, and it moves based on the task. For boilerplate? Lean toward trust. For security code? Lean toward verification. For architecture decisions? Heavy verification.

Being intentional about where you sit on that spectrum for each task type -- that's what turns AI from a source of anxiety into a source of predictable leverage.

[TIMING: 35:30]

---

## SLIDE 36: SHIFT 3 -- CONTEXT-FIRST PROMPTING

Third shift, and this one will change how you use AI tomorrow. Most people prompt with a task: "Write tests for this module." And then they're surprised when the output is generic.

Flip the order. Context first, then task, then constraints. Tell AI what it needs to know about YOUR system before you tell it what to do. The formula is simple: Context plus Task plus Constraints equals notably better output.

[TIMING: 36:30]

---

## SLIDE 37: CONTEXT MAKES THE DIFFERENCE

Look at the difference on this slide. On the left: "Write unit tests for the authentication module." No context. The AI generates generic happy-path tests. Misses token expiry, role-based access, rate limiting, session invalidation. You spend 20 minutes re-prompting.

On the right: you specify JWT with Flask and pytest. You list the edge cases -- expired tokens, invalid issuer, missing scopes, revoked sessions. You specify the framework and constraints. And the AI generates a comprehensive test suite that's ready with minimal edits.

Same model. Same capability. Here's a rule of thumb I keep coming back to: thirty extra seconds of context tends to save twenty minutes of re-prompting. It's not a precise measurement -- it's a pattern I've seen consistently. That's the most efficient investment you'll make all day.

[TIMING: 38:15]

---

## SLIDE 38: SPOT THE MISSING CONTEXT

Let's try this. Here's a prompt: "Refactor the database query in users.py to be faster. It's running slow in production."

Take 10 seconds. What context is missing? [PAUSE -- 10 seconds]

Alright, what did you come up with? [Take 2-3 audience answers]

Here's what's missing: The current query and schema structure. Which database engine. How slow -- 100ms or 10 seconds? Data volume -- 100 rows or 10 million? Existing indexes. Whether it's read-heavy or write-heavy.

Without that context, AI will suggest generic optimizations that may not apply to your case. With it, you get specific, actionable recommendations. Start asking "what context is missing?" before every prompt.

[TIMING: 40:15]

---

## SLIDE 39: SHIFT 4 -- WORKFLOW PAIRING

Fourth shift. Stop bolting AI onto your existing process. Instead, design workflows where AI and humans take turns. AI drafts, human reviews. AI refines based on feedback, human approves. It's like pair programming, but your pair is the AI.

Here's an illustrative example of the pattern. Imagine asking AI to refactor a data access layer for performance. AI cleans up the queries beautifully -- passes all unit tests. But in production, the refactored code hits the database with a new query pattern that bypasses connection pool limits and causes timeouts under load. The unit tests didn't cover production concurrency. That's a bolt-on failure: AI did the work, human skipped the integration review. When the workflow is redesigned so that AI refactors and a human explicitly checks production behavior -- connection pooling, caching assumptions, query plans -- the same task works reliably.

The key insight is that organizations that redesigned workflows WITH AI got ROI. Organizations that just added AI to existing workflows didn't. The difference is integration versus bolt-on.

[TIMING: 41:30]

---

## SLIDE 40: CASE STUDY -- AI CODE REVIEW

Here's a composite pattern drawn from multiple engineering teams adopting AI review tools. A team starts using AI for code review. Initially it works well -- AI catches formatting issues, obvious bugs, style inconsistencies. But then the team starts letting AI approve PRs on its own. Human reviewers start rubber-stamping. "AI already looked at it."

A subtle concurrency bug ships. Quality drops.

So they redesign. AI handles the routine stuff -- formatting, basic structure, obvious issues. Humans focus on what humans are good at -- logic, edge cases, architecture, security implications. Specifically: AI flags potential null pointer dereferences, humans evaluate whether the fix changes the API contract. AI catches missing error handling, humans decide which errors are recoverable.

Quality improves. Because now humans and AI each have clear roles. The fix wasn't removing AI. It was defining where AI leads and where humans lead.

[TIMING: 43:00]

---

## SLIDE 41: SHIFT 5 -- GUARDRAILS

Fifth shift. Put structure around your AI use. Not management overhead -- engineering discipline. Same idea as linting or CI gates: structure that protects quality without slowing you down.

Five guardrails. Pick your two to three tools and commit -- less context rebuilding. Time-box AI work -- if the correctness burden exceeds what the task would take manually, switch approaches. Build in AI-free time -- deep-focus work is how you keep your core engineering skills sharp. Require human review before anything ships. And invest in training -- that's what lowers the integration friction of every AI interaction going forward.

When everyone knows the rules, you stop second-guessing yourself. The mental load drops. That's how you beat brain fry.

[TIMING: 44:30]

---

## SLIDE 42: TRAINING CHANGES EVERYTHING

Remember that finding about skill erosion anxiety dropping when organizations provided support? The key number is five hours. Five hours of structured, hands-on training with your actual tools and workflows. Not a webinar. Not a Slack link to documentation. Actual practice time.

Teams that get this training stop being afraid. They become confident. They know where the tool fits. They know when to trust it and when to slow down. They know how to prompt for results they can actually use. Confidence improves when the hidden checking cost drops -- and training is what drops it.

[TIMING: 45:45]

---

## SLIDE 43: WHEN AI ACTUALLY SHINES

I don't want to leave you thinking AI is the problem. AI is extraordinary when you use it right. Let me give you three places where it genuinely transforms engineering work.

Boilerplate and scaffolding. Config files, API route stubs, Dockerfiles, CI/CD YAML. The stuff you've written a hundred times. Let AI handle it. You're 80% done in minutes.

Code explanation and docs. Understanding unfamiliar codebases, generating docstrings, writing README sections, summarizing PR changes. A new engineer joins a team with a legacy Java service -- ten thousand lines, minimal docs. They feed the core classes to AI with context and get a structured walkthrough in 30 minutes instead of two weeks of reading. That's AI earning its keep.

Test generation with context. When you give AI the function signature, the edge cases, and the framework -- it generates solid test foundations you can build on.

The key is intentionality. You know what job you're assigning AI, and it's a job AI is actually good at.

[TIMING: 47:30]

---

## SLIDE 44: FROM PROGRAMMER TO AGENT MANAGER

And here's another way to start enjoying AI: learn to manage it. Harvard Business Review wrote in February 2026 that companies need "agent managers" -- a new role, just as product managers emerged during the software revolution. The developer role is evolving from writing every line of code to orchestrating AI agents that write code for you. You set the scene, cast the actors, and know when to call "cut."

Here's the key insight: domain expertise matters MORE than AI expertise for this role. The best agent managers will come from people who already understand the business processes being automated. That's you. If you've been writing code for years, you know what good code looks like, what the edge cases are, and when to be suspicious of output. Those are exactly the skills you need to manage agents well.

Learning to manage agents is a concrete, marketable skill. It reduces the pressure of Barrier 5 by giving you a clear growth path -- from individual contributor coding to directing AI systems. And it turns the frustration of reviewing AI output into a professional competency.

[TIMING: 48:45]

---

## SLIDE 45: MANAGING AGENTS IN PRACTICE

So what does managing agents actually look like day to day? Four key practices.

Task orchestration: assign work intelligently between yourself and AI agents based on context, capability, and risk tolerance. Not everything goes to the agent -- you decide what does.

Quality gates: define what "good enough" looks like for agent output, and review it the way you'd review a junior engineer's pull request. Not every line, but the critical paths.

Context engineering: feed agents the right context upfront. CLAUDE.md files, .cursorrules, structured prompts. The better the briefing, the better the output -- same as managing people.

And know when to take over. Salesforce's Agentforce platform resolves about 74% of customer cases autonomously. But that other 26% still needs a human. Knowing which bucket a task falls into -- that's the skill.

[PLACEHOLDER: Humorous Moltbook reference TBD -- something about managing AI agents vs. managing interns vs. managing Moltbook]

[TIMING: 50:00]

---

## SLIDE 46: AGENT MANAGEMENT -- YOUR EXAMPLES

This is where it gets personal. Think about your own experience managing AI agents. What's worked? What hasn't?

[PERSONAL STORIES: Share your own agent management examples here. What tasks did you delegate to an AI agent? How did you set context? Where did the agent surprise you -- positively or negatively? Pick 2-3 examples that illustrate the agent manager practices from the previous slide in real-world scenarios. Bonus points for a story where you had to "take over" mid-task.]

The point is: this is a learnable skill. It feels awkward at first, the same way code review felt awkward when you first started doing it. But with practice, you develop instincts for what to delegate, how to brief, and when to intervene. And that's when AI starts feeling like a force multiplier instead of extra work.

[TIMING: 51:00]

---

## SLIDE 47: VIBE CODING -- THE FUN AND THE RISK

Now, some of you have been thinking -- "What about vibe coding? That's the part I actually enjoy." And you're right. Andrej Karpathy coined the term in early 2025: "Fully give in to the vibes, embrace exponentials, and forget that the code even exists." It was Collins Dictionary's Word of the Year. It's become how a lot of developers describe their best AI experience.

And I get it. The flow state is real. When AI is generating code as fast as you can describe what you want, and it's working, and you're shipping features in hours instead of days -- that feels amazing. Developers report three to five times productivity gains on scaffolding and prototyping tasks. That's enjoyment. That's what we're after.

But here's the flip side. Security researchers found that 45% of AI-generated code contains vulnerabilities. Fast.ai coined the term "dark flow" -- that feeling of productive momentum where you don't realize until weeks later that the code is unmaintainable. And analysis of vibe-coded projects showed significantly higher rates of logic errors, misconfigurations, and security holes.

So vibe coding without guardrails is Barrier 3 at scale -- the "almost right" problem, turbocharged. But vibe coding WITH the five shifts? That's the sweet spot. Assign AI the right tasks -- scaffolding and prototyping are green-light territory. Use context-first prompting even when you're in the zone. Keep a human review checkpoint before anything ships to production. And time-box the vibe sessions so dark flow doesn't eat your whole sprint.

The goal isn't to kill the vibe. It's to keep the vibe AND keep the quality. That's what the five shifts enable.

[TIMING: 52:30]

---

## SLIDE 48: VIBE CODING -- MY PROJECTS

And because I practice what I preach -- here are some things I've vibe-coded myself.

[PERSONAL STORIES: Share your own vibe-coded projects here. What you built, how long it took, what surprised you. The audience connects with real examples from the speaker's own experience. Pick 2-3 projects that show the fun side AND the "learned something the hard way" side.]

The vibe is real. These are projects I built with AI -- and I actually enjoyed the process. That's what we're aiming for.

[TIMING: 53:30]

---

## SLIDE 49: LEAD THE SHIFT -- AUGMENTATION, NOT AUTOMATION

If you have any leadership influence -- whether you're a tech lead, a manager, or an architect -- here's the mindset shift that matters most. Stop thinking about automation. Start thinking about augmentation. The goal isn't "replace the human." The goal is "make the human better."

Don't mandate AI adoption without support. That's where brain fry comes from. A tool you dread using is a tool you'll use badly.

Instead: invest in real training. Pick fewer tools and go deep. Explain where AI fits in specific workflows -- not at the department level, but at the task level. Tell your team what to use it for and what to keep human. Build a shared understanding.

That's not just better for productivity. It's better for your team. Engineers who feel supported adopt AI with confidence. Engineers who feel pressured adopt AI with resentment.

[TIMING: 54:15]

---
## SLIDE 50: YOUR SANE ADOPTION PLAYBOOK

Here's your playbook for this week. Five things, one per day.

Monday: audit your AI tools. List every one your team is using. If it's more than three, pick the best three and commit to them.

Tuesday: pick one workflow to redesign. Not five. One. Where does AI create the most friction right now? That's your target.

Wednesday: define your red zones. Where does AI NOT go? Security decisions? Architecture? Edge cases? Write it down. Make it explicit.

Thursday: require a human review checkpoint. Before anything AI-generated ships -- code, docs, analysis -- one person reads it fully. No exceptions.

Friday: schedule five hours of hands-on training. Put it on the calendar. This week or next. Use your actual tools on your actual work.

[TIMING: 55:45]

---

## SLIDE 51: YOUR MONDAY MORNING PLAN

But maybe you want something even more immediate. Here's what you can do Monday morning -- not next week's process overhaul, but tomorrow's first step.

Try managing an AI agent. Pick one task and direct an AI agent through it. Start small -- a code review, a test suite, a refactoring job. See how it feels to direct instead of write.

Vibe code something fun. Build a personal project. A tool, a prototype, a toy. Remember what got you into programming in the first place.

Apply context-first prompting. On your very next AI interaction, spend 30 extra seconds on context. Notice the difference in output quality.

Experiment without pressure. Give yourself permission to try AI on a low-stakes task. No metrics, no judgment. Just curiosity.

And share what works. Tell one teammate about something AI did well for you this week. Positive momentum spreads.

The goal: start your week with one thing that makes AI feel useful -- not mandatory.

[TIMING: 57:00]

---

## SLIDE 52: OTHER TIPS FOR ENJOYING AI (1 OF 2)

Before we wrap up, a few more practical tips that didn't fit neatly into the five shifts but are worth sharing.

Build your prompt library. When you craft a prompt that works really well -- for test generation, code review, refactoring, whatever -- save it. Keep a personal or team prompt library. You wouldn't rewrite your CI config from scratch every time. Don't rewrite your prompts from scratch either. Over time, this compounds into serious time savings.

Pair AI sessions with a buddy. Just like pair programming, try pair-prompting. One person drives the AI interaction, the other watches the output with fresh eyes. You catch more issues, you learn each other's techniques, and it's more fun than solo verification grinding.

Schedule AI-free deep work. This sounds counterintuitive in a talk about using AI better, but it's essential. Block time where you write code, think through architecture, and solve problems without AI. It keeps your core skills sharp, prevents the skill erosion anxiety we talked about in Barrier 5, and honestly -- sometimes the old-fashioned way is just faster for complex problems.

[TIMING: 58:00]

---

## SLIDE 53: OTHER TIPS FOR ENJOYING AI (2 OF 2)

Celebrate small wins. When AI saves you real time on a task, notice it. Share it with your team. The negativity bias around AI is strong -- we remember the failures but forget the saves. Keeping a "win log" of moments where AI genuinely helped changes your relationship with the tool.

Treat AI like a new hire. We talked about the junior engineer mental model in Shift 2, but take it further. You'd give a new hire an onboarding doc, context about the project, and clear expectations. Do the same for your AI tools. CLAUDE.md files, .cursorrules, project-specific context documents -- these are your AI's onboarding materials. The better you onboard it, the less you have to micromanage it.

Know when to stop re-prompting. This is a real discipline. If you've re-prompted three times and the output still isn't right, the task is probably not a good fit for AI right now. Switch to writing it yourself. The sunk cost of three prompts is nothing compared to the frustration spiral of ten. Set a personal limit and honor it.

[TIMING: 59:00]

---

## SLIDE 54: USING AI AND ENJOYING IT

Let me bring this home.

We started with a gap: widespread adoption, but confidence dropping. We mapped five barriers causing that gap. And we walked through five shifts that close it. Assign AI the right jobs. Adopt lighter mental models. Prompt with context first. Pair your workflows. Put guardrails in place.

And we added two more paths forward: learn to manage AI agents as a real professional skill, and embrace vibe coding with the guardrails to keep it productive.

Remember that three-column workflow diagram? The goal is to move your team from the middle column -- the bolted-on frustration zone -- to the right column -- where humans and AI each have clear roles.

Remember the opening? "Saved 15 minutes, lost 30." The five shifts are how you flip that ratio. Not by using less AI -- by using it with clear task boundaries and a reasonable verification budget.

Here's your challenge: pick one workflow where AI is creating more review work than value. Redesign it using the five shifts. Or try managing an agent. Or vibe code a weekend project. See what changes.

The goal isn't more AI. The goal is less friction. AI becomes useful when task boundaries are clear and the correctness burden drops.

One week. One workflow. One Monday morning. That's how you start.

[TIMING: 60:00]

---

## SLIDE 55: QUESTIONS

I'd love to hear what's on your mind. What resonated? What didn't? What's the biggest challenge you're facing with AI on your team right now?

[Q&A: ~10 minutes]


*Expand any question below for a suggested response.*

<div class="qa-index">

<div class="qa-section-title">Questions About the Core Problem</div>

<details>
<summary>You say adoption is up but confidence is down. What's the actual data behind that?</summary>
<div class="qa-answer">Two separate studies tell the same story. Qualtrics found 52% of workers are actively using AI tools. ManpowerGroup found that worker confidence in using technology at work fell 18% over roughly the same period. Stack Overflow's 2025 developer survey: only about one in three developers trust AI output accuracy, while 46% actively distrust it. More developers distrust AI-generated code than trust it. And Pew found 52% of workers are more worried than hopeful about AI at work. Different studies, different methodologies, same directional finding.</div>
</details>

<details>
<summary>Is this really an AI problem, or just normal technology adoption friction?</summary>
<div class="qa-answer">Both, but AI has unique characteristics that amplify the friction. The "almost right" problem is specific to generative AI -- traditional tools either work or they don't. AI produces output that looks correct, compiles, passes tests, but is subtly incomplete. That verification burden is structurally different from learning any previous technology. BCG's "brain fry" research found 14% more mental effort, 12% more mental fatigue, 19% more information overload, and 33% more decision fatigue among heavy AI users. That's not normal adoption friction.</div>
</details>

<details>
<summary>The "verification tax" -- is that a real measurement or an analogy?</summary>
<div class="qa-answer">It's a pattern observed across engineering teams: AI generates code in about 2 minutes, but the review cycle (reading line by line, comparing against requirements, checking edge cases, testing, fixing) often takes 15+ minutes. It's not a precise universal measurement -- it varies by task and developer -- but the directional finding is consistent: when review overhead exceeds generation time, you're not automating, you're just moving work from one column to another. The talk uses it as a framework for thinking about where AI actually saves time vs. where it shifts the burden.</div>
</details>

<hr>

<div class="qa-section-title">Questions About the Five Barriers</div>

<details>
<summary>Tool sprawl -- how many AI tools should a developer actually use?</summary>
<div class="qa-answer">BCG's 2026 research found productivity gains rose from 1 to 2 tools, peaked at 3, and dropped past 4, while cognitive strain kept climbing. The recommendation: pick your best 2-3 tools, go deep, learn their strengths, build muscle memory, let the rest go. The problem isn't having options -- it's that the tools still don't share context with each other in practice. Protocols like MCP are making progress connecting tools to data sources, but tool-to-tool context transfer remains unsolved. So YOU become the integration layer, re-explaining the same problem to 4 different systems.</div>
</details>

<details>
<summary>What do you mean by "nobody told us where AI fits"?</summary>
<div class="qa-answer">Most organizations adopted AI by bolting it onto existing workflows without redesigning anything. They said "here's a new tool, figure out where it goes." So developers make ad hoc decisions -- sometimes using AI, sometimes not -- with no shared understanding of where it adds value. The bigger problem is ownership: when nobody defines who owns correctness, edge cases, and final judgment at each step, AI-generated work creates hidden review debt. BCG found organizations that communicated clearly about where AI fits in specific workflows saw notably better adoption and satisfaction.</div>
</details>

<details>
<summary>You mentioned "AI brain fry" -- is that a clinical term?</summary>
<div class="qa-answer">It's BCG's term from their March 2026 study with Harvard Business Review, surveying nearly 1,500 workers. They found meaningful increases in mental effort (+14%), mental fatigue (+12%), information overload (+19%), and decision fatigue (+33%) among heavy AI users. 14% of knowledge workers reported significant cognitive strain, with software development flagged as one of the highest-prevalence roles. ActivTrak's analysis of 443 million hours confirmed the pattern: focus sessions dropped 9% while collaboration time surged after AI adoption.</div>
</details>

<details>
<summary>The pressure to keep up -- is that real or just FOMO?</summary>
<div class="qa-answer">Real, with data behind it. Pew found 52% are more worried than hopeful. BCG identified skill erosion -- fear that AI hollows out human capabilities -- as a top workforce concern. For engineers specifically: fear of losing debugging skill, developing shallow understanding of systems, being judged slower than AI-heavy peers, and losing engineering judgment. But here's the key finding: when organizations provided structured support (5+ hours of hands-on training), that anxiety dropped substantially. The pressure isn't inherent to AI -- it's created by lack of support.</div>
</details>

<details>
<summary>You mentioned AI usage as a metric. Isn't tracking adoption important?</summary>
<div class="qa-answer">Tracking adoption is fine -- the problem is when adoption becomes the ONLY metric. When teams are judged on how much they use AI rather than on outcomes, you get Goodhart's Law: the metric becomes the target and ceases to be useful. Microsoft found 75% of knowledge workers using AI regularly, but that doesn't tell you whether the work improved. The solution: pair adoption metrics with outcome metrics -- code quality, time to resolution, developer satisfaction, production incident rates. Usage without outcomes is just activity, and counting tokens is the new counting lines of code.</div>
</details>

<hr>

<div class="qa-section-title">Questions About the Five Shifts</div>

<details>
<summary>Shift 1 -- How do I decide which tasks to give AI vs. keep human?</summary>
<div class="qa-answer">The delegation test: think of AI as a capable junior engineer with no project context. Would you hand this task to that person? If the cost of being wrong is low and you can verify the output quickly -- AI task. If accuracy is critical and deep domain knowledge is needed to evaluate the output -- human task, with AI as support at most. Green light tasks: scaffolding, boilerplate, code explanation, test generation with context, PR summaries. Red light tasks: security reviews, architecture decisions, performance tuning without knowing your constraints.</div>
</details>

<details>
<summary>Shift 2 -- "Lighter mental models" -- can you explain what that means practically?</summary>
<div class="qa-answer">Stop expecting oracle-level answers and start expecting useful first drafts. Think of AI as a capable junior engineer: you give them tasks, review the output, provide directional feedback, send them back to fix things. That recalibrates your expectations. Instead of being frustrated that AI gave you "almost right" code, you expect a good first draft and plan to review. The trust spectrum helps: for boilerplate, lean toward trust. For security code, lean toward verification. Being intentional about where you sit on that spectrum for each task type is what turns AI from anxiety into predictable leverage.</div>
</details>

<details>
<summary>Shift 3 -- Context-first prompting sounds simple. What's the actual formula?</summary>
<div class="qa-answer">Context + Task + Constraints = better output. Tell the model what it needs to know about YOUR system before telling it what to do. Example: instead of "Write unit tests for the auth module" (generic), specify "JWT auth with Flask and pytest, edge cases: expired tokens, invalid issuer, missing scopes, revoked sessions, using our custom TokenManager class." The talk cites a rule of thumb: 30 extra seconds of context tends to save 20 minutes of re-prompting. The "Spot the Missing Context" exercise is a good habit: before every prompt, ask "what context is missing?"</div>
</details>

<details>
<summary>Shift 4 -- What does workflow pairing actually look like day-to-day?</summary>
<div class="qa-answer">Instead of bolting AI onto your existing process, design handoffs. For a code refactoring task: AI does the initial refactoring, you review the logic and check production behavior (connection pooling, caching, query plans), AI refines based on your feedback, you do final approval. The key insight from research: organizations that redesigned workflows WITH AI got ROI; organizations that just added AI to existing workflows didn't. The difference is integration vs. bolt-on.</div>
</details>

<details>
<summary>Shift 5 -- What are the specific guardrails you recommend?</summary>
<div class="qa-answer">Five: (1) Pick your 2-3 tools and commit -- less context rebuilding. (2) Time-box AI work -- if the verification burden exceeds what the task would take manually, switch approaches. (3) Build in AI-free time -- deep-focus work keeps core skills sharp. (4) Require human review before anything ships. (5) Invest in training -- 5 hours of structured, hands-on training with your actual tools and workflows. Not a webinar, not a Slack link -- actual practice time.</div>
</details>

<hr>

<div class="qa-section-title">Questions About Agent Management & Vibe Coding</div>

<details>
<summary>What's an "agent manager" and why should I care?</summary>
<div class="qa-answer">HBR's February 2026 article coined the term: just as product managers emerged during the software revolution, agent managers are becoming essential for AI-powered workforces. The role involves directing AI agents -- assigning tasks, reviewing output, handling exceptions, optimizing workflows. The key insight is that domain expertise matters more than AI expertise. If you've been an engineer for years, you already have the most important qualification: you know what good work looks like. Learning to manage agents is a concrete career growth path that turns the frustration of reviewing AI output into a professional competency.</div>
</details>

<details>
<summary>You mentioned vibe coding. Are you saying it's bad?</summary>
<div class="qa-answer">Not at all -- the talk is careful about this. Vibe coding (Andrej Karpathy's term) is genuinely enjoyable, and developers report 3-5x productivity gains on scaffolding and prototyping. The flow state is real. But vibe coding without guardrails is Barrier 3 at scale -- the "almost right" problem turbocharged. Security researchers found 45% of AI-generated code contains vulnerabilities. Fast.ai coined "dark flow" -- productive momentum where you don't realize until weeks later the code is unmaintainable. The goal isn't to kill the vibe. It's to keep the vibe AND keep the quality by applying the five shifts.</div>
</details>

<details>
<summary>How do I vibe code responsibly?</summary>
<div class="qa-answer">Four rules: (1) Assign it to the right tasks -- scaffolding and prototyping are green-light territory. (2) Use context-first prompting even in the zone. (3) Keep a human review checkpoint before anything ships to production. (4) Time-box the sessions so dark flow doesn't eat your whole sprint. Vibe code for prototyping, then shift to careful review before production.</div>
</details>

<hr>

<div class="qa-section-title">Questions About the Playbook</div>

<details>
<summary>The playbook has five items. Do I really need to do all five?</summary>
<div class="qa-answer">Start with any one. The most impactful for most teams: Monday's tool audit (if you're drowning in tools) or Wednesday's red zone definition (if you're unsure where AI shouldn't be used). Each item is independent. But the full sequence is designed to build on itself -- audit tools, pick one workflow to redesign, define red zones, add review checkpoints, schedule training. One item per day, one week, measurable improvement.</div>
</details>

<details>
<summary>What's the difference between the playbook and the Monday morning plan?</summary>
<div class="qa-answer">The Sane Adoption Playbook is a team-level process change -- audit tools, redesign workflows, define red zones, add review checkpoints, schedule training. It takes a week and involves your team. The Monday Morning Plan is what YOU can do personally, tomorrow morning, with zero organizational buy-in needed. Try managing an agent. Vibe code something fun. Apply context-first prompting. Experiment without pressure. Share what works. One is a team playbook, the other is a personal starting point. Start with whichever matches your situation.</div>
</details>

<details>
<summary>Five hours of training -- that seems like a lot. What should it cover?</summary>
<div class="qa-answer">Not AI theory. Hands-on practice with your actual tools on your actual workflows. Where does the IDE copilot help most? What prompting patterns work for your codebase? Where does AI consistently get your domain wrong? When should you stop re-prompting and just write the code? The training should produce muscle memory, not knowledge. The BCG finding was specific: 5+ hours of structured, hands-on training dropped anxiety substantially. Less than that and the effect was minimal.</div>
</details>

<details>
<summary>How do I convince my team lead or manager to invest in these changes?</summary>
<div class="qa-answer">Use the data: 95% of AI pilots failed to deliver measurable ROI (MIT, 2025). Focus session length dropped 9% after AI adoption (ActivTrak). 46% of developers distrust AI accuracy (Stack Overflow). Then show the fix: 30 seconds of context saves 20 minutes of re-prompting. Organizations that communicated where AI fits saw better adoption. 5 hours of training drops anxiety and improves adoption. Frame it as: "We're already spending time on AI. Let's spend it effectively instead of wastefully."</div>
</details>

<hr>

<div class="qa-section-title">Skeptical / Pushback Questions</div>

<details>
<summary>Isn't this just telling people to be more careful? That's not new advice.</summary>
<div class="qa-answer">The five shifts are structural changes, not just mindfulness. Shift 1 (task matrix) gives teams a decision framework they can reference. Shift 3 (context-first prompting) is a concrete technique with measurable results. Shift 4 (workflow pairing) requires process redesign, not just individual discipline. Shift 5 (guardrails) builds organizational infrastructure -- time-boxed AI sessions, mandatory review checkpoints, training schedules. "Be more careful" is a hope. The five shifts are an implementation plan.</div>
</details>

<details>
<summary>My team is already overwhelmed. Adding process seems counterproductive.</summary>
<div class="qa-answer">The five shifts reduce process overhead, not add it. Picking 2-3 tools instead of 7 removes context-switching. Defining red zones eliminates ambiguity about when to use AI. Time-boxing prevents rabbit holes. The Monday playbook is specifically designed as one item per day -- not a new process to adopt all at once. The research shows that teams with clear AI boundaries experience less cognitive load, not more.</div>
</details>

<details>
<summary>AI is getting better fast. Won't these problems just solve themselves?</summary>
<div class="qa-answer">Some will. Models will get more accurate, which reduces the verification tax on some tasks. But the structural problems -- tool sprawl, workflow confusion, cognitive overload from constant context-switching -- are organizational, not technical. A better model doesn't fix 7 tools that don't share context. A better model doesn't tell your team where AI fits in their workflow. And as AI gets more capable, the stakes of "almost right" get higher, not lower. The five shifts are about organizational readiness, which remains relevant regardless of model capability.</div>
</details>

<details>
<summary>You're essentially saying AI isn't as helpful as advertised. Isn't that pessimistic?</summary>
<div class="qa-answer">The talk ends with "When AI Actually Shines" and the agent management section for a reason. AI is extraordinary for boilerplate, code explanation, test generation with context, and scaffolding. And the shift to managing agents opens a whole new career path. The problem isn't AI -- it's how we're implementing it. The talk's thesis is that AI becomes useful when task boundaries are clear and the correctness burden drops. That's an optimistic message: the frustration is fixable with specific, achievable changes. The goal isn't less AI -- it's less friction.</div>
</details>

<hr>

</div>

---


## SLIDE 56: CLOSING SLIDE

Thank you so much. If you want to stay in touch, my contact info is on the slide. I'd love to hear how the playbook works for your team.

The goal isn't more AI. The goal is less friction. Take that with you.

Thank you. Enjoy the rest of the conference.

[TIMING: 60:00 + Q&A = ~70:00]

---

## TIMING CHECKPOINTS

| Section | Slides | Cumulative Time |
|---------|--------|----------------|
| AI bloopers + opening | 1-4 | 3:30 |
| About me & framing | 5-7 | 7:15 |
| Illustrative scenario | 8-9 | 7:45 |
| Barriers intro | 10-11 | 8:30 |
| Barrier 1: Tool sprawl | 12-14 | 12:45 |
| Barrier 2: Workflow fit | 15-16 | 16:30 |
| Barrier 3: Promise vs reality | 17-19 | 19:45 |
| Barrier 4: Brain fry | 20-23 | 23:30 |
| Barrier 5: Pressure | 24 | 25:00 |
| Midpoint interaction | 25 | 26:00 |
| Metrics problem | 26-27 | 27:30 |
| Shifts intro | 28-30 | 29:00 |
| Shift 1: Right jobs | 31-33 | 32:45 |
| Shift 2: Mental models | 34-35 | 35:30 |
| Shift 3: Context-first | 36-38 | 40:15 |
| Shift 4: Workflow pairing | 39-40 | 43:00 |
| Shift 5: Guardrails + training | 41-42 | 45:45 |
| When AI shines | 43 | 47:30 |
| Agent management | 44-46 | 51:00 |
| Vibe coding + projects | 47-48 | 53:30 |
| Leadership + playbook | 49-50 | 55:45 |
| Monday morning plan | 51 | 57:00 |
| Other tips | 52-53 | 59:00 |
| Close + challenge | 54 | 60:00 |
| Q&A | 55 | ~70:00 |
| Ending | 56 | ~70:00 |

---

## WORD COUNT: ~9,200 spoken words | ~60 min content + ~10 min Q&A = 70 min

NOTE ON TIMING: This version removes the live demo (~2 min savings), moves the Quick Check interaction to right after Barrier 5 for better narrative flow, and adds three new slides (Agent Management Examples, Other Tips 1 & 2) for approximately +3 minutes net. The deck now fits comfortably in a 70-minute slot (60 min content + 10 min Q&A). For a strict 60-minute slot: (1) keep the vibe coding projects slide (48) brief since it's placeholder content, (2) tighten the Other Tips slides (52-53) to hit highlights quickly, (3) the agent examples slide (46) is placeholder and can be brief. The Monday Morning Plan (51), agent management section (44-46), and Other Tips (52-53) are the strongest additions -- prioritize keeping those if cuts are needed.
