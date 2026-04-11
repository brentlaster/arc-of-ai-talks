# Blueprint Deck & Script — Change Report

**Date:** April 10, 2026
**Input files:** blueprint.pptm, blueprint-script.md
**Output files:** blueprint-updated.pptx, blueprint-script-updated.md
**Round 1 result:** 58 slides → 60 slides (3 added, 1 removed)
**Round 2 result:** 60 slides → 56 slides (4 removed, scenario section trimmed)
**Round 3 result:** 56 slides → 56 slides (closing section reordered)
**Final result:** 58 slides → 56 slides

---

## Change 1: Blank Placeholder Slide Inserted After Old Slide 8

**New slide 9:** "[Placeholder — Content to be Added]"

A placeholder slide was added after "The Current State: Speed vs. Safety" (old slide 8, still slide 8). The slide uses the same layout style as the Blueprint Concept slide (centered title + subtitle). A matching blank script section (SLIDE 9) was added with "[Content to be inserted here]" as placeholder text.

**Impact:** All subsequent slides shifted by +1 starting from old slide 9.

---

## Change 2: Chatbot vs. Copilot vs. Agent Moved to New Slide

**New slide 13:** "Three Tiers of AI Systems"

The script originally contained a "Return to SLIDE 10" section within the SLIDE 11 (Every Control Has a Cost) script that described three tiers of AI systems: chatbot, copilot, and agent. This content was extracted from the SLIDE 12 (formerly 11) script and placed on its own new slide with visual elements:

- Three color-coded columns (green for Chatbot, orange for Copilot, red for Agent)
- Description of each tier's behavior and risk level
- Gradient bar showing increasing autonomy → increasing security controls
- Bottom callout reinforcing the progressive control principle

The corresponding script section was extracted and given its own SLIDE 13 heading. The old "Return to SLIDE 10" instruction was removed.

**Impact:** All subsequent slides shifted by an additional +1 (cumulative +2 from old slide 12 onward).

---

## Change 3: Audience Exercise Extracted to New Slide

**New slide 18:** "Audience Exercise"

The script for old slide 15 (Policy-Driven AI) contained an "[AUDIENCE EXERCISE — 45 seconds]" section where the speaker asks the audience to decide how the policy engine should handle a specific scenario. This content was extracted onto its own dedicated slide featuring:

- The scenario description in a highlighted box: "A marketing intern asks the coding assistant to refactor a payment processing module that contains proprietary tokenization logic."
- Four color-coded option buttons: DENY (red), TRANSFORM (orange), ESCALATE (blue), ALLOW (green)
- Each option includes a brief description
- Bottom note about the policy engine making decisions at machine speed

The script was split accordingly: SLIDE 17 (formerly 15) retains the policy engine explanation, and SLIDE 18 contains the exercise interaction script.

**Impact:** All subsequent slides shifted by an additional +1 (cumulative +3 from old slide 16 onward).

---

## Change 4: Duplicate Slides 18 & 19 Combined

**Removed:** Old slide 19 "Layer 2: Three Data Boundary Rules"

Old slides 18 and 19 were reviewed for duplication:

- **Old slide 18** ("Layer 2: Context Isolation & Data Boundaries"): Listed six key principles — session scoping, PII justification, tokenization, classification propagation, multi-tenant isolation, and DLP for AI
- **Old slide 19** ("Layer 2: Three Data Boundary Rules"): Restated the same concepts as three rules — Minimum Necessary Context, PII Justified Entry, Tenant Boundaries Absolute

These were substantially redundant. Old slide 19 was removed from the deck. The script already covered all this content in a single section (the old SLIDE 18 script section), so no script content was lost. Old slide 18 is now slide 21 in the updated deck.

**Impact:** One slide removed, partially offsetting the +3 from additions (net change: +2 slides).

---

## Change 5: Script-to-Deck Sync Fixes

Three sync issues were identified and corrected:

### 5a. Off-by-one error starting at old slide 19

The original deck contained slide 19 ("Three Data Boundary Rules") which had no corresponding script section. This caused all script section numbers from SLIDE 19 onward to be 1 behind the deck slide numbers. Removing the duplicate slide 19 (Change 4) eliminated this misalignment.

### 5b. Extra script section (old SLIDE 29) with no deck slide

The original script had a "## SLIDE 29: Layer 5: What Evidence-Quality Logs Require" section that did not correspond to any individual deck slide — its content was supplementary to the Audit Trails slide. This section was merged into the SLIDE 31 (formerly 28) Audit Trails script section, bringing subsequent script numbers back into alignment with the deck.

### 5c. Swapped script sections for Live Demo and Scenario Walkthroughs

The original script had:
- SLIDE 41: [LIVE DEMO] Blueprint Defenses in Action
- SLIDE 42: Section Divider: Scenario Walkthroughs

But the deck had them in the opposite order (section divider first, then live demo). The script sections were swapped to match the deck order. They are now:
- SLIDE 43: Section Divider: Scenario Walkthroughs
- SLIDE 44: [LIVE DEMO] Blueprint Defenses in Action

---

## Slide Number Mapping (Old → New)

| Old Slide | New Slide | Notes |
|-----------|-----------|-------|
| 1–8 | 1–8 | Unchanged |
| — | **9** | **NEW: Blank placeholder** |
| 9 | 10 | +1 shift |
| 10 | 11 | +1 shift |
| 11 | 12 | +1 shift |
| — | **13** | **NEW: Three Tiers of AI Systems** |
| 12–15 | 14–17 | +2 shift |
| — | **18** | **NEW: Audience Exercise** |
| 16–18 | 19–21 | +3 shift |
| **19** | **—** | **REMOVED: Duplicate (Three Data Boundary Rules)** |
| 20–58 | 22–60 | +2 shift (net) |

---

## Round 1 Final Count

- **Original deck:** 58 slides
- **Added:** 3 (placeholder, tiers, exercise)
- **Removed:** 1 (duplicate Layer 2 rules)
- **After Round 1:** 60 slides, 59 script sections

---

# Round 2: Scenario Section Trimming

The scenarios and closing section (slides 45–60) contained repetition and excessive detail for an audience wrapping up after a dense security talk. Four slides were removed and several script sections were consolidated or tightened.

---

## Change 6: Scenario 1 Consolidated (Slides 46–47 Removed)

**Removed:** Slide 46 "All Six Layers Applied" and Slide 47 "Risk Mitigation in Action"

The original Scenario 1 (customer-facing AI chatbot) spanned three slides: an overview (45), a per-layer walkthrough (46), and a risk-mitigation recap (47). The per-layer detail and risk mapping were redundant — the overview slide already showed the blueprint applied to the chatbot scenario.

The key content from slides 46 and 47 (the layer-by-layer application and the micro-interaction exercise) was folded into the Slide 45 script, which was rewritten to be more concise while preserving the audience interaction moment ("ALLOW, ESCALATE, or DENY?").

**Impact:** Two slides removed. Script section for slide 45 tightened from ~40 lines to ~20 lines.

---

## Change 7: Scenario 2 Consolidated (Slide 50 Removed)

**Removed:** Slide 50 "IP Protection Deep Dive"

Scenario 2 (internal coding assistant) originally spanned three slides: an overview (48), the near-miss incident story (49), and an IP protection deep dive (50). The IP protection detail was already covered in the incident narrative.

The Slide 48 script was rewritten to combine the overview with the incident story (previously split across 48 and 49). Slide 49's script was tightened to focus on the defense-in-depth takeaway — three independent layers catching the same risk. Slide 50 was removed entirely.

**Impact:** One slide removed. Script sections 48 and 49 both rewritten and tightened.

---

## Change 8: Redundant Closing Slide Removed (Slide 57)

**Removed:** Slide 57 "Opening Incidents → Missing Layers"

This slide mapped the opening incidents (Chevy chatbot, DPD, EchoLeak, Copilot secrets) back to missing blueprint layers. The same mapping was already repeated in the closing slide (58). Removing the standalone mapping slide tightens the transition from scenarios directly into the closing.

**Impact:** One slide removed. No script content lost — the incident mapping is preserved in the closing slide script.

---

## Change 9: Closing Script Tightened (Slide 58)

The closing script was trimmed to remove the verbose incident-by-incident layer mapping (which duplicated the now-removed slide 57). The rewritten closing retains the 97% statistic, the forward-looking call to action ("next Monday morning..."), and the final reflection question, but delivers them more concisely.

---

## Round 2 Slide Number Mapping

After removing 4 slides, all slides from 46 onward were renumbered:

| Round 1 Slide | Round 2 Slide | Notes |
|---------------|---------------|-------|
| 1–45 | 1–45 | Unchanged |
| **46** | **—** | **REMOVED: All Six Layers Applied** |
| **47** | **—** | **REMOVED: Risk Mitigation in Action** |
| 48 | 46 | Scenario 2 overview (script rewritten) |
| 49 | 47 | Scenario 2 near-miss (script tightened) |
| **50** | **—** | **REMOVED: IP Protection Deep Dive** |
| 51 | 48 | -2 shift |
| 52 | 49 | -2 shift |
| 53 | 50 | -2 shift |
| 54 | 51 | -2 shift |
| 55 | 52 | -2 shift |
| 56 | 53 | -2 shift |
| **57** | **—** | **REMOVED: Opening Incidents → Missing Layers** |
| 58 | 54 | Closing (script tightened) |
| 59 | 55 | Q&A |
| 60 | 56 | Closing card (no script) |

---

---

# Round 3: Closing Section Reorder

The closing section (slides 48–53) was reordered to improve narrative flow. After the scenario walkthroughs, the audience now sees common mistakes and diagnostic questions before the implementation plan, creating a better arc: "here's what the blueprint does" → "here's what goes wrong without it" → "test yourself" → "here's how to build it."

---

## Change 10: Slides 48–53 Reordered

No slides were added or removed. Six slides were rearranged and script sections were renumbered with transition language updated.

| Round 2 Position | Round 3 Position | Slide Title |
|------------------|------------------|-------------|
| 48 | 50 | Implementation Roadmap |
| 49 | 51 | Your Monday Morning Checklist (1 of 2) |
| 50 | 52 | Your Monday Morning Checklist (2 of 2) |
| 51 | 53 | The Road Ahead |
| 52 | 49 | 5 Questions Every AI Team Should Answer |
| 53 | 48 | What Most Teams Get Wrong |

**Narrative arc after reorder:**
- Slides 45–47: Scenarios (blueprint in action)
- Slide 48: What Most Teams Get Wrong (reality check after seeing the ideal)
- Slide 49: 5 Questions Every AI Team Should Answer (self-assessment bridge)
- Slides 50–52: Implementation Roadmap + Monday Checklists (concrete action plan)
- Slide 53: The Road Ahead (future landscape)
- Slide 54: Closing
- Slide 55: Questions

**Script transitions added/modified:**
- Slide 47 → 48: Added bridge from scenarios to anti-patterns
- Slide 48 → 49: Added bridge from anti-patterns to self-assessment questions
- Slide 49 → 50: Updated stage direction and added bridge to roadmap
- Slide 50: Adjusted opening line from "How do you actually implement this?" to "Let's make this concrete."

---

## Final Slide Count

- **Original deck:** 58 slides
- **After Round 1:** 60 slides (+3 added, -1 removed)
- **After Round 2:** 56 slides (-4 removed)
- **After Round 3:** 56 slides (reordered, no additions/removals)
- **Net change:** -2 slides from original
- **Script sections:** 55 (slide 56 is closing card with no speaker script)
