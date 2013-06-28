#!/usr/bin/env python
import logging, os, sys

try:
    import numpy
except ImportError:
    # yoh: In a clean chroot I use I disabled system-wide numpy altogether
    # as a paranoid measure to assure that benchmark scripts do not use it
    # anyhow.  Since they would not inherit this sys.path, I am pointing
    # to local numpy build, since it is needed for proper
    # collection/processing of benchmarks
    sys.path.insert(1, os.path.join(os.getcwd(), "numpy"))

from vbench.api import BenchmarkRunner
from vbench.config import is_interactive

from suite import *

log = logging.getLogger('vb')

def run_process():
    runner = BenchmarkRunner(benchmarks, REPO_PATH, REPO_URL,
                             BUILD, DB_PATH, TMP_DIR, PREPARE,
                             clean_cmd=PREPARE,
                             run_option='eod', run_order='multires',
                             start_date=START_DATE,
                             module_dependencies=dependencies)
    runner.run()

if __name__ == '__main__':
    try:
        run_process()
    except Exception as exc:
        log.error('%s (%s)' % (str(exc), exc.__class__.__name__))
        if __debug__ and is_interactive(): # and args.common_debug:
            import pdb
            pdb.post_mortem()
        raise

