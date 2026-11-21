#!/usr/bin/env python3
"""Check the six versioned skill packages; never install or modify personal skills."""
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
MANIFEST=ROOT/'manifest.json'


def skill_name(path):
    text=(path/'SKILL.md').read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise ValueError(f'{path.name}: missing skill frontmatter')
    match=re.search(r'^name:\s*([a-z0-9-]+)\s*$',text.split('---',2)[1],re.M)
    if not match:
        raise ValueError(f'{path.name}: invalid skill name')
    return match[1]


def collect(path):
    if not path.is_dir() or path.is_symlink():
        raise ValueError(f'Missing or invalid package: {path.name}')
    files={}
    for item in sorted(path.rglob('*')):
        if item.is_symlink():
            raise ValueError(f'Symlink in package: {item.name}')
        if not item.is_file() or '__pycache__' in item.parts or item.suffix=='.pyc':
            continue
        data=item.read_bytes()
        files[item.relative_to(path).as_posix()]={
            'sha256':hashlib.sha256(data).hexdigest(),
            'bytes':len(data),
            'mode':'100755' if item.stat().st_mode&0o111 else '100644',
        }
    if 'SKILL.md' not in files:
        raise ValueError(f'{path.name}: SKILL.md missing')
    return files


def installed_by_name(root,names):
    result={}
    for entry in root.glob('*/SKILL.md'):
        name=skill_name(entry.parent)
        if name in names:
            if name in result:
                raise ValueError(f'Duplicate installed skill: {name}')
            result[name]=entry.parent
    missing=set(names)-set(result)
    if missing:
        raise ValueError('Missing installed skills: '+', '.join(sorted(missing)))
    return result


def verify(manifest,installed_root=None,refresh=False):
    if manifest.get('schema_version')!=1 or not manifest.get('skills'):
        raise ValueError('Invalid manifest')
    names=set(manifest['skills'])
    directories={p.name for p in ROOT.iterdir() if p.is_dir() and p.name!='__pycache__'}
    if directories!=names:
        raise ValueError('Skill directory/manifest mismatch')
    if not all(re.fullmatch(r'scaling-editorial-[a-z0-9-]+',name) for name in names):
        raise ValueError('Invalid package name')
    installed=installed_by_name(installed_root,names) if installed_root else {}
    count=0
    for name,entry in sorted(manifest['skills'].items()):
        package=ROOT/name
        if skill_name(package)!=name:
            raise ValueError(f'{name}: folder and frontmatter differ')
        if not set(entry.get('requires_skills',[])).issubset(names):
            raise ValueError(f'{name}: missing bundled skill dependency')
        actual=collect(package)
        if refresh:
            entry['files']=actual
        elif actual!=entry['files']:
            changed=sorted(key for key in set(actual)|set(entry['files']) if actual.get(key)!=entry['files'].get(key))
            raise ValueError(f'{name}: package drift: '+', '.join(changed))
        if installed and collect(installed[name])!=actual:
            raise ValueError(f'{name}: installed package differs')
        count+=len(actual)
    return len(names),count


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compare-installed',type=Path,help='Read-only comparison by frontmatter name')
    parser.add_argument('--refresh',action='store_true',help='Refresh checksums after an intentional repository edit')
    args=parser.parse_args()
    if args.refresh and args.compare_installed:
        parser.error('Check the installed comparison separately before refreshing checksums.')
    manifest=json.loads(MANIFEST.read_text())
    skills,files=verify(manifest,args.compare_installed,args.refresh)
    if args.refresh:
        manifest['snapshot_date']=date.today().isoformat()
        MANIFEST.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'{skills} skill packages, {files} package files: '+('checksums refreshed' if args.refresh else 'integrity verified')+(' and installed files match' if args.compare_installed else ''))


if __name__=='__main__':
    try:
        main()
    except (ValueError,OSError,KeyError) as error:
        raise SystemExit(str(error))
