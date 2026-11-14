from pathlib import Path
HERE = Path(__file__).resolve().parent
DECKS = HERE.parent / "decks"
from common import *

d = Deck(str(DECKS / "tag1"), "Von SVN zu Git – Tag 1: Allein mit Git", "Von SVN zu Git · Tag 1")
M = lambda n, t: "Modul %02d · %s" % (n, t)

# ---------- Einführung ----------
d.section("Einführung: Kursablauf, Leitidee und Übungsprojekt",
          "t1-00-einfuehrung", "Von SVN zu Git – Tag 1: Einführung")
cover(d, "cover", "Von SVN zu Git", "Git Grundlagen für Entwickler, die aus der SVN-Versionsverwaltung kommen",
      "Tag 1", "Allein mit Git: das eigene, lokale Repository",
      "Begrüßung, Vorstellung des Dozenten und der Teilnehmenden. Erwartungen kurz abfragen: Wie lange arbeitet das Team schon mit SVN, welche Projekte sollen umziehen?")

content(d, "ablauf", "Einführung", "Kursablauf", "Der erste Tag im Überblick",
        table(["Zeit", "Modul", "Schwerpunkt"], [
            ["09:00", "01 · Auftakt: Wie arbeiten wir heute?", "Ausgangslage im Team"],
            ["09:45", "02 · Das Git-Modell", "Grundbegriffe"],
            ["10:45", "03 · Arbeiten und festhalten", "Station 2"],
            ["13:00", "04 · In kleinen Schritten arbeiten", "Station 2"],
            ["14:00", "05 · Sicher experimentieren", "Station 2"],
            ["15:30", "06 · Ein Branch pro Aufgabe", "Station 1"],
            ["16:30", "07 · Übung „Der kaputte Freitag“", "Anwendung"],
        ], [14, 56, 30]) + '<p class="under">Pausen: 10:30 Uhr · 12:00 Uhr Mittagspause · 15:15 Uhr</p>',
        "Die Uhrzeiten sind Richtwerte. Wichtiger als die Uhr ist, dass jede Übung abgeschlossen wird.")

content(d, "leitidee", "Einführung", "Leitidee", "Der Weg einer Änderung in sechs Stationen",
        stations([1, 2]) + '<p class="legend">Heute im Fokus: Station 1 und 2 (dunkel hervorgehoben). Morgen folgen die Stationen 3 bis 6.</p>',
        "Der Kurs folgt nicht der Befehlsreferenz, sondern dem Weg einer Änderung durch den Entwicklungsalltag. An jeder Station fragen wir: Wie organisiert Git diesen Schritt, und was ändert sich gegenüber der bisherigen Arbeitsweise?",
        lead="Wir lernen Git nicht Befehl für Befehl, sondern entlang des Arbeitsablaufs, den Sie täglich erleben.")

content(d, "projekt", "Einführung", "Übungsprojekt", "Roter Faden: das Reiseportal",
        cards(3, [
            card("Das Projekt", "Java-Webanwendung eines erfundenen Reiseveranstalters für die Online-Buchung, seit Jahren in einem SVN-Repository gepflegt.", k="AUSGANGSLAGE", icon="Globe"),
            card("Die Inhalte", items=["pom.xml", "src/main/java/", "src/main/resources/", "src/test/java/"], k="REPOSITORY", icon="Database"),
            card("Das Ziel", "Am Ende von Tag 2 zieht das Repository samt Historie nach GitLab um.", k="ZIEL", icon="Cloud", dark=True),
        ]),
        "Alle Übungen bauen aufeinander auf. Die Schulungsumgebung in der Cloud enthält das vorbereitete Projekt; die Teilnehmenden brauchen nur Browser und Internetzugang.")

# ---------- Modul 1 ----------
crumb = M(1, "Auftakt")
d.section("Modul 01: Ausgangslage – wie arbeitet das Team heute mit SVN?",
          "t1-01-auftakt", "Von SVN zu Git – Modul 01: Auftakt")
divider(d, "m1", "01", "Auftakt: Wie arbeiten wir heute?",
        "Wir machen den heutigen Arbeitsablauf sichtbar und erkennen, an welchen Stellen Git anders denkt.",
        "09:00 – 09:45 UHR · AUSGANGSLAGE")

content(d, "m1-zentral", "Theorie", crumb, "Zentral und verteilt: zwei Arten, Historie zu organisieren",
        cards(2, [
            card("Zentrale Versionsverwaltung", k="SO KENNEN SIE ES", icon="Database",
                 items=["Die Historie liegt auf einem Server", "Viele Aktionen brauchen eine Verbindung", "Jeder Commit wird sofort für alle sichtbar"]),
            card("Verteilte Versionsverwaltung", k="SO ARBEITET GIT", icon="Users", dark=True,
                 items=["Jede Kopie enthält die vollständige Historie", "Fast alles geschieht lokal und schnell", "Veröffentlichen ist ein eigener Schritt"]),
        ]),
        "Kein Werturteil: Beide Modelle funktionieren. Entscheidend ist, dass sich daraus andere Arbeitsgewohnheiten ergeben. Fragen Sie die Gruppe, wo sie heute auf den Server warten oder Änderungen bewusst zurückhalten.")

content(d, "m1-wechsel", "Theorie", crumb, "Drei Denkwechsel, die den Alltag verändern",
        cards(3, [
            card("Historie ist lokal", "Ein Commit ist ein persönlicher Arbeitsschritt. Er stört niemanden, bis Sie ihn teilen.", k="1"),
            card("Branches sind Alltag", "Jede Aufgabe bekommt ihren eigenen Branch. Er kostet nichts und ist in Sekunden angelegt.", k="2"),
            card("Integration ist bewusst", "Zusammenführen geschieht gezielt und geprüft, nicht nebenbei beim Aktualisieren.", k="3"),
        ]),
        "Diese drei Punkte tauchen in jedem Modul wieder auf. Wenn später Fragen kommen wie ‚Warum ist das so umständlich?‘, hilft der Verweis auf einen dieser Denkwechsel.")

uebung(d, "m1-uebung", crumb, "Unser Arbeitsablauf heute", [
    "Skizzieren Sie auf Karten den Weg einer Änderung in Ihrem Team: von der Aufgabe bis zur Auslieferung.",
    "Markieren Sie Stellen, an denen Sie warten, Konflikte lösen oder Änderungen bewusst zurückhalten.",
    "Notieren Sie, wie lange eine Änderung typischerweise unveröffentlicht bei Ihnen liegt.",
    "Stellen Sie Ihre Skizze in drei Minuten vor.",
], "25 Minuten", "Kleingruppen mit 3 bis 4 Personen", "Skizze des heutigen Ablaufs; sie bleibt bis zum Ende von Tag 2 hängen.",
    notes="Die Skizzen werden fotografiert und am Ende von Tag 2 mit dem neuen Ablauf verglichen. Achten Sie darauf, dass Wartezeiten und Konfliktstellen konkret benannt werden.")

# ---------- Modul 2 ----------
crumb = M(2, "Das Git-Modell")
d.section("Modul 02: Das Git-Modell – drei Bereiche, Snapshots und Commit-Hashes",
          "t1-02-git-modell", "Von SVN zu Git – Modul 02: Das Git-Modell")
divider(d, "m2", "02", "Das Git-Modell",
        "Wir verstehen, wo eine Änderung sich gerade befindet und was ein Commit in Git tatsächlich speichert.",
        "09:45 – 10:30 UHR · GRUNDBEGRIFFE")

content(d, "m2-bereiche", "Theorie", crumb, "Drei Bereiche auf Ihrem Rechner",
        '<div class="flow">'
        '<div class="fbox"><h3>Working Directory</h3><p class="ct">Die Dateien, an denen Sie arbeiten. Hier ändern Sie wie gewohnt.</p></div>'
        '<div class="farrow"><p class="fl">git add</p><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox"><h3>Staging Area</h3><p class="ct">Die Vormerkung: Was soll in den nächsten Commit?</p></div>'
        '<div class="farrow"><p class="fl">git commit</p><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox dark"><h3>Lokales Repository</h3><p class="ct">Die vollständige Historie aller festgehaltenen Stände.</p></div>'
        '</div><p class="under">Die Staging Area ist neu für SVN-Anwender. Sie erlaubt, aus vielen Änderungen gezielt einen sauberen Arbeitsschritt zusammenzustellen.</p>',
        "Betonen Sie die Staging Area als Werkzeug, nicht als Hürde: Sie ist die Packstation, an der ein Commit zusammengestellt wird.")

content(d, "m2-snapshots", "Theorie", crumb, "Ein Commit ist ein Schnappschuss mit Fingerabdruck",
        '<div class="flow">'
        '<div class="fbox"><p class="fl" style="font-family:\'JetBrains Mono\',monospace;font-size:24px;font-weight:600;color:#B81E3E">3f2a9c1</p><h3>Projektgerüst anlegen</h3><p class="ct">Erster Stand des Projekts</p></div>'
        '<div class="farrow"><p class="fl">Vorgänger</p><x-shape class="arr" kind="arrow-left"></x-shape></div>'
        '<div class="fbox"><p class="fl" style="font-family:\'JetBrains Mono\',monospace;font-size:24px;font-weight:600;color:#B81E3E">8c1d2e4</p><h3>Reisesuche ergänzen</h3><p class="ct">Neuer Stand, verweist auf 3f2a9c1</p></div>'
        '<div class="farrow"><p class="fl">Vorgänger</p><x-shape class="arr" kind="arrow-left"></x-shape></div>'
        '<div class="fbox dark"><p class="fl" style="font-family:\'JetBrains Mono\',monospace;font-size:24px;font-weight:600;color:#F8A5B5">9a7b6c5</p><h3>Trefferzahl begrenzen</h3><p class="ct">Aktueller Stand</p></div>'
        '</div><p class="under">Jeder Commit speichert den vollständigen Projektstand und erhält einen eindeutigen Hash statt einer fortlaufenden Nummer. So können viele Kopien unabhängig voneinander Commits erzeugen.</p>',
        "Warum keine fortlaufenden Nummern? Weil es keinen zentralen Zähler gibt. Jede Kopie erzeugt Commits unabhängig; der Hash macht sie trotzdem eindeutig. Unveränderte Dateien werden nicht doppelt gespeichert, sondern nur referenziert.")

praxis(d, "m2-praxis", crumb, "Wo steht meine Änderung gerade?", [
    "$ git status",
    "On branch main",
    "Changes not staged for commit:",
    "        modified:   src/main/resources/application.yml",
    "Untracked files:",
    "        src/main/java/de/reiseportal/Merkliste.java",
    "",
    "$ git add src/main/resources/application.yml",
    "$ git status --short",
    "! M  src/main/resources/application.yml",
    "?? src/main/java/de/reiseportal/Merkliste.java",
], [
    ("modified", "Im Working Directory geändert, noch nicht vorgemerkt."),
    ("untracked", "Neue Datei, die Git noch nicht verwaltet."),
    ("M (links)", "Vorgemerkt: Diese Änderung geht in den nächsten Commit."),
], "git status ist der wichtigste Befehl des ersten Tages. Ermutigen Sie die Teilnehmenden, ihn nach jedem Schritt auszuführen.")

uebung(d, "m2-uebung", crumb, "Die drei Bereiche erleben", [
    "Öffnen Sie in der Schulungsumgebung das Verzeichnis <b>reiseportal</b> und rufen Sie den Status ab.",
    "Ändern Sie die Trefferzahl der Suche in <b>src/main/resources/application.yml</b> und prüfen Sie den Status erneut.",
    "Merken Sie die Änderung vor und prüfen Sie, wie sich die Ausgabe verändert.",
    "Halten Sie nach jedem Schritt fest, in welchem Bereich sich die Änderung befindet.",
], "15 Minuten", "Einzelarbeit", "Eine Notiz, die den Weg der Änderung durch die drei Bereiche beschreibt.",
    notes="Hier noch nicht committen: Ziel ist das Gefühl für die Bereiche. Der erste Commit folgt in Modul 03.")

# ---------- Modul 3 ----------
crumb = M(3, "Arbeiten und festhalten")
d.section("Modul 03: Arbeiten und festhalten – der lokale Arbeitszyklus",
          "t1-03-arbeiten-und-festhalten", "Von SVN zu Git – Modul 03: Arbeiten und festhalten")
divider(d, "m3", "03", "Arbeiten und festhalten",
        "Wir legen ein Repository an, halten Änderungen fest und lesen die Historie.",
        "10:45 – 12:00 UHR · STATION 2")

content(d, "m3-zyklus", "Theorie", crumb, "Der Arbeitszyklus in Git",
        '<div class="flow">'
        '<div class="fbox"><h3>Ändern</h3><p class="ct">Dateien bearbeiten wie gewohnt</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox"><h3>Prüfen</h3><p class="ct">Was hat sich geändert?</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox"><h3>Vormerken</h3><p class="ct">Den Arbeitsschritt zusammenstellen</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox dark"><h3>Festhalten</h3><p class="ct">Commit mit klarer Beschreibung</p></div>'
        '</div><p class="under">Der Zyklus wiederholt sich viele Male am Tag, vollständig lokal. Erst später entscheiden Sie, wann Sie das Ergebnis teilen.</p>',
        "Der Zyklus läuft ohne Server. Für SVN-Anwender ist das ungewohnt: Commits entstehen häufiger und kleiner, weil sie niemanden beeinträchtigen.")

statement(d, "m3-statement", "MERKSATZ", "Ein Commit ist ein Arbeitsschritt – keine Veröffentlichung.",
          "Committen Sie oft und in kleinen Schritten. Was davon wann geteilt wird, entscheiden Sie bewusst in einem eigenen Schritt.",
          "Das ist der wichtigste Denkwechsel des ersten Tages. Lassen Sie den Satz kurz wirken und fragen Sie, was das für die eigene Arbeitsweise bedeutet.")

praxis(d, "m3-start", crumb, "Ein Repository für das Reiseportal", [
    "# Einmalig: Wer sind Sie?",
    "$ git config --global user.name \"Erika Muster\"",
    "$ git config --global user.email erika@example.com",
    "",
    "$ cd reiseportal",
    "$ git init",
    "$ git add pom.xml src/",
    "$ git commit -m \"Projektgerüst anlegen\"",
    "[main (root-commit) 3f2a9c1] Projektgerüst anlegen",
    "$ git log --oneline",
    "3f2a9c1 Projektgerüst anlegen",
], [
    ("git config", "Name und E-Mail stehen in jedem Commit. Einmal pro Rechner einrichten."),
    ("git init", "Macht das Verzeichnis zum Repository. Die Historie liegt im Ordner .git."),
    ("git log", "Liest die Historie, ganz ohne Server."),
], "In der Schulungsumgebung ist die Identität noch nicht gesetzt. Das ist Absicht, damit jeder es einmal selbst macht.")

praxis(d, "m3-diff", crumb, "Prüfen, bevor festgehalten wird", [
    "$ git diff",
    "--- a/src/main/resources/application.yml",
    "+++ b/src/main/resources/application.yml",
    "@@ -3 +3 @@",
    "-    max-ergebnisse: 50",
    "! +    max-ergebnisse: 20",
    "",
    "$ git add src/main/resources/application.yml",
    "$ git diff --staged  # zeigt den nächsten Commit",
    "$ git commit -m \"Trefferzahl der Reisesuche begrenzen\"",
    "$ git show --stat",
], [
    ("git diff", "Änderungen, die noch nicht vorgemerkt sind."),
    ("git diff --staged", "Genau das, was im nächsten Commit landen wird."),
    ("git show", "Inhalt und Beschreibung eines festgehaltenen Commits."),
], "Gewohnheit etablieren: Vor jedem Commit einmal diff --staged. Das verhindert die meisten versehentlichen Commits.")

uebung(d, "m3-uebung", crumb, "Der erste eigene Commit", [
    "Richten Sie Name und E-Mail-Adresse ein.",
    "Legen Sie die Klasse <b>Merkliste</b> in <b>src/main/java/de/reiseportal/</b> an.",
    "Prüfen Sie Ihre Änderungen und merken Sie die neue Datei vor.",
    "Halten Sie die Änderung mit einer aussagekräftigen Beschreibung fest.",
    "Ändern Sie zwei weitere Werte in <b>application.yml</b> in je einem eigenen Commit und lesen Sie die Historie.",
], "30 Minuten", "Einzelarbeit", "Eine Historie mit mindestens drei nachvollziehbaren Commits.",
    notes="Gehen Sie herum und schauen Sie auf die Commit-Beschreibungen. Gute Beispiele merken, sie sind der Einstieg in Modul 04.")

# ---------- Modul 4 ----------
crumb = M(4, "In kleinen Schritten arbeiten")
d.section("Modul 04: In kleinen Schritten arbeiten – gute Commits und Commit Messages",
          "t1-04-kleine-schritte", "Von SVN zu Git – Modul 04: In kleinen Schritten arbeiten")
divider(d, "m4", "04", "In kleinen Schritten arbeiten",
        "Wir nutzen Commits als nachvollziehbares Arbeitsprotokoll, das auch Kollegen in einem Jahr noch verstehen.",
        "13:00 – 14:00 UHR · STATION 2")

content(d, "m4-protokoll", "Theorie", crumb, "Commits als Arbeitsprotokoll",
        cards(2, [
            card("So gelingt es", k="EMPFEHLUNG", icon="CheckCircle",
                 items=["Ein Commit enthält genau eine Absicht", "Häufig committen, sobald ein Schritt fertig ist", "Vor jedem Commit prüfen, was vorgemerkt ist", "Generierte Dateien vom Repository fernhalten"]),
            card("Das vermeiden Sie", k="STOLPERFALLEN", icon="Warning",
                 items=["Der „Feierabend-Commit“ mit allem, was gerade offen ist", "Mehrere Themen in einem Commit", "Beschreibungen wie „Änderungen“ oder „fix“", "Build-Ergebnisse und Logdateien im Repository"]),
        ]),
        "In SVN war der Commit oft der Moment der Veröffentlichung und deshalb groß und selten. In Git darf er klein sein. Das macht spätere Fehlersuche und Reviews deutlich leichter.")

content(d, "m4-message", "Theorie", crumb, "Eine gute Commit Message beantwortet das Warum",
        cards(2, [
            card("Suchergebnisse nach Preis sortieren", k="GUT",
                 text="Kunden vermissen laut Feedback die Sortierung nach Preis.<br>Die Sortierung nach Relevanz bleibt als Option erhalten.", dark=True),
            card("Aufbau einer Commit Message", k="REGELN",
                 items=["Betreff mit höchstens 50 Zeichen", "Betreff im Imperativ: „anpassen“, „ergänzen“", "Leerzeile, dann das Warum", "Kein „fix“, „wip“ oder „Änderungen“"]),
        ]),
        "Die Betreffzeile erscheint in allen Übersichten. Das Warum steht im Text darunter, das Was zeigt der Diff ohnehin.")

praxis(d, "m4-ignore", crumb, "Was nicht ins Repository gehört", [
    "# Datei .gitignore im Projektverzeichnis",
    "# Build-Ergebnisse von Maven",
    "target/",
    "*.log",
    "# Lokale Einstellungen der IDE",
    ".idea/",
    "*.iml",
    "",
    "$ git add .gitignore",
    "$ git commit -m \"Build-Ausgaben ignorieren\"",
], [
    (".gitignore", "Eine Datei im Repository. Alle im Team teilen dieselben Regeln."),
    ("target/", "Ein Schrägstrich am Ende steht für ein ganzes Verzeichnis."),
    ("*.log", "Muster gelten für alle passenden Dateien im Projekt."),
], "Wichtig: .gitignore wirkt nur auf Dateien, die Git noch nicht verwaltet. Bereits erfasste Dateien müssen einmal mit git rm --cached entfernt werden.")

praxis(d, "m4-patch", crumb, "Eine Datei, zwei Absichten: gezielt vormerken", [
    "$ git add -p src/main/resources/application.yml",
    "@@ -8 +8 @@",
    "-    storno-frist-tage: 14",
    "+    storno-frist-tage: 30",
    "! Stage this hunk [y,n,q,a,d,s,e,?]? y",
    "@@ -15 +15 @@",
    "-# Timeout in Millisekunden",
    "+# Timeout für den Zahlungsdienst in ms",
    "! Stage this hunk [y,n,q,a,d,s,e,?]? n",
    "",
    "$ git commit -m \"Stornofrist auf 30 Tage erhöhen\"",
], [
    ("git add -p", "Geht die Änderungen abschnittsweise durch und fragt jeweils nach."),
    ("y / n", "Abschnitt vormerken oder für einen späteren Commit liegen lassen."),
    ("Ergebnis", "Zwei saubere Commits statt eines vermischten."),
], "Hier zeigt die Staging Area ihren Nutzen: Aus einer Datei mit zwei Themen werden zwei getrennte Arbeitsschritte.")

uebung(d, "m4-uebung", crumb, "Aufräumen in kleinen Schritten", [
    "Wechseln Sie zum vorbereiteten Stand <b>modul04</b>. Er enthält drei unabhängige Änderungen und mehrere Logdateien.",
    "Verschaffen Sie sich einen Überblick über alle Änderungen.",
    "Sorgen Sie dafür, dass Logdateien künftig ignoriert werden.",
    "Erstellen Sie drei getrennte Commits mit aussagekräftigen Beschreibungen.",
    "Vergleichen Sie Ihre Historie mit der Ihres Sitznachbarn.",
], "30 Minuten", "Einzelarbeit, Vergleich zu zweit", "Saubere Historie mit drei Commits und einer .gitignore-Datei.",
    notes="Der Stand modul04 liegt als Branch in der Schulungsumgebung bereit. Wechsel mit git switch modul04; das Konzept dahinter folgt in Modul 06.")

# ---------- Modul 5 ----------
crumb = M(5, "Sicher experimentieren")
d.section("Modul 05: Sicher experimentieren – Änderungen zurücknehmen und parken",
          "t1-05-sicher-experimentieren", "Von SVN zu Git – Modul 05: Sicher experimentieren")
divider(d, "m5", "05", "Sicher experimentieren",
        "Wir nehmen Änderungen gezielt zurück, parken Zwischenstände und wissen, welcher Weg zurück wann der richtige ist.",
        "14:00 – 15:15 UHR · STATION 2")

content(d, "m5-wege", "Theorie", crumb, "Fünf Wege zurück",
        table(["Situation", "Werkzeug", "Wirkung"], [
            ["Änderung in einer Datei verwerfen", "git restore", "Datei wie im letzten Commit"],
            ["Vormerkung zurücknehmen", "git restore --staged", "Änderung bleibt erhalten"],
            ["Arbeit kurz beiseitelegen", "git stash", "Zwischenstand wird geparkt"],
            ["Geteilten Commit aufheben", "git revert", "Neuer Commit kehrt ihn um"],
            ["Lokale Commits neu ordnen", "git reset", "Nur vor dem Teilen verwenden"],
        ], [42, 26, 32]) + '<p class="under">Faustregel: Was schon geteilt ist, wird mit einem neuen Commit korrigiert. Was nur lokal existiert, darf umgeschrieben werden.</p>',
        "Achtung bei SVN-Erfahrung: Der Name revert bedeutet in Git etwas anderes, als viele erwarten. git revert verwirft keine lokalen Änderungen, sondern erzeugt einen neuen Commit, der einen alten umkehrt.")

content(d, "m5-reset", "Theorie", crumb, "git reset: was mit den drei Bereichen geschieht",
        table(["Modus", "Repository", "Staging Area", "Working Directory"], [
            ["--soft", "zurückgesetzt", "bleibt", "bleibt"],
            ["--mixed (Standard)", "zurückgesetzt", "zurückgesetzt", "bleibt"],
            ["--hard", "zurückgesetzt", "zurückgesetzt", "zurückgesetzt, Änderungen verloren"],
        ], [24, 22, 22, 32]) +
        cards(1, [card("Nur für lokale, noch nicht geteilte Commits", "Wer bereits geteilte Commits mit reset entfernt, schreibt Historie um, auf der andere aufbauen. Dafür gibt es git revert.", k="WICHTIG")]).replace('class="cards c1"', 'class="cards c1" style="margin-top:36px"'),
        "Zeigen Sie --soft als nützliches Werkzeug: den letzten lokalen Commit wieder öffnen, um ihn besser zu formulieren oder zu ergänzen.")

praxis(d, "m5-praxis", crumb, "Ein Experiment mit der Reisesuche", [
    "$ git stash  # unfertige Arbeit parken",
    "Saved working directory and index state WIP on main",
    "$ git switch --detach 3f2a9c1  # alten Stand ansehen",
    "$ git switch main",
    "$ git stash pop  # Arbeit zurückholen",
    "",
    "# Ein Commit hat sich als falsch erwiesen:",
    "$ git revert 8c1d2e4",
    "[main 4b5c6d7] Revert \"Stornofrist auf 30 Tage erhöhen\"",
    "$ git log --oneline -3",
], [
    ("git stash", "Parkt Änderungen, damit Sie kurz etwas anderes erledigen können."),
    ("git switch --detach", "Einen früheren Stand ansehen, ohne etwas zu verändern."),
    ("git revert", "Hebt einen Commit nachvollziehbar mit einem neuen Commit auf."),
], "Hinweis: Im Detached-HEAD-Zustand nicht arbeiten, nur ansehen. Mit git switch main geht es zurück.")

uebung(d, "m5-uebung", crumb, "Der Rettungsdienst", [
    "Sie haben <b>src/main/resources/application.yml</b> versehentlich geändert. Stellen Sie den letzten Stand wieder her.",
    "Sie haben zu viele Dateien vorgemerkt. Lösen Sie die Vormerkung, ohne Änderungen zu verlieren.",
    "Mitten in der Arbeit kommt ein dringender Fix. Parken Sie Ihre Arbeit, committen Sie den Fix und holen Sie die Arbeit zurück.",
    "Ein bereits geteilter Commit war falsch. Heben Sie ihn nachvollziehbar auf.",
    "Formulieren Sie Ihren letzten lokalen Commit neu.",
], "30 Minuten", "Partnerarbeit", "Fünf gelöste Situationen; für jede notieren Sie den gewählten Weg und den Grund.",
    notes="Wichtiger als der Befehl ist die Begründung: Warum war in dieser Situation genau dieser Weg richtig?")

# ---------- Modul 6 ----------
crumb = M(6, "Ein Branch pro Aufgabe")
d.section("Modul 06: Ein Branch pro Aufgabe – Branches als alltägliches Werkzeug",
          "t1-06-branch-pro-aufgabe", "Von SVN zu Git – Modul 06: Ein Branch pro Aufgabe")
divider(d, "m6", "06", "Ein Branch pro Aufgabe",
        "Wir nutzen Branches für jede Aufgabe, arbeiten parallel und führen Ergebnisse wieder zusammen.",
        "15:30 – 16:30 UHR · STATION 1")

content(d, "m6-zeiger", "Theorie", crumb, "Ein Branch ist ein Zeiger, keine Kopie",
        '<div class="split">' +
        graph(960, 360,
              [(90, 150, "A"), (300, 150, "B"), (510, 150, "C")],
              [(0, 1), (1, 2)],
              [(510, 220, "main", "main"), (510, 270, "feature/merkliste", "br"), (510, 40, "HEAD", "head")]) +
        notes_col([("Branch", "Ein beweglicher Name, der auf einen Commit zeigt. Anlegen kostet nichts."),
                   ("HEAD", "Zeigt, auf welchem Branch Sie gerade arbeiten."),
                   ("Neuer Commit", "Der aktuelle Branch rückt automatisch weiter.")]) +
        "</div>",
        "In SVN war ein Branch eine Verzeichniskopie auf dem Server und deshalb eher selten. In Git ist er ein Name von wenigen Bytes. Daraus folgt die Arbeitsweise: ein Branch pro Aufgabe.")

content(d, "m6-merge", "Theorie", crumb, "Zusammenführen: Fast-Forward und 3-Way-Merge",
        '<div class="cards c2">'
        '<div class="gpanel"><p class="gcap">Fast-Forward</p>' +
        graph(720, 300, [(70, 150, "A"), (250, 150, "B"), (430, 150, "C"), (610, 150, "D")],
              [(0, 1), (1, 2), (2, 3)],
              [(250, 210, "main vorher", "ghost"), (610, 210, "main", "main"), (610, 50, "feature", "br")]) +
        '<p class="ct">main hat sich nicht bewegt. Der Zeiger rückt einfach vor.</p></div>'
        '<div class="gpanel"><p class="gcap">3-Way-Merge</p>' +
        graph(720, 300, [(70, 200, "A"), (250, 200, "B"), (430, 200, "C"), (430, 80, "D"), (620, 200, "M")],
              [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)],
              [(620, 250, "main", "main"), (430, 10, "config", "br")], merge=(4,)) +
        '<p class="ct">Beide Linien haben sich entwickelt. Ein Merge-Commit verbindet sie.</p></div>'
        '</div>',
        "Der Merge-Commit M hat zwei Vorgänger. Konflikte entstehen nur, wenn beide Linien dieselben Stellen geändert haben. Das Lösen von Konflikten ist Thema an Tag 2.")

praxis(d, "m6-praxis", crumb, "Neue Funktion auf eigenem Branch", [
    "$ git switch -c feature/merkliste",
    "Switched to a new branch 'feature/merkliste'",
    "$ git add src/main/java/de/reiseportal/Merkliste.java",
    "$ git commit -m \"Merkliste für Reiseangebote ergänzen\"",
    "$ git switch main",
    "$ git merge feature/merkliste",
    "Updating 9a7b6c5..a1b2c3d",
    "Fast-forward",
    "$ git branch -d feature/merkliste",
    "$ git log --oneline --graph --all",
], [
    ("git switch -c", "Legt einen Branch an und wechselt sofort dorthin."),
    ("git merge", "Holt die Arbeit eines Branches in den aktuellen Branch."),
    ("git branch -d", "Entfernt den Namen nach erledigter Aufgabe. Die Commits bleiben."),
], "Namenskonvention vorschlagen: Art der Aufgabe, Schrägstrich, kurzes Thema. Das wird an Tag 2 bei den Teamvereinbarungen wieder aufgegriffen.")

uebung(d, "m6-uebung", crumb, "Zwei Aufgaben, ein Repository", [
    "Legen Sie den Branch <b>feature/bewertungen</b> an, ergänzen Sie die Klasse <b>Bewertung</b> und committen Sie.",
    "Wechseln Sie zu main und legen Sie den Branch <b>config/reservierung</b> an. Ändern Sie dort die Reservierungsdauer in application.yml und committen Sie.",
    "Führen Sie beide Branches nacheinander in main zusammen.",
    "Welche Art von Merge entsteht jeweils? Begründen Sie es anhand der grafischen Historie.",
], "35 Minuten", "Einzelarbeit", "main enthält beide Aufgaben; Sie können erklären, warum einmal Fast-Forward und einmal ein Merge-Commit entstand.",
    notes="Die beiden Branches ändern bewusst unterschiedliche Dateien, damit hier noch keine Konflikte entstehen.")

# ---------- Modul 7 ----------
crumb = M(7, "Der kaputte Freitag")
d.section("Modul 07: Übung „Der kaputte Freitag“ – Fehlersuche in der Historie",
          "t1-07-kaputter-freitag", "Von SVN zu Git – Modul 07: Der kaputte Freitag")
divider(d, "m7", "07", "Übung: Der kaputte Freitag",
        "Wir wenden alles Gelernte an und finden in der Historie den Schritt, der die Buchungsstrecke lahmgelegt hat.",
        "16:30 – 17:00 UHR · ANWENDUNG")

praxis(d, "m7-praxis", crumb, "Spurensuche in der Historie", [
    "$ git log --oneline -10 --stat",
    "$ git log --oneline -- src/main/resources/",
    "e5f6a7b Timeout Zahlungsdienst verkürzen",
    "c3d4e5f Zahlungsart Kreditkarte ergänzen",
    "$ git show e5f6a7b",
    "$ git blame src/main/resources/application.yml",
    "e5f6a7b (Max Beispiel)     timeout-ms: 500",
    "",
    "$ git revert e5f6a7b",
], [
    ("git log -- pfad", "Nur die Commits, die bestimmte Dateien oder Verzeichnisse betreffen."),
    ("git show", "Was genau hat sich geändert, und mit welcher Begründung?"),
    ("git blame", "Welcher Commit hat welche Zeile zuletzt geändert?"),
], "git blame klingt nach Schuldfrage, dient aber der Ursachenforschung. Betonen Sie, dass gute Commit Messages genau hier ihren Wert zeigen.")

uebung(d, "m7-uebung", crumb, "Der kaputte Freitag", [
    "Ermitteln Sie, welche Dateien in den letzten zehn Commits geändert wurden.",
    "Grenzen Sie ein, welcher Commit den Fehler verursacht hat.",
    "Finden Sie heraus, wer die Änderung vorgenommen hat und mit welcher Begründung.",
    "Nehmen Sie die Änderung gezielt zurück, ohne die bestehende Historie zu verändern.",
], "25 Minuten", "Partnerarbeit", "Ein Revert-Commit, dessen Beschreibung Ursache und Lösung nennt.",
    scenario="Freitag, 14:30 Uhr: Seit dem letzten Deployment scheitert jede Buchung beim Bezahlen mit Kreditkarte. Niemand weiß, was sich geändert hat.",
    notes="Der Stand freitag liegt in der Schulungsumgebung bereit. Die Ursache ist ein zu kurzes Timeout für den Zahlungsdienst in application.yml, versteckt zwischen mehreren harmlosen Commits.")

content(d, "abschluss", "Einführung", "Abschluss Tag 1", "Rückblick und Ausblick",
        stations([1, 2], ["Erledigt: Branch je Aufgabe", "Erledigt: lokale Commits", "Morgen", "Morgen", "Morgen", "Morgen"]) +
        '<p class="legend">Heute: Stationen 1 und 2 im eigenen Repository. Morgen: Teilen, Prüfen lassen, Integrieren und Ausliefern im Team, zum Abschluss der Umzug nach GitLab.</p>',
        "Kurze Feedbackrunde: Was war heute der größte Aha-Moment, was bleibt unklar? Offene Punkte für den Rückblick morgen früh notieren.")

d.write(str(DECKS / "kapitel"))
