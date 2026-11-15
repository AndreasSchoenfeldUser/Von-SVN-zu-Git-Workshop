import json, os, html, shutil
from urllib.parse import unquote

LOGO = "/_blob/c8bbd1d863b96e8d96ffc7eb58fb5315"

CSS = """
:root{--navy:#10345A;--navy2:#1B4672;--coral:#EC3C5C;--coral-ink:#B81E3E;--coral-soft:#F8A5B5;--tint:#FBE4E9;--paper:#F7F4EF;--card:#FDFCFA;--line:#DCD6CC;--muted:#4A5A6E;--onnavy:#F4F1EC;--onnavy-muted:#BCC9D8;}
section{counter-increment:page;font-family:'Inter',Arial,sans-serif;color:var(--navy);background:var(--paper);}
h1,h2,h3{font-family:'Space Grotesk',Arial,sans-serif;font-weight:700;color:var(--navy);line-height:1.1;}
section.content{padding:128px 128px 160px;display:flex;flex-direction:column;}
.head{display:flex;align-items:center;gap:24px;margin-bottom:20px;}
.tag{font-size:24px;font-weight:600;padding:6px 22px;border-radius:24px;letter-spacing:1px;}
.t-theorie{background:var(--navy);color:var(--onnavy);}
.t-praxis{background:var(--tint);color:var(--coral-ink);}
.t-uebung{background:var(--coral-ink);color:var(--onnavy);}
.t-intro{background:var(--line);color:var(--navy);}
.crumb{font-size:24px;color:var(--muted);font-weight:600;}
section.content h2{font-size:60px;margin-bottom:44px;}
.lead{font-size:32px;color:var(--muted);line-height:1.45;margin-bottom:36px;}
.footer{position:absolute;left:128px;bottom:56px;width:1664px;display:flex;justify-content:space-between;align-items:center;}
.footl{display:flex;align-items:center;gap:24px;}
.footlogo{width:113px;height:48px;object-fit:contain;}
.foot{font-size:24px;color:var(--muted);}
.pageno{font-size:24px;color:var(--muted);font-weight:600;}
.pageno::after{content:counter(page);}

.cards{display:grid;gap:32px;}
.c2{grid-template-columns:1fr 1fr;}
.c3{grid-template-columns:1fr 1fr 1fr;}
.c4{grid-template-columns:1fr 1fr 1fr 1fr;}
.card{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:40px;display:flex;flex-direction:column;gap:16px;}
.card h3{font-size:36px;}
.card .ct{font-size:32px;line-height:1.45;color:var(--muted);}
.card .k{font-size:24px;font-weight:600;color:var(--coral-ink);letter-spacing:1px;}
.card ul{font-size:32px;line-height:1.45;color:var(--muted);padding-left:34px;}
.card.dark{background:var(--navy);border-color:var(--navy);}
.card.dark h3{color:var(--onnavy);}
.card.dark .ct{color:var(--onnavy-muted);}
.card.dark .k{color:var(--coral-soft);}
.card.dark ul{color:var(--onnavy-muted);}
.cicon{width:56px;height:56px;color:var(--coral);}

.split{display:grid;grid-template-columns:1040px 1fr;gap:56px;align-items:start;}
.split.wide{grid-template-columns:1fr;}
.code{background:var(--navy);color:#DCE4EC;font-family:'JetBrains Mono','Courier New',monospace;font-size:28px;line-height:1.45;padding:40px;border-radius:16px;white-space:nowrap;}
.code .pr{color:var(--coral-soft);}
.code .cm{color:#93A9C0;}
.code .out{color:#B9C6D4;}
.code .hl{color:#FFD9A0;}
.notes{display:flex;flex-direction:column;gap:28px;}
.note{border-left:6px solid var(--coral);padding:6px 0 6px 28px;display:flex;flex-direction:column;gap:8px;}
.note .nk{font-family:'JetBrains Mono','Courier New',monospace;font-size:24px;font-weight:600;color:var(--coral-ink);}
.note .nt{font-size:32px;line-height:1.4;color:var(--navy);}

.band{position:absolute;left:0;top:0;width:24px;height:1080px;background:var(--coral);}
.ex{display:grid;grid-template-columns:1fr 470px;gap:64px;align-items:start;}
.exl{display:flex;flex-direction:column;gap:28px;}
.scenario{background:var(--tint);border-radius:16px;padding:28px 36px;font-size:32px;line-height:1.45;color:var(--navy);}
.tasks{font-size:32px;line-height:1.45;color:var(--navy);padding-left:44px;}
.meta{display:flex;flex-direction:column;gap:20px;}
.mcard{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:26px 32px;display:flex;flex-direction:column;gap:6px;}
.mcard .mk{font-size:24px;font-weight:600;color:var(--coral-ink);letter-spacing:1px;}
.mcard .mv{font-size:28px;line-height:1.4;color:var(--navy);}

section.cover{background:var(--paper);padding:128px;display:flex;flex-direction:column;justify-content:center;}
.cpanel{position:absolute;left:1312px;top:0;width:608px;height:1080px;background:var(--navy);}
.cday{position:absolute;left:1392px;top:400px;width:448px;display:flex;flex-direction:column;gap:20px;}
.cday .dk{font-size:24px;font-weight:600;color:var(--coral-soft);letter-spacing:4px;}
.cday .dn{font-family:'Space Grotesk',Arial,sans-serif;font-size:96px;font-weight:700;color:var(--onnavy);line-height:1;}
.cday .dt{font-size:36px;color:var(--onnavy-muted);line-height:1.3;}
.clogo{width:470px;height:200px;object-fit:contain;margin-bottom:72px;}
.cover h1{font-size:96px;width:1060px;margin-bottom:28px;}
.cover .sub{font-size:36px;color:var(--muted);width:1060px;line-height:1.35;margin-bottom:48px;}
.cbar{width:160px;height:12px;background:var(--coral);}

section.divider{background:var(--navy);padding:128px;display:flex;flex-direction:column;justify-content:center;}
.divider .num{font-family:'Space Grotesk',Arial,sans-serif;font-size:160px;font-weight:700;color:var(--coral);line-height:1;margin-bottom:28px;}
.divider h2{font-size:96px;color:var(--onnavy);margin-bottom:36px;width:1500px;}
.divider .goal{font-size:36px;color:var(--onnavy-muted);line-height:1.4;width:1300px;}
.divider .dmeta{font-size:24px;font-weight:600;color:var(--coral-soft);letter-spacing:3px;margin-top:56px;}

section.statement{background:var(--coral);padding:128px;display:flex;flex-direction:column;justify-content:center;}
.statement .sk{font-size:24px;font-weight:600;color:var(--onnavy);letter-spacing:4px;margin-bottom:36px;}
.statement h1{font-size:96px;color:var(--onnavy);width:1500px;}
.statement .ssub{font-size:36px;color:var(--onnavy);line-height:1.4;width:1300px;margin-top:44px;}

.stations{display:grid;grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr;gap:20px;}
.st{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:32px 26px;display:flex;flex-direction:column;gap:14px;}
.st .sn{font-family:'Space Grotesk',Arial,sans-serif;font-size:60px;font-weight:700;color:var(--coral-ink);line-height:1;}
.st h3{font-size:28px;line-height:1.2;}
.st .sd{font-size:24px;line-height:1.4;color:var(--muted);}
.st.on{background:var(--navy);border-color:var(--navy);}
.st.on .sn{color:var(--coral-soft);}
.st.on h3{color:var(--onnavy);}
.st.on .sd{color:var(--onnavy-muted);}
.legend{font-size:24px;color:var(--muted);margin-top:32px;}

.flow{display:flex;align-items:stretch;gap:20px;}
.fbox{flex:1 1 0;min-width:0;background:var(--card);border:2px solid var(--line);border-radius:16px;padding:36px;display:flex;flex-direction:column;gap:14px;}
.fbox h3{font-size:36px;}
.fbox .ct{font-size:28px;line-height:1.45;color:var(--muted);}
.fbox.dark{background:var(--navy);border-color:var(--navy);}
.fbox.dark h3{color:var(--onnavy);}
.fbox.dark .ct{color:var(--onnavy-muted);}
.farrow{width:190px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;}
.farrow .fl{font-family:'JetBrains Mono','Courier New',monospace;font-size:24px;font-weight:600;color:var(--coral-ink);}
.arr{width:110px;height:48px;background:var(--coral);}
.farrow.slim{width:72px;}
.farrow.slim .arr{width:64px;height:32px;}
.under{font-size:32px;color:var(--muted);line-height:1.45;margin-top:36px;}

.tbl{width:100%;font-size:28px;color:var(--navy);}
.tbl .th{background:#E9E4DA;}
.tbl .alt{background:#EFEBE3;}

.graph{position:relative;}
.gl{position:absolute;font-size:24px;font-weight:700;color:var(--onnavy);text-align:center;}
.gt{position:absolute;box-sizing:border-box;font-size:24px;font-weight:600;padding:4px 14px;border-radius:20px;white-space:nowrap;text-align:center;}
.gt.main{background:var(--navy);color:var(--onnavy);}
.gt.br{background:var(--tint);color:var(--coral-ink);}
.gt.head{background:var(--card);color:var(--navy);border:2px solid var(--navy);}
.gt.ghost{background:var(--paper);color:var(--muted);border:2px dashed var(--muted);}
.gcap{font-size:28px;font-weight:700;font-family:'Space Grotesk',Arial,sans-serif;margin-bottom:12px;}
.gpanel{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:32px;display:flex;flex-direction:column;gap:8px;}
.gpanel .ct{font-size:32px;line-height:1.4;color:var(--muted);}

section.content .rise{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;}
.wf{position:relative;}
.lanel{position:absolute;font-family:'JetBrains Mono','Courier New',monospace;font-size:24px;font-weight:600;color:var(--navy);}
.tagp{position:absolute;box-sizing:border-box;font-size:24px;font-weight:600;padding:3px 12px;border-radius:8px;white-space:nowrap;text-align:center;background:var(--card);color:var(--navy);border:2px solid var(--navy);}
.tagp.mr{border:2px solid var(--coral-ink);color:var(--coral-ink);background:var(--tint);}
.legend2{display:flex;gap:40px;margin-top:20px;}
.legend2 .li{font-size:24px;color:var(--muted);}
.t-ref{background:var(--card);color:var(--navy);border:2px solid var(--navy);}
.refs{display:flex;flex-direction:column;gap:22px;}
.ref{border-left:6px solid var(--coral);padding:2px 0 2px 28px;display:flex;flex-direction:column;gap:4px;}
.ref .rt{font-size:32px;font-weight:600;line-height:1.3;color:var(--navy);}
.ref .rq{font-size:24px;font-weight:400;color:var(--muted);}
.ref .ru{font-family:'JetBrains Mono','Courier New',monospace;font-size:24px;line-height:1.35;color:var(--coral-ink);}
.ref .ru a{color:var(--coral-ink);text-decoration:none;}
.checked{font-size:24px;color:var(--muted);margin-top:28px;}
.rise{animation:rise 520ms ease-out both;animation-delay:120ms;}
@keyframes rise{from{opacity:0;transform:translateY(18px);}}
"""

FACES = {
    "space-grotesk": {"family": "Space Grotesk", "href": "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap"},
    "inter": {"family": "Inter", "href": "https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"},
    "jetbrains-mono": {"family": "JetBrains Mono", "href": "https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&display=swap"},
}

TAGS = {"Theorie": "t-theorie", "Praxis": "t-praxis", "Übung": "t-uebung", "Einführung": "t-intro", "Referenzen": "t-ref"}


class Deck:
    def __init__(self, root, title, footer_text):
        self.root = root
        self.title = title
        self.footer_text = footer_text
        self.slides = []  # (id, html)
        self.sections = {}
        self.chapters = {}  # Abschnitt -> (Verzeichnisname, Titel) für die Kapitel-Decks

    def section(self, desc, slug, title):
        """Beginnt einen Abschnitt. slug: Verzeichnis des Kapitel-Decks, title: dessen Titel."""
        key = "s%d" % (len(self.sections) + 1)
        self.sections[key] = {"description": desc, "start": None}
        self.chapters[key] = (slug, title)
        self._pending = key

    def add(self, sid, html_):
        if getattr(self, "_pending", None):
            self.sections[self._pending]["start"] = sid
            self._pending = None
        self.slides.append((sid, html_))

    def footer(self):
        return ('<div class="footer"><div class="footl"><img class="footlogo" src="%s" alt="Comquent Academy">'
                '<p class="foot">%s</p></div><div class="pageno"></div></div>') % (LOGO, self.footer_text)

    def write(self, chapters_dir=None):
        """Schreibt das Gesamt-Deck nach root und, falls angegeben, ein Deck je Kapitel nach chapters_dir."""
        _write_deck(self.root, self.title, self.slides, self.sections)
        print(len(self.slides), "slides")
        if not chapters_dir:
            return
        starts = [(k, v["start"]) for k, v in self.sections.items()]
        ids = [s for s, _ in self.slides]
        for i, (key, start) in enumerate(starts):
            end = ids.index(starts[i + 1][1]) if i + 1 < len(starts) else len(ids)
            part = self.slides[ids.index(start):end]
            slug, title = self.chapters[key]
            root = os.path.join(chapters_dir, slug)
            shutil.rmtree(root, ignore_errors=True)
            _write_deck(root, title, part, {"s1": {"description": self.sections[key]["description"], "start": start}})
            print("  %-34s %2d slides" % (slug, len(part)))


def _write_deck(root, title, slides, sections):
    os.makedirs(os.path.join(root, "project", "slides"), exist_ok=True)
    idx = {"v": 5, "createdOnFiles": {"v": 1, "at": "2026-11-14T03:45:00Z"}, "lists": "css",
           "format": {"v": 1, "shared": ["project/deck.css"]}, "title": title,
           "order": [s for s, _ in slides], "cover": slides[0][0],
           "sections": sections, "faces": FACES, "designSystems": []}
    with open(os.path.join(root, "project", "deck.json"), "w") as f:
        json.dump(idx, f, ensure_ascii=False, indent=1)
    with open(os.path.join(root, "project", "deck.css"), "w") as f:
        f.write(CSS)
    keep = {sid + ".html" for sid, _ in slides}
    for name in os.listdir(os.path.join(root, "project", "slides")):
        if name.endswith(".html") and name not in keep:  # Slides, die es nicht mehr gibt
            os.remove(os.path.join(root, "project", "slides", name))
    for sid, h in slides:
        with open(os.path.join(root, "project", "slides", sid + ".html"), "w") as f:
            f.write(h)


def aside(n):
    return "<aside>%s</aside>" % html.escape(n) if n else ""


def head(tag, crumb, title):
    return ('<div class="head"><p class="tag %s">%s</p><p class="crumb">%s</p></div><h2>%s</h2>'
            % (TAGS[tag], tag, crumb, title))


def content(d, sid, tag, crumb, title, body, notes="", lead=None, cls=""):
    band = '<div class="band"></div>' if tag == "Übung" else ""
    ld = '<p class="lead">%s</p>' % lead if lead else ""
    h = ('<section id="%s" class="content %s">%s%s%s<div class="rise">%s</div>%s%s</section>'
         % (sid, cls, band, head(tag, crumb, title), ld, body, d.footer(), aside(notes)))
    d.add(sid, h)


def cover(d, sid, title, sub, daynum, daytitle, notes=""):
    h = ('<section id="%s" class="cover"><div class="cpanel"></div>'
         '<img class="clogo" src="%s" alt="Comquent Academy">'
         '<h1>%s</h1><p class="sub">%s</p><div class="cbar"></div>'
         '<div class="cday"><p class="dk">KURSTAG</p><p class="dn">%s</p><p class="dt">%s</p></div>%s</section>'
         % (sid, LOGO, title, sub, daynum, daytitle, aside(notes)))
    d.add(sid, h)


def divider(d, sid, num, title, goal, meta, notes=""):
    h = ('<section id="%s" class="divider"><p class="num">%s</p><h2>%s</h2><p class="goal">%s</p>'
         '<p class="dmeta">%s</p>%s</section>' % (sid, num, title, goal, meta, aside(notes)))
    d.add(sid, h)


def statement(d, sid, kicker, text, sub, notes=""):
    h = ('<section id="%s" class="statement"><p class="sk">%s</p><h1>%s</h1><p class="ssub">%s</p>%s</section>'
         % (sid, kicker, text, sub, aside(notes)))
    d.add(sid, h)


def card(title, text=None, k=None, items=None, dark=False, icon=None):
    out = '<div class="card%s">' % (" dark" if dark else "")
    if icon:
        out += '<x-icon class="cicon" name="%s"></x-icon>' % icon
    if k:
        out += '<p class="k">%s</p>' % k
    out += '<h3>%s</h3>' % title
    if text:
        out += '<p class="ct">%s</p>' % text
    if items:
        out += "<ul>" + "".join("<li>%s</li>" % i for i in items) + "</ul>"
    return out + "</div>"


def cards(n, items):
    return '<div class="cards c%d">%s</div>' % (n, "".join(items))


def code(lines):
    out = []
    for ln in lines:
        if ln.startswith("$ "):
            cmd = ln[2:]
            comment = ""
            if "  # " in cmd:
                cmd, comment = cmd.split("  # ", 1)
            s = '<span class="pr">$</span> ' + nb(cmd)
            if comment:
                s += ' <span class="cm">' + nb("# " + comment) + "</span>"
            out.append(s)
        elif ln.startswith("# "):
            out.append('<span class="cm">%s</span>' % nb(ln))
        elif ln.startswith("! "):
            out.append('<span class="hl">%s</span>' % nb(ln[2:]))
        elif ln == "":
            out.append("&#160;")
        else:
            out.append('<span class="out">%s</span>' % nb(ln))
    return '<p class="code">%s</p>' % "<br>".join(out)


def nb(s):
    s = html.escape(s, quote=False)
    return s.replace(" ", "&#160;")


def notes_col(pairs):
    return '<div class="notes">%s</div>' % "".join(
        '<div class="note"><p class="nk">%s</p><p class="nt">%s</p></div>' % (html.escape(k), t) for k, t in pairs)


def praxis(d, sid, crumb, title, lines, pairs, notes="", lead=None):
    body = '<div class="split">%s%s</div>' % (code(lines), notes_col(pairs))
    content(d, sid, "Praxis", crumb, title, body, notes, lead)


def uebung(d, sid, crumb, title, tasks, zeit, form, ergebnis, scenario=None, notes=""):
    left = '<div class="exl">'
    if scenario:
        left += '<p class="scenario">%s</p>' % scenario
    left += '<ol class="tasks">%s</ol></div>' % "".join("<li>%s</li>" % t for t in tasks)
    meta = ('<div class="meta"><div class="mcard"><p class="mk">ZEIT</p><p class="mv">%s</p></div>'
            '<div class="mcard"><p class="mk">ARBEITSFORM</p><p class="mv">%s</p></div>'
            '<div class="mcard"><p class="mk">ERGEBNIS</p><p class="mv">%s</p></div></div>') % (zeit, form, ergebnis)
    content(d, sid, "Übung", crumb, title, '<div class="ex">%s%s</div>' % (left, meta), notes)


REFS_CHECKED = "15. November 2026"


def referenzen(d, sid, crumb, refs, notes):
    """Übersicht weiterführender Quellen. refs: Liste von (Titel, Quelle, URL), höchstens fünf.
    Die Links prüft tools/links/check.py in den erzeugten Decks."""
    assert len(refs) <= 5, sid
    rows = "".join(
        '<div class="ref"><p class="rt">%s <span class="rq">· %s</span></p>'
        '<p class="ru"><a href="%s">%s</a></p></div>'
        % (t, q, html.escape(u), html.escape(unquote(u).split("://", 1)[1].rstrip("/")))
        for t, q, u in refs)
    body = '<div class="refs">%s</div><p class="checked">Links geprüft am %s.</p>' % (rows, REFS_CHECKED)
    content(d, sid, "Referenzen", crumb, "Zum Nachlesen", body, notes)


def table(header, rows, widths):
    out = '<table class="tbl"><tr class="th">'
    out += "".join('<th style="width:%d%%">%s</th>' % (w, h) for h, w in zip(header, widths)) + "</tr>"
    for i, r in enumerate(rows):
        out += '<tr%s>' % (' class="alt"' if i % 2 else "") + "".join("<td>%s</td>" % c for c in r) + "</tr>"
    return out + "</table>"


def stations(active, descs=None):
    names = ["Aufgabe übernehmen", "Arbeiten und festhalten", "Teilen", "Prüfen lassen", "Integrieren", "Ausliefern"]
    d = descs or ["Eigener Branch je Aufgabe", "Lokale Commits als Arbeitsschritte", "Bewusst veröffentlichen",
                  "Review per Merge Request", "Gezielt zusammenführen", "Stand markieren und übergeben"]
    out = '<div class="stations">'
    for i, n in enumerate(names):
        on = " on" if (i + 1) in active else ""
        out += '<div class="st%s"><p class="sn">%d</p><h3>%s</h3><p class="sd">%s</p></div>' % (on, i + 1, n, d[i])
    return out + "</div>"


def graph(w, h, nodes, edges, tags, merge=()):
    """nodes: list of (x,y,label); edges: (i,j); tags: (x,y,text,cls)"""
    svg = '<svg aria-label="Commit-Graph" width="%d" height="%d" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">' % (w, h, w, h)
    for i, j in edges:
        (x1, y1, _), (x2, y2, _) = nodes[i], nodes[j]
        svg += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#10345A" stroke-width="6"/>' % (x1, y1, x2, y2)
    for k, (x, y, _) in enumerate(nodes):
        fill = "#EC3C5C" if k in merge else "#10345A"
        svg += '<circle cx="%d" cy="%d" r="30" fill="%s"/>' % (x, y, fill)
    svg += "</svg>"
    out = '<div class="graph" style="width:%dpx;height:%dpx">%s' % (w, h, svg)
    for x, y, lab in nodes:
        out += '<p class="gl" style="left:%dpx;top:%dpx;width:60px">%s</p>' % (x - 30, y - 16, lab)
    for x, y, text, cls in tags:
        tw = int(len(text) * 14.5 + 40)
        out += '<p class="gt %s" style="left:%dpx;top:%dpx;width:%dpx">%s</p>' % (cls, x - tw // 2, y, tw, text)
    return out + "</div>"


LANE_COLORS = {"main": "#10345A", "hotfix": "#8E1B3A", "release": "#3E6A97", "develop": "#EC3C5C", "feature": "#7F93AA", "bugfix": "#7F93AA"}
LANE_LABELS = {"main": "main", "hotfix": "hotfix/*", "release": "release/*", "develop": "develop", "feature": "feature/*", "bugfix": "bugfix/*"}


def workflow(w, h, lanes, nodes, edges, tags, x0=200):
    """lanes: {key: y}; nodes: {id: (x, lane)}; edges: (a, b, kind) kind seq|branch|merge|dash; tags: (id, text, pos, dx, cls)"""
    svg = '<svg aria-label="Git-Workflow" width="%d" height="%d" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">' % (w, h, w, h)
    for k, y in lanes.items():
        svg += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#DCD6CC" stroke-width="3"/>' % (x0, y, w - 10, y)
    for a, b, kind in edges:
        xa, la = nodes[a]; xb, lb = nodes[b]
        ya, yb = lanes[la], lanes[lb]
        col = LANE_COLORS[lb] if kind == "branch" else LANE_COLORS[la]
        dash = ' stroke-dasharray="14 10"' if kind == "dash" else ""
        svg += '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="6"%s/>' % (xa, ya, xb, yb, col, dash)
    for nid, (x, l) in nodes.items():
        c = LANE_COLORS[l]
        if l in ("feature", "bugfix"):
            svg += '<circle cx="%d" cy="%d" r="18" fill="#F7F4EF" stroke="%s" stroke-width="6"/>' % (x, lanes[l], "#5E7590")
        else:
            svg += '<circle cx="%d" cy="%d" r="20" fill="%s"/>' % (x, lanes[l], c)
    svg += "</svg>"
    out = '<div class="wf" style="width:%dpx;height:%dpx">%s' % (w, h, svg)
    for k, y in lanes.items():
        out += '<p class="lanel" style="left:0px;top:%dpx;width:%dpx">%s</p>' % (y - 17, x0 - 30, LANE_LABELS[k])
    for nid, text, pos, dx, cls in tags:
        x, l = nodes[nid]
        y = lanes[l]
        tw = int(len(text) * 14.5 + 32)
        top = y - 64 if pos == "above" else y + 30
        out += '<p class="tagp %s" style="left:%dpx;top:%dpx;width:%dpx">%s</p>' % (cls, x + dx - tw // 2, top, tw, text)
    return out + "</div>"
