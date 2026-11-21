# Scaling Editorial

Entwicklungsquelle und Sicherung der sechs Scaling-Editorial-Skills sowie
Originalablage für die bestehenden Prozess- und Planungsunterlagen.

## Dokumente

- [Content-Plan](documents/content-planning.html)
- [Editorial-Prozess](documents/flow-chart.html)
- [Trend-Finder-Matrix](documents/master-matrix.html)
- [Arbeitsplan](documents/mvp-workplan.html)

Die vier HTML-Dateien wurden am 14. November 2026 unverändert aus der bisherigen Ablage übernommen. Dieses Repository ersetzt ihre Kopien in `creative-ops` und `public`.

## Im Browser

- [Editorial Flow](https://scout24-creative-ops.github.io/scaling-editorial/flow-chart.html)
- [Trend Matrix](https://scout24-creative-ops.github.io/scaling-editorial/master-matrix.html)
- [Working Plan](https://scout24-creative-ops.github.io/scaling-editorial/mvp-workplan.html)
- [Content Plan](https://scout24-creative-ops.github.io/scaling-editorial/content-planning.html)

## Veröffentlichung

Die vier Originaldateien unter `documents/` sind die einzige bearbeitete Quelle. Änderungen daran auf `main` veröffentlichen automatisch die entsprechende neue Fassung über GitHub Pages.

Der Workflow `.github/workflows/publish-documents.yml` veröffentlicht ausschließlich diese vier freigegebenen HTML-Dateien sowie eine erzeugte Übersichtsseite. Weitere Repository-Dateien werden nicht als Webseiten ausgeliefert. Es sind keine zusätzlichen versionierten Veröffentlichungskopien in `public` erforderlich.

## Skills

Unter `skills/` liegt der vollständige übernommene Stand vom 21. November 2026.
Jeder Skill enthält seine eigene `SKILL.md`, Referenzen, UI-Metadaten, Assets und
gegebenenfalls Skripte. Die 64 Paketdateien wurden unverändert aus den sechs
installierten Skills übernommen; erzeugte Python-Caches gehören nicht zum Paket.

| Skill | Ordner | Anbindungen und zusätzliche Voraussetzungen |
| --- | --- | --- |
| Trend Finder | [scaling-editorial-trend-finder](skills/scaling-editorial-trend-finder/) | Web-Recherche und Scout Wiki; kein Starburst |
| Story Creator | [scaling-editorial-story-creator](skills/scaling-editorial-story-creator/) | Scout Wiki; Starburst ausschließlich für geeignete erlaubte Leseanalysen |
| Article Writer | [scaling-editorial-article-writer](skills/scaling-editorial-article-writer/) | Image Creator für das Titelbild; keine eigene Web-/Wiki-/Starburst-Recherche |
| Editorial Publisher | [scaling-editorial-publisher](skills/scaling-editorial-publisher/) | Contentful Landing Page Builder MCP und Scout Wiki im dokumentierten Umfang |
| Image Creator | [scaling-editorial-image-creator](skills/scaling-editorial-image-creator/) | Bildgenerierung und Python/Pillow; originale AI-Labels sind enthalten |
| Chart Creator | [scaling-editorial-chart-creator](skills/scaling-editorial-chart-creator/) | Python/Matplotlib; benötigte Schriften sind enthalten |

Der Article Writer ruft aktuell den Image Creator auf. Der Chart Creator ist ein
separat nutzbarer Helfer und wird vom aktuellen Writer nicht automatisch aufgerufen.
Der zusammengeführte Publisher enthält seine eigenen technischen Grundlagen;
`se-lp-builder` wird nicht als siebte aktive Kopie übernommen.
Die vollständigen Verträge der einzelnen Skills bleiben für alle Aktionen maßgeblich.

### Sicherung und Wiederherstellung

`skills/manifest.json` enthält für jede Paketdatei SHA-256, Größe und Dateimodus.
Mit `python3 skills/check.py` lassen sich Vollständigkeit und Integrität prüfen.
Git-Historie und der gewählte Commit bestimmen die wiederherstellbare Version;
keine parallelen Versionsordner oder zusätzliche manuell gepflegte Skill-Kopien anlegen.

Zur Wiederherstellung den vollständigen Ordner des gewünschten Skills aus dem
gewählten Repo-Stand verwenden, einschließlich Referenzen, Assets und Skripten.
Dann über den unterstützten persönlichen Skill-Installationsweg neu installieren.
Nur die `SKILL.md` zu kopieren genügt nicht. Beim Article Writer zusätzlich den
Image Creator installieren. Die Neuinstallation hier wurde nicht ausgeführt.

Nicht Teil dieser Sicherung sind persönliche Skill-IDs, Freigaben, MCP-Verbindungen,
Anmeldungen, Tool-Berechtigungen, Gesprächsverläufe sowie die Inhalte externer
Wiki-Seiten, Contentful-Einträge oder Datenbanken. Diese müssen weiterhin verfügbar
sein oder separat eingerichtet werden. Der gleiche Paketstand bedeutet keinen
Anspruch auf identische KI-Texte oder Bilder.

### Weiterentwickeln

`skills/<name>/` ist die bearbeitbare Quelle. Vor Änderungen mit dem tatsächlich
installierten Stand vergleichen, damit spätere manuelle Skill-Änderungen nicht
verloren gehen. Der optionale Vergleich liest nur:

```sh
python3 skills/check.py
python3 skills/check.py --compare-installed /pfad/zum/persoenlichen/skill-checkout
```

Nach beauftragten Änderungen die Prüfsummen mit `python3 skills/check.py --refresh`
aktualisieren und erneut prüfen. Änderungen als PR bereitstellen. Ein Repo-Merge
ändert keine installierten Skills automatisch. Deren Aktualisierung ist ein
separater bewusster Schritt über den unterstützten Skill-Verwaltungsweg; danach
den gespeicherten Stand wieder gegen das Repo prüfen.

Dieser Import enthält keine fachlichen Änderungen und keinen neuen CMS-, Wiki-,
Datenbank- oder Bildgenerierungs-Test. Die bestehende Veröffentlichung der vier
Dokumentseiten bleibt unverändert und liefert die Skill-Dateien nicht als Pages aus.
