"""Run the fixed certificate checks, failing on the first nonzero exit."""
from pathlib import Path
import subprocess
import sys
root = Path(__file__).resolve().parent
for rel in ('phase/verify_p19.py', 'integer/verify_certificate.py',
            'compact/check_compact.py', 'compact/check_gap_formula.py',
            'compact/verify_radical.py'):
    print(f'=== {rel} ===', flush=True)
    subprocess.run([sys.executable, str(root / rel)], check=True)
print('All five exact-arithmetic checkers passed. Full Lean formalization not claimed.')
