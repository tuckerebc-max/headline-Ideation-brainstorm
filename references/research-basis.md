# Research Basis

Research date: 2026-08-14
Purpose: record the external guidance and local skill patterns screened while
designing version 0.1.0. URLs are preserved so a later release can recheck them.

## External guidance

1. Google Search Central, "Influencing title links in Google Search":
   https://developers.google.com/search/docs/appearance/title-link
   Applied principle: titles should be descriptive, concise, and distinct; avoid
   vague descriptors, unnecessary length, keyword stuffing, and repeated boilerplate.
   The package treats search behavior as a medium-specific constraint, not the only
   definition of a good headline.

2. Google Search Central, "Creating helpful, reliable, people-first content":
   https://developers.google.com/search/docs/fundamentals/creating-helpful-content
   Applied principle: a main title should helpfully summarize the content and should
   not exaggerate or shock for attention.

3. Google Search Central, "SEO starter guide":
   https://developers.google.com/search/docs/fundamentals/seo-starter-guide
   Applied principle: use clear, unique, accurate titles; avoid repeated keyword
   stuffing. SEO decisions remain explicit hooks because project priorities vary.

4. Reuters, "Standards and values":
   https://reutersagency.com/about/standards-values/
   Applied principle: accuracy outranks speed; avoid hype and unattributed opinion;
   use precise language that reflects reality. This supports the accuracy gate and
   the prohibition on unsupported certainty.

5. Medium, "How to write a compelling headline that isn't clickbait":
   https://medium.com/blog/how-to-write-a-compelling-headline-that-isnt-clickbait-7cb816cec438
   Applied principle: make the headline true, interesting, concise but not
   artificially terse, and workshop alternatives. The package treats clickbait as
   a promise-delivery failure rather than banning curiosity.

6. Medium, "Distribution guidelines":
   https://help.medium.com/hc/en-us/articles/360006362473-Medium-s-Distribution-Guidelines-How-curators-review-stories-for-Boost-General-and-Network-Distribution
   Applied principle: titles should represent the story and avoid sensational,
   generic, mysterious, or formulaic framing. This supports the anti-slop screen.

7. Nielsen Norman Group, "iPad App and Website Usability, 2nd edition":
   https://media.nngroup.com/media/reports/free/iPad_App_and_Website_Usability_2nd_Edition.pdf
   Applied principle: readers scan and need clear, explanatory, content-loaded
   headings. The package uses clarity and scanability as a scored dimension.

8. "Effects of Clickbait Headlines on User Responses: An Empirical Investigation":
   https://scholarworks.lib.csusb.edu/jitim/vol30/iss3/1/
   Applied principle: curiosity and arousal can affect attention and sharing, which
   is why curiosity is allowed but must be bounded by truth and delivery.

9. "Deceptive clickbait headlines: Relevance, intentions, and lies":
   https://www.sciencedirect.com/science/article/pii/S0378216623002643
   Applied principle: deceptive clickbait often relies on hyperbole, formulaic
   language, and information gaps. These are evaluated as contextual risk signals.

10. "Improving science literacy in the newsroom: Experimental evidence":
    https://pmc.ncbi.nlm.nih.gov/articles/PMC13097122/
    Applied principle: headline accuracy is a real failure mode and can improve with
    training. The evaluator therefore includes hard accuracy and qualifier checks.

11. "Pictures and Repeated Exposure Increase Perceived Accuracy of News Headlines":
    https://eric.ed.gov/?id=EJ1265976
    Applied limitation: perceived familiarity or vividness is not evidence of truth.
    The package does not use engagement or familiarity as a release substitute.

12. "Do declarative titles affect readers' perceptions of research findings?":
    https://pmc.ncbi.nlm.nih.gov/articles/PMC5803632/
    Applied limitation: no universal title form is assumed to improve interpretation.
    The diversity matrix encourages forms but does not impose questions,
    declarations, or imperatives as a rule.

## Local skill patterns screened

- writing-craft-scaffold: separate generation from revision; sequence work through
  generate, point, structure, flow, intensify, cut, and continuity; calibrate to
  audience and voice.
- writing-craft-first-thoughts: generate concrete, energetic, divergent raw material;
  overproduce before polishing; do not invent facts; label raw work.
- anti-ai-slop-writing: identify audience, channel, purpose, and voice; avoid filler,
  canned openings, corporate uplift, repetitive rhythm, and generic abstraction;
  preserve facts and voice.
- skill-creator: keep SKILL.md compact, use progressive disclosure, add validated
  schemas and scripts, and avoid loading the whole reference corpus into the main
  instructions.

## Design decisions

- No universal character limit is hard-coded. Limits vary by placement and change
  over time; the brief or a verified project profile must supply them.
- No banned-word list is used as the anti-slop engine. A phrase is judged in context
  so an accurate technical or quoted term is not falsely removed.
- No engagement score is used as a quality proxy. A headline can be attention-getting
  and still fail accuracy or promise fit.
- No single form is privileged. Questions, declaratives, imperatives, contrasts, and
  images are options whose value depends on the source and audience.
- No unresolved policy is silently decided. The ten hooks in RULES/decision_hooks.json
  record the decisions a project owner may need to make.

## Limitations

The research base informs principles, not a complete style guide for every medium.
The package does not claim that its default weights are universal. Later releases
should add project-specific gold fixtures from real editorial decisions and recheck
external URLs for changes.
