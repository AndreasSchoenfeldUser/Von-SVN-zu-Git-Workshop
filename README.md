# Von SVN zu Git – Git Grundlagen für SVN-Umsteiger

Zweitägiges Training der Comquent Academy für Entwickler, die von Subversion (SVN) auf Git umsteigen. Der Kurs folgt dem Weg einer Änderung in sechs Stationen statt einer Befehlsreferenz. Ein durchgehendes Übungsprojekt (das Reiseportal eines erfundenen Reiseveranstalters, eine Java-Webanwendung) zieht am Ende von Tag 2 von SVN nach GitLab um.

## Inhalt des Repositorys

| Pfad | Inhalt |
| --- | --- |
| `agenda/kursagenda.md` | Kursagenda mit Lernzielen, Leitidee, Modulen beider Tage und Zusatzmodul |
| `slides/generator/` | Python-Generator für die Slides: `common.py` (Stil und Bausteine), `tag1.py`, `tag2.py`, `merge_module.py` (Zusatzmodul Mergen und Merge-Strategien), `workflow_module.py` (Zusatzmodul Git-Workflow), `nachbereitung_module.py` (Zusatzmodul Nachbereitung des Umzugs) |
| `slides/decks/tag1/`, `slides/decks/tag2/` | Erzeugte Gesamt-Decks je Tag (`deck.json`, `deck.css`, eine HTML-Datei je Slide) |
| `slides/decks/kapitel/` | Ein Deck je Kapitel (Einführung, Module, Zusatzmodul), zum Beispiel `t1-03-arbeiten-und-festhalten` |
| `slides/assets/` | Logo der Comquent Academy |
| `slides/pptx/` | PowerPoint-Fassung beider Tage (`tag1.pptx`, `tag2.pptx`) und jedes Kapitels (`kapitel/*.pptx`), aus den Deck-Dateien erzeugt |
| `tools/preview/` | Lokale Vorschau der Slides als PNG |
| `tools/pptx/` | Export der Decks nach PowerPoint |
| `artifacts.json` | Zuordnung zu den veröffentlichten Claude-Artefakten (Decks und Agenda) |

Umfang: Tag 1 mit 55 Slides (Module 01–07), Tag 2 mit 106 Slides (Module 08–15 sowie die Zusatzmodule Merge-Strategien, Git-Workflow und Nachbereitung des Umzugs). Jedes Modul besteht aus Trennfolie, Theorie, Praxis mit Befehlsbeispielen und Übung und liegt zusätzlich als eigenes Deck vor (20 Kapitel).

## Slides erzeugen

```bash
python3 slides/generator/tag1.py
python3 slides/generator/tag2.py
```

Die Skripte schreiben das Gesamt-Deck des Tages nach `slides/decks/tag1/project` bzw. `slides/decks/tag2/project` und zusätzlich ein Deck je Kapitel nach `slides/decks/kapitel/<kapitel>/project`. Die Kapitel ergeben sich aus den Abschnitten (`d.section(...)`) in den Generator-Skripten; Verzeichnisname und Titel stehen dort beim jeweiligen Abschnitt. Die erzeugten Dateien sind Teil des Repositorys, damit Änderungen im Review sichtbar sind.

Kapitel von Tag 1: `t1-00-einfuehrung`, `t1-01-auftakt` bis `t1-07-kaputter-freitag`. Kapitel von Tag 2: `t2-00-einfuehrung`, `t2-08-rueckblick` bis `t2-15-abschluss`, dazu `t2-12y-merge-strategien`, `t2-12z-git-workflow` und `t2-14z-umzug-nachbereitung` für die Zusatzmodule.

## Vorschau

Voraussetzung: Node.js mit Playwright und Chromium sowie Python mit Pillow.

```bash
node tools/preview/pv.js slides/decks/tag2 preview/tag2
python3 tools/preview/contact_sheet.py preview/tag2
```

Die Vorschau lädt keine Web-Fonts und keine hochgeladenen Bilder. Das Logo erscheint dort nur als Platzhalter.

## PowerPoint erzeugen

Voraussetzung: Node.js und Google Chrome. Einmalig die Abhängigkeiten installieren:

```bash
cd tools/pptx
npm install
npm run build
```

Der Export lädt die erzeugten Deck-Dateien in Chrome, übernimmt das berechnete Layout und schreibt `slides/pptx/tag1.pptx`, `slides/pptx/tag2.pptx` und je Kapitel `slides/pptx/kapitel/<kapitel>.pptx`. Ein einzelnes Deck: `node export.js tag2` oder `node export.js kapitel/t2-09-integrieren`. Die Folien bestehen aus editierbaren PowerPoint-Elementen: Texte, Flächen, Tabellen, Pfeile, Commit-Graphen aus Linien und Kreisen. Überschriften liegen in Titel-Platzhaltern, Logo, Fußzeile und Seitenzahl im Folienlayout, die Sprechernotizen in den Notizen. Jedes Modul ist ein eigener Abschnitt.

Schriften: Überschriften und Text verwenden Space Grotesk und Inter. Sind sie auf dem Rechner nicht installiert, ersetzt PowerPoint sie durch Calibri; das Layout bleibt dabei erhalten. Code steht in Consolas, weil ein proportionaler Ersatz die Einrückungen zerstören würde. Mit `PPTX_CODE_FONT="JetBrains Mono" npm run build` bleibt die Code-Schrift des Decks erhalten.

Nach Änderungen am Generator die PowerPoint-Dateien neu erzeugen und mit committen.

## Veröffentlichung

Die Decks sind als Claude-Artefakte vom Typ „Slides“ veröffentlicht (Links in `artifacts.json`). Nach einer Änderung am Generator werden die geänderten Dateien unter `project/` in das jeweilige Artefakt hochgeladen. Das Logo ist pro Artefakt als eigenes Asset hinterlegt; die Asset-Adressen stehen in `artifacts.json` und in den Generator-Skripten.

## Offene Punkte für die Schulungsumgebung

- Übungsstände `modul04` und `freitag` im Übungs-Repository des Reiseportals
- GitLab-Gruppen je Team mit geschütztem main
- Übersicht des SVN-Repositorys für die Migrationsübung (trunk, drei Branches, zwölf Tags, externer Verweis, große Bild- und Videodateien)
- Aufgabenliste für die Abschlussübung „Umzugstag“
- Für das Zusatzmodul „Mergen und Merge-Strategien“: Übungsstand `merge` mit den Branches `feature/merkliste`, `feature/preisalarm` (mit Zwischen-Commits), `format/einrueckung` und `suche/trefferzahl`
- Für das Zusatzmodul „Nachbereitung des Umzugs“: Repository `portal-common` in jeder Team-Gruppe, Verzeichnis `hotel-import` im SVN-Repository des Reiseportals
