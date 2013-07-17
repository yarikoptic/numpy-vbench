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

for op in ('svd', 'inv', 'det', 'norm'):
    cmd = 'numpy.linalg.%s(a)' % op
    func = getattr(numpy.linalg, op)
    for t in squares_:
        if op == 'cholesky':
            # we need a positive definite
            astr = "numpy.dot(squares_[%r], squares_[%r].T)" % (t, t)
            atest = numpy.dot(squares_[t], squares_[t].T)
        else:
            astr = "squares_[%r]" % t
            atest = squares_[t]

        # check that dtype is supported at all
        try:
            _ = func(atest[:2, :2])
        except TypeError:
            continue
        vb_linalg.append(Benchmark(cmd, setup + "a=%s" % astr,
                                   name="%s_%s" % (cmd, t)))

# add basic lstsq test
vb_linalg.append(Benchmark('numpy.linalg.lstsq(a, b)',
                           setup + "a=squares_['float64']; b=indexes_rand[:100].astype(numpy.float64)",
                           name="numpy.linalg.lstsq(a, b)_float64"))
