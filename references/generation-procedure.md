# Headline Generation Procedure

Version: 0.1.0

This procedure is deliberately split into a generative pass and an evaluative pass.
Do not select the first plausible line before the field has been diversified.

## Phase 0: Lock the brief

Create a brief record before writing options.

Required fields:

- source point and a one-sentence source summary;
- primary audience, secondary audience, and intended action;
- purpose: inform, explain, persuade, invite, report, teach, entertain, or other;
- genre and medium;
- verified display, search, email, social, or spoken constraints;
- voice signals and two or more source excerpts when available;
- must-preserve facts, names, terms, qualifiers, and numbers;
- prohibited claims or tones;
- open decisions.

If a field is unknown, mark it unknown. A missing fact is not an invitation to invent
one. If the underlying source is unavailable, the run may produce labeled raw ideas but
cannot release a screened shortlist.

## Phase 1: State the reader contract

Write three short sentences:

1. The reader is...
2. The work gives the reader...
3. The headline may promise..., but it may not promise...

This ties the headline to audience and purpose. It distinguishes the work's actual
payoff from a vague desire to sound compelling.

## Phase 2: Extract headlineable material

Build a source-point inventory:

- central claim or question;
- strongest concrete detail;
- useful tension, contrast, or tradeoff;
- named person, place, practice, or object;
- reader consequence or action;
- emotional or intellectual charge;
- scope and uncertainty qualifiers;
- words whose exact form protects meaning or voice.

Mark each item as explicit, supported inference, or unavailable. Only explicit or
supported items may appear as factual assertions in a released option. A metaphor can
be used only if it does not imply a false fact.

## Phase 3: Allocate the diversity field

Start with the 5 by 5 planning grid from references/diversity-matrix.md. The default
allocation is:

- 5 point/result options;
- 5 reader-utility options;
- 5 tension/contrast options;
- 5 voice/person options;
- 5 image/detail options.

Across those rows, vary forms such as declarative, question, imperative, contrast,
and scene/metaphor. Vary specificity, register, and rhetorical mechanism as the brief
permits. The grid is a coverage tool, not a quota that forces unsupported angles.

If the source cannot support an angle, mark the cell unavailable and replace it with
a second supported angle. Do not fabricate variety.

## Phase 4: Generate the raw field

Generate approximately 25 options without ranking. Label every option with:

- option_id;
- angle;
- form;
- register;
- specificity;
- mechanism;
- length in characters and words;
- source anchors;
- any deliberate tradeoff.

Good mechanisms include a concrete detail, a clear promise, a contrast, a question
that the work actually answers, a useful imperative, or an authorial phrase. Avoid
synonym-only variation. Keep raw options even when they are later rejected.

## Phase 5: Normalize and deduplicate

Normalize case, whitespace, punctuation, and leading determiners for comparison.
Flag near-duplicates using shared content words and identical syntax. Retain one
representative when two lines make the same promise. A line is not diverse merely
because it swaps "important" for "essential."

Do not normalize away intentional voice, dialect, or punctuation in the released
headline. Normalization is only for comparison.

## Phase 6: Run the anti-slop screen

Apply every check in references/anti-slop-checklist.md. A flag is a prompt for
contextual judgment, not a mechanical banned-word filter. Repair a promising line
when the problem is local; reject it when the framing is structurally generic,
inflated, deceptive, or voice-mismatched.

The screen must specifically ask:

- Is the line concrete enough for this source?
- Does it promise what the work delivers?
- Is the energy earned by the material?
- Would this phrasing sound like the author?
- Is the information gap productive or deceptive?
- Is the line generic because it could title thousands of unrelated works?
- Is a keyword repeated for people or merely for search machinery?

## Phase 7: Score and gate

Use the quality rubric. Record dimension scores, evidence, and critical gates for
each survivor. Do not use an average to rescue a failure in accuracy, promise fit,
audience-purpose fit, genre-medium fit, or voice fidelity.

Default release guidance:

- ready: no critical gate failure and weighted score at least 3.2;
- ready_with_conditions: no critical gate failure, score 2.8-3.19, and named
  decision hooks or revision conditions;
- hold: source or policy evidence is insufficient;
- reject: a critical gate fails or the line is deceptive, unsupported, or clearly
  voice-mismatched.

## Phase 8: Select and explain

Return 3-5 finalists unless the brief calls for another number. Rank by fit, not by
novelty alone. For each finalist give:

- why it works for this audience, purpose, genre, and medium;
- the source anchor that earns the wording;
- the principal tradeoff;
- any subtitle, display, or platform condition;
- the smallest next revision if one is needed.

The explanation should help an author choose. It should not pretend that a numeric
score is an objective truth.

## Phase 9: Release audit

Before returning the package:

- confirm the headline does not add unsupported facts or certainty;
- confirm all must-preserve terms and qualifiers are intact;
- confirm the field has meaningful variety;
- confirm the medium constraint is verified or marked unverified;
- confirm anti-slop flags have dispositions;
- confirm rejected lines and reasons are retained;
- confirm any open decision is named;
- set status to ready, ready_with_conditions, needs_input, or hold.

## When fewer than 25 is correct

Return fewer than 25 when the source is too narrow, the audience constraints are
tight, the author requests a smaller set, or further options would be dishonest
synonym swaps. State the reason and show the unavailable diversity cells. Quantity is
a target, not permission to lower the accuracy or voice standard.
