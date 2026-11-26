# Vollständige Packages als Dateien

## Allgemeiner Vertrag

Erzeuge UTF-8-Markdown-Dateien mit genau einem vollständigen Dokument je Datei. Inhalt und Abschnittsreihenfolge sind im Ausgabevertrag verbindlich. Alle notwendigen Quellen, Fakten, Einschränkungen und Metadaten bleiben im eigentlichen Übergabepaket. Keine manuellen Kopiermarken und keine Recherche-Anhänge am Package. Stelle nur tatsächlich erzeugte und verfügbare Dateien als Downloads bereit.

Erzeuge keine neue Datei oder Package-Hülle bei einem engeren Auftrag, der nur HEADLINE_TEST, kurze Prüfung oder Feedback verlangt. Bei reiner Übertragung bestehender Inhalte ist die Datei möglich, eine neue Recherche oder Bildarbeit aber nicht automatisch erfolgt.

## Strukturiert erzeugen

Nutze bevorzugt `scripts/write_package.py` aus diesem Skill. Aufruf:

`python3 <skill-root>/scripts/write_package.py --input <internes-arbeitsobjekt.json> --output-dir <ausgabeordner>`

Übergebe Inhalte als Datei und sicher gequotete Pfadargumente, niemals als interpolierten Shell-Code. Das interne JSON ist nur ein Arbeitsobjekt und wird nicht als zusätzlicher Pflichtschritt an Freelancer übergeben. Die Markdown-Datei ist das Übergabepaket.

Das Arbeitsobjekt enthält **exakt** diese Felder:

- `kind`: `article` für das vollständige Article Package.
- `topic`: kurzer neutraler Bezeichner nur für den Dateinamen, keine zusätzliche finale Headline.
- `metadata`: Liste von Objekten mit exakt `label` und `value`, beides Strings. Pflichtlabels in dieser Reihenfolge: `Auftrag`, `Rubrik`, `Themen-Tags`, `Platzierung`, `Slug-Vorschlag`, `Autor`, `Rolle`, `Veröffentlichungsdatum`, `Status`, `Bild-URL`. Bei ausdrücklich beauftragtem Update danach die tatsächlich übergebene `Entry-ID` oder `Zielseite`, sofern vorhanden; bei einer ausdrücklichen Längenvorgabe zusätzlich `Längenvorgabe`. Platzhalter und Werte exakt nach Ausgabevertrag.
- `sections`: Liste von Objekten mit exakt `heading` und `body`, beides nicht leere Strings. Abschnittsnamen und Reihenfolge exakt aus dem Ausgabevertrag übernehmen. Nur `Offene Prüfungen` darf bei fehlenden offenen Prüfungen entfallen; alle anderen Abschnitte bleiben vollständig. „Headline-Alternativen“ enthält genau zwei Review-Bullets.
- `source_urls`: Liste der tatsächlich verwendeten vollständigen öffentlichen Original-URLs. Jede muss im jeweiligen Quellenabschnitt sichtbar auf eigener Zeile stehen; erhaltene Pfade und relevante Parameter nicht ändern. Interne Wiki-Arbeitsgrundlagen sind keine öffentlichen Artikelquellen. Nicht vorhandene URLs ausdrücklich im Inhalt kennzeichnen, nie erfinden; eine fehlende tragende Quelle nicht durch eine leere Liste scheinbar lösen.

Bei einem Article Package bleiben Artikel-Zwischenüberschriften H3. Nur die wirklich vorliegenden Bildmetadaten übernehmen und eine fehlende oder unvollständige Bildarbeit explizit kennzeichnen. Die Downloads für Titelbild/große Teaser und Kompaktbild werden getrennt bereitgestellt und ersetzen keine Hosting-URLs. Die separaten Listenteaser-Dateiangaben und Platzhalter bzw. echten Hosting-URLs gehören in den bestehenden Titelbild-Abschnitt, nicht in zusätzliche JSON-Felder oder Hauptabschnitte. Erhalte die Bild-Skill-Prüfangaben wahrheitsgemäß.

Das Skript erzeugt Überschrift und H2-Abschnitte selbst. Körpertexte dürfen H3-Unterabschnitte enthalten, aber keine zusätzlichen H1/H2, Setext-Überschriften, Pakettrenner oder Codeblöcke, die die Dateiübergabe verändern. Unbekannte Felder, zusätzliche oder doppelte Hauptabschnitte und fehlende Pflichtangaben werden zurückgewiesen. So kann keine separat übergebene Recherchebegründung unbemerkt als eigener Anhang im Package landen.

Der Renderer validiert Struktur und zählt die Wörter aus `Introtext` plus `Artikel`. Er zählt sichtbare, durch Leerraum getrennte Wörter mit mindestens einem Buchstaben oder einer Ziffer; Bindestrichwörter und Zahlen zählen jeweils als ein Wort. Markdown-/HTML-Überschriften, Linkziele, Bilder und Captions zählen nicht mit; Linktexte zählen mit. Die Ausgabe meldet `articleWords`; die Wortzahl blockiert den Export nicht. Fakten, Recherche, Freigaben und Bildqualität prüft das Skript nicht. Lüge keine Prüfbestätigung in Statusfelder. Lies jede tatsächlich erzeugte Datei vollständig zurück und prüfe Inhalt und Quellenzuordnung selbst. Der technische Dateiname ist keine Signal-ID, Registry-Registrierung oder neue fachliche Paketversion.

Falls Python oder das Skript in einer anderen Umgebung nicht ausführbar ist, verwende dortige Dateiwerkzeuge mit genau demselben Dateivertrag und vollständiger Rückleseprüfung. Zähle mit einem tatsächlich verfügbaren Werkzeug nach derselben Regel; ohne verlässliche Zählung die offene Längenprüfung ausdrücklich melden und keine bestandene Prüfung behaupten. Erfinde kein funktionierendes Skriptergebnis.

## Bereitstellung

Nutze die authentifizierte Dateifunktion der aktuellen Unterhaltung. Befolge deren aktuelle Speicher-, Export- und Linkregeln; wenn dauerhafte Speicherung vorgeschrieben ist, verwende die tatsächlich verfügbare Ablage und zurückgegebene Dateiidentität. Keine Uploads ins Wiki, CMS, Slack, fremde Projekte oder andere Empfänger. Keine fremden Dateien oder früheren Chats durchsuchen, nur um einen Download zu erzeugen.

Gib nur tatsächlich verfügbare Download-Links aus, keine erfundenen Dateipfade oder Datei-IDs. Ist kein Download möglich, benenne den konkreten Ausgabeblocker und biete Chattext lediglich als ausdrücklich wählbare Ausweichlösung an. Behaupte die Dateiübergabe erst nach erfolgreicher Bereitstellung. Eine Datei wird nicht automatisch in einen anderen Chat übertragen.
