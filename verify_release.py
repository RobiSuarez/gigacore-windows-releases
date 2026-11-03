"""Verify exact, locally scanned artifacts before publishing a Windows release."""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(downloaded=None):
    current = json.loads((ROOT / 'current.json').read_text(encoding='utf-8'))
    version = current['version']
    if not isinstance(version, str) or not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', version):
        raise ValueError('Invalid version')
    folder = ROOT / 'releases' / version
    release = json.loads((folder / 'manifest.json').read_text(encoding='utf-8'))
    filename = f'GigaCore-{version}-x64.msi'
    scan_name = f'GigaCore-{version}-x64.scan.json'
    expected_files = {filename, scan_name, 'manifest.json', 'notes.md'}
    if {p.name for p in folder.iterdir()} != expected_files or any(p.is_symlink() for p in folder.iterdir()):
        raise ValueError('Unexpected artifacts')
    if (release.get('approved') is not True or release.get('version') != version
            or release.get('filename') != filename or release.get('scanFile') != scan_name):
        raise ValueError('Release has not been approved')
    for field in ('sha256', 'scanReportSha256', 'sourceDigest'):
        if not re.fullmatch(r'[0-9a-f]{64}', release.get(field, '')):
            raise ValueError('Missing fingerprint: ' + field)
    package = folder / filename
    size = package.stat().st_size
    if not 0 < size <= 64 * 1024 * 1024 or release.get('size') != size or digest(package) != release['sha256']:
        raise ValueError('Installer fingerprint mismatch')
    report = folder / scan_name
    if digest(report) != release['scanReportSha256']:
        raise ValueError('Scan fingerprint mismatch')
    scan = json.loads(report.read_text(encoding='utf-8'))
    if (scan.get('schema') != 1 or scan.get('status') != 'no-detections'
            or scan.get('error') or scan.get('threatIds') or not scan.get('engine') or not scan.get('signatures')
            or scan.get('files') != [{'name': filename, 'size': size, 'sha256': release['sha256']}]):
        raise ValueError('Installer has no matching Defender report')
    if not (folder / 'notes.md').read_text(encoding='utf-8').strip():
        raise ValueError('Release notes are required')
    if downloaded:
        downloaded = Path(downloaded)
        if {p.name for p in downloaded.iterdir()} != {filename, scan_name}:
            raise ValueError('Unexpected remote assets')
        for name in (filename, scan_name):
            if digest(downloaded / name) != digest(folder / name):
                raise ValueError('Remote asset differs: ' + name)
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
            output.write('version=' + version + '\n')
    print('Verified exact MSI and scan: ' + version)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--downloaded')
    verify(parser.parse_args().downloaded)
