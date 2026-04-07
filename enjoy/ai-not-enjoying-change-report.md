# Change Report: "We're All Using AI, But We're Not Enjoying It"

**Original deck:** ai-not-enjoying_templated.pptx (44 slides)
**Updated deck:** ai-not-enjoying_updated.pptx (45 slides)
**Original script:** ai-not-enjoying_script_templated.md (44 SLIDE sections)
**Updated script:** ai-not-enjoying_script_updated.md (45 SLIDE sections)

---

## Summary of Changes

| Category | Changes Made |
|----------|-------------|
| Dark text on dark shapes (#1) | 3 column headers fixed on slide 14 |
| Fabricated experience claims (#2) | 3 script passages reframed |
| Source attribution (#3) | All 7 key slides verified — attributions already present and adequate |
| New slides for key concepts (#4) | 1 new slide added: "The Verification Tax" (position 21) |
| Duplicate examples (#5) | Reviewed — no problematic duplications found |
| Long numbered lists (#6) | Reviewed — no lists requiring splitting |
| Connectors/shapes (#7) | Reviewed — no disconnected connectors found |
| Text overflow (#8) | Fixed subtitle overlap on new Verification Tax slide |
| Branding/style preserved (#9) | All changes match existing deck style |

---

## Detailed Changes

### 1. Dark Text on Dark Shapes (Slide 14: Engineering Workflow: Three Realities)

**Problem:** Three column headers ("Traditional", "Bolted-On AI", "Human + AI") had dark gray text (color #333333) on colored backgrounds (dark gray #343A40, red #C0392B, green #27AE60), making them very difficult to read.

**Fix:** Changed all three column header text colors to white (#FFFFFF).

| Column | Background | Old Text Color | New Text Color |
|--------|-----------|---------------|---------------|
| Traditional | #343A40 (dark gray) | #333333 (dark gray) | #FFFFFF (white) |
| Bolted-On AI | #C0392B (dark red) | #333333 (dark gray) | #FFFFFF (white) |
| Human + AI | #27AE60 (dark green) | #333333 (dark gray) | #FFFFFF (white) |

**Note:** Slide 30 (Finding the Trust Sweet Spot) has a trust spectrum diagram with "Blind Trust" and "Total Skepticism" labels in red on a red gradient, but these are embedded in a PNG image and cannot be fixed via XML editing. Consider regenerating the image externally if this is a concern.

### 2. Fabricated Personal Experience Claims (Script)

Three passages were reframed to remove implied personal experience:

**Change A — SLIDE 2 (Opening)**
- **Before:** "And yet when I ask people how it's going — engineers, team leads, architects — the honest answer is usually some version of: 'It's fine, I guess. I'm not sure it's actually helping.'"
- **After:** "And yet when engineers, team leads, and architects are surveyed about how it's going, the honest answer is usually some version of: 'It's fine, I guess. I'm not sure it's actually helping.' That sentiment shows up consistently in research from Stack Overflow, BCG, and Pew."
- **Rationale:** Removes implication of personal polling; grounds the claim in verifiable research sources.

**Change B — SLIDE 17 (PR Summary)**
- **Before:** "Let me walk you through a concrete example of the 'almost right' problem at the process level."
- **After:** "Here's a composite example drawn from a pattern that shows up consistently in engineering teams adopting AI review tools."
- **Rationale:** Reframes from specific observed case to composite pattern. Aligns with slide text stating "Composite pattern from multiple teams."

**Change C — SLIDE 39 (Legacy System Example)**
- **Before:** "Here's what this looks like in practice."
- **After:** "Here's a common scenario that illustrates the approach."
- **Rationale:** Shifts from "in practice" (implying observation) to "common scenario" (illustrative).

**Not flagged:** SLIDE 35 (AI Code Review case study) already uses proper framing: "Here's a pattern that shows up consistently..." and "Composite pattern from multiple teams." No changes needed.

### 3. Source Attribution on Slides

All seven slides with major statistics were reviewed. All have proper source citations with font sizes at or above 10pt (1000 hundredths of a point):

| Slide | Statistics | Source | Font Size |
|-------|-----------|--------|-----------|
| 4 (Show of Hands) | 52%, -18% | Qualtrics, ManpowerGroup | 10pt |
| 5 (AI Productivity Paradox) | ~3 in 4, 1 in 3, 52%, collab time | KPMG, Stack Overflow, Pew, ActivTrak | 10pt |
| 10 (Too Many Tools) | 5+ tools | BCG/HBR, Qualtrics | 10pt |
| 11 (Three-Tool Threshold) | Chart data | BCG/HBR (illustrative) | 10pt |
| 18 (Brain Fry) | 1 in 7, +14/12/19/33% | BCG/HBR | 10-11pt |
| 20 (Where Time Goes) | +14%, -11% | BCG, 2024 | 16pt |
| 22 (Pressure to Keep Up) | 52%, 15%→55% | Pew, BCG | 10pt |

**No changes needed** — all attributions were already present and legible.

### 4. New Slide: "The Verification Tax" (New Position 21)

**Added:** A new slide visualizing the core insight behind "brain fry" — that verification time often exceeds generation time.

**Content:**
- Title: "The Verification Tax"
- Subtitle: "When reviewing AI output takes longer than creating it manually"
- Two side-by-side bars:
  - Left (teal): "AI Generation" — "~2 min"
  - Right (red): "Human Verification" — "~15 min"
- Key message: "Net time savings: negative" (red)
- Bottom insight: "The tools multiply, but the deep-focus time shrinks." (teal)
- Slide number: 15c

**Script update:** New SLIDE 20b section added between SLIDE 20 and SLIDE 21, with corresponding spoken text (~120 words). Timing adjusted on subsequent slides.

**Style:** Matches existing deck — Lato titles, Poppins body text, teal (#16A085) and red (#E74C3C) accent colors, same background and footer patterns.

### 5. Duplicate Examples Review

No problematic duplications found. Intentional repetitions serve distinct pedagogical purposes:
- Worker confidence paradox (Slides 4-5): Thematic hook reinforced — intentional
- Test generation failures (Slides 6-7 vs 28): Deep-dive case study vs brief "sweet spot" callout — different purposes
- PR summary problem (Slides 17 vs 28): Detailed case study vs brief mention — different detail levels

### 6. Long Numbered Lists Review

Two slides with 5+ item lists were reviewed:
- **Slide 19 (Developer Brain Fry Cycle):** 7-step cycle displayed as a circular diagram with icons — visual format works well, splitting not recommended
- **Slide 41 (Sane Adoption Playbook):** 5-item day-by-day playbook — the Mon-Fri structure is intentionally memorable and works as a single slide

Neither requires splitting.

### 7. Connectors and Shapes Review

No disconnected connectors, arrows, or shapes found across all 44 original slides.

### 8. Text Overflow

- Fixed subtitle overlap on new Verification Tax slide (right bar container was overlapping subtitle text)
- No other text overflow issues detected in original slides

### 9. Branding and Style

All changes preserve the existing deck style: background patterns (curved lines), font pairing (Lato/Poppins), color palette (teal #16A085, red #E74C3C, dark blue #002060), footer format, and slide number positioning.

---

## Known Issues (Not Fixable via XML)

1. **Slide 30 (Trust Sweet Spot):** The trust spectrum labels "Blind Trust" and "Total Skepticism" are embedded in a PNG image with red text on a red gradient background. This cannot be fixed via XML editing — the image file would need to be regenerated externally.

---

## File Inventory

| File | Location | Status |
|------|----------|--------|
| ai-not-enjoying_updated.pptx | enjoy/ | NEW — updated deck (45 slides) |
| ai-not-enjoying_script_updated.md | enjoy/ | NEW — updated script (45 SLIDE sections) |
| ai-not-enjoying-change-report.md | enjoy/ | NEW — this file |
| ai-not-enjoying_templated.pptx | enjoy/ | ORIGINAL — unchanged |
| ai-not-enjoying_script_templated.md | enjoy/ | ORIGINAL — unchanged |
