#emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
from vbench.benchmark import Benchmark
from datetime import datetime

from numpy_vb_common import TYPES1

common_setup = """\
from numpy_vb_common import *
"""
setup = common_setup

vb_indexing = []
vb_indexing_separate = []
for l in ['indexes', 'indexes_rand']:
    for dim in ('', ':,'):
        for op in ['', '=1']:
            act = "a[%s%s]%s" % (dim, l, op)
            name = act

            vb_indexing.append(
                Benchmark('for a in squares.itervalues(): %s' % (act,), setup, name=name))

            for t in TYPES1:
                vb_indexing_separate.append(
                    Benchmark(act, setup + "\na = squares[%r]" % t,
                              name='%s_%s' % (name, t)))

_vb_names = [x.name for x in vb_indexing_separate]
del x                                         # so it doesn't leak
assert(len(_vb_names) == len(set(_vb_names)))   # all are unique
#print '\n'.join(_vb_names)
