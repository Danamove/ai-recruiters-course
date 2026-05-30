# Template: Candidate Profile Summarizer Prompt (Module 01)

> Your first reusable recruiting prompt. Run it by hand now. You will automate it in Module 06.

---

## The prompt

Copy everything in the block below into Claude or ChatGPT. Replace the
bracketed line with the candidate's public profile text.

```
You are an experienced tech recruiter.

Below is a candidate's public profile text. Summarize it for a hiring
manager in this exact format:

- One line: who they are and current role.
- Top 3 relevant strengths (bullets).
- Seniority estimate (junior / mid / senior / lead) and why, in one line.
- One thing that is unclear or worth asking about.

Do not invent any facts. Only use what is in the profile below. If
something is not stated, say "not stated."

PROFILE:
[paste the profile text here]
```

## How to run it

1. Open a real profile you are considering for an open role.
2. Copy the visible profile text.
3. Paste it where it says `[paste the profile text here]`.
4. Run, and read the output.

## Why it works (the four parts)

- **Role:** "You are an experienced tech recruiter" sets the lens.
- **Context:** the pasted profile is the only source it may use.
- **Task:** summarize for a hiring manager.
- **Format:** the exact bullet structure, so every run is comparable.

The "do not invent any facts" line is what keeps it honest. Keep that line in
every recruiting prompt where real people are involved.

## Make it yours

- Swap "tech recruiter" for your niche (e.g. "fintech engineering recruiter").
- Add a line: "Flag anything that suggests a fit or mismatch for a [ROLE] position."
- Tighten or loosen the seniority labels to match how your clients talk.

## Safety reminder

This prompt only summarizes text you provide. It must never be used to guess
contact details or facts not present in the profile. Facts and the decision to
contact a candidate stay with you.
