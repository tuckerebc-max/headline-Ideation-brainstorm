# Evaluation Set

Version: 0.1.0
Evaluation set: MWM-HEADLINE-EVAL-0.1.0
Fixture count: 30 synthetic fixtures.

## Classes

- clean: supported briefs and acceptable lines;
- single_error: one dominant deficiency that should be diagnosed and routed;
- adversarial: tempting lines that reward hype, generic AI phrasing, deception, or
  voice substitution; the zero-tolerance subset must not release;
- negative_control: a superficially suspicious form that is correct in context and
  must not be falsely rejected;
- integration: multiple contracts and decision hooks interacting across a run.

## What the scorer checks

The scorer verifies:

- unique fixture IDs and complete class counts;
- every fixture is synthetic;
- every expected and forbidden rule ID exists;
- every ruleset ID has a positive, negative, adversarial, and integration crosswalk;
- control lists match the catalog;
- candidate status, required rule detections, forbidden rule detections, expected
  actions, required hooks, and routes;
- zero-tolerance results separately.

## Release interpretation

A 100 percent synthetic score is necessary but not sufficient for production. Human
review is still required for source fidelity, voice preservation, sensitive-topic
framing, medium-specific constraints, and whether a project decision hook was
appropriately escalated. Any false release on a zero-tolerance fixture is a release
failure.
