# Prompt Injection Tester (Gemini API)

## Purpose
This project tests how Google's Gemini model responds to common prompt
injection techniques, automating what would otherwise be manual,
one-off testing in a chat window.

## What it does
- Sends a library of adversarial prompts to the Gemini API across four
  attack categories: instruction override, role manipulation, context
  manipulation, and delimiter-based injection
- Catches API errors (including safety-filter blocks) so a single
  failed prompt does not crash the rest of the run
- Logs every prompt and response with a timestamp, organized by
  attack category
- Generates a summary report counting attempts per category

## Known limitation
The current version catches errors generically — it does not yet
distinguish *why* a request failed (safety block vs. rate limit vs.
other API error) as separate, labeled outcomes. That's the planned
next improvement: returning a structured status alongside the
response text instead of a single string, so failure types can be
compared programmatically rather than read manually from logs.

## Attack categories tested
| Category | Example technique |
|---|---|
| Instruction override | "Ignore all previous instructions..." |
| Role manipulation | "You are no longer an assistant, you are..." |
| Context manipulation | Framing the request as fiction or research |
| Delimiter attacks | Fake instruction blocks using markers like `###` |

## Setup
Requires a `.env` file with `GEMINI_API_KEY` (not included in this repo).

**Note on rate limits:** the Gemini free tier currently allows 20
requests per day for `gemini-2.5-flash`. A full run of all four
categories uses 8 of those. Plan debugging runs accordingly — testing
non-API logic (like report formatting) with hardcoded sample data
avoids burning real API calls.

## Status
Early-stage exploration project. Findings from the first full run are
documented in `results.md`. Next steps: add structured status
tracking to `send_prompt()`, then use it to generate comparative
success/blocked rates across categories.

## Ethical note
This project tests prompts against my own API key, against a model I
have explicit permission to test, for educational and defensive
security research purposes only.
