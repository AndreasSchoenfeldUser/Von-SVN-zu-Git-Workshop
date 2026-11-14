# Von SVN zu Git – Git Grundlagen für SVN-Umsteiger

Zweitägiges Training der Comquent Academy für Entwickler, die von Subversion (SVN) auf Git umsteigen. Der Kurs folgt dem Weg einer Änderung in sechs Stationen statt einer Befehlsreferenz. Ein durchgehendes Übungsprojekt (die Steuerungskonfiguration einer erfundenen Abfüllanlage) zieht am Ende von Tag 2 von SVN nach GitLab um.

## Inhalt des Repositorys

| Pfad | Inhalt |
| --- | --- |
| `agenda/kursagenda.md` | Kursagenda mit Lernzielen, Leitidee, Modulen beider Tage und Zusatzmodul |
| `slides/generator/` | Python-Generator für die Slides: `common.py` (Stil und Bausteine), `tag1.py`, `tag2.py`, `workflow_module.py` (Zusatzmodul Git-Workflow) |
| `slides/decks/tag1/`, `slides/decks/tag2/` | Erzeugte Deck-Dateien (`deck.json`, `deck.css`, eine HTML-Datei je Slide) |
| `slides/assets/` | Logo der Comquent Academy |
| `tools/preview/` | Lokale Vorschau der Slides als PNG |
| `artifacts.json` | Zuordnung zu den veröffentlichten Claude-Artefakten (Decks und Agenda) |

Umfang: Tag 1 mit 39 Slides (Module 01–07), Tag 2 mit 55 Slides (Module 08–15 und Zusatzmodul Git-Workflow). Jedes Modul besteht aus Trennfolie, Theorie, Praxis mit Befehlsbeispielen und Übung.

## Slides erzeugen

```bash
python3 slides/generator/tag1.py
python3 slides/generator/tag2.py
```

Die Skripte schreiben nach `slides/decks/tag1/project` bzw. `slides/decks/tag2/project`. Die erzeugten Dateien sind Teil des Repositorys, damit Änderungen im Review sichtbar sind.

## Vorschau

Voraussetzung: Node.js mit Playwright und Chromium sowie Python mit Pillow.

```bash
node tools/preview/pv.js slides/decks/tag2 preview/tag2
python3 tools/preview/contact_sheet.py preview/tag2
```

Die Vorschau lädt keine Web-Fonts und keine hochgeladenen Bilder. Das Logo erscheint dort nur als Platzhalter.

## Veröffentlichung

Die Decks sind als Claude-Artefakte vom Typ „Slides“ veröffentlicht (Links in `artifacts.json`). Nach einer Änderung am Generator werden die geänderten Dateien unter `project/` in das jeweilige Artefakt hochgeladen. Das Logo ist pro Artefakt als eigenes Asset hinterlegt; die Asset-Adressen stehen in `artifacts.json` und in den Generator-Skripten.

## Offene Punkte für die Schulungsumgebung

- Übungsstände `modul04` und `freitag` im Übungs-Repository der Abfüllanlage
- GitLab-Gruppen je Team mit geschütztem main
- Übersicht des SVN-Repositorys für die Migrationsübung (trunk, drei Branches, zwölf Tags, externer Verweis, CAD-Dateien)
- Aufgabenliste für die Abschlussübung „Umzugstag“
