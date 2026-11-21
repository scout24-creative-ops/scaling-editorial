#!/usr/bin/env python3
"""Write one clean editorial handoff file; structural checks are not fact checks."""
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

CONTRACTS = {'story': {'title': 'Story Package', 'sections': ['Story-Idee', 'Redaktionelle Einordnung', 'Zentrale Leserfrage und belegte Antwort', 'Zielgruppe und Vorwissen', 'Story Angle und Hauptformat', 'Core Story Claim und Story Promise', 'Headline-Potenzial', 'Fakten, Erklärungen und Story-Material', 'Empfohlene Artikelstruktur', 'Aussagegrenzen und Do-not-claim-Liste', 'Quellen und Evidenz', 'Notwendige Prüfungen'], 'optional_sections': [], 'metadata': [], 'optional_metadata': [], 'sources_section': 'Quellen und Evidenz'}, 'research': {'title': 'Recherche und redaktionelle Begründung', 'sections': ['Entscheidung und Arbeitsstand', 'Story-Kern', 'Evidenz-Ledger', 'Befund und Interpretation', 'Gegenprüfung', 'Nächste Schritte'], 'optional_sections': [], 'metadata': [], 'optional_metadata': [], 'sources_section': None}}

class PackageError(ValueError):
    pass

def fields(value, required, optional=()):
    if not isinstance(value, dict):
        raise PackageError('Expected an object')
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    if missing or extra:
        raise PackageError(f'Missing fields: {sorted(missing)}; unknown fields: {sorted(extra)}')

def clean_text(value, label, one_line=False):
    if not isinstance(value,str) or not value.strip():
        raise PackageError(f'{label}: expected nonempty text')
    if any(ord(c)<32 and c not in '\n\r\t' for c in value):
        raise PackageError(f'{label}: control character')
    if one_line and ('\n' in value or '\r' in value):
        raise PackageError(f'{label}: expected a single line')
    # H3 subheads are permitted; H1/H2, Setext and fenced blocks cannot alter the package.
    if re.search(r'^\s*(#{1,2}(?:\s|$)|```|~~~|[=-]+\s*$)',value,re.M):
        raise PackageError(f'{label}: top-level heading, separator or code fence inside content')
    return value.strip()

def public_url(value):
    if not isinstance(value,str) or any(c.isspace() or ord(c)<32 or c in '<>`"\\' for c in value):
        raise PackageError('source_urls: expected full HTTP(S) URLs')
    try:
        parsed=urlsplit(value)
        valid=parsed.scheme in ('https','http') and parsed.hostname and not parsed.username and not parsed.password
    except ValueError:
        valid=False
    if not valid:
        raise PackageError('source_urls: invalid HTTP(S) URL')
    if parsed.hostname.lower() == 'wiki.scout24.com':
        raise PackageError('Internal Wiki working references are not public article sources')
    return value

def render(data):
    fields(data,('kind','topic','metadata','sections','source_urls'))
    kind=data['kind']
    if not isinstance(kind,str) or kind not in CONTRACTS:
        raise PackageError('Unsupported package kind')
    spec=CONTRACTS[kind]
    topic=clean_text(data['topic'],'topic',True)
    metadata=data['metadata']
    if not isinstance(metadata,list):
        raise PackageError('metadata: expected a list')
    labels=[]
    metadata_lines=[]
    for item in metadata:
        fields(item,('label','value'))
        label=clean_text(item['label'],'metadata label',True)
        value=clean_text(item['value'],'metadata value',True)
        if label in labels:
            raise PackageError('Duplicate metadata label')
        labels.append(label)
        metadata_lines.append(f'- **{label}:** {value}')
    missing=set(spec['metadata'])-set(labels)
    extra=set(labels)-set(spec['metadata'])-set(spec['optional_metadata'])
    if missing or extra:
        raise PackageError(f'Invalid metadata; missing={sorted(missing)}, unknown={sorted(extra)}')
    if labels[:len(spec['metadata'])] != spec['metadata']:
        raise PackageError('Required metadata order differs from output contract')
    sections=data['sections']
    if not isinstance(sections,list):
        raise PackageError('sections: expected a list')
    names=[]
    content={}
    for item in sections:
        fields(item,('heading','body'))
        heading=clean_text(item['heading'],'section heading',True)
        if heading in content:
            raise PackageError('Duplicate section heading')
        names.append(heading)
        content[heading]=clean_text(item['body'],heading)
    expected=[s for s in spec['sections'] if s not in spec['optional_sections'] or s in content]
    if names != expected:
        raise PackageError(f'Sections must match contract in order: {expected}')
    urls=data['source_urls']
    if not isinstance(urls,list):
        raise PackageError('source_urls: expected a list')
    urls=[public_url(url) for url in urls]
    source_body=content.get(spec['sources_section'],'') if spec['sources_section'] else '\n'.join(content.values())
    visible_lines={line.strip().removeprefix('- ').rstrip() for line in source_body.splitlines()}
    for url in urls:
        if url not in visible_lines and f'[{url}]({url})' not in visible_lines and f'<{url}>' not in visible_lines:
            raise PackageError(f'Source URL must be fully visible on its own line: {url}')
    if kind=='article':
        alternatives=[line for line in content['Headline-Alternativen'].splitlines() if re.match(r'^\s*[-*+]\s+\S',line)]
        if len(alternatives)!=2:
            raise PackageError('Exactly two review-only headline alternatives are required')
    parts=['# '+spec['title']]
    if metadata_lines:
        parts.append('\n'.join(metadata_lines))
    for heading in names:
        parts.extend(['## '+heading,content[heading]])
    return kind,topic,'\n\n'.join(parts)+'\n'

def no_duplicate_keys(pairs):
    result={}
    for key,value in pairs:
        if key in result:
            raise PackageError(f'Duplicate JSON key: {key}')
        result[key]=value
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    try:
        data=json.loads(args.input.read_text(encoding='utf-8'),object_pairs_hook=no_duplicate_keys)
        kind,topic,markdown=render(data)
        slug=unicodedata.normalize('NFKD',topic).encode('ascii','ignore').decode().lower()
        slug=re.sub(r'[^a-z0-9]+','-',slug).strip('-')[:65].rstrip('-') or 'thema'
        stamp=datetime.now(ZoneInfo('Europe/Berlin')).strftime('%Y%m%d')
        args.output_dir.mkdir(parents=True,exist_ok=True)
        target=args.output_dir/f'{kind}-package-{stamp}-{slug}-{secrets.token_hex(4)}.md'
        raw=markdown.encode('utf-8')
        with target.open('xb') as handle:
            handle.write(raw)
        if target.read_bytes()!=raw:
            raise PackageError('Readback differs from package')
        print(json.dumps({'path':str(target.resolve()),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},ensure_ascii=False))
        return 0
    except (OSError,ValueError) as error:
        print(f'Package not delivered: {error}',file=sys.stderr)
        return 2

if __name__=='__main__':
    sys.exit(main())
