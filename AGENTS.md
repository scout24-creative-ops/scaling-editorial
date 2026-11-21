# Scaling Editorial: Skill-Quellen und bestehende Dokumentseiten

## Zuständigkeit

`skills/<technischer-name>/` ist die bearbeitbare Quelle der sechs aktuellen
Scaling-Editorial-Skills: Trend Finder, Story Creator, Article Writer,
Editorial Publisher, Image Creator und Chart Creator. Jeder Ordner ist ein
vollständiges eigenständiges Paket mit eigener SKILL.md und Ressourcen.

Der erste Import vom 21.11.2026 ist datei- und modusgleich zum installierten Stand,
mit Ausnahme nicht benötigter Python-Caches. Keine Regeln, Vorlagen, Snippet-
Verträge oder Modulgrenzen im Rahmen einer Sicherung ändern. Kein zusätzliches
aktives `se-lp-builder`-Paket anlegen; dessen aktuelle Grundlagen sind im Publisher.
Historische Namen bleiben nur Aliase, keine zusätzlichen Skills.

## Änderungen und Sicherung

1. Vor fachlicher Änderung die vollständige SKILL.md und die für die Änderung
   relevanten Referenzen des betroffenen Pakets lesen. Abhängigkeiten beachten.
2. Bei möglicher Abweichung zuerst das Repo gegen die tatsächlich installierte
   persönliche Ausgabe vergleichen; Namen über Frontmatter auflösen, keine
   Skill-ID oder fremden Chat voraussetzen. `skills/check.py --compare-installed`
   liest nur und installiert nichts. Keine stillen Überschreibungen.
3. Ausschließlich im zuständigen Paket bearbeiten; gemeinsame Wirkung auf
   Übergabeverträge oder abhängige Skills prüfen. Keine parallelen Knowledge-,
   Agent- oder Versionsordner erzeugen; Versionierung über Git-Historie.
4. Nach beauftragten Änderungen `python3 skills/check.py --refresh` und dann
   `python3 skills/check.py` ausführen. Die Prüfsummen sind ein Integritätsnachweis,
   kein Nachweis redaktioneller Qualität oder funktionierender App-Anbindungen.
5. Über Branch und PR bereitstellen; kein automatischer Merge. Ein Repo-Merge
   aktualisiert installierte Skills nicht. Eine beauftragte Installation oder
   Aktualisierung separat über den unterstützten persönlichen Skill-Verwaltungs-
   weg ausführen, dort validieren und anschließend die tatsächlichen Dateien prüfen.

Repo und installierter Stand sollen synchron gehalten werden, aber nicht durch
ungesteuerte automatische Überschreibungen. Neue Dateien im betroffenen Paket
vollständig einschließlich Assets, Skripten und UI-Metadaten mitnehmen. Keine
README oder zusätzliche Sicherungsanleitung in einzelne Skill-Pakete kopieren;
die Wiederherstellung ist zentral im Root-README dokumentiert.

## Grenzen und Bestandsschutz

Dieser Repo-Auftrag autorisiert keine Artikelproduktion, CMS-/Wiki-/Datenbank-
Writes, Bildgenerierung, Veröffentlichung, Nachrichten oder Änderungen an anderen
Skills. Für echte fachliche Aufträge bleiben die jeweiligen Skill-Verträge,
nativen Tool-Schemata und konkreten Nutzeraufträge maßgeblich.

MCP-Verbindungen, Authentifizierung, Berechtigungen, Freigaben, externe Wiki-/CMS-
Inhalte und Gesprächsverläufe werden nicht mit diesen Dateien gesichert. Keine
Zugangsdaten, Tokens oder Produktionsdaten in diesem Repo speichern. Eine
Wiederherstellung des Pakets stellt diese externen Voraussetzungen nicht her.

`documents/` und `.github/workflows/publish-documents.yml` erhalten unverändert
die vier bestehenden öffentlichen Dokumentseiten und ihre URLs. Der bestehende
Pages-Workflow veröffentlicht ausschließlich die freigegebenen Dokumente. Skill-
Pakete nicht still in seine Ausgabe aufnehmen und keine Live-Assets umziehen.
