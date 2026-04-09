# Using AI and Enjoying It: Anticipated Audience Q&A

## Questions About the Core Problem

**Q: You say adoption is up but confidence is down. What's the actual data behind that?**
Two separate studies tell the same story. Qualtrics found 52% of workers are actively using AI tools. ManpowerGroup found that worker confidence in using technology at work fell 18 percentage points over roughly the same period. Stack Overflow's 2025 developer survey: only about one in three developers trust AI output accuracy, while 46% actively distrust it. More developers distrust AI-generated code than trust it. And Pew found 52% of workers are more worried than hopeful about AI at work. Different studies, different methodologies, same directional finding.

**Q: Is this really an AI problem, or just normal technology adoption friction?**
Both, but AI has unique characteristics that amplify the friction. The "almost right" problem is specific to generative AI — traditional tools either work or they don't. AI produces output that looks correct, compiles, passes tests, but is subtly incomplete. That verification burden is structurally different from learning any previous technology. BCG's "brain fry" research found 14% more mental effort, 12% more mental fatigue, 19% more information overload, and 33% more decision fatigue among heavy AI users. That's not normal adoption friction.

**Q: The "verification tax" — is that a real measurement or an analogy?**
It's a pattern observed across engineering teams: AI generates code in about 2 minutes, but the review cycle (reading line by line, comparing against requirements, checking edge cases, testing, fixing) often takes 15+ minutes. It's not a precise universal measurement — it varies by task and developer — but the directional finding is consistent: when review overhead exceeds generation time, you're not automating, you're just moving work from one column to another. The talk uses it as a framework for thinking about where AI actually saves time vs. where it shifts the burden.

---

## Questions About the Five Barriers

**Q: Tool sprawl — how many AI tools should a developer actually use?**
BCG's 2026 research found productivity gains rose from 1 to 2 tools, peaked at 3, and dropped past 4, while cognitive strain kept climbing. The recommendation: pick your best 2-3 tools, go deep, learn their strengths, build muscle memory, let the rest go. The problem isn't having options — it's that none of the tools share context with each other, so YOU become the integration layer, re-explaining the same problem to 4 different systems.

**Q: What do you mean by "nobody told us where AI fits"?**
Most organizations adopted AI by bolting it onto existing workflows without redesigning anything. They said "here's a new tool, figure out where it goes." So developers make ad hoc decisions — sometimes using AI, sometimes not — with no shared understanding of where it adds value. The bigger problem is ownership: when nobody defines who owns correctness, edge cases, and final judgment at each step, AI-generated work creates hidden review debt. BCG found organizations that communicated clearly about where AI fits in specific workflows saw notably better adoption and satisfaction.

**Q: You mentioned "AI brain fry" — is that a clinical term?**
It's BCG's term from their March 2026 study with Harvard Business Review, surveying nearly 1,500 workers. They found meaningful increases in mental effort (+14%), mental fatigue (+12%), information overload (+19%), and decision fatigue (+33%) among heavy AI users. 14% of knowledge workers reported significant cognitive strain, with software development flagged as one of the highest-prevalence roles. ActivTrak's analysis of 443 million hours confirmed the pattern: focus sessions dropped 9% while collaboration time surged after AI adoption.

**Q: The pressure to keep up — is that real or just FOMO?**
Real, with data behind it. Pew found 52% are more worried than hopeful. BCG identified skill erosion — fear that AI hollows out human capabilities — as a top workforce concern. For engineers specifically: fear of losing debugging skill, developing shallow understanding of systems, being judged slower than AI-heavy peers, and losing engineering judgment. But here's the key finding: when organizations provided structured support (5+ hours of hands-on training), that anxiety dropped substantially. The pressure isn't inherent to AI — it's created by lack of support.

---

## Questions About the Five Shifts

**Q: Shift 1 — How do I decide which tasks to give AI vs. keep human?**
The delegation test: think of AI as a capable junior engineer with no project context. Would you hand this task to that person? If the cost of being wrong is low and you can verify the output quickly — AI task. If accuracy is critical and deep domain knowledge is needed to evaluate the output — human task, with AI as support at most. Green light tasks: scaffolding, boilerplate, code explanation, test generation with context, PR summaries. Red light tasks: security reviews, architecture decisions, performance tuning without knowing your constraints.

**Q: Shift 2 — "Lighter mental models" — can you explain what that means practically?**
Stop expecting oracle-level answers and start expecting useful first drafts. Think of AI as a capable junior engineer: you give them tasks, review the output, provide directional feedback, send them back to fix things. That recalibrates your expectations. Instead of being frustrated that AI gave you "almost right" code, you expect a good first draft and plan to review. The trust spectrum helps: for boilerplate, lean toward trust. For security code, lean toward verification. Being intentional about where you sit on that spectrum for each task type is what turns AI from anxiety into predictable leverage.

**Q: Shift 3 — Context-first prompting sounds simple. What's the actual formula?**
Context + Task + Constraints = better output. Tell the model what it needs to know about YOUR system before telling it what to do. Example: instead of "Write unit tests for the auth module" (generic), specify "JWT auth with Flask and pytest, edge cases: expired tokens, invalid issuer, missing scopes, revoked sessions, using our custom TokenManager class." The talk cites a rule of thumb: 30 extra seconds of context tends to save 20 minutes of re-prompting. The "Spot the Missing Context" exercise is a good habit: before every prompt, ask "what context is missing?"

**Q: Shift 4 — What does workflow pairing actually look like day-to-day?**
Instead of bolting AI onto your existing process, design handoffs. For a code refactoring task: AI does the initial refactoring → you review the logic and check production behavior (connection pooling, caching, query plans) → AI refines based on your feedback → you do final approval. The key insight from research: organizations that redesigned workflows WITH AI got ROI; organizations that just added AI to existing workflows didn't. The difference is integration vs. bolt-on.

**Q: Shift 5 — What are the specific guardrails you recommend?**
Five: (1) Pick your 2-3 tools and commit — less context rebuilding. (2) Time-box AI work — if the verification burden exceeds what the task would take manually, switch approaches. (3) Build in AI-free time — deep-focus work keeps core skills sharp. (4) Require human review before anything ships. (5) Invest in training — 5 hours of structured, hands-on training with your actual tools and workflows. Not a webinar, not a Slack link — actual practice time.

---

## Questions About Vibe Coding

**Q: You mentioned vibe coding. Are you saying it's bad?**
Not at all — the talk is careful about this. Vibe coding (Andrej Karpathy's term) is genuinely enjoyable, and developers report 3-5x productivity gains on scaffolding and prototyping. The flow state is real. But vibe coding without guardrails is Barrier 3 at scale — the "almost right" problem turbocharged. Security researchers found 45% of AI-generated code contains vulnerabilities. Fast.ai coined "dark flow" — productive momentum where you don't realize until weeks later the code is unmaintainable. The goal isn't to kill the vibe. It's to keep the vibe AND keep the quality by applying the five shifts.

**Q: How do I vibe code responsibly?**
Four rules: (1) Assign it to the right tasks — scaffolding and prototyping are green-light territory. (2) Use context-first prompting even in the zone. (3) Keep a human review checkpoint before anything ships to production. (4) Time-box the sessions so dark flow doesn't eat your whole sprint. Vibe code for prototyping, then shift to careful review before production.

---

## Questions About the Playbook

**Q: The Monday playbook has five items. Do I really need to do all five?**
Start with any one. The most impactful for most teams: Monday's tool audit (if you're drowning in tools) or Wednesday's red zone definition (if you're unsure where AI shouldn't be used). Each item is independent. But the full sequence is designed to build on itself — audit tools → pick one workflow to redesign → define red zones → add review checkpoints → schedule training. One item per day, one week, measurable improvement.

**Q: Five hours of training — that seems like a lot. What should it cover?**
Not AI theory. Hands-on practice with your actual tools on your actual workflows. Where does the IDE copilot help most? What prompting patterns work for your codebase? Where does AI consistently get your domain wrong? When should you stop re-prompting and just write the code? The training should produce muscle memory, not knowledge. The BCG finding was specific: 5+ hours of structured, hands-on training dropped anxiety substantially. Less than that and the effect was minimal.

**Q: How do I convince my team lead or manager to invest in these changes?**
Use the data: only 1 in 4 organizations have achieved repeatable AI ROI (MIT/Wharton). Focus sessions dropped 9% after AI adoption (ActivTrak). 46% of developers distrust AI accuracy (Stack Overflow). Then show the fix: 30 seconds of context saves 20 minutes of re-prompting. Organizations that communicated where AI fits saw better adoption. 5 hours of training drops anxiety and improves adoption. Frame it as: "We're already spending time on AI. Let's spend it effectively instead of wastefully."

---

## Skeptical / Pushback Questions

**Q: Isn't this just telling people to be more careful? That's not new advice.**
The five shifts are structural changes, not just mindfulness. Shift 1 (task matrix) gives teams a decision framework they can reference. Shift 3 (context-first prompting) is a concrete technique with measurable results. Shift 4 (workflow pairing) requires process redesign, not just individual discipline. Shift 5 (guardrails) builds organizational infrastructure — time-boxed AI sessions, mandatory review checkpoints, training schedules. "Be more careful" is a hope. The five shifts are an implementation plan.

**Q: My team is already overwhelmed. Adding process seems counterproductive.**
The five shifts reduce process overhead, not add it. Picking 2-3 tools instead of 7 removes context-switching. Defining red zones eliminates ambiguity about when to use AI. Time-boxing prevents rabbit holes. The Monday playbook is specifically designed as one item per day — not a new process to adopt all at once. The research shows that teams with clear AI boundaries experience less cognitive load, not more.

**Q: AI is getting better fast. Won't these problems just solve themselves?**
Some will. Models will get more accurate, which reduces the verification tax on some tasks. But the structural problems — tool sprawl, workflow confusion, cognitive overload from constant context-switching — are organizational, not technical. A better model doesn't fix 7 tools that don't share context. A better model doesn't tell your team where AI fits in their workflow. And as AI gets more capable, the stakes of "almost right" get higher, not lower. The five shifts are about organizational readiness, which remains relevant regardless of model capability.

**Q: You're essentially saying AI isn't as helpful as advertised. Isn't that pessimistic?**
The talk ends with "When AI Actually Shines" for a reason. AI is extraordinary for boilerplate, code explanation, test generation with context, and scaffolding. The problem isn't AI — it's how we're implementing it. The talk's thesis is that AI becomes useful when task boundaries are clear and the correctness burden drops. That's an optimistic message: the frustration is fixable with specific, achievable changes. The goal isn't less AI — it's less friction.
