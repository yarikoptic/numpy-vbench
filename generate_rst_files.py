#!/usr/bin/python

from suite import benchmarks, DB_PATH, RST_BASE, DESCRIPTION, REPO_BROWSE, BRANCHES
from vbench.reports import generate_rst_files, generate_rst_analysis

generate_rst_analysis(
                   benchmarks,
                   dbpath=DB_PATH,
                   outpath=RST_BASE,
                   gh_repo=REPO_BROWSE)
generate_rst_files(benchmarks,
                   dbpath=DB_PATH,
                   outpath=RST_BASE,
                   branches=BRANCHES,
                   description=DESCRIPTION + """

.. include:: analysis.rst

""")
