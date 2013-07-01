#!/usr/bin/python

from suite import benchmarks, DB_PATH, RST_BASE, DESCRIPTION
from vbench.reports import generate_rst_files

generate_rst_files(benchmarks,
                   dbpath=DB_PATH,
                   outpath=RST_BASE,
                   description=DESCRIPTION)
