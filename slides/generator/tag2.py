from pathlib import Path
HERE = Path(__file__).resolve().parent
DECKS = HERE.parent / "decks"
import common
common.LOGO = "/_blob/4e7855006161d9eb10133a3a03df1cf3"
from common import *

d = Deck(str(DECKS / "tag2"), "Von SVN zu Git – Tag 2: Gemeinsam mit Git", "Von SVN zu Git · Tag 2")
M = lambda n, t: "Modul %02d · %s" % (n, t)

# ---------- Einführung ----------
d.section("Einführung: Ablauf des zweiten Tages und die Stationen 3 bis 6",
          "t2-00-einfuehrung", "Von SVN zu Git – Tag 2: Einführung")
cover(d, "cover", "Von SVN zu Git", "Git Grundlagen für Entwickler, die aus der SVN-Versionsverwaltung kommen",
      "Tag 2", "Gemeinsam mit Git: teilen, prüfen, integrieren und ausliefern",
      "Begrüßung zum zweiten Tag. Offene Fragen von gestern einsammeln und im Rückblick beantworten.")

content(d, "ablauf", "Einführung", "Kursablauf", "Der zweite Tag im Überblick",
        table(["Zeit", "Modul", "Schwerpunkt"], [
            ["09:00", "08 · Rückblick", "Tag 1 festigen"],
            ["09:30", "09 · Integrieren", "Station 5"],
            ["10:45", "10 · Teilen und abholen", "Station 3"],
            ["13:00", "11 · Gemeinsam prüfen", "Station 4"],
            ["13:45", "12 · Den Teamablauf vereinbaren", "Teamregeln"],
            ["optional", "Zusatz · Merge-Strategien, Git-Workflow", "ca. 75 und 60 Minuten"],
            ["14:45", "13 · Den Umzug planen", "Migration"],
            ["15:30", "14 · Abschlussübung „Umzugstag“", "Station 1 bis 6"],
            ["16:45", "15 · Abschluss", "Ausblick, Feedback"],
        ], [14, 56, 30]) + '<p class="under">Pausen: 10:30 Uhr · 12:00 Uhr Mittagspause · 14:30 Uhr</p>',
        "Integrieren steht bewusst vor dem Teilen: Konflikte lassen sich zunächst lokal und ohne Druck üben, bevor das Team-Repository ins Spiel kommt.")

content(d, "leitidee", "Einführung", "Leitidee", "Heute: die Stationen 3 bis 6 im Team",
        stations([3, 4, 5, 6]) + '<p class="legend">Heute im Fokus: Stationen 3 bis 6 (dunkel hervorgehoben). Die Stationen 1 und 2 aus Tag 1 bilden die Grundlage.</p>',
        "Gestern ging es um das eigene Repository. Heute kommt das Team dazu: Wie gelangt eine Änderung geprüft und nachvollziehbar in den gemeinsamen Stand?")

referenzen(d, "t2-ref", "Einführung", [
    ("Verteiltes Git", "Pro Git, Kapitel 5 · Arbeitsabläufe im Team, deutsch", "https://git-scm.com/book/de/v2/Verteiltes-Git-Verteilter-Arbeitsablauf"),
    ("Git-Workflow im Vergleich", "Atlassian Git-Tutorial · zentrale, Feature-Branch- und Gitflow-Abläufe, deutsch", "https://www.atlassian.com/de/git/tutorials/comparing-workflows"),
    ("Merge requests", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/user/project/merge_requests/"),
    ("Pro Git", "das vollständige Buch, deutsch", "https://git-scm.com/book/de/v2/"),
], "Der zweite Tag folgt im Wesentlichen Kapitel 5 von Pro Git. Für alles, was GitLab betrifft, ist die GitLab-Dokumentation maßgeblich; sie liegt nur auf Englisch vor.")

prompts(d, "t2-ki", "Einführung", [
    ("Verstehen", "Erkläre, wie ein Team mit Git und GitLab zusammenarbeitet: vom eigenen Branch über Push und Merge Request bis zum Release-Tag. Zeige, wo sich das vom Arbeiten mit einem zentralen SVN-Server unterscheidet."),
    ("Üben", "Stelle mir zehn Quizfragen zu den Stationen Teilen, Prüfen lassen, Integrieren und Ausliefern mit Git und GitLab. Frage einzeln und erkläre falsche Antworten."),
    ("Übertragen", "Wir sind fünf Entwickler und liefern alle vier Wochen aus. Skizziere einen einfachen Teamablauf mit Git und GitLab und nenne die Regeln, die wir dafür festlegen müssen."),
], "Wie an Tag 1: Die Prompts sind für die Nacharbeit gedacht. Antworten mit den Referenzen abgleichen und keinen Firmencode eingeben.")

# ---------- Modul 8 ----------
crumb = M(8, "Rückblick")
d.section("Modul 08: Rückblick auf Tag 1",
          "t2-08-rueckblick", "Von SVN zu Git – Modul 08: Rückblick")
divider(d, "m8", "08", "Rückblick",
        "Wir festigen die Grundlagen von gestern und ergänzen die Skizze unseres Arbeitsablaufs.",
        "09:00 – 09:30 UHR · TAG 1 FESTIGEN")

content(d, "m8-wiederholung", "Theorie", crumb, "Vier Grundlagen aus Tag 1",
        cards(4, [
            card("Drei Bereiche", "Working Directory, Staging Area und lokales Repository.", k="MODELL"),
            card("Commit = Arbeitsschritt", "Klein, häufig und mit einer klaren Absicht.", k="ARBEITSWEISE"),
            card("Wege zurück", "Was geteilt ist, wird mit einem neuen Commit korrigiert.", k="SICHERHEIT"),
            card("Branch = Zeiger", "Ein Branch pro Aufgabe, ohne Kosten.", k="BRANCHES", dark=True),
        ]),
        "Fragen Sie zu jeder Karte eine Person aus der Gruppe nach einem Beispiel aus den Übungen von gestern.")

praxis(d, "m8-praxis", crumb, "Die Historie von gestern lesen", [
    "$ git log --oneline --graph --all -12",
    "*   d4e5f6a Merge branch 'config/reservierung'",
    "|\\",
    "| * b2c3d4e Reservierungsdauer auf 15 Minuten senken",
    "* | a1b2c3d Kundenbewertungen ergänzen",
    "|/",
    "* 4b5c6d7 Revert \"Stornofrist auf 30 Tage erhöhen\"",
    "* 9a7b6c5 Trefferzahl der Reisesuche begrenzen",
    "* 3f2a9c1 Projektgerüst anlegen",
], [
    ("--graph", "Zeichnet Branches und Merges als Linien."),
    ("Merge-Commit", "Die Stelle, an der zwei Aufgaben zusammengeführt wurden."),
    ("Revert", "Die nachvollziehbare Korrektur aus Modul 05."),
], "Lassen Sie die Gruppe die Historie laut vorlesen: Was ist hier passiert, in welcher Reihenfolge?")

uebung(d, "m8-uebung", crumb, "Die Skizze ergänzen", [
    "Holen Sie Ihre Skizze des SVN-Arbeitsablaufs von gestern hervor.",
    "Ergänzen Sie mit andersfarbigen Karten, wie die Stationen 1 und 2 künftig mit Git ablaufen.",
    "Markieren Sie die Stellen, die noch offen sind: Teilen, Prüfen, Integrieren, Ausliefern.",
], "15 Minuten", "Dieselben Kleingruppen wie gestern", "Eine ergänzte Skizze, auf der die offenen Stationen sichtbar sind.",
    notes="Die offenen Stationen sind genau das Programm des heutigen Tages. Verweisen Sie zu Beginn jedes Moduls auf die Skizze.")

referenzen(d, "m8-ref", crumb, [
    ("Everyday Git", "Git-Referenz · die wichtigsten Befehle nach Rolle geordnet, englisch", "https://git-scm.com/docs/giteveryday"),
    ("Einfache Snapshot-Funktionen", "Pro Git, Anhang C · Befehlsübersicht", "https://git-scm.com/book/de/v2/Anhang-C:-Git-Kommandos-Einfache-Snapshot-Funktionen"),
    ("GitHub Git Spickzettel", "Befehlsübersicht zum Ausdrucken, deutsch", "https://training.github.com/downloads/de/github-git-cheat-sheet/"),
    ("Learn Git Branching", "Wiederholung im Browser, deutsch", "https://learngitbranching.js.org/?locale=de_DE"),
], "Der Spickzettel stammt von GitHub, die Befehle gelten aber unverändert für GitLab. Everyday Git ist die offizielle Kurzfassung der Git-Dokumentation.")

prompts(d, "m8-ki", crumb, [
    ("Verstehen", "Fasse die Git-Grundlagen zusammen, die man vor der Teamarbeit sicher beherrschen sollte: drei Bereiche, Commit, Branch und Rückgängigmachen. Je ein kurzer Absatz, ohne Fachjargon."),
    ("Üben", "Zeige mir die Ausgabe von git log --oneline --graph eines kleinen Repositories und stelle mir Fragen dazu: Welche Branches gibt es, wo wurde gemergt, worauf zeigt HEAD?"),
    ("Übertragen", "Erstelle mir eine einseitige Übersicht für typische Pannen: falsche Datei vorgemerkt, Commit Message vertippt, auf dem falschen Branch gearbeitet, Änderungen versehentlich verworfen."),
], "Die erzeugte Übersicht mit der Git-Rettungskarte aus dem Schulungsportal vergleichen lassen. Abweichungen sind ein guter Anlass für Rückfragen.")

# ---------- Modul 9 ----------
crumb = M(9, "Integrieren")
d.section("Modul 09: Integrieren – Merge-Konflikte verstehen und lösen",
          "t2-09-integrieren", "Von SVN zu Git – Modul 09: Integrieren")
divider(d, "m9", "09", "Integrieren",
        "Wir führen Ergebnisse bewusst zusammen und lösen Konflikte ruhig und nachvollziehbar.",
        "09:30 – 10:30 UHR · STATION 5")

content(d, "m9-konflikt", "Theorie", crumb, "Wann entsteht ein Konflikt?",
        '<div class="split">' +
        graph(960, 360, [(90, 240, "A"), (300, 240, "B"), (510, 240, "C"), (510, 100, "D"), (740, 240, "M")],
              [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)],
              [(510, 300, "main: 20 Treffer", "main"), (510, 30, "suche: 25 Treffer", "br"), (740, 300, "Konflikt", "head")], merge=(4,)) +
        notes_col([("Automatisch", "Ändern beide Linien verschiedene Stellen, führt Git sie selbst zusammen."),
                   ("Konflikt", "Ändern beide dieselbe Stelle, entscheidet ein Mensch."),
                   ("Wichtig", "Ein Konflikt ist kein Fehler, sondern eine Rückfrage.")]) +
        "</div>",
        "Viele SVN-Anwender verbinden Konflikte mit Stress beim Update. In Git ist das Zusammenführen ein eigener, bewusster Schritt: Man kann ihn vorbereiten, abbrechen und wiederholen.")

content(d, "m9-schritte", "Theorie", crumb, "Einen Konflikt in vier Schritten lösen",
        '<div class="flow">'
        '<div class="fbox"><h3>Erkennen</h3><p class="ct">Git meldet die betroffenen Dateien.</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox"><h3>Verstehen</h3><p class="ct">Beide Seiten lesen: Was war jeweils die Absicht?</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox"><h3>Entscheiden</h3><p class="ct">Den richtigen Inhalt herstellen, notfalls mit Rückfrage.</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox dark"><h3>Abschließen</h3><p class="ct">Vormerken und den Merge festhalten.</p></div>'
        '</div><p class="under">Jederzeit möglich: den Merge abbrechen und zum Stand davor zurückkehren.</p>',
        "Der zweite Schritt ist der wichtigste. Wer nur die eigene Seite übernimmt, ohne die andere zu verstehen, verliert die Arbeit eines Kollegen.")

praxis(d, "m9-praxis", crumb, "Konflikt in der Anwendungskonfiguration", [
    "$ git merge suche/trefferzahl",
    "CONFLICT (content): Merge conflict in …/application.yml",
    "Automatic merge failed; fix conflicts and then commit.",
    "# Inhalt von application.yml:",
    "! <<<<<<< HEAD",
    "    max-ergebnisse: 20",
    "! =======",
    "    max-ergebnisse: 25",
    "! >>>>>>> suche/trefferzahl",
    "$ git add src/main/resources/application.yml",
    "$ git commit  # Merge abschließen",
], [
    ("<<<<<<< HEAD", "Ihr aktueller Stand."),
    (">>>>>>> suche/…", "Der Stand, den Sie hereinholen."),
    ("git merge --abort", "Bricht ab und stellt den Stand vor dem Merge wieder her."),
], "Zeigen Sie zusätzlich ein grafisches Merge-Werkzeug, etwa die Konfliktansicht der Entwicklungsumgebung. Die Marker im Text bleiben aber die Grundlage.")

uebung(d, "m9-uebung", crumb, "Konflikte gezielt herbeiführen", [
    "Legen Sie zwei Branches an und ändern Sie in beiden dieselbe Zeile in <b>application.yml</b>.",
    "Führen Sie die Branches zusammen und lösen Sie den Konflikt.",
    "Wiederholen Sie das mit einer Java-Klasse, ändern Sie diesmal aber benachbarte Zeilen. Was passiert?",
    "Starten Sie einen weiteren Merge und brechen Sie ihn bewusst ab.",
], "30 Minuten", "Partnerarbeit", "Zwei gelöste Konflikte und ein abgebrochener Merge in der Historie.",
    notes="Benachbarte Zeilen führen in der Regel ebenfalls zu einem Konflikt, weil Git Änderungen abschnittsweise vergleicht. Gute Gelegenheit, über kleine, fokussierte Commits zu sprechen.")

referenzen(d, "m9-ref", crumb, [
    ("Einfaches Branching und Merging", "Pro Git, Kapitel 3.2 · Abschnitt Merge-Konflikte", "https://git-scm.com/book/de/v2/Git-Branching-Einfaches-Branching-und-Merging"),
    ("Fortgeschrittenes Merging", "Pro Git, Kapitel 7.8 · Konflikte untersuchen und abbrechen", "https://git-scm.com/book/de/v2/Git-Tools-Fortgeschrittenes-Merging"),
    ("Wie löst man Merge-Konflikte in Git?", "Atlassian Git-Tutorial, deutsch", "https://www.atlassian.com/de/git/tutorials/using-branches/merge-conflicts"),
    ("Merge conflicts", "GitLab-Dokumentation · Konflikte im Merge Request lösen, englisch", "https://docs.gitlab.com/user/project/merge_requests/conflicts/"),
    ("git merge", "Git-Referenz · Konfliktmarkierungen und Strategien, englisch", "https://git-scm.com/docs/git-merge"),
], "Kapitel 7.8 zeigt, wie man einen Konflikt mit git diff und git log --merge untersucht, bevor man ihn löst. Die GitLab-Seite beschreibt, welche Konflikte direkt im Browser lösbar sind.")

prompts(d, "m9-ki", crumb, [
    ("Verstehen", "Erkläre, wann Git einen Merge-Konflikt meldet und wann es Änderungen automatisch zusammenführt. Zeige an einer YAML-Datei, wie Konfliktmarkierungen aussehen und was jeder Abschnitt bedeutet."),
    ("Üben", "Erzeuge drei Konflikte unterschiedlicher Schwierigkeit in einer application.yml, jeweils mit Konfliktmarkierungen. Ich schreibe die aufgelöste Fassung, du prüfst sie und erklärst Fehler."),
    ("Übertragen", "Wie können wir Merge-Konflikte im Team seltener machen? Nenne konkrete Maßnahmen zu Branch-Dauer, Dateistruktur und Formatierung für Java-Code und Konfigurationsdateien."),
], "Der Übungs-Prompt setzt die Übung dieses Moduls fort. Beim dritten Prompt auf einheitliche Formatierung (Formatter, .editorconfig) und kurze Branches achten.")

# ---------- Modul 10 ----------
crumb = M(10, "Teilen und abholen")
d.section("Modul 10: Teilen und abholen – mit Remote-Repositories arbeiten",
          "t2-10-teilen-und-abholen", "Von SVN zu Git – Modul 10: Teilen und abholen")
divider(d, "m10", "10", "Teilen und abholen",
        "Wir arbeiten mit dem gemeinsamen Repository in GitLab und entscheiden bewusst, wann wir einen Stand teilen.",
        "10:45 – 12:00 UHR · STATION 3")

content(d, "m10-remote", "Theorie", crumb, "Ihre Kopie und die gemeinsame Kopie",
        '<div class="flow">'
        '<div class="fbox"><h3>Lokales Repository</h3><p class="ct">Ihre vollständige Kopie. Hier entstehen Commits und Branches.</p></div>'
        '<div class="farrow"><p class="fl">git push</p><x-shape class="arr" kind="arrow-right"></x-shape>'
        '<x-shape class="arr" kind="arrow-left"></x-shape><p class="fl">git fetch</p></div>'
        '<div class="fbox dark"><h3>Remote in GitLab</h3><p class="ct">Die gemeinsame Kopie des Teams, üblicherweise origin genannt.</p></div>'
        '</div><p class="under">Beide Kopien sind gleichwertig. Das Remote ist nur die Stelle, auf die sich das Team geeinigt hat.</p>',
        "Technisch gibt es keinen Server im Sinne von SVN. GitLab hält eine weitere Kopie, die das Team als gemeinsamen Treffpunkt nutzt.")

content(d, "m10-tracking", "Theorie", crumb, "Was Sie über den Stand des Teams wissen",
        cards(4, [
            card("main", "Ihr lokaler Stand dieses Branches.", k="LOKAL"),
            card("origin/main", "Ihr letzter Blick auf den Stand in GitLab.", k="ERINNERUNG"),
            card("fetch", "Aktualisiert diesen Blick, ohne Ihre Arbeit zu verändern.", k="ABHOLEN"),
            card("pull", "Abholen und gleich in den lokalen Branch integrieren.", k="ABHOLEN UND INTEGRIEREN", dark=True),
        ]),
        "Empfehlung für den Einstieg: lieber fetch und bewusst integrieren als blind pull. So sieht man vorher, was ankommt.")

statement(d, "m10-statement", "MERKSATZ", "Veröffentlichen ist eine Entscheidung.",
          "Mit push teilen Sie einen Stand mit dem Team. Bis dahin gehört er Ihnen und darf sich noch ändern.",
          "Verbindung zu Modul 05: Alles vor dem push darf umgeschrieben werden, alles danach wird mit neuen Commits korrigiert.")

praxis(d, "m10-praxis", crumb, "Mit dem Team-Repository arbeiten", [
    "$ git clone https://gitlab.example.com/team/reiseportal",
    "$ cd reiseportal",
    "$ git switch -c feature/gutscheine",
    "$ git add src/main/java/de/reiseportal/Gutschein.java",
    "$ git commit -m \"Gutscheine bei der Buchung einlösen\"",
    "$ git push -u origin feature/gutscheine",
    "",
    "$ git fetch  # Was gibt es Neues?",
    "$ git log --oneline main..origin/main",
    "$ git switch main",
    "$ git pull",
], [
    ("git clone", "Holt die vollständige Kopie samt Historie."),
    ("git push -u", "Teilt den Branch und merkt sich die Verbindung."),
    ("main..origin/main", "Zeigt Commits, die in GitLab neu sind."),
], "In der Schulungsumgebung hat jedes Team eine eigene GitLab-Gruppe mit dem vorbereiteten Repository.")

uebung(d, "m10-uebung", crumb, "Erste Schritte im Team-Repository", [
    "Klonen Sie das Repository Ihres Teams aus GitLab.",
    "Legen Sie einen eigenen Branch an, ergänzen Sie eine kleine Funktion und teilen Sie den Branch.",
    "Holen Sie die Branches Ihrer Teamkollegen ab und sehen Sie sich deren Commits an.",
    "Ein Teammitglied ändert main in GitLab. Holen Sie die Änderung ab und integrieren Sie sie.",
], "35 Minuten", "Teams mit 3 bis 4 Personen", "Jede Person hat einen geteilten Branch; alle lokalen main-Branches sind auf dem gleichen Stand.",
    notes="Für Schritt 4 eignet sich der Web-Editor von GitLab. So sehen alle, dass auch Änderungen außerhalb des eigenen Rechners abgeholt werden müssen.")

referenzen(d, "m10-ref", crumb, [
    ("Mit Remotes arbeiten", "Pro Git, Kapitel 2.5", "https://git-scm.com/book/de/v2/Git-Grundlagen-Mit-Remotes-arbeiten"),
    ("Remote-Branches", "Pro Git, Kapitel 3.5 · Tracking-Branches, ahead und behind", "https://git-scm.com/book/de/v2/Git-Branching-Remote-Branches"),
    ("git fetch", "Git-Referenz, englisch", "https://git-scm.com/docs/git-fetch"),
    ("git pull", "Git-Referenz, englisch", "https://git-scm.com/docs/git-pull"),
    ("git push", "Git-Referenz, englisch", "https://git-scm.com/docs/git-push"),
], "Kapitel 3.5 erklärt die Tracking-Beziehung zwischen lokalem Branch und origin/main ausführlicher als dieses Modul. Bei Fragen zu pull mit Rebase oder Merge auf die Referenz zu git pull verweisen.")

prompts(d, "m10-ki", crumb, [
    ("Verstehen", "Erkläre den Unterschied zwischen git fetch, git pull und git push und was origin/main genau ist. Nutze dafür ein Bild mit meinem Rechner und dem GitLab-Server."),
    ("Üben", "Zeige mir Ausgaben von git status mit Angaben wie „ahead 2“ oder „behind 3“ und frage mich, was ich jeweils tun sollte, bevor ich meine Arbeit teile."),
    ("Übertragen", "Mein git push wird abgelehnt, weil der Remote-Branch neuere Commits enthält. Erkläre, warum das passiert, und vergleiche die Lösung mit Merge und mit Rebase."),
], "Der dritte Prompt leitet zu Modul 12 über, in dem Rebase und Merge gegenübergestellt werden.")

# ---------- Modul 11 ----------
crumb = M(11, "Gemeinsam prüfen")
d.section("Modul 11: Gemeinsam prüfen – Merge Requests und Code Review",
          "t2-11-gemeinsam-pruefen", "Von SVN zu Git – Modul 11: Gemeinsam prüfen")
divider(d, "m11", "11", "Gemeinsam prüfen",
        "Wir bringen Änderungen über Merge Requests in die Hauptlinie und prüfen sie gemeinsam.",
        "13:00 – 13:45 UHR · STATION 4")

content(d, "m11-mr", "Theorie", crumb, "Der Merge Request: der Weg in die Hauptlinie",
        '<div class="flow">'
        '<div class="fbox"><h3>Branch teilen</h3><p class="ct">Die Aufgabe ist lokal erledigt.</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox"><h3>Merge Request</h3><p class="ct">Beschreibung: was und warum.</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox"><h3>Review und Pipeline</h3><p class="ct">Kollegen und Tests prüfen.</p></div>'
        '<div class="farrow slim"><x-shape class="arr" kind="arrow-right"></x-shape></div>'
        '<div class="fbox dark"><h3>Merge</h3><p class="ct">Geprüft in main übernommen.</p></div>'
        '</div><p class="under">Protected Branches sorgen dafür, dass main nur über diesen Weg verändert wird.</p>',
        "Der Merge Request ersetzt den direkten Commit auf den Trunk. Er bündelt Diskussion, Review und Testergebnisse an einer Stelle.")

content(d, "m11-review", "Theorie", crumb, "Gute Reviews entstehen auf beiden Seiten",
        cards(3, [
            card("Für Autoren", k="ROLLE", items=["Merge Requests klein halten", "Das Warum beschreiben", "Erst selbst prüfen, dann anfragen"]),
            card("Für Reviewer", k="ROLLE", items=["Fragen statt Urteile", "Konkret auf Zeilen verweisen", "Zeitnah antworten"]),
            card("Für das Team", k="REGELN", dark=True, items=["main ist geschützt", "Mindestens eine Freigabe", "Pipeline muss grün sein"]),
        ]),
        "Review ist kein Kontrollinstrument, sondern geteiltes Wissen: Nach einem Review kennen mindestens zwei Personen jede Änderung.")

praxis(d, "m11-praxis", crumb, "Vom Push zum Merge Request", [
    "$ git push -u origin feature/gutscheine",
    "remote: To create a merge request, visit:",
    "remote: https://gitlab.example.com/…/merge_requests/new",
    "",
    "# Alternativ direkt beim Push anlegen:",
    "$ git push -o merge_request.create \\",
    ">   -o merge_request.target=main",
    "",
    "# Anmerkung aus dem Review umsetzen:",
    "$ git commit -am \"Ablaufdatum laut Review prüfen\"",
    "$ git push  # Merge Request aktualisiert sich",
], [
    ("Link im Push", "GitLab bietet nach dem Push direkt an, einen Merge Request anzulegen."),
    ("-o merge_request.*", "Push-Optionen legen den Merge Request ohne Weboberfläche an."),
    ("Weitere Commits", "Landen automatisch im offenen Merge Request."),
], "Zeigen Sie die Weboberfläche parallel: Beschreibung, Änderungen, Kommentare an Zeilen, Freigabe und Merge-Schaltfläche.")

uebung(d, "m11-uebung", crumb, "Review im Team", [
    "Öffnen Sie für Ihren Branch einen Merge Request mit einer Beschreibung, die das Warum erklärt.",
    "Prüfen Sie den Merge Request eines Teamkollegen und hinterlassen Sie mindestens zwei Kommentare.",
    "Setzen Sie die Anmerkungen zu Ihrem Merge Request um.",
    "Geben Sie frei und führen Sie den Merge durch.",
    "Versuchen Sie, direkt auf main zu pushen. Was passiert?",
], "30 Minuten", "Teams mit 3 bis 4 Personen", "Mindestens zwei geprüfte und gemergte Merge Requests je Team.",
    notes="main ist in den Team-Repositories bereits geschützt. Der abgelehnte Push in Schritt 5 ist beabsichtigt.")

referenzen(d, "m11-ref", crumb, [
    ("Merge requests", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/user/project/merge_requests/"),
    ("Merge request approvals", "GitLab-Dokumentation · Freigaberegeln, englisch", "https://docs.gitlab.com/user/project/merge_requests/approvals/"),
    ("Google Engineering Practices: Code Review", "Leitfaden für Autoren und Reviewer, englisch", "https://google.github.io/eng-practices/review/"),
    ("Conventional Comments", "Kennzeichnung von Review-Kommentaren, englisch", "https://conventionalcomments.org/"),
    ("An einem Projekt mitwirken", "Pro Git, Kapitel 5.2", "https://git-scm.com/book/de/v2/Verteiltes-Git-An-einem-Projekt-mitwirken"),
], "Der Google-Leitfaden ist in zwei Teile für Autoren und Reviewer gegliedert, wie die Slide zu guten Reviews. Conventional Comments hilft, Vorschläge von verbindlichen Änderungswünschen zu unterscheiden.")

prompts(d, "m11-ki", crumb, [
    ("Verstehen", "Was gehört in eine gute Merge-Request-Beschreibung? Erstelle eine Vorlage für GitLab mit Abschnitten für Zweck, Änderungen, Tests und offene Fragen."),
    ("Üben", "Schreibe einen kleinen Java-Diff mit drei versteckten Schwächen. Ich formuliere Review-Kommentare, und du bewertest Inhalt und Ton meiner Kommentare."),
    ("Übertragen", "Welche Regeln für Merge Requests passen zu einem Team mit fünf Personen: Größe, Anzahl der Freigaben, Pipeline-Pflicht, Antwortzeit? Begründe jede Regel."),
], "Der Übungs-Prompt lässt die KI den Code erzeugen. So muss niemand eigenen Firmencode einfügen. Die Vorlage aus dem ersten Prompt kann als .gitlab/merge_request_templates/ ins Repository.")

# ---------- Modul 12 ----------
crumb = M(12, "Den Teamablauf vereinbaren")
d.section("Modul 12: Den Teamablauf vereinbaren – Branching-Strategien und Spielregeln",
          "t2-12-teamablauf", "Von SVN zu Git – Modul 12: Den Teamablauf vereinbaren")
divider(d, "m12", "12", "Den Teamablauf vereinbaren",
        "Wir wählen eine Branching-Strategie, die zum Team passt, und halten unsere Spielregeln fest.",
        "13:45 – 14:30 UHR · TEAMREGELN")

content(d, "m12-strategien", "Theorie", crumb, "Zwei bewährte Abläufe",
        cards(2, [
            card("GitLab Flow", k="FEATURE-BRANCHES", items=["Ein Branch pro Aufgabe, Merge Request in main", "main ist jederzeit lieferbar", "Bei Bedarf Branches für Umgebungen oder Releases", "Guter Einstieg für SVN-Teams"]),
            card("Trunk-based Development", k="KURZE BRANCHES", dark=True, items=["Branches leben nur Stunden", "Mehrmals täglich in main integrieren", "Setzt automatisierte Tests voraus", "Unfertiges hinter Feature Toggles"]),
        ]),
        "Für Teams, die aus SVN kommen, ist GitLab Flow meist der natürliche Einstieg. Trunk-based Development ist ein lohnendes Ziel, sobald Tests und Pipeline stabil laufen.")

content(d, "m12-rebase", "Theorie", crumb, "Rebase oder Merge: zwei Arten, Historie zu erzählen",
        '<div class="cards c2">'
        '<div class="gpanel"><p class="gcap">Merge</p>' +
        graph(720, 300, [(70, 200, "A"), (250, 200, "B"), (430, 200, "C"), (430, 80, "D"), (620, 200, "M")],
              [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)],
              [(620, 250, "main", "main"), (430, 10, "feature", "br")], merge=(4,)) +
        '<p class="ct">Die parallele Entwicklung bleibt sichtbar.</p></div>'
        '<div class="gpanel"><p class="gcap">Rebase</p>' +
        graph(720, 300, [(70, 150, "A"), (250, 150, "B"), (430, 150, "C"), (610, 150, "D′")],
              [(0, 1), (1, 2), (2, 3)],
              [(430, 210, "main", "main"), (610, 210, "feature", "br")]) +
        '<p class="ct">Der Branch wird auf den neuen Stand gesetzt. Die Historie bleibt gerade.</p></div>'
        '</div><p class="under">Regel: Nur eigene, noch nicht von anderen genutzte Branches rebasen.</p>',
        "Rebase erzeugt neue Commits (D′). Wer bereits auf D aufgebaut hat, bekommt Probleme. Deshalb gilt die Regel aus Modul 05 auch hier: Geteiltes nicht umschreiben.")

praxis(d, "m12-praxis", crumb, "Den eigenen Branch aktualisieren", [
    "$ git switch feature/gutscheine",
    "$ git fetch",
    "$ git rebase origin/main",
    "Successfully rebased and updated refs/heads/feature/…",
    "$ git push --force-with-lease",
    "",
    "# Alternativ mit Merge:",
    "$ git merge origin/main",
    "$ git push",
], [
    ("git rebase", "Setzt die eigenen Commits auf den aktuellen Stand von main."),
    ("--force-with-lease", "Überschreibt den eigenen Branch nur, wenn niemand sonst dort gearbeitet hat."),
    ("Teamregel", "Einmal festlegen, welcher Weg gilt, und dabei bleiben."),
], "Niemals --force ohne with-lease. Und niemals auf main oder anderen gemeinsam genutzten Branches.")

uebung(d, "m12-uebung", crumb, "Spielregeln für unser Team", [
    "Einigen Sie sich auf eine Branching-Strategie und begründen Sie die Wahl.",
    "Legen Sie Namensregeln für Branches und die Mindestanforderungen an Merge Requests fest.",
    "Entscheiden Sie: Rebase oder Merge beim Aktualisieren von Branches?",
    "Halten Sie die Regeln in <b>CONTRIBUTING.md</b> fest und bringen Sie die Datei per Merge Request in main.",
], "30 Minuten", "Teams mit 3 bis 4 Personen", "Eine abgestimmte CONTRIBUTING.md in main, angenommen über einen Merge Request.",
    notes="Die Regeln müssen nicht perfekt sein. Wichtig ist, dass das Team sie gemeinsam beschließt und später anpassen kann.")

referenzen(d, "m12-ref", crumb, [
    ("What is GitLab Flow?", "GitLab, englisch", "https://about.gitlab.com/topics/version-control/what-is-gitlab-flow/"),
    ("Trunk Based Development", "Paul Hammant · Website zur Strategie, englisch", "https://trunkbaseddevelopment.com/"),
    ("Patterns for Managing Source Code Branches", "Martin Fowler · Branching-Strategien im Vergleich, englisch", "https://martinfowler.com/articles/branching-patterns.html"),
    ("Zusammenführen oder Rebase durchführen", "Atlassian Git-Tutorial, deutsch", "https://www.atlassian.com/de/git/tutorials/merging-vs-rebasing"),
    ("Protected branches", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/user/project/repository/branches/protected/"),
], "Der Artikel von Martin Fowler ist lang, aber die gründlichste Darstellung der Abwägungen zwischen den Strategien. Für die CONTRIBUTING.md der Übung ist die Seite zu Protected Branches hilfreich.")

prompts(d, "m12-ki", crumb, [
    ("Verstehen", "Vergleiche GitLab Flow, Trunk-based Development und Gitflow: Für welche Teams und Auslieferungsrhythmen eignet sich welche Strategie, und welche Voraussetzungen braucht sie?"),
    ("Üben", "Erkläre den Unterschied zwischen Merge und Rebase mit ASCII-Graphen. Stelle mir danach drei Situationen vor, und ich entscheide, ob Rebase dort unbedenklich ist."),
    ("Übertragen", "Hilf mir, eine CONTRIBUTING.md für unser Team zu schreiben. Frage mich nacheinander nach Branching-Strategie, Branch-Namen, Commit Messages und Regeln für Merge Requests."),
], "Der dritte Prompt entspricht der Übung dieses Moduls und eignet sich, um die CONTRIBUTING.md im eigenen Team zu wiederholen.")

exec((HERE / "merge_module.py").read_text(encoding="utf-8"))
exec((HERE / "workflow_module.py").read_text(encoding="utf-8"))

# ---------- Modul 13 ----------
crumb = M(13, "Den Umzug planen")
d.section("Modul 13: Den Umzug planen – ein SVN-Repository mit Historie migrieren",
          "t2-13-umzug-planen", "Von SVN zu Git – Modul 13: Den Umzug planen")
divider(d, "m13", "13", "Den Umzug planen",
        "Wir klären die Fragen, die vor einer Migration von SVN nach Git beantwortet sein müssen.",
        "14:45 – 15:30 UHR · MIGRATION")

content(d, "m13-fragen", "Theorie", crumb, "Vier Fragen vor dem Umzug",
        cards(2, [
            card("Wie viel Historie?", "Vollständig übernehmen oder ab einem Stichtag neu beginnen?", k="HISTORIE"),
            card("Welche Struktur?", "Aus trunk, branches und tags werden Branches und Tags.", k="STRUKTUR"),
            card("Welche Abhängigkeiten?", "Verweise auf andere Repositories als Maven-Abhängigkeiten oder Submodule abbilden.", k="ABHÄNGIGKEITEN"),
            card("Welche großen Dateien?", "Große Binärdateien mit Git LFS verwalten, damit Klonen schnell bleibt.", k="BINÄRDATEIEN"),
        ]),
        "Dazu kommt immer die Zuordnung der SVN-Benutzernamen zu vollständigen Git-Identitäten mit Name und E-Mail-Adresse.")

content(d, "m13-ablauf", "Theorie", crumb, "Ablauf einer Migration",
        cards(3, [
            card("Bestand analysieren", "Struktur, Größe, Abhängigkeiten, Autoren.", k="SCHRITT 1"),
            card("Autoren zuordnen", "SVN-Benutzer zu Name und E-Mail.", k="SCHRITT 2"),
            card("Probelauf", "Migration auf einer Kopie, Ergebnis prüfen.", k="SCHRITT 3"),
            card("Team vorbereiten", "Schulung, Teamregeln, Schutz von main.", k="SCHRITT 4"),
            card("Stichtag", "SVN schreibgeschützt, letzter Abgleich.", k="SCHRITT 5"),
            card("Arbeiten in GitLab", "Das Team arbeitet ab jetzt in GitLab.", k="SCHRITT 6", dark=True),
        ]),
        "Der Probelauf ist der wichtigste Schritt. Er zeigt, ob Branches, Tags und Autoren korrekt übernommen werden, ohne dass das Team schon umziehen muss.")

praxis(d, "m13-autoren", crumb, "Autoren ermitteln", [
    "$ svn checkout https://svn.example.com/reiseportal",
    "$ cd reiseportal",
    "$ svn log -q > svn.log",
    "$ cat svn.log | awk -F '|' '/^r/ {",
    ">     sub(\"^ \", \"\", $2); sub(\" $\", \"\", $2)",
    ">     print $2\" = \"$2\" <\"$2\">\"",
    ">   }' | sort -u > authors.txt",
    "",
    "$ cat authors.txt",
    "mmuster = mmuster <mmuster>",
    "tschulz = tschulz <tschulz>",
], [
    ("svn log -q", "Listet alle Revisionen mit Autor und Datum, ohne Commit-Nachrichten."),
    ("awk", "Schneidet den Benutzernamen aus der zweiten Spalte und baut daraus eine Zeile im Format der Autorenzuordnung."),
    ("sort -u", "Jeder SVN-Benutzer erscheint genau einmal."),
], "svn log arbeitet auch direkt mit der URL des Repositorys, dann ist kein Checkout nötig. Wichtig ist, dass die gesamte Historie erfasst wird, nicht nur der Teil einer Arbeitskopie.",
    lead="Schritt 1: alle SVN-Benutzer aus der Historie in eine Datei authors.txt schreiben.")

praxis(d, "m13-autoren-ergaenzen", crumb, "Die Autorenzuordnung vervollständigen", [
    "# Vorher: aus svn.log erzeugt",
    "mmuster = mmuster <mmuster>",
    "tschulz = tschulz <tschulz>",
    "jenkins = jenkins <jenkins>",
    "",
    "# Nachher: Name und E-Mail ergänzt",
    "mmuster = Max Muster <max.muster@example.com>",
    "tschulz = Tina Schulz <tina.schulz@example.com>",
    "jenkins = Build-Server <build@example.com>",
], [
    ("Links", "Der SVN-Benutzername bleibt unverändert."),
    ("Rechts", "So erscheint die Person künftig in Git: vollständiger Name und E&#8209;Mail-Adresse."),
    ("Lücken", "Fehlt ein Benutzer, bricht git svn an dieser Revision ab."),
], "Ausgeschiedene Kolleginnen und Kollegen sowie technische Benutzer wie Build-Server bekommen ebenfalls einen Eintrag, notfalls mit einer Sammeladresse. Frühe Revisionen enthalten manchmal den Benutzer „(no author)“, auch er braucht eine Zeile.",
    lead="Schritt 2: Jeder Eintrag bekommt den Namen und die E-Mail-Adresse der Person.")

praxis(d, "m13-clone", crumb, "Schrittweise migrieren", [
    "$ git svn clone https://svn.example.com/reiseportal \\",
    ">   --authors-file=authors.txt --prefix=svn/ \\",
    ">   --trunk=trunk/ --branches=branches/ \\",
    ">   --tags=tags/ -r 1:2000 reiseportal-git",
    "$ cd reiseportal-git",
    "$ git svn fetch -r 2001:4000",
    "$ git svn fetch  # restliche Revisionen bis HEAD",
    "",
    "$ git branch -r",
    "  svn/merkliste",
    "  svn/tags/1.0",
    "  svn/trunk",
], [
    ("--trunk, --branches, --tags", "Wo Hauptlinie, Branches und Tags im SVN-Repository liegen."),
    ("--prefix=svn/", "Die SVN-Stände erscheinen in Git als svn/trunk, svn/&lt;Branch&gt; und svn/tags/&lt;Tag&gt;."),
    ("-r von:bis", "Übernimmt die Historie in Etappen. Jedes git svn fetch setzt dort fort."),
], "Große Repositories mit vielen tausend Revisionen brauchen für den Klon Stunden. In Etappen lässt sich die Migration unterbrechen und fortsetzen, und erste Ergebnisse lassen sich früh prüfen.",
    lead="Schritt 3: die Historie mit git svn übernehmen, bei großen Repositories in Etappen.")

praxis(d, "m13-tags", crumb, "SVN-Tags in Git-Tags umwandeln", [
    "$ git for-each-ref refs/remotes/svn/tags \\",
    ">   | grep -v @ | cut -d / -f 5- \\",
    ">   | while read ref; do",
    ">       git tag \"$ref\" \"refs/remotes/svn/tags/$ref\"",
    ">     done",
    "",
    "$ git tag",
    "1.0",
    "1.1",
    "$ git remote add origin <GitLab-URL>",
    "$ git push --tags",
], [
    ("Ausgangslage", "In SVN sind Tags Kopien in einem Verzeichnis. git svn legt sie deshalb als Branches unter svn/tags/ ab."),
    ("grep -v @", "Lässt Hilfsstände wie 1.0@1234 aus, die git svn für gelöschte oder neu angelegte Tags anlegt."),
    ("cut -d / -f 5-", "Behält nur den Namen des Tags."),
], "Die Tags zeigen danach auf genau den Commit, den der SVN-Tag markiert hat. Wurde in SVN nach dem Taggen noch im Tag-Verzeichnis committet, ist das an dieser Stelle zu prüfen.",
    lead="Schritt 4: Aus den Tag-Verzeichnissen von SVN werden echte Git-Tags.")

praxis(d, "m13-branches", crumb, "SVN-Branches als Git-Branches anlegen", [
    "$ git for-each-ref | grep -v tags \\",
    ">   | grep -v @ | grep -v %20 \\",
    ">   | grep -v trunk | grep -v main \\",
    ">   | cut -d / -f 4- \\",
    ">   | while read ref; do",
    ">       git branch \"$ref\" \"refs/remotes/svn/$ref\"",
    ">     done",
    "$ git branch",
    "* main",
    "  merkliste",
    "$ git push --all",
], [
    ("grep -v", "Lässt Tags, Hilfsstände mit @, Namen mit Leerzeichen (%20), trunk und main aus."),
    ("trunk", "Wird nicht kopiert: Der lokale Branch main ist beim Klonen bereits aus svn/trunk entstanden."),
    ("git push --all", "Teilt alle lokalen Branches in GitLab."),
], "Branches mit Leerzeichen im Namen werden von Hand mit einem gültigen Git-Namen angelegt. Vorher mit dem Team klären, welche alten Branches überhaupt noch gebraucht werden.",
    lead="Schritt 5: Für jeden SVN-Branch entsteht ein lokaler Git-Branch.")

praxis(d, "m13-sync", crumb, "Bis zum Stichtag mit SVN abgleichen", [
    "$ git svn fetch --authors-file=authors.txt",
    "",
    "# Neue Revisionen im trunk",
    "$ git switch main",
    "$ git merge svn/trunk",
    "$ git push",
    "",
    "# Neue Revisionen in einem Branch",
    "$ git switch merkliste",
    "$ git merge svn/merkliste",
    "",
    "# Neue Branches oder Tags: Skripte erneut ausführen",
], [
    ("git svn fetch", "Holt die Revisionen, die seit dem letzten Abgleich in SVN entstanden sind."),
    ("authors.txt", "Neue SVN-Benutzer vorher ergänzen, sonst bricht der Abgleich ab."),
    ("Richtung", "Bis zum Stichtag wird nur in SVN gearbeitet, Git spiegelt den Stand."),
], "Solange das Team noch in SVN arbeitet, bleibt das Git-Repository ein Spiegel. Weil auf main in Git nicht committet wird, sind die Merges reine Fast-Forwards. Am Stichtag wird SVN schreibgeschützt, ein letzter Abgleich läuft, danach arbeitet das Team nur noch in GitLab.",
    lead="Übergangsphase: Das Team arbeitet weiter in SVN, Git wird regelmäßig nachgezogen.")

uebung(d, "m13-uebung", crumb, "Ein Migrationsplan für das Reiseportal", [
    "Analysieren Sie die vorbereitete Übersicht des SVN-Repositorys des Reiseportals.",
    "Beantworten Sie die vier Fragen: Historie, Struktur, Abhängigkeiten, Binärdateien.",
    "Erstellen Sie die Autorenzuordnung für alle beteiligten SVN-Benutzer.",
    "Legen Sie Ablauf und Stichtag für den Umzug fest.",
], "25 Minuten", "Teams mit 3 bis 4 Personen", "Ein Migrationsplan auf einer Seite, der in der Abschlussübung umgesetzt wird.",
    notes="Die Übersicht enthält: trunk, drei Branches, zwölf Tags, einen externen Verweis (svn:externals) auf eine gemeinsame Bibliothek und einen Ordner mit großen Bild- und Videodateien der Reiseziele.")

referenzen(d, "m13-ref", crumb, [
    ("Migration zu Git", "Pro Git, Kapitel 9.2 · Abschnitt Subversion", "https://git-scm.com/book/de/v2/Git-und-andere-VCS-Systeme-Migration-zu-Git"),
    ("Git als Client", "Pro Git, Kapitel 9.1 · git svn im Parallelbetrieb", "https://git-scm.com/book/de/v2/Git-und-andere-VCS-Systeme-Git-als-Client"),
    ("git svn", "Git-Referenz · alle Optionen, englisch", "https://git-scm.com/docs/git-svn"),
    ("Migrate from Subversion", "GitLab-Dokumentation · empfohlene Werkzeuge, englisch", "https://docs.gitlab.com/user/import/#migrate-from-subversion"),
    ("Von SVN zu Git migrieren", "Atlassian Git-Tutorial, deutsch", "https://www.atlassian.com/de/git/tutorials/migrating-overview"),
], "Kapitel 9.2 enthält die Schritte dieses Moduls einschließlich der Autorendatei und der Umwandlung von Tags. GitLab empfiehlt git svn nur für kleine, einfache Repositories und nennt für große und verzweigte Repositories reposurgeon.")

prompts(d, "m13-ki", crumb, [
    ("Verstehen", "Erkläre die Schritte einer Migration von SVN nach Git mit git svn: Autorendatei, Klonen mit Standardlayout, Umwandlung von Tags und Branches, Abgleich bis zum Stichtag."),
    ("Üben", "Unser SVN-Repository hat ein Standardlayout, 15 Jahre Historie und 40 Autoren. Stelle mir Fragen für einen Migrationsplan und fasse ihn am Ende als Checkliste zusammen."),
    ("Hintergrund", "Wann reicht git svn für eine Migration aus, und wann sind Werkzeuge wie reposurgeon besser geeignet? Nenne Merkmale eines SVN-Repositories, die eine Migration erschweren."),
], "Der Übungs-Prompt ergänzt die Übung „Ein Migrationsplan für das Reiseportal“. Keine echten Server-Adressen oder Benutzernamen in den Prompt schreiben.")

# ---------- Modul 14 ----------
crumb = M(14, "Umzugstag")
d.section("Modul 14: Abschlussübung „Umzugstag“ – alle sechs Stationen im Team",
          "t2-14-umzugstag", "Von SVN zu Git – Modul 14: Abschlussübung „Umzugstag“")
divider(d, "m14", "14", "Abschlussübung: Umzugstag",
        "Wir ziehen das SVN-Repository des Reiseportals nach GitLab um und liefern das erste Feature im neuen Zuhause aus.",
        "15:30 – 16:45 UHR · STATION 1 BIS 6")

content(d, "m14-ablauf", "Theorie", crumb, "Die Abschlussübung im Überblick",
        stations([1, 2, 3, 4, 5, 6]) + '<p class="legend">Teil 1: Umzug nach GitLab (35 Minuten). Teil 2: ein Feature durchläuft alle sechs Stationen (40 Minuten).</p>',
        "Jedes Team arbeitet mit dem eigenen Migrationsplan aus Modul 13. Rollen vorschlagen: eine Person migriert, eine richtet GitLab ein, die anderen bereiten das erste Feature vor.")

praxis(d, "m14-praxis", crumb, "Einen Release-Stand markieren", [
    "$ git switch main",
    "$ git pull",
    "$ git tag -a v1.0 -m \"Erster Stand aus GitLab\"",
    "$ git push origin v1.0",
    "",
    "$ git describe",
    "v1.0",
    "$ git show v1.0 --stat",
], [
    ("git tag -a", "Ein annotierter Tag mit Beschreibung, Autor und Datum."),
    ("git push origin v1.0", "Tags werden nicht automatisch geteilt."),
    ("Station 6", "Ein Tag kann in der Pipeline die Auslieferung auslösen."),
], "Tags sind unveränderliche Markierungen. Sie werden in Modul 15 beim Ausblick auf CI/CD wieder aufgegriffen.")

uebung(d, "m14-uebung1", crumb, "Teil 1: Der Umzug", [
    "Migrieren Sie das SVN-Repository des Reiseportals nach Ihrem Plan, einschließlich Autoren, Branches und Tags.",
    "Prüfen Sie das Ergebnis: Stimmen Historie, Branches und Tags?",
    "Teilen Sie das Repository in der GitLab-Gruppe Ihres Teams.",
    "Schützen Sie main und hinterlegen Sie Ihre CONTRIBUTING.md.",
], "35 Minuten", "Teams mit 3 bis 4 Personen", "Ein vollständig migriertes, geschütztes Repository in GitLab.",
    notes="Wer schneller fertig ist, migriert zusätzlich die großen Bild- und Videodateien nach Git LFS.")

uebung(d, "m14-uebung2", crumb, "Teil 2: Das erste Feature im neuen Zuhause", [
    "Jede Person übernimmt eine Aufgabe aus der Liste und arbeitet auf einem eigenen Branch.",
    "Teilen Sie Ihre Arbeit und öffnen Sie einen Merge Request.",
    "Prüfen Sie gegenseitig, lösen Sie auftretende Konflikte und führen Sie zusammen.",
    "Markieren Sie den gemeinsamen Stand als <b>v1.0</b>.",
], "40 Minuten", "Teams mit 3 bis 4 Personen", "Ein Release-Tag v1.0 mit allen Aufgaben des Teams.",
    scenario="Zwei der Aufgaben ändern bewusst dieselbe Stelle in application.yml. Ein Konflikt gehört zum Umzugstag dazu.",
    notes="Aufgabenliste: neue Zahlungsart, Anpassung der Stornofrist, Korrektur in der README, Preisfilter für die Reisesuche.")

referenzen(d, "m14-ref", crumb, [
    ("Taggen", "Pro Git, Kapitel 2.6 · annotierte und einfache Tags", "https://git-scm.com/book/de/v2/Git-Grundlagen-Taggen"),
    ("git tag", "Git-Referenz, englisch", "https://git-scm.com/docs/git-tag"),
    ("git describe", "Git-Referenz · Version aus dem letzten Tag ableiten, englisch", "https://git-scm.com/docs/git-describe"),
    ("Releases", "GitLab-Dokumentation · Release zu einem Tag anlegen, englisch", "https://docs.gitlab.com/user/project/releases/"),
    ("Semantic Versioning 2.0.0", "Regeln für Versionsnummern, deutsch", "https://semver.org/lang/de/"),
], "Semantic Versioning ist eine Empfehlung, keine Pflicht. Viele Teams aus der Automatisierung haben eigene Nummernschemata; wichtig ist, dass der Tag den ausgelieferten Stand eindeutig benennt.")

prompts(d, "m14-ki", crumb, [
    ("Verstehen", "Erkläre den Unterschied zwischen annotierten und einfachen Tags in Git und warum Release-Stände annotiert werden sollten. Wie zeigt git describe die Version eines Builds an?"),
    ("Üben", "Nenne mir fünf Änderungen an einer Software und lass mich nach Semantic Versioning entscheiden, ob Major, Minor oder Patch erhöht wird. Erkläre meine Fehler."),
    ("Übertragen", "Wie kann ich in einem Maven-Projekt die Versionsnummer aus dem Git-Tag ableiten? Zeige zwei gängige Ansätze und ihre Vor- und Nachteile."),
], "Beim dritten Prompt nennen die Modelle meist Maven-Plugins. Plugin-Namen und Versionen vor dem Einsatz auf Maven Central prüfen.")

exec((HERE / "nachbereitung_module.py").read_text(encoding="utf-8"))

# ---------- Modul 15 ----------
crumb = M(15, "Abschluss")
d.section("Modul 15: Abschluss – neuer Arbeitsablauf, Ausblick und Feedback",
          "t2-15-abschluss", "Von SVN zu Git – Modul 15: Abschluss")
divider(d, "m15", "15", "Abschluss",
        "Wir vergleichen den neuen Arbeitsablauf mit der Skizze vom Auftakt und blicken auf die nächsten Schritte.",
        "16:45 – 17:00 UHR · AUSBLICK UND FEEDBACK")

content(d, "m15-ausblick", "Theorie", crumb, "Ausblick: Git als Grundlage der CI/CD-Pipeline",
        cards(3, [
            card("Jeder Push", "Startet automatisch Build und Tests.", k="KONTINUIERLICHE INTEGRATION", icon="Play"),
            card("Jeder Merge Request", "Zeigt das Ergebnis der Pipeline vor dem Merge.", k="QUALITÄT", icon="CheckCircle"),
            card("Jeder Tag", "Kann die Auslieferung eines geprüften Stands auslösen.", k="AUSLIEFERUNG", icon="PaperPlane", dark=True),
        ]),
        "Die Arbeitsweise aus diesem Kurs ist die Voraussetzung für automatisierte Pipelines. Hinweis auf weiterführende Trainings der Comquent Academy zu GitLab CI/CD.")

uebung(d, "m15-uebung", crumb, "Unser neuer Arbeitsablauf", [
    "Legen Sie Ihren neuen Arbeitsablauf neben die Skizze vom Auftakt.",
    "Benennen Sie die drei wichtigsten Unterschiede für Ihr Team.",
    "Notieren Sie, was Sie in Ihrem Projekt als Erstes ändern wollen.",
], "10 Minuten", "Kleingruppen, dann kurze Runde im Plenum", "Je Gruppe drei Unterschiede und ein erster konkreter Schritt.",
    notes="Abschließend Feedbackbogen ausgeben und auf die Unterlagen im Schulungsportal hinweisen.")

referenzen(d, "m15-ref", crumb, [
    ("Get started with GitLab CI/CD", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/ci/"),
    ("Tutorial: Create and run your first GitLab CI/CD pipeline", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/ci/quick_start/"),
    ("Continuous Integration", "Martin Fowler · Grundlagenartikel, englisch", "https://martinfowler.com/articles/continuousIntegration.html"),
    ("Git Hooks", "Pro Git, Kapitel 8.3 · Prüfungen vor Commit und Push", "https://git-scm.com/book/de/v2/Git-einrichten-Git-Hooks"),
], "Das Tutorial von GitLab führt in etwa einer Stunde zur ersten eigenen Pipeline und ist ein guter nächster Schritt nach dem Kurs. Hinweis auf die weiterführenden Trainings der Comquent Academy zu GitLab CI/CD.")

prompts(d, "m15-ki", crumb, [
    ("Verstehen", "Erkläre, wie eine GitLab-CI/CD-Pipeline durch Push, Merge Request und Tag ausgelöst wird. Zeige eine einfache .gitlab-ci.yml für ein Maven-Projekt mit Build und Tests."),
    ("Hintergrund", "Was bedeutet Continuous Integration im Sinne von Martin Fowler, und welche Voraussetzungen muss ein Team mit Git dafür erfüllen? Wie hängen kurze Branches und CI zusammen?"),
    ("Übertragen", "Ich will die ersten 30 Tage nach unserer Umstellung auf Git planen. Stelle mir Fragen zu Team, Projekt und Werkzeugen und erstelle daraus einen Plan mit Zielen für jede Woche."),
], "Der dritte Prompt passt zur Abschlussübung: Die Teilnehmenden können ihren ersten konkreten Schritt als Ausgangspunkt nehmen. Hinweis auf die weiterführenden Trainings zu GitLab CI/CD.")

statement(d, "danke", "COMQUENT ACADEMY", "Vielen Dank!",
          "Unterlagen, Übungen und die Git-Rettungskarte finden Sie im Schulungsportal.",
          "Dank an die Teilnehmenden. Hinweis auf Feedback und die Unterlagen im Schulungsportal.")

d.write(str(DECKS / "kapitel"))
