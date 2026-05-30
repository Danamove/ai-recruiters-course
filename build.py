#!/usr/bin/env python3
"""
Build the static course site data and copy assets.

Reads the course content (modules/NN-*/lesson.md, production/audio/*.mp3, templates/)
and writes:
  site/assets/addedvalue-logo.png
  site/assets/audio/module-NN-ada.mp3
  site/assets/templates/*.md
  site/data/modules.js   ->  window.MODULES = [...]

Slides: if site/assets/slides/module-NN/ holds images, they are listed (inline
slideshow). Otherwise the player shows an "Open in Gamma" button. Re-run any time
content changes:  python site/build.py
"""
import os, json, glob, shutil, re

SITE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SITE)                       # course root
LOGO_SRC = r"C:/Users/USER/OneDrive/Sourcy-Academy/sourcy-academy/addedvalue-logo.png"

import markdown

# num, folder, title, gamma deck id
MODULES = [
    ("00", "00-welcome",                    "Welcome & What You'll Build",         "u83urwlw059ji3s"),
    ("01", "01-ai-foundations",             "AI Foundations for Recruiters",       "16gmnhynfid7ltm"),
    ("02", "02-prompting",                  "Prompting for Sourcing & Screening",  "bb1wt3wpzdb709j"),
    ("03", "03-workflow-vs-agent",          "Workflow vs Agent",                   "larp1nzrbt26k9a"),
    ("04", "04-toolkit-first-automation",   "Your Toolkit & First Automation",     "u5sllb0ybdgcpl5"),
    ("05", "05-build-sourcing-agent",       "Build 1: The Sourcing Agent",         "cpx8ndv9wdapvcv"),
    ("06", "06-build-screening-agent",      "Build 2: The Screening Agent",        "omrzsnl7rdee71a"),
    ("07", "07-build-outreach-agent",       "Build 3: The Outreach Agent",         "ur8icyekx3uxzk3"),
    ("08", "08-recruiting-operating-system","Your Recruiting Operating System",    "jgrwmfi72qeoces"),
    ("09", "09-responsible-ai-making-it-pay","Responsible AI & Making It Pay",     "sk2t5bbrcvcw6dg"),
]

def ensure(d):
    os.makedirs(d, exist_ok=True)

def template_for(num, folder):
    """Pick the take-home template by scanning lesson.md/script.md for a templates/*.md mention."""
    tdir = os.path.join(ROOT, "templates")
    names = [os.path.basename(p) for p in glob.glob(os.path.join(tdir, "*.md"))]
    text = ""
    for fn in ("lesson.md", "script.md"):
        p = os.path.join(ROOT, "modules", folder, fn)
        if os.path.isfile(p):
            text += open(p, encoding="utf-8").read()
    hits = [n for n in names if n in text]
    return hits[0] if len(hits) >= 1 else None

def pretty(fname):
    stem = re.sub(r"\.md$", "", fname)
    return stem.replace("-", " ").replace("_", " ").title()

def main():
    ensure(os.path.join(SITE, "assets"))
    ensure(os.path.join(SITE, "assets", "audio"))
    ensure(os.path.join(SITE, "assets", "templates"))
    ensure(os.path.join(SITE, "assets", "slides"))
    ensure(os.path.join(SITE, "data"))

    # logo
    if os.path.isfile(LOGO_SRC):
        shutil.copyfile(LOGO_SRC, os.path.join(SITE, "assets", "addedvalue-logo.png"))
    else:
        print("WARN: logo not found at", LOGO_SRC)

    # templates (copy all, linked per module)
    for p in glob.glob(os.path.join(ROOT, "templates", "*.md")):
        shutil.copyfile(p, os.path.join(SITE, "assets", "templates", os.path.basename(p)))

    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc"])

    out = []
    for num, folder, title, gamma in MODULES:
        # audio
        audio_src = os.path.join(ROOT, "production", "audio", "module-%s-ada.mp3" % num)
        audio_rel = "assets/audio/module-%s-ada.mp3" % num
        if os.path.isfile(audio_src):
            shutil.copyfile(audio_src, os.path.join(SITE, audio_rel))
        else:
            print("WARN: missing audio for module", num)

        # lesson -> html
        lesson_p = os.path.join(ROOT, "modules", folder, "lesson.md")
        lesson_html = ""
        if os.path.isfile(lesson_p):
            md.reset()
            lesson_html = md.convert(open(lesson_p, encoding="utf-8").read())

        # slides (inline if exported)
        slide_dir = os.path.join(SITE, "assets", "slides", "module-%s" % num)
        slides = []
        if os.path.isdir(slide_dir):
            imgs = sorted(glob.glob(os.path.join(slide_dir, "*.png")) +
                          glob.glob(os.path.join(slide_dir, "*.jpg")) +
                          glob.glob(os.path.join(slide_dir, "*.jpeg")))
            slides = ["assets/slides/module-%s/%s" % (num, os.path.basename(i)) for i in imgs]

        # take-home template
        tfile = template_for(num, folder)
        template = None
        if tfile:
            template = {"name": pretty(tfile), "url": "assets/templates/%s" % tfile}

        out.append({
            "num": num,
            "title": title,
            "gammaUrl": "https://gamma.app/docs/%s" % gamma,
            "audio": audio_rel,
            "slides": slides,
            "template": template,
            "lessonHtml": lesson_html,
        })

    data = "window.MODULES = " + json.dumps(out, ensure_ascii=False, indent=2) + ";\n"
    with open(os.path.join(SITE, "data", "modules.js"), "w", encoding="utf-8") as f:
        f.write(data)

    print("Built %d modules." % len(out))
    for m in out:
        print("  module %s  audio=%s  slides=%d  template=%s" %
              (m["num"], "ok" if os.path.isfile(os.path.join(SITE, m["audio"])) else "MISSING",
               len(m["slides"]), m["template"]["name"] if m["template"] else "-"))

if __name__ == "__main__":
    main()
