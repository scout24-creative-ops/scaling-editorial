# Einrichtung und Abgleich: nachgewiesener Stand

Stand: **19.11.2026**, Einrichtung von scaling-editorial-publisher. Diese Referenz dokumentiert Beobachtungen, keine Schreibberechtigung oder pauschale Produktionsfreigabe. Lies die aktuelle lokale Regelbasis dieses Publishers weiterhin vor jedem Einbau; der Snapshot ersetzt keine frischen Zielprüfungen.

## Abhängigkeiten und Werkzeugumfang

- Bei der ursprünglichen Einrichtung wurde die damalige persönliche Basis tatsächlich gelesen, einschließlich Ausführungsmodi, Editorial Policy, Portal UX, Portal-Konfiguration und Contentful-Integration. Die vollständigen kanonischen Blöcke für die aktuelle Navigation, Homepage, Kategorie- und Artikelseite wurden mit den beobachteten Strukturen verglichen.
- Die nativen Schemata der **Contentful Landing Page Builder MCP**-App wurden geprüft. Get, Create und Update unterstützen ausdrücklich `site: www | magazine`. Der aktuelle Adapter ist nicht die ältere Dev-Verbindung.
- **Tatsächlich ausgeführt wurden ausschließlich fünf `get_lp_builder_page`-Aufrufe**, alle mit expliziter Site. Es gab keinen Create-, Update-, Publish-, Upload-, Lifecycle- oder Wiki-Aufruf.
- Die vollständigen zurückgegebenen HTML-Inhalte wurden strukturell ausgewertet. Ihre UTF-8-Längen und SHA-256-Werte stimmten mit den vom CMS gelieferten Integritätswerten überein. Das belegt vollständige Lektüre/Übertragung dieser Versionen, keine Browserdarstellung, fachliche Prüfung oder Schreibfähigkeit.

## Vollständig gelesene Ziele

| Bereich | Entry-ID | Interner Slug | Gelesene Version | Ergebnis |
| --- | --- | --- | --- | --- |
| Magazin-Homepage | `1Nj4sEg7f95YuRHmpSbhz8` | `/magazine` | 10 | `site: magazine`, Titel `Scaling Editorial – News · MVP` bestätigt |
| Magazin Immobilienmarkt | `3iunhYCyqp2HfThOOCkjHM` | `/magazine/immobilienmarkt` | 1 | `site: magazine`, Titel `Immobilienmarkt` bestätigt |
| Magazin Lifestyle | `1KaqeGkaLE7rYJT06IP2fp` | `/magazine/lifestyle` | 1 | `site: magazine`, Titel `Lifestyle` bestätigt |
| Bestehender Magazin-Artikel als Strukturreferenz | `70nMd8ePoYCFrDQIkcljfE` | `/magazine/wohngeldreform-2027-geplante-aenderungen` | 1 | `site: magazine`; vorhandener Artikel, kein Standardziel für neue Packages |
| Getrennte bisherige Portal-Homepage | `5zLuKbEgpZyVu1BFJMc2DG` | `/dev-scaling-editorial-news-mvp` | 8 | `site: www`; keine Migration oder automatische Zielumleitung |

Alle fünf Antworten enthielten `publishedVersion: null`. Berichte dies nur für diese damaligen Versionen, nicht als aktuellen Status beliebiger späterer Ziele. Die vorhandene Magazin-Artikelreferenz ist kein neu erstellter Testartikel und darf nicht automatisch überschrieben werden.

## Bestätigter struktureller Teilabgleich

Die fünf gelesenen Seiten verwenden jeweils genau eine `lpb-explicit-spacing lpb-editorial-ux-root`, die aktuelle Drei-Punkte-Navigation und die erwartete zweite Home-/Kategorie-/Artikelkomposition. Auf die Navigation folgt ein direkter `lpb-spacer--l`, am Seitenende ein direkter `lpb-spacer--4xl`. Je Seite wurde eine H1 gefunden. Magazin und www hatten getrennte, zu ihren Bereichen passende Navigationsziele.

Die aktuelle Magazin-Artikelreferenz verwendet die kanonische Artikelseite, genau einen Introblock nach der Titelbild-Figur, den deaktivierten Google-Button einmal und den vorhandenen Autorenblock. Keine globale Script-Einbindung war im gespeicherten HTML enthalten. Dies bestätigt den gelesenen Strukturstand; Bilder, CSS/Runtime, mobile Darstellung und veröffentlichte Browserrouten wurden nicht visuell getestet.

## Festgestellte Abweichungen und Umgang damit

1. **Homepage-Bestand:** Sowohl die gelesene Magazin- als auch die www-Startseite enthielten vier kompakte Empfehlungen statt der im aktuellen UX-Vertrag vorgesehenen höchstens drei. Außerdem waren zwei reale Artikelziele über mehrere Kartenbereiche doppelt vorhanden. Diese Seiten wurden nicht korrigiert. Vor einem beauftragten Home-Einbau den konkreten Konflikt zwischen Layoutvorgabe und Erhalt des bestehenden Inhalts gezielt lösen; nicht stillschweigend Artikel verwerfen, eine vierte Position als neue Standardfähigkeit übernehmen oder die ganze Seite durch ein Demo-Template ersetzen.
2. **Autorenstand:** Der Einrichtungssnapshot enthielt einen bestehenden echten Autorenblock, während die Basis damals nur alte Testprofile aufführte. Die zentrale Autorenliste wurde anschließend am 19.11.2026 lesend mit dem veröffentlichten Autorenregister abgeglichen und um Inga Ervig / Julia Walter ergänzt. Nutze ausschließlich deren bestätigte Auswahl und zentrale Stammdaten; die alte Entwurfs-Ausnahme für fehlende Autoren gilt in diesem Publisher nicht mehr. Bestehende andere Artikel werden dadurch nicht automatisch umgestellt.
3. **Quellenlinks im Bestand:** Die gelesene Artikelreferenz enthielt externe Quellenlinks ohne das inzwischen in der Basis vorgeschriebene `nofollow`. Keine Bestandskorrektur wurde ausgeführt. Für neue Artikel beziehungsweise ausdrücklich beauftragte Quellenänderungen gilt die aktuelle Basis; kein pauschaler Sweep über alte Artikel.
4. **Vorschau-URLs:** Die fünf Get-Antworten lieferten Entry-ID, Site und internen Slug, aber **keinen expliziten Vorschau-Link**. Die im Nutzervertrag bekannte Magazin-Homepage-Vorschau ist eine zuvor übergebene Referenz und kein in diesem Lesetest frisch zurückgegebener Link. Erfinde bei einem späteren Ergebnis keinen Vorschau-Link aus diesem Host und einem Slug; verwende nur tatsächlich beim jeweiligen Ablauf vom CMS gelieferte Links oder melde den fehlenden Link.

Der ursprünglich offene Portal-/Magazinabgleich ist damit **lesend und für diese Strukturen teilweise belegt**, nicht als vollständige Produktionsabnahme abgeschlossen. Vor dem ersten echten Einbau müssen die für den konkreten Auftrag benötigten aktuellen Seiten, Komponenten und Abweichungen abgeglichen und validiert sein. Ein ungelöstes Home-Problem autorisiert weder eine Home-Korrektur noch blockiert es automatisch einen davon unabhängigen, vollständig abgeglichenen Artikelentwurf. Stoppe nur abhängige Schritte.

## Erste Tests und weitere Aufträge

Der erste Einrichtungstest dieser Skill-Fassung wurde ausschließlich lesend durchgeführt. Jede später ausdrücklich als Einrichtungs-/Zugriffsprüfung beauftragte Aufgabe bleibt ebenfalls ausschließlich lesend. Ein anderer Nutzer oder eine andere Verbindung muss seinen tatsächlichen Zugriff im eigenen Kontext verifizieren; der Snapshot beweist keine Rechte anderer Konten.

Create und Update sind **im Schema konfiguriert**, in dieser Einrichtung aber **nicht schreibend getestet**. Vorherige vom Nutzer berichtete Tests sind historische Nachweise mit ihrem eigenen Scope, keine neuen erfolgreichen Schreibaufrufe. Ein ausdrücklicher späterer Einbauauftrag darf nach erfolgreichem konkretem Abgleich und allen normalen Preflight-Prüfungen den Entwurf speichern; verlange keine zusätzliche erfundene Freigabe. Veröffentlichung und alle anderen gesperrten Aktionen bleiben außerhalb dieses MVP.

## Nachfolgend bestätigter Nutzer-Test und neue Einbauregeln

Dominik hat nach der Einrichtung berichtet, dass der Skill den Artikel erfolgreich im Magazin eingebaut hat. Der Bericht enthält hier keine neue Entry-ID oder Read-back-Daten; er ersetzt keinen eigenen Schreibtest dieser Aktualisierung. Anschließend hat Dominik verbindliche persönliche Autorinnenwahl (Inga oder Julia), eine vorab erfragte gehostete Bild-URL und **News- plus Rubrikteaser bei jeder Neuanlage** beauftragt. Diese Regeln stehen in required-inputs-and-placement.md und gehen den alten optionalen Platzierungsvorgaben und automatischen offenen Entwurfszuständen vor.

Die damaligen Homepage-Abweichungen sind historische Befunde, keine Aufforderung zu einer gesonderten Freigabeschleife: Beim jetzt beauftragten Teasereinbau vorhandene eindeutige Artikel durch kanonisches Umordnen erhalten, doppelte Darstellungen deduplizieren und überzählige kompakte Karten in den bestehenden unteren Gridbereich übernehmen. Keine Artikel löschen oder fremde Seiten ändern.

## Zusammenführung vom 19.11.2026

Komponentenbibliothek, Portal-Konfiguration, Quellenprovenienz, Building Policy, aktuelle Portal-UX, Ausführungsmodi und Contentful-Integration wurden vollständig in diesen Publisher übernommen. Die lokalen Referenzen sind jetzt die operative Regelbasis. Ein separater SE-LP-Builder-Skill ist nicht mehr erforderlich. Die nachfolgenden strengeren Vorgaben (persönliche Inga-/Julia-Auswahl, Bild-URL, beide Teaser, nur Entwürfe, nur Get/Create/Update) gelten in allen lokalen Referenzen. Die Zusammenführung selbst ist kein neuer CMS-Schreibtest oder eine visuelle Abnahme.

## Wiki-Erweiterung vom 20.11.2026

Dominik hat die integrierte Produktionsakte mit vollständigen ausgewählten TF-/SC-/Writer-Packages und den Signalregistereintrag als Teil des Magazin-Einbaus beauftragt. Die neue Referenz wiki-production-records.md ersetzt die bisherige pauschale Wiki-Write-Sperre ausschließlich für diese Ziele und den beschriebenen Workflow. Der CMS-Werkzeugumfang, die Autorinnen-/Bildauswahl und der Entwurfsstatus bleiben unverändert.

Lesend wurden die kanonischen Wiki-Seiten Signalregister und Produktionsakten samt Routing-IDs, Vergaberegeln und eine bestehende Beispielakte geprüft. Der tatsächliche Space product-intelligence wurde in list_writable_spaces mit Editor-Recht für das hier ausführende Konto gefunden. Das beweist keine Rechte anderer Kolleginnen und keinen erfolgreichen Wiki-Write. Die Elternseite bleibt unverändert; das Signalregister ist der einzige laufende Index. Bei dieser Einrichtung wurden keine Wiki- oder CMS-Inhalte erstellt, geändert oder veröffentlicht. Ein vollständiger Live-Test der neuen kombinierten Speicherfolge steht noch aus.

## Freigegebener Artikeldetailstandard vom 20.11.2026

Dominik hat zunächst an der Magazin-Weeknd-Seite den Introtext unter der Autorin und vor dem Titelbild, die Schrift 20/30 px bei unveränderter Textfarbe sowie das Entfernen des Google-Buttons geprüft und freigegeben. Anschließend wurden dort die unteren Module Markt in 60 Sekunden und SuchenPlus entfernt; der unveränderte direkte 4xl-Schlussabstand wurde im Browser mit 80 px gemessen. Danach hat Dominik diesen Aufbau für die übrigen Magazin-Artikelseiten und als Standard für neue Artikel beauftragt. Dieser aktuelle Stand ersetzt die ältere Intro-nach-Bild-/Google-/Demo-Endmodule-Beschreibung dieses Einrichtungssnapshots für reguläre Artikeldetailseiten.

Über Magazin-Homepage, beide Rubrikübersichten und die verifizierten Artikelverweise wurden acht aktuelle Magazinartikel identifiziert: Wohngeldreform, Energiewende, Heizöl, Ingolstadt, Baugenehmigungen, The Weeknd, Hape Kerkeling und eNoVA. Die sieben noch abweichenden Artikel wurden als Entwürfe aktualisiert und vollständig zurückgelesen; Weeknd entsprach bereits dem Standard. HTML-Inhalt, Identität, Metadaten und Integritätswerte wurden verglichen. Artikelkörper, Bild samt Caption, Autorenblock, Quellen, rechte Sidebar, Navigation und 4xl-Schlussabstand blieben erhalten. Die aktuellen Übersichten wurden nicht verändert. Zwei nur aus dem alten www-Register bekannte Pfade (Generationenwechsel und WG-Mieten) waren mit explizitem site magazine nicht vorhanden und wurden weder angelegt noch auf www geändert. Die Anbindung bietet keine globale Artikelauflistung; diese Bestandsaussage gilt für die ermittelten Magazinziele, nicht für unbekannte unverlinkte Einträge.

Die lokale kanonische Vorlage scaling-editorial-article-page und die aktuellen Layout-/Typografieregeln wurden auf den freigegebenen Aufbau umgestellt. Andere Page Modules sowie die separaten Embedded-Component-Blöcke bleiben erhalten; ihre Existenz autorisiert kein automatisches Wiedereinfügen der drei ausgeschlossenen Elemente auf neuen Artikelseiten. Der einzige neue Inline-Stil ist die ausdrücklich freigegebene Typografie des vorhandenen Introabsatzes; kein globales CSS oder Frontend wurde verändert. Diese Layoutumstellung ist keine Veröffentlichung und kein neuer Wiki-Speichertest.

Nach dem Rollout wurden Wohngeldreform und eNoVA zusätzlich im Browser geprüft: Intro nach dem vollständigen Metadatenblock und vor der Bildfigur, berechnet 20 px / 30 px in unverändertem Charcoal, keine der drei entfernten Komponenten und ein 80-px-Schlussspacer. Diese Desktop-Stichproben sind keine neue visuelle Abnahme sämtlicher Artikel oder eine separate Mobilprüfung.

## News-Leadkorrektur vom 20.11.2026

Auf Dominiks Auftrag wurde ausschließlich die Magazin-News-Übersicht angepasst (Entry 1Nj4sEg7f95YuRHmpSbhz8): Das große Leadbild wechselte von 16:7 auf 16:9 über den eng begrenzten Bildstil aspect-ratio:16/9!important. Der verifizierte vorhandene eNoVA-Artikel wurde als fünfter kompakter Teaser mit tatsächlichem Bild, Titel, Byline und Datum ergänzt. Bestehende vier rechte Teaser und alle übrigen Seiteninhalte blieben erhalten; die Rubrikseiten Immobilienmarkt und Lifestyle wurden nicht geändert. Version 13 wurde gespeichert und vollständig zurückgelesen. Im Browser: Leadbild 680 × 382,5 px (16:9), fünf unterschiedliche rechte Artikelziele bestätigt. Das ist ein News-Layoutnachweis, keine Veröffentlichung oder Mobilabnahme. Die aktuelle News-Regel ist daher 16:9 und bis zu fünf verifizierte kompakte Teaser; die frühere Drei-Teaser-Grenze dieses historischen Einrichtungssnapshots ist für News überholt. Artikel-Weiterlesen bleibt dagegen bei höchstens drei Einträgen.

## News-Auswahllogik und Platzhalterkorrektur vom 20.11.2026

Dominik hat anschließend die aktuelle gemischte obere Auswahl und zwei untere Rubrikreihen beauftragt. Maßgeblich ist news-selection.md: explizit redaktionell festgelegter Hauptartikel oder neuester geeigneter Artikel, weitere aktuelle Artikel rechts, übrige Artikel getrennt in Immobilienmarkt aktuell und Lifestyle aktuell, jede echte Identität genau einmal. Sortiergrundlage sind explizite redaktionelle Datumswerte, keine Klickdaten und keine CMS-Zeitstempel. Bei geringem Bestand kann pro Rubrik ein echter Artikel unten verbleiben. Die eigenständigen Rubrikseiten bleiben unverändert.

Die zunächst zu knapp umgesetzten unteren Reihen wurden auf Dominiks Klarstellung korrigiert: **Vorgesehene freie Teaserplätze bleiben als graue Bilder mit Blindtext sichtbar.** News-Version 15 wurde gespeichert und vollständig zurückgelesen: eNoVA als neuester Hauptartikel, fünf weitere echte Artikel rechts, je ein echter Artikel und drei unverbundene graue Layout-Platzhalter pro unterer Viererreihe. Die sechs Platzhalter haben keine Autoren, Daten, Entry-IDs oder Links und zählen nicht zum Bestand von acht echten Artikeln. Andere Zusatzmodule wurden erhalten. Die lokalen News-Vorlagen und Auswahlregeln wurden entsprechend abgeglichen; ihre Platzhalter dürfen nicht als echte Artikel archiviert oder gerankt werden. Das ist keine Veröffentlichung oder neue Wiki-Ablage.

## Autoren-Overlay – Entwicklung vom 20.11.2026

Neue optionale Komponente und zentrale Technik sind vorbereitet, nicht ausgerollt. Die 16 bestehenden Runtime-Regressionstests bestehen. Acht neue Browserprüfungen sind geschrieben, aber wegen blockiertem Chromium-Start nicht ausgeführt; die isolierte geschützte Site-Vorschau verlangt im Prüf-Browser eine Anmeldung. Es gibt damit noch keinen Interaktions-, mobilen Sicht- oder aktuellen CMS-Sanitizer-Nachweis. Die Kurzvorstellungen beider Autorinnen sind offen; der Mustertext ist ausdrücklich keine Biografie. Kein Contentful-Write und keine Änderung der gemeinsam ausgelieferten Runtime. Für alle weiteren Schritte gilt author-dialog.md; gewöhnliche Publisher-Aufträge bleiben beim bestehenden Autorenstandard.

## eNoVA-Autoren-Overlay: freigegebener Einzeltest vom 20.11.2026

Nach ausdrücklicher Freigabe wurden ausschließlich die beiden zentralen Contentful-CSS-/JS-Dateien um die opt-in Autorenkomponente ergänzt und ihre tatsächlich ausgelieferten Bytes geprüft. Nur eNoVA (Entry 3y9fa8c47UrnHmI0vfHgHL, site magazine, /magazine/immobilienkauf-digital-enova) wurde von Version 2 auf Entwurfsversion 3 aktualisiert. Vollständiger Read-back und Integritätswerte stimmen; nur der Autorenblock änderte sich. Name/Portrait/Rolle, Datum, Lesezeit und übriger Artikel bleiben erhalten. Die Kurzvorstellung ist ausdrücklich ein Funktionstest-Platzhalter. Im Desktop-Browser wurden Namensklick, Enter/Leertaste, Button-/Escape-/Hintergrund-Schließen und Fokus-Rückgabe auf der echten Magazinseite geprüft; das sichtbare Overlay wurde dokumentiert. Ein frischer Aufruf war nötig, weil der schon geöffnete Tab noch den alten Asset-Stand verwendete. Keine weitere Magazinseite, keine Übersicht und kein gemeinsames Frontend wurden umgestellt. Kein Publish und keine mobile/Safari-Abnahme. Die aktuelle author-dialog.md ersetzt die ältere Aussage „nicht ausgeliefert“ für diesen Einzeltest, nicht die Regeln für neue oder andere Artikel.
