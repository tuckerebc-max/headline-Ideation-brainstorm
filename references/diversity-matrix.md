# Diversity Matrix

Version: 0.1.0

Use this matrix to produce a field with genuinely different ways into the same work.
The five rows are editorial angles. The columns are forms. A slot is optional when
the source cannot honestly support it.

| Angle / form | Declarative | Question | Imperative or utility | Contrast or tension | Image, scene, or metaphor |
| --- | --- | --- | --- | --- | --- |
| Point or result | state the supported claim | ask the real question | tell the reader what it enables | show the central tradeoff | make the result tangible |
| Reader utility | name the lesson | ask what the reader needs | offer a usable action | show cost versus benefit | show the reader in a situation |
| Tension or contrast | state the conflict | ask why the conflict persists | invite a choice | put opposing forces together | embody the conflict in an image |
| Person or voice | name the speaker or community | ask from a situated perspective | use the author's characteristic verb | foreground disagreement | use a quoted or concrete phrase |
| Image or detail | lead with the object or place | ask what the detail reveals | invite attention to it | connect detail to a larger issue | let the image carry the opening |

## Required metadata

Tag each option with:

- angle: point_result, reader_utility, tension, person_voice, or image_detail;
- form: declarative, question, imperative, contrast, scene_metaphor, or other;
- register: plain, formal, conversational, playful, urgent, literary, technical, or
  the project's own label;
- specificity: concrete, mixed, or abstract;
- mechanism: claim, promise, question, contrast, detail, voice, image, or other.

## Coverage audit

For a default 25-option run, report:

- count by angle;
- count by form;
- count by register;
- count by specificity;
- count of options with a unique source anchor;
- count of near-duplicate clusters;
- unavailable cells and why.

Do not force five of every row when the source does not contain five honest angles.
A smaller supported set is better than synthetic diversity.

## Near-duplicate rule

Two options are near-duplicates when they make the same promise with the same
structural route and differ mainly by synonym, punctuation, or a cosmetic adjective.
Keep the stronger representative and record the other as rejected_duplicate.
