# Signalübersicht im Chat

Diese Darstellung wurde auf Dominiks Wunsch nach dem Test vom 19.11.2026 erweitert. Sie verändert die kompakte Chatübersicht; jedes herunterladbare Signal Package bleibt vollständig und eigenständig nach signal-package.md. Recherche- und Evidenzstandards bleiben unverändert.

## Aufbau

Beginne mit höchstens zwei kurzen Sätzen zu Zahl der tatsächlich qualifizierten Signale, Recherchestand und tatsächlich erfolgtem beziehungsweise eingeschränktem Wiki-/Historienabgleich. Danach folgt **eine nummerierte Liste**, vom aussichtsreichsten zum nachgeordneten ausgewählten Signal. Erfinde keinen Live-Abgleich, keine Quellenprüfung und keine Aktualisierung.

Jeder Listeneintrag enthält in dieser Reihenfolge:

1. Eine **fette neutrale Themenbezeichnung** mit kurzer qualitativer Ampel samt Klartext direkt daneben, etwa `🟢 Stark` oder `🟡 Mit Vorbehalt`. Die Nummer ist die Reihenfolge, keine Punktzahl. Formuliere keine finale Artikelheadline.
2. **Drei bis vier kurze Sätze**, insgesamt normalerweise etwa 50–90 Wörter. Erkläre verständlich, was konkret beobachtet wurde beziehungsweise neu ist, welcher Anlass oder Zeitraum relevant ist, wen das betrifft und warum daraus ein interessantes Signal entstehen kann. Nenne bei Bedarf die wichtigste Einschränkung oder das noch offene Potenzial. Ein Leser muss das Signal grob einordnen können, ohne zuerst die Datei zu öffnen. Keine bloßen Schlagwörter, selbstreferenzierten Werbesätze oder ausgedachten Fakten zur Verlängerung. Bei einem einfachen Signal darf der Text kürzer sein, wenn diese Fragen trotzdem beantwortet sind.
3. **Direkt darunter der Download dieses einen Signal Package**, als eigener eingerückter Absatz innerhalb desselben Listeneintrags. Beschrifte ihn eindeutig, zum Beispiel „Signal Package – [neutrales Kurzthema] herunterladen“, und verwende den tatsächlich verfügbaren Datei-Link.

Nutze CommonMark-konforme Absatzabstände und Einrückung, damit Text und Link innerhalb desselben nummerierten Punkts bleiben. Setze **zwischen zwei Signalen nach dem Download-Link eine dezente horizontale Markdown-Trennlinie** mit jeweils einer Leerzeile davor und danach. Rücke die Zeile `---` genau wie den Download-Absatz in den bisherigen Listenpunkt ein (bei `1.` bis `5.` mit drei Leerzeichen); beginne erst danach den nächsten nummerierten Punkt auf Listenebene. Die Leerzeile vor `---` ist erforderlich, damit der Link nicht versehentlich als Setext-Überschrift formatiert wird. Nach dem letzten Signal keine zusätzliche Trennlinie setzen. So bleiben Nummerierung und Download-Zuordnung erhalten, während die Oberfläche einen eigenen Trennblock zwischen den Signalen rendern kann.

Der genaue Pixelabstand und die Darstellung der Linie liegen bei der Chat-Oberfläche. Versprich keine feste Abstandshöhe; mehrere bloße Leerzeilen können zusammenfallen. Verwende keine HTML-/CSS-Abstände, `<br>`-Ketten oder unsichtbaren Füllzeichen. Gib keine zweite Liste der Packages am Antwortende aus und hänge keine getrennte Gesamtpriorisierung an. Die Listenreihenfolge und die Einordnung je Punkt erfüllen bereits diese Funktion.

Nutze ausdrücklich platzierte Markdown-Download-Links im jeweiligen Punkt. Falls die Oberfläche zusätzlich automatisch Dateikarten gruppiert, erfinde keine Möglichkeit, deren Darstellung zu kontrollieren; der zugehörige direkte Link bleibt dennoch beim Signal. Erfinde weder Sandbox-Pfade, Datei-IDs noch Download-URLs. Wenn eine Datei nicht bereitgestellt werden konnte, nenne die konkrete Lücke an diesem Signal und behaupte keinen fertigen Download.

## Bedeutung der Ampel

Die Ampel ist eine **qualitative redaktionelle Einschätzung dieses Signals**, keine objektive Messung, Wahrscheinlichkeit, Prognose oder Freigabe für eine fertige Story. Nutze Textlabels zusätzlich zur Farbe, damit die Bedeutung auch ohne Farbwahrnehmung klar bleibt.

- **🟢 Stark:** Das ausgewählte Signal verbindet einen nachvollziehbaren aktuellen Anlass, deutliche Relevanz für die Zielgruppe, erkennbares journalistisches Potenzial und belastbare tragende Evidenz. Das bedeutet nicht, dass jeder denkbare Angle belegt oder eine spätere Story bereits freigegeben ist.
- **🟡 Mit Vorbehalt:** Das Signal erfüllt weiterhin den Auswahlstandard, hat aber eine wesentliche begrenzende Eigenschaft für die weitere Storyentwicklung, zum Beispiel engere Reichweite oder begrenzte Übertragbarkeit. Erkläre diese kurz in den einordnenden Sätzen. Eine ungeklärte tragende Behauptung wird nicht durch Gelb zulässig.
- **🔴 Nicht ausreichend:** Verwerfen, kein qualifiziertes Signal Package dafür erzeugen und nicht als zusätzlichen nummerierten Themenvorschlag liefern. Nur bei ausdrücklich beauftragtem Review abgelehnter Kandidaten diese Kategorie nennen.

Bewerte nach Leserrelevanz, Aktualität, Substanz, möglichem eigenständigen Mehrwert und tatsächlicher Evidenz. Erzwinge keine Farbverteilung: Wenn alle ausgewählten Signale stark sind, dürfen alle grün sein. Ein bloßer Wiki-/Historien-Zugriffsausfall ist transparent zu benennen und keine automatische fachliche Abwertung. Zentrale Evidenzlücken können weiterhin zur Ablehnung führen.

Verwende keine numerische 1–10-Bewertung, Prozentangaben, künstliche Gewichtungsformeln oder unbelegten Klick-/Reichweitenprognosen. Die qualitative Ampel erfüllt die gewünschte visuelle Orientierung ohne vorgetäuschte Messgenauigkeit. Liefere weiterhin höchstens fünf qualifizierte Signale, weniger oder null, wenn die Qualität es erfordert.

Die Ampel und die vergleichende Reihenfolge gehören in die Chatübersicht, nicht als neue technische Felder in das interne JSON oder in die Package-Dateien. Ändere dafür weder das Übergabeformat noch den Renderer. Notwendige Fakten, Quellen und Einschränkungen müssen trotzdem vollständig im jeweiligen Package stehen; die Chat-Einordnung ersetzt sie nicht.

## Sonderfälle

- Bei einem Signal genügt ein nummerierter Punkt mit Einordnung und eigenem Download.
- Bei null qualifizierten Signalen gib das transparente Null-Ergebnis aus, keine leeren Listeneinträge, roten Ersatzvorschläge oder fingierten Packages.
- Bei ausschließlich erneuter Formatierung einer schon vorliegenden Auswahl: Verwende nur deren tatsächliche Angaben und bekannte Datei-Links. Erfinde keine zusätzlichen Fakten, neuen Recherchezeitpunkte oder neue Wiki-Abfragen, um die Chatübersicht zu füllen. Reicht das Material für eine Ampel nicht aus, kennzeichne die Einschätzung als offen.
- Bei bloßer Dateiübertragung eines vorhandenen einzelnen Packages ist keine neue Ampelbewertung oder vollständige Themenrecherche nötig.
