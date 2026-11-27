from pathlib import Path
from hashlib import sha256
r=Path(__file__).resolve().parents[1]
count=0
for line in (r/'SHA256SUMS').read_text().splitlines():
    h, name=line.split('  ',1)
    p=r/name
    if not p.is_file() or sha256(p.read_bytes()).hexdigest()!=h:
        raise SystemExit(f'Checksum mismatch: {name}')
    count+=1
print(f'{count} release files verified')
