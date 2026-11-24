# Technische Artikelprüfung

Prüfe neue und ausdrücklich vollständig überarbeitete Artikelseiten vor dem CMS-Write und nach dem vollständigen Rücklesen mit `scripts/check_article_html.py`. Der Helfer ergänzt Quellen- und Bildrollenprüfung; er ersetzt sie nicht. Er gilt für die kanonische UX-Artikelseite, nicht für Home-/Rubrikübersichten oder beliebige Legacy-Module.

## Eingabe vorbereiten

- Genau eine H1 im inneren `lpb-editorial-article`, vor den übrigen Artikelüberschriften. Kapitel beginnen mit H2; weitere Ebenen ohne Sprung verschachteln. Die separate Überschrift im kanonischen Autoren-Dialog gehört nicht zur Artikelhierarchie; dessen Bilder werden weiterhin geprüft. Überschriften nicht erfinden, um eine Prüfung zu erfüllen.
- Im vollständigen `lpb-editorial-ux--article` erhalten alle Bilder positive ganzzahlige `width`-/`height`-Attribute und ein `alt`-Attribut. Die vorhandenen rollenabhängigen Abmessungen bleiben bestehen; HTML-Abmessungen belegen keine tatsächlichen Dateipixel.
- Verwende für Titelbild und informative Bilder im Artikelkörper aussagekräftige übergebene Alttexte. Fehlenden Kontext gezielt klären, keine Bildbeschreibung erfinden. Leeres `alt` bei redundanten/dekorativen Sidebar-Bildern ist zulässig. Für ein ausdrücklich bestätigtes dekoratives Bild im Artikelkörper darf seine exakte bestehende URL mit `--decorative-image-src` übergeben werden; diese Ausnahme gilt nie für das Titelbild. Keine neuen HTML-Attribute zur Umgehung einführen.
- Das Titelbild in der bestehenden Artikel-Bildfigur erhält `loading="eager" fetchpriority="high"`. Alle anderen Bilder der aktuellen Artikelkomposition bleiben `loading="lazy"`. Priorisiere nicht sämtliche Bilder. Keine Head-Preloads, neuen Bildquellen, Layout-/CSS- oder Frontend-Änderungen daraus ableiten.

## Aufruf und Rücklesen

Vorprüfung:

```bash
python3 scripts/check_article_html.py --html /absolute/path/prepared-article.html
```

Rücklesen (die vorgeprüfte Eingabe unverändert erhalten):

```bash
python3 scripts/check_article_html.py --html /absolute/path/readback-article.html --expected-html /absolute/path/prepared-article.html
```

Bei einem Fehler vor dem Write nur die beauftragten technisch korrigierbaren Teile berichtigen und erneut prüfen. Fehlende redaktionelle Angaben klären. Bei gespeichertem Teilstand bestätigte IDs erhalten, abhängige Platzierungen stoppen und die konkrete Lücke melden. Ein CLI-Exitcode 0 bedeutet nur, dass diese lokalen Prüfungen bestanden sind.

## Enge Bestandskorrekturen

Eine reine Text-/Linkkorrektur oder andere enge Bestandsänderung autorisiert keine Nachrüstung aller früheren Artikel. Als `--baseline-html` ausschließlich den vollständig und unmittelbar vor der Änderung gelesenen Originalstand desselben Eintrags verwenden. Die vorbereitete Fassung darf nie als ihre eigene Baseline dienen. Dieselbe Originaldatei auch beim Rücklesen angeben:

```bash
python3 scripts/check_article_html.py --html /absolute/path/prepared-article.html --baseline-html /absolute/path/original-article.html
python3 scripts/check_article_html.py --html /absolute/path/readback-article.html --baseline-html /absolute/path/original-article.html --expected-html /absolute/path/prepared-article.html
```

Unveränderte bestehende Einzelbefunde erscheinen dann als `warnings`; neue oder geänderte Fehler bleiben `errors`. Die Warnungen ausdrücklich nennen, nicht als behoben oder vollständig SEO-konform melden. Fehlende/mehrdeutige Artikelwurzeln und Titelbilder bleiben Fehler. Bei alten anderen Layouts den Helfer nicht durch einen Umbau erzwingen; die beauftragten Änderungen separat prüfen und die fehlende Anwendbarkeit berichten. Keine Baseline-Ausnahme bei Neuanlagen oder vollständiger Überarbeitung.

## Aussagegrenzen

Der Helfer liest nur lokale HTML-Dateien und verändert nichts. Er prüft Überschriftenfolge, nicht leere redaktionelle Alttexte, deklarierte Bildabmessungen, Ladeattribute und deren Erhalt beim Rücklesen. Ob eine Bildbeschreibung inhaltlich stimmt, bleibt menschlich beziehungsweise anhand des bestätigten Bildkontexts zu prüfen. Kein Nachweis für echte Dateimaße, Hosting, Dateigröße, Bildqualität, Browserdarstellung, LCP, Veröffentlichung, Metatags, strukturierte Daten oder Indexierung. Kein zusätzliches Seitenlayout, keine neuen Artikelregeln und keine Veröffentlichung sind damit beauftragt.
