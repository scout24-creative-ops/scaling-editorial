#!/usr/bin/env python3
"""Read-only checks for the selected article's two hosted WebP roles."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import urlsplit

ROLE_ATTRIBUTES = {
    'title': 'data-lpb-image-title-url',
    'list': 'data-lpb-image-list-url',
}
OVERVIEW_CLASSES = {
    'lpb-editorial-ux-card__image': 'title',
    'lpb-editorial-ux-category-lead__image': 'title',
    'lpb-editorial-ux-compact__image': 'list',
    'lpb-editorial-ux-reading__image': 'list',
}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}


def hosted_url(value):
    if not isinstance(value, str) or not value or any(c.isspace() for c in value):
        return False
    try:
        p = urlsplit(value)
        return (p.scheme == 'https' and bool(p.hostname) and not p.username
                and not p.password and not p.fragment and p.path.lower().endswith('.webp')
                and 'platzhalter' not in p.path.lower() and 'placeholder' not in p.path.lower()
                and p.hostname not in ('chatgpt.com', 'www.chatgpt.com')
                and not any(c in value for c in '<>"[]'))
    except ValueError:
        return False


class Images(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.maps, self.images = [], [], []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        classes = set(d.get('class', '').split())
        if 'lpb-editorial-ux--article' in classes:
            self.maps.append(d)
        if tag == 'img':
            parents = [node for _, node in self.stack]
            parent_classes = set().union(*(set(p.get('class', '').split()) for p in parents))
            role = next((v for k, v in OVERVIEW_CLASSES.items() if k in classes), None)
            if ('lpb-image--responsive' in classes
                    and 'lpb-editorial-article__media' in parent_classes):
                role = 'title'
            if role:
                href = next((p.get('href') for t, p in reversed(self.stack) if t == 'a'), None)
                self.images.append({'role': role, 'is_hero': 'lpb-editorial-article__media' in parent_classes, 'attrs': d, 'href': href,
                                    'picture': any(t == 'picture' for t, _ in self.stack)})
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


def check(html, *, mode, title_url, list_url=None,
          article_href=None, article_only=False, expected_html=None):
    errors = []
    urls = {'title': title_url, 'list': list_url}
    required = ['title'] if article_only and mode == 'article' else list(urls)
    if article_only and mode != 'article':
        errors.append('article_only is valid only for an expressly limited article-page check')
    if mode not in ('article', 'overview'):
        errors.append('unknown page mode')
    for role in required:
        if not hosted_url(urls[role]):
            errors.append(f'{role}: missing or unsafe hosted image URL (downloads/placeholders are invalid)')
    supplied = [v for v in urls.values() if v is not None]
    if len(supplied) != len(set(supplied)):
        errors.append('image roles require distinct confirmed URLs')
    if mode == 'overview' and not article_href:
        errors.append('overview requires the exact verified article href')
    parser = Images()
    parser.feed(html)
    if mode == 'article':
        selected = [x for x in parser.images if x['is_hero']]
        if len(parser.maps) != 1:
            errors.append('article requires one canonical article root with saved image-role attributes')
        else:
            if 'data-lpb-image-teaser-url' in parser.maps[0]:
                errors.append('legacy third image-role attribute is not allowed for the new schema')
            for role in required:
                if parser.maps[0].get(ROLE_ATTRIBUTES[role]) != urls[role]:
                    errors.append(f'{role}: saved role attribute is missing or changed')
    else:
        selected = [x for x in parser.images
                    if not x['is_hero'] and x['href'] == article_href]
    if len(selected) != 1:
        errors.append('expected exactly one managed image for the selected article on this page')
    signatures = []
    for image in selected:
        d, role = image['attrs'], image['role']
        if d.get('src') != urls[role]:
            errors.append(f'{role}: wrong image URL in selected slot')
        if d.get('srcset') or image['picture']:
            errors.append('unverified responsive image sources may override the selected role URL')
        try:
            width, height = int(d.get('width', '')), int(d.get('height', ''))
            valid_dimensions = ((width, height) == (128, 72) if role == 'list'
                                else (width, height) == (1920, 1080))
        except ValueError:
            valid_dimensions = False
        if not valid_dimensions:
            errors.append(f'{role}: canonical image dimensions/ratio are missing or changed')
        signatures.append((role, *(d.get(k) for k in ('src', 'alt', 'width', 'height', 'loading'))))
    if expected_html is not None:
        expected = check(expected_html, mode=mode, title_url=title_url,
                         list_url=list_url,
                         article_href=article_href, article_only=article_only)
        if not expected['ok']:
            errors.append('expected HTML did not pass its own preflight')
        if signatures != expected['images']:
            errors.append('saved image attributes differ from the validated input')
    return {'ok': not errors, 'mode': mode, 'checkedImages': len(selected),
            'images': signatures, 'errors': errors}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--html', type=Path, required=True)
    p.add_argument('--mode', choices=('article', 'overview'), required=True)
    p.add_argument('--title-url', required=True)
    p.add_argument('--list-url')
    p.add_argument('--article-href')
    p.add_argument('--article-only', action='store_true')
    p.add_argument('--expected-html', type=Path)
    args = p.parse_args()
    try:
        result = check(args.html.read_text(encoding='utf-8'), mode=args.mode,
                       title_url=args.title_url, teaser_url=args.teaser_url,
                       list_url=args.list_url, article_href=args.article_href,
                       article_only=args.article_only,
                       expected_html=args.expected_html.read_text(encoding='utf-8')
                       if args.expected_html else None)
    except (OSError, ValueError) as exc:
        p.exit(1, f'Image-role check failed: {exc}\n')
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if result['ok'] else 1)
