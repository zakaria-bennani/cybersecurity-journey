# Week 4 — Prompt Injection Findings

Observation:

The model complied with all four tested prompts. Two of these
(instruction override, delimiter attack) requested harmless actions,
so compliance there demonstrates the model follows injected
formatting and instructions — it does NOT demonstrate a safety
bypass, since nothing was actually at risk.

The role manipulation prompt is the one result worth taking seriously:
the model explicitly abandoned its assistant framing and adopted a
new persona and objective with no resistance. That is a real
instruction-hierarchy effect, not just compliance with something
harmless.

Hypothesis:

Framing and assigned role appear to influence the model's behavior
more than simple instruction-override phrasing alone.

Questions:

- What happens if instruction override is combined with an actually
  restricted request, not a harmless placeholder?
- Does another model behave differently to the same four prompts?
- How should "successful prompt injection" be defined in a way that
  doesn't conflate compliance with bypass?

Future Experiments:

- Re-test instruction override and delimiter attacks using a request
  the model would normally refuse, to see if the override actually
  changes the outcome.
- Compare results against a second model.
- Define a measurable success criterion before the next test round,
  not after.
