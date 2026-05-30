/* AI Agents for Tech Recruiters - course player (static MVP) */
(function () {
  "use strict";

  var MODULES = window.MODULES || [];
  var STORE_KEY = "aiagents-progress-v1";

  /* ---------- progress (localStorage) ---------- */
  function loadDone() {
    try { return new Set(JSON.parse(localStorage.getItem(STORE_KEY) || "[]")); }
    catch (e) { return new Set(); }
  }
  function saveDone(set) {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(Array.from(set))); } catch (e) {}
  }
  var done = loadDone();

  function updatePill() {
    var pill = document.getElementById("progressPill");
    if (pill) pill.textContent = done.size + " / " + MODULES.length + " complete";
  }

  /* ---------- routing ---------- */
  function currentNum() {
    var h = (location.hash || "").replace(/^#m/, "");
    var found = MODULES.some(function (m) { return m.num === h; });
    return found ? h : (MODULES[0] ? MODULES[0].num : null);
  }
  function go(num) {
    if (location.hash !== "#m" + num) location.hash = "#m" + num;
    else render();
  }

  /* ---------- sidebar ---------- */
  function renderNav() {
    var nav = document.getElementById("moduleNav");
    var active = currentNum();
    nav.innerHTML = "";
    MODULES.forEach(function (m) {
      var a = document.createElement("a");
      a.href = "#m" + m.num;
      a.className = "mod-link" + (m.num === active ? " active" : "") + (done.has(m.num) ? " done" : "");
      a.innerHTML =
        '<span class="mod-num">' + m.num + '</span>' +
        '<span class="mod-title">' + escapeHtml(m.title) + '</span>' +
        '<span class="mod-check">✓</span>';
      nav.appendChild(a);
    });
  }

  /* ---------- slide panel ---------- */
  function slidePanel(m, opts) {
    opts = opts || {};
    var wrap = document.createElement("div");
    wrap.className = "slides";
    var api = { wrap: wrap, total: 0, goTo: function () {} };

    var deck = (window.SLIDES || {})[m.num] || [];   // inline HTML slides
    var imgs = m.slides || [];                         // exported slide images

    if (deck.length || imgs.length) {
      var useHtml = deck.length > 0;
      var total = useHtml ? deck.length : imgs.length;
      var idx = 0;

      var stage = document.createElement("div");
      stage.className = "slides-stage" + (useHtml ? " html" : "");
      var holder = document.createElement(useHtml ? "div" : "img");
      if (useHtml) holder.className = "slide-holder"; else holder.alt = "Slide";
      stage.appendChild(holder);

      var bar = document.createElement("div");
      bar.className = "slides-bar";
      var prev = mkBtn("← Prev", "btn btn-sm btn-ghost");
      var next = mkBtn("Next →", "btn btn-sm btn-ghost");
      var count = document.createElement("span");
      count.className = "slide-count";
      var open = mkLink("Open in Gamma ↗", m.gammaUrl, "btn btn-sm btn-ghost");

      function paint() {
        if (useHtml) holder.innerHTML = deck[idx];
        else holder.src = imgs[idx];
        count.textContent = "Slide " + (idx + 1) + " / " + total;
        prev.disabled = idx === 0;
        next.disabled = idx === total - 1;
        stage.scrollTop = 0;
      }
      prev.onclick = function () { if (idx > 0) { idx--; paint(); if (opts.onManual) opts.onManual(idx, total); } };
      next.onclick = function () { if (idx < total - 1) { idx++; paint(); if (opts.onManual) opts.onManual(idx, total); } };

      bar.appendChild(prev);
      bar.appendChild(count);
      bar.appendChild(next);
      var sp = document.createElement("span"); sp.className = "spacer"; bar.appendChild(sp);
      bar.appendChild(open);
      wrap.appendChild(stage);
      wrap.appendChild(bar);
      paint();
      api.total = total;
      api.goTo = function (i) { i = Math.max(0, Math.min(total - 1, i)); if (i !== idx) { idx = i; paint(); } };
    } else {
      var stage2 = document.createElement("div");
      stage2.className = "slides-stage";
      stage2.innerHTML =
        '<div class="slides-empty">' +
          '<div class="ico">▣</div>' +
          '<p>Slides for this module open in Gamma. Inline slides appear here once the deck is exported to images.</p>' +
        '</div>';
      var bar2 = document.createElement("div");
      bar2.className = "slides-bar";
      var sp2 = document.createElement("span"); sp2.className = "spacer";
      bar2.appendChild(sp2);
      bar2.appendChild(mkLink("Open slides in Gamma ↗", m.gammaUrl, "btn btn-sm btn-accent"));
      wrap.appendChild(stage2);
      wrap.appendChild(bar2);
    }
    return api;
  }

  /* ---------- module view ---------- */
  function renderModule(m, i) {
    var v = document.createElement("div");
    v.className = "view";

    v.appendChild(el('<p class="eyebrow">Module ' + m.num + '</p>'));
    v.appendChild(el('<h1>' + escapeHtml(m.title) + '</h1>'));

    var au = document.createElement("audio");
    au.controls = true; au.preload = "none"; au.src = m.audio;

    // slides; manual nav seeks the audio to that slide's position (two-way lock)
    var slidesApi = slidePanel(m, {
      onManual: function (i, total) {
        if (au.duration && isFinite(au.duration) && total) {
          au.currentTime = (i / total) * au.duration;
        }
      }
    });
    v.appendChild(slidesApi.wrap);

    // audio card
    var audio = document.createElement("div");
    audio.className = "audio-card";
    audio.innerHTML =
      '<div class="ada-badge">A</div>' +
      '<div class="audio-meta"><span class="who">Narrated by Ada</span>' +
      '<span class="sub">AI voice · slides follow automatically</span></div>';
    audio.appendChild(au);
    v.appendChild(audio);

    // auto-advance slides as Ada plays (even split across the track)
    if (slidesApi.total > 1) {
      au.addEventListener("timeupdate", function () {
        if (!au.duration || !isFinite(au.duration)) return;
        var per = au.duration / slidesApi.total;
        slidesApi.goTo(Math.min(slidesApi.total - 1, Math.floor(au.currentTime / per)));
      });
    }

    // lesson
    var lesson = document.createElement("div");
    lesson.className = "lesson";
    lesson.innerHTML = m.lessonHtml || "";
    v.appendChild(lesson);

    // take-home
    if (m.template && m.template.url) {
      var th = document.createElement("div");
      th.className = "takehome";
      th.innerHTML =
        '<div><div class="label">Take-home asset</div>' +
        '<div class="name">' + escapeHtml(m.template.name) + '</div></div>';
      var sp = document.createElement("span"); sp.className = "spacer"; sp.style.flex = "1"; th.appendChild(sp);
      th.appendChild(mkLink("Open template ↗", m.template.url, "btn btn-sm"));
      v.appendChild(th);
    }

    // pager
    var pager = document.createElement("div");
    pager.className = "pager";
    var prevM = MODULES[i - 1], nextM = MODULES[i + 1];
    var pBtn = mkBtn("← Previous", "btn btn-ghost");
    pBtn.disabled = !prevM; pBtn.onclick = function () { if (prevM) go(prevM.num); };
    var doneBtn = mkBtn(done.has(m.num) ? "✓ Completed" : "Mark complete", "btn btn-accent");
    doneBtn.onclick = function () {
      if (done.has(m.num)) done.delete(m.num); else done.add(m.num);
      saveDone(done); updatePill(); renderNav();
      doneBtn.textContent = done.has(m.num) ? "✓ Completed" : "Mark complete";
    };
    var nBtn = mkBtn("Next →", "btn");
    nBtn.disabled = !nextM; nBtn.onclick = function () { if (nextM) go(nextM.num); };
    pager.appendChild(pBtn); pager.appendChild(doneBtn); pager.appendChild(nBtn);
    v.appendChild(pager);

    return v;
  }

  function render() {
    var num = currentNum();
    var i = MODULES.findIndex(function (m) { return m.num === num; });
    if (i < 0) i = 0;
    var content = document.getElementById("content");
    content.innerHTML = "";
    content.appendChild(renderModule(MODULES[i], i));
    content.scrollTop = 0;
    window.scrollTo(0, 0);
    renderNav();
  }

  /* ---------- helpers ---------- */
  function mkBtn(text, cls) { var b = document.createElement("button"); b.className = cls; b.textContent = text; return b; }
  function mkLink(text, href, cls) { var a = document.createElement("a"); a.className = cls; a.href = href; a.target = "_blank"; a.rel = "noopener"; a.textContent = text; return a; }
  function el(html) { var t = document.createElement("template"); t.innerHTML = html.trim(); return t.content.firstChild; }
  function escapeHtml(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* ---------- boot ---------- */
  if (!MODULES.length) {
    document.getElementById("content").innerHTML =
      '<div class="view"><h1>No modules loaded</h1><p>data/modules.js is missing or empty.</p></div>';
    return;
  }
  window.addEventListener("hashchange", render);
  updatePill();
  render();
})();
