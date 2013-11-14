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

    """
    # Do not bother about separate for now -- too much time/space/html
    for t in safe_types:
        vb_ufunc_separate.append(
            Benchmark(cmd,
                      common_setup + "\na = squares_[%r]" % t,
                      name='%s_%s' % (cmd, t)))
    """
#Print [x.name for x in vb_random], vb_random_shuffle100000.name

# some interesting selective tests
vb_ufunc_custom = [
    Benchmark('numpy.nonzero(d)',
              common_setup + 'd = numpy.ones(20000, dtype=numpy.bool)',
              name='numpy.nonzero'),
    Benchmark('numpy.count_nonzero(d)',
              common_setup + 'd = numpy.ones(20000, dtype=numpy.bool)',
              name='numpy.count_nonzero'),
    Benchmark('~d', common_setup + 'd = numpy.ones(20000, dtype=numpy.bool)',
              name='numpy.not_bool'),
    Benchmark('d & d',
              common_setup + 'd = numpy.ones(20000, dtype=numpy.bool)',
              name='numpy.and_bool'),
    Benchmark('d | d',
              common_setup + 'd = numpy.ones(20000, dtype=numpy.bool)',
              name='numpy.or_bool')]

for type in ('numpy.float32', 'numpy.float64'):
    vb_ufunc_custom += [
        Benchmark('numpy.add(d, 1)',
                  common_setup + 'd = numpy.ones(20000, dtype=%s)' % type,
                  name='numpy.add_scalar2_' + type),
        Benchmark('numpy.divide(d, 1)',
                  common_setup + 'd = numpy.ones(20000, dtype=%s)' % type,
                  name='numpy.divide_scalar2_' + type),
        Benchmark('numpy.divide(d, 1, out=d)',
                  common_setup + 'd = numpy.ones(20000, dtype=%s)' % type,
                  name='numpy.divide_scalar2_inplace_' + type),
        Benchmark('d < 1',
                  common_setup + 'd = numpy.ones(20000, dtype=%s)' % type,
                  name='numpy.less_than_scalar2_' + type)]

vb_ufunc_scalar = [
    Benchmark('x+x',
              common_setup + 'x = numpy.asarray(1.0)',
              name='numpy.add_scalar'),
    Benchmark('x+1.',
              common_setup + 'x = numpy.asarray(1.0)',
              name='numpy.add_scalar_conv'),
    Benchmark('x+y',
              common_setup + 'x = numpy.asarray(1.0+1j); y = complex(1., 1.)',
              name='numpy.add_scalar_conv_complex'),
    ]

vb_broadcast = Benchmark('d - e',
                         common_setup + """\
d = numpy.ones((50000, 100), dtype=numpy.float64)
e = numpy.ones((100,), dtype=numpy.float64)
""",
                         name='numpy.broadcast')

