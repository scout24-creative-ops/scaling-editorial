# Bildrollen und drei gehostete Dateien

Aktuelle Vorgabe von Dominik, 24.11.2026. Diese Zuordnung präzisiert „dasselbe Bild“: ein ausgewähltes Motiv in drei Dateien. Sie ändert keine Bildfläche, Klassen, Abstände, Navigation oder URLs von Artikeln.

## Eingaben und Zuordnung

| Bestätigte Hosting-URL | Verwendung | Gelieferte Datei | Sichtbares AI-Label bei KI-Motiv |
| --- | --- | --- | --- |
| `Bild-URL` | Titelbild auf der Artikeldetailseite | WebP, 1920 × 1080 | Ja |
| `Teaser-Bild-URL` | Großer News-Aufmacher, großer Rubrikteaser, mittlere Artikelkacheln | WebP, 1536 × 864 | Ja |
| `Listenteaser-Bild-URL` | Kleine 120 × 80-Teaser rechts auf News | WebP, 480 × 320, 3:2 | Nein; ausdrückliche Ausnahme nur für diese Rolle |

Die Rolle wird nach der konkreten Komponente gewählt, nicht nach Seitenname oder zufälliger bisheriger Position: `lpb-image--responsive` innerhalb der Artikel-Bildfigur → Titelbild; `lpb-editorial-ux-card__image` und `lpb-editorial-ux-category-lead__image` → große/mittlere Teaserdatei; `lpb-editorial-ux-compact__image` → Listenteaserdatei. Die kanonischen HTML-Abmessungen und Seitenverhältnisse der jeweiligen Komponente bleiben erhalten. Eine Aufmacher-zu-Liste-Umplatzierung wechselt die Datei, nicht das Layout oder das Motiv.

Die getrennten 80 × 56-Weiterlesen-Bilder auf Artikeldetailseiten, Autorenporträts, Beispielimmobilien und andere Module sind nicht Bestandteil dieser Umstellung. Erhalte deren vorhandene Bilder. Die Ausnahme für fehlendes sichtbares Label nicht darauf ausdehnen. Alttext, Quellen, Rechtehinweise und KI-Herkunft bleiben auch bei der kleinen Liste korrekt; setze kein erfundenes Label auf eine authentische Aufnahme.

Hole für einen neuen Standard-Artikeleinbau Autorin und alle drei vollständigen Hosting-URLs gebündelt ein. Bereits ausdrücklich persönlich bestätigte Rollen im aktuellen Einbaudialog nicht erneut abfragen; fehlen einzelne, frage nur diese nach. Package-Felder können die Bestätigung vorbereiten, ersetzen sie aber nicht. Download-/Library-Links, lokale Pfade und Platzhalter gelten nicht als Hosting. Erfinde keine Ableitungen durch Dateinamenwechsel, Parameter, Bild-CDN-Pfade oder Hosttausch. Verwende drei eindeutige tatsächlich bestätigte URLs, keine stillschweigende Kopie des Titelbildes in alle Rollen. Keine Bildgenerierung, Umrechnung oder Uploads im Publisher.

Bei einem ausdrücklich auf die Artikelseite begrenzten Auftrag ist nur die Titelbild-URL nötig; fehlende Teaserrollen bleiben offen. Unverwandte Bestandskorrekturen lösen keine neue Bildabfrage oder Bildmigration aus. Eine neue Bildrolle darf nicht aus der sichtbaren Größe einer alten Datei erschlossen werden.

## Zuordnung für Fortsetzungen erhalten

Speichere bei neuen Standardartikeln die drei bestätigten URLs zusätzlich als reine Datenattribute auf dem vorhandenen `div.lpb-editorial-ux--article`:

- `data-lpb-image-title-url`
- `data-lpb-image-teaser-url`
- `data-lpb-image-list-url`

Dies sind zugelassene HTML-Metadaten für den Publisher, keine neuen Contentful-Felder, Styles oder Frontend-Funktionen. Setze echte bestätigte Werte mit normalem HTML-Attribut-Escaping ein; keine Leerwerte oder Vorlagenmarker speichern. Das kanonische Library-Beispiel kennzeichnet die einzusetzenden Werte. Bei einem engeren Artikelauftrag nur die tatsächlich bekannten Rollen hinterlegen.

Beim Umplatzieren eines vorhandenen Artikels seine vollständige bestätigte Zuordnung aus dem aktuellen Artikel-HTML, dem tatsächlich verfügbaren Package oder dem dokumentierten Einbaustand verwenden. Wenn nötig den verifizierten Artikel derselben Site lesen. Nicht die aktuell sichtbare kleine Datei ohne Label in den Aufmacher übernehmen. Fehlt die neue benötigte Rolle, gezielt klären und nur davon abhängige Änderungen stoppen. Unberührte Legacy-Bildbelegungen bleiben erhalten; keine automatische Massennachrüstung. Vorhandene Metadaten bei reinen Fremdänderungen nicht verändern.

Die drei beim Einbau persönlich gewählten URLs und ihr Rollen-/Kennzeichnungsstand werden unter **Umsetzung** in der ohnehin beauftragten Produktionsakte dokumentiert. Das originale Writer-Package mit ursprünglichen Platzhaltern bleibt unverändert archiviert. Ein reiner CMS-Auftrag bleibt ohne Wiki-Schreibschritt.

## Prüfung vor dem Speichern und nach dem Rücklesen

Prüfe das vollständige vorbereitete HTML und danach das vollständig zurückgelesene HTML mit `scripts/check_image_roles.py`. Nutze explizite lokale Dateien und sicher gequotete Argumente; URLs mit Parametern nicht als Shell-Code interpolieren.

- Artikelseite: `--mode article --title-url … --teaser-url … --list-url …`.
- Je Übersicht: `--mode overview` mit denselben drei URLs und `--article-href` aus dem echten verifizierten Linkziel. Der Check prüft nur die ausgewählte Artikelidentität, nicht sämtliche Bestandsbilder gegen dieselben URLs.
- Rücklesen: zusätzlich `--expected-html` mit der erfolgreich vorgeprüften Eingabe, ohne diese danach zu überschreiben.
- Ausschließlich bei bewusst engem Artikelauftrag darf `--article-only` mit der tatsächlichen Titel-URL benutzt werden. Das ist keine Umgehung fehlender Rollen im Standardauftrag.

Der Helfer prüft URL-Sicherheit und eindeutige Rollenwerte, das Titelbild und die drei gespeicherten Datenattribute, die zur Teaservariante passende Datei, kanonische Seitenverhältnisse bzw. 120 × 80, genau ein ausgewähltes Bild pro Ziel und die erhaltenen Bildattribute beim Rücklesen. Ungeprüfte `picture`-/`srcset`-Quellen dürfen die Rollen nicht umgehen. Der Helfer liest nur und verändert oder lädt nichts. Er belegt keine Servererreichbarkeit, echten Dateipixel, Dateigröße, Bildqualität, Kennzeichnung im Bild oder Browserdarstellung.

Bei fehlendem Python dieselben Zuordnungen auf vollständiger Eingabe und Rücklesefassung nachvollziehbar mit einem anderen Parser prüfen; keinen ausgeführten Helfer behaupten. Ein nicht verlässlich geprüfter oder fehlerhafter Rollenabgleich stoppt davon abhängige Writes/Platzierungen. Bei gespeichertem Teilstand die bestätigten IDs erhalten und konkret melden, was noch offen ist.
