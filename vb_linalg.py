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

for op in ('svd', 'pinv', 'det', 'norm'):
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

# and basic testing of .dot and .einsum
setup = """\
import numpy
a = numpy.arange(60000.).reshape(150, 400)
b = numpy.arange(24000.).reshape(400, 60)
c = numpy.arange(60)
d = numpy.arange(400)
"""

eindot_benchmarks = [
    Benchmark(cmd, setup, name=cmd)
    for cmd in ("numpy.einsum('ij,jk', a, b)",
                "numpy.sum(numpy.dot(a, b))",
                "numpy.einsum('i,ij,j', d, b, c)",
                "numpy.dot(d, numpy.dot(b, c))")]

setup = """\
import numpy
a = numpy.arange(4800.).reshape(6, 8, 100)
b = numpy.arange(1920.).reshape(8, 6, 40)
"""

tensordor_benchmarks = [
    Benchmark(cmd, setup, name=cmd)
    for cmd in ("numpy.einsum('ijk,jil->kl', a, b)",
                "numpy.tensordot(a, b, axes=([1,0], [0,1]))")]
