# KI-Prompts im Kurs: Ergebnis der Prüfung

Stand: 15.11.2026

Jedes Kapitel endet mit der Slide „Mit KI vertiefen“ und drei Prompts für Claude und ChatGPT. Dieses Dokument beschreibt, wie die Prompts getestet wurden, was dabei herauskam und worauf Trainer im Kurs hinweisen sollten.

## Kurzfassung

- Die Prompts eignen sich als Einstieg in eigene Fragen. Als Nachschlagewerk taugen die Antworten nicht: In den ersten beiden Testläufen enthielt ein Viertel bis gut ein Drittel der Antworten mindestens einen fachlichen Fehler, bei den schwierigsten Prompts die Hälfte.
- Am zuverlässigsten funktionieren die Übungs-Prompts mit Rollenspiel (Quiz, Rettungsdienst, Konflikte auflösen). Absichtlich falsche Antworten der Tester hat Claude fast immer erkannt und richtig erklärt.
- Die Überarbeitung der Prompts hat Probleme im Ablauf und im Kontext behoben (siehe unten). Fehler im Detailwissen ließen sich durch Umformulieren kaum verringern: Jeder Lauf brachte andere Fehler, einige Fehlvorstellungen traten in allen Läufen auf.
- Bei den Themen Migration mit git svn, GitLab-Preisstufen und Vergleiche mit SVN sind die Antworten am fehleranfälligsten.

## Vorgehen

- **Modell:** Claude Sonnet 5.5, das Standardmodell in claude.ai.
- **Aufruf:** über die Claude-Code-CLI, ohne Werkzeuge, ohne Projektkontext, jeder Prompt in einer eigenen Sitzung:
  `claude -p --model sonnet --system-prompt "Du bist Claude, ein KI-Assistent von Anthropic." --tools "" --strict-mcp-config --setting-sources "" --output-format json "<Prompt>"`
- **Prüfung:** Die Antworten wurden von unabhängigen Prüf-Agenten gegengelesen. Befehle haben sie in Wegwerf-Repositories mit Git 2.54 und git-lfs 3.7 ausgeführt, Java-Code mit javac kompiliert und Maven-Plugins auf Maven Central gesucht. GitLab-Aussagen wurden gegen docs.gitlab.com geprüft, SVN-Aussagen gegen das SVN-Book 1.7.
- **Interaktive Prompts:** Hier haben die Prüfer zusätzlich eine zweite Runde als Teilnehmer gespielt, mit einer absichtlich teilweise falschen Antwort.
- **Nicht geprüft:** ChatGPT; echte Läufe von svn, git svn, git filter-repo und Maven, die auf dem Testrechner nicht installiert waren (dort nur Abgleich mit Doku und Quelltext); echte Pipelines in GitLab.

## Ergebnisse

| Lauf | Prompts | Antworten | Korrekt | Kleine Ungenauigkeiten | Fachlicher Fehler |
| --- | --- | --- | --- | --- | --- |
| 1: erste Fassung | 57 | 57 | 9 | 35 | 13 |
| 2: überarbeitete Fassung, dazu die drei Prompts des Zusatzmoduls Merge-Strategien | 60 | 78 | 17 | 30 | 29 |
| 3: dritte Fassung der 13 Prompts mit den hartnäckigsten Fehlern | 13 | 26 | – | – | 13 |

Lauf 2 enthält für die 18 Problem-Prompts aus Lauf 1 je zwei unabhängige Antworten. Bei zwei Antworten hat Claude die Übung missverstanden; sie sind in der Tabelle nicht mitgezählt. Die Prüfer von Lauf 2 und 3 suchten gezielt nach bekannten Fehlerarten. Die Zahlen sind deshalb nicht direkt vergleichbar und zeigen keinen Trend.

### Was die Überarbeitung behoben hat

- **Ablauf der Übungen:** Claude stellt jetzt eine Situation, wartet auf die Antwort und verrät die Lösung nicht vorab. Ohne diese Anweisung hatte Claude einmal die Rollen vertauscht und zweimal die Lösung vorweggenommen.
- **GitLab-Kontext:** Mit „GitLab“ oder „GitLab Free“ im Prompt verwendet Claude seltener GitHub-Begriffe und nennt häufiger die Preisstufe.
- **Branch `main`:** Übungen setzten `main` voraus, Git 2.54 legt ohne Konfiguration `master` an. Der Zusatz `git init -b main` behebt das.
- **Ausführbare Befehlsfolgen:** Die Übung zu Branches (Modul 06) liefert jetzt eine Befehlsfolge, die in einem frischen Repository läuft.
- **Einzelne Fehler, die in Lauf 3 ausblieben:** `core.ignorecase` global setzen (Modul 03), Hotfix-Abzweig von `develop` (Zusatzmodul Workflow), Force-Push nach Rebase (Modul 10, in einer von zwei Antworten noch angedeutet), doppelte Pipelines (Modul 15), Minor-Einstufung nach SemVer als Fehler gewertet (Modul 14).
- **Fehlvorstellungen:** Hier half eine Bitte wie „Beschreibe SVN zutreffend“ nicht. Wirksamer war, die richtige Tatsache in den Prompt zu schreiben, etwa „Bedenke: Auch in SVN sind Branches billige Kopien“.

### Hartnäckige Fehlvorstellungen der KI

Diese Aussagen tauchten in mehreren Läufen auf, teils trotz Gegenhinweis im Prompt. Sie eignen sich gut, um im Kurs zu zeigen, warum KI-Antworten geprüft werden müssen.

| Thema | Typische falsche Aussage | Richtig | Beleg |
| --- | --- | --- | --- |
| SVN offline | SVN braucht den Server für jede Statusabfrage. | `svn status`, `svn diff` und `svn revert` arbeiten ohne Netzwerk. | SVN-Book 1.7, Kap. 2 |
| SVN-Branches | Branches und Tags sind in SVN teure, vollständige Kopien. | `svn copy` ist eine Cheap Copy mit konstantem Aufwand; aufwendig war das Mergen. | SVN-Book 1.7, Kap. 4 „Cheap Copies“ |
| git pull | Bei auseinandergelaufenen Branches erzeugt `git pull` einen Merge-Commit. | Ohne `pull.rebase` oder `pull.ff` bricht `git pull` ab („Need to specify how to reconcile divergent branches“). | git-pull(1) |
| Push nach Rebase | Nach einem Rebase ist immer ein Force-Push nötig. | Waren die umgeschriebenen Commits nie auf dem Server, ist der Push ein Fast-Forward. | Nachgestellt mit Git 2.54 |
| Merge-Konflikte | Änderungen in direkt benachbarten Zeilen werden automatisch zusammengeführt. | Git meldet einen Konflikt; erst eine unveränderte Zeile dazwischen erlaubt den automatischen Merge. | Nachgestellt mit Git 2.54 |
| GitLab-Stufen | Pflicht-Approvals, „Prevent approval by author“ und Code Owners gibt es in GitLab Free. | In Free sind Approvals optional; erzwingen lassen sie sich erst ab Premium. | docs.gitlab.com, Merge request approvals |
| MR-Pipelines | Eine Merge-Request-Pipeline testet das Merge-Ergebnis. | Sie testet den Source-Branch; das Merge-Ergebnis testen erst Merged-results-Pipelines ab Premium. | docs.gitlab.com, Merge request pipelines |
| git svn | `--no-metadata` ist eine gute Wahl; Tags werden vor dem letzten Abgleich umgewandelt. | Ohne Metadaten ist kein weiterer `git svn fetch` möglich; Tags und Branches erst nach dem letzten Abgleich umwandeln. Schleifen über Refs scheiterten oft an falschen Ref-Namen. | git-svn(1) |
| Submodule | `submodule.recurse true` ersetzt `git clone --recurse-submodules`. | Laut git-config wirkt die Einstellung nicht auf `clone`. | git-config(1) |
| Klon als Backup | Jede Git-Kopie ist ein vollständiges Backup, nichts geht verloren. | Ein Klon enthält nur die Refs vom letzten fetch, keine Issues, Merge Requests oder CI-Variablen. | — |

Daneben fielen auf:

- **Simulierte Ausgaben sind formal oft unstimmig:** Hunk-Header passen nicht zum Inhalt, `git blame` passt nicht zur Historie, ASCII-Graphen haben verschobene Abzweige.
- **Erzeugter Übungscode enthält meist mehr Schwächen als verlangt** (Modul 11).
- **Plugin-Versionen werden teils erfunden.** Deshalb fragt der Prompt in Modul 14 nur nach groupId und artifactId.

### Persönliche Daten in den Antworten

In mehreren Antworten standen Name und E-Mail-Adresse des angemeldeten Kontos als Beispielwerte, etwa in einer Autorendatei für git svn, obwohl der Prompt erfundene Namen verlangte. Wer mit angemeldetem Konto fragt, kann also eigene Daten in Beispielkonfigurationen bekommen. Solche Antworten nicht unverändert in geteilte Unterlagen übernehmen.

## Empfehlungen für den Kurs

1. **Prompts richtig einordnen:** Die Prompts beim ersten Auftreten als Anregung zum Weiterfragen vorstellen. Antworten mit den Referenzen auf der Slide davor abgleichen; darauf weist auch die Hinweiszeile jeder Prompt-Slide hin.
2. **Übungs-Prompts hervorheben:** Zum Festigen empfehlen sich vor allem die Übungs-Prompts. Bei ihnen ist eine falsche Erklärung am wenigsten schädlich, weil die Teilnehmenden selbst antworten.
3. **Warnen und einen Fehler vorführen:** In den Modulen 10, 13 und 15 sowie im Zusatzmodul Nachbereitung ausdrücklich warnen. Die Sprechernotizen nennen dort die im Test beobachteten Fehler. Ein Beispiel aus der Tabelle oben eignet sich, um im Plenum zu zeigen, wie man eine KI-Antwort prüft.
4. **Keine vertraulichen Daten:** Keinen Firmencode und keine echten Server-Adressen oder Namen in Prompts eingeben.

## Prompts ändern

- **Regeln:** Neue oder geänderte Prompts folgen den Regeln in `CLAUDE.md`.
- **Erneut testen:** Danach mit dem oben genannten Aufruf testen, aus einem neutralen Verzeichnis außerhalb des Repositorys. Interaktive Prompts mit einer zweiten Runde prüfen: `claude -p … --resume <session_id> "<Antwort>"`.
- **Mehrfach laufen lassen:** Weil die Antworten von Lauf zu Lauf schwanken, jeden geänderten Prompt mindestens zweimal laufen lassen.
