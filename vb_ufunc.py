#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
import numpy

from vbench.benchmark import Benchmark
from datetime import datetime

from numpy_vb_common import TYPES1, squares_

common_setup = """\
from numpy_vb_common import *
"""

ufuncs = [x for x in dir(numpy) if isinstance(getattr(numpy, x), numpy.ufunc)]
vb_ufunc = []
vb_ufunc_separate = []

for ufunc in ufuncs:
    f = getattr(numpy, ufunc)
    cmd = 'numpy.%s(%s)' % (ufunc, ','.join(['a']*f.nin))

    # figure out compatible types
    safe_types = []
    for t,a in squares_.iteritems():
        try:
            eval(cmd, dict(numpy=numpy, a=a))
            safe_types.append(t)
        except TypeError:
            pass

    vb_ufunc.append(
        Benchmark('[%s for t, a in squares_.iteritems() if t in types]' % (cmd,),
            common_setup + "types=%r" % safe_types, name=cmd + "_%dtypes" % len(safe_types)))

    for t in safe_types:
        vb_ufunc_separate.append(
            Benchmark(cmd,
                      common_setup + "\na = squares_[%r]" % t,
                      name='%s_%s' % (cmd, t)))

#Print [x.name for x in vb_random], vb_random_shuffle100000.name
