#!/usr/bin/env python3
"""Render one complete TF handoff; validate structure, never claim fact checking."""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import secrets
import sys
import unicodedata
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo


class PackageError(ValueError):
    pass


def object_fields(value, required, optional=()):
    if not isinstance(value, dict):
        raise PackageError('Expected an object')
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    if missing or extra:
        raise PackageError(f'Missing fields: {sorted(missing)}; unknown fields: {sorted(extra)}')


def text(value, field, one_line=False):
    if not isinstance(value, str) or not value.strip():
        raise PackageError(f'{field}: expected nonempty text')
    if any(ord(c) < 32 and c not in '\n\t\r' for c in value):
        raise PackageError(f'{field}: control character')
    if one_line and ('\n' in value or '\r' in value):
        raise PackageError(f'{field}: must be one line')
    if re.search(r'^\s*(#{1,6}\s|```|~~~|[=-]+\s*$)', value, re.M):
        raise PackageError(f'{field}: package sections or code fences are not allowed inside fields')
    return value.strip()


def string_list(value, field, allow_empty=False):
    if not isinstance(value, list) or (not value and not allow_empty):
        raise PackageError(f'{field}: expected a nonempty list' if not allow_empty else f'{field}: expected a list')
    return [text(item, field) for item in value]


def bullets(values):
    return '\n'.join('- ' + value.replace('\n', '\n  ') for value in values)


def render(data):
    object_fields(data, ('theme', 'rubrik', 'tags', 'checks', 'signal',
                        'reader_relevance', 'reader_questions', 'potential_value',
                        'limits', 'sources'))
    theme = text(data['theme'], 'theme', one_line=True)
    rubrik = text(data['rubrik'], 'rubrik', one_line=True)
    tags = string_list(data['tags'], 'tags', allow_empty=True)
    object_fields(data['checks'], ('research_date', 'taxonomy', 'registry'))
    checks = {key: text(value, f'checks.{key}') for key, value in data['checks'].items()}
    signal = text(data['signal'], 'signal')
    relevance = text(data['reader_relevance'], 'reader_relevance')
    questions = string_list(data['reader_questions'], 'reader_questions')
    value = text(data['potential_value'], 'potential_value')
    limits = string_list(data['limits'], 'limits')
    sources = data['sources']
    if not isinstance(sources, list) or not sources:
        raise PackageError('sources: expected a nonempty list')
    source_blocks = []
    urls = []
    for i, source in enumerate(sources, 1):
        object_fields(source, ('title', 'kind', 'evidence', 'publication_date',
                              'event_date', 'reference_period', 'url'), ('url_note',))
        title = text(source['title'], f'source {i}.title', one_line=True)
        kind = text(source['kind'], f'source {i}.kind', one_line=True)
        evidence = text(source['evidence'], f'source {i}.evidence')
        dates = {}
        for key in ('publication_date', 'event_date', 'reference_period'):
            dates[key] = text(source[key], f'source {i}.{key}', one_line=True) if source[key] is not None else 'nicht bekannt'
        url = source['url']
        note = source.get('url_note')
        if note is not None:
            note = text(note, f'source {i}.url_note')
        if url is None:
            if not note:
                raise PackageError(f'source {i}: missing URL requires url_note')
            url_line = 'Original-URL nicht verfügbar: ' + note
        else:
            if not isinstance(url, str) or any(c.isspace() or ord(c) < 32 or c in '<>`"\\' for c in url):
                raise PackageError(f'source {i}: URL must be a full visible HTTP(S) address')
            try:
                parsed = urlsplit(url)
                valid_url = parsed.scheme in ('https', 'http') and parsed.hostname and not parsed.username and not parsed.password
            except ValueError:
                valid_url = False
            if not valid_url:
                raise PackageError(f'source {i}: invalid HTTP(S) URL')
            urls.append(url)
            url_line = url + ('\n\nZugriffsgrenze: ' + note if note else '')
        source_blocks.append(
            f'**{title}**  \n{kind}; Veröffentlichung: {dates["publication_date"]}; '
            f'Ereignisdatum: {dates["event_date"]}; Bezugsstand: {dates["reference_period"]}  \n'
            f'{url_line}\n\nBelegte Aussage und Einordnung: {evidence}'
        )
    if not urls:
        raise PackageError('At least one source with a full HTTP(S) URL is required; this does not verify evidence')
    metadata = bullets([
        f'**Vorläufige Rubrik:** {rubrik}',
        '**Themen-Tags:** ' + (', '.join(tags) if tags else 'keine passende Zuordnung vorgenommen'),
        f'**Recherchestand:** {checks["research_date"]}',
        f'**Taxonomy-Abgleich:** {checks["taxonomy"]}',
        f'**Signalhistorie-Abgleich:** {checks["registry"]}',
    ])
    parts = ['# Signal Package', '## Thema', theme, metadata,
             '## Beobachtetes Signal', signal, '## Leserrelevanz', relevance,
             '## Mögliche Leserfragen', bullets(questions),
             '## Potenzieller eigenständiger Mehrwert', value,
             '## Offene Fragen und Grenzen', bullets(limits),
             '## Quellen und Evidenz', '\n\n'.join(source_blocks)]
    return theme, '\n\n'.join(parts) + '\n'


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise PackageError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding='utf-8'), object_pairs_hook=unique_object)
        theme, markdown = render(data)
        slug = unicodedata.normalize('NFKD', theme).encode('ascii', 'ignore').decode().lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')[:65].rstrip('-') or 'thema'
        stamp = datetime.now(ZoneInfo('Europe/Berlin')).strftime('%Y%m%d')
        args.output_dir.mkdir(parents=True, exist_ok=True)
        path = args.output_dir / f'signal-package-{stamp}-{slug}-{secrets.token_hex(4)}.md'
        content = markdown.encode('utf-8')
        with path.open('xb') as output:
            output.write(content)
        if path.read_bytes() != content:
            raise PackageError('File readback differs from rendered package')
        print(json.dumps({'path': str(path.resolve()), 'bytes': len(content),
                          'sha256': hashlib.sha256(content).hexdigest()}, ensure_ascii=False))
        return 0
    except (OSError, ValueError) as error:
        print(f'Package not delivered: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
