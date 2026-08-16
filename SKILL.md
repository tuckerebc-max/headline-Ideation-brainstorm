---
name: headline-ideation
description: Generate and evaluate approximately 25 accurate, distinctive, voice-preserving headlines for a defined audience, purpose, genre, and medium. Use for article headlines, essay titles, newsletter subject lines, talks, reports, landing pages, social posts, and other headline-like framing. Separate wide ideation from evidence-based screening, enforce diversity, detect AI-slop and clickbait patterns, adapt to medium constraints, and explain the shortlist. Do not invent facts, optimize for clicks alone, flatten the author's voice, or treat a generic formula as a quality standard.
---

# Headline Ideation

Treat headline work as two different jobs: generate a wide field of materially different possibilities, then screen and refine them against the brief. The headline is a promise about the reader's experience, not a baited gap between the headline and the work.

## Run

1. Load and validate schemas/headline-input.schema.json. Lock the source
   point, audience, purpose, genre, medium, voice, hard constraints, and the
   facts or words that must be preserved. If a required brief element is
   missing, state the assumption or return needs_input; never fill the gap from
   model memory.
2. Read references/generation-procedure.md and use the diversity matrix. Aim
   for 25 options, with each option tagged by angle, form, register,
   specificity, and mechanism. Produce the raw field before selecting winners.
3. Apply references/anti-slop-checklist.md to the raw field. Remove or rewrite
   formulaic, generic, inflated, keyword-stuffed, false-urgency, and
   voice-mismatched options. Do not ban a word mechanically when the subject
   requires it; judge the phrase in context.
4. Score survivors with references/quality-rubric.md. Accuracy/promise fit,
   audience-purpose fit, genre/medium fit, specificity, voice, clarity,
   distinctiveness, and energy are separate dimensions. A critical gate
   failure cannot be rescued by a high aggregate score.
5. Return a validated result using schemas/output.schema.json: the full
   option set, diversity audit, rubric scores, rejected options with reasons,
   a 3-5 item shortlist, and a brief explanation of why each selected option
   works and what tradeoff it carries.
6. Preserve the author's diction, rhythm, humor, formality, and point of view.
   Route unresolved length/platform limits, factual certainty, sensitive-topic
   framing, SEO terms, title/subtitle relations, and acceptable rhetorical risk
   through the decision hooks in RULES/decision_hooks.json.

## Quality gates

- Do not state a fact, result, causation, scale, or certainty that the source
  does not support.
- Do not use mystery, outrage, or curiosity as a substitute for a clear reason
  to read. Curiosity is acceptable only when the headline remains honest about
  the work.
- Do not submit 25 near-duplicates. If the brief cannot support 25 honest
  options, return fewer and explain the constraint.
- Do not silently apply current platform character limits; use supplied medium
  constraints or mark them UNVERIFIED.
- Do not discard the raw field or rejected options before recording the reason.

## Output

Invoke as $headline-ideation. Return the requested headline set, a ranked
shortlist, scores, diversity and anti-slop checks, assumptions, and unresolved
decisions. Use ready, ready_with_conditions, needs_input, or hold as the
top-level status. The skill creates options and evidence-backed judgments; the
author or editor owns the final choice.
