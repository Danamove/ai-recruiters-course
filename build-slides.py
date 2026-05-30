#!/usr/bin/env python3
"""
Turn Gamma deck content (saved from read_gamma into data/gamma-raw/module-NN.html)
into inline HTML slides for the course player.

Output: data/slides.js  ->  window.SLIDES = { "00": ["<div class=slide>...</div>", ...], ... }

The player shows these as a prev/next slideshow. Images are hotlinked from Gamma's
public CDN. Re-run after refreshing any raw deck:  python site/build-slides.py
"""
import os, glob, json, re, html
from bs4 import BeautifulSoup

SITE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(SITE, "data", "gamma-raw")

def transform(body, soup):
    # infographic -> img
    for ig in body.find_all("infographic"):
        img = soup.new_tag("img"); img["src"] = ig.get("src", ""); img["class"] = "g-info"
        ig.replace_with(img)
    # icon -> img (small)
    for ic in body.find_all("icon"):
        src = ic.get("src", "")
        img = soup.new_tag("img"); img["src"] = src; img["class"] = "g-icon"
        ic.replace_with(img)
    # diagram (data-meta steps) -> rendered step chips
    for dg in body.find_all("diagram"):
        steps_html = ""
        meta = dg.get("data-meta")
        if meta:
            try:
                data = json.loads(html.unescape(meta))
                for st in data.get("step", []):
                    txt = re.sub("<[^>]+>", "", st.get("text", "")).strip()
                    icon = (st.get("icon") or {}).get("src", "")
                    ic = ('<img class="g-icon" src="%s">' % icon) if icon else ""
                    steps_html += '<div class="g-step">%s<span>%s</span></div>' % (ic, html.escape(txt))
            except Exception:
                pass
        new = soup.new_tag("div"); new["class"] = "g-diagram"
        new.append(BeautifulSoup(steps_html, "html.parser"))
        dg.replace_with(new)
    # background-color attribute -> inline style on a colored panel
    for el in body.find_all(attrs={"background-color": True}):
        color = el.get("background-color")
        style = el.get("style", "")
        el["style"] = (style + ";" if style else "") + ("background:%s;color:#fff;padding:14px 16px;border-radius:10px" % color)
        el["class"] = (el.get("class", []) + ["g-colorpanel"]) if isinstance(el.get("class"), list) else "g-colorpanel"
        del el["background-color"]
    return body

def col_flex(col_widths):
    try:
        nums = json.loads(col_widths)
        return [str(n) for n in nums]
    except Exception:
        return None

def build_slide(section, soup):
    layout = section.get("image-layout", "blank")
    accent = section.find("img", class_="accent-image")
    body = section.find("div", class_="body")
    if body is None:
        return None
    body = transform(body, soup)

    # set flex ratios on columns
    for cols in body.find_all("columns"):
        ratios = col_flex(cols.get("col-widths", ""))
        kids = [c for c in cols.find_all("div", recursive=False)]
        if ratios and len(ratios) == len(kids):
            for c, r in zip(kids, ratios):
                style = c.get("style", "")
                c["style"] = (style + ";" if style else "") + "flex:%s 1 0" % r

    art = ""
    if accent and accent.get("src") and layout in ("left", "right"):
        art = '<div class="slide-art"><img src="%s" alt=""></div>' % accent.get("src")

    body_html = "".join(str(c) for c in body.contents)
    cls = "slide slide-%s" % (layout if layout in ("left", "right") else "full")
    inner_order = (art + '<div class="slide-body">%s</div>' % body_html) if layout == "left" \
        else ('<div class="slide-body">%s</div>' % body_html + art) if layout == "right" \
        else '<div class="slide-body">%s</div>' % body_html
    return '<div class="%s">%s</div>' % (cls, inner_order)

def main():
    out = {}
    for f in sorted(glob.glob(os.path.join(RAW, "module-*.html"))):
        num = re.search(r"module-(\d+)\.html", f).group(1)
        soup = BeautifulSoup(open(f, encoding="utf-8").read(), "html.parser")
        slides = []
        for sec in soup.find_all("section"):
            s = build_slide(sec, soup)
            if s:
                slides.append(s)
        out[num] = slides
        print("module %s: %d slides" % (num, len(slides)))
    with open(os.path.join(SITE, "data", "slides.js"), "w", encoding="utf-8") as fh:
        fh.write("window.SLIDES = " + json.dumps(out, ensure_ascii=False) + ";\n")
    print("wrote data/slides.js for %d modules" % len(out))

if __name__ == "__main__":
    main()
