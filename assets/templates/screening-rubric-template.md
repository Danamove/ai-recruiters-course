# Template: Screening Rubric (Module 06)

> Define the criteria once, score consistently. Score the skills, not the person.

---

## Role criteria

**Role:** ____________________

**Must-haves (3 to 6, these decide fit):**
1. ____________________
2. ____________________
3. ____________________
4. ____________________

**Nice-to-haves (do not gate on these):**
- ____________________
- ____________________

**Off-limits (never score on these):** name, age, gender, photo, nationality, background, anything not about the work.

---

## The scoring prompt (for the AI step)

```
You are an experienced tech recruiter screening against fixed criteria.

MUST-HAVES:
[paste the must-haves above]

CANDIDATE (structured fields):
[the candidate's row: title, company, skills, etc.]

TASK: Score this candidate's fit. Score only on the must-haves. Do not
consider name, age, background, or anything not about the work.

FORMAT (return exactly this, same order every time):
- Verdict: strong / possible / weak
- Score: X/10
- Must-have match: each must-have -> met / partly met / not stated
- Top risk or gap: one line

Use only the provided data. Mark missing items "not stated." Do not invent.
```

## Output columns to add to the shortlist

| Column | Value |
|--------|-------|
| Verdict | strong / possible / weak |
| Score | X/10 |
| Must-have match | per-criterion result |
| Top risk | one line |
| Human check | your note after review |

## Review habits

- [ ] Sorted by score, highest first.
- [ ] Spot-checked the reasons behind the top scores, not just the numbers.
- [ ] Checked a few low scores for unfair "not stated" penalties.
- [ ] Confirmed scoring used job-relevant criteria only.
