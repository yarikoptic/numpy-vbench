#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
from datetime import datetime

from numpy_vb_common import TYPES1

common_setup = """\
from numpy_vb_common import *
"""
#----------------------------------------------------------------------
# mappers
setup = common_setup

vb_add_reduce = []
vb_add_reduce_separate = []
for a in [0, 1]:
    name = "numpy.add.reduce(axis=%d)" % (a,)
    vb_add_reduce.append(
        Benchmark('[numpy.add.reduce(a, axis=%d) for a in squares.itervalues()]' % (a,),
            setup, name=name))

    for t in TYPES1:
        vb_add_reduce_separate.append(
            Benchmark('numpy.add.reduce(a, axis=%d)' % a,
                      setup + "\na = squares[%r]" % t,
                      name='%s_%s' % (name, t)))

vb_any_slow = Benchmark('d.any()', 'd = np.zeros(100000, np.bool)',
                        name='numpy.any_slow')
vb_any_fast = Benchmark('d.any()', 'd = np.ones(100000, np.bool)',
                        name='numpy.any_fast')
vb_all_slow = Benchmark('d.all()', 'd = np.ones(100000, np.bool)',
                        name='numpy.all_slow')
vb_all_fast = Benchmark('d.all()', 'd = np.zeros(100000, np.bool)',
                        name='numpy.all_fast')
