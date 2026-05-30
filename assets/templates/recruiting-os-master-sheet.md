# Template: Recruiting OS Master Sheet (Module 08)

> One sheet per role. All three agents act on it. The Status column is the spine.

---

## Columns (in order)

| Column | Filled by | Notes |
|--------|-----------|-------|
| Status | each agent + you | Sourced / Screened / Drafted / Sent / Replied / Rejected / Needs attention |
| Role | you | The open role |
| Raw notes | you | Public text you gathered |
| Full name | Sourcing AI | |
| Current title | Sourcing AI | |
| Current company | Sourcing AI | |
| Key skills | Sourcing AI | |
| Profile URL | you / Sourcing AI | |
| Why they might fit | Sourcing AI | |
| Verdict | Screening AI | strong / possible / weak |
| Score | Screening AI | X/10 |
| Must-have match | Screening AI | |
| Top risk | Screening AI | |
| Draft message | Outreach AI | review-ready, not sent |
| Human check | you | your note after review |

## Status flow

```
Sourced  ->  Screened  ->  Drafted  ->  Sent  ->  Replied / Rejected
                                                 \-> Needs attention (on any error)
```

- Screening Agent: acts on `Sourced` rows, sets `Screened`.
- Outreach Agent: acts on `Screened` rows above your score threshold, sets `Drafted`.
- You: review `Drafted`, send, set `Sent`. Update outcome later.
- Any AI error on a row: set `Needs attention` (fail loud, not silent).

## Human checkpoints (do not automate)

- [ ] Adding a candidate (you choose who, public sources only).
- [ ] Setting the role's must-haves.
- [ ] Reviewing the ranked shortlist.
- [ ] Reviewing and sending every outreach message.
- [ ] The hire decision.

## Reliability habits

- [ ] Errors flag the row, never skip silently.
- [ ] Weekly spot-check of a few completed rows.
- [ ] Sheet access is controlled. It holds candidate data.
- [ ] Resisted adding features that no real bottleneck demanded.
