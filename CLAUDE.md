# CLAUDE.md

Kontext für Claude Code in diesem Repository.

## Projekt

Training „Von SVN zu Git – Git Grundlagen für SVN-Umsteiger“ der Comquent Academy (Geschäftsbereich der Comquent GmbH, Puchheim). Zwei Kurstage, zwei optionale Zusatzmodule. Zielgruppe: Entwickler mit SVN-Erfahrung, oft aus Industrie und Automatisierung.

Didaktischer Grundsatz: Die Teilnehmenden werden über den Arbeitsablauf an Git herangeführt, nicht über eine Wort-für-Wort-Übersetzung von SVN-Befehlen. Keine Gegenüberstellungstabellen „SVN-Befehl → Git-Befehl“. Prozessvergleiche (wie organisiert Git einen Schritt anders) sind erwünscht.

Leitidee mit sechs Stationen: Aufgabe übernehmen, Arbeiten und festhalten, Teilen, Prüfen lassen, Integrieren, Ausliefern. Tag 1 behandelt die Stationen 1–2, Tag 2 die Stationen 3–6. Roter Faden ist das Reiseportal, eine Java-Webanwendung (Maven, Spring Boot) eines erfundenen Reiseveranstalters: `pom.xml`, Code unter `src/main/java/de/reiseportal/`, Konfiguration in `src/main/resources/application.yml` (Trefferzahl der Suche, Stornofrist, Reservierungsdauer, Timeout des Zahlungsdienstes), Tests unter `src/test/java/`. Neue Funktionen entstehen auf Branches wie `feature/merkliste`.

## Sprache und Ton

- Deutsch, formell, vollständige Sätze, Anrede „Sie“ in Übungen.
- Natürliche, präzise Formulierungen; keine Marketing-Sprache, keine KI-typischen Floskeln.
- Englische Fachbegriffe bleiben englisch (Branch, Merge Request, Staging Area, Working Directory, Pipeline).
- Deutsche Anführungszeichen „…“ im Fließtext; gerade Anführungszeichen nur in Code.

## Aufbau

- `slides/generator/common.py`: Stil (CSS), Farben, Schriften, Bausteine (`cover`, `divider`, `content`, `statement`, `card`, `cards`, `table`, `praxis`, `uebung`, `stations`, `graph`, `workflow`).
- `slides/generator/tag1.py`, `tag2.py`: Inhalte je Tag. `tag2.py` bindet `workflow_module.py` (Zusatzmodul Git-Workflow) nach Modul 12 und `nachbereitung_module.py` (Zusatzmodul Nachbereitung des Umzugs) nach Modul 14 ein.
- Ausgabe: `slides/decks/<tag>/project/` (Gesamt-Deck des Tages) und `slides/decks/kapitel/<kapitel>/project/` (ein Deck je Kapitel), jeweils mit `deck.json`, `deck.css`, `slides/<id>.html`. Jedes Kapitel beginnt mit `d.section(beschreibung, verzeichnis, titel)`; neue Kapitel brauchen dort einen eindeutigen Verzeichnisnamen (`t1-…`, `t2-…`). Nach jeder Änderung am Generator neu erzeugen und die Ausgabe mit committen.
- PowerPoint: `tools/pptx/export.js` rendert die Deck-Dateien in Chrome und baut daraus `slides/pptx/<tag>.pptx` und `slides/pptx/kapitel/<kapitel>.pptx` (`cd tools/pptx && npm run build`). Nach jeder Neuerzeugung der Decks ebenfalls neu erzeugen und mit committen. Der Export kennt die Bausteine aus `common.py` nicht einzeln, sondern übersetzt das berechnete Layout; neue CSS-Effekte (Verläufe, Schatten, Transformationen) dort nachziehen.
- `agenda/kursagenda.md`: Kursagenda. Bei Änderungen an Modulen oder Zeiten mitpflegen.

## Slide-Konventionen

- Jedes Modul: Trennfolie (`divider`), Theorie, Praxis (Code links, Erläuterungen rechts), Übung (Aufgaben, Zeit, Arbeitsform, Ergebnis). Kennzeichnung oben links: „Theorie“, „Praxis“, „Übung“, „Einführung“.
- Jede Slide hat Sprechernotizen (`notes`).
- Farben aus dem Logo der Comquent Academy: Navy `#10345A`, Koralle `#EC3C5C`, Text-Koralle `#B81E3E`, Papier `#F7F4EF`.
- Schriften: Space Grotesk (Überschriften), Inter (Text), JetBrains Mono (Code).
- Logo als Asset pro Artefakt; die `LOGO`-Adresse unterscheidet sich zwischen Tag 1 und Tag 2 (siehe `artifacts.json`).

## Technische Grenzen des Slides-Formats

- Canvas 1920×1080, Ränder 128 px, Fußzeile ab y 920. Inhalt passt in etwa 620 px Höhe unter der Überschrift; zu viel Inhalt auf zwei Slides verteilen.
- Schriftgröße mindestens 24 px; Fließtext 32 px, Code 28 px.
- Codezeilen in Praxis-Slides höchstens 56 Zeichen, höchstens etwa 12 Zeilen.
- Höchstens 200 Elemente pro Slide, höchstens 24 positionierte Kinder pro Container.
- Kein `<pre>`/`<code>`; Code ist ein `<p class="code">` mit `<br>` und `&#160;`.
- Nach Änderungen eine Vorschau mit `tools/preview/` rendern und die Übersichtsbilder ansehen.

## Veröffentlichung

Die Decks sind Claude-Artefakte vom Typ „Slides“ (Slugs und URLs in `artifacts.json`). Hochladen nur der geänderten Dateien im Patch-Modus. Steht in Claude Code kein Artefakt-Werkzeug zur Verfügung, die Änderungen hier committen und die Veröffentlichung in der Claude-App anstoßen.
