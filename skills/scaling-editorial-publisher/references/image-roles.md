# Zwei gehostete WebPs, ein Motiv

Verbindlich für Magazin-Entwürfe seit 25.11.2026:

| Bestätigte Hosting-URL | WebP-Datei (16:9) | Verwendung |
| --- | --- | --- |
| `Bild-URL` | 1920 × 1080 | Artikelaufmacher, News-/Rubrik-Lead und mittlere Karten |
| `Listenteaser-Bild-URL` | 480 × 270 | Kleine News-Teaser und Weiterlesen, jeweils bei 128 × 72 px |

Bei KI-generierten Motiven enthalten beide Dateien das Original-Label „AI Created“, bei wesentlich KI-bearbeiteten das passende „AI modified“. Die frühere Ausnahme für kleine News-Teaser entfällt. Maß und Rahmen erhalten; das vollständige Label soll im kleinen Slot sichtbar sein und nicht abgeschnitten werden. Keine dritte Bilddatei oder separate unmarkierte Variante. Authentische Fotos, graue Platzhalter und unveränderte echte Porträts erhalten kein falsches KI-Label. Autorinnenporträts verwenden die registrierten quadratischen 240 × 240-WebPs und bleiben im Layout rund. Keine aus dieser Entwurfsregel abgeleitete rechtliche Freigabe oder Livegang.

## Abfragen und speichern

Bestätige für Standardaufträge beide vollständigen, voneinander verschiedenen HTTPS-WebP-URLs und die Autorin. Wiederhole bereits dafür beantwortete Fragen nicht. Für einen ausdrücklich reinen Artikelauftrag genügt die große URL. Verwende weder Downloadlinks noch abgeleitete/erfundene URLs. Keine Bildgenerierung, Umrechnung oder Uploads durch den Publisher.

Auf dem vorhandenen Artikelroot `div.lpb-editorial-ux--article` nur `data-lpb-image-title-url` und `data-lpb-image-list-url` hinterlegen (nur bekannte Rollen bei Artikel-only). Kein drittes Attribut, kein neues Contentful-Feld. Verwende bei Umplatzierungen nur bestätigte Werte aus dem Artikelroot, Package oder belegtem Einbaustand. Bei älteren Einträgen fehlende Rollen gezielt klären statt Dateien abzuleiten oder automatisch zu migrieren. Ein unberührter Altbestand wird nicht umgebaut. Dokumentiere bei einem ohnehin beauftragten Wiki-Schritt die zwei URLs und den Prüfstatus unter Umsetzung; Original-Package unverändert lassen.

- Titelbild `lpb-image--responsive` in der Bildfigur, `lpb-editorial-ux-card__image` und `lpb-editorial-ux-category-lead__image`: große URL, `width="1920" height="1080"`.
- `lpb-editorial-ux-compact__image` und verlinktes `lpb-editorial-ux-reading__image`: kompakte URL des jeweils verlinkten Artikels, `width="128" height="72"` und beauftragter Inline-Stil laut Portal-UX. Dieselbe kompakte URL für beide Slots. Beim Wechsel von Lead zu Liste die Datei bewusst wechseln.

## Vor- und Rückleseprüfung

Validiere vollständige Eingabe und Rücklesefassung mit `scripts/check_image_roles.py --html … --mode article --title-url … --list-url …`. Für Übersichten `--mode overview --article-href …` mit dem exakt verifizierten Ziel, beim Rücklesen zusätzlich `--expected-html …`. Bei ausdrücklich reinem Artikelauftrag `--article-only` und nur die Titel-URL. Prüfe für verlinktes Weiterlesen die kompakte URL des verlinkten Artikels auf dieselbe Weise (als einzelnes Linkziel in `--mode overview`); unverlinkte Beispielinserate sind keine Empfehlungen. Der Helfer prüft HTML/URL-Zuordnung und deklarierte Maße, nicht Server, echte Pixel, Dateityp-Bytes, Gewicht oder sichtbare KI-Kennzeichnung. Prüfe letztere an tatsächlichen Assets/Previews, sofern zugänglich. Fehlt eine verlässliche Rollenprüfung, stoppe davon abhängige Writes und melde die konkrete Lücke.
