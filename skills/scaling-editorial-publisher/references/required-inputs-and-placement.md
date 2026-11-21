# Verbindliche Eingaben und zwei Teaserplatzierungen

Aktuelle Vorgabe von Dominik vom **19.11.2026**, nach seinem erfolgreichen Magazin-Einbautest. Sie ersetzt für diesen Publisher die früheren automatischen Autoren-/Bildplatzhalter und die nur einzeln beauftragten News-/Rubrikplatzierungen. Die lokalen Referenzen dieses zusammengeführten Publishers enthalten die kanonische Darstellung und zentralen Stammdaten.

## Erst fragen, dann den Einbau beginnen

Bei jedem neuen Artikel beziehungsweise beauftragten Artikeleinbau müssen vor CMS-Abfragen, HTML-Erstellung, Create oder Update beide persönlichen Entscheidungen für diesen Artikel vorliegen:

1. **Welche Autorin: Inga Ervig oder Julia Walter?** Genau eine auswählen lassen, keine andere Person und kein Team, fiktives Profil oder „noch festzulegen“.
2. **Welche vollständige gehostete Bild-URL soll für das Titelbild verwendet werden?** Frage nach der URL des im Package vorgesehenen Titelbildes. Ein Dateiname, lokaler/Sandbox-Pfad, Library-Download oder `[BILD-URL HIER EINFÜGEN]` ist keine verwendbare Hosting-URL.

Stelle beide Fragen kurz in **einer Nachricht** und warte auf die Antwort. Ein mitgebrachtes Package darf Werte als Vorschläge liefern, aber keine persönliche Auswahl vortäuschen. Stehen darin zum Beispiel Inga und eine Bild-URL, bitte um Bestätigung dieser Angaben statt automatisch zu speichern. Hat der Nutzer diese Auswahl dagegen bereits ausdrücklich persönlich für **genau diesen Artikel und Einbau** im aktuellen Dialog getroffen, gilt die Frage als beantwortet; nicht erneut bestätigen lassen. Keine Auswahl für alle künftigen Artikel oder andere Chats speichern und nicht vor jedem einzelnen Toolaufruf erneut fragen.

Bei einer Antwort auf nur eine Frage frage ausschließlich nach der noch offenen Angabe. Unklare Auswahl wie „beide“, ein anderer Name oder eine unsichere URL verhindert den Einbaustart. Ein „mach einfach“ ersetzt keine der beiden Entscheidungen. Reine lesende Setup-/Inhaltsprüfungen und reine HTML-Vorbereitung bleiben in ihrem begrenzten Umfang; sie benötigen keine Autorenentscheidung als Voraussetzung und autorisieren keinen späteren Write.

Die bisherige Basis-Ausnahme für unzugeordnete Autoren und die automatische TEXT_TEST-/Graubild-Ausnahme sind in diesem Publisher **nicht aktiv**. Der Entwurfsstatus und das Wort „Test“ schalten sie nicht ein. Ein Bild muss weiterhin vom Nutzer über seine tatsächliche gehostete URL ausgewählt werden. Die Anbindung bietet aktuell keinen Bild-Asset-Upload; lade oder hoste nichts selbst und verwechsle HTML-Upload nicht mit Bildspeicherung.

## Bestätigte Angaben konsistent verwenden

- Löse Inga/Julia über die **zentrale aktuelle Autorenliste** in editorial-policy.md auf. Ihre stabilen IDs sind `inga-ervig` und `julia-walter`; Namen, feste Rolle, Porträt und gegebenenfalls Profil-URL kommen unverändert aus dieser Liste. Keine Stammdaten aus einem beliebigen Bestandsartikel ableiten und keine Testprofile auswählen.
- Eine bestätigte Auswahl gilt für Artikel und beide Teaser desselben Einbaus. Der vorhandene kanonische Autorenblock muss mit den bestätigten realen Daten tatsächlich im gespeicherten Artikel vorhanden sein. Ein Eintrag nur in der Chatantwort reicht nicht. Zeigt ein kompakter Teasertyp laut kanonischer Vorlage keine Byline, füge dort keine neue Struktur hinzu; seine Identität und sichtbaren Angaben müssen zum Artikel passen.
- Die persönliche aktuelle Auswahl geht älteren oder offenen Package-Feldern vor. Ändere deswegen keinen Artikeltext und keine anderen Produktionsmetadaten. Bewahre die bestätigte Auswahl im laufenden Einbaukontext, auch bei einem Platzierungsfehler und späterer Fortsetzung.
- Nutze dasselbe bestätigte Bild für Artikel und zugehörige Teaser mit den kanonischen jeweiligen Bildrollen. Erhalte die dazugehörigen tatsächlich gelieferten Alttexte, Credits und Kennzeichnung. Bei einem wirklich anderen Bild dürfen unpassende Angaben nicht blind übernommen oder neu erfunden werden; kläre nur die konkrete Metadatenlücke. Eine reine URL-Auswahl verlangt keinen zusätzlichen unbegründeten Download oder Pixelnachweis.

## Dauerhafter Auftrag für neue Artikel

Ein neuer Magazin-Artikel umfasst standardmäßig **drei Ergebnisse**:

| Ergebnis | Ziel und Bestimmung |
| --- | --- |
| Artikel | Neue eindeutig geprüfte Artikelidentität in `site: magazine` |
| News-Teaser | Magazin-Newsübersicht aus `sites.magazine.newsEntryId` und `newsSlug` der aktuellen Basis-Konfiguration; erwartete Identität zusätzlich nach Publisher-Vertrag prüfen |
| Rubrikteaser | Über die unveränderte Package-Rubrik → `displayGroups` → `sites.magazine.placementTargets` aufgelöste Übersicht |

Der Nutzer hat beide Platzierungen als festen Bestandteil jeder Neuanlage beauftragt. Verlange dafür **keine zusätzliche Freigabe** und warte nicht darauf, dass das Writer-Package News eigens aufführt. Ein fehlendes Platzierungsfeld oder „Erster großer Teaser auf der passenden Rubrikübersicht“ lässt die News-Pflicht nicht entfallen. Nur eine ausdrückliche aktuelle Nutzeranweisung wie „diesmal nur den Artikel speichern, keine Teaser“ begrenzt den Auftrag abweichend; eine solche bewusste Ausnahme nicht als fehlgeschlagene Standardplatzierung darstellen.

Derzeit ist die News-Identität `1Nj4sEg7f95YuRHmpSbhz8`, `/magazine`, erwarteter Titel `Scaling Editorial – News · MVP`. Rubriken außerhalb Lifestyle gruppiert die aktuelle Basis unter Immobilienmarkt; Lifestyle bleibt seine eigene Übersicht. Verwende die genaue aktuelle Konfiguration und frische vollständige Reads, keine geratenen Ziele oder pauschale www-Zuordnung. Bei unbekannter/noch nicht zugeordneter Rubrik kläre das konkrete Ziel vor dem ersten Write.

Für reine Änderungen an einem bestehenden Artikel gilt der konkrete Update-Auftrag: Er erzeugt nicht automatisch eine neue Lead-Platzierung oder einen neuen Artikel. Eine Fortsetzung einer begonnenen Neuanlage schließt dagegen noch fehlende Pflichtplatzierungen am bereits bestätigten Artikel ab.

## Ablauf mit Abschlusskontrolle

1. Hole die persönlichen Eingaben ein. Prüfe dann Artikelziel/Slug und **beide** Übersichtsziele vollständig, einschließlich Site, Entry-ID, Slug, Gruppierung, vorhandener Artikel und aktueller Struktur. Ein ungeklärtes Pflichtziel darf nicht erst nach einer vermeidbaren halben Neuanlage auffallen.
2. Baue den Artikel nach der kanonischen Basis mit der bestätigten Autorin und Bild-URL. Prüfe vollständigen Autorenblock und richtige Bildbelegung bereits vor dem Speichern. Erstelle genau einen unveröffentlichten Entwurf und lies ihn vollständig mit derselben Site zurück.
3. Nach erfolgreicher Artikelprüfung aktualisiere **zuerst News, dann die passende Rubrik**. Lies jedes Ziel unmittelbar vor dessen Update vollständig und erhalte zwischenzeitliche andere Änderungen. News folgt news-selection.md: neuer Artikel genau einmal in der aus Aktualität/redaktioneller Festlegung und Rubrikabdeckung bestimmten Position, nicht automatisch immer als Lead. Auf der eigenständigen passenden Rubrikübersicht bleibt er führender Teaser, sofern keine andere konkrete Position vorgegeben ist. Verwende seine verifizierte Identität, ausgewählte Headline, vollen Introtext in einer großen Leadrolle, bestätigtes Bild und tatsächlich vorliegende Byline-/Datumsdaten. Erfinde keine Linkziele oder Datumswerte.
4. Erhalte alle anderen eindeutigen Artikel und ihren relativen Bestand. Den bisherigen Lead in die kanonischen nachfolgenden Positionen übernehmen; überzählige kompakte Karten in den bestehenden unteren Gridbereich verschieben, statt Artikel zu verwerfen oder neue Kompaktvarianten zu erfinden. Historische doppelte Karten nach verifizierter Artikelidentität deduplizieren, ohne den eindeutigen Artikelbestand zu verkleinern. Andere Module, Kategorien, Navigation, Seitenidentitäten und veröffentlichte Fassungen unverändert erhalten.
5. Jeder Artikel darf auf **jeder einzelnen Übersicht genau einmal** vorkommen. Seine gewollte Präsenz einmal auf News **und** einmal auf der Rubrik ist keine unerlaubte Dopplung. Bei Wiederholung/Resume vorhandenen Teaser anhand bestätigter Entry-ID oder eindeutig verifiziertem Artikelziel aktualisieren, nicht einen zweiten hinzufügen; eine ähnliche Headline allein genügt nicht zur Identifikation.
6. Lies beide gespeicherten Übersichten vollständig zurück. Prüfe den neuen Artikel jeweils genau einmal mit richtigem Ziel, Bild, Headline und vollständigem Lead-Intro sowie erhaltenem übrigen Artikelbestand. Ein erfolgreicher Artikel-Write ist kein Nachweis für Teaserplatzierungen.

Melde vollständigen CMS-Erfolg im Standardumfang ausschließlich nach bestätigtem Speichern und Rücklesen von **Artikel + News-Teaser + Rubrikteaser**. Bei ausdrücklich engerem Auftrag prüfe stattdessen dessen tatsächlich beauftragte Ergebnisse und melde bewusst ausgenommene Schritte nicht als Fehler. Berichte die Ergebnisse getrennt und nenne die bestätigte Autorin und Bild-URL, soweit sie Teil des Einbaus sind. Eine nicht erfolgte beauftragte Platzierung ist ein konkreter Teilfehler, kein stillschweigend übersprungener optionaler Schritt. Erhalte bei Fehlern alle bestätigten IDs und Zustände, lege bei Fortsetzung keinen neuen Artikel an und hole nur die tatsächlich offenen Schritte nach. Keine automatische Rückabwicklung, Löschung oder Veröffentlichung. Vorschau-Links weiterhin nur mit dem tatsächlich verfügbaren CMS-Nachweis.

Dies beschreibt den CMS-Teil. Seit dem 20.11.2026 umfasst der neue Magazin-Standard zusätzlich die **Produktionsakte und Signalregisterzeile** nach wiki-production-records.md. Deren bestätigtes Speichern und vollständiges Rücklesen ist für den Gesamterfolg separat erforderlich. Ein reiner Seitenupdate-Auftrag startet keine rückwirkende Vollarchivierung; ein Wiki-Fehler verwirft keine bestätigten CMS-Ergebnisse.
