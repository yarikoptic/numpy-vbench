#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark

common_setup = """\
from numpy_vb_common import *
from tempfile import TemporaryFile
"""
#----------------------------------------------------------------------
# mappers
setup = common_setup + """\
outfile = TemporaryFile()
"""
cleanup = "outfile.close()"

vb_savez_squares = Benchmark('numpy.savez(outfile, squares)', setup, cleanup=cleanup)

