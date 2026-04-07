# Change Report: "The Enterprise AI Security Blueprint"

**Original deck:** ai-security-blueprint.pptx (58 slides)
**Updated deck:** ai-security-blueprint_updated.pptx (60 slides)
**Original script:** ai-security-blueprint-script.md (58 SLIDE sections)
**Updated script:** ai-security-blueprint-script_updated.md (60 SLIDE sections)

---

## Summary of Changes

| Category | Changes Made |
|----------|-------------|
| Dark text on dark shapes (#1) | Fixed on slides 12, 19, 37, 41 |
| Fabricated experience claims (#2) | None found — script was clean |
| Source attribution (#3) | Added IBM/Ponemon attribution to 6 script passages; added source text box on slide 8 |
| New slides for key concepts (#4) | 1 new slide: "Every Control Has a Cost" (position 10, SLIDE 9b) |
| Duplicate examples (#5) | Reviewed — no problematic duplications found |
| Long numbered lists (#6) | Split slide 51 (8-item checklist) into 2 slides (positions 52-53) |
| Connectors/shapes (#7) | Reviewed — no disconnected connectors found |
| Text overflow (#8) | No overflow issues detected |
| Branding/style preserved (#9) | All changes match existing deck style |

---

## Detailed Changes

### 1. Dark Text on Dark Shapes

**Slide 12 (End-to-End: An AI Request Through All 6 Layers):**
Fixed 6 layer labels (L1-L6) that had dark gray text (#333333) on colored backgrounds:

| Layer | Background | Old Text Color | New Text Color |
|-------|-----------|---------------|---------------|
| L1 | #1A5276 (dark blue) | #333333 | #FFFFFF |
| L2 | #117A65 (dark green) | #333333 | #FFFFFF |
| L3 | #7D3C98 (dark purple) | #333333 | #FFFFFF |
| L4 | #B9770E (dark orange) | #333333 | #FFFFFF |
| L5 | #2E86C1 (dark blue) | #333333 | #FFFFFF |
| L6 | #C0392B (dark red) | #333333 | #FFFFFF |

**Slide 19 (Layer 2: Multi-Tenant Context Isolation):**
Title text changed from dark (#1D1D1D) to white (#FFFFFF) for visibility against the dark slide master background. Code text (Consolas font) inside the two white content boxes ("Without Isolation" / "With Isolation") was initially changed to white, then corrected back to dark (#1D1D1D) to maintain readability against the white box backgrounds.

**Slide 37 (AI Security RACI: Key Ownership Boundaries):**
Fixed 5 table header cells with dark gray text (#333333) on dark blue background (#011936) — changed to white (#FFFFFF).

**Slide 41 (What Breaks Without Each Control?):**
- "Model Gov" label: changed from #011936 (dark navy) to #FFFFFF on dark navy background
- "Audit" label: changed from #E74C3C (red) to #FFFFFF on red background

**Slides reviewed but no changes needed:** 4, 7, 9, 27, 40, 43, 50, 53, 54 — either adequate contrast already present or text on light/transparent backgrounds.

### 2. Fabricated Personal Experience Claims

**No fabricated claims found.** The script appropriately uses third-party incident narratives (Chevy chatbot, DPD), hypothetical scenarios, and general guidance language. No instances of "I've worked with teams," "In my experience," or similar fabricated firsthand claims.

### 3. Source Attribution

**Slide 8 (deck):** Added source citation text box: "Source: IBM/Ponemon 2025 Cost of a Data Breach Report" — positioned bottom-right, 10.5pt Poppins, gray (#999999).

**Slides 5, 6, 7 (deck):** Already had proper source citations — no changes needed.

**Script attribution fixes (6 passages):**

| Slide | Change |
|-------|--------|
| SLIDE 6 | Added "according to the same IBM/Ponemon study" before the 13% statistic |
| SLIDE 7 | Added "The IBM/Ponemon data breaks it down further" before the detailed stats |
| SLIDE 8 | Added "According to the IBM/Ponemon 2025 report" before 98% stat; added "the same study found" before <1 in 10 stat |
| SLIDE 15 | Changed "Most organizations" to "Many organizations" (unsourced claim softened) |
| SLIDE 24 | Added "According to the IBM/Ponemon data" before the 61% classification stat |
| SLIDE 30 | Added "the IBM/Ponemon numbers" before the 33%/6% audit trail stats |

### 4. New Slide: "Every Control Has a Cost" (SLIDE 9b)

**Added:** A new slide visualizing the five tradeoffs of security controls, inserted after SLIDE 9 (The Blueprint Concept).

**Content:**
- Title: "Every Control Has a Cost"
- Subtitle: "Making tradeoffs deliberately, not accidentally"
- Five items: Latency, UX Friction, False Positives, Developer Overhead, Infrastructure Cost
- Key message: "The blueprint helps you make these tradeoffs deliberately." (teal)
- Slide number: 9b

**Script update:** New SLIDE 9b section added with ~100 words of spoken text walking through the five tradeoffs.

**Style:** Matches existing deck — Lato titles, Poppins body, red (#E74C3C) labels, teal (#16A085) accent.

### 5. Duplicate Examples Review

No problematic duplications found. Intentional repetitions serve distinct purposes:
- IBM/Ponemon statistics referenced in opening (slides 6-8) and revisited in later layers (slides 24, 30) — different context each time
- Chevy chatbot incident used as opening hook and briefly referenced in later context — different detail levels

### 6. Long List Split: Monday Morning Checklist

**Original:** Slide 51 — single slide with 8-item checklist
**Split into:**
- **Slide 51 (Part 1):** "Your Monday Morning Checklist (1 of 2)" — Foundation & Boundaries (items 1-4: Inventory, Service Identities, Tenant Boundaries, Prompt Filtering)
- **Slide 51b (Part 2):** "Your Monday Morning Checklist (2 of 2)" — Operations & Governance (items 5-8: Model Registry, Audit Logging, Kill Switches, RACI Ownership)

**Script update:** SLIDE 51 section split into SLIDE 51 and SLIDE 51b with expanded spoken text walking through each group of four items.

### 7. Connectors and Shapes Review

No disconnected connectors, arrows, or shapes found across all slides.

### 8. Text Overflow

No text overflow issues detected in original or modified slides.

### 9. Branding and Style

All changes preserve the existing deck style: font pairing (Lato/Poppins), color palette (teal #16A085, red #E74C3C, dark navy #011936, dark gray #343A40), slide number format, and layout patterns.

---

## Known Issues

1. **Slide 30 (Audit Trail Maturity Ladder):** Statistics "33% no trails / 6% comprehensive" are embedded in a PNG diagram image. Source attribution cannot be added via XML — the image would need to be regenerated externally.

2. **Slide 19:** Title text is white (for dark master background). Code text in content boxes was corrected back to dark — verified visually.

---

## File Inventory

| File | Location | Status |
|------|----------|--------|
| ai-security-blueprint_updated.pptx | blueprint/ | NEW — updated deck (60 slides) |
| ai-security-blueprint-script_updated.md | blueprint/ | NEW — updated script (60 SLIDE sections) |
| ai-security-blueprint-change-report.md | blueprint/ | NEW — this file |
| ai-security-blueprint.pptx | blueprint/ | ORIGINAL — unchanged |
| ai-security-blueprint-script.md | blueprint/ | ORIGINAL — unchanged |
