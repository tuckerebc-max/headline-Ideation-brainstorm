# Headline Ideation Skill Specification

Version: 0.1.0
Status: draft-for-editorial-review
Package: headline-ideation
Design authority: this specification, with cited external guidance recorded in references/research-basis.md.

## 1. Purpose

Provide a repeatable, evidence-aware method for generating and evaluating a field of
approximately 25 headline options. The method must improve the chance of finding a
strong headline without turning headline work into a click-optimization exercise or
flattening the author's voice.

The package is designed for article headlines, essays, reports, newsletters, talks,
landing pages, social posts, and related title-like framing. It supports a title and
subtitle relationship but does not silently rewrite the underlying work.

## 2. Core proposition

A quality headline makes an honest, useful promise about the work and makes a
specific reader want to spend attention. A strong option is not necessarily the
shortest, loudest, most searchable, or most familiar. The skill therefore separates:

- ideation from selection;
- attraction from accuracy;
- curiosity from deception;
- diversity from arbitrary novelty;
- platform fit from universal rules;
- editorial judgment from unresolved project policy.

## 3. Required input

A run must identify:

- source point: the article, talk, report, post, or brief being titled;
- audience and intended reader action;
- purpose and genre;
- medium, placement, and any verified length or display constraints;
- author voice signals, including examples when available;
- claims, names, terms, numbers, and qualifiers that must be preserved;
- prohibited claims or topics, tones, or words;
- whether SEO, search, accessibility, or translation requirements apply.

If source content is unavailable or the brief cannot support factual screening, return
needs_input or hold. Do not infer material facts from a title request alone.

## 4. Required output

Return:

- approximately 25 raw and screened options, or a smaller justified set;
- option metadata for angle, form, register, specificity, mechanism, and length;
- quality scores and critical-gate results;
- diversity coverage and duplicate analysis;
- anti-slop flags and disposition;
- a 3-5 option shortlist with tradeoffs and rationale;
- assumptions, unresolved decision hooks, and release status.

The raw field, rejected options, and rejection reasons are retained for auditability.

## 5. Operating rules

1. Every option must be traceable to the source point and brief.
2. No option may add unsupported facts, certainty, causality, scale, or urgency.
3. Options must differ by meaningful editorial angle, not only synonym swaps.
4. The field should contain multiple forms and registers when the brief permits.
5. A critical gate failure is a release failure, regardless of aggregate score.
6. Curiosity is allowed only when the promised information and reader payoff are
   honest and the work delivers them.
7. The author's voice is a protected input. Improvement is not permission to
   replace diction, humor, rhythm, cultural references, or point of view.
8. Medium constraints are configuration. The skill does not invent current limits.
9. Unsupported platform, SEO, legal, safety, or sensitivity decisions are escalated.
10. The final selection belongs to the author or editor, not the scorer.

## 6. Quality model

The default weighted dimensions are:

- accuracy and promise fit: 25%;
- audience and purpose fit: 15%;
- genre and medium fit: 10%;
- clarity and scanability: 15%;
- specificity and reader value: 15%;
- voice fidelity: 10%;
- distinctiveness: 5%;
- energy and memorability: 5%.

Score each dimension from 0 to 4. Apply the hard gates in the rubric before ranking.
Weights and thresholds can be changed only through a versioned project decision hook.

## 7. Boundaries

In scope: ideation, contrastive diversity, headline-level accuracy, voice calibration,
medium adaptation, anti-slop screening, explanation, and regression capture.

Out of scope: rewriting the source, fact-checking the entire work, deciding editorial
policy for a publication, guaranteeing search ranking or engagement, legal clearance,
translation quality, or replacing an author/editor's final judgment.

## 8. Formal contracts

Input and output data are defined in schemas/. Rules and unresolved decisions are
defined in RULES/. Evals/ contains synthetic fixtures and a scorer. Production
failures are captured under CHANGELOG_REGRESSION/. The package is self-contained and
does not require network access at run time.

## 9. Release criteria

A release candidate must:

- pass scripts/validate_package.py;
- pass evals/scorer.py --validate-suite --self-test;
- compile both Python scripts;
- contain a unique crosswalk row for every rule;
- show all five fixture classes;
- pass all zero-tolerance fixtures;
- disclose unverified medium limits and unresolved project decisions;
- preserve provenance for research claims and external guidance.

## 10. Open decisions

The following are intentionally not silently resolved:

- target length and truncation behavior by medium;
- SEO term priority versus natural language;
- whether a subtitle is available and how much it may carry;
- allowable rhetorical risk for sensitive or high-stakes topics;
- local policy on questions, imperatives, title case, punctuation, and numerals;
- accessibility, localization, and translation constraints;
- whether a publication uses a separate search title and display title.
