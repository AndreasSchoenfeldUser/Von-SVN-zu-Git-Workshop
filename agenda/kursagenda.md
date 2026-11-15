# Von SVN zu Git – Git Grundlagen für SVN-Umsteiger

Stand: 15.11.2026 · Quelle: Claude Doc https://claude.ai/artifact/CGsZJULWGf8HpK7FWd6Dan

## Kursüberblick

In zwei Tagen lernen Entwickler mit SVN-Erfahrung die Arbeitsweise mit Git kennen. Im Mittelpunkt stehen nicht einzelne Befehle, sondern der Weg einer Änderung von der Aufgabe bis zur Auslieferung.

| Merkmal | Beschreibung |
| --- | --- |
| Zielgruppe | Entwickler, die bisher mit Subversion (SVN) arbeiten und auf Git umsteigen |
| Dauer | 2 Tage, jeweils 09:00–17:00 Uhr |
| Format | Präsenz oder remote, hoher Übungsanteil |
| Voraussetzungen | Praktische Erfahrung mit SVN (checkout, update, commit, Branches und Tags); keine Git-Kenntnisse erforderlich |

**Nach dem Kurs können die Teilnehmenden:**

- den Unterschied zwischen zentraler und verteilter Versionsverwaltung erklären und ihre SVN-Gewohnheiten gezielt anpassen
- das Git-Modell aus Working Directory, Staging Area und lokalem Repository sicher anwenden
- Änderungen lokal committen, nachvollziehen und gezielt rückgängig machen
- mit Branches arbeiten und Merge-Konflikte lösen
- über Remote-Repositories und Merge Requests in GitLab zusammenarbeiten
- die wichtigsten Schritte einer Migration von SVN nach Git einschätzen

## Leitidee: vom Arbeitsablauf her denken

Der Kurs folgt dem Weg einer Änderung durch den Entwicklungsalltag. An jeder Station wird deutlich, wie Git die Zusammenarbeit anders organisiert, als es die Teilnehmenden aus SVN gewohnt sind.

1. **Aufgabe übernehmen:** Jede Aufgabe bekommt ihren eigenen Branch. Branches sind Alltag, keine Ausnahme für Releases.
2. **Arbeiten und festhalten:** Die Historie liegt lokal. Ein Commit ist ein persönlicher Arbeitsschritt, der niemanden stört.
3. **Teilen:** Veröffentlichen ist eine eigene, bewusste Entscheidung und nicht mehr Teil des Commits.
4. **Prüfen lassen:** Änderungen werden über einen Merge Request begutachtet, bevor sie in die Hauptlinie gelangen.
5. **Integrieren:** Zusammenführen geschieht gezielt und sichtbar, nicht nebenbei beim Aktualisieren.
6. **Ausliefern:** Ein geprüfter Stand wird markiert und an die Pipeline übergeben.

## Roter Faden: der Umzug des Reiseportals

Alle Übungen bauen auf einem gemeinsamen Projekt auf: dem Reiseportal eines erfundenen Reiseveranstalters, einer Java-Webanwendung für die Online-Buchung von Reisen, die seit Jahren in einem SVN-Repository gepflegt wird.

- **Zum Auftakt** skizzieren die Teilnehmenden ihren heutigen Arbeitsablauf mit SVN – von der Aufgabe bis zur Auslieferung.
- **Tag 1 – Allein mit Git:** Die Stationen 1 und 2 im eigenen, lokalen Repository.
- **Tag 2 – Gemeinsam mit Git:** Die Stationen 3 bis 6 im Team über GitLab, zum Abschluss der Umzug des SVN-Repositorys samt Historie.
- **Zum Abschluss** legen die Teams ihren neuen Arbeitsablauf neben die Skizze vom Auftakt und halten fest, was sie im eigenen Projekt ändern wollen.

## Tag 1: Allein mit Git

Der erste Tag behandelt die Stationen „Aufgabe übernehmen“ und „Arbeiten und festhalten“. Ziel ist ein sicherer Umgang mit dem eigenen, lokalen Repository.

| Zeit | Modul | Inhalte |
| --- | --- | --- |
| 09:00 | Auftakt: Wie arbeiten wir heute? | Die Teilnehmenden skizzieren ihren Arbeitsablauf mit SVN. Daran wird sichtbar, an welchen Stellen Git anders denkt. |
| 09:45 | Das Git-Modell | Warum jeder eine vollständige Kopie besitzt; Working Directory, Staging Area und lokales Repository; was ein Commit in Git bedeutet |
| 10:30 | Pause | |
| 10:45 | Arbeiten und festhalten | Repository anlegen, Änderungen vormerken und committen, die Historie lesen |
| 12:00 | Mittagspause | |
| 13:00 | In kleinen Schritten arbeiten | Commits als Arbeitsprotokoll: häufig, klein und mit klarer Absicht; aussagekräftige Commit Messages; was nicht ins Repository gehört |
| 14:00 | Sicher experimentieren | Änderungen zurücknehmen, Zwischenstände parken, frühere Stände ansehen – lokale Fehler bleiben folgenlos für das Team |
| 15:15 | Pause | |
| 15:30 | Ein Branch pro Aufgabe | Branches als alltägliches Werkzeug; parallel an mehreren Aufgaben arbeiten und Ergebnisse zusammenführen |
| 16:30 | Übung „Der kaputte Freitag“ | In der Historie den Schritt finden, der die Buchungsstrecke lahmgelegt hat, und ihn gezielt zurücknehmen |
| 17:00 | Ende | |

## Tag 2: Gemeinsam mit Git

Der zweite Tag behandelt die Stationen „Teilen“ bis „Ausliefern“ und endet mit dem Umzug eines SVN-Repositorys nach GitLab.

| Zeit | Modul | Inhalte |
| --- | --- | --- |
| 09:00 | Rückblick | Die Teilnehmenden ergänzen ihre Skizze vom Vortag um das Gelernte |
| 09:30 | Integrieren | Ergebnisse zusammenführen und Konflikte lösen; Integration als bewusster Schritt |
| 10:30 | Pause | |
| 10:45 | Teilen und abholen | Mit Remote-Repositories arbeiten; entscheiden, wann ein Stand veröffentlicht wird |
| 12:00 | Mittagspause | |
| 13:00 | Gemeinsam prüfen | Merge Requests und Code Review in GitLab; die Hauptlinie mit Protected Branches schützen |
| 13:45 | Den Teamablauf vereinbaren | Branching-Strategien wie GitLab Flow oder Trunk-based Development; Rebase oder Merge; Spielregeln für das eigene Team |
| 14:30 | Pause | |
| 14:45 | Den Umzug planen | Migration mit Historie: Projektstruktur, Abhängigkeiten zu anderen Repositories, große Binärdateien; Autoren ermitteln und zuordnen, schrittweise mit git svn migrieren, Tags und Branches übernehmen, bis zum Stichtag mit SVN abgleichen |
| 15:30 | Abschlussübung „Umzugstag“ | Die Teams ziehen das SVN-Repository des Reiseportals nach GitLab um, durchlaufen alle sechs Stationen mit einem Feature und markieren den ersten Release-Stand |
| 16:45 | Abschluss | Neuer Arbeitsablauf neben der Skizze vom Auftakt; Ausblick auf CI/CD; Feedback |
| 17:00 | Ende | |

## Zusatzmodul: Mergen und Merge-Strategien

Das optionale Modul (ca. 75 Minuten) schließt an Modul 12 an und vertieft, was Fast-Forward und 3-Way-Merge (Modul 06), Konflikte (Modul 09) und die Gegenüberstellung von Rebase und Merge (Modul 12) begonnen haben. Es eignet sich für Teams, die ihre Merge-Regeln in GitLab festlegen wollen.

| Thema | Inhalte |
| --- | --- |
| Grundlagen | Was Git beim Mergen vergleicht: Merge-Basis, ours und theirs im 3-Way-Merge |
| Wege der Integration | Merge-Commit (`--no-ff`), Fast-Forward (`--ff-only`), Squash (`--squash`), Rebase mit Fast-Forward; was jeweils in der Historie sichtbar bleibt |
| Strategien und Optionen | Die Strategien ort, recursive, resolve, octopus, ours und subtree; Optionen wie `-X ignore-space-change`, `-X ours`/`-X theirs` und `-X renormalize`; Unterschied zwischen `-X ours` und `-s ours` |
| Konflikte und Korrekturen | Konfliktdarstellung mit `merge.conflictStyle zdiff3`, gelöste Konflikte mit `rerere` wiederverwenden, einen Merge mit `ORIG_HEAD` verwerfen oder mit `git revert -m 1` zurücknehmen |
| GitLab und Best Practices | Merge-Methoden „Merge commit“, „Merge commit with semi-linear history“ und „Fast-forward merge“, Squash-Einstellungen; welcher Weg wozu passt; Regeln vor, beim und nach dem Merge |

**Übung:** „Vier Branches, vier Wege“ (35 Minuten).

Für den Einstieg nach SVN wird „Merge commit with semi-linear history“ mit Squash auf „Allow“ empfohlen. Die Historie bleibt übersichtlich und zeigt trotzdem, wo eine Aufgabe begonnen und geendet hat.

## Zusatzmodul: Der Git-Workflow

Das optionale Modul (ca. 60 Minuten) stellt einen Workflow mit festen Freigaben vor: main hält den produktiven Stand, develop liegt in der Verantwortung der Entwicklung. Es schließt an Modul 12 an und eignet sich für Teams mit versionierten Auslieferungen.

| Branch | Zweck | Entsteht aus | Wird gemergt in | Tag |
| --- | --- | --- | --- | --- |
| main | Produktiver Stand | – | – | Auslieferung, Hotfix |
| develop | Stand der Entwicklung | main (einmalig) | – | Entwicklungsrelease |
| feature/\* | Neue Funktion | develop | develop (Merge Request) | – |
| bugfix/\* | Fehler im Entwicklungsstand | develop | develop (Merge Request) | – |
| release/\* | Release festigen | develop | main, empfohlen auch develop | Auslieferung |
| hotfix/\* | Dringender Fix in Produktion | main | main, empfohlen auch develop | Hotfix |

**Inhalte:** Überblick über alle Branch-Arten mit Grafik, Feature- und Bugfix-Branches, Entwicklungsreleases und Release-Branches, Hotfix-Branches, Verantwortung und Schutz in GitLab, Eignung des Workflows, drei Praxisbeispiele und eine Übung „Ein vollständiger Release-Zyklus“ (45 Minuten).

Die Rückführung von Release- und Hotfix-Branches nach develop ist eine Ergänzung zur Vorgabe. Ohne sie fehlen die Korrekturen im nächsten Release.

## Zusatzmodul: Nachbereitung des Umzugs

Das optionale Modul (ca. 60 Minuten) schließt an die Abschlussübung „Umzugstag“ (Modul 14) an. Es zeigt, wie das migrierte Repository aufgeräumt wird, bevor das Team damit arbeitet. Es eignet sich für Teams, deren SVN-Repository große Binärdateien, svn:externals oder mehrere Teilprojekte enthält.

| Thema | Inhalte |
| --- | --- |
| Git LFS | Große Dateien in der Historie finden (`git lfs migrate info`), nach Git LFS verschieben (`git lfs migrate import`), Ergebnis prüfen (`git lfs ls-files`), neue Dateitypen mit `git lfs track` aufnehmen |
| Submodule | Eine gemeinsame Bibliothek mit relativer URL einbinden, Submodule nach dem Klonen initialisieren, eine neue Version der Bibliothek bewusst übernehmen |
| Repositories schneiden | Ein Verzeichnis mit seiner Historie als eigenes Repository abtrennen und anschließend aus dem ursprünglichen Repository entfernen (`git filter-branch`) |

**Übung:** „Das migrierte Reiseportal aufräumen“ (35 Minuten).

LFS-Migration und Schneiden schreiben die Historie um. Beides gehört deshalb direkt hinter die Migration, bevor das Team das Repository klont.

## Schulungsumgebung und Unterlagen

Für jedes Training wird eine eigene Cloud-Umgebung bereitgestellt. Eine lokale Installation ist daher nicht erforderlich.

- **Unterlagen:** Slides, Dokumentation und Übungen stehen im Schulungsportal der Comquent Academy bereit.
- **Git-Rettungskarte:** Das Cheat Sheet zum Mitnehmen beantwortet die häufigsten Notfälle mit dem passenden Befehl, zum Beispiel „Ich habe auf den falschen Branch committet“.
- **Dozenten:** Alle Dozenten sind als Certified GitLab Fundamentals Associate und Certified GitLab CI/CD Associate zertifiziert.
