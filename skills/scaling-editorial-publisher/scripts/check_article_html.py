#!/usr/bin/env python3
"""Read-only article heading/image checks; no network, CMS writes or SEO-tag audit."""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}
IGNORED = {'script', 'style', 'template', 'noscript'}
IMAGE_KEYS = ('src', 'alt', 'width', 'height', 'loading', 'fetchpriority')


class Article(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.headings, self.images = [], [], []
        self.roots = self.articles = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        classes = set(d.get('class', '').split())
        parents = set().union(*(set(a.get('class', '').split()) for _, a in self.stack))
        ignored = tag in IGNORED or any(t in IGNORED for t, _ in self.stack)
        if not ignored:
            self.roots += 'lpb-editorial-ux--article' in classes
            self.articles += 'lpb-editorial-article' in classes
            inside = 'lpb-editorial-ux--article' in parents
            if inside and tag == 'img':
                self.images.append({
                    'attrs': d,
                    'hero': 'lpb-editorial-article__media' in parents,
                    'body': 'lpb-editorial-article__body' in parents,
                    'duplicates': len(attrs) != len(d),
                })
            if ('lpb-editorial-article' in parents and len(tag) == 2
                    and tag[0] == 'h' and tag[1] in '123456'):
                self.headings.append({'level': int(tag[1]), 'text': '',
                                      'hidden': any('hidden' in a or a.get('aria-hidden') == 'true'
                                                    for _, a in self.stack + [(tag, d)])})
        if tag not in VOID:
            self.stack.append((tag, d))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if (self.headings and any(t in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6')
                                  for t, _ in self.stack)
                and any('lpb-editorial-article' in a.get('class', '').split()
                        for _, a in self.stack)
                and not any(t in IGNORED for t, _ in self.stack)):
            self.headings[-1]['text'] += data


def inspect(html, decorative_image_srcs):
    p = Article()
    p.feed(html)
    issues = []

    def issue(code, detail, subject):
        issues.append({'code': code, 'detail': detail, 'subject': subject})

    if p.roots != 1 or p.articles != 1:
        issue('article-root', 'Require one canonical UX article root and one inner article.',
              [p.roots, p.articles])
    if any('lpb-editorial-ux--article' in a.get('class', '').split() for _, a in p.stack):
        issue('unclosed-root', 'Article root was not closed.', [])
    levels = [h['level'] for h in p.headings]
    if levels.count(1) != 1 or not levels or levels[0] != 1:
        issue('h1', 'Require exactly one H1, before the other article headings.', levels)
    previous = 0
    for i, h in enumerate(p.headings):
        h['text'] = ' '.join(h['text'].split())
        if not h['text'] or h['hidden']:
            issue('heading-content', 'Article headings must contain visible text.', [i, h])
        if h['level'] > previous + 1:
            issue('heading-order', 'Do not skip a heading level (H2 before H3).', [i, levels])
        previous = h['level']
    heroes = [im for im in p.images if im['hero']]
    if len(heroes) != 1:
        issue('hero-count', 'Require exactly one article title image.', len(heroes))
    for i, im in enumerate(p.images):
        a = im['attrs']
        src = a.get('src')
        if im['duplicates']:
            issue('image-attributes', 'Duplicate image attributes are ambiguous.', [i, src])
        if 'alt' not in a:
            issue('image-alt', 'Every image needs an alt attribute.', [i, src])
        if (im['hero'] or im['body']) and not a.get('alt', '').strip():
            if im['hero'] or src not in decorative_image_srcs:
                issue('editorial-alt', 'Supply editorial alt text; do not invent it.', [i, src])
        dims = [a.get('width', ''), a.get('height', '')]
        if not all(v.isascii() and v.isdecimal() and int(v) > 0 for v in dims):
            issue('image-dimensions', 'Image width and height must be positive integers.', [i, src, dims])
        required_loading = 'eager' if im['hero'] else 'lazy'
        if a.get('loading') != required_loading:
            issue('image-loading', f'Require loading="{required_loading}" in this image slot.',
                  [i, src, a.get('loading')])
        if im['hero'] and a.get('fetchpriority') != 'high':
            issue('hero-priority', 'Require fetchpriority="high" on the title image.',
                  [i, src, a.get('fetchpriority')])
        if not im['hero'] and a.get('fetchpriority') == 'high':
            issue('other-priority', 'Reserve high image priority for the title image.', [i, src])
    signature = {'headings': p.headings,
                 'images': [[im['hero'], im['body'], *[im['attrs'].get(k) for k in IMAGE_KEYS]]
                            for im in p.images]}
    return issues, signature


def check(html, *, expected_html=None, baseline_html=None, decorative_image_srcs=()):
    issues, signature = inspect(html, set(decorative_image_srcs))
    old = Counter()
    if baseline_html is not None:
        prior, _ = inspect(baseline_html, set(decorative_image_srcs))
        old.update(json.dumps(x, sort_keys=True) for x in prior
                   if x['code'] not in ('article-root', 'unclosed-root', 'hero-count'))
    errors, warnings = [], []
    for issue in issues:
        key = json.dumps(issue, sort_keys=True)
        if old[key]:
            old[key] -= 1
            warnings.append(issue)
        else:
            errors.append(issue)
    if expected_html is not None:
        expected = check(expected_html, baseline_html=baseline_html,
                         decorative_image_srcs=decorative_image_srcs)
        if not expected['ok']:
            errors.append({'code': 'invalid-preflight', 'detail': 'Expected HTML failed its own preflight.'})
        if signature != expected['signature']:
            errors.append({'code': 'readback', 'detail': 'Saved headings or image attributes differ from validated input.'})
    return {'ok': not errors, 'checkedImages': len(signature['images']),
            'checkedHeadings': len(signature['headings']), 'errors': errors,
            'warnings': warnings, 'signature': signature}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--html', type=Path, required=True)
    p.add_argument('--expected-html', type=Path)
    p.add_argument('--baseline-html', type=Path)
    p.add_argument('--decorative-image-src', action='append', default=[])
    args = p.parse_args()
    try:
        result = check(args.html.read_text(encoding='utf-8'),
                       expected_html=args.expected_html.read_text(encoding='utf-8') if args.expected_html else None,
                       baseline_html=args.baseline_html.read_text(encoding='utf-8') if args.baseline_html else None,
                       decorative_image_srcs=args.decorative_image_src)
    except (OSError, ValueError) as exc:
        p.exit(1, f'Article HTML check failed: {exc}\n')
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
