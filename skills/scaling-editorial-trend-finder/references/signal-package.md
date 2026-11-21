# Signal Package und Dateiübergabe

## Übergabevertrag

Erzeuge für jeden ausgewählten Kandidaten eine **UTF-8-Markdown-Datei (.md)**. Jede Datei enthält genau ein vollständiges Signal Package. Der Story Creator kann diese Datei direkt als Eingabe erhalten; es ist kein Markieren oder Herauslöschen von Recherche-Anhängen nötig.

Verwende exakt die Überschrift `# Signal Package`, ohne Nummerierung, BEGINN-/ENDE-Marker, Codeblock oder Schreibblock. Verwende folgende Abschnitte als H2 in genau dieser Reihenfolge:

1. `Thema` — kurze neutrale Themenbeschreibung, keine finale Artikelheadline. Darunter Metadaten als Bullets mit fett gesetzten Labels: `Vorläufige Rubrik` und `Themen-Tags`. Vorhandene Taxonomy-Bezeichnungen exakt erhalten, Unsicherheiten oder neue Begriffe als Vorschlag kennzeichnen. Für Lifestyle Rubrik `Lifestyle`, kein Feld „Redaktioneller Modus“.
2. `Beobachtetes Signal` — konkrete Entwicklung, Erkenntnis, Veränderung, Debatte oder Ereignis. Tatsachen, Einordnung und Hypothesen trennen.
3. `Leserrelevanz` — betroffene Zielgruppe und möglicher Nutz-, Orientierungs- oder Erkenntniswert.
4. `Mögliche Leserfragen` — mögliche Fragen für den Story Creator, keine verbindlichen Angles oder fertigen Headlines.
5. `Potenzieller eigenständiger Mehrwert` — was ein ImmoScout24-Artikel zusätzlich leisten könnte. Für Lifestyle kann eine eigenständige, verständliche, sorgfältig belegte Nachrichtenaufbereitung genügen; zusätzliche eigene Fakten sind keine Pflicht.
6. `Offene Fragen und Grenzen` — fehlende Fakten, Widersprüche, Unsicherheiten, begrenzte Aussagekraft und nötige Folgerecherche. Kein bloßes „alles geklärt“, wenn wesentliche Einschränkungen bestehen.
7. `Quellen und Evidenz` — sämtliche Quellen mit eindeutiger Zuordnung zu den jeweils belegten Aussagen, Quellenart, Dokumenttitel, vorhandenen Veröffentlichungs-/Ereignisdaten und Bezugsständen sowie **vollständig sichtbar ausgeschriebener Original-URL**.

Erhalte die notwendige Recherche-/Wiki-Herkunft im Package als Metadaten im Abschnitt „Thema“: `Recherchestand`, `Taxonomy-Abgleich` und `Signalhistorie-Abgleich`. Formuliere den tatsächlich belegten Stand einschließlich Ausfällen oder gekennzeichnetem Altstand. Diese Kontextangaben ergänzen das bestehende Web-Signal-Format; erfinde keine Signal-ID.

Jede Quelle muss so lesbar sein:

Quellenname / Dokumenttitel  
Quellenart; Veröffentlichungsdatum beziehungsweise Bezugsstand, soweit bekannt; Ereignisdatum, falls abweichend  
https://vollständige-original-url

Ordne darunter die belegte Aussage und gegebenenfalls Grenzen zu. Erhalte genaue Dokumentpfade und relevante URL-Parameter. Beschriftete Links oder interne Zitationsmarker allein genügen nicht. Benenne fehlende/nicht lesbare URLs ausdrücklich, statt sie zu erfinden. Such-Snippets ersetzen keine Quellenprüfung.

## Inhalt sauber trennen

Ins Package gehören alle für dieses Signal erforderlichen Quellen, Metadaten, Unsicherheiten und Recherchebedarfe. **Nicht hinein** gehören Suchprotokolle, interne Überlegungen, abgelehnte andere Kandidaten, eine Gesamtpriorisierung mehrerer Themen, Folgeaufträge oder Kommentare nach dem Package. Nicht jede Recherche ist ein unerwünschter Anhang: Die tragende Evidenz und nötige Quellen müssen für den Story Creator erhalten bleiben.

Im Chat stehen ein kurzer wahrheitsgemäßer Recherche-/Wiki-Status und genau eine nummerierte Signalübersicht nach chat-output.md. Jeder Listeneintrag enthält die neutrale Themenbezeichnung, eine qualitative Ampel mit Klartext, drei bis vier kurze einordnende Sätze und direkt darunter seinen eigenen echten Package-Download. Die Reihenfolge ist bereits die Gesamtpriorisierung; keine zweite Zusammenfassung oder gebündelte Download-Liste anfügen. Begründe die Einordnung durch Entwicklung, Leserrelevanz, Aktualität, Substanz und Evidenz, ohne Punktesystem oder spekulative Klickprognose. Bei einer reinen Formatübertragung genügt der einzelne Download mit gegebenenfalls konkreten Lücken; keine neu recherchierte Bewertung vortäuschen.

## Dateien zuverlässig erzeugen

Nutze bevorzugt `scripts/render_signal_package.py`: Es nimmt **ein** internes JSON-Objekt an und schreibt ausschließlich die erlaubten Package-Inhalte in eine neue Markdown-Datei. Dieses interne Arbeitsformat ist weder das alte Datenanalyseformat noch ein zusätzliches Übergabepaket. Übergebe den Freelancern die `.md`, nicht die interne JSON-Datei.

Aufruf (Pfade als Argumente sicher quoten, keine Inhalte als Shell-Code interpolieren):

`python3 <skill-root>/scripts/render_signal_package.py --input <arbeitsdatei.json> --output-dir <ausgabeordner>`

Pflichtfelder des internen Objekts:

| Key | Typ und Inhalt |
| --- | --- |
| `theme` | String: neutrale Themenbeschreibung |
| `rubrik` | String: vorläufige Zuordnung, Unsicherheit explizit |
| `tags` | String-Liste; leer zulässig, wenn keine passende Zuordnung |
| `checks` | Objekt mit Strings `research_date`, `taxonomy`, `registry`; tatsächlicher Stand, niemals Standardbehauptung |
| `signal` | String: beobachtetes Signal |
| `reader_relevance` | String: Leserrelevanz |
| `reader_questions` | Nicht leere String-Liste |
| `potential_value` | String: möglicher Mehrwert |
| `limits` | Nicht leere String-Liste; auch offene Fragen und nötige Folgeprüfungen |
| `sources` | Nicht leere Liste von Quellenobjekten |

Quellenobjekt: `title`, `kind`, `evidence` als nicht leere Strings; `publication_date`, `event_date`, `reference_period` jeweils String oder `null`; `url` als tatsächlich vorliegende vollständige HTTP(S)-URL oder `null`. Bei fehlender URL zusätzlich `url_note` mit konkreter Einschränkung, sonst optional. Mindestens eine tatsächlich prüfbare Quellen-URL ist nötig; fehlende zentrale Evidenz muss redaktionell geklärt werden. Unbekannte Felder werden abgelehnt, damit keine Recherche-Anhänge versehentlich in Dateien geraten.

Der Renderer prüft Struktur, keine Fakten. Prüfe die journalistische Qualität, tatsächliche Quellenlektüre und jede übergebene Statusbehauptung selbst. Verwende keine künstlichen Prüfbestätigungen. Lies die komplette erzeugte Datei zurück; prüfe insbesondere sichtbare URLs, Vollständigkeit und fehlende Zusatzabschnitte. Der Renderer meldet nur Pfad, Größe und Hash seiner wirklich geschriebenen Datei, keinen fertigen Download-Link.

Falls der Renderer in einer anderen Umgebung nicht ausführbar ist, erzeuge die Datei mit den dort verfügbaren Dateiwerkzeugen nach demselben Vertrag und prüfe sie vollständig. Der Dateivertrag ist maßgeblich, Python keine fachliche Voraussetzung.

Stelle die Dateien mit der verfügbaren authentifizierten Datei-/Download-Funktion der aktuellen Unterhaltung bereit. Befolge deren aktuelle Speicher- und Linkregeln. Falls die Umgebung eine dauerhafte Ablage für erzeugte Dateien verlangt, speichere dort und verwende die zurückgegebene Dateiidentität. Dies erlaubt keine Ablage in Wiki, CMS, Slack oder einem fremden Projekt. Erfinde weder Sandbox-Pfade noch Datei-IDs oder Links.

Ist kein echter Download möglich, benenne den konkreten Ausgabeblocker. Gib nicht stillschweigend wieder lange Kopierblöcke aus; biete Chattext nur als ausdrücklich wählbare Ausweichlösung an. Behaupte eine Dateiübergabe erst, wenn die Datei tatsächlich verfügbar ist.
