#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
from datetime import datetime

from numpy_vb_common import squares_, numpy

common_setup = """\
from numpy_vb_common import *
"""
setup = common_setup

vb_linalg = []
# SVDs
cmd = 'numpy.linalg.svd(a)'
for t in squares_:
    # check that dtype is supported at all
    try:
        _ = numpy.linalg.svd(squares_[t][:2, :2])
    except TypeError:
        continue
    vb_linalg.append(Benchmark(cmd, setup + "a=squares_[%r]" % t,
                               name="%s_%s" % (cmd, t)))
