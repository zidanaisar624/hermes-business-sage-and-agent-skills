#!/usr/bin/env python3
"""Small stdlib-only audit for expected repository structure and social preview."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
skills = [p for p in (ROOT / 'skills').iterdir() if p.is_dir() and (p / 'SKILL.md').exists()]
assert len(skills) == 49, f'Expected 49 skill dirs, found {len(skills)}'
assert (ROOT/'skills/business-sage/scripts/cli_anything_business_sage.py').is_file()
assert (ROOT/'assets/github_social_preview_1280x640.jpg').is_file()
for f in (ROOT/'README.md',ROOT/'docs/INSTALLATION.md',ROOT/'docs/GITHUB_SETUP.md'):
    assert f.is_file(), f'Missing {f}'
# Read JPG dimensions using stdlib if Pillow not installed in CI.
raw = (ROOT/'assets/github_social_preview_1280x640.jpg').read_bytes()
assert len(raw) < 1_000_000, f'Social preview too large: {len(raw)} bytes'
assert raw[:3] == b'\xff\xd8\xff', 'Social preview must be a JPEG'
# Verify key metadata in the built JPG, rather than relying on the filename.
def jpeg_size(data):
    i=2
    while i<len(data):
        while i<len(data) and data[i] != 0xff: i+=1
        while i<len(data) and data[i] == 0xff: i+=1
        if i>=len(data):break
        marker=data[i];i+=1
        if marker in (0x01,0xD8,0xD9):continue
        if i+2>len(data):break
        length=int.from_bytes(data[i:i+2],'big')
        if marker in (0xC0,0xC1,0xC2,0xC3):
            return int.from_bytes(data[i+3:i+5],'big'),int.from_bytes(data[i+5:i+7],'big')
        i+=length
    raise ValueError('Image dimensions not found')
assert jpeg_size(raw) == (640,1280), f'Unexpected social preview dimensions: {jpeg_size(raw)}'
print(f'OK: {len(skills)} skills, 1280x640 JPG, {len(raw):,} bytes; required docs present')
