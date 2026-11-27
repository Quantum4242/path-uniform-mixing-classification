#!/usr/bin/env python3
"""Build the portable enumerator and run the exact verification suite.
Run from any working directory. No network access is needed after installation.
"""
from pathlib import Path
import argparse, os, platform, shutil, subprocess, sys, time
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SCRIPTS=("verify_short_relations.py","verify_three_blocks.py","verify_classification.py",
         "verify_low_degree.py","verify_all.py","verify_small_density.py","verify_lattice.py",
         "verify_q33_density.py","verify_localization.py","verify_uniform_floor.py",
         "verify_release_consistency.py")
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cxx',default=os.environ.get('CXX','g++'),help='C++17 compiler executable (e.g. g++, clang++)')
    p.add_argument('--log-dir',type=Path,default=ROOT/'records'/'latest')
    p.add_argument('--quick',action='store_true',help='Only run the release consistency and localization checks; NOT the full suite.')
    args=p.parse_args()
    if sys.flags.optimize:raise SystemExit('Assertions must be enabled; do not use Python -O.')
    import sympy
    logs=args.log_dir.resolve();logs.mkdir(parents=True,exist_ok=True)
    exe=HERE/('enumerate_lattice.exe' if os.name=='nt' else 'enumerate_lattice')
    with (logs/'summary.log').open('w',encoding='utf-8') as summary:
        def note(s):print(s,flush=True);print(s,file=summary,flush=True)
        note(f'Python {platform.python_version()}, SymPy {sympy.__version__}, {platform.platform()}')
        if not args.quick:
            if not shutil.which(args.cxx):raise SystemExit(f'C++ compiler not found: {args.cxx}')
            subprocess.run([args.cxx,'-std=c++17','-O3',str(HERE/'enumerate_lattice.cpp'),'-o',str(exe)],check=True,cwd=HERE)
        scripts=SCRIPTS if not args.quick else ('verify_localization.py','verify_release_consistency.py')
        for script in scripts:
            start=time.monotonic()
            with (logs/(Path(script).stem+'.log')).open('w',encoding='utf-8') as log:
                child_env=dict(os.environ,PYTHONIOENCODING='utf-8')
                result=subprocess.run([sys.executable,str(HERE/script)],cwd=HERE,stdout=log,stderr=subprocess.STDOUT,env=child_env)
            note(f'{script}: exit={result.returncode}, elapsed={time.monotonic()-start:.2f}s')
            if result.returncode:raise SystemExit(f'Check failed: see {logs/ (Path(script).stem+".log")}')
        note(f'{len(scripts)}/{len(scripts)} executed checks passed'+(' (quick subset only)' if args.quick else ' (full arithmetic suite)'))
if __name__=='__main__':main()
