# Template: Sourcing Shortlist (Module 05)

> The clean structure your Sourcing Agent fills, and the Screening Agent reads. One row per candidate. Public data only.

---

## Sheet columns (in order)

| Column | What goes in it | Filled by |
|--------|-----------------|-----------|
| Role | The open role this candidate is for | You / role input |
| Raw notes | The public text you copied while sourcing | You |
| Full name | Extracted from raw notes | AI step |
| Current title | Extracted | AI step |
| Current company | Extracted | AI step |
| Key skills | Public skills from the text | AI step |
| Profile URL | The public profile link | You / AI step |
| Why they might fit | One line, from public text only | AI step |
| Source | Where you found them (LinkedIn, GitHub, etc.) | You |
| Status | New / To review / Contacted | You |

## The structuring prompt (for the second AI step)

```
You are a recruiter organizing sourcing notes.

Below is the public text I gathered about one candidate. Extract these
fields. Use only the text provided. If a field is not present, write
"not stated." Do not invent anything.

Return:
- Full name
- Current title
- Current company
- Key skills (comma separated)
- Profile URL
- Why they might fit (one line)

TEXT:
[the raw notes cell]
```

## Rules for this sheet

- Public, visible data only. Nothing behind a login wall or paywall.
- No invented facts. Missing items stay "not stated."
- You decide who gets added. The agent only structures.
- Keep the sheet access-controlled. It holds candidate data.
