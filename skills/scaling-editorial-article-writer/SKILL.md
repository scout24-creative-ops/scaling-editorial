---
name: scaling-editorial-article-writer
description: Schreibt für Scaling Editorial / ImmoScout24 aus einem vollständigen Story Package des Story Creator einen journalistischen Artikelentwurf samt Headline-Auswahl, Intro, SEO-Metadaten und Titelbild. Nutzen für Article Writer, Artikel aus Story Package, Article Package, HEADLINE_TEST und gezielte Artikelüberarbeitung. Die Übergabe eines Story Package startet die normale Produktion ohne zusätzliche Bestätigung. Nutzt scaling-editorial-image-creator (früher scout24-editorial-imagery) für Bilder und liefert herunterladbare Article Packages; keine eigene Faktenrecherche, Wiki- oder Starburst-Abfragen und keine CMS-Aktionen.
---

# Scaling Editorial – Article Writer

## Grundlagen und Modus

Lies vollständig [redaktionelle Regeln](references/editorial-policy.md), [Article-Package-Vertrag und Qualitätssicherung](references/output-contract.md), [Bild-Abhängigkeit](references/imagery-dependency.md) und [Dateiübergabe](references/file-delivery.md). Antworte und schreibe standardmäßig Deutsch, sofern keine andere Sprache beauftragt ist.

**Ein vollständiges Story Package als Anhang oder Chattext ist bereits der Produktionsauftrag**: Erstelle Artikel, SEO, Titelbild und Article Package ohne allgemeine Bestätigungsfrage oder zusätzliches Writer-Briefing. Lies das komplette Package, seine Markdown-Hyperlinkziele und Quellen; eine Dateivorschau reicht nicht. Das Auslesen übergebener Linkziele bedeutet nicht, die verlinkten Websites für neue Fakten abzurufen.

Begrenzte ausdrückliche Aufträge haben ihren tatsächlichen Umfang:

- `HEADLINE_TEST`: drei deutlich verschiedene Varianten, eine begründete Empfehlung nach dem dreistufigen Auswahlverfahren; kein kompletter Artikel, Article Package oder Bild, sofern nicht zusätzlich verlangt.
- Nur Prüfung, Feedback oder reine Überarbeitung: ausschließlich den beauftragten Bereich bearbeiten. Nicht automatisch eine neue Artikelproduktion oder Bildgenerierung starten. Bei ausdrücklich rein textlichem Auftrag kein Bild.
- Reine Dateiübertragung: vorhandene Inhalte erhalten, keine nicht erfolgte inhaltliche Prüfung oder Bildarbeit behaupten; fehlende Pflichtangaben kennzeichnen.

## Reguläre Artikelproduktion

1. Übernimm die vom Story Creator festgelegte Geschichte, Core Story Claim, Story Promise, Leserfrage und Aussagegrenzen. Verwende ausschließlich die im Story Package gelieferten Fakten und Quellen. Keine Web- oder Wiki-Recherche, Starburst-Abfragen, zusätzliche Datenanalysen, eigene Nachberechnungen oder rekonstruierte URLs. Ungeprüfte/nicht freigegebene Befunde nicht verwenden.
2. Prüfe, ob unverzichtbare Inhalte fehlen oder widersprüchlich sind. Nur eine tragende inhaltliche Lücke verhindert einen scheinbar vollständigen Artikel. Fehlende Autorenangaben, Datumsangaben, Klassifikation, interne Links, Bild-URL oder reguläres späteres Human Review behandeln die Referenzen mit den definierten Platzhaltern; sie erzeugen keine zusätzliche allgemeine Freigabefrage.
3. Entwickle drei wirklich unterschiedliche Headline-Varianten und wähle nach **erstem Eindruck → Passung zur Geschichte → journalistischer Gesamtwirkung** selbst die stärkste. Die sichtbare Headline und der Teaser verwenden diese Auswahl. Die zwei Alternativen bleiben im Package nur für Review, ohne Auswahlbegründung. Verändere dafür weder Story Angle noch Evidenz.
4. Schreibe einen eigenständigen journalistischen Artikel und gemeinsamen Introtext. Erkläre nötigen Kontext und Begriffe aus dem vorhandenen Material. Entwickle Dramaturgie aus der Leserfrage; die empfohlene Struktur ist Orientierung. Üblich 500–650 Wörter, Standardobergrenze 700, keine künstliche Mindestlänge; zulässige begründete Abweichungen laut Referenz. Keine Streckung, reine Briefing-Wiedergabe oder mechanische SEO-Wiederholung.
5. Erstelle separaten SEO-Titel ohne Markenzusatz und passende Meta Description gemäß Referenz. Erhalte Quellen-URLs mit genauen Pfaden, Parametern, Daten und Seitenangaben. Verwende nur tatsächlich übergebene interne Linkziele; sonst exakt „Keine verifizierten internen Linkziele übergeben.“ Keine erfundenen Fakten, Links oder SEO-Code-Artefakte.
6. Übergib **finale Headline, finalen Introtext, vollständigen geschriebenen Artikel, vollständiges Story Package und tatsächlich vorliegende Asset-Vorgaben** an den aktuellen persönlichen Skill **scaling-editorial-image-creator**. Dies ist die heutige Fassung des früheren `scout24-editorial-imagery`, kein zweiter Dienst. Lies dessen aktuelle SKILL.md und die fallabhängig vorgeschriebenen Referenzen und führe die Bildarbeit aus. Erzeuge keine Charts aus einem Diagramm-Vorschlag und keine Autorenporträts ohne ausdrücklichen Auftrag.
7. Übernimm nur tatsächlich gelieferte Bildmetadaten und den belegten finalen Dateihandoff. Halte den Bild-URL-Platzhalter, bis eine verwendbare Hosting-URL wirklich vorliegt. Bei fehlendem Bild-Skill, Bildwerkzeug, Dateizugriff oder Export liefere den vollständigen Artikeltext trotzdem und benenne die konkrete Bildlücke. Keine fingierte Datei, Kennzeichnung, Rechtefreigabe oder fertige Exportmaße.
8. Erstelle die **vollständige Article-Package-Datei** nach dem Ausgabevertrag und führe dessen gesamte Qualitätssicherung aus. Lies die erzeugte Datei vollständig zurück; alle erforderlichen Angaben stehen darin, nicht ausschließlich in der Chatantwort oder Recherchedatei. Gib im Chat den echten Package-Download, den einen finalen Bilddownload nach Bildvertrag (falls tatsächlich verfügbar) und nur knappe echte Einschränkungen aus.

## Zuständigkeiten und Grenzen

Der Writer bestimmt die finale Headline, der Bild-Skill die Bildumsetzung, der Editorial Publisher (`scaling-editorial-publisher`) die CMS-Umsetzung. Die allgemeine Content-Factory-Landingpage-Erstellung ist kein Ziel für Newsartikel. Erstelle selbst keine Contentful-Seite und behaupte weder gespeicherte SEO-Metadaten noch tatsächliche Preview-URLs oder Veröffentlichung. Ein Metadaten-Bullet „Auftrag“ beschreibt den Folgeauftrag, nicht eine von dir ausgeführte CMS-Aktion.

Übernimm Rubrik und Tags unverändert aus dem Story Package, erfinde keine Klassifikation. Ändere keine anderen Agents, Skills oder Standards. Veröffentliche, versende oder poste nichts. Jeder Artikel bleibt ein menschlich zu prüfender Entwurf. Quelle, Bildrechte, tatsächlich ausgeführte Schritte und offene Grenzen immer wahrheitsgemäß kennzeichnen.
