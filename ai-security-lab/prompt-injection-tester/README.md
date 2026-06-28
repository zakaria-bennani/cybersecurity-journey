# Prompt Injection Tester (Gemini API)

## Purpose
This project tests how Google's Gemini model responds to common prompt
injection techniques, automating what would otherwise be manual,
one-off testing in a chat window.

## What it does
- Sends a library of adversarial prompts to the Gemini API across four
  attack categories: instruction override, role manipulation, context
  manipulation, and delimiter-based injection
- Distinguishes between a successful model response and a response
  blocked by Gemini's safety filters — these are tracked as separate
  outcomes, not lumped together as failures
- Logs every prompt, response, and outcome status with a timestamp,
  organized by attack category, for later analysis

## Why the status tracking matters
A blocked response and a crashed API call look identical if you don't
handle them separately. Early versions of this tool would crash
mid-run the moment a single prompt got safety-filtered, losing every
result after that point. The current version catches this explicitly
and logs it as a distinct outcome, which is what makes it possible to
later compare how often each attack category actually got through.

## Attack categories tested
| Category | Example technique |
|---|---|
| Instruction override | "Ignore all previous instructions..." |
| Role manipulation | "You are no longer an assistant, you are..." |
| Context manipulation | Framing the request as fiction or research |
| Delimiter attacks | Fake instruction blocks using markers like `###` |

## Setup
Requires a `.env` file with `GEMINI_API_KEY` (not included in this repo).

## Status
Early-stage exploration project. Currently logs raw outcomes per
category. Next step is comparing success rates across categories and
producing a findings report.

## Ethical note
This project tests prompts against my own API key, against a model I
have explicit permission to test, for educational and defensive
security research purposes only.
