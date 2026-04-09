# Context Engineering: Anticipated Audience Q&A

## Questions About the Core Concept

**Q: How is context engineering different from prompt engineering?**
Prompt engineering is a subset of context engineering. Prompt engineering focuses on crafting the text of a single input. Context engineering is the full system: instructions, retrieval pipelines, memory architecture, formatting, constraints, and workflow decomposition. It's the difference between writing one email well and designing the entire communication system. The Anthropic engineering blog frames it as "what configuration of context is most likely to generate the desired behavior" — that's a systems design question, not a copywriting question.

**Q: Isn't this just RAG with extra steps?**
RAG is one pillar (Retrieval) out of six. A team can have excellent RAG and still fail because their system prompt is generic, their context window is unstructured, they have no constraints, and they're cramming everything into one massive prompt. Context engineering treats all six pillars as an integrated system. RAG is necessary but not sufficient.

**Q: Does context engineering work with all models, or only frontier models?**
It works across models — that's actually one of the key findings. The ACE framework research showed context-engineered systems matching GPT-4.1-based agents without fine-tuning. In practice, a well-contexted smaller model often outperforms a poorly-contexted larger one. Start with context engineering on whatever model you have; upgrade the model only after you've optimized context.

**Q: You mentioned the ACE framework showed +10.6% accuracy. Is that a meaningful improvement?**
In the context of agentic tasks, yes — these are complex, multi-step workflows where even small accuracy gains cascade across steps. But the more striking number is the 86.9% latency reduction. Faster AND better is rare in AI. The mechanism is straightforward: focused context means fewer wasted tokens, which means faster inference and less noise for the model to parse. As noted in the talk, it's one study — strong directional evidence, not the final word.

---

## Questions About Implementation

**Q: Where do I start? All six pillars feel overwhelming.**
Use the diagnostic ladder from the talk: (1) Is your system prompt specific? (2) Is retrieval pulling relevant docs? (3) Is context structured? (4) Are constraints explicit? (5) Should the task be decomposed? Work top to bottom. Most teams find their biggest win in pillar 1 (rewriting a generic system prompt) or pillar 2 (fixing retrieval relevance). The Monday morning playbook gives you seven concrete steps — start with items 1 and 2 this week.

**Q: How do I measure context quality vs. model quality?**
Use the five-step eval recipe: freeze the model, change exactly one context lever, score 20 representative tasks on accuracy/relevance/latency, then repeat with the next lever. Track both output quality metrics (accuracy, relevance, consistency, confidence) and context health metrics (retrieval precision, coverage, redundancy, latency). If improving context moves the output metrics, context was the bottleneck.

**Q: How much time does context engineering actually take?**
The system prompt rewrite example in the talk took 20 minutes and caught a race condition the old prompt missed. Structuring prompts with XML tags takes 30 seconds per prompt. The support bot case study was two weeks of work for a hallucination drop from 23% to under 4%. The ROI is typically very fast because you're not training models or building new infrastructure — you're reorganizing information you already have.

**Q: What tools should I use for context engineering?**
There's no single "context engineering tool" — it's a practice applied across your stack. For retrieval: whatever vector DB you're using (ChromaDB to start, Pinecone/Weaviate at scale). For memory: session stores and summarization pipelines. For evaluation: custom scoring scripts against your 20 representative tasks. The tooling is less important than the methodology.

**Q: How do I handle context rot in production?**
Four practical mitigations: context pruning (remove irrelevant old messages), summarization (condense conversation history into digests), session resets (start fresh when context gets too long), and sliding windows (keep only the last N relevant turns). Monitor conversation length vs. output quality — when you see accuracy drop at a consistent turn count, that's your pruning threshold.

---

## Questions About Retrieval & RAG

**Q: What's the right chunk size for RAG?**
There's no universal answer, but the litmus test from the talk is useful: if a chunk makes sense to a human on its own, it will make sense to the model. Fixed 512-token chunks that break mid-paragraph are a common anti-pattern. Use semantic chunking that respects document structure — paragraphs, sections, code blocks. Start with larger chunks and shrink only if retrieval precision drops.

**Q: How do I handle deprecated docs in my RAG index?**
Add a "last-verified" metadata tag and a recency filter to your retrieval pipeline. When docs are updated, flag old versions. The talk describes a documentation agent giving wrong API answers because deprecated docs were still in the index — a recency filter and metadata tag eliminated the problem overnight.

**Q: What's the difference between naive RAG and a context engine?**
Naive RAG: embed query → find similar documents → dump them in the prompt. A context engine: retrieval + verification (is this doc current and accurate?) + reasoning (is this relevant to THIS specific question?) + access control (is this user authorized to see this?). The operational difference is between "here are the 5 most similar documents" and "here are the 3 documents that are verified current, relevant to this question type, and authorized for this user."

---

## Questions About Memory & Formatting

**Q: Can you explain the "lost in the middle" problem more?**
Stanford/UC Berkeley/Samaya AI research found that LLMs use information at the beginning and end of the context window effectively, but information placed in the middle gets significantly less attention. This is an architectural property of transformer attention mechanisms. The practical fix: front-load your most important information, back-load constraints and output format, compress the middle aggressively.

**Q: How should I structure my prompts? XML, JSON, or markdown?**
All three work — the key is using any consistent semantic structure rather than unstructured text. XML tags are popular because they create clear, labeled boundaries the model can parse. JSON works well for structured data. Markdown headers work for document-style context. The FlowHunt analysis cited in the talk found 30-40% error rate reductions just from structuring inputs. Pick one format and be consistent.

---

## Questions About Multi-Agent & Decomposition

**Q: When should I use multi-agent architectures vs. a single prompt?**
Use multi-agent when specialization is real — when different steps of your workflow genuinely benefit from different context. The code review example in the talk decomposes into: understand the ticket → diff against style guide → check test coverage → validate deployment config. Each step has focused context and produces better results. Don't create agents for the sake of it — only when context separation genuinely helps.

**Q: How do agents share context without losing information?**
Through an orchestrator that manages context routing. Each specialist agent gets only what it needs, and the orchestrator aggregates results. The key is explicit interfaces between agents — what information flows in, what flows out. Think of it like microservices: clear contracts, focused responsibilities.

---

## Skeptical / Pushback Questions

**Q: Isn't this just good software engineering applied to AI?**
Yes, and that's the point. The talk frames context engineering as "systems engineering, not aesthetic prompt writing." The same principles that make software systems reliable — clear interfaces, focused components, structured data, explicit constraints, measurable outcomes — apply directly to AI systems. The gap is that most teams treat AI prompts as one-off text rather than engineered systems.

**Q: My team doesn't have time for this. We're shipping features.**
The system prompt rewrite takes 20 minutes. Structuring your 5 most common prompts takes an afternoon. The support bot case study was 2 weeks. Compare that to weeks spent debugging inconsistent AI outputs, or months evaluating model upgrades that don't solve the actual problem. Context engineering is typically the fastest path to better AI output because you're reorganizing existing information, not building new systems.

**Q: Won't this all be automated away as models get smarter?**
Possibly some of it — the talk's road ahead section mentions context engineering partially automating itself. But even the ACE research showed that structured context still dramatically outperforms unstructured context on frontier models. As long as models operate on context windows, the quality of what goes in will determine the quality of what comes out. And as agents become more autonomous, context engineering becomes more important, not less — an agent with bad context makes confident mistakes at scale.

**Q: We tried RAG and it didn't work. Why would context engineering be different?**
RAG failing is often a symptom of broader context problems — bad chunking, no recency filtering, no relevance verification, irrelevant docs in the index. The six-pillar framework helps you diagnose which specific aspect failed. Was it the retrieval itself, the formatting of retrieved content, missing constraints, or trying to do too much in one prompt? "RAG didn't work" usually means one specific pillar needs fixing, not that the approach is wrong.
