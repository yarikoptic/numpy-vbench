#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
from datetime import datetime

from numpy_vb_common import TYPES1

common_setup = """
from numpy_vb_common import *

"""
#----------------------------------------------------------------------
# mappers
setup = common_setup + """
"""



vb_add_reduce = []
vb_add_reduce_separate = []
for a in [0, 1]:
    name = "numpy.add.reduce(axis=%d)" % (a,)
    vb_add_reduce.append(
        Benchmark('[numpy.add.reduce(squares[t], axis=%d) for t in TYPES1]' % (a,),
            setup, name=name))

    for t in TYPES1:
        vb_add_reduce_separate.append(
            Benchmark('numpy.add.reduce(array, axis=%d)' % a,
                      setup + "\narray = squares[%r]" % t,
                      name='%s_%s' % (name, t)))
