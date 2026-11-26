"""Focused behavioral checks for article length and source-link validation."""
from copy import deepcopy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / 'skills'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


writer = load('writer', 'scaling-editorial-article-writer/scripts/write_package.py')
publisher = load('publisher', 'scaling-editorial-publisher/scripts/check_source_links.py')


def package(words):
    spec = writer.CONTRACTS['article']
    bodies = {heading: 'Inhalt' for heading in spec['sections']}
    bodies.update({'Headline-Alternativen': '- Alternative eins\n- Alternative zwei',
                   'Introtext': 'Einleitung', 'Artikel': ' '.join(['Wort'] * (words - 1))})
    return {'kind': 'article', 'topic': 'Test', 'source_urls': [],
            'metadata': [{'label': label, 'value': 'Wert'} for label in spec['metadata']],
            'sections': [{'heading': heading, 'body': bodies[heading]}
                         for heading in spec['sections']]}


def sources(*anchors):
    return '<ul class="lpb-editorial-article__sources-list">' + ''.join(
        '<li>' + anchor + '</li>' for anchor in anchors) + '</ul>'


class ArticleLength(unittest.TestCase):
    def test_word_count_has_no_cutoff(self):
        for words in (499, 500, 820):
            with self.subTest(words=words):
                data = package(words)
                self.assertEqual(writer.article_word_count(data['sections']), words)
                writer.render(data)

    def test_explicit_length_is_optional_metadata(self):
        data = package(820)
        self.assertNotIn('Längenvorgabe', writer.render(data)[2])
        data['metadata'].append({'label': 'Längenvorgabe', 'value': 'Nutzer: Bitte etwa 820 Wörter.'})
        self.assertIn('Längenvorgabe', writer.render(data)[2])

    def test_no_minimum_length(self):
        writer.render(package(2))

    def test_only_intro_and_article_count(self):
        data = package(499)
        for section in data['sections']:
            if section['heading'] in ('Quellen', 'Titelbild', 'SEO'):
                section['body'] = ' '.join(['Zusatz'] * 200)
        self.assertEqual(writer.article_word_count(data['sections']), 499)

    def test_headings_urls_and_captions_excluded(self):
        text = ('### Sehr lange Überschrift\n'
                'Ein [guter Link](https://example.org/a_(b)) hilft.\n'
                '<h3>Weitere lange Überschrift</h3>'
                '<p>Homeoffice-Platz kostet 1.250 Euro.</p>'
                '<figure><img alt="Bild mit vielen Wörtern" src="x">'
                '<figcaption>Diese Bildunterschrift zählt nicht mit.</figcaption></figure>')
        self.assertEqual(writer.word_count(text), 8)


class SourceLinkChecks(unittest.TestCase):
    def test_external_requires_nofollow(self):
        bad = sources('<a href="https://example.org/a" rel="noopener noreferrer">Quelle</a>')
        self.assertFalse(publisher.check(bad)['ok'])
        good = bad.replace('noopener', 'nofollow noopener')
        self.assertTrue(publisher.check(good, good)['ok'])

    def test_real_is24_hosts_remain_followed(self):
        html = sources('<a href="https://www.immobilienscout24.de/a">A</a>',
                       '<a href="https://immobilienscout24.de/b">B</a>')
        result = publisher.check(html)
        self.assertTrue(result['ok'])
        self.assertEqual(result['externalSources'], 0)

    def test_similar_domain_is_external(self):
        html = sources('<a href="https://immobilienscout24.de.evil.example/a">A</a>')
        self.assertFalse(publisher.check(html)['ok'])

    def test_readback_lost_token_or_changed_target_fails(self):
        before = sources('<a href="https://example.org/a?x=1&amp;y=2" rel="nofollow noopener noreferrer">A</a>')
        self.assertTrue(publisher.check(before, before)['ok'])
        self.assertFalse(publisher.check(before.replace(' noreferrer', ''), before)['ok'])
        self.assertFalse(publisher.check(before.replace('/a?', '/b?'), before)['ok'])

    def test_author_and_sidebar_links_outside_source_list_untouched(self):
        outside = '<a href="https://linkedin.com/x">Autorin</a>'
        html = outside + sources('<a href="https://example.org/a" rel="nofollow">A</a>') + outside
        result = publisher.check(html)
        self.assertTrue(result['ok'])
        self.assertEqual(result['sources'], 1)

    def test_missing_source_list_or_unsafe_url_does_not_pass(self):
        for html in ('<p>Kein Artikel</p>', sources('<a href="javascript:bad()">A</a>'),
                     sources('<a href="https://bad host/a" rel="nofollow">A</a>')):
            with self.subTest(html=html):
                self.assertFalse(publisher.check(html)['ok'])

    def test_failed_preflight_cannot_verify_saved_version(self):
        before = sources('<a href="https://example.org/a">A</a>')
        after = before.replace('href=', 'rel="nofollow" href=')
        self.assertFalse(publisher.check(after, before)['ok'])


if __name__ == '__main__':
    unittest.main()
