# Vollständige Packages als Dateien

## Allgemeiner Vertrag

Erzeuge UTF-8-Markdown-Dateien mit genau einem vollständigen Dokument je Datei. Inhalt und Abschnittsreihenfolge sind im Ausgabevertrag verbindlich. Alle notwendigen Quellen, Fakten, Einschränkungen und Metadaten bleiben im eigentlichen Übergabepaket. Keine manuellen Kopiermarken und keine Recherche-Anhänge am Package. Stelle nur tatsächlich erzeugte und verfügbare Dateien als Downloads bereit.

Erzeuge keine neue Datei oder Package-Hülle bei einem engeren Auftrag, der nur HEADLINE_TEST, kurze Prüfung oder Feedback verlangt. Bei reiner Übertragung bestehender Inhalte ist die Datei möglich, eine neue Recherche oder Bildarbeit aber nicht automatisch erfolgt.

## Strukturiert erzeugen

Nutze bevorzugt `scripts/write_package.py` aus diesem Skill. Aufruf:

`python3 <skill-root>/scripts/write_package.py --input <internes-arbeitsobjekt.json> --output-dir <ausgabeordner>`

Übergebe Inhalte als Datei und sicher gequotete Pfadargumente, niemals als interpolierten Shell-Code. Das interne JSON ist nur ein Arbeitsobjekt und wird nicht als zusätzlicher Pflichtschritt an Freelancer übergeben. Die Markdown-Datei ist das Übergabepaket.

Das Arbeitsobjekt enthält **exakt** diese Felder:

- `kind`: `story` für das Story Package oder `research` für die getrennte Recherchebegründung.
- `topic`: kurzer neutraler Bezeichner nur für den Dateinamen, keine zusätzliche finale Headline.
- `metadata`: Liste von Objekten mit exakt `label` und `value`, beides Strings. Für beide Dokumente eine leere Liste; Story-Metadaten gehören in „Redaktionelle Einordnung“.
- `sections`: Liste von Objekten mit exakt `heading` und `body`, beides nicht leere Strings. Abschnittsnamen und Reihenfolge exakt aus dem Ausgabevertrag übernehmen. Kein Abschnitt ist optional. Negative Entscheidungen erzeugen kein Story Package.
- `source_urls`: Liste der tatsächlich verwendeten vollständigen öffentlichen Original-URLs. Jede muss im jeweiligen Quellenabschnitt sichtbar auf eigener Zeile stehen; erhaltene Pfade und relevante Parameter nicht ändern. Interne Wiki-Arbeitsgrundlagen sind keine öffentlichen Artikelquellen. Nicht vorhandene URLs ausdrücklich im Inhalt kennzeichnen, nie erfinden; eine fehlende tragende Quelle nicht durch eine leere Liste scheinbar lösen.

Bei `research` verwende exakt diese Abschnitte: `Entscheidung und Arbeitsstand`, `Story-Kern`, `Evidenz-Ledger`, `Befund und Interpretation`, `Gegenprüfung`, `Nächste Schritte`. Die Recherchedatei trägt `# Recherche und redaktionelle Begründung`; sie ist nicht der Writer-Handoff. Öffentliche Quellen-URLs in ihr ebenfalls vollständig sichtbar angeben.

Das Skript erzeugt Überschrift und H2-Abschnitte selbst. Körpertexte dürfen H3-Unterabschnitte enthalten, aber keine zusätzlichen H1/H2, Setext-Überschriften, Pakettrenner oder Codeblöcke, die die Dateiübergabe verändern. Unbekannte Felder, zusätzliche oder doppelte Hauptabschnitte und fehlende Pflichtangaben werden zurückgewiesen. So kann keine separat übergebene Recherchebegründung unbemerkt als eigener Anhang im Package landen.

Der Renderer validiert Struktur, nicht Fakten, Recherche, Freigaben oder Bildqualität. Lüge keine Prüfbestätigung in Statusfelder. Lies jede tatsächlich erzeugte Datei vollständig zurück und prüfe Inhalt und Quellenzuordnung selbst. Der technische Dateiname ist keine Signal-ID, Registry-Registrierung oder neue fachliche Paketversion.

Falls Python oder das Skript in einer anderen Umgebung nicht ausführbar ist, verwende dortige Dateiwerkzeuge mit genau demselben Dateivertrag und vollständiger Rückleseprüfung. Erfinde kein funktionierendes Skriptergebnis.

## Bereitstellung

Nutze die authentifizierte Dateifunktion der aktuellen Unterhaltung. Befolge deren aktuelle Speicher-, Export- und Linkregeln; wenn dauerhafte Speicherung vorgeschrieben ist, verwende die tatsächlich verfügbare Ablage und zurückgegebene Dateiidentität. Keine Uploads ins Wiki, CMS, Slack, fremde Projekte oder andere Empfänger. Keine fremden Dateien oder früheren Chats durchsuchen, nur um einen Download zu erzeugen.

Gib nur tatsächlich verfügbare Download-Links aus, keine erfundenen Dateipfade oder Datei-IDs. Ist kein Download möglich, benenne den konkreten Ausgabeblocker und biete Chattext lediglich als ausdrücklich wählbare Ausweichlösung an. Behaupte die Dateiübergabe erst nach erfolgreicher Bereitstellung. Eine Datei wird nicht automatisch in einen anderen Chat übertragen.
