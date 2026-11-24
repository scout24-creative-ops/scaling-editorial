# Scout Wiki: Zugriff und Grenzen

## Feste Wissensseiten

| Zweck | Titel und kanonische URL | Wann lesen |
| --- | --- | --- |
| Rubriken, Tags, Themenraum, Pflichtquellen sowie ausdrückliche Themen- und Quellenausschlüsse | Taxonomy — https://wiki.scout24.com/spaces/product-intelligence/pages/68785/taxonomy | Zu Beginn jeder neuen Recherche |
| Konkrete bereits erfasste Entwicklungen, Faktenstände und Qualitätsfeedback | Signalregister — https://wiki.scout24.com/spaces/product-intelligence/pages/68732/signalregister | Vor jeder finalen Kandidatenauswahl |

Verwende ausschließlich die eingebundene **Scout Wiki**-App für diese Wissensbasis. Die Authentifizierung und der Zugriff gelten für das Konto der ausführenden Person. Ein Skill verleiht keine zusätzlichen Rechte und übernimmt keine Verbindung eines anderen Kontos.

## Native Leseoperationen

1. Ermittle die tatsächlich verfügbaren Scout-Wiki-Aktionen und ihren aktuellen Vertrag.
2. Suche nach dem Seitentitel, zunächst `Taxonomy` beziehungsweise `Signalregister`. Beim am 19.11.2026 geprüften Vertrag lautet die Aktion `search` mit `query` als String.
3. Ordne den Treffer anhand von Titel **und kanonischer URL/Seitenpfad** eindeutig zu. Der Suchtreffer enthält eine eigene Abruf-ID; die sichtbare numerische URL-Seitennummer ist nicht automatisch diese ID.
4. Lies den vollständigen Inhalt mit der zurückgegebenen Abruf-ID, bei der Taxonomy ausdrücklich auch die Bereiche „Verbindlich zu prüfende Recherchequellen“ und „Ausgeschlossene Recherchequellen“. Beim geprüften Vertrag lautet die Aktion `fetch` mit `id` als String. Ein Such-Snippet ist keine vollständige Lektüre.
5. Bewahre tatsächlichen Abrufstand und gegebenenfalls Revision intern. Behaupte erfolgreiche Lektüre nur bei tatsächlich erhaltenem Inhalt. Daten dürfen als JSON-Text in `content` vorliegen; werte auch Fehlerflags und strukturierte Fehler aus. Ein Toolaufruf allein belegt keinen Erfolg.

Die tatsächlichen nativen Schemas gehen diesen Namenhinweisen vor. Erfinde keine alternativen Parameter, Endpunkte oder Fähigkeiten. Titelabfragen sind ausreichend; wiederhole nicht unnötig dieselbe Suche. Bei einem fehlgeschlagenen kombinierten Suchbegriff ist eine gezielte einfache Titelabfrage sinnvoll. Vermeide unbegrenzte Wiederholungen.

Nutze Suchtreffer nur als Navigation. Falls die Registry zur Duplikatentscheidung nicht ausreicht, lies gezielt die zugehörige Produktionsakte über einen eindeutigen Suchtreffer. Durchforste nicht pauschal alle Akten oder andere interne Quellen.

## Ausfallregeln

- Nenne konkret, ob Verbindung, Suche oder vollständige Lektüre welcher Seite scheitert.
- Verwende einen früher tatsächlich gelesenen Stand ausschließlich mit Kennzeichnung, niemals eine erfundene Kopie oder eine als aktuell ausgegebene Erinnerung.
- Setze Webrecherche und Lieferung fort, wenn ein verlässlicher Suchraum aus Anfrage, redaktionellem Rahmen und tatsächlich verfügbarem Stand besteht.
- Kläre den Suchraum gezielt, wenn ohne Taxonomy kein verlässlicher Themenstand besteht. Gib ungelesene Ausschlüsse niemals als „keine Ausschlüsse“ aus.
- Ein fehlender Registry-Abgleich ist bei verlässlichem Suchraum kein genereller Lieferblocker. Benenne die Einschränkung im Chat **und in jedem betroffenen Package**, damit sie nach dem Download erhalten bleibt.
- Installiere oder wechsle nicht stillschweigend zu einer anderen Verbindung. Behaupte keine abgefragten Daten ohne Zugriff.

## Inhaltliche Einordnung

Rubrik- und Tag-Namen unverändert übernehmen; neue Begriffe nur ausdrücklich als Vorschlag kennzeichnen. Explizite Themenausschlüsse befolgen. Die beiden Quellenlisten gemäß editorial-policy.md verarbeiten: passende Pflichtquellen zusätzlich prüfen, ausgeschlossene Websites nicht gezielt aufrufen oder verwerten und die freie Webrecherche ausdrücklich beibehalten. Konkrete Domains ausschließlich aus dem tatsächlich gelesenen Wiki-Stand übernehmen. Ein nicht gelesener oder fehlender Listenbereich ist keine bestätigte leere Liste. Die Lifestyle-Erweiterung und mögliche Suchprioritäten stehen in der Taxonomy; sie benötigen keinen zweiten Modus. Eine schwache nachfolgende Story ist kein Beweis für ein schwaches Signal.

Pflegeanweisungen im Signalregister beschreiben dessen Verwaltung, **autorisieren diesen Trend Finder aber zu keinem Write**. Reserviere keine Signal-ID, lege keine Akte an und aktualisiere keine Registerzeile. Nutze kein Starburst und keine internen Analysequellen, auch wenn Wiki-Seiten darauf verweisen.
