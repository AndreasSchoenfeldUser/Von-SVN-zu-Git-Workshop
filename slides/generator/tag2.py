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
            ["optional", "Zusatz · Der Git-Workflow", "ca. 60 Minuten"],
            ["14:45", "13 · Den Umzug planen", "Migration"],
            ["15:30", "14 · Abschlussübung „Umzugstag“", "Station 1 bis 6"],
            ["16:45", "15 · Abschluss", "Ausblick, Feedback"],
        ], [14, 56, 30]) + '<p class="under">Pausen: 10:30 Uhr · 12:00 Uhr Mittagspause · 14:30 Uhr</p>',
        "Integrieren steht bewusst vor dem Teilen: Konflikte lassen sich zunächst lokal und ohne Druck üben, bevor das Team-Repository ins Spiel kommt.")

content(d, "leitidee", "Einführung", "Leitidee", "Heute: die Stationen 3 bis 6 im Team",
        stations([3, 4, 5, 6]) + '<p class="legend">Heute im Fokus: Stationen 3 bis 6 (dunkel hervorgehoben). Die Stationen 1 und 2 aus Tag 1 bilden die Grundlage.</p>',
        "Gestern ging es um das eigene Repository. Heute kommt das Team dazu: Wie gelangt eine Änderung geprüft und nachvollziehbar in den gemeinsamen Stand?")

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

praxis(d, "m13-praxis", crumb, "Migration mit git svn", [
    "# authors.txt: SVN-Benutzer zu Git-Identität",
    "mmuster = Max Muster <max.muster@example.com>",
    "",
    "$ git svn clone --stdlayout \\",
    ">   --authors-file=authors.txt \\",
    ">   https://svn.example.com/reiseportal reiseportal",
    "$ cd reiseportal",
    "$ git branch -a  # übernommene SVN-Branches",
    "$ git remote add origin <GitLab-URL>",
    "$ git push -u origin --all",
    "$ git push origin --tags",
], [
    ("--stdlayout", "Erkennt die übliche Struktur aus trunk, branches und tags."),
    ("--authors-file", "Ordnet jedem SVN-Benutzer Name und E-Mail zu."),
    ("Nacharbeit", "SVN-Tags kommen als Branches an und werden in echte Git-Tags umgewandelt."),
], "Comquent bringt für Migrationen vorgefertigte, in Projekten erprobte Skripte mit, die unter anderem die Umwandlung der Tags übernehmen. Im Kurs zeigen wir den Grundablauf mit git svn.")

uebung(d, "m13-uebung", crumb, "Ein Migrationsplan für das Reiseportal", [
    "Analysieren Sie die vorbereitete Übersicht des SVN-Repositorys des Reiseportals.",
    "Beantworten Sie die vier Fragen: Historie, Struktur, Abhängigkeiten, Binärdateien.",
    "Erstellen Sie die Autorenzuordnung für alle beteiligten SVN-Benutzer.",
    "Legen Sie Ablauf und Stichtag für den Umzug fest.",
], "25 Minuten", "Teams mit 3 bis 4 Personen", "Ein Migrationsplan auf einer Seite, der in der Abschlussübung umgesetzt wird.",
    notes="Die Übersicht enthält: trunk, drei Branches, zwölf Tags, einen externen Verweis (svn:externals) auf eine gemeinsame Bibliothek und einen Ordner mit großen Bild- und Videodateien der Reiseziele.")

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

statement(d, "danke", "COMQUENT ACADEMY", "Vielen Dank!",
          "Unterlagen, Übungen und die Git-Rettungskarte finden Sie im Schulungsportal.",
          "Dank an die Teilnehmenden. Hinweis auf Feedback und die Unterlagen im Schulungsportal.")

d.write(str(DECKS / "kapitel"))
