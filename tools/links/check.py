#!/usr/bin/env python3
"""Prüft die Links der Referenz-Slides in den erzeugten Decks.

Aufruf (aus dem Repository-Wurzelverzeichnis):  python3 tools/links/check.py
Liest alle Slides unter slides/decks/<tag>/project/slides/, sammelt die Links und ruft jeden
einmal mit curl ab (nutzt die Zertifikate des Systems). Gemeldet werden HTTP-Status, Seitentitel und, bei Links mit #Anker, ob der Anker
auf der Seite vorkommt. Rückgabewert 1, wenn ein Link nicht erreichbar ist.
"""
import glob, html, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UA = "Mozilla/5.0 (compatible; link-check)"


def collect():
    links = {}
    for tag in ("tag1", "tag2"):
        for f in sorted(glob.glob(os.path.join(ROOT, "slides/decks", tag, "project/slides/*.html"))):
            for u in re.findall(r'<a href="([^"]+)"', open(f, encoding="utf-8").read()):
                links.setdefault(html.unescape(u), []).append("%s/%s" % (tag, os.path.basename(f)[:-5]))
    return links


def check(url):
    base, _, anchor = url.partition("#")
    r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, "-H", "Accept-Language: de,en",
                        "-w", "\n%{http_code}", base], capture_output=True)
    body, _, status = r.stdout.decode("utf-8", "ignore").rpartition("\n")
    status = int(status or 0)
    if r.returncode:
        return url, status, "curl-Fehler %d" % r.returncode, False
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.S)
    title = re.sub(r"\s+", " ", html.unescape(m.group(1))).strip()[:70] if m else ""
    ok = status == 200 and (not anchor or re.search(r'id="?%s[" >]' % re.escape(anchor), body) is not None)
    return url, status, title, ok


def main():
    links = collect()
    with ThreadPoolExecutor(8) as ex:
        results = list(ex.map(check, links))
    bad = 0
    for url, status, title, ok in results:
        bad += not ok
        print("%s %3s  %s\n        %s  (%s)" % ("OK  " if ok else "FEHL", status, url, title, ", ".join(links[url])))
    print("\n%d Links, %d nicht erreichbar" % (len(results), bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
