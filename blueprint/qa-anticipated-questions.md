# Enterprise AI Security Blueprint: Anticipated Audience Q&A

## Questions About Scope & Framing

**Q: Is this blueprint specific to a particular cloud provider or AI vendor?**
No. The blueprint is vendor-agnostic — it works regardless of whether you're using OpenAI, Anthropic, open-source models, or a mix. The six layers map to infrastructure capabilities (IAM, DLP, logging, rate limiting) that exist in every cloud platform. The talk shows Terraform examples, but the patterns apply to AWS, Azure, GCP, or on-prem. The security principles are the same; the implementation syntax changes.

**Q: We're a small company with limited security resources. Is this overkill?**
The blueprint is layered specifically so you can adopt incrementally. Start with three things: inventory your AI systems, add audit logging, and implement kill switches. Those are platform-owned controls that protect every AI system from day one. The phased roadmap in the talk goes from "Week 1: asset inventory" to "Months 3-6: full governance." You don't need all six layers on day one. But you need to know which layers you're missing.

**Q: How does this relate to existing security frameworks like NIST or ISO 42001?**
The blueprint complements them. The EU AI Act is the regulatory "what you must do" (risk assessments, audit trails, human oversight for high-risk systems). ISO 42001 and NIST AI RMF are governance frameworks — the "how to do it." The blueprint provides the technical architecture that implements what those frameworks require. Your legal team maps controls to compliance requirements; the blueprint gives engineers the implementation spec.

---

## Questions About the Six Layers

**Q: Layer 1 — Why do AI agents need their own service accounts? Can't they use the developer's credentials?**
If an agent gets compromised while running on a developer's credentials, the attacker has the full run of that developer's access — code repos, databases, internal systems, everything. An agent with its own scoped service account limits the blast radius to exactly what the agent needs. This is standard principle of least privilege, applied to AI. NIST's AI Agent Standards Initiative is explicitly working on agent identity specifications for this reason.

**Q: Layer 2 — How does PII tokenization work in practice? Doesn't the model need real data to give useful answers?**
The model works with "CUST_TOKEN_4829" instead of "John Smith, 555-0123." Surprisingly, this works well for most tasks — the model can reason about relationships, patterns, and logic without seeing real PII. When the response needs to include the real name, the tokenization is reversed at the application layer after the model responds. The key insight: if the model hallucinates or the conversation gets logged, no real data is exposed. For the minority of tasks that genuinely need real PII, that access should be explicitly justified, approved, minimized, and auditable.

**Q: Layer 3 — Can you really defend against prompt injection? Isn't it an unsolved problem?**
No single technique is sufficient — that's why the blueprint uses defense-in-depth. Four layers: input sanitization (strip known patterns), instruction hierarchy (system instructions always override user/retrieved content), canary tokens (detect if system prompt was extracted), and output scanning (catch data leakage in responses). The talk's RAG injection walkthrough shows how the defenses work in sequence. If one layer misses a novel encoding, the next layer catches it. Is it 100% secure? No. Is it dramatically better than no defenses? Absolutely. And OWASP lists prompt injection as #1 on the Top 10 for LLMs specifically because most organizations have zero defenses.

**Q: What's shadow AI and how do I deal with it?**
Shadow AI is when AI adoption outpaces governance — developers using AI tools with real customer data, teams deploying models without going through any governance process, agents running under personal credentials. 59% of enterprises confirm it's already in their environment. It shows up three ways: *data leakage* (sensitive data flowing into unvetted models and can't be recalled), *compliance gaps* (no audit trail, no oversight, no way to prove regulatory compliance), and *invisible identities* (fragmented accounts and unmanaged AI service credentials). The triage approach: inventory first to find everything, then wrap the highest-risk systems with audit logging and kill switches before trying to move them into a governed pipeline. Don't try to shut everything down on day one — you'll lose the teams getting real value. Meet them where they are and bring the controls to them.

**Q: Layer 5 — What's the difference between debugging logs and evidence-quality logs?**
Debugging logs tell engineers what went wrong: stack traces, error messages, timing data. Evidence-quality logs tell regulators and incident responders what happened, who was affected, and whether controls were in place. They capture: WHO made the request (identity + role), WHAT was asked (full prompt), WHAT was returned (full response + confidence), WHAT data was accessed (sources + scope), and WHY decisions were made (policy engine reasoning). Log structured metadata, not raw prompts — you don't want your audit trail becoming a data exfiltration target.

**Q: Layer 6 — 60% of orgs can't kill a rogue AI agent. What does a good kill switch look like?**
A simple API endpoint that: stops accepting new requests, cancels in-flight calls, logs the kill event with reason and initiator, and alerts the incident channel. Recovery requires manual review before restart — fail-safe, not fail-open. The critical design principle: if your AI agent starts hallucinating financial advice to customers at 3 AM, can you stop it in 60 seconds? If not, this should be your top priority. A kill switch is a few dozen lines of code — the implementation is trivial, the organizational decision to build it is what's usually missing.

---

## Questions About Real-World Scenarios

**Q: In the coding assistant scenario, how does the system know code is proprietary?**
Content classification. Code in certain directories, repos, or containing certain patterns (proprietary algorithms, internal API signatures, custom tokenization logic) gets tagged as proprietary by classification rules. When the coding assistant assembles context to send to a model, the DLP filter checks those tags. Proprietary code routes to the internal model; non-proprietary code can use external providers. The developer doesn't need to think about it — the platform makes the routing decision automatically. That's the key UX insight: secure routing should be invisible.

**Q: How do you handle the financial chatbot scenario where a customer asks something out of scope?**
The policy engine intercepts it. The chatbot's scope is defined in its service account and behavioral constraints: individual account queries only, no aggregate analytics, no investment advice. When a customer asks "What's the average balance across all accounts in my zip code?" — that's aggregate analytics across multiple accounts. The policy engine denies it automatically, logs the attempt, and the chatbot responds with something like "I can help with your individual account. For aggregate analytics, please contact your account manager."

**Q: What about multi-tenant RAG systems? How do you prevent data leakage?**
Retrieval security is a five-step chain: tenant filter first (before any similarity search), then classification propagation (sensitivity tags survive through the pipeline), then retrieved-content scanning (verify nothing slipped through), then prompt assembly boundary enforcement (each request scoped to a single tenant at infrastructure level), then output scanning. If any link breaks, data leaks. The insidious thing is the response will look completely normal — the model seamlessly weaves leaked information into a response that looks right. You need automated cross-tenant testing to catch it.

---

## Questions About Compliance & Regulation

**Q: What are the actual penalties under the EU AI Act?**
The penalty structure is tiered: prohibited AI practices can trigger fines up to 35 million euros or 7% of global annual turnover (whichever is higher). Other obligation categories carry lower maximums but are still significant. The Act entered into force in August 2024 with phased deadlines — full application by August 2026. The governance obligations include documented risk assessments, audit trails, and human oversight for high-risk systems. Check the latest enforcement calendar before presenting to leadership.

**Q: Do we need to comply with the EU AI Act if we're US-based?**
If your AI systems process data from or serve users in the EU, yes. The Act has extraterritorial reach similar to GDPR. Even if it doesn't apply directly, the governance frameworks (ISO 42001, NIST AI RMF) are becoming de facto standards that auditors and enterprise customers expect. Building the blueprint now positions you ahead of wherever regulation lands.

**Q: How do we demonstrate compliance to auditors?**
Three things: structured audit trails (Layer 5) that show every AI interaction with WHO/WHAT/WHY/OUTCOME, a model registry (Layer 4) showing approved models with version tracking and expiration dates, and clear accountable ownership across Platform, Security, App Teams, and Legal — the "Who Owns What?" model — so each control has a named owner. The blueprint makes compliance demonstrable because everything is logged, version-controlled, and attributable.

---

## Questions About Implementation

**Q: What's the phased implementation roadmap?**
Phase 0 (Week 1): AI asset inventory — find every AI system. Phase 1 (Month 1): Identity and audit trails — the foundation. Phase 2 (Months 2-3): Data boundaries, prompt defenses, tool isolation. Phase 3 (Months 3-6): Model governance, operational controls, vendor risk, security testing, governance operating model. Each phase builds on the previous one. Ship Phase 0 this week.

**Q: Who owns AI security — the platform team, the security team, or the app team?**
Distributed ownership across four teams, each owning what they're best positioned to own. *Platform* builds the infrastructure everyone else depends on: IAM and identity, audit infrastructure, operational controls like canary deploys and kill switches. *Security* is accountable for the most capabilities — data boundaries, prompt defenses, model registry, red teaming, incident response. *App teams* own red teaming their own AI features, implementing input guards, and being first responders for their apps. *Legal* owns vendor risk and regulatory guidance. The key principle: app teams do not invent their own security model. They consume platformized controls. Security sets policies; every team has skin in the game. If you have a platform engineering team, the blueprint maps directly to what they already do.

**Q: What's the cost of implementing this?**
The biggest cost is organizational, not technical. Kill switches are a few dozen lines of code. Audit logging is a database table and a structured JSON schema. A redaction script is 50 lines. The real investment is: getting teams to adopt scoped service accounts instead of shared credentials, getting data teams to propagate classification tags, getting governance to define model registry policies, and building the organizational discipline to maintain it all. The phased roadmap spreads this over 6 months.

---

## Skeptical / Pushback Questions

**Q: We're using OpenAI/Anthropic enterprise APIs with data processing agreements. Aren't we already covered?**
A DPA covers what the provider does with your data. It doesn't cover what your application does before and after the API call. If your app sends raw PII in prompts, retrieves cross-tenant data in RAG, has no audit trail, runs on shared credentials, and has no kill switch — the DPA doesn't help. The blueprint addresses the security architecture around the model, not just the model provider relationship.

**Q: The opening incidents are consumer chatbots. Enterprise systems are more sophisticated.**
The talk explicitly addresses this: Microsoft 365 Copilot had the EchoLeak vulnerability — a zero-click prompt injection that could exfiltrate data, bypassing Microsoft's injection classifier. Researchers found thousands of valid API keys in GitHub Copilot output. These are the biggest tech companies in the world. The same architectural failures (no input filtering, no output scanning, no behavioral constraints) recur at very different scales. The difference between a chatbot selling a car for a dollar and an enterprise AI leaking financial data is scale and consequence.

**Q: 97% had no proper controls — that number seems too high to be real.**
It's from the IBM/Ponemon 2025 Cost of a Data Breach study, specifically among organizations that experienced an AI-related breach. The qualifier matters: this is 97% of breached organizations, not 97% of all organizations. But 13% of organizations have already experienced AI-related breaches, and 33% have zero audit trails. The number is alarming but consistent with the maturity gap the talk describes.

**Q: Won't all this security overhead slow down our AI development?**
The closing thesis of the talk is "security enables innovation." Organizations that can observe, throttle, and stop their AI systems deploy more often, not less, because they trust their safety net. The blueprint isn't about adding friction — it's about building the foundation that lets you deploy AI systems your organization actually trusts. When teams trust the safety net, they ship faster and take on harder problems.
