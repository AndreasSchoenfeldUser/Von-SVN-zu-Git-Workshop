# ---------- Zusatzmodul: Git-Workflow ----------
crumb = "Zusatzmodul · Git-Workflow"
d.section("Zusatzmodul: Git-Workflow mit develop-, Feature-, Bugfix-, Release- und Hotfix-Branches",
          "t2-12z-git-workflow", "Von SVN zu Git – Zusatzmodul: Der Git-Workflow")
divider(d, "zw", "+", "Zusatzmodul: Der Git-Workflow",
        "Wir lernen einen Workflow kennen, in dem main den produktiven Stand hält und develop in der Verantwortung der Entwicklung liegt.",
        "ZUSATZMODUL · CA. 60 MINUTEN",
        "Dieses Modul ist optional. Es eignet sich für Teams mit versionierten Auslieferungen und festen Freigaben. Es baut auf Modul 11 (Merge Requests) und Modul 12 (Branching-Strategien) auf.")

content(d, "zw-branches", "Theorie", crumb, "Sechs Arten von Branches, zwei davon dauerhaft",
        table(["Branch", "Zweck", "Entsteht aus", "Wird gemergt in", "Tag"], [
            ["main", "Produktiver Stand", "–", "–", "Auslieferung, Hotfix"],
            ["develop", "Stand der Entwicklung", "main (einmalig)", "–", "Entwicklungsrelease"],
            ["feature/*", "Neue Funktion", "develop", "develop", "–"],
            ["bugfix/*", "Fehler im Entwicklungsstand", "develop", "develop", "–"],
            ["release/*", "Release festigen", "develop", "main und develop", "Auslieferung"],
            ["hotfix/*", "Dringender Fix in Produktion", "main", "main und develop", "Hotfix"],
        ], [14, 30, 18, 20, 18]) +
        '<p class="under">main und develop bestehen dauerhaft. Alle anderen Branches leben nur so lange wie ihre Aufgabe und werden per Merge Request zurückgeführt.</p>',
        "Die Rückführung von Release- und Hotfix-Branches nach develop ist eine Empfehlung: Ohne sie fehlt die Korrektur im nächsten Release. Wo ein Release-Branch offen ist, wird ein Hotfix stattdessen dorthin zurückgeführt.")

lanes = {"main": 80, "hotfix": 170, "release": 260, "develop": 350, "feature": 440, "bugfix": 530}
nodes = {"M0": (300, "main"), "D0": (380, "develop"), "F1": (460, "feature"), "F2": (540, "feature"),
         "D1": (620, "develop"), "B1": (690, "bugfix"), "D2": (800, "develop"), "R1": (860, "release"),
         "R2": (960, "release"), "M1": (1080, "main"), "D3": (1080, "develop"), "D4": (1200, "develop"),
         "H1": (1180, "hotfix"), "H2": (1260, "hotfix"), "M2": (1380, "main"), "D5": (1420, "develop"),
         "D6": (1560, "develop")}
edges = [("M0", "M1", "seq"), ("M1", "M2", "seq"), ("M0", "D0", "branch"),
         ("D0", "D1", "seq"), ("D1", "D2", "seq"), ("D2", "D3", "seq"), ("D3", "D4", "seq"), ("D4", "D5", "seq"), ("D5", "D6", "seq"),
         ("D0", "F1", "branch"), ("F1", "F2", "seq"), ("F2", "D1", "merge"),
         ("D1", "B1", "branch"), ("B1", "D2", "merge"),
         ("D2", "R1", "branch"), ("R1", "R2", "seq"), ("R2", "M1", "merge"), ("R2", "D3", "dash"),
         ("M1", "H1", "branch"), ("H1", "H2", "seq"), ("H2", "M2", "merge"), ("H2", "D5", "dash")]
tags = [("M0", "v1.0.0", "above", 0, ""), ("D2", "v1.1.0-dev.1", "below", 95, ""),
        ("R2", "v1.1.0", "above", -40, ""), ("M2", "v1.1.1", "above", 0, "")]
content(d, "zw-ueberblick", "Theorie", crumb, "Der Workflow im Überblick",
        workflow(1664, 570, lanes, nodes, edges, tags) +
        '<div class="legend2"><p class="li">Schräge Linien: Abzweigen oder Merge Request</p><p class="li">Gestrichelt: empfohlene Rückführung nach develop</p><p class="li">Kasten: Tag</p></div>',
        "Von links nach rechts: develop entsteht einmalig aus main. Feature und Bugfix gehen von develop ab und kommen per Merge Request zurück. Ein Entwicklungsrelease wird auf develop getaggt. Der Release-Branch festigt den Stand, das Release wird dort getaggt und nach main gemergt. Ein Hotfix geht von main ab und kommt als Hotfix-Version zurück.")

# Feature / Bugfix
fl = {"develop": 90, "feature": 210, "bugfix": 330}
fn = {"D0": (220, "develop"), "F1": (300, "feature"), "F2": (390, "feature"), "F3": (480, "feature"),
      "D1": (400, "develop"), "D2": (570, "develop"), "B1": (660, "bugfix"), "B2": (750, "bugfix"),
      "D3": (850, "develop"), "D4": (960, "develop")}
fe = [("D0", "D1", "seq"), ("D1", "D2", "seq"), ("D2", "D3", "seq"), ("D3", "D4", "seq"),
      ("D0", "F1", "branch"), ("F1", "F2", "seq"), ("F2", "F3", "seq"), ("F3", "D2", "merge"),
      ("D2", "B1", "branch"), ("B1", "B2", "seq"), ("B2", "D3", "merge")]
ft = [("D2", "Merge Request", "above", 0, "mr"), ("D3", "Merge Request", "above", 40, "mr")]
content(d, "zw-feature", "Theorie", crumb, "Feature- und Bugfix-Branches",
        '<div class="split">' + workflow(1000, 380, fl, fn, fe, ft, x0=170) +
        notes_col([("Abzweigen", "Jede Funktion und jeder Fehler bekommt einen eigenen Branch von develop."),
                   ("Zurückführen", "Per Merge Request mit Review und Pipeline nach develop."),
                   ("Aufräumen", "Nach dem Merge wird der Branch gelöscht.")]) + "</div>",
        "develop liegt in der Verantwortung der Entwicklung. Hier gelten die Regeln aus Modul 11: Merge Request, Review, grüne Pipeline. Direkte Commits auf develop sind nicht vorgesehen.")

# Release
rl = {"main": 90, "release": 210, "develop": 330}
rn = {"M0": (220, "main"), "D0": (280, "develop"), "D1": (400, "develop"), "R1": (480, "release"),
      "R2": (580, "release"), "M1": (720, "main"), "D2": (720, "develop"), "D3": (860, "develop"), "D4": (960, "develop")}
re_ = [("M0", "M1", "seq"), ("M0", "D0", "branch"), ("D0", "D1", "seq"), ("D1", "D2", "seq"), ("D2", "D3", "seq"), ("D3", "D4", "seq"),
       ("D1", "R1", "branch"), ("R1", "R2", "seq"), ("R2", "M1", "merge"), ("R2", "D2", "dash")]
rt = [("M0", "v1.0.0", "above", 0, ""), ("D1", "v1.1.0-dev.1", "below", 0, ""), ("R2", "v1.1.0", "above", -50, "")]
content(d, "zw-release", "Theorie", crumb, "Entwicklungsreleases und Release-Branches",
        '<div class="split">' + workflow(1000, 400, rl, rn, re_, rt, x0=170) +
        notes_col([("Entwicklungsrelease", "Ein erreichter Stand wird auf develop getaggt, etwa für Tests in der Testumgebung."),
                   ("Release festigen", "Im Release-Branch nur noch Korrekturen, keine neuen Funktionen."),
                   ("Ausliefern", "Den Auslieferungsstand taggen und per Merge Request nach main bringen.")]) + "</div>",
        "Ein Release-Branch ist optional. Er lohnt sich, wenn die Stabilisierung Zeit braucht und develop parallel weiterlaufen soll. Korrekturen aus dem Release-Branch gehen zurück nach develop.")

# Hotfix
hl = {"main": 90, "hotfix": 210, "develop": 330}
hn = {"M0": (220, "main"), "H1": (340, "hotfix"), "H2": (440, "hotfix"), "M1": (580, "main"),
      "D0": (260, "develop"), "D1": (420, "develop"), "D2": (700, "develop"), "D3": (860, "develop")}
he = [("M0", "M1", "seq"), ("D0", "D1", "seq"), ("D1", "D2", "seq"), ("D2", "D3", "seq"),
      ("M0", "H1", "branch"), ("H1", "H2", "seq"), ("H2", "M1", "merge"), ("H2", "D2", "dash")]
ht = [("M0", "v1.1.0", "above", 0, ""), ("M1", "v1.1.1", "above", 0, "")]
content(d, "zw-hotfix", "Theorie", crumb, "Hotfix-Branches: schnelle Korrektur der Produktion",
        '<div class="split">' + workflow(1000, 380, hl, hn, he, ht, x0=170) +
        notes_col([("Abzweigen von main", "Der Fix setzt auf dem ausgelieferten Stand auf, nicht auf develop."),
                   ("Minimal halten", "Nur die Korrektur, keine weiteren Änderungen."),
                   ("Zurückführen", "Per Merge Request nach main, dort als Hotfix taggen, dann nach develop.")]) + "</div>",
        "Der Hotfix darf keine unfertige Entwicklung aus develop mitnehmen. Deshalb zweigt er von main ab. Die Rückführung nach develop verhindert, dass der Fehler mit dem nächsten Release zurückkommt.")

statement(d, "zw-statement", "MERKSATZ", "main enthält nur, was ausgeliefert ist.",
          "Jeder Stand auf main stammt aus einem Release- oder Hotfix-Branch und ist über einen Tag nachvollziehbar. So ist jederzeit klar, was in Produktion läuft.",
          "Dieser Satz ist der Kern des Workflows. Er erklärt, warum main geschützt ist und warum Merges nach main nur aus release/* und hotfix/* kommen.")

content(d, "zw-regeln", "Theorie", crumb, "Verantwortung, Schutz und Tags",
        table(["Branch", "Verantwortung", "Schutz in GitLab", "Tag-Beispiel"], [
            ["main", "Release-Verantwortliche", "Merge nur aus release/* und hotfix/*", "v1.1.0, v1.1.1"],
            ["develop", "Entwicklung", "Merge nur per Merge Request", "v1.2.0-dev.3"],
            ["release/*", "Release-Verantwortliche", "Nur Korrekturen per Merge Request", "v1.2.0"],
            ["feature/*, bugfix/*", "Entwickler", "Kein Schutz, kurzlebig", "–"],
            ["hotfix/*", "Entwicklung mit Freigabe", "Merge Request mit Freigabe", "v1.1.2"],
        ], [20, 26, 34, 20]) +
        '<p class="under">Die Tag-Namen sind ein Vorschlag nach Semantic Versioning. Wichtig ist, dass das Team ein Schema festlegt und in der CONTRIBUTING.md dokumentiert.</p>',
        "Protected Branches in GitLab erzwingen den Workflow: main und develop sind geschützt, Merges erfolgen nur über Merge Requests mit Freigabe.")

content(d, "zw-eignung", "Theorie", crumb, "Wann passt dieser Workflow?",
        cards(2, [
            card("Gut geeignet", k="STÄRKEN", icon="CheckCircle",
                 items=["Versionierte Auslieferungen mit Freigabe", "Mehrere Stände parallel in Betrieb und Entwicklung", "Regulierte Umgebungen mit Nachweispflicht", "Klare Trennung von Produktion und Entwicklung"]),
            card("Das kostet es", k="AUFWAND", icon="Warning",
                 items=["Mehr langlebige Branches und Merges", "Disziplin bei der Rückführung nach develop", "Längere Wege bis zur Auslieferung", "Für kontinuierliche Auslieferung eher zu schwer"]),
        ]),
        "Vergleich mit Modul 12: GitLab Flow und Trunk-based Development sind leichter, passen aber weniger gut zu festen Freigabezyklen, etwa wenn der Fachbereich jedes Release vor der Auslieferung abnimmt.")

praxis(d, "zw-praxis-feature", crumb, "Feature bis zum Entwicklungsrelease", [
    "$ git switch develop && git pull",
    "$ git switch -c feature/preisalarm",
    "$ git add src/main/java/de/reiseportal/Preisalarm.java",
    "$ git commit -m \"Preisalarm für Reiseangebote ergänzen\"",
    "$ git push -u origin feature/preisalarm",
    "# Merge Request: feature/… → develop",
    "",
    "# Nach dem Merge: Entwicklungsrelease taggen",
    "$ git switch develop && git pull",
    "$ git tag -a v1.1.0-dev.1 -m \"Entwicklungsrelease\"",
    "$ git push origin v1.1.0-dev.1",
], [
    ("Ausgangspunkt", "Feature-Branches starten immer vom aktuellen develop."),
    ("Merge Request", "Zielbranch ist develop, nie main."),
    ("Entwicklungsrelease", "Ein Tag auf develop markiert einen testbaren Stand."),
], "Bugfix-Branches laufen genauso, nur mit dem Präfix bugfix/.")

praxis(d, "zw-praxis-release", crumb, "Ein Release festigen und ausliefern", [
    "$ git switch -c release/1.1 develop",
    "$ git push -u origin release/1.1",
    "# Nur Korrekturen, jeweils per Merge Request",
    "",
    "$ git switch release/1.1 && git pull",
    "$ git tag -a v1.1.0 -m \"Auslieferung 1.1.0\"",
    "$ git push origin v1.1.0",
    "# Merge Request: release/1.1 → main",
    "# Merge Request: release/1.1 → develop",
    "$ git branch -d release/1.1",
], [
    ("release/1.1", "Ab hier läuft develop für das nächste Release weiter."),
    ("v1.1.0", "Der Auslieferungsstand wird im Release-Branch getaggt."),
    ("Zwei Merge Requests", "Nach main zur Auslieferung, nach develop für die Korrekturen."),
], "Wer möchte, setzt den Auslieferungs-Tag nach dem Merge auf main. Wichtig ist, dass das Team sich auf eine Stelle festlegt.")

praxis(d, "zw-praxis-hotfix", crumb, "Ein Hotfix für die Produktion", [
    "$ git switch main && git pull",
    "$ git switch -c hotfix/1.1.1-preisrundung",
    "$ git commit -am \"Rundung der Reisepreise korrigieren\"",
    "$ git push -u origin hotfix/1.1.1-preisrundung",
    "# Merge Request: hotfix/… → main",
    "",
    "$ git switch main && git pull",
    "$ git tag -a v1.1.1 -m \"Hotfix 1.1.1\"",
    "$ git push origin v1.1.1",
    "# Merge Request: hotfix/… → develop",
], [
    ("Von main", "Der Fix basiert auf dem Stand, der in Produktion läuft."),
    ("v1.1.1", "Die Hotfix-Version wird auf main getaggt."),
    ("Nach develop", "Damit der Fehler im nächsten Release nicht zurückkehrt."),
], "Wenn gerade ein Release-Branch offen ist, geht der Hotfix statt nach develop in den Release-Branch. Von dort gelangt er mit dem Release nach develop.")

uebung(d, "zw-uebung", crumb, "Ein vollständiger Release-Zyklus", [
    "Legen Sie develop aus main an und schützen Sie beide Branches in GitLab.",
    "Entwickeln Sie zwei Features und einen Bugfix auf eigenen Branches und führen Sie sie per Merge Request nach develop.",
    "Taggen Sie das Entwicklungsrelease <b>v1.1.0-dev.1</b>.",
    "Festigen Sie das Release in <b>release/1.1</b>, taggen Sie <b>v1.1.0</b> und führen Sie nach main und develop.",
    "Beheben Sie einen Fehler in Produktion über <b>hotfix/1.1.1</b> und taggen Sie <b>v1.1.1</b>.",
], "45 Minuten", "Teams mit 3 bis 4 Personen", "Eine grafische Historie, die den ganzen Zyklus mit allen drei Tags zeigt.",
    notes="Zum Abschluss die Historie mit git log --oneline --graph --all anzeigen und mit dem Überblicksbild des Moduls vergleichen.")

referenzen(d, "zw-ref", crumb, [
    ("A successful Git branching model", "Vincent Driessen · Ursprung des Workflows, englisch", "https://nvie.com/posts/a-successful-git-branching-model/"),
    ("Gitflow-Workflow", "Atlassian Git-Tutorial, deutsch", "https://www.atlassian.com/de/git/tutorials/comparing-workflows/gitflow-workflow"),
    ("Branching-Workflows", "Pro Git, Kapitel 3.4 · langlebige und Themen-Branches", "https://git-scm.com/book/de/v2/Git-Branching-Branching-Workflows"),
    ("Protected branches", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/user/project/repository/branches/protected/"),
    ("Semantic Versioning 2.0.0", "Regeln für Versionsnummern, deutsch", "https://semver.org/lang/de/"),
], "Driessen hat seinem Artikel von 2010 später eine Anmerkung vorangestellt: Für kontinuierlich ausgelieferte Software empfiehlt er einfachere Abläufe. Das passt zur Slide „Wann passt dieser Workflow?“.")

prompts(d, "zw-ki", crumb, [
    ("Verstehen", "Erkläre den Git-Workflow mit develop-, Feature-, Release- und Hotfix-Branches als nummerierte Befehlsfolge. Warum wird ein Hotfix nach main und nach develop zurückgeführt, und was gilt, wenn gerade ein Release-Branch existiert?"),
    ("Üben", "Spiele mit mir einen Release-Zyklus in diesem Workflow für ein Maven-Projekt in GitLab durch. Du beschreibst die Situation, ich nenne die Git-Befehle, und du korrigierst mich, auch bei den Merge-Optionen."),
    ("Übertragen", "Unser Produkt läuft bei Kunden in mehreren Versionen parallel. Passt ein Workflow mit develop- und Release-Branches dazu, oder gibt es einfachere Alternativen? Wäge ab."),
], "Die KI nennt den Workflow oft „Gitflow“; das ist derselbe Ansatz. Im Test ließ eine ASCII-Grafik den Hotfix von develop abzweigen; deshalb fragt der Prompt nach einer Befehlsfolge. Mit der Slide „Wann passt dieser Workflow?“ abgleichen.")
