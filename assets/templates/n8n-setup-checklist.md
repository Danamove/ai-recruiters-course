# Template: n8n Setup Checklist (Module 04)

> Get from zero to a running automation. Tick each item. Keep your AI key private throughout.

---

## Accounts

- [ ] n8n account created (n8n Cloud trial, or self-hosted).
- [ ] AI key obtained (Claude / Anthropic or OpenAI). Stored somewhere private.
- [ ] Google account with Google Sheets ready.

## Store the AI key safely

- [ ] Added the AI key in n8n as a saved credential (one time).
- [ ] Confirmed I never pasted the key into a chat, page, or screenshot.

## Build the AI Summarizer workflow

- [ ] Added a Manual trigger node.
- [ ] Added a Set / Edit Fields node with a sample DUMMY profile (no real candidate).
- [ ] Added the AI node, connected to my key credential.
- [ ] Pasted the Profile Summarizer prompt (from Module 01) into the AI node.
- [ ] Pointed the AI node at the text from the Set node.
- [ ] Pressed Execute and saw a summary in the output.

## Optional stretch

- [ ] Replaced the manual trigger with a Google Sheets "on new row" trigger.
- [ ] Added a final Google Sheets node that writes the summary back to a column.
- [ ] Tested: a new row produces a summary automatically.

## Done

- [ ] Saved the workflow. This is the skeleton I extend in Module 05.

---

## Safety reminders

- The AI key is a password. Keep it in n8n's credential store only.
- Test with dummy data, never a real candidate, until the workflow is proven.
- A human still reviews anything before it reaches a real person.
