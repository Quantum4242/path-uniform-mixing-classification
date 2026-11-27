#!/usr/bin/env python3
"""Run archived post-release finite audits and Lean SOURCE checks, not Lean."""
from pathlib import Path
import argparse, os, subprocess, sys, time
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cxx',default=os.environ.get('CXX','g++'))
    p.add_argument('--log-dir',type=Path,default=ROOT/'records'/'latest-supplements')
    a=p.parse_args()
    if sys.flags.optimize: raise SystemExit('Do not use Python -O.')
    logs=a.log_dir.resolve(); logs.mkdir(parents=True,exist_ok=True)
    audit=ROOT/'research-history'/'21-postrelease-audit'
    exe=audit/('enumerate_lattice.exe' if os.name=='nt' else 'enumerate_lattice')
    subprocess.run([a.cxx,'-std=c++17','-O3',str(audit/'enumerate_lattice.cpp'),'-o',str(exe)],check=True)
    tasks=[audit/'verify_odd_inventory.py',audit/'verify_large_even.py',ROOT/'lean'/'stage1'/'verify_phase1.py']
    try:
        with (logs/'summary.log').open('w',encoding='utf-8') as summary:
            for script in tasks:
                start=time.monotonic()
                with (logs/(script.stem+'.log')).open('w',encoding='utf-8') as log:
                    r=subprocess.run([sys.executable,str(script)],cwd=script.parent,stdout=log,stderr=subprocess.STDOUT,env=dict(os.environ,PYTHONIOENCODING='utf-8'))
                msg=f'{script.name}: exit={r.returncode}, elapsed={time.monotonic()-start:.2f}s'
                print(msg,flush=True);print(msg,file=summary,flush=True)
                if r.returncode:raise SystemExit(f'Failed: {script.name}')
            msg='3/3 supplemental arithmetic/source checks passed. Lean kernel compilation NOT performed.'
            print(msg);print(msg,file=summary)
    finally:
        exe.unlink(missing_ok=True)
if __name__=='__main__':main()
