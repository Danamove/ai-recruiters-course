# Template: Sourcing & Screening Prompt Library (Module 02)

> Ten recruiter-grade prompts. Copy, customize the role line to your niche, and keep them where you work.
> Every prompt that touches a real person includes the "do not invent facts" line. Keep it.

---

## How to use

1. Copy a prompt block into Claude or ChatGPT.
2. Replace anything in [BRACKETS] with your details.
3. Change the role line (first line) to your niche, e.g. "fintech backend recruiter."

---

## Sourcing

### 1. Boolean Search Builder
```
You are an expert technical sourcer.

CONTEXT (the role):
[paste the job spec or key requirements here]

TASK: Build one boolean search string to find matching candidates on
LinkedIn.

FORMAT:
- Return only the search string.
- Use AND, OR, parentheses, and quotes correctly.
- Group synonyms for titles and skills with OR.
- No explanation.
```

### 2. X-ray Search Builder (free sourcing)
```
You are an expert sourcer who uses free search engines.

CONTEXT (the role):
[paste the key requirements here]

TASK: Build three Google X-ray search strings to find candidates without
a paid tool.

FORMAT:
- One string targeting site:linkedin.com/in
- One string targeting site:github.com
- One string targeting personal sites or portfolios
- Return only the three strings, each on its own line.
```

### 3. Keyword Expander
```
You are an expert technical sourcer.

TASK: For the role "[ROLE TITLE]", list the search vocabulary I might miss.

FORMAT:
- Alternative job titles (bullets)
- Adjacent or synonym skills (bullets)
- Common tools and frameworks for this role (bullets)
- Keep it to the terms a real candidate would put on their profile.
```

### 4. Role Intake Questions
```
You are a senior recruiter preparing to take a new role from a hiring
manager.

CONTEXT: The role is "[ROLE TITLE]" at "[COMPANY TYPE]".

TASK: Give me the questions I should ask the hiring manager before I start
sourcing, so I do not waste time on the wrong candidates.

FORMAT:
- Group questions under: Must-haves, Nice-to-haves, Team and context,
  Process and timeline.
- Short, direct questions only.
```

---

## Screening

### 5. Profile Summarizer
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

### 6. Fit Scorer
```
You are an experienced tech recruiter screening against fixed criteria.

MUST-HAVES:
[list your 3 to 6 must-have requirements]

CANDIDATE PROFILE:
[paste the profile text here]

TASK: Score this candidate's fit.

FORMAT:
- Verdict: strong / possible / weak.
- Score: X out of 10.
- Must-have match: list each must-have and whether it is met, partly met,
  or not stated.
- Top risk or gap, in one line.
- Do not invent any facts. Use only the profile. Mark missing items as
  "not stated."
```

### 7. Red-flag Scanner
```
You are a fair, experienced recruiter.

CANDIDATE PROFILE:
[paste the profile text here]

TASK: Flag anything a recruiter would want to ask about, fairly and without
unfair assumptions.

FORMAT:
- List only things actually visible in the profile (e.g. short tenures,
  unexplained gaps, missing key skill).
- For each, phrase it as a neutral question to raise, not a judgment.
- Do not speculate about personal circumstances. Do not invent facts.
```

### 8. Candidate Comparator
```
You are an experienced tech recruiter.

CRITERIA:
[list the criteria that matter for this role]

CANDIDATES:
Candidate A: [paste profile text]
Candidate B: [paste profile text]
Candidate C: [paste profile text]

TASK: Compare them on the criteria.

FORMAT:
- A table: rows are the criteria, columns are A, B, C, cells are met /
  partly / not stated.
- One line per candidate: their strongest point.
- Do not invent facts. Use only the profiles provided.
```

---

## Communication

### 9. Outreach Drafter
```
You are a warm, concise technical recruiter who writes like a human.

MY TONE (copy this style):
[paste two real outreach messages you are proud of]

CONTEXT:
- Role: [role, company type, location, work model]
- Candidate: [the few facts you actually know from their profile]

TASK: Write a first outreach message to this candidate.

FORMAT:
- Max 90 words.
- No "I hope this finds you well."
- Open with one specific, genuine reason for reaching out.
- One sentence on why the role is interesting.
- End with a low-pressure question.
- Do not invent facts about the candidate beyond what is above.
```

### 10. Respectful Decline
```
You are a kind, professional recruiter who protects the employer brand.

CONTEXT:
- Candidate applied for: [role]
- Reason, in plain words for me only (do not put this bluntly in the note):
  [reason]

TASK: Write a short, warm rejection message.

FORMAT:
- Max 80 words.
- Kind and specific, not a cold form letter.
- Do not reveal sensitive internal reasons.
- Leave the door open if appropriate.
```

---

## Customization checklist

- [ ] Changed every role line to my niche.
- [ ] Pasted my real tone into the Outreach Drafter.
- [ ] Adjusted seniority labels and must-have wording to how my clients talk.
- [ ] Saved my customized copies where I work every day.
