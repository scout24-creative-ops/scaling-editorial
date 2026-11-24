#!/usr/bin/env python3
"""Read-only check of canonical editorial source links before and after CMS storage."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urlsplit

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
        'link', 'meta', 'param', 'source', 'track', 'wbr'}


class SourceLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.links = []
        self.lists = 0
        self.errors = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        is_list = 'lpb-editorial-article__sources-list' in (values.get('class') or '').split()
        inside = is_list or any(frame[1] for frame in self.stack)
        if is_list:
            self.lists += 1
        if tag == 'a' and inside:
            for key in ('href', 'rel'):
                if sum(name == key for name, _ in attrs) > 1:
                    self.errors.append(f'Duplicate {key} attribute in source link')
            self.links.append((values.get('href') or '', set((values.get('rel') or '').lower().split())))
        if tag not in VOID:
            self.stack.append((tag, inside))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break


def check(html, expected_html=None):
    parser = SourceLinks()
    parser.feed(html)
    parser.close()
    errors = list(parser.errors)
    if not parser.lists or not parser.links:
        errors.append('No linked canonical source list found; real-article verification is incomplete')
    external = 0
    for href, rel in parser.links:
        try:
            url = urlsplit(href)
            host = (url.hostname or '').lower().rstrip('.')
            safe = (url.scheme == 'https' and host and not url.username and not url.password
                    and not any(c.isspace() or ord(c) < 32 or c in '<>`"\\' for c in href))
        except ValueError:
            safe = False
        if not safe:
            errors.append(f'Source requires a full safe HTTPS URL: {href}')
            continue
        internal = host == 'immobilienscout24.de' or host.endswith('.immobilienscout24.de')
        if not internal:
            external += 1
            if 'nofollow' not in rel:
                errors.append(f'Missing nofollow: {href}')
    if expected_html is not None:
        baseline = check(expected_html)
        if not baseline['ok']:
            errors.append('Expected input did not pass the source-link preflight')
        expected = SourceLinks()
        expected.feed(expected_html)
        if [href for href, _ in parser.links] != [href for href, _ in expected.links]:
            errors.append('Saved source destinations/order differ from validated input')
        else:
            for (href, actual_rel), (_, required_rel) in zip(parser.links, expected.links):
                if not required_rel.issubset(actual_rel):
                    errors.append(f'Saved source lost required rel tokens: {href}')
    return {'ok': not errors, 'sources': len(parser.links),
            'externalSources': external, 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, required=True)
    parser.add_argument('--expected-html', type=Path,
                        help='Validated pre-write HTML for a saved-content comparison')
    args = parser.parse_args()
    try:
        result = check(args.html.read_text(encoding='utf-8'),
                       args.expected_html.read_text(encoding='utf-8') if args.expected_html else None)
    except (OSError, ValueError) as error:
        result = {'ok': False, 'errors': [str(error)]}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result['ok'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
