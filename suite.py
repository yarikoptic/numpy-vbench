from datetime import datetime
import logging
import os, sys

from vbench.api import collect_benchmarks

log = logging.getLogger('vb')
log.setLevel(logging.DEBUG)
#log.addHandler(logging.StreamHandler(sys.stdout))

benchmarks = collect_benchmarks(
    ['vb_io',
     'vb_indexing',
     'vb_random', 'vb_reduce', 'vb_ufunc',
     'vb_linalg'
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
    #REPO_URL = '/home/yoh/proj/pymvpa/numpy-vbench/numpy'
    DB_PATH = os.path.join(cur_dir, 'db/benchmarks.db')
    TMP_DIR = os.path.join(cur_dir, 'tmp')
    # Assure corresponding directories existence
    for s in (REPO_PATH, os.path.dirname(DB_PATH), TMP_DIR):
        if not os.path.exists(s):
            os.makedirs(s)

# : python setup.py clea
PREPARE = """
git clean -dfx
"""

BUILD = """
python setup.py build_ext --inplace
"""

DESCRIPTION = """
The ``numpy_vb_common`` setup script defining various variables and data
structures used through-out the bench can be found here_

.. _here: https://github.com/yarikoptic/numpy-vbench/blob/master/numpy_vb_common.py

Produced on a machine with

  - XXX (use lego)
  - AMD XXX
  - Debian wheezy
  - Python 2.7.2 64-bit
"""
dependencies = ['numpy_vb_common.py']

# for now -- arbitrary day in the memorable past when NumPy existed
# already
START_DATE = datetime(2011, 01, 01)
#START_DATE = datetime(2012, 06, 20)

# Might not even be there and I do not see it used
# repo = GitRepo(REPO_PATH)

RST_BASE = 'source'
