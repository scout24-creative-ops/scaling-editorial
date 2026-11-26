import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

EXPORTER = (Path(__file__).resolve().parents[1] / 'skills' /
            'scaling-editorial-article-writer' / 'scripts' / 'write_package.py')
SOURCE = 'https://example.org/report'


def package(words):
    sections = {
        'Headline': 'Wie sich der Markt verändert',
        'Headline-Alternativen': '- Variante eins\n- Variante zwei',
        'Introtext': ' '.join(['Einordnung'] * 20),
        'SEO': 'Einordnung der jüngsten Zahlen',
        'Artikel': '### Kontext\n\n' + ' '.join(['Zusammenhang'] * (words - 20)),
        'Quellen': SOURCE,
        'Interne Linkvorschläge': 'Keine verifizierten internen Linkziele übergeben.',
        'Titelbild': 'Reiner Textexport; kein Bild erstellt.',
    }
    return {
        'kind': 'article',
        'topic': 'Test zur flexiblen Länge',
        'metadata': [
            {'label': key, 'value': 'Testwert'} for key in
            ('Auftrag', 'Rubrik', 'Themen-Tags', 'Platzierung', 'Slug-Vorschlag',
             'Autor', 'Rolle', 'Veröffentlichungsdatum', 'Status', 'Bild-URL')
        ],
        'sections': [{'heading': key, 'body': value} for key, value in sections.items()],
        'source_urls': [SOURCE],
    }


class ArticlePackageLengthTests(unittest.TestCase):
    def run_export(self, data, folder):
        source = folder / 'input.json'
        source.write_text(json.dumps(data), encoding='utf-8')
        return subprocess.run(
            [sys.executable, str(EXPORTER), '--input', str(source),
             '--output-dir', str(folder / 'output')],
            text=True, capture_output=True, check=False,
        )

    def test_length_is_reported_not_enforced(self):
        for words in (250, 499, 500, 620, 721):
            with self.subTest(words=words), tempfile.TemporaryDirectory() as temp:
                data = package(words)
                result = self.run_export(data, Path(temp))
                self.assertEqual(result.returncode, 0, result.stderr)
                exported = json.loads(result.stdout)
                self.assertEqual(exported['articleWords'], words)
                body = Path(exported['path']).read_text(encoding='utf-8')
                self.assertIn(data['sections'][4]['body'], body)

    def test_invalid_source_still_blocks_export(self):
        with tempfile.TemporaryDirectory() as temp:
            data = package(620)
            data['source_urls'] = ['https://example.org/other-report']
            result = self.run_export(data, Path(temp))
            self.assertEqual(result.returncode, 2)
            self.assertIn('Source URL must be fully visible', result.stderr)
            self.assertFalse((Path(temp) / 'output').exists())


if __name__ == '__main__':
    unittest.main()
