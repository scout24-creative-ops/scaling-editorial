# Autoren-Overlay – aktueller Magazinstandard

Stand: 20.11.2026. **Der Rollout auf alle acht erfassten Magazinartikel ist ausdrücklich beauftragt und umgesetzt.** Für neue Magazinartikel gilt nach bestätigter Autorinnenwahl dieser Overlay-Standard. Bestehende Overlays bei Teiländerungen erhalten. Keine Veröffentlichung und keine Migration anderer Sites.

## Einsatz und Voraussetzungen

`scaling-editorial-author-dialog` ist eine Embedded-Variante des bestehenden Autorenblocks im Metadaten-Slot, kein Page Module. Sie ersetzt bei ausdrücklicher Beauftragung genau einen Autorenblock; H1 → Autor/Metadaten → Intro → Titelbild → Artikelkörper und Schlussabstand bleiben unverändert. Unabhängige Artikelkorrekturen erhalten die bisherige Verlinkung.

Vor dem ersten CMS-Einbau müssen alle Voraussetzungen nachgewiesen sein:

1. Die zentrale Bridge und Runtime mit dieser Komponente wurden separat zur Auslieferung freigegeben und ihre Verfügbarkeit im tatsächlichen Magazin-Renderer geprüft. Ein privater Entwicklungsstand, eine Skillinstallation oder funktionierende isolierte Vorschau beweist das nicht. Der tatsächliche Renderer muss dialog, hidden, IDs und aria-/data-Attribute erhalten.
2. Portrait, Name und Rolle stammen aus der zentralen Autorenliste; die Autorin ist für den Artikel bestätigt. Inga Ervig und Julia Walter bleiben die einzigen wählbaren Autorinnen. Für Julia und Inga die registrierten quadratischen WebPs verwenden; der sichtbare Kreis bleibt erhalten.
3. Eine vom Nutzer bestätigte Kurzvorstellung liegt für genau diese Autorin vor. Fehlt sie, gezielt nach dem Text fragen. Keine Biografie aus Namen, Artikeltexten oder externen Profilen ableiten, keine Recherche starten und keine persönlichen Angaben erfinden. Ein bereits bestätigter gespeicherter Text muss bei Folgeaufträgen nicht neu erfragt werden.
4. Der konkrete Auftrag bezeichnet das einzelne CMS-Ziel eindeutig. Zunächst nur eine ausdrücklich beauftragte Testseite anpassen, vollständig zurücklesen und auf Desktop und schmalem Display prüfen. Weitere Artikel erst nach gesondertem Rolloutauftrag. Vorher bestehende ID, Site, Slug, Autorinnenzuordnung, Datum, Lesezeit und den gesamten restlichen Inhalt erhalten.

Fehlt die zentrale Technik, die technische oder visuelle Prüfung oder die Kurzvorstellung, den genauen offenen Punkt nennen. Kein per-Page-JavaScript, Script-Tag, Inline-Eventhandler, Runtime-Loader, eigene Style-Datei oder improvisierter CSS-Dialog als Ersatz. Bei normalen Artikeleinbauten ohne Overlay-Auftrag bleibt der bestehende Autorenstandard benutzbar.

## Kanonischer Vertrag

Den vollständigen Block aus component-library.html lesen. Zulässige Ersetzungen: bestätigter Name, Rolle, Portrait/Alttext, freigegebene Kurzvorstellung als sicherer Klartext, vorhandene Artikelmetadaten sowie konsistent eindeutige IDs. Zusätzlich zur vollständigen Beschreibung den bestätigten LinkedIn-Link als normalen Textlink „LinkedIn-Profil ansehen“ in einem Absatz mit der vorhandenen Klasse lpb-editorial-author-dialog__bio vor die Schließen-Aktionen setzen. target="_blank" und rel="noopener noreferrer" verwenden. Keine zweite Schaltfläche und keine erfundenen Profile. Der Beschreibungsabsatz mit data-lpb-author-bio bleibt erhalten. `data-lpb-author-bio-status="review-pending"` gehört zur Gestaltungsvorlage und zum ausdrücklich beauftragten einzelnen eNoVA-Funktionstest; dort steht ausschließlich „Die Kurzvorstellung folgt. Dieses Overlay ist ein Funktionstest.“. Für regulären Einsatz durch `approved` mit tatsächlich bestätigtem Text ersetzen. Das Attribut allein beweist keine Freigabe. Beispieltext und offene Datums-/Lesezeitwerte niemals über echte Artikeldaten kopieren.

- Root: `.lpb-editorial-author[data-lpb-component="scaling-editorial-author-dialog"]`; registrierte author-id und assigned-Status erhalten.
- Statischer Name `[data-lpb-author-static]` ist initial sichtbar. Namensbutton `[data-lpb-author-open]` und `dialog[data-lpb-author-dialog]` sind initial hidden.
- Namensbutton: type button, aria-haspopup dialog, aria-expanded false, aria-controls exakt Dialog-ID. Kein href und kein target blank.
- Dialog: kanonische Klasse `lpb-editorial-author-dialog`, eindeutige ID, aria-labelledby exakt Überschrift-ID, aria-describedby exakt Kurzvorstellungs-ID. Die beiden Ziel-IDs sind vorhanden und ebenfalls eindeutig. Namen plus Instanzsuffix verwenden und alle Referenzen gemeinsam ersetzen, nie IDs zwischen Artikeln/Instanzen mischen.
- Dialoginhalt: registriertes rundes Portrait, Name mit data-lpb-author-title, Rolle, bestätigter Klartext mit data-lpb-author-bio, sichtbarer Button Schließen mit type button und data-lpb-author-close.
- Root-gebundene zentrale Runtime zeigt den Button erst nach erfolgreicher Prüfung von Markup und nativer Dialog-Unterstützung. Ohne Enhancement bleibt der Name ungeklickter Text, die Biografie verborgen. Kein automatisch zurückfallender externer Profil-Tab.

## Verhalten und Prüfung

Geplant und implementiert: showModal im nativen Top Layer, dunkler transparenter Backdrop, Fokus auf Schließen, nativer Modal-Fokus und Escape, Schließen per Button oder außerhalb begonnenem/abgeschlossenem Klick, Fokus zurück auf Namensbutton. Klick in Dialog-Padding oder Ziehen vom Inhalt nach außen darf nicht schließen. Hintergrundscroll ist während des offenen Dialogs gesperrt. Schmale Displays erhalten eine begrenzte, bei langen Texten scrollbare Box. Wiederholtes init und Live-Preview-Ersatz müssen ohne doppelte Handler oder zurückbleibende Scrollsperre funktionieren.

Eine Browserprüfung muss Öffnen via Maus/Enter/Leertaste, Tab/Shift+Tab, Escape, Button/Backdrop, Fokus-Rückgabe, mehrere Autorinnen/Instanzen, Root-Begrenzung, fehlendes JavaScript/native Unterstützung, lange Texte und mindestens 320/390 px prüfen. Nicht getestete Browser oder echte Geräte nicht als verifiziert bezeichnen.

## Nachgewiesener Auslieferungs- und CMS-Stand

Nach ausdrücklicher Nutzerfreigabe wurden nur die neuen opt-in Ergänzungen in den bestehenden öffentlichen Contentful-CSS-/JS-Dateien ausgeliefert. Öffentlicher Commit d29450101d8fd7b34f2a32c849f90babf74af7ac; Pages-Deployment 44725837435 erfolgreich. Die tatsächlich ausgelieferten Bytes beider Dateien stimmen mit dem abgegrenzten Release überein; keine privaten Library-Erweiterungen und keine anderen Runtime-Dateien wurden übernommen. Quellstand und Baseline liegen in scout24-creative-ops/lp-builder-contentful.

Einziges CMS-Testziel: site magazine, Entry 3y9fa8c47UrnHmI0vfHgHL, /magazine/immobilienkauf-digital-enova. Version 3 ist als unveröffentlichter Entwurf gespeichert und vollständig zurückgelesen; HTML und Integritätswerte stimmen. Nur der Autorenblock änderte sich. Inga Ervig samt vorhandenem Portrait, Datum 12.11.2026, Lesezeit 3 Minuten und übriger Artikel blieben erhalten. Der Testtext ist keine freigegebene Biografie. Der tatsächliche Renderer erhält dialog, hidden und alle erforderlichen ID-/ARIA-/data-Attribute.

Die 16 bestehenden Runtime-Regressionstests bestehen. Acht neue vollständige Playwright-Prüfungen sind vorbereitet, konnten in der Ausführungsumgebung aber Chromium nicht starten. Direkt auf der eNoVA-Seite im Desktop-Chromium geprüft: Öffnen per Namensklick, Enter und Leertaste; sichtbares Portrait/Name/Rolle/Testtext; abgedunkelter Hintergrund; Schließen per Button, Escape und Klick auf den Hintergrund; Fokus-Rückgabe zum Namensbutton und aria-expanded false nach dem Schließen. Beim Tab-Test blieb der Hintergrund nicht fokussierbar (Browser-Body als nativer Zwischenstopp). Ein frischer Seitenaufruf lud die neue Technik; ein bereits geöffneter Tab behielt zunächst den alten Asset-Stand (max-age=600). Screenshot des offenen Overlays gesichert. Das ist eine Desktop-Stichprobe, keine mobile, Safari- oder vollständige Acht-Test-Playwright-Abnahme. Keine weitere Seite wurde umgestellt.

## Aktueller freigegebener Rollout und Wiki-Stammdaten

Dominik hat am 20.11.2026 nach Abnahme beider Autorinnen-Tests den Rollout auf alle Magazinartikel und Julias Namenskorrektur einschließlich aller Teaser beauftragt. Dies ersetzt den oben historisch dokumentierten Einzelseiten-Testumfang. Die nachfolgenden Angaben wurden vollständig aus https://wiki.scout24.com/spaces/product-intelligence/pages/68902/autorenregister gelesen und sind für die beauftragten Overlays bestätigt. Beschreibung vollständig übernehmen, Portraitdateien nicht umbenennen. Bei einem ausdrücklich beauftragten Register-Update die genaue Wiki-Seite frisch lesen. Für neue Artikel bleibt die persönliche Autorinnenwahl erforderlich; reine Autorenstammdatenkorrekturen am Bestand brauchen keine neue Artikel-/Bildauswahl.

```json
[
  {
    "id": "inga-ervig",
    "name": "Inga Ervig",
    "role": "Freie Autorin",
    "portrait": "https://www.static-immobilienscout24.de/statpic/scaling-editorial/c2e67242abf8f7858ad7ee881a9abbf7_scaling-editorial-portraet-inga-ervig-v02.webp",
    "bio": "Als Redakteurin für verschiedene Bauherren- und Haustechnikmagazine hat sich Inga Ervig mehr als zehn Jahre lang mit Themen rund um die energetische Modernisierung, Heiztechnologien und nachhaltiges Sanieren beschäftigt. Die studierte Germanistin und Kulturmanagerin hat ein Faible für historische Altbauten. Inga arbeitet als selbstständige Content Marketing Managerin und übersetzt gerne Bau-Fachchinesisch in verständliche und unterhaltsame Artikel.",
    "profile": "https://www.linkedin.com/in/inga-ervig/"
  },
  {
    "id": "julia-walter",
    "name": "Julia Walter",
    "role": "Freie Autorin",
    "portrait": "https://www.static-immobilienscout24.de/statpic/scaling-editorial/460d851cbbd183a405ec8785a4dfd928_scaling-editorial-portraet-julia-walter-v02.webp",
    "bio": "Julia Walter arbeitet seit 2019 hauptberuflich als Copywriterin. Wohnen, Einrichten und Lifestyle begleiten sie dabei seit vielen Jahren. Als Content Expertin war sie unter anderem für zwei Heimwerker-Plattformen und eine App für 360°-Immobilienbesichtigungen tätig. Ihr Schwerpunkt liegt darauf, komplexe Zusammenhänge verständlich zu erklären und die inneren Fragen aufzugreifen, die Menschen bei wichtigen Entscheidungen rund um Immobilienkauf, -verkauf und Mietsuche beschäftigen. Für ImmoScout24 ordnet sie Entwicklungen auf dem Immobilienmarkt ein. Sie erklärt leicht und verständlich, was höhere Zinsen, neue Bauzahlen oder geplante Reformen für Wohnungssuchende und Eigentümer bedeuten.",
    "profile": "https://www.linkedin.com/in/julia-walter2/"
  }
]
```

Alle acht über News, Immobilienmarkt, Lifestyle und deren Artikelverweise ermittelten Magazinartikel haben ein Overlay (vier pro Autorin). Sieben Artikel wurden aktualisiert; eNoVA war bereits korrekt. Acht sichtbare Julia-Fraese-Nennungen auf den drei Übersichtsseiten sind zu Julia Walter korrigiert (News vier, Immobilienmarkt zwei, Lifestyle zwei). Alle zehn geänderten Einträge wurden vollständig zurückgelesen und mit dem validierten HTML und seinen Integritätswerten verglichen. Die Anbindung bietet keine globale Artikelauflistung; dies umfasst den vollständig ermittelten verlinkten Magazinbestand. Keine fremden Inhalte, Datumswerte, Slugs, IDs, Layouts oder Runtime-Dateien geändert und nichts veröffentlicht.
