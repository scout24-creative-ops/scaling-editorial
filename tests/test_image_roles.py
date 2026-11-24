"""Prevent role swaps, lost associations and accidental changes to other articles."""
from html import escape
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/scaling-editorial-publisher/scripts/check_image_roles.py'
spec = importlib.util.spec_from_file_location('image_roles', SCRIPT)
roles = importlib.util.module_from_spec(spec)
spec.loader.exec_module(roles)
URLS = dict(title_url='https://images.example.org/title.webp',
            teaser_url='https://images.example.org/teaser.webp',
            list_url='https://images.example.org/list.webp')
HREF = '/verified-article'


def article(urls=None):
    urls = urls or URLS
    attrs = ' '.join(f'{roles.ROLE_ATTRIBUTES[k]}="{escape(urls[k + "_url"], quote=True)}"'
                     for k in ('title', 'teaser', 'list'))
    return (f'<div class="lpb-editorial-ux lpb-editorial-ux--article" {attrs}>'
            '<figure class="lpb-editorial-article__media"><div>'
            f'<img class="lpb-image--responsive" src="{escape(urls["title_url"], quote=True)}" '
            'width="1920" height="1080" alt="Selected motif" loading="eager">'
            '</div></figure></div>')


def overview(kind='card', src=None, href=HREF):
    cls = {'card': 'lpb-editorial-ux-card__image',
           'lead': 'lpb-editorial-ux-category-lead__image',
           'compact': 'lpb-editorial-ux-compact__image'}[kind]
    src = src or URLS['list_url' if kind == 'compact' else 'teaser_url']
    width, height = (120, 80) if kind == 'compact' else (1920, 1080)
    return (f'<article><a href="{href}"><img class="{cls}" '
            f'src="{escape(src, quote=True)}" width="{width}" height="{height}" '
            'alt="Selected motif" loading="lazy"></a></article>')


class PublisherImageRoles(unittest.TestCase):
    def overview_check(self, html, **extra):
        return roles.check(html, mode='overview', article_href=HREF, **URLS, **extra)

    def test_article_and_all_overview_slots_use_distinct_right_roles(self):
        self.assertTrue(roles.check(article(), mode='article', **URLS)['ok'])
        for kind in ('card', 'lead', 'compact'):
            self.assertTrue(self.overview_check(overview(kind))['ok'], kind)

    def test_compact_without_label_cannot_be_promoted_using_its_current_url(self):
        self.assertFalse(self.overview_check(overview('card', src=URLS['list_url']))['ok'])
        self.assertFalse(self.overview_check(overview('compact', src=URLS['teaser_url']))['ok'])

    def test_title_cannot_silently_fill_all_slots(self):
        self.assertFalse(self.overview_check(overview(src=URLS['title_url']))['ok'])
        same = dict.fromkeys(URLS, URLS['title_url'])
        self.assertFalse(roles.check(article(same), mode='article', **same)['ok'])

    def test_stored_role_map_is_required_and_checked_after_readback(self):
        html = article()
        changed = html.replace('data-lpb-image-list-url', 'data-lost-list-url')
        self.assertFalse(roles.check(changed, mode='article', expected_html=html, **URLS)['ok'])
        self.assertTrue(roles.check(html, mode='article', expected_html=html, **URLS)['ok'])

    def test_other_articles_and_reading_list_images_are_out_of_scope(self):
        other = overview('compact', src='https://legacy.example.org/original.png', href='/other')
        reading = '<img class="lpb-editorial-ux-reading__image" src="legacy.png" width="80" height="56">'
        result = self.overview_check(other + overview('compact') + reading)
        self.assertTrue(result['ok'])
        self.assertEqual(result['checkedImages'], 1)

    def test_unknown_link_and_duplicate_selected_image_fail(self):
        self.assertFalse(self.overview_check(overview(href='/other'))['ok'])
        self.assertFalse(self.overview_check(overview() + overview())['ok'])

    def test_missing_url_download_and_unsafe_url_do_not_pass(self):
        for bad in (None, '[TEASER-BILD-URL HIER EINFÜGEN]',
                    'https://chatgpt.com/library?file_id=example', 'javascript:alert(1)',
                    'https://user:password@images.example.org/a.webp'):
            urls = {**URLS, 'teaser_url': bad}
            self.assertFalse(roles.check(article(), mode='article', **urls)['ok'], bad)

    def test_query_parameters_and_html_escaping_survive(self):
        urls = {k: v + '?width=1&version=2' for k, v in URLS.items()}
        html = article(urls)
        self.assertTrue(roles.check(html, mode='article', expected_html=html, **urls)['ok'])
        self.assertFalse(roles.check(html.replace('version=2', 'version=3'), mode='article', **urls)['ok'])

    def test_srcset_cannot_override_the_confirmed_file(self):
        html = overview().replace(' loading=', ' srcset="https://images.example.org/wrong.webp 2x" loading=')
        self.assertFalse(self.overview_check(html)['ok'])

    def test_picture_override_is_not_implicitly_approved(self):
        html = overview().replace('<img', '<picture><source srcset="other.webp"><img').replace('</a>', '</picture></a>')
        self.assertFalse(self.overview_check(html)['ok'])

    def test_saved_alt_or_dimensions_change_is_detected(self):
        original = overview()
        for changed in (original.replace('Selected motif', 'Changed motif'),
                        original.replace('1920', '1921')):
            self.assertFalse(self.overview_check(changed, expected_html=original)['ok'])

    def test_invalid_preflight_cannot_verify_its_own_readback(self):
        bad = overview(src=URLS['list_url'])
        self.assertFalse(self.overview_check(bad, expected_html=bad)['ok'])

    def test_article_only_exception_does_not_allow_missing_urls_on_overview(self):
        html = article()
        self.assertTrue(roles.check(html, mode='article', title_url=URLS['title_url'], article_only=True)['ok'])
        self.assertFalse(roles.check(overview(), mode='overview', article_href=HREF,
                                     title_url=URLS['title_url'], article_only=True)['ok'])

    def test_cli_returns_failure_on_wrong_role(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'input.html'
            path.write_text(overview(src=URLS['list_url']))
            cmd = [sys.executable, str(SCRIPT), '--html', str(path), '--mode', 'overview',
                   '--article-href', HREF, '--title-url', URLS['title_url'],
                   '--teaser-url', URLS['teaser_url'], '--list-url', URLS['list_url']]
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('wrong image URL', result.stdout)


if __name__ == '__main__':
    unittest.main()
