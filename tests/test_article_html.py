"""Check article guardrails and saved HTML without touching CMS or network."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/scaling-editorial-publisher/scripts/check_article_html.py'
spec = importlib.util.spec_from_file_location('article_html', SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


def article():
    return '''<div class="lpb-editorial-ux--article">
    <section class="lpb-editorial-article">
    <header><h1>Eine belegte Nachricht</h1></header>
    <img class="avatar" src="https://example.org/author.png" alt="Julia Walter" width="240" height="240" loading="lazy">
    <figure class="lpb-editorial-article__media"><div>
    <img src="https://example.org/title.webp" alt="Wohnhaus mit Garten" width="1920" height="1080" loading="eager" fetchpriority="high">
    </div></figure>
    <div class="lpb-editorial-article__body"><h2>Die Entwicklung</h2><p>Einordnung.</p>
    <h3><span>Ein Detail</span></h3><h2>Was folgt</h2></div>
    <aside><h2>Quellen</h2></aside></section>
    <aside><h2>Weiterlesen</h2><img src="https://example.org/related.webp" alt="" width="80" height="56" loading="lazy"></aside>
    </div>'''


class ArticleHTML(unittest.TestCase):
    def test_valid_and_unchanged_readback(self):
        result = guard.check(article(), expected_html=article())
        self.assertTrue(result['ok'], result)
        self.assertEqual(result['checkedHeadings'], 5)
        self.assertEqual(result['checkedImages'], 3)

    def test_one_h1_and_heading_order(self):
        for html in (article().replace('<h1>', '<h2>').replace('</h1>', '</h2>'),
                     article().replace('</header>', '<h1>Zweite</h1></header>'),
                     article().replace('<h2>Die Entwicklung</h2>', '<h3>Die Entwicklung</h3>')):
            self.assertFalse(guard.check(html)['ok'])

    def test_empty_and_hidden_headings_fail(self):
        for replacement in ('<h1> </h1>', '<h1 hidden>Unsichtbar</h1>',
                            '<h1 aria-hidden="true">Unsichtbar</h1>'):
            self.assertFalse(guard.check(article().replace('<h1>Eine belegte Nachricht</h1>', replacement))['ok'])

    def test_each_image_needs_positive_integer_dimensions(self):
        for value in ('0', '-1', '1920px', '1.5', ''):
            self.assertFalse(guard.check(article().replace('width="1920"', f'width="{value}"'))['ok'])
        self.assertFalse(guard.check(article().replace(' height="240"', ''))['ok'])

    def test_title_alt_and_loading_and_priority(self):
        for old, new in (('Wohnhaus mit Garten', ''), ('loading="eager"', 'loading="lazy"'),
                         (' fetchpriority="high"', ''), ('fetchpriority="high"', 'fetchpriority="low"')):
            self.assertFalse(guard.check(article().replace(old, new))['ok'])

    def test_other_images_lazy_and_decorative_sidebar_allowed(self):
        self.assertTrue(guard.check(article())['ok'])
        self.assertFalse(guard.check(article().replace('loading="lazy"', 'loading="eager"'))['ok'])
        self.assertFalse(guard.check(article().replace(' alt=""', ''))['ok'])
        self.assertFalse(guard.check(article().replace('class="avatar"', 'class="avatar" fetchpriority="high"'))['ok'])

    def test_body_alt_decorative_exception_does_not_apply_to_title(self):
        body_image = '<img src="https://example.org/divider.webp" alt="" width="120" height="80" loading="lazy">'
        html = article().replace('<p>Einordnung.</p>', '<p>Einordnung.</p>' + body_image)
        self.assertFalse(guard.check(html)['ok'])
        self.assertTrue(guard.check(html, decorative_image_srcs=['https://example.org/divider.webp'])['ok'])
        self.assertFalse(guard.check(article().replace('Wohnhaus mit Garten', ''),
                                    decorative_image_srcs=['https://example.org/title.webp'])['ok'])

    def test_duplicate_attributes_are_rejected(self):
        self.assertFalse(guard.check(article().replace('fetchpriority="high"', 'fetchpriority="high" fetchpriority="low"'))['ok'])

    def test_no_article_duplicate_roots_missing_hero_and_unclosed_root_fail(self):
        for html in ('<h1>Falsche Seite</h1>', article() + article(),
                     article().replace('lpb-editorial-article__media', 'other-figure'), article()[:-6]):
            self.assertFalse(guard.check(html)['ok'])

    def test_inert_template_headings_are_not_visible_article_headings(self):
        html = article().replace('<header>', '<template><h1>Vorlage</h1></template><header>')
        self.assertTrue(guard.check(html)['ok'])

    def test_unrelated_page_heading_does_not_pollute_article_check(self):
        self.assertTrue(guard.check('<nav><h2>Navigation</h2></nav>' + article())['ok'])

    def test_existing_issue_warns_only_with_real_original_baseline(self):
        original = article().replace(' fetchpriority="high"', '')
        updated = original.replace('Einordnung.', 'Korrigierte Einordnung.')
        result = guard.check(updated, baseline_html=original, expected_html=updated)
        self.assertTrue(result['ok'], result)
        self.assertEqual([w['code'] for w in result['warnings']], ['hero-priority'])
        self.assertFalse(guard.check(updated)['ok'])
        self.assertFalse(guard.check(updated, baseline_html=original.replace('lpb-editorial-ux--article', 'other'))['ok'])

    def test_new_error_does_not_disappear_among_existing_warnings(self):
        original = article().replace(' fetchpriority="high"', '')
        result = guard.check(original.replace('width="240"', 'width="0"'), baseline_html=original)
        self.assertFalse(result['ok'])
        self.assertTrue(result['warnings'])

    def test_changed_bad_dimensions_are_new_error(self):
        original = article().replace('width="240"', 'width="0"')
        self.assertFalse(guard.check(original.replace('width="0"', 'width="bad"'), baseline_html=original)['ok'])

    def test_readback_loss_of_headings_or_attributes_fails(self):
        for old, new in (('fetchpriority="high"', 'fetchpriority="low"'),
                         ('Wohnhaus mit Garten', 'Andere Beschreibung'),
                         ('Ein Detail', 'Geändertes Detail'), ('width="240"', 'width="241"'),
                         ('<h3><span>Ein Detail</span></h3>', '')):
            self.assertFalse(guard.check(article().replace(old, new), expected_html=article())['ok'])

    def test_invalid_input_cannot_verify_itself(self):
        bad = article().replace(' fetchpriority="high"', '')
        result = guard.check(bad, expected_html=bad)
        self.assertFalse(result['ok'])
        self.assertIn('invalid-preflight', [e['code'] for e in result['errors']])

    def test_cli_success_failure_and_no_mutation(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'article.html'
            for html, expected in ((article(), 0), (article().replace(' fetchpriority="high"', ''), 1)):
                path.write_text(html)
                result = subprocess.run([sys.executable, str(SCRIPT), '--html', str(path)], capture_output=True, text=True)
                self.assertEqual(result.returncode, expected, result.stderr)
                self.assertEqual(json.loads(result.stdout)['ok'], not expected)
                self.assertEqual(path.read_text(), html)


if __name__ == '__main__':
    unittest.main()
