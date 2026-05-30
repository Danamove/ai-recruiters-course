# AI Agents for Tech Recruiters — course site (MVP)

Static course player for the "AI Agents for Tech Recruiters & Headhunters" course.
A learner opens the link, picks a module, hears **Ada** (the AI host voice), reads the
lesson, and opens the matching slide deck. Learner-paced: no payments, no accounts.

**Live:** GitHub Pages (see repo settings).

## How it works

- `index.html` / `styles.css` / `app.js` — the player. Vanilla JS, no framework, no build step at runtime.
- `data/modules.js` — generated module data (`window.MODULES`): title, Gamma deck URL, Ada audio path, lesson HTML, take-home template, optional slide images.
- `assets/audio/` — the ten Ada narration MP3s.
- `assets/templates/` — the take-home templates.
- `assets/slides/module-NN/` — optional. Drop exported slide images here (PNG/JPG) and that module shows an inline slideshow instead of the "Open in Gamma" button.

## Rebuilding the data

The data and assets are generated from the course content one folder up
(`../modules`, `../production/audio`, `../templates`):

```bash
pip install markdown
python build.py
```

Re-run after editing any lesson, narration audio, or after exporting slide images.

## Inline slides

Gamma decks cannot be iframe-embedded (`X-Frame-Options: SAMEORIGIN`), so slides are rendered as native inline HTML.

- `data/gamma-raw/module-NN.html` — each deck's content, saved from Gamma's `read_gamma`.
- `build-slides.py` — parses those into `data/slides.js` (`window.SLIDES`). Needs `pip install beautifulsoup4`.
- The player shows a prev/next slideshow per module. Images are hotlinked from Gamma's public CDN.

To refresh a deck after editing it in Gamma: re-pull its content into the matching `data/gamma-raw/module-NN.html`, then `python build-slides.py`.

## Known MVP limits

- Slides are learner-advanced, not auto-synced to the audio.
- Slide images are hotlinked from Gamma's CDN; if Gamma removes them, re-pull the decks.
