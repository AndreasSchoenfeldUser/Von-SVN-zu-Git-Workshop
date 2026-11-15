# ---------- Zusatzmodul: Mergen und Merge-Strategien ----------
crumb = "Zusatzmodul · Merge-Strategien"
d.section("Zusatzmodul: Mergen und Merge-Strategien – Fast-Forward, Squash, Strategien und Merge-Methoden in GitLab",
          "t2-12y-merge-strategien", "Von SVN zu Git – Zusatzmodul: Mergen und Merge-Strategien")
divider(d, "zm", "+", "Zusatzmodul: Mergen und Merge-Strategien",
        "Wir lernen die Wege kennen, auf denen Git und GitLab Branches zusammenführen, und wählen den Weg, der zu unserem Team passt.",
        "ZUSATZMODUL · CA. 75 MINUTEN",
        "Dieses Modul ist optional. Es baut auf Modul 06 (Fast-Forward und 3-Way-Merge), Modul 09 (Konflikte lösen) und Modul 12 (Rebase oder Merge) auf und eignet sich für Teams, die ihre Merge-Regeln in GitLab festlegen wollen.")

content(d, "zm-basis", "Theorie", crumb, "Was Git beim Mergen vergleicht",
        '<div class="split">' +
        graph(960, 360, [(90, 240, "A"), (300, 240, "B"), (510, 240, "C"), (510, 100, "D"), (740, 240, "M")],
              [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)],
              [(300, 300, "Merge-Basis", "ghost"), (510, 300, "ours: main", "main"),
               (510, 30, "theirs: feature", "br"), (740, 300, "Ergebnis", "head")], merge=(4,)) +
        notes_col([("Merge-Basis", "Der letzte gemeinsame Commit beider Branches. git merge-base zeigt ihn an."),
                   ("ours", "Der Stand des Branches, auf dem Sie stehen (HEAD)."),
                   ("theirs", "Der Stand, den Sie hereinholen.")]) +
        "</div>",
        "Git vergleicht nur drei Stände: Basis, ours und theirs. Die einzelnen Commits dazwischen spielen keine Rolle. Daraus folgt eine Überraschung: Hat ein Branch eine Änderung erst gemacht und dann wieder zurückgenommen, zählt das als keine Änderung. Die Begriffe ours und theirs tauchen in den Optionen später wieder auf.")

content(d, "zm-wege", "Theorie", crumb, "Vier Wege, einen Branch zu integrieren",
        cards(4, [
            card("--no-ff", "Ein Merge-Commit klammert den Branch, auch wenn ein Fast-Forward möglich wäre.", k="MERGE-COMMIT"),
            card("--ff-only", "main rückt nur vor. Ist main weitergelaufen, bricht Git ab.", k="FAST-FORWARD"),
            card("--squash", "Alle Änderungen des Branches werden zu einem einzigen neuen Commit.", k="SQUASH"),
            card("rebase", "Die Commits werden auf den neuen Stand von main gesetzt, dann rückt main vor.", k="REBASE", dark=True),
        ]) +
        '<p class="under">Ohne Option macht git merge einen Fast-Forward, wenn das möglich ist, und sonst einen Merge-Commit.</p>',
        "Fast-Forward und 3-Way-Merge kennen die Teilnehmenden aus Modul 06, Rebase aus Modul 12. Neu sind die Optionen, mit denen man einen der Wege erzwingt, und der Squash. Alle vier Wege führen zum selben Code in main. Sie unterscheiden sich nur darin, welche Historie entsteht.")

content(d, "zm-graphen", "Theorie", crumb, "Merge-Commit oder Squash: Was in main sichtbar bleibt",
        '<div class="cards c2">'
        '<div class="gpanel"><p class="gcap">Merge-Commit mit --no-ff</p>' +
        graph(720, 300, [(70, 200, "A"), (250, 200, "B"), (380, 80, "C1"), (510, 80, "C2"), (640, 200, "M")],
              [(0, 1), (1, 2), (2, 3), (3, 4), (1, 4)],
              [(640, 250, "main", "main"), (510, 10, "feature", "br")], merge=(4,)) +
        '<p class="ct">Die einzelnen Schritte bleiben erhalten, M zeigt Anfang und Ende der Aufgabe.</p></div>'
        '<div class="gpanel"><p class="gcap">Squash mit --squash</p>' +
        graph(720, 300, [(70, 200, "A"), (250, 200, "B"), (380, 80, "C1"), (510, 80, "C2"), (640, 200, "S")],
              [(0, 1), (1, 2), (2, 3), (1, 4)],
              [(640, 250, "main", "main"), (510, 10, "feature (löschen)", "ghost")], merge=(4,)) +
        '<p class="ct">Der neue Commit S enthält alles. Die Verbindung zum Branch geht verloren.</p></div>'
        '</div><p class="under">Nach einem Squash hält git branch -d den Branch für nicht gemergt. Er wird mit -D gelöscht.</p>',
        "Beim Merge-Commit hat M zwei Vorgänger, beim Squash hat S nur einen. Für Git sind C1 und C2 deshalb nie in main angekommen. Wer nach dem Squash auf dem alten Branch weiterarbeitet und erneut mergt, bekommt Konflikte mit den eigenen Änderungen. Darum: Branch nach dem Squash löschen.")

praxis(d, "zm-praxis-wege", crumb, "Den Weg beim Mergen festlegen", [
    "$ git switch main",
    "$ git merge --no-ff feature/merkliste",
    "Merge made by the 'ort' strategy.",
    "",
    "$ git merge --ff-only feature/gutscheine",
    "fatal: Not possible to fast-forward, aborting.",
    "",
    "$ git merge --squash feature/bewertung",
    "Squash commit -- not updating HEAD",
    "$ git commit -m \"Kundenbewertungen ergänzen\"",
    "$ git branch -D feature/bewertung",
], [
    ("--no-ff", "Legt immer einen Merge-Commit an, auch wenn main nicht weitergelaufen ist."),
    ("--ff-only", "Bricht ab, statt einen Merge-Commit anzulegen. Dann zuerst den Branch aktualisieren."),
    ("--squash", "Bringt alle Änderungen in die Staging Area. Den Commit legen Sie selbst an."),
], "Die Ausgaben sind gekürzt. Bei --ff-only schlägt Git zusätzlich vor, mit --no-ff zu mergen oder vorher zu rebasen. Die Commit Message beim Squash beschreibt die ganze Aufgabe, nicht den letzten Zwischenschritt. Wer immer mit --ff-only arbeiten will, setzt git config merge.ff only.",
    lead="Mit einer Option wählen Sie den Weg selbst, statt ihn Git zu überlassen.")

content(d, "zm-strategien", "Theorie", crumb, "Strategien: wie Git zwei Stände zusammenführt",
        table(["Strategie", "Wofür", "Hinweis"], [
            ["ort", "Zwei Branches mergen", "Standard seit Git 2.34, erkennt Umbenennungen"],
            ["recursive", "Früherer Standard", "Seit Git 2.50 nur ein anderer Name für ort"],
            ["resolve", "Einfacher 3-Way-Merge", "Ohne Erkennung von Umbenennungen, selten nötig"],
            ["octopus", "Mehr als zwei Branches auf einmal", "Bricht ab, sobald ein Konflikt entsteht"],
            ["ours", "Einen Branch als erledigt markieren", "Übernimmt nichts aus dem anderen Branch"],
            ["subtree", "Projekt in einem Unterverzeichnis", "Gleicht die Verzeichnisstruktur an"],
        ], [18, 38, 44]) +
        '<p class="under">Gewählt wird mit -s, etwa git merge -s ours. Im Alltag bleibt es bei ort, Git wählt die Strategie selbst.</p>',
        "Die Strategie ist das Verfahren, mit dem Git die Stände zusammenrechnet. Davon zu unterscheiden sind die Wege von der vorigen Slide, die bestimmen, welche Historie entsteht. Wer git merge mit zwei Branches aufruft, bekommt automatisch octopus. Die Strategie ours ist für abgelöste Branches gedacht, deren Inhalt bewusst verworfen wird.")

praxis(d, "zm-optionen", crumb, "Optionen für ort mit -X", [
    "# Nur Leerzeichen geändert: kein Konflikt",
    "$ git merge -X ignore-space-change format/einrueckung",
    "",
    "# Bei Konflikten automatisch eine Seite wählen",
    "$ git merge -X theirs config/standardwerte",
    "",
    "# Unterschiedliche Zeilenenden angleichen",
    "$ git merge -X renormalize altbestand/windows",
    "",
    "# Etwas anderes: der Branch zählt gar nicht",
    "$ git merge -s ours release/1.0",
], [
    ("-X ignore-space-change", "Zeilen, die sich nur in Leerzeichen unterscheiden, gelten als unverändert."),
    ("-X ours, -X theirs", "Nur widersprüchliche Stellen gehen an eine Seite. Alles andere wird normal gemergt."),
    ("-s ours", "Übernimmt keine Änderung, hält aber den Merge in der Historie fest."),
], "-X theirs löst Konflikte, ohne dass jemand hinsieht. Das ist nur sinnvoll, wenn vorher klar ist, dass die andere Seite gewinnen soll, etwa bei erzeugten Dateien. Verwechslungsgefahr: -X ours mergt normal und entscheidet nur Konflikte, -s ours verwirft den ganzen Branch. Eine Strategie theirs gibt es nicht. renormalize hilft nach der Migration, wenn alte SVN-Branches andere Zeilenenden haben.",
    lead="Optionen ändern, wie ort mit einzelnen Stellen umgeht. Die Strategie bleibt dieselbe.")

praxis(d, "zm-konflikte", crumb, "Konflikte besser lesen, Lösungen wiederverwenden", [
    "$ git config --global merge.conflictStyle zdiff3",
    "$ git config --global rerere.enabled true",
    "$ git merge suche/trefferzahl",
    "Recorded preimage for '…/application.yml'",
    "# Inhalt von application.yml:",
    "! <<<<<<< HEAD",
    "    max-ergebnisse: 30",
    "! ||||||| 066b886",
    "    max-ergebnisse: 20",
    "! =======",
    "    max-ergebnisse: 25",
    "! >>>>>>> suche/trefferzahl",
], [
    ("zdiff3", "Zeigt zusätzlich den Stand der Merge-Basis. So ist erkennbar, wer was geändert hat."),
    ("rerere", "Merkt sich gelöste Konflikte und löst denselben Konflikt beim nächsten Mal selbst."),
    ("git checkout --theirs", "Übernimmt für eine einzelne Datei vollständig eine Seite."),
], "Ohne zdiff3 sieht man nur 30 gegen 25. Mit der Basis 20 wird klar: Beide Seiten haben die Trefferzahl erhöht, das Team muss sich auf einen Wert einigen. rerere steht für „reuse recorded resolution“. Es hilft, wenn derselbe Konflikt mehrfach auftritt, etwa bei einem wiederholten Rebase. Die gelöste Datei muss trotzdem mit git add vorgemerkt werden.",
    lead="Zwei Einstellungen, die jedes Team setzen sollte. Sie ergänzen das Vorgehen aus Modul 09.")

praxis(d, "zm-revert", crumb, "Einen Merge zurücknehmen", [
    "# Noch nicht geteilt: Merge verwerfen",
    "$ git reset --hard ORIG_HEAD",
    "",
    "# Schon in main: Merge mit neuem Commit aufheben",
    "$ git revert a940811",
    "error: commit … is a merge but no -m option was given.",
    "$ git revert -m 1 a940811",
    "[main 9494a1d] Revert \"Merge branch 'suche/…'\"",
], [
    ("ORIG_HEAD", "Git merkt sich den Stand vor dem Merge. Nur für lokale, nicht geteilte Merges."),
    ("-m 1", "Der erste Vorgänger, also main, gilt als Hauptlinie. Die Änderungen des Branches werden aufgehoben."),
    ("Später erneut mergen", "Zuerst den Revert selbst mit git revert aufheben, sonst fehlen die alten Änderungen."),
], "Ein Merge-Commit hat zwei Vorgänger. Mit -m 1 sagen Sie Git, welcher davon die Hauptlinie ist. Nach dem Revert gelten die Commits des Branches für Git weiterhin als gemergt. Ein neuer Merge bringt deshalb nur Commits, die danach entstanden sind. In GitLab erzeugt die Schaltfläche „Revert“ im gemergten Merge Request denselben Commit.",
    lead="Die Regel aus Modul 05 gilt auch hier: Was geteilt ist, wird mit einem neuen Commit korrigiert.")

content(d, "zm-gitlab", "Theorie", crumb, "Merge-Methoden in GitLab",
        table(["Merge method", "Historie in main", "Wenn main weitergelaufen ist"], [
            ["Merge commit", "Jeder Merge Request ergibt einen Merge-Commit", "Merge ohne Rebase möglich"],
            ["Merge commit with semi-linear history", "Merge-Commit, Branch beginnt auf aktuellem main", "Merge erst nach „Rebase“"],
            ["Fast-forward merge", "Gerade, ohne Merge-Commits", "Merge erst nach „Rebase“"],
        ], [32, 38, 30]) +
        '<p class="under">Dazu „Squash commits when merging“: Do not allow, Allow, Encourage oder Require. Beides unter Settings › Merge requests.</p>',
        "Die Einstellung gilt für das ganze Projekt und setzt die Teamregel technisch durch. Kann GitLab ohne Konflikt rebasen, erscheint im Merge Request die Schaltfläche „Rebase“, sonst muss lokal rebased werden. Squash und Merge commit zusammen ergeben zwei Commits in main: den Squash-Commit und den Merge-Commit. Bei Fast-forward merge bleibt nur der Squash-Commit.")

content(d, "zm-wahl", "Theorie", crumb, "Welcher Weg passt wozu?",
        table(["Situation", "Empfehlung", "Warum"], [
            ["Branch mit sauberen, einzeln sinnvollen Commits", "Merge-Commit, semi-linear", "Schritte und Klammer bleiben sichtbar"],
            ["Branch mit vielen Zwischenständen", "Squash", "Ein Commit je Aufgabe in main"],
            ["Kurze Branches, Trunk-based Development", "Rebase und Fast-Forward", "Gerade Historie, leicht zu lesen"],
            ["Release- oder Hotfix-Branch zurückführen", "Merge-Commit mit --no-ff", "Die Rückführung bleibt nachvollziehbar"],
            ["Eigenen Branch aktualisieren", "Rebase, bei geteilten Branches Merge", "Regel aus Modul 12"],
        ], [38, 30, 32]) +
        '<p class="under">Für den Einstieg nach SVN bewährt sich: Merge commit with semi-linear history, Squash auf „Allow“.</p>',
        "Die Empfehlung für den Einstieg hält die Historie übersichtlich und zeigt trotzdem, wo eine Aufgabe begonnen und geendet hat. Die semi-lineare Methode zwingt dazu, den Branch vor dem Merge auf den aktuellen Stand zu bringen; die Pipeline läuft so auf dem Stand, der in main ankommt. Squash bleibt eine Entscheidung je Merge Request.")

statement(d, "zm-statement", "MERKSATZ", "Die Historie ist für ihre Leser da.",
          "Wählen Sie die Merge-Methode danach, was Ihr Team später in main nachlesen will: jeden Arbeitsschritt, einen Commit je Aufgabe oder eine gerade Linie.",
          "Hier lohnt die Frage an die Gruppe: Wer hat in SVN zuletzt die Historie gelesen, und wozu? Die Antwort, etwa Fehlersuche oder Nachweis für ein Audit, bestimmt die passende Methode.")

content(d, "zm-best", "Theorie", crumb, "Best Practices für das Mergen im Team",
        cards(3, [
            card("Vorbereiten", k="VOR DEM MERGE", items=["Branches kurz halten, oft integrieren", "Branch auf den neuen Stand bringen", "Pipeline auf dem Merge-Ergebnis"]),
            card("Nachvollziehbar mergen", k="BEIM MERGE", items=["Eine Merge-Methode im Projekt", "Messages, die die Aufgabe nennen", "Konflikte mit dem Autor lösen"]),
            card("Aufräumen", k="NACH DEM MERGE", dark=True, items=["Gemergte Branches löschen", "Fehler per Revert, nicht per Force-Push", "Regeln in der CONTRIBUTING.md"]),
        ]),
        "Kurze Branches sind der wirksamste Schutz vor schwierigen Merges. Konflikte in fremdem Code nicht mit -X ours oder -X theirs wegdrücken, sondern mit der Person klären, die ihn geschrieben hat. In GitLab Premium prüfen Merged-Results-Pipelines das Ergebnis des Merges, bevor er stattfindet.")

uebung(d, "zm-uebung", crumb, "Vier Branches, vier Wege", [
    "Richten Sie <b>merge.conflictStyle zdiff3</b> und <b>rerere.enabled</b> ein.",
    "Führen Sie <b>feature/merkliste</b> <span style='white-space:nowrap'>mit --no-ff</span> und <b>feature/preisalarm</b> <span style='white-space:nowrap'>mit --squash</span> nach main. Vergleichen Sie die Historie.",
    "Mergen Sie <b>format/einrueckung</b> einmal ohne und einmal <span style='white-space:nowrap'>mit -X ignore-space-change</span>.",
    "Lösen Sie den Konflikt mit <b>suche/trefferzahl</b>, verwerfen Sie den Merge mit ORIG_HEAD und mergen Sie erneut. Was übernimmt rerere?",
    "Wählen Sie im Team eine Merge-Methode, stellen Sie sie in GitLab ein und halten Sie sie in der <b>CONTRIBUTING.md</b> fest.",
], "35 Minuten", "Partnerarbeit, Schritt 5 im Team", "Eine Historie mit allen Wegen und eine eingestellte Merge-Methode im Team-Repository.",
    notes="Die vier Branches liegen im Übungsstand merge des Reiseportals bereit. feature/preisalarm enthält bewusst Zwischen-Commits wie „WIP“ und „fix“. Zum Abschluss git log --oneline --graph zeigen und mit der Slide „Merge-Commit oder Squash“ vergleichen.")

referenzen(d, "zm-ref", crumb, [
    ("git merge", "Git-Referenz · Abschnitt Merge Strategies, englisch", "https://git-scm.com/docs/git-merge#_merge_strategies"),
    ("Fortgeschrittenes Merging", "Pro Git, Kapitel 7.8 · Optionen, Strategien, Merges rückgängig machen", "https://git-scm.com/book/de/v2/Git-Tools-Fortgeschrittenes-Merging"),
    ("Rerere", "Pro Git, Kapitel 7.9", "https://git-scm.com/book/de/v2/Git-Tools-Rerere"),
    ("Merge methods", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/user/project/merge_requests/methods/"),
    ("Squash and merge", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/user/project/merge_requests/squash_and_merge/"),
], "Kapitel 7.8 von Pro Git ist die ausführlichste deutschsprachige Darstellung: Es behandelt -X ignore-space-change, die Strategie ours und das Zurücknehmen von Merges mit revert -m. Die Referenz zu git merge listet alle Strategien und Optionen vollständig.")

prompts(d, "zm-ki", crumb, [
    ("Verstehen", "Erkläre den 3-Way-Merge in Git: Was ist die Merge-Basis, und warum vergleicht Git nur drei Stände statt aller Commits? Zeige ein Beispiel, bei dem das überrascht."),
    ("Üben", "Zeichne eine kleine Git-Historie als ASCII-Graph. Frage mich, wie sie nach --no-ff, --squash und Rebase mit Fast-Forward aussieht, und korrigiere meine Antworten."),
    ("Übertragen", "Wir arbeiten mit GitLab und Merge Requests. Hilf mir, zwischen Merge commit, semi-linearer Historie und Fast-forward merge zu wählen, mit oder ohne Squash. Frage nach unserem Ablauf."),
], "Der Übungs-Prompt wiederholt die Übung dieses Moduls ohne Repository. Beim dritten Prompt die Antwort mit der Slide „Welcher Weg passt wozu?“ abgleichen.")
