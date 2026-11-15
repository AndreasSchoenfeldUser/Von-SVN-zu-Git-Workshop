# ---------- Zusatzmodul: Nachbereitung des Umzugs ----------
crumb = "Zusatzmodul · Nachbereitung des Umzugs"
d.section("Zusatzmodul: Nachbereitung des Umzugs – Git LFS, Submodule und Repositories schneiden",
          "t2-14z-umzug-nachbereitung", "Von SVN zu Git – Zusatzmodul: Nachbereitung des Umzugs")
divider(d, "zn", "+", "Zusatzmodul: Nachbereitung des Umzugs",
        "Wir räumen das migrierte Repository auf: große Dateien nach Git LFS, gemeinsame Bibliotheken als Submodule, Teilprojekte in eigene Repositories.",
        "ZUSATZMODUL · CA. 60 MINUTEN",
        "Dieses Modul ist optional und schließt an den Umzugstag (Modul 14) an. Es eignet sich für Teams, deren SVN-Repository große Binärdateien, svn:externals oder mehrere Teilprojekte enthält.")

content(d, "zn-ueberblick", "Theorie", crumb, "Drei Aufgaben nach dem Umzug",
        cards(3, [
            card("Große Dateien", "Bilder, Videos und Bibliotheken liegen auf dem LFS-Server. Im Repository bleibt nur ein kleiner Verweis.", k="GIT LFS"),
            card("Gemeinsame Bibliotheken", "Ein anderes Repository wird in einer festen Version eingebunden. Das ersetzt svn:externals.", k="SUBMODULE"),
            card("Zu große Repositories", "Teilprojekte samt ihrer Historie in eigene Repositories auslagern.", k="SCHNEIDEN", dark=True),
        ]) +
        '<p class="under">LFS-Migration und Schneiden schreiben die Historie um. Beides gehört direkt hinter die Migration, bevor das Team das Repository klont.</p>',
        "Nach dem Umschreiben haben alle Commits neue IDs. Wer vorher geklont hat, muss neu klonen. Deshalb diese Schritte im Probelauf üben und am Stichtag direkt nach der Migration ausführen.")

praxis(d, "zn-lfs-info", crumb, "Große Dateien finden", [
    "$ git lfs migrate info --everything",
    "*.mp4    1.8 GB     112/112 files   100%",
    "*.jpg    640 MB   2310/2410 files    96%",
    "*.jar     96 MB       41/41 files   100%",
    "*.png     58 MB     380/520 files    73%",
    "",
    "# Nur bestimmte Dateitypen",
    "$ git lfs migrate info --everything \\",
    ">   --include=\"*.mp4,*.jpg,*.png,*.jar\"",
], [
    ("migrate info", "Zeigt, welche Dateitypen wie viel Platz in der Historie belegen. Es ändert nichts."),
    ("--everything", "Durchsucht alle Branches und Tags, nicht nur den aktuellen Branch."),
    ("--include", "Beschränkt die Auswertung auf die genannten Dateimuster."),
], "Die Ausgabe zeigt die Kandidaten für Git LFS: Dateitypen, die viel Platz belegen und sich nicht sinnvoll zeilenweise vergleichen lassen. Quellcode bleibt immer im normalen Repository.",
    lead="Schritt 1: Überblick verschaffen, welche Dateien das Repository groß machen.")

praxis(d, "zn-lfs-import", crumb, "Große Dateien nach Git LFS verschieben", [
    "$ git lfs migrate import --everything \\",
    ">   --include=\"*.mp4,*.jpg,*.png,*.jar\" --verbose",
    "$ git lfs ls-files",
    "3f9a2c41d7 * media/reiseziele/mallorca.mp4",
    "8b1e07c2aa * media/reiseziele/kreta.jpg",
    "$ git push --force --all",
    "$ git push --force --tags",
    "",
    "# Neue Dateitypen künftig über LFS",
    "$ git lfs track \"*.pdf\"",
    "$ git add .gitattributes",
    "$ git commit -m \"PDF-Dateien über Git LFS verwalten\"",
], [
    ("migrate import", "Ersetzt die Dateien in der gesamten Historie durch Verweise und legt die passende .gitattributes an."),
    ("git lfs ls-files", "Listet die Dateien in LFS mit ihrer Referenz (OID)."),
    ("git lfs track", "Trägt neue Muster in .gitattributes ein. Die Datei nicht von Hand bearbeiten."),
], "Weil die Historie umgeschrieben wird, ist ein push mit --force nötig. In GitLab muss dafür der Schutz von main kurz gelockert werden. Danach klonen alle neu. Das Repository in GitLab wird erst kleiner, wenn die alten Objekte aufgeräumt sind (Housekeeping).",
    lead="Schritt 2: Die Migration schreibt die Historie um. Deshalb gehört sie vor die Arbeit im Team.")

praxis(d, "zn-sub-add", crumb, "Eine gemeinsame Bibliothek als Submodule einbinden", [
    "$ git submodule add ../portal-common.git \\",
    ">   externals/portal-common",
    "$ git commit -m \"portal-common als Submodule einbinden\"",
    "$ cat .gitmodules",
    "[submodule \"externals/portal-common\"]",
    "    path = externals/portal-common",
    "    url = ../portal-common.git",
    "",
    "# Nach dem Klonen: Submodule holen",
    "$ git submodule update --init --remote --force",
], [
    ("Relative URL", "../portal-common.git gilt relativ zur Adresse des Reiseportals und funktioniert so mit HTTPS und SSH."),
    ("--init", "Registriert die Submodule aus .gitmodules und klont sie."),
    ("--remote --force", "Holt den neuesten Stand des Branches und verwirft lokale Änderungen."),
], "Ohne --remote wird genau die Version ausgecheckt, die das Reiseportal festhält. Das ist der übliche Weg für reproduzierbare Builds. git clone --recurse-submodules erledigt Klonen und Initialisieren in einem Schritt.",
    lead="Anders als svn:externals ohne Revision zeigt ein Submodule immer auf einen festen Commit.")

praxis(d, "zn-sub-update", crumb, "Eine neue Version des Submodules übernehmen", [
    "$ cd externals/portal-common",
    "$ git checkout main  # falls nötig",
    "$ git pull",
    "$ cd -",
    "$ git status",
    "  modified:   externals/portal-common (new commits)",
    "$ git add externals/portal-common",
    "$ git commit -m \"portal-common auf neuen Stand bringen\"",
    "$ git push",
], [
    ("Im Submodule", "Ein eigenes Repository: neuen Stand der Bibliothek abholen."),
    ("cd -", "Zurück in das Reiseportal."),
    ("git add, commit", "Hält fest, welchen Commit der Bibliothek das Reiseportal ab jetzt verwendet."),
], "git add . funktioniert ebenso, nimmt aber alle anderen Änderungen mit. Der Commit macht die neue Version für das ganze Team verbindlich, so wie jede andere Änderung über einen Merge Request.",
    lead="Eine neue Version der Bibliothek zu übernehmen, ist ein bewusster Schritt mit eigenem Commit.")

praxis(d, "zn-schneiden", crumb, "Verzeichnisse abtrennen und entfernen", [
    "# 1. In einer Kopie als eigenes Repository abtrennen",
    "$ git clone <Reiseportal-URL> hotel-import",
    "$ cd hotel-import",
    "$ git filter-branch -f --prune-empty \\",
    ">   --subdirectory-filter hotel-import/ -- --all",
    "",
    "# 2. Im Reiseportal aus der Historie entfernen",
    "$ git filter-branch --force --index-filter \\",
    ">   'git rm -r --cached --ignore-unmatch hotel-import' \\",
    ">   --prune-empty --tag-name-filter cat -- --all",
], [
    ("--subdirectory-filter", "Das Verzeichnis wird zur neuen Wurzel, nur seine Historie bleibt erhalten."),
    ("--index-filter", "Entfernt das Verzeichnis aus jedem Commit, leere Commits fallen weg."),
    ("--tag-name-filter cat", "Überträgt die Tags auf die neuen Commits."),
], "Erst abtrennen, dann entfernen, sonst ist die Historie des Verzeichnisses verloren. Git selbst empfiehlt heute das schnellere Werkzeug git filter-repo, das zusätzlich installiert werden muss. filter-branch ist in jeder Git-Installation enthalten und zeigt beim Start einen entsprechenden Hinweis.",
    lead="Ein Teilprojekt bekommt ein eigenes Repository und verlässt das Reiseportal, jeweils mit Historie.")

uebung(d, "zn-uebung", crumb, "Das migrierte Reiseportal aufräumen", [
    "Verschaffen Sie sich mit <b>git lfs migrate info</b> einen Überblick und wählen Sie die Dateitypen für Git LFS aus.",
    "Verschieben Sie diese Dateitypen nach Git LFS und prüfen Sie das Ergebnis mit <b>git lfs ls-files</b>.",
    "Binden Sie die Bibliothek <b>portal-common</b> als Submodule ein und übernehmen Sie anschließend eine neue Version.",
    "Trennen Sie das Verzeichnis <b>hotel-import</b> als eigenes Repository ab und entfernen Sie es aus dem Reiseportal.",
    "Teilen Sie beide Repositories in der GitLab-Gruppe Ihres Teams.",
], "35 Minuten", "Teams mit 3 bis 4 Personen", "Ein schlankes Reiseportal mit Git LFS und Submodule sowie ein eigenes Repository hotel-import.",
    notes="Grundlage ist das in Modul 14 migrierte Repository. portal-common liegt bereits in der GitLab-Gruppe jedes Teams. Für die neue Version in Schritt 3 legt die Trainerin oder der Trainer während der Übung einen Commit in portal-common an.")

referenzen(d, "zn-ref", crumb, [
    ("Git Large File Storage", "Projektseite mit Installation, englisch", "https://git-lfs.com/"),
    ("git lfs migrate", "Git-LFS-Handbuch, englisch", "https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.adoc"),
    ("Git Large File Storage (LFS)", "GitLab-Dokumentation, englisch", "https://docs.gitlab.com/topics/git/lfs/"),
    ("Submodule", "Pro Git, Kapitel 7.11", "https://git-scm.com/book/de/v2/Git-Tools-Submodule"),
    ("git filter-repo", "Nachfolger von filter-branch, englisch", "https://github.com/newren/git-filter-repo"),
], "Die Referenz zu git filter-branch rät selbst zu git filter-repo; dessen Dokumentation enthält eine Übersicht, wie sich filter-branch-Aufrufe übertragen lassen. Für Submodule ist Kapitel 7.11 von Pro Git die beste deutschsprachige Darstellung.")
