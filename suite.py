from datetime import datetime
import logging
import os, sys

from vbench.api import collect_benchmarks

log = logging.getLogger('vb')
log.setLevel(logging.INFO)
#log.addHandler(logging.StreamHandler(sys.stdout))

benchmarks = collect_benchmarks(
    ['vb_core',
     'vb_io',
     'vb_indexing',
     'vb_random',
     'vb_reduce',
     'vb_ufunc',
     'vb_linalg',
     'vb_app',
     'vb_function_base',
    ])

log.info("Initializing settings")
import sys

try:
    import ConfigParser

    config = ConfigParser.ConfigParser()
    config.readfp(open(os.path.expanduser('~/.vbenchcfg')))

    REPO_PATH = config.get('setup', 'repo_path')
    REPO_URL = config.get('setup', 'repo_url')
    DB_PATH = config.get('setup', 'db_path')
    TMP_DIR = config.get('setup', 'tmp_dir')
except:
    cur_dir = os.path.dirname(__file__)
    REPO_PATH = os.path.join(cur_dir, 'numpy')
    REPO_URL = 'git://github.com/numpy/numpy.git'
    REPO_BROWSE = 'https://github.com/numpy/numpy'
    #REPO_URL = '/home/yoh/proj/pymvpa/numpy-vbench/numpy'
    DB_PATH = os.path.join(cur_dir, 'db/benchmarks.db')
    TMP_DIR = os.path.join(cur_dir, 'tmp')
    # Assure corresponding directories existence
    for s in (REPO_PATH, os.path.dirname(DB_PATH), TMP_DIR):
        if not os.path.exists(s):
            os.makedirs(s)

BRANCHES = ['master', 'origin/maintenance/1.8.x', 'origin/maintenance/1.7.x', 'origin/maintenance/1.6.x']

# : python setup.py clea
PREPARE = """
git clean -dfx
"""

BUILD = """
python setup.py build_ext --inplace
"""

DESCRIPTION = """
These historical benchmark graphs were produced with `vbench
<http://github.com/pydata/vbench>`__ (ATM with yet to be integrated
upstream changes in https://github.com/pydata/vbench/pull/33).

Original repository with the The `numpy_vb_common
<https://github.com/yarikoptic/numpy-vbench/blob/master/numpy_vb_common.py>`__
setup script defining various variables and data structures used
through-out the bench can be found on github_ .

.. _github: https://github.com/yarikoptic/numpy-vbench

Results were collected on a following machine:

  - Dual AMD Opteron(tm) Processor 246, 3GB RAM
  - Debian wheezy, amd-64 build (chroot on Debian with 3.2.0-4-amd64 kernel)
  - Python 2.7.3 64-bit

cpuinfo::

    vendor_id       : AuthenticAMD
    cpu family      : 15
    model           : 5
    model name      : AMD Opteron(tm) Processor 246
    stepping        : 8
    microcode       : 0x46
    cpu MHz         : 1994.032
    cache size      : 1024 KB
    fpu             : yes
    fpu_exception   : yes
    cpuid level     : 1
    wp              : yes
    flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx
                      fxsr sse sse2 syscall nx mmxext lm 3dnowext 3dnow rep_good nopl
    bogomips        : 3988.06
    TLB size        : 1024 4K pages
    clflush size    : 64
    cache_alignment : 64
    address sizes   : 40 bits physical, 48 bits virtual
    power management: ts ttp

"""
dependencies = ['numpy_vb_common.py']

# for now -- arbitrary day in the memorable past when NumPy existed
# already
START_DATE = datetime(2011, 03, 01)
#START_DATE = datetime(2012, 06, 20)

# Might not even be there and I do not see it used
# repo = GitRepo(REPO_PATH)

RST_BASE = 'source'
